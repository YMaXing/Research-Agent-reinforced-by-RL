## Context of the Article

### What We Are Planning to Share

- A comprehensive 2025 research update surveying the post-DeepSeek-R1 landscape of inference-time compute scaling techniques for enhancing LLM reasoning capabilities.
- Clear introduction of the four core categories of reasoning model development (inference-time compute scaling, pure reinforcement learning, RL plus supervised fine-tuning, and supervised fine-tuning with distillation) and detailed explanation of how training compute and inference compute interact and overlap in practical systems.
- Summaries of 14 recent papers that illustrate diverse methods for regulating and scaling test-time computation, ranging from simple token-based controls and budget forcing, through search and optimization loops, to dynamic depth and latent-space strategies.
- Concrete mechanisms, empirical observations, limitations, and benchmark correlations drawn directly from each paper, while maintaining a strictly theoretical lens with zero implementation code or deployment instructions.
- Visual Mermaid diagrams that distill category relationships, process flows, performance plots, and architectural mechanisms so the reader can grasp trade-offs at a glance.

### Why We Think It's Valuable

- AI Engineers must track inference-time scaling advances to make informed decisions on balancing model size, training costs, latency, and accuracy when building agentic systems. These methods enable smaller models to rival much larger ones on complex reasoning tasks, directly impacting production trade-offs in cost, speed, and capability.

### Expected Length of the Article

**4,690 words**

### Theory / Practice Ratio

100% theory - 0% practice

## Article Outline

1. Introduction
2. Implementing and improving reasoning in LLMs: The four main categories
3. Inference-time compute scaling methods
4. s1: Simple test-time scaling
5. Other noteworthy research papers on inference-time compute scaling
6. Test-Time Preference Optimization
7. Thoughts Are All Over the Place
8. Trading Inference-Time Compute for Adversarial Robustness
9. Chain-of-Associated-Thoughts
10. Step Back to Leap Forward
11. Scaling up Test-Time Compute with Latent Reasoning
12. Can a 1B LLM Surpass a 405B LLM?
13. Learning to Reason from Feedback at Test-Time
14. Inference-Time Computations for LLM Reasoning and Planning
15. Inner Thinking Transformer
16. Test Time Scaling for Code Generation
17. Chain of Draft
18. Better Feedback and Edit Models
19. Conclusion

## Section 1 - Introduction

- We open by establishing why stronger LLM reasoning is a top priority in 2025: complex user tasks in agentic systems require reliable multi-step problem solving that direct-answer models routinely fail.
- We describe the recent research surge that blends inference-time scaling, pure RL, RL plus SFT hybrids, and SFT with distillation, noting the rapid pace of publications since DeepSeek-R1.
- We explicitly state the article’s narrow focus on post-DeepSeek-R1 inference-time compute scaling papers.
- Insert a graph with the following online URL syntax:
![The four main categories of implementing reasoning models I explained in Understanding Reasoning LLMs. This article focuses on inference-time-scaling methods.](https://substackcdn.com/image/fetch/$s_!IOSP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9e2677-652a-4af1-9f57-dc0c253d2198_1448x1260.png)
- Transition to Section 2: We now examine each of the four categories in detail so the reader can understand how inference-time scaling fits inside the broader landscape.

- **Section length:** 130 words

## Section 2 - Implementing and improving reasoning in LLMs: The four main categories

- We define reasoning models as those that generate explicit or internal intermediate thought processes before producing a final answer, contrasting them sharply with direct-answer LLMs that map input to output in a single forward pass.
- Insert a graph with the following online URL syntax:
![Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.](https://substackcdn.com/image/fetch/$s_!ZsN9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbfe39-f656-4845-b376-18c1e563210a_1326x564.png)
- We contrast increasing training compute (modifying weights via RL or SFT) versus increasing inference compute (extra FLOPs at test time without weight changes), using the reader’s existing knowledge of chain-of-thought prompting as the simplest inference example.
- We explain that most practical systems combine heavy train-time preparation with test-time thinking to achieve best results, because training alone can produce reward hacking while pure inference scaling on weak base models yields limited gains.
- Insert a graph with the following online URL syntax:
![Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling.](https://substackcdn.com/image/fetch/$s_!pgyl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png)
- We break down the four categories in sequence, explaining each category with a paragraph: (1) Inference-time compute scaling, including its core idea, its application in LLMs like o1 and what was reported in the DeepSeek R1 paper: explicit inference-time methods were largely unsuccessful, yet note its own implicit inference scaling through training that produces longer responses, which directly raises inference costs. (2) Pure reinforcement learning, including its challenges (3) Reinforcement learning and supervised fine-tuning and (4) Supervised fine-tuning and model distillation - stress how if differs from traditional distillation. Insert a graph with the following online URL syntax in an appropriate place:
![Four categories of reasoning models development](https://substackcdn.com/image/fetch/$s_!_2dU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e5fdf9-e72c-497b-9cf4-b4e3c24f33f1_1600x591.png)
- Transition to Section 3: With the four categories now mapped, we zoom in on the inference-time compute scaling branch that forms the core of this article.

- **Section length:** 870 words

## Section 3 - Inference-time compute scaling methods

- We articulate the core idea that extra inference compute lets models “think longer,” directly analogous to humans spending more time on hard problems.
- We review classic prompt engineering approaches such as chain-of-thought and their direct impact on token count, latency, and monetary cost.
- Insert a graph with the following online URL syntax:
![An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!Knds!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d37faa4-3261-492c-85a4-766926b8c17c_1600x419.png)
- We cover search and voting strategies, specifically majority voting and beam search guided by process reward models, showing how these parallel or sequential methods allocate additional compute.
- Insert a graph with the following online URL syntax:
![Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!O9a-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ad9742b-993f-4ecd-8f80-2fa41d43164b_1334x798.png)
- Transition to Section 4: We now examine a concrete recent instantiation of these ideas in the s1 paper, which combines curated traces with explicit length-control tokens.

- **Section length:** 200 words

## Section 4 - s1: Simple test-time scaling

- We describe the hybrid approach in [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393) (31 Jan, 2025) that uses a carefully curated 1k-example SFT dataset of reasoning traces together with inference-time length control, distinguishing it from pure distillation.
- We detail the mechanism of “wait” tokens that encourage self-verification and self-correction, contrasting them with simple end-of-thinking delimiters.
- We explain budget forcing as a sequential scaling technique and contrast it with parallel methods such as majority voting, showing how the former directly controls output length.
- We report the observed correlation between generated response length and accuracy on reasoning benchmarks, citing the paper’s empirical curves.
- We surface the paper’s stated limitations and its call for future comparisons against beam search, lookahead search, compute-optimal search, and basic CoT baselines.
- We connect the technique to DeepSeek-R1’s “Aha moment” and present the paper’s empirical comparison of “Wait” versus “Hmm” tokens on downstream accuracy.
- Insert the following graphs with the following online URL syntax in the appropriate places:
![Illustration of "wait" token insertion to control the length of the output. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!qk_K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e7f4d94-9f8f-4353-87ad-78f3cba7b9cd_1154x854.png)
![Correlation between response accuracy and length. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!kYWF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f0c49b-a644-4142-bed0-7d114ecd39c2_798x456.png)
!["Wait" vs "Hmm" tokens. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!Qd4X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdfe7db-8c97-4240-8be0-11efa7abdf7c_758x510.png)
- Transition to Section 5: No transition needed.

- **Section length:** 450 words

## Section 5 - Other noteworthy research papers on inference-time compute scaling

- We explain our rationale for keeping individual summaries brief given the high volume of recent papers, allowing the reader to see the breadth without exhaustive repetition.
- We highlight the common pattern that many papers blend some training with explicit control of inference-time compute rather than treating scaling as purely prompt-based.
- We differentiate these regulated approaches from distillation or SFT approaches that merely produce longer outputs without active length regulation or compute budgeting during inference.
- Transition to Section 6: No transition needed.

- **Section length:** 150 words

## Section 6 - Test-Time Preference Optimization

- We describe the iterative on-the-fly alignment process in "Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback" (https://arxiv.org/abs/2501.12895) that avoids changing underlying model weights, positioning it as a pure inference-time method.
- We detail the use of a reward model to select chosen and rejected responses, followed by generation of textual critiques and suggestions that guide refinement.
- We walk through the four-step loop—generation, scoring, critique, and refinement—that repeats to progressively improve outputs on a per-query basis.
- Insert a graph with the following online URL syntax:
![Test-Time Preference Optimization process. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!dmJN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a1bd16-7cf7-4898-8dce-a2d8352f76a8_1600x819.png)
- Transition to Section 7: No transition needed.

- **Section length:** 150 words

## Section 7 - Thoughts Are All Over the Place

- We define the underthinking phenomenon in o1-like models as in "Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs"(https://arxiv.org/abs/2501.18585) where frequent reasoning path switches reduce final accuracy.
- We present the Thought Switching Penalty (TIP) method that modifies logits at inference time to discourage premature path transitions without any fine-tuning.
- We report how this no-fine-tuning approach improves accuracy on challenging benchmarks by forcing deeper exploration of promising reasoning paths.
- Insert a graph with the following online URL syntax:
![Thought Switching Penalty method visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!vvCX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7111ccaa-c4c1-4c7c-84f9-74d38df3c663_1528x894.png)
- Transition to Section 8: No transition needed.

- **Section length:** 120 words

## Section 8 - Trading Inference-Time Compute for Adversarial Robustness

- We show how increased inference-time compute, as in "Trading Inference-Time Compute for Adversarial Robustness"(https://arxiv.org/abs/2501.18841), generally reduces successful attack rates even without adversarial training, citing the paper’s empirical trade-off curves.
- We highlight important exceptions where gains are limited, especially in policy ambiguity or loophole exploitation scenarios.
- We describe new attack strategies introduced in the paper—Think Less and Nerd Sniping—that can counteract robustness gains from scaling.
- We conclude that inference scaling helps but is not a complete standalone solution for LLM safety.
- Insert a graph with the following online URL syntax:
![Trading Inference-Time Compute for Adversarial Robustness analysis. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!Gt2_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F704acd82-10a8-4879-9bd3-26bb67c3155f_1600x1173.png)
- Transition to Section 9: No transition needed.
- **Section length:** 150 words

## Section 9 - Chain-of-Associated-Thoughts

- We describe the combination of Monte Carlo Tree Search with an associative memory in "CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning"(https://arxiv.org/abs/2502.02390) that acts as a dynamic knowledge base during inference.
- We explain the benefit of associative memory for recalling earlier reasoning paths and incorporating newly generated information without losing context.
- We detail how the overall framework aids systematic exploration of reasoning pathways at test time.
- Insert a graph with the following online URL syntax:
![CoAT: Chain-of-Associated-Thoughts Framework visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!AtpC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0635fb-c0b4-45df-b8d3-b54254ab92b5_1600x777.png)

- Transition to Section 10: No transition needed.
- **Section length:** 100 words

## Section 10 - Step Back to Leap Forward

- We present the self-backtracking mechanism in "Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models"(https://arxiv.org/abs/2502.0440) that teaches models when and where to revise suboptimal paths using a learned backtrack token.
- We contrast the training phase that uses the special backtrack token with the key inference-time contribution of tree-based search that leverages the learned ability.
- We emphasize the advantage of not requiring external reward models, unlike standard process-reward-guided search.
- Insert a graph with the following online URL syntax:
![Step Back to Leap Forward: Self-Backtracking mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!e6x3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1df5fbf3-97f2-4976-b46f-2d5196b6bdc4_1594x888.png)

- We describe how the model can dynamically adjust search depth and breadth using its acquired backtracking skill.
- Transition to Section 11: No transition needed.
- **Section length:** 180 words

## Section 11 - Scaling up Test-Time Compute with Latent Reasoning

- We explain the recurrent depth approach in "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"(https://arxiv.org/abs/2502.05171) that iterates in latent space rather than producing additional output tokens.
- We describe the hidden-state-like behavior similar to RNNs that refines reasoning without increasing visible output length.
- We discuss the major drawback: the absence of explicit reasoning steps that aid human interpretability and debugging.
- Insert a graph with the following online URL syntax:
![Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!kVPW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb82da925-5736-44ba-bed1-ea3207b06382_1516x602.png)

- Transition to Section 12: No transition needed.
- **Section length:** 120 words

## Section 12 - Can a 1B LLM Surpass a 405B LLM?

- We summarize the systematic study of interactions in "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"(https://arxiv.org/abs/2502.06703) between inference-time scaling, process reward models, and problem difficulty.
- We detail the compute-optimal scaling strategy that adapts the inference budget according to PRM choice, policy model size, and task complexity.
- We report the evidence that a 1B model with proper scaling can outperform an unscaled 405B Llama 3 on the same benchmarks.
- We draw the broader implication that the right inference budget lets small models surpass much larger unscaled models, directly informing engineer trade-off decisions.
- Insert a graph with the following online URL syntax:
![Can 1B LLM Surpass 405B LLM? Compute-optimal scaling comparison. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!DiM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c471e7f-36e7-41a8-a7e0-80bebf3c0f36_1600x1046.png)
- Transition to Section 13: No transition needed.
- **Section length:** 160 words

## Section 13 - Learning to Reason from Feedback at Test-Time

- We acknowledge the challenge of classifying the method in "Learning to Reason from Feedback at Test-Time"(https://www.arxiv.org/abs/2502.12521) as pure inference-time or training-time because it updates model weights during inference.
- We describe the OpTune optimizer that adjusts model weights based on previous mistakes without storing failed attempts in the prompt context.
- We contrast this weight-update approach with sequential revision (adding attempts to the prompt) and parallel sampling approaches.
- We highlight the benefit of remembering errors via lightweight weight updates rather than growing context length indefinitely.
- Insert a graph with the following online URL syntax:
![Learning to Reason from Feedback at Test-Time: OpTune optimizer visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!nJMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1925302-7fc2-4c7b-91e9-1c0fc4f0609e_1426x652.png)
- Transition to Section 14: No transition needed.
- **Section length:** 180 words

## Section 14 - Inference-Time Computations for LLM Reasoning and Planning

- We present the benchmark in "Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights"(https://www.arxiv.org/abs/2502.12521) that evaluates CoT, Tree-of-Thought, Reasoning as Planning, and additional techniques across eleven diverse tasks.
- We list the task categories covered: arithmetic, logical, commonsense, algorithmic reasoning, and planning domains.
- We extract the key insight that no single inference-time technique dominates across all task types, forcing engineers to match methods to domains.
- We summarize the analysis of computational cost versus performance trade-offs provided in the paper.
- Insert a graph with the following online URL syntax:
![Inference-Time Computations for LLM Reasoning and Planning benchmark results. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!Vm7j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42115dab-1086-4035-9a64-65a83631377e_1600x1023.png)

- Transition to Section 15: No transition needed.

- **Section length:** 120 words

## Section 15 - Inner Thinking Transformer

- We introduce dynamic depth scaling in "Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking"(https://arxiv.org/abs/2502.13842) that avoids using a fixed transformer layer count for every token.
- We detail Adaptive Token Routing, which sends difficult tokens through the same layer multiple times, selectively increasing the inference compute budget for harder tokens.
- We explain how this mechanism allocates extra thinking effort exactly where it is needed without lengthening the output sequence.
- Insert a graph with the following online URL syntax:
![Inner Thinking Transformer: Adaptive Token Routing mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!-oC7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6eb47e-fcbe-4c71-8d45-e7d82ae14ba1_1414x1090.png)
- Transition to Section 16: No transition needed.
- **Section length:** 120 words

## Section 16 - Test Time Scaling for Code Generation

- We describe the S* method in " S\*: Test Time Scaling for Code Generation"(https://arxiv.org/abs/2502.14382) specialized for code that combines parallel generation of candidate solutions with sequential iterative debugging.
- Insert a graph with the following online URL syntax:
![S*: Test Time Scaling for Code Generation overview. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!quMS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94a88f17-b4b1-4642-aeb1-6db29071ef91_972x752.png)
- We break down the two-stage process: first, generation with execution feedback on public test cases; second, adaptive selection and repair of candidates.
- We explain the use of execution results and errors to iteratively repair solutions and the technique of adaptive input synthesis that creates discriminating test cases to distinguish between passing solutions.
- We connect the approach to earlier Google research on optimal test-time compute scaling.
- Transition to Section 17: No transition needed.
- **Section length:** 440 words

## Section 17 - Chain of Draft

- We report the observation that humans often use concise drafts rather than verbose step-by-step explanations when solving problems internally.
- We present Chain of Draft prompting in "Chain of Draft: Thinking Faster by Writing Less"(https://arxiv.org/abs/2502.18600) that generates minimal yet informative intermediate steps instead of full natural-language reasoning.
- Insert a graph with the following online URL syntax:
![Chain of Draft: Thinking Faster by Writing Less comparison. Annotated figures from the paper](https://substackcdn.com/image/fetch/$s_!Gaj6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869a967-9498-435f-85f2-a38557db14e3_1460x982.png)
- We quantify the efficiency gains from drastically reduced token count while retaining accuracy comparable to full chain-of-thought on reasoning benchmarks.
- We discuss the trade-off: loss of human-readable reasoning traces versus faster generation and lower cost, helping engineers decide when interpretability can be sacrificed.
- Transition to Section 18: No transition needed.
- **Section length:** 200 words

## Section 18 - Better Feedback and Edit Models

- We outline the challenge of applying inference scaling to open-ended tasks that lack verifiable answers such as creative writing or high-level planning.
- We describe a specialized architecture in "Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks"(https://arxiv.org/abs/2503.04378) that decouples a generator model, a feedback model, and an edit model, each optimized for its role.
- We explain how the feedback and edit models are trained on large human-annotated datasets of responses, critiques, and revisions to produce higher-quality signals than a single model could.
- We show how the dedicated models enable iterative refinement during inference that surpasses generic self-critique loops.
- Insert a graph with the following online URL syntax:
![Dedicated Feedback and Edit Models for Inference-Time Scaling system architecture](https://substackcdn.com/image/fetch/$s_!zA8v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73568387-83fb-4744-bd3d-f5cbcfe53f1d_1136x716.png)
- Transition to Section 19: No transition needed.engineering practice.

- **Section length:** 150 words

## Section 19 - Conclusion

- We position inference-time compute scaling as a major 2025 research direction precisely because it avoids permanent weight modification and can be applied to existing models.
- We recap the range of techniques surveyed, from simple wait tokens and budget forcing through sophisticated search, optimization loops, dynamic routing, and latent-space iteration.
- We reiterate the recurring finding that small models with proper inference-time scaling can rival or exceed much larger models that lack such scaling.
- We surface important caveats: increased inference costs, latency impact on user experience, and the absence of any universally best technique across all tasks.
- We describe the emerging industry trend toward “thinking-on-demand” toggles that let developers or users dial inference compute up or down depending on task difficulty.
- We predict that explicit reasoning will become the default rather than an optional feature in future agentic systems.
- We tease the upcoming article that will cover train-time compute scaling methods including advanced reinforcement learning, hybrid RL plus SFT, and distillation approaches in depth.
- Insert a graph with the following online URL syntax in the appropriate place:
[](https://substackcdn.com/image/fetch/$s_!nhEn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f749e4-4167-4013-b1c9-651c83bf8d3b_1504x756.png)
- **Section length:** 700 words

## Golden Sources

<!-- [Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) -->
"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters.md"

<!-- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) -->
"DeepSeek-R1 _ Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.md"

<!-- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) -->
"Large Language Models are Zero-Shot Reasoners.md"

## Other Sources

<!-- [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393) -->
"s1 _  Simple test-time scaling.md"

<!-- [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585) -->
"Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs.md"

<!-- [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895) -->
"Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback.md"

<!-- [Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841) -->
"TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS.md"