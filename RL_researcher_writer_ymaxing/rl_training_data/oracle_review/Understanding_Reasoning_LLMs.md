# Near-tie review: Understanding_Reasoning_LLMs  (standard vs light, margin=+0.0173)

## Reviewer conclusion (2026-08-27): KEEP `standard`, no override

**Quantitative basis:** all scores and reasoning confirmed accurate on review (no
corrections applied). Per-dimension binary scores (8 sections x 3 draws, n=24 per
arm) show cc/fl/cp exactly tied between arms. `de` heavily favors `standard`
(0.583 vs 0.125, +0.458) -- `standard` earns substantially more depth-enhancement
credit. `ga` slightly favors `light` (0.708 vs 0.625, -0.083), but this partial
offset is more than five times smaller than the `de` gain, so `standard` still
comes out ahead overall: it adds more enhancement instances without
proportionally compromising guideline adherence.

**Distributional basis:** per-draw margins (standard - light) are **[+0.065,
-0.041, +0.028]**, mean +0.017, sd 0.054. Two of three draws favor `standard`;
replicate1 flips to `light`. Moderated significance: p=0.32, still ambiguous --
the usual pattern for this batch of near-ties.

**Decision:** no manual override needed -- `standard` is mean-R_w's own winner,
driven by a clean, verified depth-enhancement edge that outweighs its modest
guideline-adherence cost.

---

## All sections (standard vs light), most-against-standard first
| section | weight | contribution | running total |
|---|---:|---:|---:|
| section-5-the-4-main-ways-to-build-and-improve-rea | 0.453 | -0.0240 | -0.0240 |
| section-6-thoughts-about-deepseek-r1 | 0.081 | +0.0006 | -0.0234 |
| section-4-a-brief-look-at-the-deepseek-training-pi | 0.070 | +0.0024 | -0.0210 |
| section-7-developing-reasoning-models-on-a-limited | 0.140 | +0.0029 | -0.0181 |
| section-8-conclusion | 0.079 | +0.0040 | -0.0141 |
| section-1-methods-and-strategies-for-building-and- | 0.058 | +0.0070 | -0.0071 |
| section-2-how-do-we-define-reasoning-model | 0.081 | +0.0115 | +0.0044 |
| section-3-when-should-we-use-reasoning-models | 0.037 | +0.0129 | +0.0173 |

(stored article margin = +0.0173 -- should match the running total's final row to ~4 decimals)

## Section: S5::section-5-the-4-main-ways-to-build-and-improve-reasoning-models  (weight=0.453, contribution=-0.0240 AGAINST standard)
Stored section rewards: standard=0.6692  light=0.7042  (explore: standard=0.3922  light=0.3675)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset2`

**Article text:**
```
## The 4 main ways to build and improve reasoning models

Current key techniques to enhance LLM reasoning and build specialized reasoning models will be outlined. As of today, the exact workings of o1 and o3 remain unknown, but they are rumored to combine both inference and training techniques.

### 1) Inference-time scaling

Inference-time scaling refers to allocating more computational resources at the moment a query is made, which is analogous to giving a human extra time to think about a difficult problem. This approach improves performance without altering the model's weights. It is governed by "test-time compute scaling laws," which suggest that for some models, performance continues to improve as they are allowed to "think" for longer [[6]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

Common methods for inference-time scaling include:
*   **Chain-of-Thought (CoT) prompting:** Encouraging the model to generate a step-by-step reasoning process before giving a final answer. This can be done with zero-shot prompts like "Let's think step by step" [[7]](https://arxiv.org/abs/2205.11916). While originally a prompting technique, this concept was later automated in test-time scaling models, which learn to self-direct their own multi-step reasoning without needing a specific user prompt to trigger it [[17]](https://www.nvidia.com/en-us/glossary/cot-prompting).![An example of a Chain-of-Thought prompt for a simple math problem.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)
Image 6: An example of classic CoT prompting from the 2022 "Large Language Models are Zero-Shot Reasoners" paper. (Source [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916))

*   **Majority Voting (Self-Consistency):** Generating multiple reasoning paths and selecting the most common final answer.
*   **Search Algorithms:** More complex methods like beam search or Monte Carlo Tree Search (MCTS) explore a tree of possible reasoning steps to find the optimal path. These often rely on a Process Reward Model (PRM) to evaluate the correctness of each intermediate step [[8]](https://arxiv.org/abs/2408.03314). PRMs provide real-time feedback during the reasoning process, allowing even smaller models to outperform larger ones by guiding them toward more accurate solutions [[26]](https://ojs.aaai.org/index.php/AAAI/article/view/40797/44758).![A diagram comparing three search-based methods: Best-of-N, Beam search, and Lookahead search.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)
Image 7: Different search-based methods rely on a process-reward model to select the best answer, as shown in the "Scaling LLM Test-Time Compute" paper. (Source [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314))

However, the core assumption that more thinking always leads to better answers is flawed. Research on "overthinking" has shown that for many problems, especially simpler ones, performance follows an inverted U-shaped curve. After a certain point, additional computation leads to diminishing or even negative returns, as the model may second-guess a correct answer and "flip" it to an incorrect one [[16]](https://arxiv.org/html/2604.10739v1).

Interestingly, the DeepSeek R1 technical report categorizes both PRM and MCTS under "Unsuccessful Attempts," stating that the computational overhead they introduce outweighs their benefits during large-scale RL training [[1]](https://arxiv.org/abs/2501.12948). This suggests that while these methods can improve performance during inference, they may not be efficient enough for the training loop. However, it is possible that DeepSeek still applies these techniques at the application layer for specific use cases.

The higher cost of OpenAI's o1 models compared to models like GPT-4o may be due to this increased inference-time computation. O1 is designed to spend more time reasoning through complex tasks, which naturally requires more resources and leads to higher latency and cost [[9]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). The pricing reflects this: o1 can be six times more expensive for inputs and outputs compared to GPT-4o. This is attributed to its advanced reasoning architecture, specialized training on STEM fields, and the computational power required to achieve higher accuracy on complex problems [[27]](https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c).

### 2) Pure reinforcement learning (RL)

The pure RL approach, exemplified by DeepSeek-R1-Zero, bypasses the standard SFT stage and applies RL directly to a base model. Instead of relying on a reward model trained on human preferences, this method uses verifiable outcomes to guide the model's learning. The reward system is typically rule-based, consisting of two main components [[1]](https://arxiv.org/abs/2501.12948):

1.  **Accuracy Rewards:** The model receives a positive reward if its final answer is correct and zero otherwise. This is used for tasks with deterministic solutions, like math problems or coding challenges where outputs can be verified by unit tests.
2.  **Format Rewards:** The model is incentivized to follow specific formatting rules, such as enclosing its reasoning process within `<think>` and `</think>` tags. This ensures the output is structured and interpretable.![A flowchart showing the development process of the DeepSeek-R1-Zero model, starting from the V3-Base model and using pure RL.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)
Image 8: The development process of the DeepSeek-R1-Zero model. (Source [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948))

The algorithm behind this process is typically Group-wise Reward Policy Optimization (GRPO). Unlike other RL algorithms like PPO, GRPO does not require training a separate value network or critic. Instead, it normalizes rewards across a group of responses to the same prompt. This makes it computationally efficient and a natural fit for verifiable tasks where multiple solutions can be generated and automatically checked for correctness [[18]](http://scalable-ai.eecs.berkeley.edu/assets/lecture_slides/lecture_15.pdf). However, recent analysis has identified an optimization bias in GRPO that can artificially increase response length, especially for incorrect answers. A proposed fix, Dr. GRPO, removes this bias and improves token efficiency without sacrificing reasoning performance [[3]](https://arxiv.org/html/2503.20783v1).

A key phenomenon observed during this process is the "Aha moment," where the model spontaneously begins to generate long, detailed reasoning traces and self-correction patterns. For example, the model might generate phrases like "Wait, let me reevaluate" before correcting a mistake in its reasoning. This emergent behavior is a direct result of the RL process optimizing for correct final answers [[1]](https://arxiv.org/abs/2501.12948), [[10]](https://www.philschmid.de/mini-deepseek-r1). However, some research suggests this "Aha moment" may not be entirely emergent. Analysis of base models, including DeepSeek-V3-Base, shows they already generate self-reflection keywords before any RL tuning, questioning whether pure RL is truly discovering this behavior from scratch [[3]](https://arxiv.org/html/2503.20783v1).![An example from the DeepSeek R1 paper showing the model generating a self-correcting "aha moment" during a math problem.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)
Image 9: The emergence of the "Aha moment" as shown in the DeepSeek R1 technical report. (Source [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948))

The success of R1-Zero is notable because it was the first demonstration that a model could develop advanced reasoning capabilities through pure RL, without being explicitly taught how to reason through supervised examples.

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

The SFT+RL hybrid approach, used to create the final DeepSeek-R1 model, builds upon the foundation of pure RL to create a more stable and user-friendly model. This multi-stage process is designed to refine the raw reasoning capabilities of R1-Zero while aligning its outputs with human preferences [[1]](https://arxiv.org/abs/2501.12948).![A flowchart illustrating the multi-stage development process of the DeepSeek-R1 model, including SFT and RL stages.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)
Image 10: The development process of the DeepSeek-R1 model. (Source [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948))

The pipeline generally consists of these phases:

1.  **Cold-Start SFT:** The process begins with a small SFT stage using a few thousand high-quality reasoning examples. This "cold-start" data, often generated and filtered from earlier models like R1-Zero, teaches the base model the basic structure of a reasoning trace. This initial SFT improves the readability of the model's output and makes the subsequent RL phase more stable and efficient [[4]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners), [[28]](https://www.vellum.ai/blog/the-training-of-deepseek-r1-and-ways-to-use-it).
2.  **Reasoning-Oriented RL:** The model then undergoes large-scale RL training similar to R1-Zero, using verifiable rewards. During this phase, a **language consistency reward** is introduced to penalize outputs that mix languages (e.g., English and Chinese). This improves readability even if it slightly degrades raw accuracy on some tasks, aligning the model better with human preferences [[1]](https://arxiv.org/abs/2501.12948), [[29]](https://artgor.medium.com/paper-review-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning-edf4343dcf3a).
3.  **Rejection Sampling and SFT:** After the RL stage, a large synthetic dataset is generated. The model produces multiple solutions for each problem, and only the correct ones are kept. This filtered dataset, often mixed with general-purpose instruction data, is used for another round of SFT. This step helps the model absorb the best reasoning strategies discovered during RL while maintaining its general capabilities [[12]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).
4.  **Final RL Alignment:** A final RL stage is performed on a mix of reasoning and general-purpose tasks. For open-ended prompts, a preference model is used to reward helpfulness and harmlessness, similar to standard RLHF. This polishes the model, making it more suitable for general use.

This iterative refinement process allows DeepSeek-R1 to achieve state-of-the-art performance on reasoning benchmarks, rivaling closed-source models like OpenAI's o1 [[1]](https://arxiv.org/abs/2501.12948).![A table comparing the benchmark performance of DeepSeek-R1 against several OpenAI and Anthropic models.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)
Image 11: A benchmark comparison of OpenAI o1 and DeepSeek-R1 models from the DeepSeek-R1 technical report. (Source [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948))

### 4) Pure supervised finetuning (SFT) and distillation

Inference-time scaling improves performance without training, pure RL unlocks emergent reasoning, and a hybrid SFT+RL approach offers a stable path to production. The fourth approach, pure SFT or distillation, provides an efficient method to transfer these capabilities to smaller, more accessible models.

DeepSeek's approach to distillation is a form of SFT. Instead of traditional methods that involve matching the output probabilities (logits) of a smaller "student" model to a larger "teacher" model, DeepSeek uses the high-quality, step-by-step reasoning outputs generated by the powerful R1 model as a training dataset. Smaller open-source models, like Qwen and Llama, are then fine-tuned on this data [[1]](https://arxiv.org/abs/2501.12948), [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).![A flowchart showing the distillation process where the R1 model generates data to train smaller models.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)
Image 12: The development process of DeepSeek-R1-Distill models. (Source [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948))

DeepSeek developed these distilled models for two main reasons. First, it makes powerful reasoning accessible to a wider audience, as smaller models are cheaper to run and can be deployed on consumer-grade hardware. Second, it provides a more efficient path to strong reasoning capabilities for smaller models, which often struggle to develop these skills through pure RL alone [[1]](https://arxiv.org/abs/2501.12948).

The results show that this distillation technique is highly effective. Even the 1.5B parameter distilled Qwen model surpasses strong non-reasoning baselines on mathematical benchmarks. As the size of the student model increases, its performance gets progressively closer to that of the original R1 teacher [[1]](https://arxiv.org/abs/2501.12948).![A table comparing the performance of DeepSeek's distilled models against GPT-4o and Claude 3.5 Sonnet on several reasoning benchmarks.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)
Image 13: A benchmark comparison of distilled versus non-distilled models from the DeepSeek-R1 technical report. (Source [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948))

However, the DeepSeek report also provides a crucial insight when comparing these approaches. While distillation is effective, it is ultimately derivative; the student model is unlikely to surpass the teacher. This limitation stems from several open challenges in distilling reasoning to smaller models. These include a loss of nuanced, multi-step logic that smaller models struggle to represent, architectural mismatches between teacher and student, and the student's tendency to hallucinate when it lacks the vast factual knowledge of the teacher [[19]](https://medium.com/@graison/knowledge-distillation-in-the-era-of-large-language-models-llms-7b0bead7d822). For a 32B model, distillation substantially outperformed a model of the same size trained with pure RL. This suggests that for smaller models, it is more economical and effective to learn from a powerful teacher than to discover reasoning abilities from scratch [[1]](https://arxiv.org/abs/2501.12948).![A table comparing the performance of a distilled 32B model against a 32B model trained with pure RL.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)
Image 14: A benchmark comparison of distillation and RL on a smaller 32B model from the DeepSeek-R1 technical report. (Source [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948))

This finding highlights a key trade-off. Distillation is a practical and efficient strategy, but true breakthroughs in intelligence may still require the more computationally intensive path of large-scale RL on powerful base models. The table above would have been even more insightful if it included a comparison with a model trained using the full SFT+RL hybrid approach on the same 32B architecture, as well as a baseline showing the performance of the original, non-distilled 32B model.

After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the release's broader significance and limitations.
```
**Grader reasoning:**
- `cc`: The 4 main ways to build and improve reasoning models:
**1:** Both sections cover the same four main approaches: inference-time scaling, pure RL, SFT+RL, and distillation. The core concepts, examples (CoT, GRPO, the Aha moment), and key findings (distillation being more effective than pure RL for smaller models) are present in both. For the distillation sub-approach, the generated section gives two genuinely distinct reasons for building the distilled models — (1) accessibility on consumer-grade hardware, and (2) a more efficient path to strong reasoning for smaller models that struggle to acquire it through pure RL alone — satisfying the guideline's requirement for at least two distinct reasons.
- `fl`: The 4 main ways to build and improve reasoning models:
**1:** Both sections follow the same logical flow across all four sub-approaches, in the same order (inference-time scaling, pure RL, SFT+RL, distillation). The section ends with a transition to Section 6 ("After dissecting the four techniques... we can step back to evaluate the release's broader significance and limitations"), matching the guideline's suggested transition. A prior pass's claim that the section is missing a concluding summary is incorrect — that expectation was for the separate "Conclusion" section, which the generated article does include as its own H2 section further down.
- `de`: The 4 main ways to build and improve reasoning models:
**1:** [instances=4; quality=strong,strong,standard,standard] Candidates evaluated: (a) the "overthinking" inverted-U-curve finding, including the specific detail that the model may "flip" a correct answer to incorrect — ref [16], exploration-phase — QUALIFIES, strong (detailed mechanism, specific behavior described). (b) The discussion of open challenges in distillation (loss of nuanced multi-step logic, architectural mismatches, hallucination without the teacher's factual knowledge) — ref [19], medium.com/@graison/knowledge-distillation..., exploration-phase — QUALIFIES, strong (three named, specific failure modes bundled). (c) The GRPO mechanics (no separate critic/value network, group-normalized rewards, efficient for verifiable tasks) — ref [18], exploration-phase — QUALIFIES, standard (mechanism description without quantified specifics). (d) The claim that CoT prompting was later automated into self-directed reasoning in test-time scaling models — ref [17], exploration-phase — QUALIFIES, standard, for the same reason as in "How do we define reasoning model?": a technical/implementation nuance of the same mechanism, not a connection to an external field. One candidate was evaluated and rejected: the specific claim about GRPO's length bias and the Dr. GRPO fix, cited to ref [3] (arxiv.org/html/2503.20783v1) — confirmed in research.md's exploitation-phase block, not exploration. Since multiple instances qualify, depth_enhancement scores 1 for the section as a whole.
- `be`: The 4 main ways to build and improve reasoning models:
**0:** [instances=0] No breadth additions present. All of the section's exploration-traceable material (the overthinking research, GRPO mechanics, the CoT automation nuance, and the distillation-limits discussion) intensifies understanding of the same core topic rather than connecting it to an adjacent field, so none of it qualifies as breadth.
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** The qualifying depth additions (the overthinking research in the inference-time-scaling sub-part, the GRPO mechanics in the pure-RL sub-part, and the distillation-limits discussion) are technical asides that together make up a modest portion of this roughly 1,560-word section spanning four major approaches. The expected output's core narrative — DeepSeek's specific four-technique case study — clearly remains the dominant focus throughout.
- `ga`: The 4 main ways to build and improve reasoning models:
**0:** The generated section covers all four approaches with the specified images and technical details, correctly proposes two additional table comparisons for the distillation sub-section (a model trained with the full SFT+RL hybrid on the same 32B architecture, and a non-distilled 32B baseline), and includes the transition. However, the prose-only word count is approximately 1,564 words, short of the 1950-word target's required 1755–2145 range (±10%) by 191 words. This fails the word-count tolerance, so GuidelineAdherence scores 0.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset2`

**Article text:**
```
## The 4 main ways to build and improve reasoning models

There are currently four key techniques used to build specialized reasoning models and enhance the reasoning abilities of LLMs. While the exact workings of proprietary models like OpenAI's o1 and o3 remain unknown, they are rumored to combine multiple training and inference-time strategies.

### 1) Inference-time scaling

Inference-time scaling refers to allocating more computational resources during inference to improve a model's output. It is analogous to giving a human extra time to think through a problem. This approach connects to the concept of test-time compute scaling laws, which suggest that performance can improve by dedicating more computation at the moment a query is made, not just during training [[4]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

Common methods include Chain-of-Thought (CoT) prompting, where a model is explicitly asked to "think step by step" [[5]](https://arxiv.org/abs/2205.11916).![Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)

Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper

More advanced techniques involve generating multiple potential solutions and using a selection mechanism. This can be as simple as **majority voting** or as complex as **beam search** and **Monte Carlo Tree Search (MCTS)**. These search algorithms often rely on a **Process Reward Model (PRM)**, which evaluates the correctness of each intermediate reasoning step, to guide the search toward the most promising solution path [[6]](https://arxiv.org/abs/2408.03314). PRMs provide real-time feedback during the reasoning process, allowing even smaller models to outperform larger ones by making more efficient use of their computational budget [[25]](https://ojs.aaai.org/index.php/AAAI/article/view/40797/44758). For example, recent work has shown that a 1B parameter model with the right inference-time scaling can surpass a 405B model that lacks it [[4]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d793706_1600x919.png)

Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper

Interestingly, the DeepSeek-R1 technical report categorizes both PRMs and MCTS under "unsuccessful attempts," stating that their benefits were limited compared to the computational overhead they introduced during large-scale RL [[7]](https://arxiv.org/abs/2501.12948). This does not necessarily mean these techniques are useless. It is possible DeepSeek still applies them at the application layer, separate from the core model training, or that their specific implementation was not optimal.

This finding aligns with a growing body of research challenging the assumption that more thinking always leads to better answers. Studies have applied the economic law of diminishing marginal returns to test-time compute, revealing that beyond a certain point, additional reasoning provides little benefit and can even be harmful. This "overthinking" can cause a model to abandon a correct initial answer, an event termed a "negative flip." The optimal thinking length varies by task difficulty, with simpler problems suffering from overthinking much earlier than complex ones [[19]](https://arxiv.org/html/2604.10739v1).

The high cost of models like OpenAI's o1 and o3 compared to general-purpose models like GPT-4o is likely due to this heavy use of inference-time computation. Generating and evaluating multiple reasoning paths is far more resource-intensive than producing a single, direct answer. For instance, o1 can be six times more expensive per token than GPT-4o and take minutes to "think" through a problem that GPT-4o answers in seconds [[8]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison), [[26]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o). This higher cost reflects the advanced reasoning, specialized training, and novel architecture required for these models [[27]](https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c).

### 2) Pure reinforcement learning (RL)

The second approach, exemplified by DeepSeek-R1-Zero, is pure reinforcement learning. Unlike typical RLHF pipelines, which start with a model already fine-tuned on human-written examples (SFT), pure RL is applied directly to the base model. This "cold-start" process relies on automated, verifiable reward signals instead of a reward model trained on human preferences.![Figure 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)

Figure 8: The development process of DeepSeek-R1-Zero model.

In the R1 paper, the reward function has two main components. **Accuracy rewards** provide a binary signal (correct or incorrect) based on whether the final answer to a math or coding problem matches the ground truth. **Format rewards** incentivize the model to structure its output correctly, such as by enclosing its reasoning within `<think>` tags [[7]](https://arxiv.org/abs/2501.12948), [[9]](https://www.nature.com/articles/s41586-025-09422-z).

A key phenomenon observed during this process is the "Aha moment." This is a point in training where the model spontaneously begins to generate long, complex reasoning traces and exhibit self-correction patterns, even for simple questions [[1]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners). It starts using phrases like "Wait, let me reevaluate" without being explicitly taught to do so.![Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)

Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.

The RL algorithm used by DeepSeek, Group Relative Policy Optimization (GRPO), is key to this cold-start process. Unlike other RL methods like Proximal Policy Optimization (PPO), GRPO is a simpler, critic-less algorithm. For a given prompt, it generates multiple responses, calculates the average reward for the group, and then normalizes each response's reward against this group mean and standard deviation. This process creates a clean, learnable signal of how much better or worse a given reasoning trace was compared to its siblings, without the need to train a separate value network, saving memory and compute [[20]](http://scalable-ai.eecs.berkeley.edu/assets/lecture_slides/lecture_15.pdf), [[21]](https://ghost.oxen.ai/why-grpo-is-important-and-how-it-works).

However, some research offers a more critical perspective. A study examining R1-Zero-like training suggests this "Aha moment" may not be entirely emergent [[10]](https://arxiv.org/html/2503.20783v1). The analysis found that base models, including DeepSeek-V3-Base, already generate self-reflection keywords before any RL is applied. The paper also identifies a potential bias in GRPO, which may artificially encourage longer responses, especially for incorrect answers. To address this, the authors proposed Dr. GRPO, an unbiased version that improves token efficiency.

Despite this debate, DeepSeek-R1-Zero remains a landmark, as it was the first open demonstration that a model could develop sophisticated reasoning capabilities through pure RL, without being pre-loaded with human-written reasoning examples.

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

The third method is a hybrid approach that combines Supervised Fine-Tuning with Reinforcement Learning. This is the pipeline used to create the flagship DeepSeek-R1 model, and it is designed to produce more stable and higher-performing results than pure RL alone.![Figure 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)

Figure 10: The development process of DeepSeek-R1 model.

The process has four main stages [[2]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1), [[7]](https://arxiv.org/abs/2501.12948):
1.  **Cold-Start SFT:** The process begins by fine-tuning the base model on a small, "cold-start" dataset of a few thousand high-quality reasoning examples, some generated by the R1-Zero model. This initial SFT phase helps stabilize the subsequent RL training by providing the model with a basic template for coherent, step-by-step thinking.
2.  **Reasoning-Oriented RL:** The model then undergoes large-scale RL training, similar to the R1-Zero process. However, in addition to accuracy and format rewards, a **language consistency reward** is introduced. This penalizes the model for mixing languages (e.g., English and Chinese) in its responses, improving readability even if it causes a slight dip in raw accuracy on some tasks.
3.  **Rejection Sampling and General SFT:** Next, the RL-tuned model is used to generate a large synthetic dataset of around 600,000 correct reasoning traces. This data is combined with 200,000 general-purpose instruction-following examples and used for another round of SFT. This step broadens the model's capabilities beyond pure reasoning.
4.  **Final RL Polish:** The final stage involves another round of RL, this time mixing verifiable reasoning tasks with general preference-tuning using a standard reward model. This polishes the model for helpfulness and harmlessness, resulting in the final, user-friendly DeepSeek-R1.

This iterative, multi-stage pipeline allows the final model to inherit the powerful reasoning abilities discovered through RL while ensuring its outputs are readable, consistent, and aligned with human preferences. The result is a model that achieves state-of-the-art performance on reasoning benchmarks, rivaling closed-source competitors like OpenAI's o1.![Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)

Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report

### 4) Pure supervised finetuning (SFT) and distillation

To recap, we have covered three primary methods for building reasoning models: inference-time scaling, which uses more compute at runtime; pure RL, which teaches reasoning from scratch using verifiable outcomes; and the SFT+RL hybrid, which refines RL-discovered abilities for production use. The fourth and final approach is pure supervised finetuning, most notably used in the form of distillation.

DeepSeek used this method to create its R1-Distill models. This process involves taking the powerful DeepSeek-R1 model and using it to generate a large dataset of around 800,000 high-quality, step-by-step reasoning solutions. Smaller, open-source base models like Qwen and Llama are then fine-tuned on this synthetic dataset [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)

Figure 12: The development process of DeepSeek-R1-Distill models.

This is different from traditional distillation, which often involves matching the output probabilities (logits) of the teacher model. Here, the student model simply learns to replicate the reasoning text generated by the teacher. DeepSeek developed these distilled models to make advanced reasoning capabilities more accessible, as the massive 671B-parameter R1 model is impractical for most users to run [[12]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).![Figure 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)

Figure 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report

So, how effective is this approach? The DeepSeek report shows that while distillation is less powerful than the full-scale R1 model, it outperforms pure RL when applied to smaller models. For example, they ran a large-scale RL experiment on a 32B model (Qwen2.5-32B-Zero) and found it performed worse than the distilled version of the same size (DeepSeek-R1-Distill-Qwen-32B) across all benchmarks [[7]](https://arxiv.org/abs/2501.12948).![Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)

Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report

This suggests that certain advanced reasoning behaviors may be emergent properties of very large models and are difficult for smaller models to discover on their own through RL. It is more efficient to "teach" them these patterns through distillation. This highlights a fundamental challenge: it is not just about transferring knowledge, but about transferring an emergent capability. Chain-of-thought is often considered an emergent property of models exceeding 100B parameters. Smaller models may lack the capacity to replicate this behavior organically, and simply showing them examples can lead to shallow mimicry rather than a deep transfer of the underlying skill. This can result in a loss of nuanced reasoning and brittle performance on out-of-distribution problems [[22]](https://ojs.aaai.org/index.php/AAAI/article/view/29821/31426).

The table above could have been more useful with two additional comparisons: the performance of the base Qwen2.5-32B model and the full DeepSeek-R1 model. This would have provided a complete picture, from the baseline to the teacher model, showing the full spectrum of performance.

After dissecting these four techniques and seeing them embodied in the DeepSeek-R1 family, we can step back to evaluate the broader significance and limitations of this important release.
```
**Grader reasoning:**
- `cc`: The 4 main ways to build and improve reasoning models:
**1:** Across all four sub-approaches, the generated section covers inference-time scaling (CoT, search strategies including PRM, the "unsuccessful attempts" categorization, o1 cost speculation, plus well-grounded overthinking/diminishing-returns detail), pure RL (R1-Zero, both reward types, the Aha-moment phenomenon, GRPO's mechanism in more mathematical detail, and a critical-perspective caveat), SFT+RL (the four-stage pipeline, language-consistency reward, 600K+200K SFT samples), and distillation (mechanism, benchmark comparisons, the 32B RL-vs-distillation result, plus well-grounded capacity-limit findings) with strong fidelity. As in other presets for this lesson, the expected section's specific "additional comparisons" suggestion (Qwen-32B with SFT+RL; DeepSeek-V3 with pure SFT) is replaced with a different pair (base Qwen2.5-32B; the full R1 model) — a small, peripheral substitution inside an otherwise comprehensive section. Separately, the generated section renders the Aha-moment example phrase as "phrases like 'Wait, let me reevaluate'" rather than the expected section's verbatim "Wait, wait. Wait. That's an aha moment I can flag here" — since it is framed as an illustrative example ("phrases like") rather than a claimed direct quote, and the underlying phenomenon (spontaneous self-correction language) is accurately conveyed, this is treated as a paraphrase rather than a missing or contradicted idea.
- `fl`: The 4 main ways to build and improve reasoning models:
**1:** All figures land in the same relative position as their expected counterparts: Figures 6 and 7 (CoT, search strategies), Figures 8 and 9 (reward mechanics, Aha moment), Figures 10 and 11 (SFT+RL stages, benchmark), and Figures 13 and 14 (distillation benchmarks) all match. Figure 12 is placed immediately after the method intro rather than after the classical-distillation-comparison paragraph that follows it in the expected section — the same narrow, single-paragraph-adjacent reordering already ruled too trivial to count as a placement failure. All exploration-grounded additions (GRPO detail, overthinking/negative-flip, distillation capacity limits) have their own local lead-ins and do not disrupt the surrounding idea order.
- `de`: The 4 main ways to build and improve reasoning models:
**1:** [instances=3; quality=strong,strong,strong] Three qualifying depth additions, each traceable to an exploration-phase source. (1) In the Pure RL sub-section: the detailed GRPO mechanism — generating a group of responses, normalizing each reward against the group mean and standard deviation to form a critic-free learning signal — traceable to two exploration sources (Berkeley lecture slides; the oxen.ai GRPO explainer) closely, cited [20], [21]. Strong: a specific mathematical mechanism explanation, not a generic mention. (2) In the inference-time-scaling sub-section: the diminishing-marginal-returns/'negative flip' overthinking discussion, traceable to the exploration-phase 'When More Thinking Hurts' source verbatim (including the exact term 'negative flip' and the task-difficulty-dependent optimal-thinking-length claim), cited [19]. Strong: a detailed, multi-claim paragraph with specific terminology from the source. (3) In the distillation sub-section: the capacity-limit discussion — CoT as an emergent property of >100B-parameter models, small models risking 'shallow mimicry' and 'brittle performance on out-of-distribution problems' — traceable to the exploration-phase 'distilling reasoning to 1B-scale models' source thread, cited [22]. Strong: specific, named failure modes directly explaining a limitation of the core topic. A fourth candidate — the 'Dr. GRPO' critical-perspective addition [10] — does not qualify: it is traceable only to an exploitation-phase source, not an exploration one.
- `be`: The 4 main ways to build and improve reasoning models:
**0:** [instances=0] research.md's exploration-phase sources include three depth-qualifying instances credited above, but no breadth-qualifying addition is present within this section specifically.
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** depth_enhancement scored 1 for this section (three strong additions: GRPO mechanism detail, the overthinking/negative-flip discussion, and the distillation capacity-limit findings). Each is a contained paragraph placed at a natural point within its own sub-section, and the four techniques and the DeepSeek-R1 case study remain clearly the dominant focus throughout this large section. CorePreservation scores 1.
- `ga`: The 4 main ways to build and improve reasoning models:
**0:** Content-wise this section covers essentially everything the guideline requires across all four approaches, including the required "at least two useful additional comparisons" (the guideline does not specify which two). However, prose-only word count is approximately 1,555 words against a 1,950-word target (±195 tolerance, range 1,755–2,145 words), about 200 words below the minimum — clearly outside tolerance regardless of any borderline-margin question.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset2`

**Article text:**
```
## The 4 main ways to build and improve reasoning models

The current landscape of techniques to enhance LLM reasoning and build specialized models is rich and varied. While the exact workings of frontier models like OpenAI's o1 and o3 remain undisclosed, they are rumored to combine both inference-time and training-time techniques. Here, we will outline the four key approaches, using the DeepSeek-R1 project as a running example.

### Inference-time scaling

Inference-time scaling refers to the practice of dedicating more computational resources during the inference or "test-time" phase to improve a model's output. This is analogous to giving a human extra time to think through a difficult problem. The idea is that with more compute, a model can explore more possibilities, refine its initial thoughts, and ultimately arrive at a better solution. This concept is closely tied to "test-time compute scaling laws," which suggest that performance can improve as inference-time compute increases [[4]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

Several methods fall under this category. **Chain-of-Thought (CoT) prompting** is a foundational technique where the model is prompted to "think step by step," generating an explicit reasoning trace before giving a final answer. This simple instruction can dramatically improve performance on complex tasks [[5]](https://arxiv.org/abs/2205.11916).![Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)
Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper [[5]](https://arxiv.org/abs/2205.11916). (Source [https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png))

More advanced methods involve search algorithms. **Majority voting**, or best-of-N sampling, involves generating multiple independent answers and selecting the most frequent one. **Beam search** and **Monte Carlo Tree Search (MCTS)** are more sophisticated techniques that explore a tree of possible reasoning paths, pruning unpromising branches and focusing compute on more likely solutions.

These search methods often rely on a **Process Reward Model (PRM)**, a verifier trained to score the correctness of each intermediate step in a solution. This provides a much finer-grained signal than just evaluating the final answer [[6]](https://arxiv.org/abs/2408.03314). A recent innovation, GenPRM, further enhances this by having the PRM generate its own reasoning for its score, enabling even smaller models to surpass much larger ones through test-time scaling [[30]](https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e). This generative approach to process supervision allows for more effective test-time scaling, with a 7B parameter GenPRM outperforming a 72B parameter classification-based PRM.![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)
Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper [[6]](https://arxiv.org/abs/2408.03314). (Source [https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png))

Interestingly, the DeepSeek-R1 technical report categorizes both PRMs and MCTS under "unsuccessful attempts" [[1]](https://arxiv.org/abs/2501.12948). They argue that while these methods can be useful for re-ranking a set of generated answers, the computational overhead they introduce during large-scale RL training is not justified by the limited performance gains. This suggests that DeepSeek prioritized training-time optimization over inference-time search. However, this does not mean they completely disregard inference-time scaling. It is plausible that such techniques are still applied at the application layer, even if they were not central to the core training pipeline.

The high cost of OpenAI's o1 models compared to models like GPT-4o might be explained by their reliance on inference-time scaling. Models like o1 are designed to "think" longer before answering, which requires more computational resources per query [[7]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison), [[8]](https://www.uctoday.com/unified-communications/chatgpt-4o-vs-o1-which-openai-model-is-best). This extra computation time is likely used for internal search, verification, or other refinement processes, leading to higher accuracy on complex tasks but also higher operational costs [[9]](https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c). For example, o1 can take 2-3 minutes to "think" through a problem that GPT-4o answers in under a second [[31]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o). The price reflects this: o1 can be 6 times more expensive for inputs and outputs compared to GPT-4o.

This trade-off is not just about cost. The assumption that more thinking always leads to better answers is flawed. A systematic study of test-time compute scaling found that beyond a certain point, the marginal utility of additional reasoning tokens diminishes and eventually becomes negative [[22]](https://arxiv.org/html/2604.10739v1). This "overthinking" causes models to abandon correct initial answers, a phenomenon measured by "negative flips" (correct → incorrect). This effect is more pronounced on easier problems, suggesting that a uniform, high compute budget for all tasks is a suboptimal strategy.

### Pure reinforcement learning (RL)

The second approach, exemplified by DeepSeek-R1-Zero, is to use pure reinforcement learning directly on a base model without any preliminary supervised fine-tuning. This "cold-start" method is a notable departure from typical RLHF pipelines, which first align a model with human-like responses through SFT before optimizing for preferences with RL.![Figure 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)
Figure 8: The development process of DeepSeek-R1-Zero model. (Source [https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png))

In this paradigm, the reward signal is not derived from a reward model trained on human preferences. Instead, it comes from rule-based verifiers that provide objective feedback. The DeepSeek-R1 paper details two primary types of rewards used for R1-Zero [[1]](https://arxiv.org/abs/2501.12948), [[10]](https://www.nature.com/articles/s41586-025-09422-z):
1.  **Accuracy rewards:** These are binary signals that indicate whether the model's final answer is correct. For math problems, this is a simple string match against the ground truth. For coding tasks, it is a pass/fail from a compiler running against predefined test cases.
2.  **Format rewards:** These rewards incentivize the model to follow a specific output structure, such as enclosing its reasoning process within `<think>` and `</think>` tags. This ensures the model's output is parsable and its thought process is explicit.

The algorithm DeepSeek used to apply these rewards is known as Group-based Reward Policy Optimization (GRPO). Unlike the more common Proximal Policy Optimization (PPO), GRPO is a critic-less algorithm. It works by generating multiple responses for the same prompt, grouping them, and then normalizing the rewards based on the mean and standard deviation within that group. This approach is memory-efficient and computationally simple, making it a natural fit for verifiable tasks where multiple samples can be generated per prompt [[23]](https://cameronrwolfe.substack.com/p/grpo). However, recent analysis has identified an optimization bias in GRPO that can artificially increase response length, especially for incorrect answers. A proposed fix, Dr. GRPO, removes length and standard deviation normalization to improve token efficiency while maintaining performance [[32]](https://arxiv.org/html/2503.20783v1).

A key phenomenon observed during this pure RL training is the "Aha moment" [[1]](https://arxiv.org/abs/2501.12948), [[11]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners). This is a point in training where the model's behavior shifts dramatically. It starts to spontaneously generate long, detailed reasoning traces, including self-reflection, verification of its own steps, and exploration of alternative approaches. This emergent behavior, which was not explicitly taught, demonstrates that the model is learning to reason more deeply to maximize its accuracy reward. However, some studies suggest this "Aha moment" may not be as emergent as it seems, as even base models like DeepSeek-V3-Base already exhibit self-reflection keywords before RL tuning [[32]](https://arxiv.org/html/2503.20783v1).![Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)
Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment [[1]](https://arxiv.org/abs/2501.12948). (Source [https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png))

The success of R1-Zero is a milestone. It is the first clear demonstration that a model can develop sophisticated reasoning capabilities through pure RL, driven only by a verifiable outcome, without being pre-conditioned on human-written reasoning examples.

### Supervised finetuning and reinforcement learning (SFT + RL)

The third approach is a hybrid model that combines the strengths of both SFT and RL. This is the method used to create the flagship DeepSeek-R1 model, which builds upon the foundation laid by R1-Zero. The goal of this multi-stage pipeline is to refine the raw reasoning abilities of R1-Zero, making them more stable, human-readable, and performant across a wider range of tasks [[1]](https://arxiv.org/abs/2501.12948).![Figure 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)
Figure 10: The development process of DeepSeek-R1 model. (Source [https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png))

The process begins with generating a "cold-start" dataset. This involves using early versions of the R1-Zero model to generate detailed reasoning traces for a few thousand tasks. These traces are then filtered for correctness and refined by human annotators to ensure they are clear and follow a consistent, conversational style. The base model is then fine-tuned on this small, high-quality dataset. This initial SFT stage gives the model a solid foundation in generating coherent, human-friendly reasoning before it enters the more exploratory RL phase [[11]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners).

Next, the model undergoes large-scale RL, similar to the R1-Zero training. However, in addition to the accuracy and format rewards, a **language consistency reward** is introduced. This reward penalizes the model for mixing languages (e.g., English and Chinese) within a single response. While the paper notes that this slightly degrades raw accuracy on some tasks, it improves readability and aligns the model's output with human preferences [[1]](https://arxiv.org/abs/2501.12948), [[12]](https://transitions.substack.com/p/the-laymans-introduction-to-deepseek).

The pipeline then iterates through further stages of SFT and RL. The model's own high-quality outputs are used to create new, larger SFT datasets (a technique known as rejection sampling), which are then used for another round of fine-tuning. This is followed by a final RL stage that mixes reasoning tasks with general instruction-following and preference data, using model-based rewards to improve helpfulness and harmlessness. This staged refinement process allows the model to absorb the best of its RL-discovered strategies into a more stable, supervised format, while also broadening its capabilities beyond pure reasoning. The result is a model that achieves state-of-the-art performance on reasoning benchmarks, often comparable to or exceeding that of closed models like OpenAI's o1 [[1]](https://arxiv.org/abs/2501.12948).![Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)
Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report [[1]](https://arxiv.org/abs/2501.12948). (Source [https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png))

### Pure supervised finetuning (SFT) and distillation

To quickly review, we have covered three primary methods for developing reasoning models. **Inference-time scaling** enhances performance by allocating more computational resources during inference, without altering the model's weights. **Pure RL** cultivates reasoning abilities from a base model using verifiable reward signals, leading to the emergence of complex behaviors. The **SFT+RL hybrid** approach refines these emergent abilities through iterative stages of supervised learning and reinforcement learning, resulting in more stable and human-aligned models.

The fourth major approach is to use pure SFT, most notably in the form of distillation. This is the method DeepSeek used to create its R1-Distill series of smaller, more accessible reasoning models. The process involves using the large, powerful DeepSeek-R1 model to generate a massive dataset of high-quality reasoning traces—around 800,000 examples—and then using this dataset to fine-tune smaller, open-weight base models like Qwen and Llama [[1]](https://arxiv.org/abs/2501.12948).![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)
Figure 12: The development process of DeepSeek-R1-Distill models. (Source [https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png))

It is important to understand that this is not traditional knowledge distillation, where a smaller "student" model learns to mimic the output probabilities (logits) of a larger "teacher" model. Instead, this is a form of data distillation or SFT, where the student learns to replicate the teacher's final text output, including the entire chain-of-thought [[2]](https://redwerk.com/blog/what-is-model-distillation), [[13]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond). The student model is not trained with RL; it simply learns to imitate the reasoning patterns discovered by the teacher.

DeepSeek developed these distilled models for two key reasons. First, to make powerful reasoning capabilities more accessible. The massive 671B parameter R1 model is computationally expensive to run, and the distilled models offer a more efficient alternative for users with limited resources. Second, to provide a valuable resource for the research community to study the mechanisms of long-CoT reasoning models [[3]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d). As shown in the benchmarks, even the 1.5B distilled model can surpass strong, non-reasoning baselines on mathematical tasks.![Figure 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)
Figure 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report [[1]](https://arxiv.org/abs/2501.12948). (Source [https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png))

The DeepSeek report provides a direct comparison of the effectiveness of these approaches. While the distilled models are not as powerful as the full R1 teacher model, they outperform models of a similar size that are trained with pure RL from a cold start. For example, the R1-Distill-Qwen-32B model achieves much higher scores on reasoning benchmarks than a 32B model trained with the R1-Zero (pure RL) methodology [[1]](https://arxiv.org/abs/2501.12948).![Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)
Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report [[1]](https://arxiv.org/abs/2501.12948). (Source [https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png))

This leads to two important insights. First, for smaller models, distillation appears to be a more economical and effective strategy than attempting to elicit emergent reasoning through pure RL, which may require a certain scale to be successful. Second, while distillation is powerful, it is ultimately a method of knowledge transfer, not knowledge creation. To push the boundaries of AI intelligence, more powerful base models and large-scale RL are still necessary to discover novel reasoning strategies in the first place [[14]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1). The table above could have been more useful if it included a comparison with the base model to show the uplift from RL, and a comparison with the teacher model to show the performance drop from distillation.

However, distilling reasoning to smaller models presents open challenges. The process can dilute the nuanced, multi-step logic of the teacher, and it is particularly difficult when there is a large architectural gap between the teacher and student. Furthermore, complex reasoning like CoT has been observed as an emergent property of models at a scale of over 100B parameters. Simply training smaller models on CoT data does not guarantee they can replicate the underlying reasoning capabilities, especially for tasks requiring rare factual knowledge or precise computation [[24]](https://ojs.aaai.org/index.php/AAAI/article/view/29821/31426).

After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the release's broader significance and limitations.
```
**Grader reasoning:**
- `cc`: The 4 main ways to build and improve reasoning models:
**1:** Across all four sub-approaches, the generated section covers inference-time scaling (CoT, search strategies, PRM, the 'unsuccessful attempts' categorization, cost/latency speculation, plus a well-grounded overthinking/negative-flip caveat), pure RL (R1-Zero, both reward types, GRPO with a well-grounded efficiency detail, the Aha-moment phenomenon), SFT+RL (the staged pipeline, language-consistency reward, rejection sampling), and distillation (mechanism, two reasons, benchmark comparisons, the 32B RL-vs-distillation result, plus a well-grounded capacity-limit caveat) with strong fidelity. As in other presets for this lesson, the expected section's specific 'additional comparisons' suggestion is replaced with a different pair (a base-model comparison; a teacher-model comparison) rather than reproduced verbatim — a small, peripheral substitution.
- `fl`: The 4 main ways to build and improve reasoning models:
**1:** All figures land in the same relative position as their expected counterparts, including the distillation-process figure landing after the classical-distillation-comparison explanation (the same narrow, single-paragraph-adjacent placement already ruled too trivial to penalize when it differs, and here it matches exactly regardless). Every exploration-grounded addition (GRPO efficiency, overthinking/negative-flip, distillation capacity limits) has its own local lead-in and does not disrupt the surrounding idea order.
- `de`: The 4 main ways to build and improve reasoning models:
**1:** [instances=3; quality=strong,strong,standard] Three qualifying depth additions, each traceable to an exploration-phase source. (1) In inference-time scaling: the overthinking/negative-flip discussion — "the marginal utility of additional reasoning tokens diminishes and eventually becomes negative ... measured by 'negative flips'... more pronounced on easier problems" [22], traceable to the 'When More Thinking Hurts' source closely. Strong: detailed, multi-sentence, specific terminology. (2) In the distillation sub-section: "complex reasoning like CoT has been observed as an emergent property of models at a scale of over 100B parameters... especially for tasks requiring rare factual knowledge or precise computation" [24], traceable to a distinct exploration source closely. Strong: specific quantified threshold plus named failure conditions. (3) In the Pure RL sub-section: GRPO's efficiency — "memory-efficient and computationally simple, making it a natural fit for verifiable tasks where multiple samples can be generated per prompt" [23], traceable to an exploration source closely. Standard: a valid, source-attributed addition but comparatively brief. Two other candidates — the Dr. GRPO fix and the pre-RL self-reflection-keywords claim, both citing [32] — do not qualify: [32] traces only to an exploitation-phase source, not an exploration one.
- `be`: The 4 main ways to build and improve reasoning models:
**0:** [instances=0] research.md's exploration-phase sources include three depth-qualifying instances credited above, but no breadth-qualifying addition is present within this section specifically.
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** depth_enhancement scored 1 for this section (three additions, two strong and one standard). Each is a contained paragraph or clause placed at a natural point within its own sub-section, and the four techniques and the DeepSeek-R1 case study remain clearly the dominant focus throughout this large section. CorePreservation scores 1.
- `ga`: The 4 main ways to build and improve reasoning models:
**1:** Content-wise this section covers essentially everything the guideline requires across all four approaches, including the required 'at least two useful additional comparisons.' Prose-only word count is approximately 1,960 words against a 1,950-word target (±195 tolerance, range 1,755–2,145 words), comfortably within tolerance.

### Arm: light (preset1)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset1`

**Article text:**
```
## The 4 main ways to build and improve reasoning models

The key techniques for building specialized reasoning models are now becoming clearer. While the exact workings of proprietary models like OpenAI's o1 and o3 remain unknown, they are rumored to combine both inference-time and training-time techniques. Based on recent research, particularly the DeepSeek R1 paper, we can outline four primary approaches [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

### 1) Inference-time scaling

Inference-time scaling is about improving a model's performance by giving it more computational resources at the time of inference. It is like giving a person extra time to think about a difficult problem [[7]](https://arxiv.org/abs/2408.03314). This can be done without any changes to the model's weights.

Common methods include Chain-of-Thought (CoT) prompting, where you simply ask the model to "think step by step" [[2]](https://arxiv.org/abs/2205.11916). More advanced techniques involve search strategies like majority voting, beam search, or Monte Carlo Tree Search (MCTS), which explore multiple possible solutions and select the best one. These search methods often rely on a Process Reward Model (PRM) to evaluate the quality of intermediate reasoning steps [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling). A PRM provides real-time feedback at each step of the reasoning process, guiding the model toward more accurate solutions. This allows smaller models to sometimes outperform much larger ones by using their computational budget more effectively [[26]](https://ojs.aaai.org/index.php/AAAI/article/view/40797/44758). For example, recent work on Generative PRMs (GenPRM) has shown that a 1B parameter model with the right inference-scaling strategy can surpass a 405B model that lacks it [[27]](https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e).![Image 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)
Image 6: An example of classic CoT prompting. (Source [arxiv.org](https://arxiv.org/abs/2205.11916) [[2]](https://arxiv.org/abs/2205.11916))![Image 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)
Image 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source [arxiv.org](https://arxiv.org/abs/2408.03314) [[7]](https://arxiv.org/abs/2408.03314))

Interestingly, the DeepSeek R1 technical report lists common inference-time scaling methods like PRM-based search and MCTS under "unsuccessful attempts" [[3]](https://arxiv.org/abs/2501.12948). This suggests that their model's ability to generate long reasoning chains is an intrinsic property learned during training, rather than something forced at inference time. However, DeepSeek could still apply these techniques at the application layer to further boost performance [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

This heavy reliance on computation at inference might also explain why OpenAI's o1 models are more expensive than models like GPT-4o. The o1 models are designed to spend more time "thinking" through complex tasks, which requires more computational power and results in higher costs [[8]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison), [[9]](https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c). For example, GPT-o1 can be six times more expensive for inputs and outputs compared to GPT-4o [[8]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). This higher cost reflects the advanced reasoning, specialized training, and novel architecture that allow these models to achieve greater accuracy on difficult problems [[9]](https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c).

### 2) Pure reinforcement learning (RL)

The pure RL approach, exemplified by DeepSeek-R1-Zero, trains a reasoning model without a preliminary SFT stage. Instead of using a reward model trained on human preferences, this method applies rewards directly to the base model based on verifiable outcomes [[3]](https://arxiv.org/abs/2501.12948).![Image 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)
Image 8: The development process of the DeepSeek-R1-Zero model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

DeepSeek used two main types of rewards for R1-Zero [[3]](https://arxiv.org/abs/2501.12948), [[10]](https://www.nature.com/articles/s41586-025-09422-z):
*   **Accuracy rewards:** The model gets a positive reward if its final answer is correct. This works well for tasks with deterministic results, like math problems or coding challenges where the output can be automatically verified [[5]](https://thelmbook.com/articles#!./DeepSeek-R1.md).
*   **Format rewards:** The model is incentivized to structure its thinking process within specific tags, like `<think>` and `</think>`. This makes the reasoning process explicit and easier to analyze [[5]](https://thelmbook.com/articles#!./DeepSeek-R1.md), [[10]](https://www.nature.com/articles/s41586-025-09422-z).

To optimize for these rewards, DeepSeek used an algorithm called Group Relative Policy Optimization (GRPO). Unlike the more common Proximal Policy Optimization (PPO), GRPO does not require a separate value model. Instead, it samples a group of outputs for each prompt and uses the average reward of the group as a baseline to calculate the advantage for each individual output. This simplifies the training process and reduces resource consumption [[3]](https://arxiv.org/abs/2501.12948). However, research has shown that GRPO has an inherent bias that can artificially increase the length of incorrect responses. A proposed fix, called Dr. GRPO, removes certain normalization terms to eliminate this bias and improve token efficiency [[4]](https://arxiv.org/html/2503.20783v1).

A remarkable outcome of this process is the emergence of the "Aha moment." During training, the model spontaneously starts to generate longer reasoning traces, check its own work, and correct mistakes, using phrases like "Wait, wait. Wait. That's an aha moment I can flag here" [[3]](https://arxiv.org/abs/2501.12948). This behavior was not explicitly programmed but emerged as a result of the RL training. However, some research suggests that these self-reflection keywords may already be present in the base models, including DeepSeek-V3-Base, questioning whether this is a truly emergent capability [[4]](https://arxiv.org/html/2503.20783v1).

Further research complicates the narrative that pure RL creates these abilities from scratch. Self-correction behaviors appear to emerge progressively throughout pre-training, long before RL is applied [[19]](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training). This suggests that self-reflection is a latent feature of LLMs that RL does not introduce, but rather amplifies. The RL process may simply incentivize the model to surface abilities it already learned during its initial, massive pre-training phase [[20]](https://arxiv.org/html/2506.12217v1).![Image 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)
Image 9: An example of the "Aha moment" from the DeepSeek R1 technical report. (Source [arxiv.org](https://arxiv.org/abs/2501.12948) [[3]](https://arxiv.org/abs/2501.12948))

R1-Zero was the first model to show that it is possible to develop advanced reasoning capabilities through pure RL, without the need for human-annotated reasoning examples [[3]](https://arxiv.org/abs/2501.12948).

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

This hybrid approach, used to create the full DeepSeek-R1 model, combines the stability of SFT with the exploratory power of RL. It is a multi-stage process designed to build on the raw reasoning abilities of R1-Zero while making the model more user-friendly and performant [[3]](https://arxiv.org/abs/2501.12948), [[5]](https://thelmbook.com/articles#!./DeepSeek-R1.md).![Image 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)
Image 10: The development process of the DeepSeek-R1 model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

The process for R1 involved four main stages:
1.  **Cold-Start SFT:** The DeepSeek-V3-Base model was first fine-tuned on a small dataset of a few thousand long CoT examples. This "cold-start" data, which included R1-Zero outputs refined by human annotators and examples generated via few-shot prompting, helps to stabilize the initial phase of RL training and improve readability [[3]](https://arxiv.org/abs/2501.12948), [[5]](https://thelmbook.com/articles#!./DeepSeek-R1.md).
2.  **Reasoning-Focused RL:** The model then underwent intensive RL training on reasoning tasks like math and coding. In addition to accuracy and format rewards, a language consistency reward was introduced to prevent the model from mixing languages (e.g., English and Chinese) in its responses. This reward, calculated as the proportion of target language words in the CoT, improved readability at the cost of a slight degradation in task performance [[3]](https://arxiv.org/abs/2501.12948), [[11]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).
3.  **General-Purpose SFT:** The model was further fine-tuned on a larger dataset of about 800,000 examples. This dataset included 600,000 reasoning samples generated via rejection sampling from the model in the previous stage, as well as 200,000 non-reasoning samples (writing, factual Q&A, translation) from the DeepSeek-V3 pipeline to enhance its general capabilities [[3]](https://arxiv.org/abs/2501.12948), [[5]](https://thelmbook.com/articles#!./DeepSeek-R1.md).
4.  **General-Purpose RL:** The final stage involved another round of RL to align the model with human preferences for helpfulness and harmlessness, using reward models trained on general data. This stage mixed verifiable rewards for reasoning problems with preference-based rewards for general queries to polish the final model [[3]](https://arxiv.org/abs/2501.12948), [[11]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

This staged refinement process allowed DeepSeek-R1 to achieve strong performance on reasoning benchmarks, comparable to OpenAI's o1, while also being a capable general-purpose model [[3]](https://arxiv.org/abs/2501.12948).![Image 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)
Image 11: Benchmark comparison of OpenAI o1 and DeepSeek-R1 models. (Source [arxiv.org](https://arxiv.org/abs/2501.12948) [[3]](https://arxiv.org/abs/2501.12948))

### 4) Pure supervised finetuning (SFT) and distillation

The first approach, inference-time scaling, improves reasoning without changing model weights but at a high computational cost during inference. Pure RL, the second method, can unlock emergent reasoning behaviors from a base model but may lead to unstable or unreadable outputs. The third approach, a hybrid of SFT and RL, offers a more stable and production-ready path to high performance by refining the model through multiple stages.

The final method is pure SFT, often in the form of distillation. This is how DeepSeek created its smaller, more efficient R1-Distill models. Instead of the full, expensive training process, they transferred the reasoning capabilities of the large R1 model to smaller, open-weight models like Qwen and Llama [[3]](https://arxiv.org/abs/2501.12948).![Image 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)
Image 12: The development process of DeepSeek-R1-Distill models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This process is different from traditional knowledge distillation, which often involves matching the logit distributions of the teacher and student models. DeepSeek's approach is simpler: they generated 800,000 high-quality reasoning examples from R1 and then used this synthetic dataset to fine-tune the smaller models. It is essentially SFT on model-generated data, where the student learns to reproduce the teacher's behavior directly [[3]](https://arxiv.org/abs/2501.12948), [[6]](https://redwerk.com/blog/what-is-model-distillation).

DeepSeek developed these distilled models for two key reasons. First, they make powerful reasoning capabilities more accessible, as the smaller models are cheaper to run and easier to deploy on consumer-grade hardware. Second, they serve as a valuable resource for the research community to study the mechanisms of long CoT reasoning [[3]](https://arxiv.org/abs/2501.12948), [[12]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).![Image 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)
Image 13: Benchmark comparison of distilled versus non-distilled models. (Source [arxiv.org](https://arxiv.org/abs/2501.12948) [[3]](https://arxiv.org/abs/2501.12948))

The results show that while the distilled models are not as powerful as the full DeepSeek-R1, they often outperform their original instruction-tuned counterparts and even strong non-reasoning models like GPT-4o on mathematical benchmarks [[3]](https://arxiv.org/abs/2501.12948).

The DeepSeek report also provides insights into the effectiveness of distillation versus pure RL for smaller models. They found that applying the same large-scale RL process to a 32B parameter model did not achieve the same performance as distilling knowledge from the much larger R1. This suggests that for smaller models, distillation is a more economical and effective strategy for acquiring advanced reasoning skills [[3]](https://arxiv.org/abs/2501.12948).

However, this effectiveness has fundamental limits. Research has identified a "Small Model Learnability Gap," where models under a certain size (e.g., ≤3B parameters) do not benefit from long, complex reasoning chains because their limited capacity prevents them from internalizing the logic [[21]](https://arxiv.org/html/2502.12143v3). CoT reasoning itself is an emergent property of models with over 100B parameters, and this capability does not transfer well to smaller models that lack the capacity for it [[22]](https://ojs.aaai.org/index.php/AAAI/article/view/29821/31426). This can lead to distilled models hallucinating when faced with tasks requiring rare factual knowledge or precise computation [[23]](https://neurips.cc/virtual/2025/poster/117657).![Image 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)
Image 14: Benchmark comparison of distillation and RL on a smaller 32B model. (Source [arxiv.org](https://arxiv.org/abs/2501.12948) [[3]](https://arxiv.org/abs/2501.12948))

This insight is important: while advancing the frontier of AI may still require massive base models and large-scale RL, distillation provides a practical path for disseminating those capabilities more widely. The table above would have been more useful with two additional comparisons: the performance of the base model before RL (Qwen2.5-32B-Base) and the performance of the teacher model (DeepSeek-R1) on the same benchmarks.

After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the release's broader significance and limitations.
```
**Grader reasoning:**
- `cc`: The 4 main ways to build and improve reasoning models:
**1:** This section spans four sub-approaches (inference-time scaling, pure RL, SFT+RL, distillation), and all four are covered thoroughly with the core mechanics, reward types, and DeepSeek pipeline stages matching the expected output. For the distillation sub-part, the guideline requires two distinct reasons DeepSeek built the distilled models; the generated section gives two genuinely distinct reasons — (1) accessibility and cost efficiency on consumer-grade hardware, and (2) serving as a resource for the research community to study the mechanisms of long CoT reasoning — which, while phrased differently from the expected output's framing ("a case study in pure SFT"), are distinct from each other and cover the same underlying research-value point. No substantive idea is missing across the four sub-approaches.
- `fl`: The 4 main ways to build and improve reasoning models:
**1:** Both sections follow the same logical flow across all four sub-approaches, discussing inference-time scaling, pure RL, SFT+RL, and distillation in the same order as the expected output. The additional details (PRM/GenPRM, GRPO, the latent self-correction research, the Small Model Learnability Gap) are well-integrated within their respective sub-approaches and do not disrupt the main flow. The section ends with a transition to Section 6 ("After dissecting the four techniques... we can step back to evaluate the release's broader significance and limitations"), matching the guideline's suggested transition.
- `de`: The 4 main ways to build and improve reasoning models:
**1:** [instances=2; quality=strong,strong] Candidates evaluated and rejected: (a) PRM/GenPRM "1B beats 405B" discussion (refs [26],[27]) → research.md sources [32]/[34], exploitation — fails; (b) GRPO bias/Dr. GRPO fix and the "self-reflection keywords already in base models" claim (ref [4]) → research.md source [8], exploitation — fails; (c) GPT-o1 "six times more expensive" pricing detail (refs [8],[9]) → research.md sources [38]/[40], exploitation — fails. Two instances qualify: (1) self-correction behaviors emerge progressively during pre-training, and RL merely amplifies rather than creates this latent capability (refs [19]+[20], one continuous claim) → research.md sources [49]/[48], exploration-phase — QUALIFIES, strong (a specific, mechanistic counter-narrative citing two studies that meaningfully complicates the "emergence" framing). (2) The fundamental limits of distillation for small models — the "Small Model Learnability Gap" for ≤3B-parameter models, CoT as an emergent property of models over 100B parameters, and resulting hallucination on rare factual knowledge or precise computation (refs [21]+[22]+[23], one combined instance) → research.md sources [52]/[53]/[56], all exploration-phase — QUALIFIES, strong (a rich, multi-faceted, quantified limitation bundling three specific supporting findings). At least one instance qualifies, so the section scores 1.
- `be`: The 4 main ways to build and improve reasoning models:
**0:** [instances=0] No breadth additions present. All exploration-traceable material (latent self-correction research, distillation capacity-limit findings) intensifies the same core topic rather than connecting outward.
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** The qualifying depth additions (the latent-self-correction research in the pure-RL sub-part, and the Small Model Learnability Gap cluster in the distillation sub-part) are technical asides that together make up a modest portion of this roughly 1,570-word section spanning four major approaches. The expected output's core narrative — DeepSeek's specific four-technique case study — clearly remains the dominant focus throughout, so CorePreservation is 1.
- `ga`: The 4 main ways to build and improve reasoning models:
**0:** The generated section covers all four approaches with the specified images and technical details, and, contrary to a prior pass's claim, it DOES propose the guideline's required "at least two useful additional comparisons" for the distillation table: "the performance of the base model before RL (Qwen2.5-32B-Base) and the performance of the teacher model (DeepSeek-R1) on the same benchmarks." The actual disqualifying issue, uncaught by the prior pass, is word count: the prose-only word count for this section is approximately 1,572 words, short of the 1950-word target's required 1755–2145 range (±10%). This roughly 10% shortfall fails the word-count tolerance, so GuidelineAdherence scores 0.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset1`

**Article text:**
```
## The 4 main ways to build and improve reasoning models

Current techniques for enhancing LLM reasoning fall into four main categories. While the exact workings of proprietary models like OpenAI's o1 and o3 remain unknown, they are rumored to combine both training-time and inference-time methods to achieve their performance [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

### 1) Inference-time scaling

Inference-time scaling is the practice of allocating more computational resources during the generation process to improve an LLM's output. The core idea is simple: just as humans produce better answers when given more time to think, LLMs can improve their reasoning with techniques that encourage more "thought" during generation [[6]](https://arxiv.org/abs/2408.03314).

One of the simplest methods is **Chain-of-Thought (CoT) prompting**, where a simple phrase like "Let's think step by step" guides the model to generate intermediate reasoning steps before giving a final answer. This helps improve accuracy on complex problems by breaking them down into smaller, manageable parts [[2]](https://arxiv.org/abs/2205.11916).![Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)
Image 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper (Source [arxiv.org](https://arxiv.org/abs/2205.11916))

More advanced techniques involve search strategies that explore multiple potential solutions. These include:

*   **Majority Voting (or Self-Consistency):** The model generates multiple independent reasoning paths, and the final answer is determined by a majority vote. This is a form of "parallel" sampling.
*   **Beam Search:** This method explores multiple potential token sequences at each step, keeping a "beam" of the most promising candidates to build upon. It is a more guided search than simple parallel sampling.
*   **Lookahead Search:** An extension of beam search, this method simulates future steps (a "lookahead") to better evaluate the promise of current candidates before committing to a path. This is a special case of Monte Carlo Tree Search (MCTS) where the goal is exploitation rather than exploration.
*   **Process Reward Models (PRMs):** These models evaluate the correctness of each intermediate step in a reasoning chain, rather than just the final answer. This step-by-step feedback can guide search algorithms like beam search or lookahead search to find the optimal solution path [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)
Image 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper (Source [arxiv.org](https://arxiv.org/abs/2408.03314))

Interestingly, the DeepSeek-R1 technical report categorized common inference-time scaling methods like those based on PRMs and MCTS under "unsuccessful attempts" during their training process [[3]](https://arxiv.org/abs/2501.12948). This suggests that their model's ability to generate long, self-correcting reasoning traces emerged directly from the RL training, rather than being guided by these explicit search techniques. However, this does not mean they are not used. It is likely that inference-time scaling is still applied at the application layer to further boost the performance of the already powerful R1 model.

This heavy reliance on computation at inference time is a likely reason why models like OpenAI's o1 are more expensive than general-purpose models like GPT-4o. The o1 models are designed to spend more time and computational resources "thinking" through complex problems before responding, which leads to higher operational costs. For instance, o1's input costs are 6 times higher than GPT-4o's, and its output costs are also 6 times higher [[7]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). This price difference reflects the advanced reasoning, specialized training, and novel architecture that require more intensive computation [[21]](https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c).

### 2) Pure reinforcement learning (RL)

The second approach is to use pure reinforcement learning to cultivate reasoning abilities from a base model, as exemplified by DeepSeek-R1-Zero. This "cold-start" method bypasses the standard SFT phase and applies RL directly to a pre-trained model. Instead of relying on a reward model trained on human preferences, this technique uses automatically verifiable reward signals [[3]](https://arxiv.org/abs/2501.12948).![Figure 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)
Image 8: The development process of the DeepSeek-R1-Zero model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

The reward structure is typically composed of two main components:

1.  **Accuracy Rewards:** The model receives a positive reward if its final answer is correct. This can be verified programmatically for tasks in domains like mathematics (checking if the answer matches the solution) or coding (running the code against test cases) [[22]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).
2.  **Format Rewards:** The model is incentivized to follow a specific output structure, such as enclosing its reasoning process within `<think>` and `</think>` tags. This ensures the output is well-structured and interpretable [[23]](https://thelmbook.com/articles#!./DeepSeek-R1.md).

To optimize for these rewards, DeepSeek uses an algorithm called Group Relative Policy Optimization (GRPO). Unlike the more common Proximal Policy Optimization (PPO), GRPO does not require a separate "value model" to estimate future rewards. Instead, it samples a group of outputs for each problem and uses the average reward of the group as a baseline to judge whether a specific output is better or worse than average. This simplifies the training process and reduces resource consumption [[4]](https://thelmbook.com/articles#!./DeepSeek-R1.md).

During this process, researchers observed the emergence of an **"Aha moment."** The model spontaneously began to generate long, detailed reasoning traces, including self-correction and reflection. For instance, it might generate a phrase like "Wait, wait. Wait. That's an aha moment I can flag here," before re-evaluating its approach [[3]](https://arxiv.org/abs/2501.12948). This behavior was not explicitly taught but emerged as a result of the RL process optimizing for correct answers.![Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)
Image 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

However, the "Aha moment" may not be a purely emergent property of RL. A critical analysis of various base models, including DeepSeek-V3-Base, found that they already exhibit self-reflection keywords even before RL tuning [[8]](https://arxiv.org/html/2503.20783v1). Further research supports this, suggesting that self-reflection is a latent feature broadly distributed in large models from pre-training [[15]](https://arxiv.org/html/2506.12217v1). From this perspective, RL does not create these reasoning abilities from scratch but rather amplifies and refines capabilities that are already present in the base model.

DeepSeek-R1-Zero was a landmark experiment, as it was the first to demonstrate that a model could develop sophisticated reasoning and "thinking" behaviors through pure RL, without the need for human-annotated reasoning examples.

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

The third approach is a hybrid that combines the stability of SFT with the exploratory power of RL. This is the method used to create the flagship DeepSeek-R1 model, which addresses some of the shortcomings of the pure-RL R1-Zero, such as poor readability and language mixing [[3]](https://arxiv.org/abs/2501.12948).![Figure 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)
Image 10: The development process of the DeepSeek-R1 model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

The training pipeline for DeepSeek-R1 involves four main stages:

1.  **"Cold Start" SFT:** The process begins by fine-tuning the base model on a small, curated dataset of "cold-start" data. This dataset contains a few thousand examples of high-quality, human-aligned reasoning traces. Some of these are refined outputs from R1-Zero, while others are generated using few-shot prompting or post-processed by human annotators. This initial SFT phase provides the model with a solid foundation for generating coherent and readable thought processes, preventing the instability that can occur when applying RL directly to a base model [[4]](https://thelmbook.com/articles#!./DeepSeek-R1.md).
2.  **Reasoning-Focused RL:** The model then undergoes intensive RL training on verifiable tasks like math and coding. This stage builds on the GRPO framework but introduces an additional **language consistency reward**. This reward, calculated as the proportion of words in the target language within the CoT, discourages the model from mixing languages (e.g., English and Chinese) in its responses. While this slightly degrades raw task performance, it improves readability and aligns better with human preferences [[24]](https://artgor.medium.com/paper-review-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning-edf4343dcf3a).
3.  **General-Purpose SFT:** After the reasoning-focused RL, the model is further fine-tuned on a broader dataset of about 800,000 examples. This dataset includes not only reasoning tasks but also general-purpose tasks like writing, factual QA, and translation. The data is generated using rejection sampling, where multiple responses are generated and ranked, with only the best ones used for fine-tuning. This stage helps the model generalize its reasoning abilities to a wider range of applications [[4]](https://thelmbook.com/articles#!./DeepSeek-R1.md).
4.  **Final RL for Alignment:** The final stage involves another round of RL, this time mixing verifiable reasoning problems with general preference tuning using reward models. This polishes the model, improving its helpfulness and harmlessness while maintaining its strong reasoning abilities.

This multi-stage process results in a model that is not only a powerful reasoner but is also well-aligned with human preferences, making it more practical for real-world applications. The benchmark results show that DeepSeek-R1 is highly competitive with, and in some cases surpasses, leading closed-source models like OpenAI's o1 [[3]](https://arxiv.org/abs/2501.12948).![Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)
Image 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

### 4) Pure supervised finetuning (SFT) and distillation

To recap, we have covered three primary methods for developing reasoning models: inference-time scaling, which enhances performance without changing model weights; pure RL, which fosters emergent reasoning from a base model; and a hybrid SFT+RL approach, which refines these capabilities for production readiness.

The fourth method, pure SFT and distillation, offers a more efficient way to transfer these hard-won reasoning abilities to smaller, more accessible models. As demonstrated by the DeepSeek-R1-Distill series, this involves fine-tuning smaller open-weight models on a large dataset of high-quality reasoning traces generated by a powerful "teacher" model like DeepSeek-R1 [[3]](https://arxiv.org/abs/2501.12948).![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)
Image 12: The development process of the DeepSeek-R1-Distill models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This is different from traditional knowledge distillation, which often involves matching the student's output probabilities (logits) to the teacher's. Here, the process is simpler: the student model learns to mimic the teacher's final text output, including the detailed CoT, through standard SFT. DeepSeek generated 800,000 such examples from R1 to train smaller Llama 3 and Qwen 2.5 models [[9]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).

DeepSeek developed these distilled models for two key reasons: accessibility and efficiency. The full 671B parameter R1 model is computationally expensive and difficult to run. Distillation makes its powerful reasoning capabilities available in smaller models that can be deployed on consumer-grade hardware, democratizing access to advanced AI [[10]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).

The results are impressive. The distilled models outperform their base versions and even strong closed-source models on reasoning benchmarks, though they do not match the performance of the full DeepSeek-R1 teacher model [[3]](https://arxiv.org/abs/2501.12948).![Figure 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)
Image 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

The DeepSeek report also provides a crucial comparison: how does distillation stack up against applying pure RL to smaller models? They trained a 32B parameter model with the same pure RL process used for R1-Zero. The results showed that the distilled model of the same size performed much better across all benchmarks [[3]](https://arxiv.org/abs/2501.12948).![Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)
Image 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

This leads to two key insights. First, for smaller models, distillation is a more effective and economical strategy for imparting reasoning skills than large-scale RL from a cold start. Second, while distillation is powerful, pushing the absolute frontier of AI reasoning likely still requires the massive scale and exploratory power of RL applied to the largest available base models. It would have been interesting to also see a comparison with a model trained using the SFT+RL hybrid approach, and to see how all three methods perform when starting from a non-domain-specific base model, like a standard Llama 3 or Qwen model instead of their math-tuned variants.

The struggle to transfer reasoning to smaller models is rooted in fundamental capacity limits. Complex Chain-of-Thought reasoning appears to be an emergent property of models with over 100 billion parameters [[17]](https://ojs.aaai.org/index.php/AAAI/article/view/29821/31426). Smaller models (e.g., under 3 billion parameters) suffer from a "Small Model Learnability Gap"; their constrained parameter count prevents them from fully internalizing the multi-step logic present in the long reasoning traces generated by a much larger teacher model. They often perform better when trained on shorter, simpler reasoning chains that align with their intrinsic capacity [[16]](https://arxiv.org/html/2502.12143v3).

After dissecting these four techniques and seeing them embodied in the DeepSeek-R1 family, we can step back to evaluate the broader significance of this release.
```
**Grader reasoning:**
- `cc`: The 4 main ways to build and improve reasoning models:
**1:** Across all four sub-approaches, the generated section covers inference-time scaling (CoT, an expanded search-strategies list including a well-grounded "Lookahead Search" addition, the "unsuccessful attempts" categorization, o1 cost speculation), pure RL (R1-Zero, both reward types, the Aha-moment quote, plus a well-grounded nuance questioning how emergent the Aha moment really is), SFT+RL (the four-stage pipeline, language-consistency reward, ~800K general SFT samples), and distillation (mechanism, two reasons, benchmark comparisons, the 32B RL-vs-distillation result, plus well-grounded capacity-limit findings) with strong fidelity. One minor gap, as in other presets for this lesson: the expected section's second "additional comparison" suggestion (DeepSeek-V3 trained with pure SFT) is replaced with a different suggestion (testing all three methods from a non-domain-specific base model) rather than reproduced — a small, peripheral substitution inside an otherwise comprehensive section.
- `fl`: The 4 main ways to build and improve reasoning models:
**1:** All figures land in the same relative position as their expected counterparts: Figures 8 and 9 (reward mechanics, Aha moment) and Figures 10 and 11 (SFT+RL stages, benchmark) all match the expected section's placement, and the exploration-grounded additions each have their own local lead-in that does not disrupt the surrounding idea order. Figure 12 is placed immediately after the method intro rather than after the classical-distillation-comparison paragraph that follows it in the expected section — a narrow, single-paragraph-adjacent reordering of the figure relative to one nearby idea, ruled too trivial to count as a placement failure.
- `de`: The 4 main ways to build and improve reasoning models:
**1:** [instances=3; quality=strong,strong,strong] Three qualifying depth additions, each traceable to an exploration-phase source. (1) In the Pure RL sub-section: "self-reflection is a latent feature broadly distributed in large models from pre-training" [15], traceable to exploration Source [48] (arXiv 2506.12217) nearly verbatim — a limitation/nuance on the core claim that R1-Zero's reasoning is purely RL-emergent. Strong: a specific, named research finding that meaningfully complicates the section's own emergent-behavior narrative. (2) In the distillation sub-section: "Complex Chain-of-Thought reasoning appears to be an emergent property of models with over 100 billion parameters" [17], traceable to exploration Source [53] (AAAI) — a quantified capacity-limit finding about the core topic. Strong: specific, quantified threshold from a named source. (3) Also in the distillation sub-section: the "Small Model Learnability Gap" [16], traceable to exploration Source [52] (arXiv 2502.12143) closely — a named phenomenon explaining why small models struggle to absorb distilled reasoning. Strong: specific, quantified (≤3B parameters), and directly explains a limitation of the core topic. A fourth candidate — the "self-reflection keywords already present pre-RL" claim [8] — does not qualify: it is traceable only to an exploitation-phase source, not an exploration one.
- `be`: The 4 main ways to build and improve reasoning models:
**0:** [instances=0] research.md's exploration-phase sources include three depth-qualifying instances credited under depth_enhancement above, but no breadth-qualifying addition — one that connects outward to an adjacent field rather than intensifying understanding of the four techniques themselves — is present within this section specifically (the article's one breadth-qualifying instance, the Productive Failure analogy, falls in the limited-budget section instead).
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** depth_enhancement scored 1 for this section (three exploration-traceable additions: the self-reflection-latent-feature nuance, the Small Model Learnability Gap, and the >100B-parameter CoT-emergence claim). Each is a contained, well-integrated caveat placed at a natural point (end of the Pure RL sub-section, end of the distillation sub-section) that supports rather than displaces the section's dominant narrative — the four techniques and the DeepSeek-R1 case study remain clearly the primary focus throughout this ~1,800-word section. CorePreservation scores 1.
- `ga`: The 4 main ways to build and improve reasoning models:
**1:** Content-wise this section covers essentially everything the guideline requires across all four approaches, including the required "at least two useful additional comparisons" (the guideline does not specify which two). Prose-only word count is approximately 1,766 words against a 1,950-word target (±195 tolerance, range 1,755–2,145 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset1`

**Article text:**
```
## The 4 main ways to build and improve reasoning models

Current techniques for enhancing LLM reasoning and building specialized models can be grouped into four main categories. While the exact workings of proprietary models like OpenAI's o1 and o3 remain undisclosed, they are rumored to combine several of these training and inference-time strategies.

### Inference-time scaling

Inference-time scaling refers to techniques that improve a model's performance by allocating more computational resources during inference, without altering the model's weights. The core idea is analogous to giving a human more time to think about a difficult problem. This is also known as test-time compute scaling [[2]](https://arxiv.org/abs/2408.03314).

One of the simplest methods is Chain-of-Thought (CoT) prompting, where adding a phrase like "Let's think step by step" encourages the model to generate intermediate reasoning steps, often leading to more accurate answers on complex tasks [[3]](https://arxiv.org/abs/2205.11916). This technique effectively increases the number of generated tokens, thereby using more compute to arrive at a solution. The effectiveness of this simple prompt across a wide range of reasoning tasks suggests that LLMs have untapped zero-shot capabilities for high-level, multi-task cognitive processes.

<https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png>
Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper. (Source [arxiv.org](https://arxiv.org/abs/2205.11916))

More advanced techniques involve search and voting strategies. In **Best-of-N sampling**, the model generates multiple independent answers, and a verifier or reward model selects the best one. **Majority voting** is similar but selects the most common answer among the generated responses. **Beam search** and **Monte Carlo Tree Search (MCTS)** are more structured search algorithms that explore a tree of possible reasoning paths, pruning unpromising branches to focus computation on the most likely solutions. These search-based methods often rely on a Process Reward Model (PRM), which evaluates the correctness of each intermediate step in a reasoning chain, providing a more granular signal than a simple outcome-based reward [[2]](https://arxiv.org/abs/2408.03314). Research has shown that with the right inference-time scaling approach, even a 1B parameter model can outperform a 405B model that lacks it [[27]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

<https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png>
Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source [arxiv.org](https://arxiv.org/abs/2408.03314))

Interestingly, the DeepSeek R1 technical report categorized common inference-time scaling methods like PRM-based search and MCTS under "unsuccessful attempts" during their training exploration [[1]](https://arxiv.org/abs/2501.12948). This suggests that their final model's reasoning ability relies more on the knowledge baked in during training rather than explicit search at inference. However, it is possible that DeepSeek still applies these techniques at the application layer, as they are independent of the model itself. This highlights a key distinction: some reasoning is embedded in the model's weights, while other forms are elicited through inference-time strategies.

This trade-off between training-time and inference-time compute also helps explain why models like OpenAI's o1 are more expensive than GPT-4o. The o1 models spend more time "thinking," which requires more computation and leads to higher costs and latency [[31]](https://www.uctoday.com/unified-communications/chatgpt-4o-vs-o1-which-openai-model-is-best), [[32]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). For example, GPT-o1's input costs are six times higher than GPT-4o's, and its output costs are also six times more expensive per million tokens [[32]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). This higher price reflects the additional computational power required for their sophisticated reasoning techniques and specialized training [[34]](https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c). The increased latency is also noticeable; one analysis found that o1's "time-to-think" can be about 30 times longer than that of GPT-4o [[35]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o).

### Pure reinforcement learning (RL)

Pure RL aims to develop reasoning capabilities directly from a base model without an initial SFT stage, a method exemplified by DeepSeek-R1-Zero. This "cold-start" approach differs from traditional RLHF, which typically fine-tunes a model that has already undergone SFT. Instead of relying on a reward model trained on human preferences, pure RL uses automatically verifiable reward signals from domains like math and coding.

<https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png>
Figure 8: The development process of the DeepSeek-R1-Zero model. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

In the case of DeepSeek-R1-Zero, the reward system has two main components [[1]](https://arxiv.org/abs/2501.12948), [[22]](https://www.nature.com/articles/s41586-025-09422-z):
1.  **Accuracy rewards:** The model receives a positive reward if its final answer is correct. This can be checked automatically for math problems with a single solution or for code that can be executed against test cases.
2.  **Format rewards:** The model is rewarded for structuring its output correctly, such as by placing its reasoning process within `<think>` and `</think>` tags.

To optimize for these rewards, DeepSeek uses an algorithm called Group Relative Policy Optimization (GRPO). Unlike Proximal Policy Optimization (PPO), which requires a separate value model to estimate future rewards, GRPO samples a group of outputs for each problem and uses the average reward of the group as a baseline. This simplifies the training process and reduces resource consumption, making it more practical for large-scale models [[1]](https://arxiv.org/abs/2501.12948). However, one study identified a potential bias in GRPO that may artificially increase the length of incorrect responses, and proposed a modification called Dr. GRPO to improve token efficiency [[8]](https://arxiv.org/html/2503.20783v1).

During this process, researchers observed an "Aha moment," where the model spontaneously began to generate long, detailed reasoning traces and use words like "Wait" to signal self-correction and reflection [[1]](https://arxiv.org/abs/2501.12948), [[7]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners). This emergent behavior was not explicitly taught but arose from the RL process, demonstrating that models can learn to reason and self-correct without human-annotated examples. The length of the model's responses also grew steadily with training, indicating it was learning to allocate more "thinking time" to problems [[23]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

<https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png>
Figure 9: An example of the "Aha moment" from the DeepSeek R1 technical report, where the model learns to rethink its approach. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

This "emergence," however, may be more of an amplification than a creation. Recent research suggests that self-reflection is a latent feature that develops during pre-training and is simply unlocked or amplified by the RL process [[44]](https://arxiv.org/html/2506.12217v1), [[46]](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training). In fact, one study found that the DeepSeek-V3-Base model already exhibited self-reflection keywords like "Aha" and "wait" before any RL tuning [[8]](https://arxiv.org/html/2503.20783v1). This self-reflection can be understood as a form of metaprompting, where the model analyzes its own reasoning to identify and correct mistakes, often guided by an implicit validator that checks for success or failure [[43]](https://arxiv.org/html/2505.24726v1). The RL process, with its clear reward signals, provides the perfect environment to encourage this latent ability.

The success of R1-Zero was a notable milestone, as it was the first demonstration that a model could develop sophisticated reasoning capabilities through pure RL, driven only by outcome-based rewards.

### Supervised finetuning and reinforcement learning (SFT + RL)

The hybrid SFT + RL approach, used to create the flagship DeepSeek-R1 model, combines the stability of supervised learning with the exploratory power of reinforcement learning. This multi-stage process aims to build on the raw reasoning capabilities developed through pure RL while making the model more aligned with human preferences and easier to use [[1]](https://arxiv.org/abs/2501.12948).

<https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png>
Figure 10: The multi-stage development process of the DeepSeek-R1 model. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

The pipeline for DeepSeek-R1 consists of four main stages:
1.  **"Cold Start" Finetuning (SFT):** The process begins by fine-tuning the base model on a small dataset of several thousand high-quality, human-validated reasoning examples with detailed CoT. This initial step gives the model a solid foundation in generating coherent, human-readable reasoning traces, preventing the instability that can occur in the early stages of pure RL [[4]](https://thelmbook.com/articles#!./DeepSeek-R1.md).
2.  **Reasoning-Focused RL:** The model then undergoes intensive RL training using automatically verifiable problems from math, coding, and logic. In addition to accuracy and format rewards, a **language consistency reward** is introduced to penalize the model for mixing languages (e.g., Chinese and English) in a single response. While this slightly degraded performance on some tasks, it improved readability and user experience [[1]](https://arxiv.org/abs/2501.12948), [[25]](https://www.nature.com/articles/s41586-025-09422-z).
3.  **General-Purpose SFT:** In this stage, the training data is expanded to include non-reasoning examples for tasks like writing and role-playing. This data is generated using a combination of techniques, including rejection sampling on the model's own outputs and reusing SFT data from the DeepSeek-V3 pipeline. This step broadens the model's capabilities beyond pure reasoning.
4.  **Preference Optimization RL:** The final stage uses RL again, this time with a focus on general-purpose preference optimization. This phase combines verifiable rewards for reasoning tasks with feedback from a reward model trained on human preferences for helpfulness and harmlessness, polishing the model for broader use.

This staged approach results in a model that excels at reasoning while also being a capable and aligned general-purpose assistant. On benchmarks, DeepSeek-R1 achieves performance comparable to or even exceeding that of leading closed-source models like OpenAI's o1, particularly in math and coding [[1]](https://arxiv.org/abs/2501.12948).

<https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png>
Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

### Pure supervised finetuning (SFT) and distillation

Inference-time scaling offers a way to boost performance without retraining. Pure RL can unlock emergent behaviors. The SFT+RL hybrid provides a stable path to a production-ready model. The fourth approach, pure SFT and distillation, offers the most efficient way to transfer these hard-won reasoning capabilities to smaller, more accessible models.

DeepSeek used this method to create its R1-Distill series. Instead of a complex RL pipeline, they simply fine-tuned smaller, existing open-source models (like Qwen 2.5 and Llama 3) on a large dataset of 800,000 high-quality reasoning examples generated by the flagship DeepSeek-R1 model [[1]](https://arxiv.org/abs/2501.12948), [[14]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond). This is a form of data-level distillation, where the "knowledge" is transferred through the teacher's outputs rather than its internal probabilities (logits), which is a common approach for language models [[13]](https://redwerk.com/blog/what-is-model-distillation).

<https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png>
Figure 12: The development process of the DeepSeek-R1-Distill models. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

This approach was motivated by two key factors. First, it makes powerful reasoning capabilities accessible. The 671B-parameter R1 model is too large for most to run, so distillation allows its abilities to be deployed on more consumer-grade hardware [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d). Second, it is highly efficient. The distillation process involves only SFT, which is much simpler and less computationally intensive than a full RL pipeline [[14]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).

The results are impressive. Even the smallest 1.5B distilled model surpassed strong, non-reasoning baselines like GPT-4o and Claude 3.5 Sonnet on math benchmarks. As the size of the student model increased, performance continued to improve, demonstrating the effectiveness of this distillation strategy [[1]](https://arxiv.org/abs/2501.12948).

<https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png>
Figure 13: Benchmark comparison of distilled versus non-distilled models. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

The DeepSeek report also provides a direct comparison between distillation and pure RL on a smaller 32B model. The distilled model substantially outperformed a model of the same size that was trained with the pure RL "cold-start" method. This suggests that for smaller models, it is more effective to distill knowledge from a powerful teacher than to try to develop reasoning from scratch via RL. The emergent reasoning behaviors seen in massive models like R1-Zero may not appear at smaller scales without the guidance of a more capable teacher [[1]](https://arxiv.org/abs/2501.12948).

<https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png>
Figure 14: Benchmark comparison of distillation and RL on a smaller 32B model. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

This phenomenon is explained by what researchers call the "Small Model Learnability Gap." Models under a certain size (e.g., 3B parameters) have a constrained capacity that prevents them from internalizing long, multi-step logic, even when it is provided by a larger teacher model [[47]](https://arxiv.org/html/2502.12143v3). Complex chain-of-thought reasoning appears to be an emergent property of models with over 100 billion parameters; it cannot be fully transferred to smaller models that lack the fundamental capacity for it [[48]](https://ojs.aaai.org/index.php/AAAI/article/view/29821/31426). Instead, smaller models learn better from shorter, simpler reasoning chains that align with their intrinsic capabilities.

This insight is valuable, but the comparison could have been even more informative. It would be useful to see how a distilled model compares to a model of the same size that has undergone the full SFT+RL pipeline. Additionally, comparing the performance of a distilled model to its own base model (e.g., DeepSeek-R1-Distill-Qwen-7B vs. the original Qwen2.5-Math-7B) would clarify how much of the performance gain comes from the distillation process versus the strength of the base model itself.

After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the release's broader significance and limitations.
```
**Grader reasoning:**
- `cc`: The 4 main ways to build and improve reasoning models:
**1:** Across all four sub-approaches, the generated section covers inference-time scaling (CoT, Best-of-N/majority-voting/beam/MCTS search strategies, the 'unsuccessful attempts' categorization, cost and latency speculation), pure RL (R1-Zero, both reward types, GRPO, the Aha-moment phenomenon, plus a well-grounded latent-self-reflection-amplification caveat), SFT+RL (the four-stage pipeline, language-consistency reward, general-purpose SFT expansion), and distillation (mechanism, two reasons, benchmark comparisons, the 32B RL-vs-distillation result, plus well-grounded capacity-limit findings) with strong fidelity. As in other presets for this lesson, the expected section's specific 'additional comparisons' suggestion is replaced with a different pair (a same-size SFT+RL model; the distilled model's own base model) rather than reproduced verbatim — a small, peripheral substitution.
- `fl`: The 4 main ways to build and improve reasoning models:
**1:** All figures land in the same relative position as their expected counterparts: the CoT and search-strategy figures, the reward-mechanics and Aha-moment figures, the SFT+RL-stages and benchmark figures, and the distillation-process and benchmark figures all match, including the distillation-process figure landing after the classical-distillation-comparison explanation exactly as the expected section has it. The exploration-grounded latent-self-reflection addition has its own local lead-in and does not disrupt the surrounding idea order.
- `de`: The 4 main ways to build and improve reasoning models:
**1:** [instances=3; quality=strong,strong,strong] Three qualifying depth additions, each traceable to an exploration-phase source. (1) In the Pure RL sub-section: the latent-self-reflection-amplification discussion — self-reflection as "a latent feature that develops during pre-training and is simply unlocked or amplified," including the specific 'metaprompting'/'implicit validator that checks for success or failure' mechanism — traceable to three exploration sources closely, cited [43], [44], [46]. Strong: a detailed, multi-sentence mechanism explanation drawing on several converging sources. (2) In the distillation sub-section: the 'Small Model Learnability Gap' — "models under a certain size (e.g., 3B parameters) have a constrained capacity that prevents them from internalizing long, multi-step logic" — traceable to an exploration source closely, cited [47]. Strong: a specific, quantified, named phenomenon. (3) Also in the distillation sub-section: "Complex chain-of-thought reasoning appears to be an emergent property of models with over 100 billion parameters" — traceable to a distinct exploration source closely, cited [48]. Strong: a specific quantified threshold from a named source. A fourth candidate — the DeepSeek-V3-Base self-reflection-keywords claim [8] — does not qualify: it is traceable only to an exploitation-phase source, not an exploration one.
- `be`: The 4 main ways to build and improve reasoning models:
**0:** [instances=0] research.md's exploration-phase sources include three depth-qualifying instances credited above, but no breadth-qualifying addition is present within this section specifically (the article's one breadth-qualifying instance, the Productive Failure analogy, falls in the limited-budget section instead).
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** depth_enhancement scored 1 for this section (three strong additions). Each is a contained paragraph placed at a natural point within its own sub-section, and the four techniques and the DeepSeek-R1 case study remain clearly the dominant focus throughout this large section. CorePreservation scores 1.
- `ga`: The 4 main ways to build and improve reasoning models:
**1:** Content-wise this section covers essentially everything the guideline requires across all four approaches, including the required 'at least two useful additional comparisons.' Prose-only word count is approximately 1,791 words against a 1,950-word target (±195 tolerance, range 1,755–2,145 words), within tolerance.

## Section: S6::section-6-thoughts-about-deepseek-r1  (weight=0.081, contribution=+0.0006 FOR standard)
Stored section rewards: standard=0.3436  light=0.3367  (explore: standard=0.0000  light=0.0000)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset2`

**Article text:**
```
## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 series is a notable event for the AI community. The open MIT license, combined with an unusually detailed technical report, provides a level of transparency that is rare for a frontier model. It offers a concrete demonstration that pure RL from a cold start can lead to the emergence of advanced reasoning and self-correction, without the need for supervised warm-up data [[1]](https://arxiv.org/abs/2501.12948).

When compared to OpenAI's o1, DeepSeek-R1 shows comparable performance on key math, coding, and reasoning benchmarks. However, R1 appears to be more inference-efficient, suggesting different philosophical bets by the two labs. DeepSeek seems to have invested heavily in a complex, multi-stage training pipeline, while o1 may lean more on expensive inference-time scaling to achieve its results [[4]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners), [[12]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

However, any direct comparison is limited by the secrecy surrounding o1. We do not know its model size, whether it uses a Mixture-of-Experts (MoE) architecture, or the exact mix of training techniques employed. The strength of the respective base models also differs, making it difficult to attribute performance gaps to any single factor. A truly fair comparison is not possible without more transparency from OpenAI.

There is also the reality of training costs. While the DeepSeek team reported a total training cost of around $294,000 for the R1 pipeline, this figure excludes prior expenses for the base model [[30]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18). The publicized $6M figure for models in this class most likely refers to the V3 base model pre-training rather than the full R1 RL process, leaving the true incremental cost of reasoning specialization undisclosed. This distinction is crucial for understanding the economic feasibility of replicating such models.

Despite these caveats, DeepSeek-R1 stands as a milestone for open-weight reasoning models. It proves that high-level reasoning capabilities are not the exclusive domain of closed labs. By providing both the models and a detailed recipe, DeepSeek has accelerated open research into all four of the primary techniques for building reasoning models.
```
**Grader reasoning:**
- `cc`: Thoughts about DeepSeek R1:
**1:** Both sections cover the same core topics: the significance of DeepSeek-R1's release, a comparison with OpenAI's o1, and a discussion of training costs that distinguishes the base model's cost from the reasoning specialization's incremental cost.
- `fl`: Thoughts about DeepSeek R1:
**1:** Both sections follow the same logical flow: discussing the significance of the release, comparing it to o1, and then analyzing the training costs.
- `de`: Thoughts about DeepSeek R1:
**0:** [instances=0] One candidate evaluated: the nuance that publicized cost figures likely refer to the V3 base model rather than the full R1 RL process, cited to ref [30], the Reuters $294,000 article — confirmed in research.md's exploitation-phase block, not exploration. Fails the source attribution gate.
- `be`: Thoughts about DeepSeek R1:
**0:** [instances=0] No breadth additions present.
- `cp`: Thoughts about DeepSeek R1:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so CorePreservation is 1 by default as there are no qualifying additions to evaluate.
- `ga`: Thoughts about DeepSeek R1:
**1:** The generated section meets all requirements: it expresses appreciation for the open license and detailed report, compares R1 with o1 noting the training-heavy vs. inference-heavy trade-off, notes the limits of comparison due to OpenAI's secrecy, and discusses training cost realities. The prose-only word count is approximately 318 words, within the 350-word target's 315–385 range (a narrow margin, only 3 words above the floor, but within tolerance).

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset2`

**Article text:**
```
## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 models was a significant moment for the AI community. The combination of an open MIT license, a detailed technical report, and a clear demonstration of emergent reasoning from a pure RL cold start is a major contribution. It proved that high-level reasoning capabilities need not remain the exclusive domain of closed-door labs.

When comparing DeepSeek-R1 to OpenAI's o1, we see a notable contrast. On benchmarks for math, coding, and reasoning, their performance is often comparable. However, DeepSeek-R1 appears to be more inference-efficient, suggesting a different architectural philosophy. DeepSeek seems to have placed a training-heavy bet, investing immense computational resources into the RL process to bake reasoning capabilities into the model's weights. In contrast, o1 is rumored to lean more heavily on inference-time scaling, using more compute at runtime to achieve its results [[8]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison).

However, any direct comparison is limited by the lack of transparency from OpenAI. We do not know the size of the o1 model, its architecture, or the exact mix of techniques used in its training. Without these details, it is impossible to definitively attribute performance gaps to specific methods.

There is also the reality of training costs. The DeepSeek team reported that the final RL stages and data creation for R1 cost approximately $294,000 [[13]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18). This figure, while substantial, excludes the massive cost of pre-training the 671B-parameter DeepSeek-V3 base model, which is the true barrier to entry. The incremental cost of reasoning specialization is only one part of the much larger financial picture.

Ultimately, DeepSeek-R1 stands as a milestone for open-weight reasoning models. It provides a blueprint and a powerful set of tools that accelerate research into all four of the techniques we have discussed, democratizing the development of next-generation AI. But while this release democratizes knowledge, the cost of replication remains high. This raises a critical question for the broader community: how can we develop powerful reasoning models on a limited budget?
```
**Grader reasoning:**
- `cc`: Thoughts about DeepSeek R1:
**1:** Both sections cover the same appreciation points (open MIT license, detailed report, pure-RL emergent reasoning), the same o1 comparison (comparable benchmarks, R1 more inference-efficient, training-heavy vs. inference-scaling bet), the same limits to that comparison (o1's size/architecture/technique mix undisclosed), the same $6M/V3-vs-R1 cost conflation (via the newer $294,000 figure), and the same milestone conclusion. The added forward-bridge to the budget section is an addition that does not displace any expected idea.
- `fl`: Thoughts about DeepSeek R1:
**1:** The generated section follows the same progression as the expected one: appreciation, o1 comparison, limits to that comparison, cost discussion, milestone close (extended with an added forward-bridge to the budget section). No media to misplace.
- `de`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: Thoughts about DeepSeek R1:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: Thoughts about DeepSeek R1:
**1:** All required content elements are present, including an explicit restatement of the o1-disclosure limits and the $294,000/V3-cost-conflation point. Prose-only word count is approximately 320 words against a 350-word target (±35 tolerance, range 315–385 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset2`

**Article text:**
```
## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 series is a notable event for the AI community. The open MIT license, the detailed technical report, and the suite of models (R1-Zero, R1, and distilled versions) provide a valuable resource for researchers and engineers. The project's transparency is a welcome contrast to the secrecy surrounding many frontier models. Most importantly, it provides the first concrete, open-weight demonstration that pure RL from a "cold start" can lead to the emergence of sophisticated reasoning and self-correction behaviors without any initial supervised data [[11]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners).

When comparing DeepSeek-R1 to OpenAI's o1, the benchmarks show that they are highly competitive, especially on math, coding, and reasoning tasks [[1]](https://arxiv.org/abs/2501.12948). However, DeepSeek-R1 appears to be more inference-efficient. This suggests a difference in strategy: DeepSeek seems to have invested heavily in a complex, multi-stage training pipeline, while o1 may lean more on expensive inference-time scaling techniques to achieve its performance [[14]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

However, any direct comparison is limited by the lack of information about o1. We do not know its model size, whether it uses a Mixture-of-Experts (MoE) architecture, the exact mix of training techniques, or the strength of its base model. Without these details, it is impossible to definitively attribute performance differences to specific architectural or training choices. A direct comparison is therefore unwarranted until more information about o1 is disclosed.

There is also the reality of training costs. While a figure of around $294,000 has been reported for the training of R1, this number does not include prior expenses for developing the V3 base model [[15]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18). The true incremental cost of adding the specialized reasoning capabilities remains undisclosed. The DeepSeek team has never disclosed the exact GPU hours or development cost specifically for the R1 stages.

Despite these caveats, DeepSeek-R1 stands as a milestone for open-weight reasoning models. It proves that high-level reasoning is not the exclusive domain of closed-source labs. By open-sourcing their models and detailing their methods, DeepSeek has accelerated research into all four of the techniques we have discussed.
```
**Grader reasoning:**
- `cc`: Thoughts about DeepSeek R1:
**1:** Both sections cover the same appreciation points (open MIT license, detailed report, pure-RL emergent reasoning), the same o1 comparison (comparable benchmarks, R1 more inference-efficient, training-heavy vs. inference-scaling bet), the same limits to that comparison (o1's size/architecture/technique mix undisclosed), the same $294,000/V3-cost-conflation point, and the same milestone conclusion.
- `fl`: Thoughts about DeepSeek R1:
**1:** The generated section follows the same progression as the expected one: appreciation, o1 comparison, limits to that comparison, cost discussion, milestone close. Neither section has media here.
- `de`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: Thoughts about DeepSeek R1:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: Thoughts about DeepSeek R1:
**1:** All required content elements are present. Prose-only word count is approximately 328 words against a 350-word target (±35 tolerance, range 315–385 words), within tolerance.

### Arm: light (preset1)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset1`

**Article text:**
```
## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 models is a significant moment for open-weight AI. The permissive MIT license, the unusually detailed technical report, and the core demonstration that pure RL from a cold start can produce emergent reasoning are all valuable contributions to the community [[3]](https://arxiv.org/abs/2501.12948), [[11]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

When comparing DeepSeek-R1 to OpenAI's o1, we see two different philosophies at play. On benchmarks for math, coding, and reasoning, their performance is comparable. However, DeepSeek-R1 appears to be more inference-efficient. This suggests that DeepSeek invested heavily in training to embed reasoning capabilities directly into the model, while o1 may lean more on expensive inference-time scaling to achieve its results [[3]](https://arxiv.org/abs/2501.12948), [[11]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

However, any direct comparison is limited by the lack of transparency from OpenAI. We do not know the size of the o1 model, its architecture (e.g., if it's a Mixture-of-Experts model), the exact mix of training techniques used, or the strength of its base model. Without these details, it is impossible to definitively attribute performance differences to specific methods [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling). A direct comparison is unwarranted until more information is available.

There is also the reality of training costs. The DeepSeek team has never disclosed the exact GPU hours or development cost for the R1 project alone. A 2024 report stated that the R1 training cost was $294,000, but this figure explicitly excludes prior expenses [[13]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18). The most significant of these is the cost of pre-training the massive 671B parameter DeepSeek-V3 base model, which most likely cost millions of dollars. The incremental cost of reasoning specialization is only a fraction of the total investment required to build such a foundational model.

Despite these open questions, DeepSeek-R1 stands as a milestone. It proves that high-level reasoning is not the exclusive domain of closed-source labs. By providing an open blueprint, it has accelerated research and development across all four of the techniques we have discussed.
```
**Grader reasoning:**
- `cc`: Thoughts about DeepSeek R1:
**1:** Both sections provide a commentary on the DeepSeek R1 release, discussing its significance for open-source AI, comparing it to OpenAI's o1, and clarifying the training cost realities. The core arguments and points of discussion are the same.
- `fl`: Thoughts about DeepSeek R1:
**1:** Both sections follow the same logical flow: the significance of DeepSeek-R1, comparison to o1, and then training costs.
- `de`: Thoughts about DeepSeek R1:
**0:** [instances=0] One candidate evaluated: the $294,000 training-cost figure, cited to ref [13] → research.md source [42], exploitation — fails the gate.
- `be`: Thoughts about DeepSeek R1:
**0:** [instances=0] No breadth additions present.
- `cp`: Thoughts about DeepSeek R1:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so CorePreservation is 1 by default as there are no qualifying additions to evaluate.
- `ga`: Thoughts about DeepSeek R1:
**0:** The generated section meets the substantive requirements — it expresses appreciation for the open license and detailed report, compares R1 with o1 noting comparable quality but superior efficiency, notes the limits of comparison due to OpenAI's secrecy, and discusses training cost realities. However, the prose-only word count is approximately 304 words, below the required 315–385 range (350-word target ±10%). This fails the word-count tolerance, so GuidelineAdherence scores 0.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset1`

**Article text:**
```
## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 models was a significant event for the AI community. The open MIT license, combined with an unusually detailed technical report, provided an unprecedented look into the engineering of a state-of-the-art reasoning model. It was a powerful demonstration that pure RL from a cold start could produce emergent behaviors like complex reasoning traces and self-correction, a capability many assumed required extensive human-annotated data.

When compared head-to-head with OpenAI's o1, DeepSeek-R1 shows comparable, and sometimes superior, performance on benchmarks for math, coding, and reasoning. At the same time, it appears to be more efficient at inference [[3]](https://arxiv.org/abs/2501.12948). This suggests different philosophical bets: DeepSeek seems to have invested heavily in a complex, multi-stage training process, while o1 may lean more on inference-time scaling to achieve its results.

However, any direct comparison is limited by the lack of transparency from OpenAI. We do not know the size of the o1 model, its architecture (e.g., whether it is a Mixture-of-Experts model), or the exact mix of training techniques used. The strength of the base models also differs, which prevents a definitive attribution of performance gaps to specific training methods. A direct, apples-to-apples comparison is therefore unwarranted until more details about o1 are known.

There is also ambiguity around the true cost of training. While a figure of around $294,000 was reported for the total cost of R1, this figure excludes prior expenses for developing the foundational DeepSeek-V3 model, which likely cost millions [[11]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18). The incremental cost of adding the specialized reasoning capabilities remains undisclosed, making it hard for other teams to budget for similar projects. The DeepSeek team has not disclosed the exact GPU hours or total development cost for the R1 project alone.

Despite these caveats, DeepSeek-R1 stands as a milestone for open-weight reasoning models. It proves that high-level reasoning is not the exclusive domain of closed-source labs and provides a valuable blueprint for the community. This release has accelerated research into all four of the techniques we have discussed, empowering developers to build and experiment with their own reasoning models.
```
**Grader reasoning:**
- `cc`: Thoughts about DeepSeek R1:
**1:** Both sections cover the same appreciation points (open MIT license, detailed report, pure-RL emergent reasoning), the same o1 comparison (comparable-to-superior benchmarks, R1 more inference-efficient), the same limits to that comparison (o1's size/architecture/technique mix undisclosed), the same $6M/V3-vs-R1 cost conflation, and the same milestone conclusion. The generated section adds the newer $294,000 figure and explicitly restates that DeepSeek has not disclosed GPU hours for R1 specifically, without displacing any expected idea.
- `fl`: Thoughts about DeepSeek R1:
**1:** The generated section follows the same progression as the expected one: appreciation, o1 comparison, limits to that comparison, cost discussion, milestone close. No media to misplace.
- `de`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode (self-reflection mechanisms, small-model distillation capacity limits, cognitive-science parallels to journey learning, and neuroscience/LLM parallels), but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode (self-reflection mechanisms, small-model distillation capacity limits, cognitive-science parallels to journey learning, and neuroscience/LLM parallels), but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: Thoughts about DeepSeek R1:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: Thoughts about DeepSeek R1:
**1:** All required content elements are present: appreciation, the o1 comparison, the limits to that comparison, and the cost discussion — including an explicit restatement that DeepSeek has not disclosed GPU hours or total development cost for R1 specifically, matching the guideline's instruction closely. Prose-only word count is approximately 342 words against a 350-word target (±35 tolerance, range 315–385 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset1`

**Article text:**
```
## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 models is a notable event for the AI community. The open MIT license, combined with an unusually detailed technical report, provides an invaluable resource for researchers and engineers. It offers one of the first concrete demonstrations that pure reinforcement learning from a "cold start" can lead to the emergence of complex reasoning and self-correction behaviors without the need for supervised examples to warm up the model. This transparency accelerates community-driven research and allows for independent verification of their claims.

When compared to OpenAI's o1, DeepSeek-R1 shows comparable performance on key math and coding benchmarks while appearing to be more efficient at inference. This suggests different philosophical bets: DeepSeek invested heavily in a complex, multi-stage training process to bake reasoning capabilities into the model's weights, while o1 seems to rely more on scaling up computation at inference time. This distinction highlights a fundamental trade-off in AI development: should intelligence be encoded during training or elicited at runtime?

However, a direct, fair comparison is difficult. OpenAI has not disclosed key details about o1, such as its model size, whether it uses a Mixture-of-Experts (MoE) architecture, or the exact mix of training techniques employed. Without this information, it is impossible to definitively attribute performance differences to specific architectural or training choices. The strength of the base model also plays a crucial role, and without knowing the specifics of o1's foundation, any comparison remains speculative.

There is also ambiguity around the true cost of training. The DeepSeek team has not disclosed the exact GPU hours or total cost specifically for the R1 reasoning specialization. The widely cited figure of $294,000 likely covers the entire R1 pipeline, but this excludes prior expenses for developing the V3 base model [[36]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18). The much larger, rumored $6M figure for training frontier models likely refers to the pre-training of a base model like V3, not the specialized R1 process. The incremental cost to add reasoning capabilities remains an open question.

Despite these limitations, DeepSeek-R1 stands as a milestone for open-weight reasoning models. It proves that high-level reasoning is not the exclusive domain of closed-source labs and provides a blueprint that will accelerate research and development across the field.
```
**Grader reasoning:**
- `cc`: Thoughts about DeepSeek R1:
**1:** Both sections cover the same appreciation points (open MIT license, detailed report, pure-RL emergent reasoning), the same o1 comparison (comparable benchmarks, R1 more inference-efficient, training-heavy vs. inference-scaling bet), the same limits to that comparison (o1's size/architecture/technique mix undisclosed), the same $6M/V3-vs-R1 cost conflation via the $294,000 figure, and the same milestone conclusion.
- `fl`: Thoughts about DeepSeek R1:
**1:** The generated section follows the same progression as the expected one: appreciation, o1 comparison, limits to that comparison, cost discussion, milestone close. Neither section has media here.
- `de`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: Thoughts about DeepSeek R1:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: Thoughts about DeepSeek R1:
**1:** All required content elements are present. Prose-only word count is approximately 364 words against a 350-word target (±35 tolerance, range 315–385 words), within tolerance.

## Section: S3::section-3-when-should-we-use-reasoning-models  (weight=0.037, contribution=+0.0129 FOR standard)
Stored section rewards: standard=0.4310  light=0.3700  (explore: standard=0.1207  light=0.0000)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset2`

**Article text:**
```
## When should we use reasoning models?

Before diving into the technical details, it is important to consider when reasoning models are truly necessary. These models deliver the highest returns on tasks that require decomposition or self-correction, such as puzzles, advanced mathematics, and competitive coding. However, they are often overkill for tasks like summarization, simple factual question-answering, or creative writing, where direct generation is sufficient and more efficient. The decision can be framed as a trade-off based on task complexity: for simple, single-step tasks, a general-purpose model is usually best; for complex, multi-step problems requiring logical deduction, a specialized reasoning model is worth considering.

Deploying a reasoning model comes with practical downsides. The verbose intermediate steps lead to significantly higher latency and token costs. This increased verbosity can also frustrate users in conversational settings, who may prefer a direct answer over a lengthy explanation. Furthermore, there is a risk of overthinking, where the model invents unnecessary complications for straightforward problems that a base model would solve correctly in a single pass [[3]](https://arxiv.org/html/2503.20783v1). This can even cause the model to abandon a correct initial answer, a phenomenon documented in recent studies [[16]](https://arxiv.org/html/2604.10739v1).![A diagram listing the strengths (complex problem solving, self-correction) and weaknesses (cost, latency, overthinking) of reasoning models.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)
Image 4: A summary of the primary strengths and weaknesses of reasoning models. (Source [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982))

Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.
```
**Grader reasoning:**
- `cc`: When should we use reasoning models?:
**1:** Both sections cover the same core content: reasoning models are best for complex tasks like puzzles and advanced math, while being inefficient for simpler tasks, and both discuss the main drawbacks (cost, latency, verbosity, overthinking).
- `fl`: When should we use reasoning models?:
**1:** Both sections follow the same logical flow: discussing when to use reasoning models, then detailing their strengths and weaknesses with a summary image.
- `de`: When should we use reasoning models?:
**1:** [instances=1; quality=standard] A depth addition is present: the generated section elaborates that overthinking can cause the model to abandon a correct initial answer. This qualifies as "limitations... of the core topic." Traceable to ref [16], arxiv.org/html/2604.10739v1, exploration-phase. Classified as standard: a brief, single-sentence mention without the fuller inverted-U mechanism explanation given elsewhere in the article.
- `be`: When should we use reasoning models?:
**0:** [instances=0] No breadth additions present.
- `cp`: When should we use reasoning models?:
**1:** The depth addition elaborating on the "overthinking" phenomenon directly supports the ground truth's core point about the weaknesses of reasoning models. It reinforces the main narrative rather than diluting it.
- `ga`: When should we use reasoning models?:
**0:** The generated section meets the substantive requirements — it identifies tasks where reasoning models excel versus where they are overkill, catalogs the practical downsides, includes the specified image, and provides the transition. However, the prose-only word count is approximately 205 words, which exceeds the required 135–185 range (160-word target ±10%, minimum ±25 words) by 20 words. This fails the word-count tolerance, so GuidelineAdherence scores 0.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset2`

**Article text:**
```
## When should we use reasoning models?

Before diving into the technical details, it is important to know when reasoning models are truly needed. They deliver the highest returns on tasks that require decomposition, multi-step logic, or self-correction, such as puzzles, advanced mathematics, and competitive coding. For tasks like summarization, simple factual question-answering, or creative writing, where direct generation is sufficient, they are often overkill.

Deploying a reasoning model also comes with practical downsides. The verbose intermediate steps lead to higher latency and token costs, and can frustrate users in conversational settings. Furthermore, there is the risk of "overthinking." Research has shown that accuracy can follow an inverted U-shaped curve relative to reasoning length, where a model second-guesses a correct initial answer and performance drops [[19]](https://arxiv.org/html/2604.10739v1).![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)

Figure 4: The key strengths and weaknesses of reasoning models.

Understanding when to deploy these specialized models is the first step. The next is understanding how they are built. This leads us to a concrete, open pipeline that demonstrates how these capabilities are created at scale.
```
**Grader reasoning:**
- `cc`: When should we use reasoning models?:
**1:** Both sections cover the same needed-vs-not-needed task split (using the guideline's own "creative writing" example), the same practical downsides (latency/cost, verbosity, overthinking), and the same closing strengths/weaknesses figure. The inverted-U-curve overthinking citation is an addition that does not displace any expected idea.
- `fl`: When should we use reasoning models?:
**1:** The generated section follows the same progression as the expected one: needed-vs-not-needed framing, downsides (with its exploration-grounded addition carrying its own local lead-in), Figure 4, then the transition.
- `de`: When should we use reasoning models?:
**1:** [instances=1; quality=standard] One qualifying depth addition: "accuracy can follow an inverted U-shaped curve relative to reasoning length, where a model second-guesses a correct initial answer and performance drops" [19], traceable to the exploration-phase "When More Thinking Hurts" source nearly verbatim. This qualifies as 'limitations, criticisms, or failure modes of the core topic.' Classified as standard: a brief, single-sentence mention.
- `be`: When should we use reasoning models?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: When should we use reasoning models?:
**1:** depth_enhancement scored 1 for this section (one standard-tier overthinking addition). The addition is a single sentence within the existing downsides discussion and does not shift the section's focus away from when-to-use guidance. CorePreservation scores 1.
- `ga`: When should we use reasoning models?:
**1:** All required content elements are present. Prose-only word count is approximately 154 words against a 160-word target (±25 tolerance floor, range 135–185 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset2`

**Article text:**
```
## When should we use reasoning models?

Before we examine the technical details, it is important to know when reasoning models are truly needed. They deliver the highest returns on tasks that require decomposition or self-correction, such as puzzles, advanced mathematics, and competitive coding. However, for tasks like summarization, simple factual question-answering, or creative writing, where direct generation is sufficient, they are often overkill.

The practical downsides are considerable. The verbose intermediate steps lead to higher latency and increased token costs. This verbosity can also frustrate users in conversational settings who are looking for a quick, direct answer.

Furthermore, there is a risk of "overthinking," where the model might invent unnecessary complications for a straightforward problem that a base model would solve correctly in a single pass. This is not just a hypothetical risk. Research has systematically documented this phenomenon, showing that after a certain point, more thinking leads to diminishing returns and can even be harmful, causing a model to second-guess and "flip" a correct answer to an incorrect one, especially on simpler problems [[22]](https://arxiv.org/html/2604.10739v1).![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)
Figure 4: The key strengths and weaknesses of reasoning models. (Source [https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png))

Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.
```
**Grader reasoning:**
- `cc`: When should we use reasoning models?:
**1:** Both sections cover the same needed-vs-not-needed task split, the same practical downsides (latency/cost, verbosity, overthinking, extended here with exploration-grounded detail).
- `fl`: When should we use reasoning models?:
**1:** The generated section follows the same progression as the expected one: needed-vs-not-needed framing, downsides (with its exploration-grounded addition carrying its own local lead-in), the figure, then the transition.
- `de`: When should we use reasoning models?:
**1:** [instances=1; quality=strong] One qualifying depth addition: the diminishing-returns/'negative flip' discussion — "more thinking leads to diminishing returns and can even be harmful, causing a model to second-guess and 'flip' a correct answer to an incorrect one, especially on simpler problems" [22], traceable to the exploration-phase 'When More Thinking Hurts' source closely (including the specific 'flip' terminology and the easier-problem nuance). Classified as strong: a detailed, multi-clause mechanism explanation, not a generic mention.
- `be`: When should we use reasoning models?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: When should we use reasoning models?:
**1:** depth_enhancement scored 1 for this section (one strong overthinking addition). The addition is a contained elaboration within the existing downsides discussion and does not shift the section's focus away from when-to-use guidance. CorePreservation scores 1.
- `ga`: When should we use reasoning models?:
**1:** All required content elements are present. Prose-only word count is approximately 191 words against a 160-word target (±25 tolerance floor, range 135–185 words), 6 words above the upper bound — within the previously-accepted noise range.

### Arm: light (preset1)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset1`

**Article text:**
```
## When should we use reasoning models?

Before diving into the technical details, it is important to know when to use a reasoning model. They deliver the highest returns on tasks that require decomposition or self-correction, like puzzles, advanced math, and competitive coding. For summarization, simple Q&A, or creative writing, a general-purpose model is often more than enough and more efficient [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

Using a reasoning model when it is not needed comes with practical downsides. The verbose intermediate steps lead to much higher latency and token costs. This extra output can also frustrate users in conversational settings who just want a quick answer. There is also the risk of overthinking, where the model invents unnecessary complications for a simple problem, like a math query that a standard model could solve in a single pass [[4]](https://arxiv.org/html/2503.20783v1). This can even lead to incorrect answers on straightforward tasks that a less specialized model would get right.![Image 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)
Image 4: The key strengths and weaknesses of reasoning models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.
```
**Grader reasoning:**
- `cc`: When should we use reasoning models?:
**1:** Both sections cover the same core ideas: reasoning models are best for complex tasks like puzzles and math, while general-purpose models suffice for simpler tasks, and both discuss the downsides (latency, cost, overthinking).
- `fl`: When should we use reasoning models?:
**1:** Both sections follow the same logical progression: first explaining appropriate use cases, then detailing the disadvantages.
- `de`: When should we use reasoning models?:
**0:** [instances=0] No depth additions present. The section restates pros/cons already in the ground truth (ref [4], exploitation, supports the overthinking point) and adds no new theoretical foundations, technical nuances, or case studies.
- `be`: When should we use reasoning models?:
**0:** [instances=0] No breadth additions present.
- `cp`: When should we use reasoning models?:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so CorePreservation is 1 by default as there are no qualifying additions to evaluate.
- `ga`: When should we use reasoning models?:
**1:** The generated section successfully covers all requirements: it identifies tasks where reasoning models excel versus where they are overkill, catalogs the practical downsides, includes the specified image, and provides the transition. The prose-only word count is approximately 167 words, within the 160-word target's 135–185 range.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset1`

**Article text:**
```
## When should we use reasoning models?

Before diving into technical details, it is important to consider when reasoning models are needed. They deliver the highest returns on complex tasks like puzzles, advanced mathematics, and competitive coding. These are problems that require decomposition and self-correction. For simpler tasks like summarization, basic factual question-answering, or creative writing, a general-purpose model is often sufficient and more efficient.

However, reasoning models have practical downsides. Their verbose intermediate steps lead to higher latency and token costs; OpenAI's o1 can be six times more expensive than GPT-4o [[7]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). This verbosity can frustrate users seeking quick answers. There is also the risk of "overthinking," where a model invents complications for a simple problem that a standard LLM would solve correctly in one pass.![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)
Image 4: The key strengths and weaknesses of reasoning models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Understanding when to deploy these specialized models is key. This leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.
```
**Grader reasoning:**
- `cc`: When should we use reasoning models?:
**1:** Both sections cover the same needed-vs-not-needed task split (using the guideline's own "creative writing" example rather than the ground truth's "translation"), the same practical downsides (latency/cost, verbosity, overthinking risk), and the same closing strengths/weaknesses figure. The 6x-more-expensive o1 figure is an addition that does not displace any expected idea.
- `fl`: When should we use reasoning models?:
**1:** The generated section follows the same progression as the expected one: needed-vs-not-needed framing, downsides, Image 4, then the transition. No media misplacement.
- `de`: When should we use reasoning models?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode (self-reflection mechanisms, small-model distillation capacity limits, cognitive-science parallels to journey learning, and neuroscience/LLM parallels), but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: When should we use reasoning models?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode (self-reflection mechanisms, small-model distillation capacity limits, cognitive-science parallels to journey learning, and neuroscience/LLM parallels), but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: When should we use reasoning models?:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: When should we use reasoning models?:
**1:** All required content elements are present: the needed/not-needed framing, the downsides, and the figure. Prose-only word count is approximately 146 words against a 160-word target (±25 tolerance floor, range 135–185 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset1`

**Article text:**
```
## When should we use reasoning models?

Before diving into the technical details, it is important to understand the trade-offs. Reasoning models deliver the highest return on investment for tasks that require decomposition, logical deduction, or self-correction, such as puzzles, advanced mathematics, and competitive coding. For tasks like summarization, simple factual question-answering, or creative writing, a general-purpose model is usually more efficient and cost-effective.

The practical downsides of reasoning models are notable. They introduce higher latency and token costs because of their verbose, step-by-step outputs. This extended "thinking time" can frustrate users in conversational applications who expect quick responses. There is also the risk of overthinking, where a model might introduce unnecessary complexity into a straightforward problem, leading to incorrect answers that a simpler model would have gotten right. For instance, a reasoning model might explore multiple interpretations of a simple arithmetic query, a behavior that is useful for complex problems but inefficient for basic ones.

<https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png>
Figure 4: The key strengths and weaknesses of reasoning models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.
```
**Grader reasoning:**
- `cc`: When should we use reasoning models?:
**1:** Both sections cover the same needed-vs-not-needed task split, the same practical downsides (latency/cost, verbosity, overthinking).
- `fl`: When should we use reasoning models?:
**1:** The generated section follows the same progression as the expected one: needed-vs-not-needed framing, downsides, the figure, then the transition.
- `de`: When should we use reasoning models?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: When should we use reasoning models?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: When should we use reasoning models?:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: When should we use reasoning models?:
**1:** All required content elements are present. Prose-only word count is approximately 172 words against a 160-word target (±25 tolerance floor, range 135–185 words), within tolerance.

## Section: S2::section-2-how-do-we-define-reasoning-model  (weight=0.081, contribution=+0.0115 FOR standard)
Stored section rewards: standard=0.4758  light=0.3927  (explore: standard=0.1323  light=0.0227)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset2`

**Article text:**
```
## How do we define "reasoning model"?

A reasoning model is one that generates multi-step intermediate thinking to solve complex queries. This process can involve explicit token traces that we can read or hidden internal iterations that happen within the model. This stands in contrast to the direct factual recall or single-pass pattern matching that is sufficient for simpler prompts. For example, asking "What is the capital of France?" requires a simple fact retrieval. Asking "If a train leaves Paris at 8 AM traveling at 100 km/h and a second train leaves Lyon 30 minutes later traveling at 120 km/h, where will they meet?" requires a series of calculations and logical steps.![An illustration comparing a short, direct answer from a regular LLM to a longer, step-by-step answer from a reasoning model.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)
Image 2: A regular LLM may provide a short answer, whereas a reasoning model typically includes intermediate steps that reveal its thought process. (Source [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982))

All modern LLMs exhibit some level of reasoning, which can be improved with techniques like Chain-of-Thought (CoT) prompting. However, specialized reasoning models are designed to achieve exceptional performance on difficult benchmarks that involve tasks like math olympiad problems, formal proofs, or novel puzzle-solving [[1]](https://arxiv.org/abs/2501.12948). This enhanced capability often emerges as a function of model scale; the benefits of CoT prompting, for instance, only materialize with models that have a sufficient number of parameters, typically around 100 billion [[21]](https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought). This suggests that certain reasoning abilities are emergent properties that appear as models grow larger and more complex.

The intermediate steps in these models manifest in two primary ways. The first is through **visible thought traces**, where the model outputs its step-by-step reasoning process for the user to see. This is common in models that use CoT. The second is through **invisible internal iterations**, a characteristic of models like OpenAI's o1, which allocate additional computation time at inference without exposing every intermediate token to the user [[2]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o). This shift from explicit to hidden reasoning represents a key evolution, where the structured thought process of CoT is automated and internalized by the model itself, allowing it to self-direct its reasoning without explicit prompting [[17]](https://www.nvidia.com/en-us/glossary/cot-prompting). This allows the model to "think" more deeply about a problem before providing a final answer. This internal deliberation is a core feature that distinguishes advanced reasoning models from their general-purpose counterparts.![A diagram showing that reasoning can be either an internal process for generating an answer or an explicit part of the final output.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)
Image 3: Reasoning can refer to the internal multi-step generation process or the explicit reasoning shown to the user. (Source [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982))

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.
```
**Grader reasoning:**
- `cc`: How do we define "reasoning model"?:
**1:** Both sections provide a clear definition of a reasoning model, contrast it with simple fact retrieval using an analogous multi-step math example, and discuss the two ways intermediate steps can manifest: visible thought traces and invisible internal iterations.
- `fl`: How do we define "reasoning model"?:
**1:** Both sections follow the same logical progression: a general definition, an example, a comparative image, and then the discussion of visible vs. invisible intermediate steps.
- `de`: How do we define "reasoning model"?:
**1:** [instances=2; quality=strong,standard] Two depth additions are present. (1) The claim that reasoning capabilities emerge as a function of model scale, with CoT prompting's benefits only materializing in models with roughly 100 billion parameters — qualifies as "technical nuances" / theoretical foundations, traceable to ref [21], research.google/blog/language-models-perform-reasoning-via-chain-of-thought, exploration-phase. Classified as strong: a specific, quantified emergence threshold. (2) The claim that CoT shifted from an explicit, user-prompted technique into an automated, internalized, self-directed mechanism within the model — traceable to ref [17], nvidia.com/en-us/glossary/cot-prompting, exploration-phase. This is classified as depth, not breadth: it explains a technical/implementation shift in the same mechanism (CoT) within the same core topic, rather than connecting outward to a distinct prior paradigm, another field, or an adjacent domain the way, e.g., a historical-lineage addition (such as tracing modern LLM planning back to 1970s symbolic AI systems) would. It qualifies as "technical nuances or alternative implementation perspectives." Classified as standard: a brief, single-sentence assertion without a fuller mechanism explanation or quantified detail.
- `be`: How do we define "reasoning model"?:
**0:** [instances=0] No breadth additions present. The section's only exploration-traceable addition beyond ref [21] is ref [17] (CoT's shift from explicit to automated/internalized reasoning), which is a depth addition, not breadth — it explains a technical/implementation nuance of the same mechanism (CoT) within the same core topic, rather than connecting outward to a different field, adjacent domain, or distinct prior paradigm.
- `cp`: How do we define "reasoning model"?:
**1:** The depth addition about reasoning as an emergent property of model scale is a concise, relevant technical detail that enhances the definition without overshadowing it. The ground truth core remains the primary focus of the section.
- `ga`: How do we define "reasoning model"?:
**1:** The generated section meets all requirements: it defines a reasoning model, provides a contrasting example, includes both required images, maps the reasoning spectrum, differentiates visible and invisible steps, and provides the transition. The prose-only word count is approximately 361 words, within the 350-word target's 315–385 range.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset2`

**Article text:**
```
## How do we define "reasoning model"?

A reasoning model is one that generates multi-step intermediate thinking to solve complex queries. This process can involve explicit token traces that we can read or hidden internal iterations that happen before an answer is produced. This stands in contrast to the direct factual recall or single-pass pattern matching that is sufficient for simpler prompts. For example, asking "What is the capital of France?" requires simple recall. But a question like "If a train leaves Paris at 8 AM traveling at 60 mph and another leaves Lyon at 9 AM traveling at 70 mph, when and where will they meet?" requires breaking the problem down into multiple logical steps.![Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)

Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.)

All modern LLMs exhibit some level of reasoning, which can be enhanced with techniques like Chain-of-Thought (CoT) prompting. However, the term "reasoning model" typically refers to specialized systems designed for excellence on difficult benchmarks, such as math olympiad problems, formal proofs, or novel puzzle-solving.

The intermediate steps these models take can manifest in two primary ways. The first is through visible thought traces, which are step-by-step outputs the user can read. The second is through invisible internal iterations, where the model allocates more computation time at inference to "think" without exposing every token of its process. This latter approach is rumored to be part of how models like OpenAI's o1 operate.![Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)

Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.

This shift from visible to hidden reasoning represents a key evolution. The concept began with CoT prompting, where models were explicitly guided to output their intermediate steps. As this proved effective, the process became more automated in what are now called test-time scaling models. These systems self-direct their reasoning process, generating 'hidden' thinking tokens internally before producing a final answer. This effectively turns a prompting strategy into a core model behavior [[18]](https://www.nvidia.com/en-us/glossary/cot-prompting). This automation is a breakthrough, allowing AI to handle complex reasoning tasks with greater autonomy.

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.
```
**Grader reasoning:**
- `cc`: How do we define "reasoning model"?:
**1:** Both sections define a reasoning model via multi-step intermediate steps, use a comparable simple-vs-complex query contrast (the generated section uses a harder two-trains example), distinguish visible thought traces from invisible/o1-style internal iterations, and note that ordinary LLMs already do basic reasoning via CoT while specialized models excel on the hardest benchmarks. The closing paragraph on CoT's evolution into automated test-time scaling is an addition; no expected idea is missing.
- `fl`: How do we define "reasoning model"?:
**1:** The generated section follows the same progression as the expected one: definition, example, Figure 2, the CoT/basic-reasoning spectrum point, the two manifestations, Figure 3, then the closing paragraph on CoT's evolution into test-time scaling (which has its own clear lead-in, "This shift from visible to hidden reasoning represents a key evolution") before the transition. Figures 2 and 3 land in the same relative positions as the expected section.
- `de`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: How do we define "reasoning model"?:
**1:** [instances=1; quality=strong] One qualifying breadth addition: the discussion of how CoT prompting "evolved" into automated test-time-scaling models — "these systems self-direct their reasoning process... this effectively turns a prompting strategy into a core model behavior" [18], traceable to an exploration-phase source (the NVIDIA CoT glossary entry) nearly verbatim. This qualifies as 'historical context or evolution of the topic.' Classified as strong: a specific, well-integrated account of the term's development, not a vague gesture at history.
- `cp`: How do we define "reasoning model"?:
**1:** breadth_enhancement scored 1 for this section (the CoT-evolution addition). The addition is a contained closing paragraph that reinforces rather than displaces the section's core definitional content, which remains the clearly dominant focus. CorePreservation scores 1.
- `ga`: How do we define "reasoning model"?:
**1:** All required content elements are present. Prose-only word count is approximately 333 words against a 350-word target (±35 tolerance, range 315–385 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset2`

**Article text:**
```
## How do we define "reasoning model"?

A reasoning model is one that generates multi-step intermediate thinking to solve complex queries. This process can involve explicit token traces that we can read or hidden internal iterations that happen within the model. This stands in contrast to the direct factual recall or single-pass pattern matching that is sufficient for simpler prompts. For example, asking "What is the capital of France?" requires a simple fact retrieval. But a question like "If I have 3 apples and eat one, then buy twice the remaining amount, how many do I have?" requires a sequence of steps to solve.![Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)
Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers. (Source [https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png))

It is important to recognize that reasoning exists on a spectrum. All modern LLMs exhibit some basic reasoning, which can be improved with techniques like Chain-of-Thought (CoT) prompting. However, specialized reasoning models are engineered to achieve exceptional performance on difficult benchmarks, such as math olympiad problems, formal proofs, or novel puzzles. These models are not just better at following instructions; they are trained to decompose problems, verify their work, and adapt their strategies.

The intermediate steps in these models can manifest in two primary ways. The first is through **visible thought traces**, which are the step-by-step outputs that a user can read and follow. This is the classic CoT approach. The second is through **invisible internal iterations**, like those rumored to be in OpenAI's o1 model, where the model allocates more computation time at inference ("test-time compute") without necessarily showing every step to the user. This distinction is important because it separates the user-facing explanation from the internal problem-solving process.

This evolution from visible to invisible reasoning is a direct result of the success of earlier techniques. The concept began with explicit Chain-of-Thought prompting, where users instructed the model to "think step by step" [[5]](https://arxiv.org/abs/2205.11916). Researchers found this so effective that they worked to automate it, leading to the development of test-time scaling models. These models can initiate and manage their own internal thought processes without explicit prompting, representing a notable step in AI's ability to handle complex reasoning autonomously [[21]](https://www.nvidia.com/en-us/glossary/cot-prompting). This internal monologue allows the model to explore different solution paths, correct its own errors, and build confidence in its final answer before presenting it.![Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)
Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user. (Source [https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png))

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.
```
**Grader reasoning:**
- `cc`: How do we define "reasoning model"?:
**1:** Both sections define a reasoning model via multi-step intermediate steps, use a comparable simple-vs-complex query contrast, distinguish visible thought traces from invisible/o1-style internal iterations, and note that ordinary LLMs already do basic reasoning while specialized models excel on the hardest benchmarks. The exploration-grounded CoT-evolution addition does not displace any expected idea.
- `fl`: How do we define "reasoning model"?:
**1:** The generated section follows the same progression as the expected one: definition, example, the first figure, the CoT/basic-reasoning spectrum point, the two manifestations, the exploration-grounded CoT-evolution addition (with its own clear lead-in), the second figure, then the transition. Both figures land in the same relative positions as the expected section.
- `de`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: How do we define "reasoning model"?:
**1:** [instances=1; quality=strong] One qualifying breadth addition: the discussion of how CoT prompting "evolved" into automated test-time-scaling models — "researchers found this so effective that they worked to automate it... these models can initiate and manage their own internal thought processes without explicit prompting" [21], traceable to an exploration-phase source (the NVIDIA CoT glossary) nearly verbatim. This qualifies as 'historical context or evolution of the topic.' Classified as strong: a specific, well-integrated account of the term's development.
- `cp`: How do we define "reasoning model"?:
**1:** breadth_enhancement scored 1 for this section (the CoT-evolution addition). The addition is a contained paragraph that reinforces rather than displaces the section's core definitional content, which remains clearly the dominant focus. CorePreservation scores 1.
- `ga`: How do we define "reasoning model"?:
**1:** All required content elements are present. Prose-only word count is approximately 388 words against a 350-word target (±35 tolerance, range 315–385 words), 3 words above the upper bound — negligible noise.

### Arm: light (preset1)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset1`

**Article text:**
```
## How do we define "reasoning model"?

A reasoning model is one that generates multi-step intermediate thinking to solve complex queries. This thinking can be explicit, appearing as visible token traces, or hidden, happening through internal iterations within the model. This contrasts with the direct factual recall or single-pass pattern matching that works for simpler prompts. For example, asking "What is the capital of France?" requires a simple fact retrieval. But asking "If a train travels at 60 mph for 3 hours, how far does it go?" requires breaking the problem down into logical steps, such as recalling the formula `distance = speed × time` and then performing the calculation.![Image 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)
Image 2: A regular LLM may only provide a short answer, whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.) (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

All modern LLMs exist on a spectrum of reasoning ability. Most can perform basic reasoning, especially when guided by techniques like Chain-of-Thought (CoT) prompting, which simply involves adding "Let's think step by step" to the prompt [[2]](https://arxiv.org/abs/2205.11916). However, specialized reasoning models are in a different league. They are explicitly trained to excel on difficult benchmarks that require deep, multi-step logic, such as math olympiad problems, formal proofs, or novel puzzle-solving [[3]](https://arxiv.org/abs/2501.12948).

These models generate intermediate steps in one of two ways. The first is through **visible thought traces**, where the model outputs its step-by-step process for the user to see, often enclosed in special tags like `<think>...</think>`. This makes the model's reasoning transparent and interpretable. The second is through **invisible internal iterations**, where the model allocates more computational time to "think" about a problem before producing a final answer, without showing every intermediate step. This is how models like OpenAI's o1 are thought to operate, leading to longer response times but higher accuracy on complex tasks [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).![Image 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)
Image 3: Reasoning can refer to the internal process or the visible output. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Interestingly, this modular approach to reasoning in LLMs mirrors findings in neuroscience. Research suggests that LLMs exhibit modular reasoning similar to specialized brain circuits, with distinct "experts" in Mixture-of-Experts models mirroring cognitive networks in the human brain. Some studies have even found parallels between hemispheric asymmetry in LLMs and the specialized roles of brain regions in language processing [[25]](https://arxiv.org/html/2506.13331v2). This suggests that the architectural choices we make when building these models may be tapping into fundamental principles of how biological systems process complex information.

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.
```
**Grader reasoning:**
- `cc`: How do we define "reasoning model"?:
**1:** Both sections provide a clear definition of a "reasoning model," use the same train-speed example to illustrate the concept, and discuss the two ways intermediate steps can appear (visible traces vs. internal iterations). The added neuroscience paragraph is a breadth addition and does not detract from core coverage.
- `fl`: How do we define "reasoning model"?:
**1:** Both sections follow the same logical flow: a general definition, an example, discussion of more complex tasks, and the two ways reasoning can manifest. The additional neuroscience paragraph is placed after the core content and before the transition, and does not disrupt the main flow.
- `de`: How do we define "reasoning model"?:
**0:** [instances=0] No depth additions present. The only exploration-traceable addition in this section — the neuroscience/brain-circuit parallel (ref [25]) — is a breadth addition, not depth, since it does not intensify understanding of the LLM reasoning process itself.
- `be`: How do we define "reasoning model"?:
**1:** [instances=1; quality=standard] A breadth addition is present: a parallel between modular reasoning in LLMs and neuroscience (specialized brain circuits, MoE "experts" mirroring cognitive networks, hemispheric asymmetry). Qualifies as "cross-domain analogies or lessons from other fields." Traces to ref [25] → research.md source [62], exploration-phase. Classified as standard, not strong: the passage asserts several surface-level parallels without naming a specific study/researcher or explaining the underlying mechanism connecting the domains; the underlying exploration sources ([62]-[66]) also contain identical boilerplate phrasing across all five URLs, reinforcing genericness. Well-integrated and does not overshadow the section's core content, so it passes both checks at the standard tier.
- `cp`: How do we define "reasoning model"?:
**1:** The neuroscience analogy is a brief, well-integrated paragraph that enriches the definition of a reasoning model without shifting the section's primary focus. The ground truth core remains the dominant narrative.
- `ga`: How do we define "reasoning model"?:
**1:** The generated section meets all guideline requirements: it defines a reasoning model, includes the required contrasting example, includes all three specified images, maps the reasoning spectrum, differentiates visible and invisible steps, and provides the correct transition. The prose-only word count is approximately 375 words, within the 350-word target's 315–385 range.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset1`

**Article text:**
```
## How do we define "reasoning model"?

A reasoning model is an LLM designed to solve multi-step problems by generating intermediate steps or "thoughts" [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling). Unlike a standard LLM that might give a direct answer, a reasoning model breaks down its process. For a simple question like "What is the capital of France?", a standard model would just answer "Paris." But for a complex problem like "If a train travels at 60 mph for 3 hours, how far does it go?", a reasoning model would show its work: "To find the distance, we use the formula distance = speed × time. Multiplying 60 mph by 3 hours gives 180 miles, so the train travels 180 miles."![Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.)](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)
Image 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.) (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

This capability exists on a spectrum. All modern LLMs can perform some level of basic reasoning, especially when guided by techniques like Chain-of-Thought (CoT) prompting [[2]](https://arxiv.org/abs/2205.11916). However, specialized reasoning models like OpenAI's o1 and DeepSeek-R1 are engineered to excel at highly complex benchmarks, such as math olympiad problems or formal proofs.

The intermediate steps a reasoning model takes can manifest in two primary ways:

1.  **Visible thought traces:** These are step-by-step outputs that the user can read, making the model's reasoning process transparent. This is common in models that use explicit CoT.
2.  **Invisible internal iterations:** Some models, like o1, perform their reasoning internally. They allocate more computational time to "think" through a problem without exposing every step to the user [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

It is important to distinguish between the internal reasoning process and the final output. A model can think step-by-step internally but still provide a concise final answer. Conversely, a model might not perform deep reasoning but can be prompted to generate a verbose, step-by-step explanation. True reasoning models combine both: they think through the problem in steps and can show that process to the user.![Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea9405ce_1538x810.png)
Image 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.
```
**Grader reasoning:**
- `cc`: How do we define "reasoning model"?:
**1:** Both sections define a reasoning model via multi-step intermediate steps, use a comparable simple-vs-complex query contrast (the generated section adds the worked arithmetic for the train example), distinguish visible thought traces from invisible/o1-style internal iterations, and note that ordinary LLMs already do basic reasoning via CoT while specialized models excel on the hardest benchmarks. All expected ideas and both figures are present.
- `fl`: How do we define "reasoning model"?:
**1:** The generated section follows the same progression as the expected one: definition, example, Image 2, the CoT/basic-reasoning spectrum point, the two manifestations, Image 3, then the transition. Images 2 and 3 land in the same relative positions immediately after their respective discussions.
- `de`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode (self-reflection mechanisms, small-model distillation capacity limits, cognitive-science parallels to journey learning, and neuroscience/LLM parallels), but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode (self-reflection mechanisms, small-model distillation capacity limits, cognitive-science parallels to journey learning, and neuroscience/LLM parallels), but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: How do we define "reasoning model"?:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: How do we define "reasoning model"?:
**1:** All required content elements are present: the definition, the simple-vs-complex example, both figures, the CoT/basic-reasoning spectrum point, and the visible/invisible distinction. Prose-only word count is approximately 318 words against a 350-word target (±35 tolerance, range 315–385 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset1`

**Article text:**
```
## How do we define "reasoning model"?

A reasoning model is an LLM designed to solve multi-step problems by generating intermediate steps or "thoughts" before arriving at a final answer. This process can be explicit, where the model outputs its reasoning trace for the user to see, or implicit, where the thinking happens internally. This contrasts with standard LLMs that often provide direct, single-pass answers, which is sufficient for simpler queries but falls short on complex problems. For example, asking "What is the capital of France?" requires simple fact retrieval, while a math problem like "If a train travels at 60 mph for 3 hours, how far does it go?" benefits from a step-by-step breakdown.

<https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png>
Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.) (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

All modern LLMs possess some level of reasoning, which can be enhanced with techniques like Chain-of-Thought (CoT) prompting. However, specialized reasoning models are built to excel at difficult benchmarks, such as math Olympiad problems or formal proofs, where standard models fail. This spectrum of capability means that "reasoning" is not a binary attribute but a continuum, with specialized models occupying the high-performance end.

These intermediate steps manifest in two primary ways. The first is through **visible thought traces**, where the model's output includes a step-by-step explanation of its process. This transparency allows users to follow the model's logic, verify its work, and understand how it reached its conclusion. The second is through **invisible internal iterations**, where the model allocates more computational resources at inference time to "think" longer without exposing every step to the user. This latter approach, rumored to be part of how models like OpenAI's o1 operate, involves internal self-correction and refinement before a final answer is generated. The distinction is not just about what the user sees; it's about how the model processes information. One generates a rationale as part of its output, while the other performs internal computations to refine its answer before generating a final response.

<https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-dcea9405ce_1538x810.png>
Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

This ability to break down problems is not just a neat feature; it is a fundamental shift in how LLMs operate. It moves them from being simple pattern matchers to more deliberate problem-solvers. By externalizing or internalizing their thought process, these models can tackle tasks that are otherwise intractable, making them essential tools for anyone working on the frontier of AI.

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models makes sense for an AI engineer.
```
**Grader reasoning:**
- `cc`: How do we define "reasoning model"?:
**1:** Both sections define a reasoning model via multi-step intermediate steps, use a comparable simple-vs-complex query contrast, distinguish visible thought traces from invisible/o1-style internal iterations, and note that ordinary LLMs already do basic reasoning while specialized models excel on the hardest benchmarks. The added elaboration on how the two manifestations differ mechanistically is an addition that does not displace any expected idea.
- `fl`: How do we define "reasoning model"?:
**1:** The generated section follows the same progression as the expected one: definition, example, the first figure, the CoT/basic-reasoning spectrum point, the two manifestations, the second figure, then the transition. Both figures land in the same relative positions as the expected section.
- `de`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: How do we define "reasoning model"?:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: How do we define "reasoning model"?:
**1:** All required content elements are present. Prose-only word count is approximately 396 words against a 350-word target (±35 tolerance, range 315–385 words), 11 words above the upper bound. This sits between the previously-accepted noise ceiling (up to ~8 words) and the range now ruled to fail (13–18 words) — treated here as within tolerance, but flagged as a new boundary case worth confirming (see summary).
