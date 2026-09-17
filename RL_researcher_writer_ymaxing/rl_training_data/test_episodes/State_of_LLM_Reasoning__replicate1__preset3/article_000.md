# What's New in Test-Time Scaling?

In 2025, building agentic systems that can reliably solve complex, multi-step problems is a top priority for AI engineers. The direct-answer models that served us well in simpler applications often fail at these tasks, making stronger reasoning capabilities a critical need.

Since the release of models like DeepSeek-R1, we've seen a surge in research exploring how to enhance LLM reasoning. This new wave of innovation blends several techniques: inference-time compute scaling, pure reinforcement learning (RL), hybrids of RL and supervised fine-tuning (SFT), and SFT with model distillation. The pace is rapid, with new papers appearing almost weekly.

This article provides a comprehensive survey of the latest advancements in one of these key areas: inference-time compute scaling. We will focus on noteworthy papers published since the DeepSeek-R1 release, breaking down the diverse methods being explored to make models "think longer" and more effectively at runtime.![The four main categories of implementing reasoning models I explained in Understanding Reasoning LLMs. This article focuses on inference-time-scaling methods.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9e2677-652a-4af1-9f57-dc0c253d2198_1448x1260.png)

Image 1: The four main categories of implementing reasoning models. This article focuses on inference-time-scaling methods. (Source: [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

To give you a clear map of this evolving landscape, we will first examine each of the four main categories of reasoning model development. This will help you understand how inference-time scaling fits into the bigger picture before we dive into the specific techniques.

## Implementing and improving reasoning in LLMs: The four main categories

Reasoning models are a specialized class of LLMs designed to tackle complex problems by generating a series of intermediate steps—either explicitly shown to the user or processed internally—before arriving at a final answer. This is a significant departure from standard, direct-answer LLMs, which perform a single forward pass to map an input directly to an output.

This distinction is crucial. A direct-answer model might give you a simple, one-line response, whereas a reasoning model will show its work, breaking down the problem into a logical sequence. This "thinking" process, whether visible or not, is what allows these models to handle tasks that require multi-step logic, like solving math proofs or complex coding challenges.![Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbfe39-f656-4845-b376-18c1e563210a_1326x564.png)

Image 2: Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response. (Source: [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

To build these reasoning capabilities, researchers and engineers primarily focus on two types of computational scaling: increasing **training compute** or increasing **inference compute**. Increasing training compute involves modifying the model's weights, typically through reinforcement learning or supervised fine-tuning on vast datasets. This process is expensive and time-consuming but fundamentally alters the model's internal knowledge and behavior.

On the other hand, increasing inference compute involves allocating additional FLOPs at test time to improve the quality of the output without changing the model's weights. The simplest and most well-known example of this is chain-of-thought (CoT) prompting, where adding a phrase like "Let's think step by step" encourages the model to generate a more detailed reasoning process, thereby using more computational resources during inference [[1]](https://arxiv.org/abs/2205.11916).

In practice, the most effective systems often blend both approaches. Relying solely on training-time compute can lead to issues like reward hacking, where the model learns to exploit the reward function without genuinely improving its reasoning. Conversely, applying pure inference-time scaling to a weak base model often yields limited gains. The sweet spot is a powerful base model, refined through extensive training, that is also capable of leveraging additional compute at inference time to "think" more deeply about a problem.![Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png)

Image 3: Accuracy improvements can be achieved through increased training or test-time compute. (Source: [S\*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382))

The development of reasoning models generally falls into four main categories. Understanding these categories is essential for navigating the current landscape of AI research and making informed decisions when building your own systems [[2]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).![Four categories of reasoning models development](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e5fdf9-e72c-497b-9cf4-b4e3c24f33f1_1600x591.png)

Image 4: The four main categories of reasoning model development. (Source: [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

**1. Inference-time compute scaling.** This is the category we will focus on in this article. It involves techniques that increase computational resources during inference to improve output quality, without altering the model's weights. Models like OpenAI's o1 are rumored to heavily leverage this approach, which would explain their higher cost and latency compared to other models. The DeepSeek-R1 paper reported that their attempts to use explicit inference-time methods like Process Reward Model-based and Monte Carlo Tree Search-based approaches were largely unsuccessful. However, the model does exhibit an *implicit* form of inference scaling by generating longer, more detailed responses, which naturally increases inference costs [[3]](https://arxiv.org/abs/2501.12948).

**2. Pure reinforcement learning (RL).** This approach, demonstrated by DeepSeek-R1-Zero, shows that reasoning capabilities can emerge from pure RL without any initial supervised fine-tuning. The model is trained using rewards based on the accuracy of its final answers, and over time, it learns to generate intermediate reasoning steps to improve its performance. While this is a fascinating research direction, it presents practical challenges, such as the need for reliable, automated verifiers to provide reward signals and the risk of the model developing "unnatural" or uninterpretable reasoning patterns.

**3. Reinforcement learning and supervised fine-tuning (SFT + RL).** This is a hybrid approach and the most common method for building high-performance reasoning models today. It typically involves an initial SFT stage to teach the model a baseline reasoning format, followed by RL to further refine its capabilities. DeepSeek-R1 is a prime example of this method, building upon the pure RL-trained DeepSeek-R1-Zero with additional SFT and RL stages to enhance both its reasoning performance and its alignment with human-readable formats [[3]](https://arxiv.org/abs/2501.12948).

**4. Supervised fine-tuning (SFT) and model distillation.** This approach involves training a smaller, more efficient model on the outputs of a larger, more powerful "teacher" model. This is different from traditional knowledge distillation, where the student model is trained on the teacher's logits. Here, the student is simply fine-tuned on the high-quality reasoning traces generated by the teacher. The DeepSeek-R1-Distill models, for example, were created by fine-tuning smaller models like Llama and Qwen on data generated by the 671B-parameter DeepSeek-R1. This is a cost-effective way to create capable reasoning models, but it is fundamentally limited by the performance of the teacher model and does not drive new innovations in reasoning [[2]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

With these four categories mapped out, we can now zoom in on the first one—inference-time compute scaling—which forms the core of this article.

## Inference-time compute scaling methods

The core idea behind inference-time compute scaling is simple: allowing a model to "think longer" about a problem often leads to a better answer, much like how humans benefit from spending more time on difficult tasks. This concept is not new; it extends a long-standing principle in machine learning, where ensemble methods have historically been used to improve performance by combining multiple models at test time, albeit at a higher computational cost [[35]](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling). In the context of LLMs, "thinking longer" translates to using more computational resources during the inference phase.

The most classic example is **chain-of-thought (CoT) prompting**, where adding a phrase like "Let's think step by step" encourages intermediate reasoning. This increases the generated token count, which raises latency and monetary cost. While effective for complex problems, this approach is not a free lunch; it makes inference more expensive [[1]](https://arxiv.org/abs/2205.11916), [[4]](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more).![An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d37faa4-3261-492c-85a4-766926b8c17c_1600x419.png)

Image 5: An example of classic CoT prompting [[1]](https://arxiv.org/abs/2205.11916).

Beyond simple prompting, more sophisticated **search and voting strategies** offer another way to scale inference compute. A straightforward approach is **majority voting**, where you have the LLM generate multiple answers to the same question and then select the most frequent one as the final response. This parallel approach can improve robustness, but it can also be computationally expensive.

More advanced techniques like **beam search** and **lookahead search** use a **process reward model (PRM)** to guide the generation process more intelligently. A PRM evaluates the correctness of each *intermediate step* in a reasoning chain, rather than just the final answer. This allows a search algorithm to explore different reasoning paths, pruning the ones that are likely incorrect and expanding on the more promising ones. These methods represent a more sequential approach to scaling inference compute, where each step builds upon the last [[5]](https://arxiv.org/abs/2408.03314).![Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ad9742b-993f-4ecd-8f80-2fa41d43164b_1334x798.png)

Image 6: Different search-based methods rely on a process-reward model to select the best answer [[5]](https://arxiv.org/abs/2408.03314).

We will now examine a concrete recent instantiation of these ideas in the `s1` paper, which combines curated reasoning traces with explicit length-control tokens to manage the inference budget.

## s1: Simple test-time scaling

The paper "[s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393)" (31 Jan, 2025) presents a hybrid approach that combines a small, carefully curated SFT dataset with a simple yet effective inference-time technique for controlling compute. Instead of relying on complex reinforcement learning or massive datasets, the authors demonstrate that fine-tuning a model on just 1,000 high-quality reasoning traces is sufficient to unlock significant reasoning capabilities. This distinguishes their method from pure distillation, as it combines a training-time component (the curated dataset) with an inference-time control mechanism [[6]](https://huggingface.co/papers/2501.19393).

The core of their inference-time technique is **budget forcing**, a method for controlling the length of the model's reasoning process. This is achieved in two ways:
1.  **Forcing termination:** If the model's thinking process exceeds a desired token limit, an end-of-thinking token is appended to force the model to generate its final answer.
2.  **Encouraging continuation:** If the model attempts to stop thinking too early, the end-of-thinking token is suppressed. Instead, a special **"Wait" token** is appended to the prompt, encouraging the model to continue its reasoning, double-check its work, and potentially self-correct any errors.

This "Wait" token is more than just a pause; it seems to induce a state of doubt or reflection in the model. The paper's empirical results show that using "Wait" leads to better performance than neutral phrases like "Hmm" or no extrapolation at all. This suggests that the token actively triggers a self-verification mechanism, a behavior also observed in the "Aha moment" of DeepSeek-R1, where the model learned to use similar reflective language during its RL training [[3]](https://arxiv.org/abs/2501.12948), [[7]](https://ai.gopubby.com/i-wrote-thinking-gpt-4-months-ago-now-stanford-researchers-prove-it-right-beating-deepseek-r1-13a65d7f705a?sk=5d7cf4a72f59e530958698ffcb8631f9).

Budget forcing is a sequential scaling technique, as it directly manipulates the length of a single reasoning trace. This contrasts with parallel methods like majority voting, which generate multiple independent traces. The paper reports a clear correlation between the length of the generated response and its accuracy on reasoning benchmarks, with performance generally improving as more thinking tokens are used, up to a certain point.![Illustration of "wait" token insertion to control the length of the output. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e7f4d94-9f8f-4353-87ad-78f3cba7b9cd_1154x854.png)

Image 7: Illustration of "wait" token insertion to control the length of the output [[6]](https://huggingface.co/papers/2501.19393).

However, the authors also acknowledge the limitations of this approach. The performance gains from budget forcing eventually flatten out, and the technique is constrained by the model's context window. Further research has revealed other critical failure modes. One significant issue is **inverse scaling**, where providing more reasoning steps can actually decrease accuracy by reinforcing bad reasoning patterns or distracting the model with irrelevant information. Budget forcing can also lead to repetition or instability where the model gets stuck in a loop. The technique's effectiveness also appears to be model-dependent, with some studies showing it rarely helps and often hurts performance for Llama and Mistral model families [[36]](https://www.turingpost.com/p/testtimescaling2).![Correlation between response accuracy and length. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f0c49b-a644-4142-bed0-7d114ecd39c2_798x456.png)

Image 8: Correlation between response accuracy and length [[6]](https://huggingface.co/papers/2501.19393).!["Wait" vs "Hmm" tokens. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdfe7db-8c97-4240-8be0-11efa7abdf7c_758x510.png)

Image 9: "Wait" vs "Hmm" tokens [[6]](https://huggingface.co/papers/2501.19393).

## Other noteworthy research papers on inference-time compute scaling

The release of models like o1 and DeepSeek-R1 has ignited a flurry of research into inference-time compute scaling. Given the high volume of recent papers, we will keep our summaries of each one brief, focusing on the core mechanism and key takeaways. This will allow you to get a broad overview of the landscape without getting bogged down in repetitive details.

A common pattern you will notice is that many of these papers blend some form of training with explicit control of inference-time compute. This is an important distinction. These are not purely prompt-based techniques; they often involve fine-tuning a model to respond to specific control mechanisms or to perform certain actions, like self-correction, at inference time.

This also differentiates them from simple distillation or SFT approaches that just happen to produce longer outputs. The methods we will discuss involve active regulation of the compute budget or reasoning process during inference, rather than just passively generating more tokens as a byproduct of training.

## Test-Time Preference Optimization

The paper "[Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895)" introduces an iterative alignment process that operates purely at inference time, without updating the model's underlying weights. This makes it a true test-time scaling technique [[8]](https://proceedings.mlr.press/v267/li25ac.html).

The method uses a reward model to score multiple generated responses to a single query. The highest-scoring response is labeled "chosen," and the lowest-scoring one is "rejected." The LLM is then prompted to generate a textual critique, explaining the strengths of the chosen response and the weaknesses of the rejected one. This critique, along with specific suggestions for improvement, is then used to guide the model in generating a new, refined set of responses.

This four-step loop—**generation, scoring, critique, and refinement**—is repeated for a set number of iterations, progressively improving the quality of the output for that specific query. It is a clever way to perform on-the-fly preference optimization without the need for costly retraining [[9]](https://icml.cc/virtual/2025/poster/46149).![Test-Time Preference Optimization process. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a1bd16-7cf7-4898-8dce-a2d8352f76a8_1600x819.png)

Image 10: The Test-Time Preference Optimization process [[8]](https://proceedings.mlr.press/v267/li25ac.html).

## Thoughts Are All Over the Place

The paper "[Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585)" identifies a phenomenon called **underthinking**, where models like o1 frequently switch between different reasoning paths without fully exploring any single one. This premature abandonment of promising lines of thought often leads to incorrect answers and reduced performance on complex problems [[10]](https://tldr.takara.ai/p/2501.18585).

To address this, the authors propose a decoding strategy called **Thought Switching Penalty (TIP)**. This technique modifies the model's logits at inference time, applying a penalty to tokens associated with thought transitions (e.g., "alternatively," "on the other hand"). By discouraging these premature switches, TIP forces the model to explore each reasoning path more thoroughly before moving on. This approach improves accuracy on challenging benchmarks without requiring any fine-tuning, making it a lightweight and effective inference-time intervention [[11]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme).![Thought Switching Penalty method visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7111ccaa-c4c1-4c7c-84f9-74d38df3c663_1528x894.png)

Image 11: The Thought Switching Penalty mechanism [[10]](https://tldr.takara.ai/p/2501.18585).

## Trading Inference-Time Compute for Adversarial Robustness

The paper "[Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841)" explores the relationship between inference-time compute and a model's resilience to adversarial attacks. The authors find that, in many cases, simply giving a model more time to "think" (i.e., increasing its inference-time compute) can significantly reduce the success rate of various attacks, even without any specific adversarial training [[12]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness), [[13]](https://huggingface.co/papers/2501.18841).

However, the paper also highlights important exceptions. When a policy is ambiguous or contains loopholes, an attacker can often find ways to exploit them, and in these scenarios, increased compute does not necessarily improve robustness. The authors also introduce two novel attack strategies aimed specifically at reasoning models:
-   **Think Less:** An attack that tries to fool the model into using less compute than it should.
-   **Nerd Sniping:** An attack that traps the model in unproductive thinking loops, wasting its compute budget.

The key takeaway is that while scaling inference-time compute is a promising direction for improving LLM safety, it is not a standalone solution and must be combined with other robustness measures [[12]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness), [[14]](https://arxiv.org/html/2507.15974v1).![Trading Inference-Time Compute for Adversarial Robustness analysis. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F704acd82-10a8-4879-9bd3-26bb67c3155f_1600x1173.png)

Image 12: An illustration of the trade-off between inference-time compute and attack success probability [[12]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness).

## Chain-of-Associated-Thoughts

The "[CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/abs/2502.02390)" paper proposes a framework that combines **Monte Carlo Tree Search (MCTS)** with a dynamic **associative memory**. This memory acts as a knowledge base that is updated in real-time during the inference process, allowing the model to recall earlier reasoning steps and incorporate new information without losing context [[15]](https://arxiv.org/html/2502.02390v3).

The MCTS algorithm systematically explores different reasoning pathways, while the associative memory helps the model maintain a coherent and evolving understanding of the problem. This synergy between structured search and adaptive learning allows the model to tackle complex, multi-hop reasoning tasks more effectively at test time [[15]](https://arxiv.org/html/2502.02390v3).![CoAT: Chain-of-Associated-Thoughts Framework visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0635fb-c0b4-45df-b8d3-b54254ab92b5_1600x777.png)

Image 13: The Chain-of-Associated-Thoughts framework [[15]](https://arxiv.org/html/2502.02390v3).

## Step Back to Leap Forward

The paper "[Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/abs/2502.0440)" introduces a novel **self-backtracking** mechanism that teaches a model to recognize and correct its own suboptimal reasoning paths. This is a hybrid approach that involves both a training phase and an inference-time component [[16]](https://arxiv.org/html/2502.04404v1).

During training, the model learns to generate a special **`<backtrack>` token** when it identifies a point in its reasoning where it may have gone wrong. This teaches the model to recognize when and where a revision is needed. At inference time, the model leverages this learned skill to perform a dynamic tree-based search. When the `<backtrack>` token is generated, the model rolls back to a previous state and explores an alternative reasoning path [[17]](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947).

This allows the model to dynamically adjust the depth and breadth of its search, systematically exploring multiple reasoning trajectories without the need for an external reward model to guide the process. It is an interesting approach that empowers the model with a learned mechanism for self-correction and exploration [[16]](https://arxiv.org/html/2502.04404v1).![Step Back to Leap Forward: Self-Backtracking mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1df5fbf3-97f2-4976-b46f-2d5196b6bdc4_1594x888.png)

Image 14: The self-backtracking mechanism [[17]](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947).

## Scaling up Test-Time Compute with Latent Reasoning

The paper "[Scaling by Thinking in Continuous Space](https://arxiv.org/abs/2502.05171)" proposes a novel architecture that scales test-time compute by reasoning in a continuous **latent space** rather than by generating more output tokens. The model uses a recurrent block that iterates multiple times, refining its internal hidden state before producing an output [[18]](https://huggingface.co/papers/2502.05171), [[19]](https://openreview.net/forum?id=S3GhJooWIC).

This approach is similar to how Recurrent Neural Networks (RNNs) process information, allowing for deeper computation without increasing the length of the visible output. While this method can significantly improve performance on reasoning tasks, it comes with a major drawback: the reasoning process is entirely implicit and not represented in words, which makes it difficult for humans to interpret or debug [[18]](https://huggingface.co/papers/2502.05171), [[20]](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db).![Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb82da925-5736-44ba-bed1-ea3207b06382_1516x602.png)

Image 15: The recurrent depth approach for latent reasoning [[18]](https://huggingface.co/papers/2502.05171).

## Can a 1B LLM Surpass a 405B LLM?

The paper "[Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703)" conducts a systematic study of the interactions between inference-time scaling, process reward models (PRMs), and problem difficulty. The authors propose a **compute-optimal scaling strategy** that adaptively allocates the inference budget based on the specific policy model, PRM, and the complexity of the task at hand.

Their key finding is that with the right scaling strategy, a much smaller model can outperform a significantly larger one. For example, they show that a 1B parameter model with compute-optimal scaling can surpass the performance of an unscaled 405B Llama 3 model on the same benchmarks.

This has important implications for AI engineers, as it demonstrates that simply using a larger model is not always the best solution. Instead, intelligently allocating inference-time compute can allow for the use of smaller, more efficient models without sacrificing performance, directly impacting the trade-off between cost, latency, and capability.![Can 1B LLM Surpass 405B LLM? Compute-optimal scaling comparison. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c471e7f-36e7-41a8-a7e0-80bebf3c0f36_1600x1046.png)

Image 16: Compute-optimal scaling allows a 3B model to outperform a 405B model [[21]](https://arxiv.org/abs/2502.06703).

## Learning to Reason from Feedback at Test-Time

The paper "[Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)" introduces a method that blurs the line between pure inference-time and training-time techniques, as it involves updating the model's weights during inference. The authors propose an optimizer called **OpTune** that adjusts the model's weights based on mistakes made on previous, similar problems [[22]](https://www.arxiv.org/abs/2502.12521).

This is different from sequential revision, which adds failed attempts to the prompt context, and parallel sampling, which generates multiple independent attempts. Instead of growing the context window indefinitely, OpTune allows the model to "remember" its errors through lightweight weight updates. This approach offers a way to learn from mistakes at test-time without the overhead of storing long histories in the prompt.

While this is not a pure inference-time scaling method in the strictest sense, it's a noteworthy approach that combines elements of both training and inference to achieve on-the-fly adaptation and improvement [[22]](https://www.arxiv.org/abs/2502.12521).![Learning to Reason from Feedback at Test-Time: OpTune optimizer visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1925302-7fc2-4c7b-91e9-1c0fc4f0609e_1426x652.png)

Image 17: The OpTune optimizer updates model weights at test time based on feedback [[22]](https://www.arxiv.org/abs/2502.12521).

## Inference-Time Computations for LLM Reasoning and Planning

The paper "[Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)" introduces **Sys2Bench**, a comprehensive benchmark for evaluating various inference-time techniques across a wide range of tasks. The benchmark covers five categories: arithmetic, logical, commonsense, and algorithmic reasoning, as well as planning domains [[22]](https://www.arxiv.org/abs/2502.12521), [[23]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM).

The authors use this benchmark to evaluate several popular techniques, including CoT, Tree-of-Thought, and Reasoning as Planning. Their key finding is that **no single inference-time technique consistently performs best** across all task types. This highlights the need for engineers to carefully match the right method to the specific domain and problem they are trying to solve. The paper also provides a valuable analysis of the trade-off between computational cost and performance gains for each technique, offering practical insights for building efficient and effective reasoning systems [[22]](https://www.arxiv.org/abs/2502.12521).

This domain-specificity is echoed in other specialized applications. In medical diagnosis, for example, simply increasing the thinking budget can lead to "overthinking" and performance degradation, and it cannot compensate for a model's fundamental lack of medical knowledge [[37]](https://neurips.cc/virtual/2025/124931). Similarly, in robotics, inference-time techniques are adapted to ground plans in physical reality, often by combining LLMs with classical planners or affordance functions to ensure that generated actions are feasible and safe [[38]](https://arxiv.org/html/2510.10787v1).![Inference-Time Computations for LLM Reasoning and Planning benchmark results. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42115dab-1086-4035-9a64-65a83631377e_1600x1023.png)

Image 18: Results from the Sys2Bench benchmark, showing that no single method dominates across all tasks [[22]](https://www.arxiv.org/abs/2502.12521).

## Inner Thinking Transformer

The "[Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/abs/2502.13842)" paper proposes an architecture that uses **dynamic depth scaling** instead of a fixed number of transformer layers for every token. The key mechanism is **Adaptive Token Routing (ATR)**, which identifies "difficult" tokens that require more complex reasoning and sends them through the same layer multiple times [[24]](https://arxiv.org/pdf/2502.13842), [[25]](https://arxiv.org/html/2502.13842v1).

This approach selectively increases the inference compute budget for the specific tokens that need it most, allowing the model to "think deeper" about critical parts of the input without lengthening the overall output sequence. It's an efficient way to allocate extra computational effort exactly where it is needed, balancing performance and resource consumption. To ensure training stability across these deep, recursive computations, the architecture uses techniques like residual connections and step encoding to manage gradient propagation, although complex tokens can still trigger abrupt gradient spikes [[24]](https://arxiv.org/pdf/2502.13842), [[26]](https://www.emergentmind.com/topics/inner-thinking-transformer-itt), [[39]](https://aclanthology.org/2025.acl-long.1369.pdf).![Inner Thinking Transformer: Adaptive Token Routing mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6eb47e-fcbe-4c71-8d45-e7d82ae14ba1_1414x1090.png)

Image 19: The Adaptive Token Routing mechanism in the Inner Thinking Transformer [[25]](https://arxiv.org/html/2502.13842v1).

## Test Time Scaling for Code Generation

The paper "[S\*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)" introduces **S\***, a hybrid test-time scaling framework specifically designed for code generation. This method combines the strengths of both parallel and sequential scaling to improve the coverage and accuracy of generated code.![S*: Test Time Scaling for Code Generation overview. Annotated figure from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94a88f17-b4b1-4642-aeb1-6db29071ef91_972x752.png)

Image 20: An overview of the S\* framework for code generation [[27]](https://arxiv.org/abs/2502.14382).

The S\* framework operates in a two-stage process:

1.  **Generation:** The model first generates multiple candidate solutions in parallel. Each of these solutions is then sequentially refined through a process of **iterative debugging**. The code is executed against public test cases, and the resulting outputs and error messages are fed back to the model to guide the repair process. This continues until a solution passes all public tests or a maximum number of revisions is reached.
2.  **Selection and Repair:** After generating a set of refined candidates, the framework uses a novel technique called **adaptive input synthesis** to select the best one. Instead of relying on a pre-trained reward model, an LLM is prompted to generate new, discriminating test cases specifically designed to tell the difference between the remaining candidate solutions. The candidates are executed against these new test cases, and the one that performs best is chosen as the final answer.

This approach is particularly interesting because it leverages the unique properties of the code domain—namely, the ability to get precise feedback from execution—to create a robust, self-correcting system. It also connects back to earlier research from Google on compute-optimal test-time scaling, showing how these ideas can be adapted and specialized for different domains.

## Chain of Draft

The paper "[Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/abs/2502.18600)" is based on a simple but powerful observation: when humans solve problems, they often jot down concise notes or "drafts" rather than writing out verbose, step-by-step explanations. Inspired by this, the authors propose **Chain of Draft (CoD) prompting**, a technique that encourages LLMs to generate minimal yet informative intermediate steps [[28]](https://www.helicone.ai/blog/chain-of-draft), [[29]](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169).

Instead of producing full natural-language reasoning, the model is prompted to output only the essential calculations or logical transformations needed to move to the next step. This approach drastically reduces the number of tokens generated, leading to significant gains in efficiency and lower latency, while maintaining an accuracy comparable to that of full chain-of-thought on many reasoning benchmarks [[30]](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft), [[31]](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock).

This presents an interesting trade-off for engineers: while you lose the human-readable reasoning traces that are useful for debugging and interpretability, you gain a much faster and cheaper system. This makes CoD a valuable technique for applications where efficiency is paramount and full transparency of the reasoning process can be sacrificed [[32]](https://arxiv.org/html/2502.18600v1).![Chain of Draft: Thinking Faster by Writing Less comparison. Annotated figures from the paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869a967-9498-435f-85f2-a38557db14e3_1460x982.png)

Image 21: A comparison of Chain of Draft with standard and Chain of Thought prompting [[32]](https://arxiv.org/html/2502.18600v1).

## Better Feedback and Edit Models

One of the major challenges in applying inference-time scaling is that many of the most effective techniques rely on having a verifiable, ground-truth answer to provide a reward signal. This works well for domains like math and coding, but it is much harder for open-ended tasks like creative writing or high-level strategic planning.

The paper "[Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378)" addresses this challenge by proposing a specialized, multi-model architecture. Instead of a single model performing all tasks, their system decouples the process into three distinct roles [[33]](https://arxiv.org/html/2503.04378v1), [[34]](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended):
1.  A **generator model** that produces an initial response.
2.  A **feedback model** that provides a detailed critique of the response.
3.  An **edit model** that revises the initial response based on the feedback.

Each of these models is trained on large, human-annotated datasets specifically designed for its role. This specialization allows the feedback and edit models to produce much higher-quality signals than a single, general-purpose model attempting a generic self-critique loop. By enabling this iterative refinement process at inference time, the system can significantly improve performance on open-ended tasks where automated verifiers are not available [[33]](https://arxiv.org/html/2503.04378v1).![Dedicated Feedback and Edit Models for Inference-Time Scaling system architecture](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73568387-83fb-4744-bd3d-f5cbcfe53f1d_1136x716.png)

Image 22: The system architecture with dedicated feedback and edit models [[33]](https://arxiv.org/html/2503.04378v1).

## Chain-of-Layers: Dynamic Depth Adaptation

Another approach to adaptive computation is **Chain-of-Layers (CoLa)**, which adjusts a model's depth and layer composition for each input at test time. Instead of using a fixed architecture, CoLa treats a pretrained model's layers as modular building blocks that can be rearranged, skipped, or repeated [[40]](https://arxiv.org/abs/2507.07996).

To find the best layer configuration for a given input, the method uses Monte Carlo Tree Search (MCTS). The search algorithm explores different "paths" through the model's layers, rewarding sequences that produce correct answers while penalizing those that use too many layers. This allows the model to use fewer layers for simple tasks and "think deeper" by reusing layers for more difficult problems. The technique demonstrates that dynamically adapting model architecture at inference time can unlock performance gains without any retraining [[36]](https://www.turingpost.com/p/testtimescaling2).

## Test-Time Diffusion Deep Researcher

Google's **Test-Time Diffusion Deep Researcher (TTD-DR)** framework applies inference-time scaling to the task of generating long-form research reports. It treats report generation as an iterative refinement process, similar to how a human researcher might work: draft, search, revise, and repeat [[41]](https://arxiv.org/abs/2507.16075).

The process begins with an LLM agent creating a research plan and a rough initial draft. Then, in a loop, the agent generates search queries based on what's missing in the draft, retrieves new information, and uses it to "denoise" and improve the report. This cycle of "search, update, refine" happens entirely at test time. The system also features a self-evolution component that independently optimizes each part of the workflow (planning, questioning, writing), making the entire process more robust and effective [[36]](https://www.turingpost.com/p/testtimescaling2).

## Quantum-Inspired Monte Carlo Scaling

A novel approach adapts particle-based Monte Carlo methods to inference-time scaling, showing significant improvements on challenging mathematical reasoning tasks. This method, called Particle Filtering (PF), was reported to have a 4–16x better scaling rate than deterministic search methods [[42]](https://arxiv.org/html/2502.01618v2).

The research demonstrated that a 1.5B parameter model (Qwen2.5-Math-1.5B-Instruct) using this technique could surpass the accuracy of GPT-4o, and a 7B model could match the performance of o1-preview on the MATH500 benchmark. This work connects the rich literature on probabilistic inference with LLM scaling, opening up new directions for developing more robust and efficient algorithms for test-time computation [[42]](https://arxiv.org/html/2502.01618v2).

## Conclusion

Inference-time compute scaling is shaping up to be a major research direction in 2025, and for good reason. Unlike training-time methods that require permanent and costly weight modifications, inference-time techniques can often be applied to existing models, offering a more flexible way to enhance their capabilities.

In this article, we have surveyed a wide range of these techniques, from simple "wait" tokens and budget forcing to sophisticated search algorithms, optimization loops, dynamic routing, and even iteration in latent space. A recurring theme across many of these papers is a powerful and encouraging finding: a smaller model with a well-designed inference-time scaling strategy can often rival or even exceed the performance of a much larger model that lacks such scaling. This has profound implications for engineering practice, as it directly impacts the trade-offs between model size, training costs, inference latency, and overall accuracy.

However, it is also important to acknowledge the caveats. All of these methods come with an increased cost at inference time, which can affect user experience due to higher latency. Furthermore, as we have seen, there is no universally best technique that dominates across all tasks. The optimal approach often depends on the specific domain, the complexity of the problem, and the capabilities of the base model.

We are already beginning to see this reality reflected in the industry, with the emergence of "thinking-on-demand" toggles in APIs that allow developers or even end-users to dial the amount of inference compute up or down depending on the difficulty of the task. This move toward more explicit and controllable reasoning is a trend we expect to continue. In the future, we predict that explicit reasoning will become the default mode of operation for agentic systems, rather than an optional feature.![Scaling up the number of initial responses and effective feedback can significantly improve performance.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f749e4-4167-4013-b1c9-651c83bf8d3b_1504x756.png)

Image 23: Scaling up the number of initial responses and effective feedback can significantly improve performance [[33]](https://arxiv.org/html/2503.04378v1).

While this article has focused on inference-time scaling, it is only one piece of the puzzle. In an upcoming article, we will dive into the other side of the equation: train-time compute scaling. We will explore advanced reinforcement learning techniques, hybrid RL and SFT approaches, and distillation methods in depth, providing a complete picture of the state of the art in building powerful reasoning models.

## References

- [1] [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- [2] [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [3] [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [4] [Token Economics of Chain-of-Thought: When Thinking Costs More Than It's Worth](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more)
- [5] [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [6] [s1: Simple test-time scaling](https://huggingface.co/papers/2501.19393)
- [7] [I Wrote “Thinking GPT” 4 Months Ago. Now Stanford Researchers Prove It Right, Beating DeepSeek R1.](https://ai.gopubby.com/i-wrote-thinking-gpt-4-months-ago-now-stanford-researchers-prove-it-right-beating-deepseek-r1-13a65d7f705a?sk=5d7cf4a72f59e530958698ffcb8631f9)
- [8] [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://proceedings.mlr.press/v267/li25ac.html)
- [9] [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://icml.cc/virtual/2025/poster/46149)
- [10] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://tldr.takara.ai/p/2501.18585)
- [11] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme)
- [12] [Trading Inference-Time Compute for Adversarial Robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)
- [13] [Trading Inference-Time Compute for Adversarial Robustness](https://huggingface.co/papers/2501.18841)
- [14] [Follow-up Paper on Trading Inference-Time Compute](https://arxiv.org/html/2507.15974v1)
- [15] [CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/html/2502.02390v3)
- [16] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/html/2502.04404v1)
- [17] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947)
- [18] [Scaling by Thinking in Continuous Space](https://huggingface.co/papers/2502.05171)
- [19] [Scaling by Thinking in Continuous Space](https://openreview.net/forum?id=S3GhJooWIC)
- [20] [Scaling Test-Time Compute: How Recurrent Depth Transforms AI Reasoning](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db)
- [21] [Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703)
- [22] [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)
- [23] [Sys2Bench: A Benchmark for Inference-Time Computation in LLMs](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [24] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/pdf/2502.13842)
- [25] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/html/2502.13842v1)
- [26] [Inner Thinking Transformer (ITT)](https://www.emergentmind.com/topics/inner-thinking-transformer-itt)
- [27] [S\*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)
- [28] [Chain of Draft](https://www.helicone.ai/blog/chain-of-draft)
- [29] [What Is Chain of Drafts? Bye Bye Chain of Thoughts](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169)
- [30] [Chain of Draft](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft)
- [31] [Move Beyond Chain-of-Thought with Chain-of-Draft on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock)
- [32] [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/html/2502.18600v1)
- [33] [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/html/2503.04378v1)
- [34] [HelpSteer3: Human-Annotated Feedback and Edit Data to Empower Inference-Time Scaling in Open-Ended General-Domain Tasks](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended)
- [35] [Categories of Inference-Time Scaling](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling)
- [36] [What's New in Test-Time Scaling?](https://www.turingpost.com/p/testtimescaling2)
- [37] [Test-Time Scaling for Medical Reasoning](https://neurips.cc/virtual/2025/124931)
- [38] [LLM Inference-Time Scaling in Robotics](https://arxiv.org/html/2510.10787v1)
- [39] [Inner Thinking Transformer Paper](https://aclanthology.org/2025.acl-long.1369.pdf)
- [40] [Chain-of-Layers: A Test-time-adaptive-depth Method for LLMs](https://arxiv.org/abs/2507.07996)
- [41] [Test-Time Diffusion Deep Researcher](https://arxiv.org/abs/2507.16075)
- [42] [Inference-Time Scaling with Probabilistic Inference](https://arxiv.org/html/2502.01618v2)