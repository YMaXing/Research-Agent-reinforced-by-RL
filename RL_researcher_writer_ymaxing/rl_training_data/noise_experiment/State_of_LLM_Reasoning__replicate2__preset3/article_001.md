# What’s New in Test-Time Scaling?

In 2025, building agentic systems that can reliably solve complex, multi-step problems is a top priority for AI engineers. Direct-answer LLMs often fail at these tasks, requiring more sophisticated reasoning capabilities. This need has sparked a surge of research into how we can make LLMs "think" more effectively.

Since the release of DeepSeek-R1, the field has seen a rapid evolution of techniques that blend inference-time scaling, pure reinforcement learning (RL), RL-SFT hybrids, and supervised fine-tuning (SFT) with distillation. This article focuses on one of these key areas: the latest advancements in inference-time compute scaling, surveying the post-DeepSeek-R1 landscape. We will explore how these methods allow engineers to balance model size, training costs, latency, and accuracy, often enabling smaller models to rival much larger ones on complex reasoning tasks.![The four main categories of implementing reasoning models I explained in Understanding Reasoning LLMs. This article focuses on inference-time-scaling methods.](https://substackcdn.com/image/fetch/$s_!IOSP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9e2677-652a-4af1-9f57-dc0c253d2198_1448x1260.png)

Image 1: The four main categories of implementing reasoning models. This article focuses on inference-time-scaling methods. (Source [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]])

We will now examine each of the four categories in detail so you can understand how inference-time scaling fits inside the broader landscape.

## Implementing and improving reasoning in LLMs: The four main categories

Reasoning models are LLMs that generate intermediate steps, either explicitly in their output or internally, before arriving at a final answer. This is a significant departure from standard LLMs, which typically map an input directly to an output in a single forward pass. For simple questions, a direct answer is enough. But for complex problems requiring multiple steps, showing the reasoning process often leads to more accurate results.![Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.](https://substackcdn.com/image/fetch/$s_!ZsN9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbfe39-f656-4845-b376-18c1e563210a_1326x564.png)

Image 2: Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response. (Source [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]])

There are two primary ways to enhance an LLM's reasoning capabilities: increasing training compute or increasing inference compute. Training compute involves modifying the model's weights through techniques like reinforcement learning or supervised fine-tuning. This is a one-time, upfront investment. Inference compute, on the other hand, involves allocating additional FLOPs at test time to improve output quality without altering the model's weights. The simplest example of this is chain-of-thought (CoT) prompting, where adding a phrase like "Let's think step by step" encourages the model to generate a more detailed reasoning process, thereby using more computational resources during inference [[2]](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more), [[3]](https://aclanthology.org/2025.emnlp-main.165.pdf), [[4]](https://www.aussieai.com/research/cot-optimization), [[5]](https://arxiv.org/html/2406.09136v1), [[6]](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought).![Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling.](https://substackcdn.com/image/fetch/$s_!pgyl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png)

Image 3: Accuracy improvements can be achieved through increased training or test-time compute. (Source [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382) [[7]])

In practice, most state-of-the-art systems combine both approaches. Relying solely on training can lead to issues like reward hacking, where the model learns to exploit the reward function without genuinely improving its reasoning. Conversely, pure inference scaling on a weak base model often yields limited gains. The most effective reasoning models, therefore, are typically built through a heavy train-time preparation phase, followed by further thinking at test time.

The development of reasoning models can be broken down into four main categories, as outlined by Sebastian Raschka [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).![Four categories of reasoning models development](https://substackcdn.com/image/fetch/$s_!_2dU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e5fdf9-e72c-497b-9cf4-b4e3c24f33f1_1600x591.png)

Image 4: The four main categories for developing reasoning models. (Source [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]])

**1. Inference-time compute scaling** improves a model's reasoning capabilities without altering its underlying weights. This is achieved by increasing the computational resources used during inference. Models like OpenAI's o1 are rumored to leverage this technique, which helps explain their higher cost compared to models like GPT-4o. The DeepSeek R1 technical report noted that their explicit attempts at inference-time scaling, such as using Process Reward Model-based and Monte Carlo Tree Search-based approaches, were largely unsuccessful. However, the model implicitly scales inference compute by generating longer, more detailed responses, which naturally increases inference costs compared to its base V3 model [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

**2. Pure reinforcement learning (RL)** is an approach where reasoning emerges as a learned behavior without an initial supervised fine-tuning stage. DeepSeek-R1-Zero is a prime example of this method. The model was trained using RL with accuracy and format rewards, and surprisingly, it began to generate reasoning traces on its own. This confirmed that it is possible to develop a reasoning model using pure RL. While this approach is interesting from a research perspective, it generally leads to weaker models compared to methods that combine RL with SFT [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

**3. Reinforcement learning and supervised fine-tuning (SFT + RL)** is the most common approach for building high-performance reasoning models. This method typically involves an SFT stage before RL, as seen in the standard RLHF pipeline. DeepSeek-R1, for instance, was developed using this approach, building upon DeepSeek-R1-Zero with additional SFT and RL stages to enhance its reasoning performance. The SFT data often contains more CoT examples, and the RL stage may use verifiable rewards in addition to human preference-based rewards. OpenAI's o1 was also likely developed using a similar method [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

**4. Supervised fine-tuning and model distillation (SFT + Distillation)** is a cost-effective alternative for creating smaller, more efficient reasoning models. In this context, distillation differs from the traditional approach where a smaller "student" model is trained on the output probabilities (logits) of a larger "teacher" model. Instead, it refers to instruction fine-tuning a smaller LLM on a dataset of high-quality reasoning traces generated by a larger, more capable model. The DeepSeek team used this approach to create their R1-distilled models, which, despite being significantly smaller, achieve surprisingly strong performance. However, this method is limited by its dependence on an existing, stronger model to generate the SFT data [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

With these four categories mapped out, we can now zoom in on the branch that forms the core of this article: inference-time compute scaling.

## Inference-time compute scaling methods

The core idea behind inference-time compute scaling is to allow a model to "think longer" on a problem, much like a human would when faced with a complex task. This is achieved by allocating additional computational resources during the inference phase to improve the quality of the output.

The most classic example of this is CoT prompting. By simply adding a phrase like "Let's think step by step," the model is encouraged to generate intermediate reasoning steps before providing a final answer. This process naturally increases the number of tokens generated, which in turn increases latency and cost, but often leads to more accurate results on complex problems [[2]](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more), [[3]](https://aclanthology.org/2025.emnlp-main.165.pdf), [[4]](https://www.aussieai.com/research/cot-optimization), [[5]](https://arxiv.org/html/2406.09136v1), [[6]](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought).![An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!Knds!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d37faa4-3261-492c-85a4-766926b8c17c_1600x419.png)

Image 5: An example of classic CoT prompting. (Source [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) [[8]])

Beyond simple prompting, more advanced strategies involve search and voting mechanisms. One common approach is majority voting, where the LLM generates multiple answers, and the most frequent one is selected. Similarly, beam search and other search algorithms can be used to explore different reasoning paths and select the best response, often guided by a process reward model (PRM). These PRMs evaluate each step of the reasoning process, providing a more granular signal than simply judging the final outcome [[9]](https://openreview.net/forum?id=l19DmXbwPK), [[10]](https://icml.cc/virtual/2025/oral/47195), [[11]](https://arxiv.org/html/2512.15146v1), [[12]](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf), [[13]](https://cameronrwolfe.substack.com/p/reward-models).![Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!O9a-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ad9742b-993f-4ecd-8f80-2fa41d43164b_1334x798.png)

Image 6: Different search-based methods that use a process-reward model to select the best answer. (Source [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) [[14]])

We will now examine a concrete recent instantiation of these ideas in the s1 paper, which combines curated traces with explicit length-control tokens.

## s1: Simple test-time scaling

The paper "[s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393)" (31 Jan, 2025) presents a hybrid approach that combines a small, curated SFT dataset with an inference-time length control mechanism. This method stands out for its simplicity and sample efficiency, demonstrating that strong reasoning and test-time scaling can be achieved without the complexity of large-scale reinforcement learning.

The core of the s1 approach is a dataset of just 1,000 carefully selected question-and-answer pairs with reasoning traces, called s1K. These examples were curated based on three criteria: difficulty, diversity, and quality. An off-the-shelf model, Qwen2.5-32B-Instruct, was then fine-tuned on this small dataset.![Illustration of "wait" token insertion to control the length of the output. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!qk_K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e7f4d94-9f8f-4353-87ad-78f3cba7b9cd_1154x854.png)

Image 7: The "wait" token encourages the model to continue its reasoning process. (Source [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) [[15]])

To control the amount of test-time compute, the authors introduced a technique called **budget forcing**. This sequential scaling method works in two ways:

1.  **Forcing termination:** If the model's thinking process exceeds a desired token limit, an end-of-thinking token is appended to force the model to generate its final answer.
2.  **Lengthening the process:** If more thinking time is desired, the end-of-thinking token is suppressed. Instead, a "Wait" token is appended to the reasoning trace. This encourages the model to pause, re-evaluate its current reasoning, and potentially self-correct any errors [[16]](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8). This mechanism is similar to the "Aha moment" observed in DeepSeek-R1, where the model learned to use reflective language to improve its reasoning.

The paper provides empirical evidence showing a correlation between the length of the generated response and the model's accuracy on reasoning benchmarks. Longer reasoning traces, encouraged by budget forcing, often lead to better performance.![Correlation between response accuracy and length. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!kYWF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f0c49b-a644-4142-bed0-7d114ecd39c2_798x456.png)

Image 8: The correlation between response length and accuracy. (Source [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) [[15]])

Interestingly, the choice of token matters. The paper found that using "Wait" was more effective at inducing self-correction than a more neutral phrase like "Hmm," suggesting that the "Wait" token specifically triggers a sense of doubt and reconsideration in the model [[17]](https://huggingface.co/papers/2501.19393).!["Wait" vs "Hmm" tokens. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!Qd4X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdfe7db-8c97-4240-8be0-11efa7abdf7c_758x510.png)

Image 9: A comparison of "Wait" vs. "Hmm" tokens on accuracy. (Source [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) [[15]])

The paper acknowledges its limitations, noting that the performance gains from budget forcing eventually flatten out and are constrained by the model's context window. The authors call for future work to compare this technique against other sequential and parallel methods like beam search, lookahead search, and compute-optimal search. Subsequent research has also highlighted practical failure modes: the technique can cause repetition, is ineffective for certain model families like Llama and Mistral, and struggles with abstract tasks where reasoning paths are less defined [[18]](https://iclr-blogposts.github.io/2026/blog/2026/wait-do-we-need-to-wait), [[19]](https://aclanthology.org/2025.emnlp-main.1025.pdf). Despite these constraints, the simplicity of the s1 approach makes it a valuable contribution.

## Other noteworthy research papers on inference-time compute scaling

The rapid pace of research in inference-time compute scaling has produced a wide array of techniques, each with its own trade-offs. Given the sheer volume of recent papers, we will provide brief summaries of several noteworthy approaches. This will allow you to get a broad overview of the landscape without getting bogged down in repetitive details.

A common pattern you will notice is that many of these papers blend some form of training with explicit control over inference-time compute. This is a departure from purely prompt-based methods, as it involves preparing the model to better utilize additional computation at test time. For example, methods like Chain-of-Layers (CoLa) and MindJourney show how architectural adaptations at test-time can unlock new capabilities [[20]](https://www.turingpost.com/p/testtimescaling2).

It is also important to distinguish these regulated approaches from SFT or distillation methods that simply train a model to produce longer outputs. The key difference is the active management of compute. The techniques we will discuss are not just about generating more tokens; they are about strategically allocating computational resources during inference to enhance reasoning.

## Test-Time Preference Optimization

"[Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895)" introduces an iterative alignment process that operates entirely at inference time, without modifying the model's weights. This makes it a pure inference-time method.

The technique, called Test-time Preference Optimization (TPO), uses a reward model to score multiple generated responses to a single query. The best and worst responses are then used to generate textual critiques and suggestions for improvement. This feedback is then fed back to the model to refine its next generation [[21]](https://icml.cc/virtual/2025/poster/46149), [[22]](https://proceedings.mlr.press/v267/li25ac.html).

This process is a four-step loop:

1.  **Generate:** The model produces multiple answers.
2.  **Score:** A reward model picks the best and worst ones.
3.  **Critique:** The model reflects on the strengths and weaknesses of the selected responses.
4.  **Refine:** Based on the critique, the model rewrites a better version.

Repeating this loop just a few times has been shown to significantly improve the model's alignment with human preferences.![Test-Time Preference Optimization process. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!dmJN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a1bd16-7cf7-4898-8dce-a2d8352f76a8_1600x819.png)

Image 10: The four-step loop of Test-Time Preference Optimization. (Source [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895) [[22]])

## Thoughts Are All Over the Place

The paper "[Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585)" identifies a phenomenon called "underthinking" in o1-like models. This occurs when a model frequently switches between different reasoning paths without sufficiently exploring any single one, which can lead to a decrease in final accuracy, especially on challenging problems [[23]](https://tldr.takara.ai/p/2501.18585).

To address this, the authors propose a decoding strategy called **Thought Switching Penalty (TIP)**. This method modifies the model's logits at inference time to discourage premature transitions between thoughts. By applying penalties to tokens associated with thought switching, the model is encouraged to explore each reasoning path more thoroughly before moving on to another [[24]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme).![Thought Switching Penalty method visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!vvCX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7111ccaa-c4c1-4c7c-84f9-74d38df3c663_1528x894.png)

Image 11: The Thought Switching Penalty discourages premature transitions between thoughts. (Source [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585) [[23]])

This no-fine-tuning approach has been shown to improve accuracy on difficult benchmarks by forcing the model to engage in deeper, more focused reasoning.

## Trading Inference-Time Compute for Adversarial Robustness

The paper "[Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841)" explores the relationship between inference-time compute and a model's resilience to adversarial attacks [[25]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness), [[26]](https://huggingface.co/papers/2501.18841). The authors found that, in many cases, increasing the amount of "thinking time" for o1-like models significantly reduces the success rate of various attacks, even without any specific adversarial training.

However, the paper also highlights important exceptions. When a policy is ambiguous or an attacker can exploit a loophole, the benefits of increased compute are limited [[25]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness). The research also introduced two new attack strategies designed to counteract the gains from scaling:

*   **Think Less:** An attack that tricks the model into reducing its computational effort, making it more vulnerable.
*   **Nerd Sniping:** An attack that causes the model to get stuck in unproductive thinking loops, wasting its computational budget.![Trading Inference-Time Compute for Adversarial Robustness analysis. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!Gt2_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F704acd82-10a8-4879-9bd3-26bb67c3155f_1600x1173.png)

Image 12: Increased inference-time compute can improve robustness, but it has its limits. (Source [Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841) [[27]])

The paper concludes that while inference scaling is a powerful tool for improving robustness, it is not a complete solution on its own and must be part of a broader safety strategy [[28]](https://arxiv.org/html/2507.15974v1).

## Chain-of-Associated-Thoughts

The paper "[CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/abs/2502.02390)" introduces a framework that combines Monte Carlo Tree Search (MCTS) with an "associative memory" mechanism. This memory acts as a dynamic knowledge base during inference, allowing the model to recall earlier reasoning paths and incorporate new information without losing context.

The synergy between the structured exploration of MCTS and the adaptive learning of the associative memory helps the model to systematically explore diverse reasoning pathways at test time. This allows the framework to revisit and refine previous inferences, ensuring that the final output is both comprehensive and accurate [[29]](https://arxiv.org/html/2502.02390v3).![CoAT: Chain-of-Associated-Thoughts Framework visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!AtpC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0635fb-c0b4-45df-b8d3-b54254ab92b5_1600x777.png)

Image 13: The CoAT framework combines MCTS with an associative memory. (Source [CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/abs/2502.02390) [[29]])

## Step Back to Leap Forward

"[Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/abs/2502.0440)" introduces a self-backtracking mechanism that teaches models to recognize and revise suboptimal reasoning paths. This is achieved by training the model to generate a special backtrack token when it identifies a point where its reasoning may have gone wrong [[30]](https://arxiv.org/html/2502.04404v1).

During the training phase, the model learns when and where to perform backtracking. At inference time, it leverages this learned skill to conduct a dynamic, tree-based search. When the model generates the backtrack token, it can roll back to a previous state and explore an alternative reasoning trajectory. This allows the model to dynamically adjust its search depth and breadth, systematically exploring multiple paths to find the best solution [[31]](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947). By learning to recognize its own suboptimal states, the model can re-evaluate prior decisions and explore multiple reasoning trajectories, improving the efficiency of generating optimal paths.![Step Back to Leap Forward: Self-Backtracking mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!e6x3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1df5fbf3-97f2-4976-b46f-2d5196b6bdc4_1594x888.png)

Image 14: The self-backtracking mechanism allows the model to revise its reasoning paths. (Source [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/abs/2502.0440) [[30]])

A key advantage of this approach is that it does not require an external reward model to guide the search, unlike standard process-reward-guided methods. The model learns to self-correct, making the process more autonomous and efficient.

## Scaling up Test-Time Compute with Latent Reasoning

The paper "[Scaling by Thinking in Continuous Space](https://arxiv.org/abs/2502.05171)" presents a novel approach that scales test-time compute by iterating in a latent, continuous space rather than by generating additional output tokens [[32]](https://huggingface.co/papers/2502.05171), [[33]](https://openreview.net/forum?id=S3GhJooWIC), [[34]](https://neurips.cc/virtual/2025/poster/117966), [[35]](https://icml.cc/virtual/2025/51856). This is achieved through a recurrent depth architecture, where a recurrent block is iterated to refine the model's understanding before an output is produced [[36]](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db).

This technique allows the model to "think" more deeply without increasing the length of the visible output. The reasoning process occurs in the model's hidden states, similar to how Recurrent Neural Networks (RNNs) operate. While this method can significantly improve performance on reasoning tasks, it comes with a major drawback: the absence of explicit reasoning steps makes the process opaque, hindering human interpretability and debugging.![Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!kVPW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb82da925-5736-44ba-bed1-ea3207b06382_1516x602.png)

Image 15: The recurrent depth architecture allows for reasoning in latent space. (Source [Scaling by Thinking in Continuous Space](https://arxiv.org/abs/2502.05171) [[32]])

## Can a 1B LLM Surpass a 405B LLM?

The paper "[Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703)" conducts a systematic study of the interactions between inference-time scaling, process reward models (PRMs), and problem difficulty. The authors propose a **compute-optimal scaling strategy** that adapts the inference budget based on the specific policy model, PRM, and the complexity of the task at hand.

The key finding is that with a properly allocated inference budget, a much smaller model can outperform a significantly larger one. The paper provides empirical evidence showing that a 1B model with compute-optimal scaling can surpass the performance of an unscaled 405B Llama 3 model on the same benchmarks.![Can 1B LLM Surpass a 405B LLM? Compute-optimal scaling comparison. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!DiM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c471e7f-36e7-41a8-a7e0-80bebf3c0f36_1600x1046.png)

Image 16: A 3B model with compute-optimal TTS can outperform a 405B model on MATH-500 and AIME24. (Source [Can 1B LLM Surpass a 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703) [[37]])

This has significant implications for AI engineers, as it demonstrates that the right inference strategy can allow for the use of smaller, more efficient models without sacrificing performance. This directly informs the trade-off decisions between model size, cost, and capability in production systems, showing that simply using a larger model is not always the most effective or efficient solution.

## Learning to Reason from Feedback at Test-Time

The paper "[Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)" introduces a hybrid approach that is difficult to classify as purely inference-time or training-time, as it involves updating the model's weights during inference. The paper introduces the **OpTune optimizer**, which adjusts the model's weights based on previous mistakes without storing the failed attempts in the prompt context.

This weight-update approach is a departure from both sequential revision, where previous attempts are added to the prompt, and parallel sampling methods. The key benefit of this technique is that it allows the model to "remember" its errors through lightweight weight updates, rather than by indefinitely growing the context length. This makes the process more efficient and scalable, as it avoids the limitations of a finite context window.![Learning to Reason from Feedback at Test-Time: OpTune optimizer visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!nJMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1925302-7fc2-4c7b-91e9-1c0fc4f0609e_1426x652.png)

Image 17: The OpTune optimizer updates model weights at test time. (Source [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521) [[38]])

By learning from its mistakes on the fly, the model can continuously improve its reasoning capabilities during a single inference session, leading to more accurate and reliable outputs over time.

## Inference-Time Computations for LLM Reasoning and Planning

The paper "[Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)" introduces **Sys2Bench**, a comprehensive benchmark for evaluating various inference-time techniques across a wide range of tasks [[39]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[40]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[41]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM). The benchmark covers five categories: arithmetic, logical, commonsense, and algorithmic reasoning, as well as planning domains.

The paper evaluates several methods, including CoT, Tree-of-Thought, and Reasoning as Planning. The key insight from this extensive evaluation is that no single inference-time technique consistently performs well across all task types. This finding forces engineers to match the right method to the specific domain they are working in.![Inference-Time Computations for LLM Reasoning and Planning benchmark results. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!Vm7j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42115dab-1086-4035-9a64-65a83631377e_1600x1023.png)

Image 18: Results from the Sys2Bench benchmark show that no single method dominates across all tasks. (Source [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521) [[38]])

The paper also analyzes the cost-performance trade-offs for each technique, offering guidance for applications.

## Inner Thinking Transformer

The "[Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/abs/2502.13842)" paper introduces a dynamic depth scaling mechanism that avoids using a fixed number of transformer layers for every token [[42]](https://arxiv.org/html/2502.13842v1). Instead, it uses a technique called **Adaptive Token Routing (ATR)**, which selectively sends more difficult tokens through the same layer multiple times [[43]](https://aclanthology.org/2025.acl-long.1369.pdf), [[44]](https://arxiv.org/pdf/2502.13842), [[45]](https://www.emergentmind.com/topics/inner-thinking-transformer-itt).

This approach allows the model to dynamically increase its inference compute budget for harder tokens, allocating extra "thinking" effort exactly where it is needed. A key advantage of this method is that it enhances the model's reasoning capabilities without lengthening the output sequence. The additional processing happens internally, preserving a concise output while allowing for deeper computation on critical tokens.![Inner Thinking Transformer: Adaptive Token Routing mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!-oC7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6eb47e-fcbe-4c71-8d45-e7d82ae14ba1_1414x1090.png)

Image 19: The Adaptive Token Routing mechanism sends difficult tokens through a layer multiple times. (Source [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/abs/2502.13842) [[42]])

## Test Time Scaling for Code Generation

The paper "[S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)" proposes a hybrid method called **S\***, which is specifically designed for code generation tasks. This approach combines parallel generation of multiple candidate solutions with sequential iterative debugging.![S*: Test Time Scaling for Code Generation overview. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!quMS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94a88f17-b4b1-4642-aeb1-6db29071ef91_972x752.png)

Image 20: The S* framework combines parallel generation with sequential debugging. (Source [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382) [[7]])

The S\* framework operates in a two-stage process:

1.  **Generation:** The model first generates multiple code samples in parallel. Each sample is then executed against public test cases. The execution results, including outputs and error messages, are fed back to the model to iteratively debug and refine the code.
2.  **Selection and Repair:** After the generation stage, the framework uses a technique called **adaptive input synthesis**. This involves using an LLM to generate new, discriminating test cases that can distinguish between the candidate solutions that passed the public tests. The solutions are then executed against these new test cases, and the best-performing one is selected. This adaptive, execution-grounded approach ensures robust identification of correct solutions.

This approach is connected to earlier research from Google on compute-optimal test-time scaling, but it is tailored to the unique challenges of code generation, where execution feedback provides a powerful signal for improvement.

## Chain of Draft

The paper "[Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/abs/2502.18600)" is based on the observation that humans often rely on concise drafts or shorthand notes rather than verbose, step-by-step explanations when solving problems internally. Inspired by this, the authors propose **Chain of Draft (CoD)** prompting, a technique that encourages LLMs to generate minimal yet informative intermediate steps instead of full natural-language reasoning [[46]](https://www.helicone.ai/blog/chain-of-draft), [[47]](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft), [[48]](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169), [[49]](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock).![Chain of Draft: Thinking Faster by Writing Less comparison. Annotated figures from the paper](https://substackcdn.com/image/fetch/$s_!Gaj6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869a967-9498-435f-85f2-a38557db14e3_1460x982.png)

Image 21: A comparison of CoD and CoT, showing the significant token reduction with CoD. (Source [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/abs/2502.18600) [[50]])

This approach offers significant efficiency gains. By drastically reducing the number of tokens generated, CoD lowers both the cost and latency of inference. The paper quantifies these gains, showing that CoD can achieve accuracy comparable to full chain-of-thought on reasoning benchmarks while using significantly fewer tokens.

However, this efficiency comes at a trade-off. The loss of human-readable reasoning traces can make it more difficult to interpret and debug the model's process. This forces engineers to decide when the benefits of speed and cost outweigh the need for full transparency.

## Better Feedback and Edit Models

Most inference scaling techniques are designed for tasks with verifiable answers, like math or coding. But what about open-ended tasks such as creative writing or high-level planning? The paper "[Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378)" addresses this challenge [[51]](https://arxiv.org/html/2503.04378v1), [[52]](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended).

The authors propose a specialized architecture that decouples the generation, feedback, and editing processes into three distinct models:

1.  A **generator model** produces an initial response.
2.  A **feedback model**, trained on human-annotated critiques, provides detailed feedback on the response.
3.  An **edit model**, trained on human revisions, refines the initial response based on the feedback.![Dedicated Feedback and Edit Models for Inference-Time Scaling system architecture](https://substackcdn.com/image/fetch/$s_!zA8v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73568387-83fb-4744-bd3d-f5cbcfe53f1d_1136x716.png)

Image 22: The decoupled architecture of generator, feedback, and edit models. (Source [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378) [[51]])

By training each model on large, human-annotated datasets, the system can produce higher-quality signals than a single model performing a generic self-critique loop. This allows for effective iterative refinement during inference, even on tasks without a clear right or wrong answer.

## Conclusion

Inference-time compute scaling has firmly established itself as a major research direction in 2025. Its appeal lies in its flexibility: it can be applied to existing models without the need for permanent weight modifications, offering a powerful way to enhance reasoning capabilities on demand.

In this article, we have surveyed a wide range of techniques, from simple "wait" tokens and budget forcing to more sophisticated methods involving search, optimization loops, dynamic routing, and even latent-space iteration. A recurring theme across these papers is the remarkable finding that smaller models, when combined with the right inference-time scaling strategy, can often rival or even exceed the performance of much larger models that lack such scaling.

However, it is important to acknowledge the caveats. Increased inference compute translates directly to higher costs and latency, which can impact user experience. A significant caveat is the risk of **inverse scaling**, where allocating more compute can actually decrease accuracy. Research shows that longer reasoning can cause models to get distracted by irrelevant information, prematurely jump to familiar but incorrect solutions, or get stuck exploring chaotic, unproductive reasoning paths [[20]](https://www.turingpost.com/p/testtimescaling2). Furthermore, scaling compute cannot fix fundamental knowledge gaps in a model. In specialized domains like medicine, for example, while scaling can improve reasoning on known information, it cannot generate correct diagnoses if the underlying medical knowledge is absent from the model's weights. Studies show performance may even degrade with too much "thinking," a phenomenon sometimes called overthinking [[53]](https://neurips.cc/virtual/2025/124931). As we have seen, there is no universally best technique; the optimal approach often depends on the specific task, model, and available resources.

We are already seeing an emerging trend in the industry toward "thinking-on-demand" toggles. These features allow developers or even end-users to dial the amount of inference compute up or down depending on the difficulty of the task at hand. This level of control is a significant step forward in making powerful AI more efficient and accessible.

As we move forward, it is likely that explicit reasoning will become the default mode of operation for agentic systems, rather than an optional feature. The ability to "think" more deeply when needed will be a critical component of building truly intelligent and reliable AI.

This article has focused on the "how" of inference-time scaling. In an upcoming article, we will shift our focus to train-time compute scaling methods, including advanced reinforcement learning, hybrid RL-SFT approaches, and distillation techniques.

## References

- [1] [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [2] [Token Economics of Chain-of-Thought: When Thinking Costs More Than It's Worth](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more)
- [3] [Chain-of-Thought increases token count and latency significantly, often without improving accuracy.](https://aclanthology.org/2025.emnlp-main.165.pdf)
- [4] [Chain-of-Thought Optimization: Reducing Cost and Latency](https://www.aussieai.com/research/cot-optimization)
- [5] [Chain-of-Thought increases token count and latency significantly, often without improving accuracy.](https://arxiv.org/html/2406.09136v1)
- [6] [Tech Report: Chain-of-Thought](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought)
- [7] [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)
- [8] [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- [9] [Process Reward Models (PRMs) enhance mathematical reasoning for LLMs by leveraging increased inference-time computation.](https://openreview.net/forum?id=l19DmXbwPK)
- [10] [PRMs enhance mathematical reasoning for LLMs by leveraging increased inference-time computation.](https://icml.cc/virtual/2025/oral/47195)
- [11] [Test-time reinforcement learning uses majority voting results as pseudo-labels to improve reasoning in LLMs without annotated data.](https://arxiv.org/html/2512.15146v1)
- [12] [Let's Verify Step by Step](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf)
- [13] [Reward Models](https://cameronrwolfe.substack.com/p/reward-models)
- [14] [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [15] [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393)
- [16] [Paper Review of s1: Simple test-time scaling](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8)
- [17] [s1: Simple test-time scaling](https://huggingface.co/papers/2501.19393)
- [18] [Wait, do we need to wait?](https://iclr-blogposts.github.io/2026/blog/2026/wait-do-we-need-to-wait)
- [19] [s1: Simple Test-Time Scaling](https://aclanthology.org/2025.emnlp-main.1025.pdf)
- [20] [What's New in Test-Time Scaling?](https://www.turingpost.com/p/testtimescaling2)
- [21] [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://icml.cc/virtual/2025/poster/46149)
- [22] [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://proceedings.mlr.press/v267/li25ac.html)
- [23] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://tldr.takara.ai/p/2501.18585)
- [24] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme)
- [25] [Trading Inference-Time Compute for Adversarial Robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)
- [26] [Trading Inference-Time Compute for Adversarial Robustness](https://huggingface.co/papers/2501.18841)
- [27] [TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS.](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf)
- [28] [TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS.](https://arxiv.org/html/2507.15974v1)
- [29] [CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/html/2502.02390v3)
- [30] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/html/2502.04404v1)
- [31] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947)
- [32] [Scaling by Thinking in Continuous Space](https://huggingface.co/papers/2502.05171)
- [33] [Scaling by Thinking in Continuous Space](https://openreview.net/forum?id=S3GhJooWIC)
- [34] [Scaling by Thinking in Continuous Space](https://neurips.cc/virtual/2025/poster/117966)
- [35] [Scaling by Thinking in Continuous Space](https://icml.cc/virtual/2025/51856)
- [36] [Scaling Test-Time Compute: How Recurrent Depth Transforms AI Reasoning](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db)
- [37] [Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703)
- [38] [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)
- [39] [Sys2Bench evaluates inference-time computations for LLM reasoning across diverse tasks. It assesses multiple methods and architectures. The benchmark includes tasks like arithmetic, logical, and common sense reasoning.](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [40] [Our benchmarking evaluates inference-time computation across: Six inference-time computation methods, Eight reasoning tasks, Multiple LLM architectures (Llama, Qwen, Mistral, etc.).](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [41] [With the advancement of large language models (LLMs), solving complex reasoning tasks has gained increasing attention.](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [42] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/html/2502.13842v1)
- [43] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://aclanthology.org/2025.acl-long.1369.pdf)
- [44] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/pdf/2502.13842)
- [45] [Inner Thinking Transformer (ITT)](https://www.emergentmind.com/topics/inner-thinking-transformer-itt)
- [46] [Chain of Draft](https://www.helicone.ai/blog/chain-of-draft)
- [47] [Chain of Draft](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft)
- [48] [What is Chain of Drafts? Bye-Bye Chain of Thoughts!](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169)
- [49] [Move beyond Chain of Thought with Chain of Draft on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock)
- [50] [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/html/2502.18600v1)
- [51] [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/html/2503.04378v1)
- [52] [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended)
- [53] [Test-Time Scaling for Medical Reasoning](https://neurips.cc/virtual/2025/124931)