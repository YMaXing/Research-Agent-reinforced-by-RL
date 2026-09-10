# Near-tie review: Understanding_Reasoning_LLMs  (standard vs deep, margin=+0.0340)

## Reviewer conclusion (2026-09-02, updated after re-scoring): KEEP `standard`, no override

**Note on runner-up change:** after this round of re-scoring, the runner-up arm
flipped from `light` (previous review, margin +0.0173) to `deep` -- `light`'s
averaged R_w dropped to third place (0.349, behind `deep`'s 0.362), driven by a
collapsed production-draw value for `light` (0.494 -> 0.228). `standard`
remains the winner throughout, and its margin over the new runner-up nearly
doubled.

**Quantitative basis:** per-dimension binary scores (8 sections x 3 draws,
n=24 per arm) show cc/fl/cp/ga all exactly tied between `standard` and `deep`
(unlike the previous standard-vs-light comparison, where `ga` cost `standard`
-0.083). `de` still favors `standard` (0.583 vs 0.333, +0.250), and `be`
slightly favors `deep` (-0.042). This is now a cleaner picture than the prior
review: `standard`'s edge comes from a clean `de` advantage with zero
guideline-adherence or core-content offsetting cost.

**Distributional basis:** per-draw margins (standard - deep) are **[+0.034,
+0.003, +0.065]**, mean +0.034, sd 0.031 -- **all 3 of 3 draws favor
`standard`** (up from 2/3 favoring `standard` over `light` previously).
Moderated significance: p=0.098 (one-tailed, df=2) -- notably stronger than
the prior review's p=0.32 against `light`. `standard` also beats `skip` with
the strongest evidence in the article (p=0.031, 3/3). By contrast,
`standard`-vs-`light` is now the weak pairing (p=0.22, only 2/3), and `deep`
vs `light` is essentially a coin flip (p=0.40, 1/3) -- `light`'s standing in
this article has generally weakened across the board.

**Decision:** no manual override needed -- `standard` is mean-R_w's own
winner, and the evidence for it strengthened substantially after this
re-scoring: margin nearly doubled (+0.017 -> +0.034), the runner-up comparison
moved from a 2/3-split, p=0.32 result to a unanimous 3/3, p=0.098 result, and
the quantitative picture simplified to a single clean `de` advantage with no
offsetting `ga` cost.

---

## All sections (standard vs deep), most-against-standard first
| section | weight | contribution | running total |
|---|---:|---:|---:|
| section-8-conclusion | 0.079 | -0.0071 | -0.0071 |
| section-7-developing-reasoning-models-on-a-limited | 0.140 | -0.0001 | -0.0072 |
| section-3-when-should-we-use-reasoning-models | 0.037 | +0.0035 | -0.0037 |
| section-6-thoughts-about-deepseek-r1 | 0.081 | +0.0038 | +0.0001 |
| section-5-the-4-main-ways-to-build-and-improve-rea | 0.453 | +0.0050 | +0.0051 |
| section-4-a-brief-look-at-the-deepseek-training-pi | 0.070 | +0.0052 | +0.0103 |
| section-1-methods-and-strategies-for-building-and- | 0.058 | +0.0073 | +0.0176 |
| section-2-how-do-we-define-reasoning-model | 0.081 | +0.0164 | +0.0340 |

(stored article margin = +0.0340 -- should match the running total's final row to ~4 decimals)

## Section: S8::section-8-conclusion  (weight=0.079, contribution=-0.0071 AGAINST standard)
Stored section rewards: standard=0.2136  deep=0.2657  (explore: standard=0.0700  deep=0.1350)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset2`

**Article text:**
```
## Conclusion

We have explored the four primary approaches to building and refining reasoning models. Inference-time scaling offers performance gains with no training cost but can be expensive to serve. Pure RL is a powerful research tool that can unlock emergent, non-human-like reasoning. The SFT+RL hybrid provides a production-ready blueprint for creating stable, high-performing models. Finally, distillation offers an efficient way to transfer these capabilities to smaller models, though the results are ultimately derivative of the teacher.

The future of the most capable systems will likely be a hybrid one. We suspect that frontier models like o1, and its successors, already combine complex SFT+RL training pipelines with substantial inference-time scaling. This allows them to benefit from both the robust, emergent behaviors discovered during training and the "extra thinking time" at inference. This hybrid approach is also becoming central to the development of multi-agent systems, where reasoning models act as the cognitive engines that enable agents to collaborate, plan, and execute complex tasks [[22]](https://arxiv.org/html/2507.21969v1). By integrating structured critique and a "Theory of Mind," these systems can achieve a level of coordination and problem-solving that a single agent cannot [[22]](https://arxiv.org/html/2507.21969v1).

Furthermore, the advanced logical capabilities of reasoning models are proving invaluable in scientific discovery. They are being used to accelerate research by screening molecular datasets, generating novel hypotheses, and analyzing complex experimental data [[23]](https://arxiv.org/html/2503.17604v1). As these models become more integrated with agentic workflows and external tools, they are evolving from task-specific assistants into more autonomous scientific partners [[24]](https://arxiv.org/html/2505.13259v1). This progression also offers a new lens through which to study human cognition, as the reasoning patterns and biases exhibited by LLMs show remarkable similarities to our own [[25]](https://www.browndailyherald.com/article/2026/01/llm-reasoning-has-striking-similarities-with-human-cognition-brown-researchers-find).

For AI engineers, the key takeaway is strategic. There is no single best approach. The right choice depends on your specific constraints: budget, performance targets, latency requirements, and the need for novel problem-solving versus reliable execution. Instead of defaulting to the largest proprietary model, you should match the chosen technique to concrete constraints, using the task-complexity framework we discussed to guide your decision. By understanding the trade-offs between these four methods, you can build or select the right reasoning model for your application.
```
**Grader reasoning:**
- `cc`: Conclusion:
**0:** Both sections recap the four strategies and forecast a hybrid future combining SFT+RL with inference-time scaling. However, the expected section makes a specific claim — stated twice, once in point 2 of the recap and again in the closing paragraph — that OpenAI's o1 "probably starts from a weaker, smaller base model than DeepSeek-R1 but compensates with RL + SFT and inference-time scaling," offered as the author's explanation for why DeepSeek-R1 performs so well while remaining cheap at inference. This specific argument is entirely absent from the generated conclusion, which states only that frontier models like o1 likely combine SFT+RL with inference-time scaling, without the base-model-strength attribution. Since this argument is substantive and emphasized twice in the expected section yet wholly missing here, CoreContent scores 0.
- `fl`: Conclusion:
**1:** Both sections follow the same logical flow: recapping the four approaches in the same order, then forecasting a hybrid future likely used by o1. The generated section's additional material on multi-agent systems, scientific discovery, and human cognition is inserted after the forecast and before the closing strategic guidance, and does not disrupt the core recap-then-forecast progression.
- `de`: Conclusion:
**0:** [instances=0] No depth additions present. The exploration-sourced material in this section (multi-agent systems, scientific discovery, human cognition) connects the core topic to adjacent fields and industries rather than intensifying understanding of the core topic itself, so it is evaluated under breadth_enhancement, not depth_enhancement.
- `be`: Conclusion:
**1:** [instances=1; quality=strong] A breadth addition is present, combining three closely-clustered adjacent-domain connections into one instance: the application of reasoning models as cognitive engines in multi-agent systems via Theory of Mind and structured critique (ref [22], arxiv.org/html/2507.21969v1); their use in scientific discovery for screening molecular datasets, generating hypotheses, and evolving into autonomous scientific partners (refs [23]+[24], arxiv.org/html/2503.17604v1 and arxiv.org/html/2505.13259v1); and a cross-domain analogy to human cognition, noting that LLM reasoning patterns and biases show similarities to our own (ref [25], browndailyherald.com/.../llm-reasoning-has-striking-similarities-with-human-cognition). These qualify as "practical applications of the core topic in other industries or domains" and "cross-domain analogies or lessons from other fields." All four references are confirmed inside research.md's exploration-phase block. Classified as strong: a rich, multi-faceted addition bundling several specific, named applications and mechanisms (Theory of Mind, structured critique, molecular screening, hypothesis generation) rather than a single generic mention.
- `cp`: Conclusion:
**1:** The multi-agent systems, scientific discovery, and human cognition material is a substantial addition — roughly a third of the section's length, with no ground truth counterpart. However, it is framed as a natural extension of the "hybrid future" forecast and is bookended by the ground truth's core recap (first paragraph) and the guideline-required strategic guidance (final paragraph), both of which remain clearly present and prominent. The core narrative is not overshadowed, so CorePreservation is 1.
- `ga`: Conclusion:
**1:** The generated section meets all requirements: it recaps the four approaches, forecasts a hybrid future, and delivers strategic guidance for AI engineers referencing the task-complexity framework introduced earlier. Target 340, tolerance ±34, range 306-374. Exact count: 353. Within range.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset2`

**Article text:**
```
## Conclusion

We have explored the four primary approaches to building and improving reasoning models. **Inference-time scaling** offers a way to boost performance without retraining but comes at a high serving cost and can lead to overthinking. **Pure RL** provides a valuable research insight, unlocking emergent behaviors from a cold start with verifiable rewards. The **SFT+RL hybrid** offers a production-ready blueprint that balances raw reasoning power with readability and general-purpose utility. Finally, **distillation** provides an efficient method for transferring capabilities to smaller models, though its performance is ultimately derivative of the teacher.

The future of the most capable AI systems is likely to be a hybrid one. We suspect that frontier models like o1, and likely future o3-class models, already combine robust SFT+RL training pipelines with sophisticated inference-time scaling. This allows them to benefit from both the deep, baked-in reasoning abilities developed during training and the dynamic, on-the-fly computational depth available at inference. This combination addresses the core trade-off: training-time methods build a strong foundation, while inference-time methods provide the flexibility to tackle novel or exceptionally difficult problems.

For AI engineers, the key takeaway is strategic. The choice of which technique to use should be matched to concrete constraints. Budget, performance targets, innovation needs, and deployment latency all play a role. There is no one-size-fits-all answer. Instead of defaulting to the largest proprietary model available, a clear understanding of these trade-offs allows you to build more efficient, targeted, and cost-effective AI systems. This means evaluating whether the high cost of an o1-class model is justified for your use case, or if a smaller, distilled model could achieve 90% of the performance for a fraction of the cost. It is about making an informed engineering decision rather than chasing the state-of-the-art.
```
**Grader reasoning:**
- `cc`: Conclusion:
**0:** Both sections recap the four approaches and forecast a hybrid future combining SFT+RL with inference-time scaling, and the closing guidance names all of budget, performance targets, innovation needs, and deployment latency. However, the expected section additionally claims that o1 "probably starts from a weaker, smaller base model than DeepSeek-R1 but compensates with RL + SFT and inference-time scaling" — a substantive explanatory argument entirely absent from the generated conclusion, which covers only the general hybrid-pattern point. The CoreContent rule has no exception for speculative or hedged claims; since this is a substantive idea present in the expected section and absent from the generated one, CoreContent scores 0. [Previously scored 1 under an untraceable-GT-only-content exception that does not appear anywhere in the prompt; reverted, consistent with the same correction applied elsewhere in this review.]
- `fl`: Conclusion:
**1:** The four-item recap and the hybrid-future paragraph follow the same order as the expected section. The untraceable "o1 has a weaker base model" claim (not scored here — see CoreContent) does not leave a bridgeless transition.
- `de`: Conclusion:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Conclusion:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: Conclusion:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: Conclusion:
**1:** The four-approach recap, the hybrid-future forecast, and the constraint-matching guidance are present, and all four guideline constraint types (budget, performance targets, innovation needs, deployment latency) are explicitly named. However, prose-only word count is approximately 290 words against a 340-word target (±34 tolerance, range 306–374 words), 16 words below the lower bound — outside tolerance. [Revised: this section's 16-word shortfall was previously scored as a failure per the same now-corrected ruling described under Section 4. Per the corrected standard, this shortfall does not warrant a penalty. GuidelineAdherence scores 1.]

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset2`

**Article text:**
```
## Conclusion

We have explored the four primary approaches to building and improving reasoning models. **Inference-time scaling**, which includes techniques like CoT prompting and MCTS, enhances performance without any training cost but incurs high serving costs. **Pure RL**, as demonstrated by DeepSeek-R1-Zero, is a powerful research tool that can unlock emergent behaviors like self-correction from a cold start. The **SFT+RL hybrid** approach, used for the flagship DeepSeek-R1, offers a production-ready blueprint that combines the stability of supervised learning with the exploratory power of RL, especially effective when verifiable rewards are available. Finally, **distillation** provides an efficient method for transferring capabilities to smaller models, though the resulting models are ultimately derivative of the teacher.

Looking ahead, the future of the most capable systems will likely be a hybrid one. We suspect that frontier models like o1, and future o3-class systems, already combine complex SFT+RL training pipelines with sophisticated inference-time scaling. This allows them to benefit from both the robust, emergent behaviors discovered during training and the on-the-fly refinement and search at inference time. This combination is crucial for creating agentic systems that can decompose goals, self-correct, and handle multi-step problems reliably. The integration of reasoning models into multi-agent frameworks, where different agents can critique and refine each other's work, represents another promising direction for building more robust and collaborative AI [[26]](https://www.emergentmind.com/topics/multi-agent-reasoning-frameworks).

For AI engineers, the key takeaway is to match the technique to the constraints of the project. There is no one-size-fits-all solution. The choice between these four approaches should be driven by a clear understanding of the trade-offs between budget, performance targets, innovation needs, and deployment latency. Rather than defaulting to the largest, most expensive proprietary model, a strategic engineer will consider whether the task truly requires the power of a full reasoning model, or if a more efficient, distilled model or even a general-purpose LLM with smart prompting would suffice. This decision framework is essential for building systems that are not just powerful, but also practical and cost-effective. The art of AI engineering lies in making these informed decisions, moving beyond hype to build reliable, production-grade applications.
```
**Grader reasoning:**
- `cc`: Conclusion:
**0:** Both sections recap the four approaches and forecast a hybrid future combining SFT+RL with inference-time scaling, and the closing guidance explicitly names all of budget, performance targets, innovation needs, and deployment latency. However, the expected section additionally claims that o1 "probably starts from a weaker, smaller base model than DeepSeek-R1 but compensates with RL + SFT and inference-time scaling" — a substantive explanatory argument entirely absent from the generated conclusion. The CoreContent rule has no exception for speculative or hedged claims; since this is a substantive idea present in the expected section and absent from the generated one, CoreContent scores 0. [Previously scored 1 under an untraceable-GT-only-content exception that does not appear anywhere in the prompt; reverted, consistent with the same correction applied elsewhere in this review.]
- `fl`: Conclusion:
**1:** The four-item recap, the hybrid-future paragraph, and the exploration-grounded multi-agent addition (with its own clear lead-in) follow the same order as the expected section. Neither section has media here.
- `de`: Conclusion:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Conclusion:
**1:** [instances=1; quality=strong] One qualifying breadth addition: "the integration of reasoning models into multi-agent frameworks, where different agents can critique and refine each other's work, represents another promising direction" [26], traceable to an exploration-phase source (emergentmind.com) closely. This qualifies as 'practical applications... or emerging trends in adjacent fields or the broader ecosystem.' Classified as strong: a specific, named architectural pattern rather than a vague gesture at future work.
- `cp`: Conclusion:
**1:** breadth_enhancement scored 1 for this section (the multi-agent-frameworks addition). The addition is a single contained sentence placed after the hybrid-future paragraph, and the section's core recap and guidance remain clearly the dominant focus. CorePreservation scores 1.
- `ga`: Conclusion:
**1:** The four-approach recap, the hybrid-future forecast, and the constraint-matching guidance are present, and all four guideline constraint types (budget, performance targets, innovation needs, deployment latency) are explicitly named. Prose-only word count is approximately 347 words against a 340-word target (±34 tolerance, range 306–374 words), within tolerance.

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset3`

**Article text:**
```
## Conclusion

We have explored the four primary approaches to building reasoning models, each with distinct trade-offs. **Inference-time scaling** offers a training-free way to boost performance but at a high serving cost, making it a flexible but expensive tool. **Pure RL** provides a powerful research pathway, unlocking emergent behaviors like self-correction from a cold start and revealing the latent potential within base models. The **SFT+RL hybrid** offers a production-ready blueprint, refining these emergent abilities with supervised data and verifiable rewards to achieve stability and peak performance. Finally, **distillation** presents an efficient method for transferring these hard-won capabilities to smaller, more accessible models, though the resulting models are ultimately derivative of their larger teacher.

We forecast a hybrid future where the most capable systems will combine these techniques. The production pipeline will likely involve a robust SFT+RL process to build a strong base model, which is then further enhanced with adaptive inference-time scaling at deployment. This is the pattern we suspect underlies OpenAI's o1 and will likely define future o3-class models. This combination allows for a powerful, efficient, and adaptable system that can handle a wide range of tasks. Looking further ahead, emerging research into quantum-classical hybrid architectures could reshape LLM reasoning. These approaches aim to use quantum circuits as targeted accelerators for computational bottlenecks in classical models, such as attention mechanisms or feature mapping, rather than replacing the entire architecture [[23]](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.177004376.69666864), [[24]](https://arxiv.org/html/2504.08732v1). While still in early stages, this line of work points toward a future where specialized hardware could unlock new levels of efficiency and capability in reasoning systems.

For AI engineers, the key is to move beyond the default of using the largest proprietary model for every task. The choice of technique should be a strategic one, matched to concrete constraints like budget, performance targets, and latency. This strategic thinking is already being applied in domains like finance, where reasoning models act as algorithmic trading agents [[25]](https://arxiv.org/html/2504.10789v1), and in robotics, where techniques like Embodied Chain-of-Thought (ECoT) guide autonomous systems in complex, real-world tasks [[26]](https://www.mdpi.com/2673-2688/6/7/158), [[27]](https://venturebeat.com/business/researchers-develop-technique-to-give-robots-embodied-reasoning-abilities). By understanding these trade-offs, you can architect systems that are not only powerful but also practical and efficient.
```
**Grader reasoning:**
- `cc`: Conclusion:
**0:** Both sections recap the four strategies and forecast a hybrid future combining SFT+RL with inference-time scaling. However, the expected section makes a specific claim — stated twice, once in point 2 of the recap and again in the closing paragraph — that OpenAI's o1 "probably starts from a weaker, smaller base model than DeepSeek-R1 but compensates with RL + SFT and inference-time scaling," offered as the author's explanation for why DeepSeek-R1 performs so well while remaining cheap at inference. This specific argument is entirely absent from the generated conclusion, which states only that the pattern "underlies OpenAI's o1" without the base-model-strength attribution. Since this argument is substantive and emphasized twice in the expected section yet wholly missing here, CoreContent scores 0.
- `fl`: Conclusion:
**1:** Both sections serve as a conclusion, summarizing the main takeaways in the same order. The generated section is more expansive, adding detail to the summary and forward-looking statements the expected output lacks, which is an accepted complementary addition that does not disrupt the flow.
- `de`: Conclusion:
**0:** [instances=0] No depth additions present. The additional material in this section (robotics, finance, quantum-classical hybrids) connects the core topic to adjacent fields and industries rather than intensifying understanding of the core topic itself, so it is evaluated under breadth_enhancement, not depth_enhancement.
- `be`: Conclusion:
**1:** [instances=2; quality=strong,strong] Two breadth additions are present, each combining closely-clustered same-paragraph citations into one instance. (1) Emerging research into quantum-classical hybrid architectures — using quantum circuits as targeted accelerators for computational bottlenecks like attention mechanisms or feature mapping, rather than replacing the classical architecture — traceable to ref [23] (techrxiv.org/doi/pdf/10.36227/techrxiv.177004376.69666864) and ref [24] (arxiv.org/html/2504.08732v1), both exploration-phase. Qualifies as "enabling/disrupting technologies that intersect with the core topic." Classified as strong: specific technical detail (targeted accelerators for named bottleneck components) rather than a vague mention. (2) Practical applications in finance (reasoning models as algorithmic trading agents) and robotics (Embodied Chain-of-Thought guiding autonomous systems), which appear together in the same sentence/paragraph and are treated as one combined instance — traceable to ref [25] (arxiv.org/html/2504.10789v1), ref [26] (mdpi.com/2673-2688/6/7/158), and ref [27] (venturebeat.com/.../researchers-develop-technique-to-give-robots-embodied-reasoning-abilities), all exploration-phase. Qualifies as "practical applications of the core topic in other industries or domains beyond the section's primary scope." Classified as strong: two named industry applications with a specific technique (ECoT) called out.
- `cp`: Conclusion:
**1:** The robotics, finance, and quantum-classical hybrid material is presented as forward-looking, illustrative examples at the end of the conclusion, directly serving the guideline's required strategic-guidance and hybrid-future-forecast elements. The core recap of the four approaches and the closing strategic guidance remain clearly present and dominant, so CorePreservation is 1.
- `ga`: Conclusion:
**1:** The generated section recaps the four approaches and forecasts a hybrid future combining SFT+RL with inference-time scaling. It delivers strategic guidance by advising engineers to match technique to concrete constraints (budget, performance targets, latency) rather than defaulting to the largest model — a sufficient paraphrase of "reference the decision heuristic and task-complexity framework introduced earlier," even without naming Figure 4 explicitly. The additional material on robotics, finance, and quantum-classical hybrids directly illustrates this strategic-guidance point (matching technique to domain) and extends the hybrid-future forecast, making it closely related complementary information rather than an unrelated topic under the guideline's "More" rule. The prose-only word count is approximately 347 words, within the 340-word target's 306–374 range.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset3`

**Article text:**
```
## Conclusion

We have explored the four primary approaches to building and improving reasoning models. **Inference-time scaling** offers a way to boost performance without any training cost but comes at a high serving cost, impacting latency and user experience. **Pure RL**, as demonstrated by DeepSeek-R1-Zero, is a powerful research tool for unlocking emergent behaviors like self-correction, though it can be unstable. The **SFT+RL hybrid** method provides a production-ready blueprint that balances the stability of supervised data with the exploratory power of RL, making it a robust choice for developing reliable models. Finally, **distillation** offers an efficient method for transferring capabilities to smaller models, making advanced reasoning more accessible, though its performance is ultimately limited by the teacher model.

The future of reasoning models will likely be a hybrid one. The most capable systems will probably combine robust SFT+RL training pipelines with sophisticated inference-time scaling techniques. This is precisely the pattern we suspect underlies models like o1 and will likely define future o3-class systems. The impact of these techniques extends beyond benchmarks. In robotics, reasoning models are being adapted to decompose high-level commands into executable steps for navigation and manipulation, allowing autonomous systems to handle complex, long-horizon tasks [[36]](https://www.mdpi.com/2673-2688/6/7/158). Similarly, in finance, LLMs are being deployed as trading agents that can express their reasoning in natural language, creating new possibilities for algorithmic trading and market analysis [[37]](https://arxiv.org/html/2504.10789v1).

For AI engineers, the key takeaway is strategic. The choice of which technique to use should be driven by concrete constraints: budget, performance targets, latency requirements, and the need for innovation. Instead of defaulting to the largest, most expensive proprietary model, a careful analysis of the task's complexity and the available resources can lead to a more optimal solution. For instance, a project with a tight budget might start with distillation, while a research-focused team might explore pure RL to push the boundaries of emergent capabilities. For production systems requiring a balance of performance and reliability, the SFT+RL hybrid approach currently offers the most promising path. By understanding the trade-offs between these four approaches, you can design and build reasoning systems that are not only powerful but also practical and efficient.
```
**Grader reasoning:**
- `cc`: Conclusion:
**0:** Both sections recap the four approaches and forecast a hybrid future combining SFT+RL with inference-time scaling, and the closing guidance names budget, performance targets, latency, and innovation needs. However, the expected section additionally claims that o1 "probably starts from a weaker, smaller base model than DeepSeek-R1 but compensates with RL + SFT and inference-time scaling" — a substantive explanatory argument entirely absent from the generated conclusion. The CoreContent rule has no exception for speculative or hedged claims; since this is a substantive idea present in the expected section and absent from the generated one, CoreContent scores 0. [Previously scored 1 under an untraceable-GT-only-content exception that does not appear anywhere in the prompt; reverted, consistent with the same correction applied elsewhere in this review.]
- `fl`: Conclusion:
**1:** The four-item recap, the hybrid-future paragraph, and the exploration-grounded robotics/finance additions (each with their own clear lead-in) follow the same order as the expected section. The untraceable 'o1 has a weaker base model' claim (not scored here — see CoreContent) does not leave a bridgeless transition.
- `de`: Conclusion:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Conclusion:
**1:** [instances=2; quality=strong,strong] Two qualifying breadth additions, each traceable to a distinct exploration-phase source. (1) "In robotics, reasoning models are being adapted to decompose high-level commands into executable steps for navigation and manipulation" [36], traceable to an exploration source on LLMs in robotic control closely. (2) "In finance, LLMs are being deployed as trading agents that can express their reasoning in natural language" [37], traceable to a distinct exploration source on LLM trading agents closely. Both qualify as 'practical applications of the core topic in other industries or domains beyond the section's primary scope' and are classified strong: specific, named industry applications rather than a vague gesture at broader relevance.
- `cp`: Conclusion:
**1:** breadth_enhancement scored 1 for this section (the robotics and finance additions). Both are contained sentences placed after the hybrid-future paragraph and before the closing strategic guidance, and the section's core recap and guidance remain clearly the dominant focus. CorePreservation scores 1.
- `ga`: Conclusion:
**1:** The four-approach recap, the hybrid-future forecast, and the constraint-matching guidance are present, and all four guideline constraint types (budget, performance targets, latency, and 'the need for innovation') are explicitly named. Prose-only word count is approximately 356 words against a 340-word target (±34 tolerance, range 306–374 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset3`

**Article text:**
```
## Conclusion

We have explored the four primary approaches to building and improving reasoning models. **Inference-time scaling** offers a way to enhance performance without retraining but comes at a high serving cost. **Pure RL** provides a path to emergent, novel reasoning but can be unstable and computationally intensive. The **SFT+RL hybrid** offers a production-ready blueprint that balances stability and performance, especially when verifiable rewards are available. Finally, **distillation** provides an efficient method for transferring capabilities to smaller models, though its performance is ultimately limited by the teacher model.

Looking ahead, we forecast a hybrid future where the most capable systems will combine these techniques. Production-grade reasoning models will likely be built using robust SFT+RL pipelines and then further enhanced with inference-time scaling for the most challenging tasks. This is the pattern we suspect underlies models like o1 and will likely define the next generation of o3-class models.

The impact of these reasoning techniques extends far beyond benchmarks. In fields like robotics, they are being adapted to give autonomous systems the ability to handle long-horizon planning, execute multi-step tasks, and recover from errors in dynamic environments [[27]](https://www.mdpi.com/2673-2688/6/7/158). Similarly, in finance, reasoning LLMs are being deployed as autonomous trading agents that can adhere to complex strategies like value investing or momentum trading, reacting to market dynamics in real-time [[28]](https://arxiv.org/html/2504.10789v1). These applications show that mastering reasoning is not just an academic exercise but a core component of building next-generation AI products.

For AI engineers, the key takeaway is to match the technique to the constraints of the project. There is no one-size-fits-all solution. The choice between these approaches should be a strategic one, guided by your budget, performance targets, latency requirements, and the need for innovation versus proven reliability. Instead of defaulting to the largest proprietary model, a careful consideration of these trade-offs will lead to more effective and sustainable AI systems.
```
**Grader reasoning:**
- `cc`: Conclusion:
**0:** Both sections recap the four approaches and forecast a hybrid future combining SFT+RL with inference-time scaling, and the closing guidance explicitly names all of budget, performance targets, latency, and innovation needs. However, the expected section additionally claims that o1 "probably starts from a weaker, smaller base model than DeepSeek-R1 but compensates with RL + SFT and inference-time scaling" — a substantive explanatory argument entirely absent from the generated conclusion. The CoreContent rule has no exception for speculative or hedged claims; since this is a substantive idea present in the expected section and absent from the generated one, CoreContent scores 0. [Previously scored 1 under an untraceable-GT-only-content exception that does not appear anywhere in the prompt; reverted, consistent with the same correction applied elsewhere in this review.]
- `fl`: Conclusion:
**1:** The four-item recap, the hybrid-future paragraph, and the exploration-grounded robotics/finance additions (each with their own clear lead-in) follow the same order as the expected section. Neither section has media here.
- `de`: Conclusion:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Conclusion:
**1:** [instances=2; quality=strong,strong] Two qualifying breadth additions, each traceable to a distinct exploration-phase source. (1) "In fields like robotics, they are being adapted to give autonomous systems the ability to handle long-horizon planning, execute multi-step tasks, and recover from errors in dynamic environments" [27], traceable to an exploration source on LLMs in robotic control closely. (2) "In finance, reasoning LLMs are being deployed as autonomous trading agents that can adhere to complex strategies like value investing or momentum trading, reacting to market dynamics in real-time" [28], traceable to a distinct exploration source on LLM trading agents closely. Both qualify as 'practical applications of the core topic in other industries or domains' and are classified strong: specific, named industry applications.
- `cp`: Conclusion:
**1:** breadth_enhancement scored 1 for this section (the robotics and finance additions). Both are contained sentences placed after the hybrid-future paragraph and before the closing strategic guidance, and the section's core recap and guidance remain clearly the dominant focus. CorePreservation scores 1.
- `ga`: Conclusion:
**1:** The four-approach recap, the hybrid-future forecast, and the constraint-matching guidance are present, and all four guideline constraint types (budget, performance targets, latency, and innovation needs) are explicitly named. Prose-only word count is approximately 307 words against a 340-word target (±34 tolerance, range 306–374 words), within tolerance (just above the lower bound).

## Section: S7::section-7-developing-reasoning-models-on-a-limited-budget  (weight=0.140, contribution=-0.0001 AGAINST standard)
Stored section rewards: standard=0.4011  deep=0.4032  (explore: standard=0.1575  deep=0.1725)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset2`

**Article text:**
```
## Developing reasoning models on a limited budget

The high cost of developing reasoning models can be discouraging for researchers and engineers with limited resources. However, several recent projects have demonstrated that it is possible to achieve impressive results on a tight budget.

One practical approach is distillation, as shown by the Sky-T1 project. A team from UC Berkeley's Sky Computing Lab used just 17,000 carefully curated samples generated by another reasoning model to train a 32B parameter model for less than $450. The data was refactored into a more workable format using GPT-4o-mini, and the training took about 19 hours on a rack of 8 NVIDIA H100 GPUs. This distilled model approached the performance of an early version of o1 on several reasoning benchmarks, illustrating how effectively the capabilities of a large model can be transferred [[13]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450).![A table showing the performance of the Sky-T1 model on several benchmarks compared to an early version of OpenAI's o1.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)
Image 15: The performance of Sky-T1, a reasoning model trained for under $450. (Source [Sky-T1: Train your own O1 preview model within $450](https://novasky-ai.github.io/posts/sky-t1/))

Even pure RL can be applied at a smaller scale. The TinyZero project demonstrated this by training a 3B parameter model for under $30 on specific tasks like the countdown numbers game and multiplication. Built on the `veRL` framework, the model exhibited emergent self-verification and reasoning traces, reinforcing the idea that cold-start RL can produce useful behaviors without massive compute [[14]](https://github.com/Jiayi-Pan/TinyZero), [[31]](https://www.dailycal.org/news/campus/research-and-ideas/campus-researchers-replicate-disruptive-chinese-ai-for-30/article_a1cc5cd0-dee4-11ef-b8ca-171526dfb895.html). This emergence in smaller models is not random; it follows predictable scaling laws. Research suggests that pre-training loss, more so than just parameter count, is a key predictor for when these abilities will appear, often following a sharp transition once a critical loss threshold is passed [[20]](https://gregrobison.medium.com/emergent-properties-in-large-language-models-a-deep-research-analysis-d6886c37061b).![An image showing an example of the TinyZero model performing self-verification on the countdown numbers game.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)
Image 16: An example from the TinyZero repository demonstrating the model's self-verification capabilities. (Source [TinyZero GitHub Repository](https://github.com/Jiayi-Pan/TinyZero))

Another powerful, budget-conscious technique is **journey learning**. This paradigm shifts the focus of SFT from "shortcut learning," where models are only trained on "golden" solution paths, to training on the entire problem-solving journey. This includes incorrect paths, dead ends, self-corrections, and reflections [[15]](https://arxiv.org/abs/2410.18982).![A diagram comparing "shortcut learning" (a direct path to the correct answer) with "journey learning" (a path that includes incorrect branches and backtracking).](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)
Image 17: Journey learning includes incorrect solution paths in the training data, in contrast to traditional shortcut learning. (Source [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982))

By exposing the model to the full, messy process of human (or AI) thought, journey learning reinforces self-correction mechanisms. Models trained only on perfect solutions can be less robust and struggle when they encounter novel errors. In contrast, models trained on journey-style data learn how to recognize and recover from mistakes, leading to more reliable reasoning. This approach has shown great potential, with one study reporting an 8% performance boost on the MATH dataset using only 327 journey learning examples compared to shortcut learning [[15]](https://arxiv.org/abs/2410.18982). This method fosters a deeper understanding of the problem domain, moving beyond just knowing the correct answer to comprehending the process of arriving at it.

Looking ahead, the most effective budget-friendly approaches will likely involve hybrid pipelines. By combining insights from these projects—using distillation for efficient knowledge transfer (Sky-T1), pure RL for emergent behaviors (TinyZero), and journey learning for robustness—it is possible to create powerful reasoning models that balance cost, performance, and reliability.
```
**Grader reasoning:**
- `cc`: Developing reasoning models on a limited budget:
**1:** Both sections cover the same core ideas for developing reasoning models on a budget: distillation via Sky-T1, small-scale pure RL via TinyZero, and "journey learning" as an alternative to shortcut learning.
- `fl`: Developing reasoning models on a limited budget:
**1:** Both sections follow the same logical flow: distillation (Sky-T1), then pure RL (TinyZero), then journey learning, then a forward-looking close. A prior pass's claim that the generated section omits a "final summary paragraph" present in the expected output is incorrect — the generated section's closing paragraph ("Looking ahead, the most effective budget-friendly approaches will likely involve hybrid pipelines...") conveys the same forward-looking, combine-these-approaches sentiment as the expected output's closing sign-off, just in different words.
- `de`: Developing reasoning models on a limited budget:
**1:** [instances=1; quality=strong] A depth addition is present: when discussing TinyZero, the generated section adds that emergent self-verification abilities follow predictable scaling laws, with pre-training loss (more than parameter count) predicting when they appear, often via a sharp transition at a critical loss threshold. This qualifies as "theoretical foundations." Traceable to ref [20], gregrobison.medium.com/emergent-properties-in-large-language-models..., exploration-phase. Classified as strong: a specific, named mechanism (pre-training loss as predictor, critical threshold) rather than a generic claim. One candidate was evaluated and rejected: the "8% improvement with 327 training samples" journey-learning statistic, cited to ref [15] — this is the golden O1 Replication Journey paper, not an exploration-phase source, so it does not qualify.
- `be`: Developing reasoning models on a limited budget:
**0:** [instances=0] No breadth additions present.
- `cp`: Developing reasoning models on a limited budget:
**1:** The depth addition on scaling laws for smaller models is a relevant theoretical point that supports the discussion of the TinyZero project. It is a concise paragraph that enriches the core narrative without overshadowing it.
- `ga`: Developing reasoning models on a limited budget:
**0:** The generated section meets the substantive requirements — it details Sky-T1, TinyZero, and journey learning with their respective images, and outlines future directions. However, target 600, tolerance ±60, range 540-660. Exact count: 437. **103 words below the minimum.** This fails the word-count tolerance, so GuidelineAdherence scores 0. Confirmed per ruling: this shortfall is large enough to still result in a penalty.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset2`

**Article text:**
```
## Developing reasoning models on a limited budget

The cost of developing a reasoning model, even starting from an open-weight base, can be discouraging for researchers and engineers with limited budgets. Fortunately, several recent projects have demonstrated that it is possible to achieve impressive results without massive computational resources.

### Distillation on a Budget: The Sky-T1 Project

The Sky-T1 project from UC Berkeley's Sky Computing Lab exemplifies budget-conscious distillation. By fine-tuning a 32-billion-parameter open-source model on a curated dataset of just 17,000 samples generated by a more powerful reasoning model, the team trained their model for under $450 [[14]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450). The training took about 19 hours on a rack of 8 NVIDIA H100 GPUs. The resulting model approaches o1-preview performance on several reasoning benchmarks, showing how effective small-scale distillation can be.![Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)

Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article

### Pure RL at Small Scale: The TinyZero Project

The TinyZero project demonstrates that pure RL can yield results even at a much smaller scale. By training a 3B parameter model on specific tasks like the Countdown numbers game and multiplication, the researchers were able to elicit emergent self-verification and reasoning traces for under $30 [[16]](https://github.com/Jiayi-Pan/TinyZero). The project provides code and instructions to reproduce the "Aha moment" on a small scale, using a couple of GPUs. This reinforces the finding from DeepSeek-R1-Zero: a cold-start RL process can produce useful reasoning behaviors even without massive compute, provided the task has a clear, verifiable reward signal.![Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)

Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.

The emergence of such capabilities in small models is not random but can be predicted by scaling laws. Research shows that these abilities follow power-law scaling with compute, and that a model's pre-training loss is a better predictor of emergence than parameter count alone. A lower loss seems to be a prerequisite for these downstream skills to unlock during RL [[23]](https://www.emergentmind.com/topics/emergent-self-verification), [[24]](https://gregrobison.medium.com/emergent-properties-in-large-language-models-a-deep-research-analysis-d6886c37061b).

### Journey Learning: Training on the Entire Process

A third powerful, budget-friendly technique is "journey learning." This concept, explored in the O1 Replication Journey report, shifts the focus of supervised fine-tuning [[17]](https://arxiv.org/abs/2410.18982). Instead of training a model only on "shortcut" or "golden path" solutions, journey learning involves training on the entire problem-solving trajectory, including incorrect paths, self-corrections, and reflections. This paradigm is designed to teach the model not just the final answer, but the process of exploration, error, and recovery that mirrors human cognition.![Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. Annotated figure from the O1 Replication Journey: A Strategic Progress Report – Part 1](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)

Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. Annotated figure from the O1 Replication Journey: A Strategic Progress Report – Part 1

By exposing the model to mistakes and how to recover from them, journey learning reinforces self-correction mechanisms. This contrasts with shortcut-only datasets, which can lead to brittle behavior when the model encounters a novel error. The O1 Replication Journey report showed that with only 327 training samples, journey learning outperformed conventional SFT by over 8% on the MATH dataset, demonstrating its powerful potential [[17]](https://arxiv.org/abs/2410.18982).

Looking ahead, the most effective budget-conscious pipelines will likely be hybrids. One could imagine combining insights from all these projects: using journey learning to create a high-quality, error-inclusive dataset, distilling it into a smaller model like Sky-T1, and then running a final, targeted RL polish similar to TinyZero. This would balance cost, emergent behavior, and reliability. These budget-conscious approaches provide a path forward for the entire community, complementing the large-scale industrial efforts and enriching our understanding of the core techniques.
```
**Grader reasoning:**
- `cc`: Developing reasoning models on a limited budget:
**1:** Both sections cover Sky-T1 (Sky Computing Lab, 32B, <$450, ~17K samples, 19 hours/8 H100 GPUs, near-o1 performance), TinyZero (3B, Countdown and multiplication, <$30, emergent self-verification), and journey learning (shortcut vs. journey framing, the 327-sample/8%+ MATH improvement figure), closing on a hybrid-future outlook. All expected ideas, including both named TinyZero tasks, are present.
- `fl`: Developing reasoning models on a limited budget:
**1:** The generated section follows the same progression as the expected one: Sky-T1, TinyZero, journey learning, hybrid-future close. Figures 15, 16, and 17 each land at the same relative position as their expected counterparts, and the exploration-grounded scaling-laws addition between TinyZero and journey learning has its own topic sentence and does not disrupt the surrounding order.
- `de`: Developing reasoning models on a limited budget:
**1:** [instances=1; quality=strong] One qualifying depth addition: "these abilities follow power-law scaling with compute, and that a model's pre-training loss is a better predictor of emergence than parameter count alone," traceable to two exploration-phase sources (emergentmind.com and gregrobison.medium.com) closely, cited [23], [24]. This qualifies as 'theoretical foundations or mathematical underpinnings' explaining why TinyZero-scale models can exhibit emergent behavior. Classified as strong: a specific, named mechanism (pre-training loss as predictor) rather than a generic claim.
- `be`: Developing reasoning models on a limited budget:
**0:** [instances=0] research.md's exploration-phase sources include a depth-qualifying instance credited above (the power-law-scaling addition), but no breadth-qualifying addition is present in this section.
- `cp`: Developing reasoning models on a limited budget:
**1:** depth_enhancement scored 1 for this section (the power-law-scaling addition). The addition is a contained paragraph placed between the TinyZero and journey-learning discussions, and the section's dominant narrative — Sky-T1, TinyZero, and journey learning as budget-conscious projects — remains clearly the primary focus. CorePreservation scores 1.
- `ga`: Developing reasoning models on a limited budget:
**0:** Sky-T1, TinyZero, and journey learning are all covered with their required figures. However, prose-only word count is approximately 508 words against a 600-word target (±60 tolerance, range 540–660 words), 32 words below the minimum — outside tolerance, consistent with this section falling short in every preset graded so far for this lesson.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset2`

**Article text:**
```
## Developing reasoning models on a limited budget

The development costs of reasoning models, even when starting from an open-weight base, can be discouraging for researchers and engineers with limited budgets. However, several recent projects have shown that it is possible to achieve impressive reasoning capabilities without massive computational resources.

One of the most practical approaches is distillation. The **Sky-T1** project from UC Berkeley's Sky Computing Lab is a prime example. By carefully curating a dataset of just 17,000 high-quality reasoning examples and using them to fine-tune a 32B parameter model, the team was able to approach the performance of an early version of OpenAI's o1 on several benchmarks. The entire training process cost less than $450, illustrating that smart data curation and distillation can be an extremely effective, budget-conscious strategy [[16]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450).![Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)
Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article [[17]](https://novasky-ai.github.io/posts/sky-t1/). (Source [https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png))

It is also possible to explore pure RL on a smaller scale. The **TinyZero** project demonstrated this by training a 3B parameter model on specific tasks like the Countdown game for under $30 [[18]](https://github.com/Jiayi-Pan/TinyZero), [[19]](https://www.dailycal.org/news/campus/research-and-ideas/campus-researchers-replicate-disruptive-chinese-ai-for-30/article_a1cc5cd0-dee4-11ef-b8ca-171526dfb895.html). Even at this small scale, the model exhibited emergent behaviors like self-verification, reinforcing the idea that the "cold-start" RL approach can yield useful reasoning patterns without massive compute.

This emergence of capabilities in smaller models is not entirely random. Research suggests it is governed by predictable scaling laws. A key insight is that a model's pre-training loss is a more fundamental predictor of emergent abilities than parameter count alone [[25]](https://gregrobison.medium.com/emergent-properties-in-large-language-models-a-deep-research-analysis-d6886c37061b). This implies that even a sub-7B model can develop sophisticated behaviors like self-verification if it is trained efficiently enough to reach a critical loss threshold, providing a theoretical basis for projects like TinyZero.![Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)
Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification [[18]](https://github.com/Jiayi-Pan/TinyZero). (Source [https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png))

Another promising, low-cost technique is **journey learning**. This concept, explored in the O1 Replication Journey report, proposes a shift in how we approach SFT [[20]](https://arxiv.org/abs/2410.18982). Instead of training a model only on "shortcut" solutions (the direct, correct path to an answer), journey learning involves training on the entire problem-solving trajectory, including incorrect paths, self-corrections, and backtracking.![Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. Annotated figure from the O1 Replication Journey: A Strategic Progress Report – Part 1](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)
Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. Annotated figure from the O1 Replication Journey: A Strategic Progress Report – Part 1 [[20]](https://arxiv.org/abs/2410.18982). (Source [https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png))

By exposing the model to its own mistakes and the process of correcting them, it learns more robust self-correction mechanisms. A model trained only on "golden" solutions may be brittle when it encounters a novel error, as it has never seen a recovery path. In contrast, a model trained on journey-style data is better equipped to recognize and correct its own mistakes. The O1 Replication Journey report showed that with only 327 training samples, journey learning outperformed conventional shortcut learning by over 8% on the MATH dataset, demonstrating its potential [[20]](https://arxiv.org/abs/2410.18982).

The future of budget-conscious reasoning model development likely lies in combining insights from these projects. A hybrid pipeline could involve using a small-scale RL model like TinyZero to generate initial reasoning traces, curating them using journey learning principles, and then using that high-quality, small dataset to distill a capable model, similar to the Sky-T1 approach. This would balance the emergent discovery of RL with the efficiency of distillation, offering a path to powerful reasoning without an enormous budget.
```
**Grader reasoning:**
- `cc`: Developing reasoning models on a limited budget:
**1:** Both sections cover Sky-T1 (Sky Computing Lab, 32B, <$450, ~17K samples, near-o1 performance), TinyZero (3B, <$30, emergent self-verification, extended with a well-grounded theoretical-basis caveat), and journey learning (shortcut vs. journey framing, the 327-sample/8%+ MATH improvement figure), closing on a hybrid-future outlook. The generated section names only the Countdown game for TinyZero rather than both example tasks the expected section names — a single dropped example, not treated as a missing substantive idea.
- `fl`: Developing reasoning models on a limited budget:
**1:** The generated section follows the same progression as the expected one: Sky-T1, TinyZero (with its exploration-grounded scaling-laws addition inserted with its own clear lead-in before the figure, not disrupting the underlying TinyZero-then-figure order once the addition is stepped over), journey learning, hybrid-future close. The journey-learning figure is placed immediately after the definition rather than after the self-correction-reinforcement discussion as in the expected section — the same narrow, single-idea-adjacent reordering already ruled too trivial to count as a placement failure.
- `de`: Developing reasoning models on a limited budget:
**1:** [instances=1; quality=strong] One qualifying depth addition: "a model's pre-training loss is a more fundamental predictor of emergent abilities than parameter count alone... even a sub-7B model can develop sophisticated behaviors like self-verification if trained efficiently enough to reach a critical loss threshold, providing a theoretical basis for projects like TinyZero" [25], traceable to an exploration-phase source (gregrobison.medium.com) closely. This qualifies as 'theoretical foundations or mathematical underpinnings.' Classified as strong: a specific, named mechanism (pre-training loss as predictor) rather than a generic claim.
- `be`: Developing reasoning models on a limited budget:
**0:** [instances=0] research.md's exploration-phase sources include a depth-qualifying instance credited above (the scaling-laws addition), but no breadth-qualifying addition is present in this section.
- `cp`: Developing reasoning models on a limited budget:
**1:** depth_enhancement scored 1 for this section (the scaling-laws addition). The addition is a contained paragraph placed after the TinyZero description and before the figure, and the section's dominant narrative — Sky-T1, TinyZero, and journey learning as budget-conscious projects — remains clearly the primary focus. CorePreservation scores 1.
- `ga`: Developing reasoning models on a limited budget:
**0:** Sky-T1, TinyZero, and journey learning are all covered with their required figures, plus well-grounded theoretical detail. However, prose-only word count is approximately 482 words against a 600-word target (±60 tolerance, range 540–660 words), 58 words below the minimum — outside tolerance. This section has now fallen short in every preset graded for this lesson across both replicates (8 for 8).

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset3`

**Article text:**
```
## Developing reasoning models on a limited budget

The development costs for frontier reasoning models are substantial, even when starting from an open-weight base model. This can be discouraging for researchers and engineers with limited budgets. Fortunately, recent projects have demonstrated effective, budget-conscious methods for developing reasoning capabilities.

One practical approach is **distillation**, as shown by the **Sky-T1** project from UC Berkeley’s Sky Computing Lab. The team created Sky-T1-32B-Preview, a reasoning model competitive with early versions of o1, by fine-tuning on just 17,000 carefully curated samples. The entire training process cost under \$450 [[19]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450). This illustrates how the distillation concept we covered earlier can be scaled down effectively.![Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article.](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)

Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article.

Another method is **pure RL at a smaller scale**. The **TinyZero** project successfully reproduced DeepSeek-R1-Zero's emergent behaviors on a 3B parameter model for under \$30. The model was trained on countdown and multiplication tasks and learned self-verification and search abilities on its own [[20]](https://github.com/Jiayi-Pan/TinyZero). This reinforces the finding that cold-start RL can produce useful reasoning behaviors even without massive compute.![Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)

Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.

A third, and perhaps most innovative, budget-friendly technique is **journey learning**. This concept, introduced in the "O1 Replication Journey" paper, contrasts with traditional "shortcut learning," where models are only trained on correct, optimal solutions. In journey learning, the training data includes the entire problem-solving process: incorrect paths, self-corrections, and reflections, culminating in the final success [[11]](https://arxiv.org/abs/2410.18982).![Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data.](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)

Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. (Source [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982))

By exposing the model to mistakes during SFT, we reinforce the self-correction mechanisms that are crucial for robust reasoning. A model trained only on "golden paths" can be brittle; when it encounters a novel error, it does not know how to recover. In contrast, a model trained on journey-style data has learned to recognize and navigate failures. The "O1 Replication Journey" paper showed that with only 327 training samples, journey learning outperformed shortcut learning by over 8% on the MATH dataset, demonstrating its powerful potential [[11]](https://arxiv.org/abs/2410.18982).

While powerful, journey learning is not without its failure modes. If the training data is dominated by incorrect paths, the model can learn to persistently generate wrong answers or get stuck in unstable convergence loops. A key challenge is balancing the ratio of error paths to "golden paths" to teach self-correction without reinforcing bad habits [[21]](https://arxiv.org/html/2510.01624v1), [[22]](https://arxiv.org/html/2604.10079v2).

Looking ahead, the most effective budget-conscious pipelines will likely be hybrids. We can combine insights from these projects: using distillation like Sky-T1 for efficient knowledge transfer, applying small-scale pure RL like TinyZero to encourage emergent behaviors, and incorporating journey learning to build robust self-correction capabilities. This allows for a balance between cost, performance, and reliability.
```
**Grader reasoning:**
- `cc`: Developing reasoning models on a limited budget:
**1:** Both sections discuss the same core topic: developing reasoning models on a limited budget, covering distillation (Sky-T1), small-scale pure RL (TinyZero), and "journey learning" as an alternative to traditional SFT.
- `fl`: Developing reasoning models on a limited budget:
**1:** Both sections follow the same logical progression: acknowledging the high cost of frontier models, then introducing budget-friendly alternatives in sequence — distillation (Sky-T1), pure RL (TinyZero), and journey learning.
- `de`: Developing reasoning models on a limited budget:
**1:** [instances=1; quality=strong] A depth addition is present: the section discusses the specific failure modes of journey learning — persistently generating wrong answers or getting stuck in unstable convergence loops if error paths dominate the training data, and the challenge of balancing the error-path-to-golden-path ratio. This qualifies as "limitations, criticisms, or failure modes of the core topic." Traceable to ref [21] (arxiv.org/html/2510.01624v1) and ref [22] (arxiv.org/html/2604.10079v2), both confirmed inside the exploration-phase block, treated as one instance since both support the same claim in the same paragraph. Classified as strong: a specific mechanism (error-path domination causing persistent errors/unstable convergence) rather than a generic caveat.
- `be`: Developing reasoning models on a limited budget:
**0:** [instances=0] No breadth additions present.
- `cp`: Developing reasoning models on a limited budget:
**1:** The depth addition on journey learning's failure modes is a concise, relevant paragraph that enriches the core topic without overshadowing the main narrative about budget-friendly techniques.
- `ga`: Developing reasoning models on a limited budget:
**0:** The generated section meets its substantive requirements — contrary to a prior pass's claim, it DOES explicitly mention the failure mode of shortcut-only training ("A model trained only on 'golden paths' can be brittle; when it encounters a novel error, it does not know how to recover," line 159). The actual disqualifying issue is word count: the prose-only word count is approximately 408 words, well below the required 540–660 range (600-word target ±10%). This fails the word-count tolerance, so GuidelineAdherence scores 0.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset3`

**Article text:**
```
## Developing reasoning models on a limited budget

The development costs for state-of-the-art reasoning models can be discouraging for teams with limited budgets. However, recent open-source projects have demonstrated that it is possible to achieve impressive reasoning capabilities without massive computational resources.

One practical approach is distillation, as demonstrated by the **Sky-T1** project from UC Berkeley’s Sky Computing Lab. By fine-tuning a 32B parameter model on a carefully curated dataset of 17,000 reasoning examples, the team was able to create a model competitive with early versions of OpenAI's o1 on several benchmarks. The entire training process cost less than \$450, showcasing how effective distillation can be when paired with high-quality data [[28]](https://www.linkedin.com/posts/muhammad-ali-masood-phd_researchers-open-source-sky-t1-a-reasoning-activity-7285536292493299712-M8b5), [[29]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450).![Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)
Image 15: Benchmark results for the budget-friendly Sky-T1 model. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Even pure RL can be applied at a smaller scale. The **TinyZero** project successfully reproduced DeepSeek R1-Zero's emergent behaviors on a 3B parameter model for under \$30 [[30]](https://github.com/Jiayi-Pan/TinyZero). By focusing on specific tasks like the Countdown numbers game, the model learned self-verification and search abilities on its own, reinforcing the idea that cold-start RL can yield useful results even without massive compute [[31]](https://huggingface.co/blog/open-r1/mini-r1-contdown-game), [[32]](https://www.dailycal.org/news/campus/research-and-ideas/campus-researchers-replicate-disruptive-chinese-ai-for-30/article_a1cc5cd0-dee4-11ef-b8ca-171526dfb895.html).![Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)
Image 16: An example from the TinyZero repository showing the model's self-verification capabilities. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Another promising, budget-conscious technique is **journey learning**. This paradigm shifts from "shortcut learning," where models are only trained on correct solution paths, to a more holistic approach. In journey learning, the training data includes the entire problem-solving process: incorrect paths, self-corrections, and reflections, culminating in the final success. The "O1 Replication Journey" paper found that training a model on just 327 examples of these full "journeys" improved performance on the MATH dataset by over 8% compared to training on only the correct "shortcut" solutions [[33]](https://arxiv.org/abs/2410.18982).![Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. Annotated figure from the O1 Replication Journey: A Strategic Progress Report – Part 1](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)
Image 17: Journey learning includes incorrect solution paths in the SFT data, unlike traditional shortcut learning. (Source: [arxiv.org](https://arxiv.org/abs/2410.18982) [[33]](https://arxiv.org/abs/2410.18982))

By exposing the model to the process of making and correcting mistakes, journey learning reinforces self-correction mechanisms. This contrasts with models trained only on "golden" solutions, which can become brittle and fail when they encounter novel errors.

However, journey learning is not without its failure modes. If the training data is dominated by error paths, it can lead to unstable convergence or even cause the model to persistently generate incorrect answers, as the fine-tuning objective conflicts with the base model's prior knowledge [[34]](https://arxiv.org/html/2510.01624v1). There is also a risk of overfitting to specific types of errors in the data, which can paradoxically increase the frequency of certain mistakes while improving overall accuracy [[35]](https://aclanthology.org/2025.findings-acl.605.pdf).

Looking ahead, the most effective budget-friendly strategies will likely be hybrids. By combining insights from these projects—using high-quality distilled data like Sky-T1, fostering emergent behaviors with small-scale RL like TinyZero, and building robustness with journey learning—teams can create powerful reasoning models that balance cost, performance, and reliability. Future work could explore pipelines that use journey learning data for a cold-start SFT, followed by a small-scale RL phase, and finally, distillation to an even smaller, more efficient model.
```
**Grader reasoning:**
- `cc`: Developing reasoning models on a limited budget:
**1:** Both sections cover Sky-T1 (Sky Computing Lab, 32B, <$450, ~17K samples, near-o1 performance), TinyZero (3B, Countdown game, <$30, emergent self-verification), and journey learning (shortcut vs. journey framing, self-correction reinforcement, plus well-grounded failure-mode caveats), closing on a hybrid-future outlook with a concrete suggested pipeline. The generated section names only the Countdown game for TinyZero rather than both example tasks the expected section names — a single dropped example, not treated as a missing substantive idea.
- `fl`: Developing reasoning models on a limited budget:
**1:** The generated section follows the same progression as the expected one: Sky-T1, TinyZero, journey learning, hybrid-future close. Images 15 and 16 land in the same relative position as their expected counterparts. Image 17 is placed after the exploration-grounded 327-sample/8% statistic (an addition not present in the expected section at all) rather than immediately after the shortcut-vs-journey definition as in the expected section — but stepping over that addition, the underlying reordering is a single-idea-adjacent shift of the same narrow kind already ruled too trivial to count as a placement failure (see summary).
- `de`: Developing reasoning models on a limited budget:
**1:** [instances=2; quality=strong,strong] Two qualifying depth additions, each traceable to a distinct exploration-phase source. (1) "If the training data is dominated by error paths, it can lead to unstable convergence or even cause the model to persistently generate incorrect answers, as the fine-tuning objective conflicts with the base model's prior knowledge" [34], traceable to an exploration source on journey-learning failure modes closely. (2) "There is also a risk of overfitting to specific types of errors in the data, which can paradoxically increase the frequency of certain mistakes while improving overall accuracy" [35], traceable to a distinct exploration source on SFT error analysis closely. Both qualify as 'limitations, criticisms, or failure modes of the core topic' and are classified strong: specific, named failure mechanisms rather than generic cautions.
- `be`: Developing reasoning models on a limited budget:
**0:** [instances=0] research.md's exploration-phase sources include two depth-qualifying instances credited above (the failure-mode additions), but no breadth-qualifying addition — one that connects outward to an adjacent field — is present in this section.
- `cp`: Developing reasoning models on a limited budget:
**1:** depth_enhancement scored 1 for this section (two failure-mode additions). Each is a contained paragraph placed after the core journey-learning explanation, and the section's dominant narrative — Sky-T1, TinyZero, and journey learning as budget-conscious projects — remains clearly the primary focus. CorePreservation scores 1.
- `ga`: Developing reasoning models on a limited budget:
**0:** Sky-T1, TinyZero, and journey learning are all covered with their required figures, plus well-grounded failure-mode detail. However, prose-only word count is approximately 438 words against a 600-word target (±60 tolerance, range 540–660 words), 102 words below the minimum — outside tolerance, and this section has now fallen short in every preset graded for this lesson.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset3`

**Article text:**
```
## Developing reasoning models on a limited budget

The development costs of reasoning models, even when starting from an open-weight base, can be discouraging for researchers and engineers with limited budgets. Fortunately, several recent projects have demonstrated effective, budget-conscious approaches.

One of the most practical methods is **distillation**, as shown by the Sky-T1 project from UC Berkeley’s Sky Computing Lab. By curating a dataset of just 17,000 high-quality reasoning samples, they were able to train a model for under $450 that is competitive with an earlier version of OpenAI's o1 on several reasoning benchmarks. This illustrates how the distillation concept can be scaled down effectively, providing a powerful yet affordable path to specialized reasoning [[23]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450).![Image 15: Benchmark results for the Sky-T1-32B-Preview model.](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)
Image 15: Benchmark results for the Sky-T1-32B-Preview model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

**Pure RL at a small scale** has also shown promise. The TinyZero project trained a 3B parameter model for under $30 on specific tasks like countdown and multiplication. Even at this small scale, the model exhibited emergent self-verification and reasoning traces, reinforcing the idea that cold-start RL can produce useful behaviors without massive compute [[24]](https://github.com/Jiayi-Pan/TinyZero).![Image 16: A figure from the TinyZero repository showing that the model is capable of self-verification.](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)
Image 16: A figure from the TinyZero repository showing that the model is capable of self-verification (Source [[24]](https://github.com/Jiayi-Pan/TinyZero)).

A third, and perhaps most interesting, budget-friendly approach is **journey learning**. This concept, explored in the O1 Replication Journey report, contrasts with "shortcut learning," where models are only trained on "golden paths" or correct solutions. Journey learning involves training the model on the full problem-solving trajectory, including incorrect paths, self-corrections, and backtracking [[25]](https://arxiv.org/abs/2410.18982).![Image 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solution paths in the SFT data.](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)
Image 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solution paths in the SFT data. Annotated figure from the O1 Replication Journey: A Strategic Progress Report – Part 1 (Source [[25]](https://arxiv.org/abs/2410.18982)).

By exposing the model to mistakes during SFT, it learns robust self-correction mechanisms. Models trained only on perfect solutions can be brittle and struggle when they encounter novel errors. In contrast, a model trained with journey learning understands how to identify and recover from mistakes. However, this approach requires careful data balancing. If incorrect paths and self-corrections dominate the training data distribution, it can lead to unstable convergence or even cause the model to persistently generate incorrect answers, as the error patterns can conflict with the base model's pretrained knowledge [[26]](https://arxiv.org/html/2510.01624v1). The O1 Replication Journey report showed that with only 327 training samples, journey learning outperformed conventional SFT by over 8% on the MATH dataset, demonstrating its powerful potential [[25]](https://arxiv.org/abs/2410.18982).

Future directions will likely involve combining insights from these budget-conscious projects. Hybrid pipelines that use distillation for a strong baseline, incorporate journey learning data to build robustness, and apply small-scale RL for targeted improvements could offer a balanced approach to developing capable and reliable reasoning models without breaking the bank.
```
**Grader reasoning:**
- `cc`: Developing reasoning models on a limited budget:
**1:** Both sections cover Sky-T1 (Sky Computing Lab, 32B, <$450, ~17K samples, near-o1 performance), TinyZero (3B, Countdown and multiplication, <$30, emergent self-verification), and journey learning (shortcut vs. journey framing, the 327-sample/8%+ MATH improvement figure, plus a well-grounded failure-mode caveat), closing on a hybrid-future outlook. All expected ideas, including both named TinyZero tasks, are present.
- `fl`: Developing reasoning models on a limited budget:
**1:** The generated section follows the same progression as the expected one: Sky-T1, TinyZero, journey learning (with its exploration-grounded failure-mode addition carrying its own local lead-in), hybrid-future close. The Sky-T1 and TinyZero figures land in the same relative position as their expected counterparts. The journey-learning figure is placed immediately after the definition rather than after the self-correction-reinforcement discussion as in the expected section — the same narrow, single-idea-adjacent reordering already ruled too trivial to count as a placement failure.
- `de`: Developing reasoning models on a limited budget:
**1:** [instances=1; quality=strong] One qualifying depth addition: "if incorrect paths and self-corrections dominate the training data distribution, it can lead to unstable convergence or even cause the model to persistently generate incorrect answers, as the error patterns can conflict with the base model's pretrained knowledge" [26], traceable to an exploration-phase source on journey-learning failure modes closely. This qualifies as 'limitations, criticisms, or failure modes of the core topic.' Classified as strong: a specific, named failure mechanism rather than a generic caution.
- `be`: Developing reasoning models on a limited budget:
**0:** [instances=0] research.md's exploration-phase sources include a depth-qualifying instance credited above (the failure-mode addition), but no breadth-qualifying addition is present in this section.
- `cp`: Developing reasoning models on a limited budget:
**1:** depth_enhancement scored 1 for this section (one strong failure-mode addition). The addition is a contained paragraph placed after the core journey-learning explanation, and the section's dominant narrative remains clearly the primary focus. CorePreservation scores 1.
- `ga`: Developing reasoning models on a limited budget:
**0:** Sky-T1, TinyZero, and journey learning are all covered with their required figures, plus well-grounded failure-mode detail. However, prose-only word count is approximately 381 words against a 600-word target (±60 tolerance, range 540–660 words), 159 words below the minimum — the largest shortfall yet for this section, which has now fallen short in every preset graded for this lesson across both replicates (9 for 9).

## Section: S3::section-3-when-should-we-use-reasoning-models  (weight=0.037, contribution=+0.0035 FOR standard)
Stored section rewards: standard=0.4310  deep=0.4173  (explore: standard=0.1207  deep=0.0866)

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
**0:** The generated section meets the substantive requirements — it identifies tasks where reasoning models excel versus where they are overkill, catalogs the practical downsides, includes the specified image, and provides the transition. Target 160, tolerance ±25, range 135-185. Exact count: 205. **20 words above the maximum.** Same open question as Section 1: this is an overage, not a shortfall, so the recent shortfall-leniency ruling doesn't directly settle it. Scoring 0 conservatively pending that determination — flagged as borderline, see summary.

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

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset3`

**Article text:**
```
## When should we use reasoning models?

Before diving into the technical details, it is important to know when to use a reasoning model. They deliver the highest returns on tasks that require decomposition, self-correction, or complex logic, such as puzzles, advanced mathematics, and competitive coding. For tasks like summarization, simple factual question-answering, or creative writing, a general-purpose model is often sufficient and more efficient.

The power of reasoning models comes with practical downsides. Their verbose, intermediate steps lead to higher latency and token costs. This can frustrate users in conversational settings who expect quick answers. There is also the risk of overthinking, where the model might invent unnecessary complications for a straightforward problem that a base model would have solved correctly in a single pass [[4]](https://arxiv.org/abs/2501.18585). This trade-off between capability and efficiency is a central challenge in applying these models effectively.![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)

Figure 4: The key strengths and weaknesses of reasoning models.

Understanding when to deploy these specialized models is key. This leads us to a concrete, open pipeline that demonstrates how such capabilities are created at scale: the DeepSeek-R1 series.
```
**Grader reasoning:**
- `cc`: When should we use reasoning models?:
**1:** Both sections cover the same core ideas: reasoning models are best for complex tasks like puzzles and advanced math, while general-purpose models are better for simpler tasks. They both discuss the same disadvantages, including higher latency/cost and the risk of "overthinking."
- `fl`: When should we use reasoning models?:
**1:** Both sections follow the same logical progression: explaining when to use reasoning models, then discussing the practical downsides, then a summary figure.
- `de`: When should we use reasoning models?:
**0:** [instances=0] One candidate evaluated: the overthinking/single-pass-error point, cited to ref [4], "Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs" (arxiv.org/abs/2501.18585) — confirmed scraped into research.md's exploitation-phase block ("the-state-of-llm-reasoning-model-inference.md"), not exploration. This candidate also restates content already present in the expected output rather than introducing a new addition, so it fails on both counts; either way, the score is 0.
- `be`: When should we use reasoning models?:
**0:** [instances=0] No breadth additions present.
- `cp`: When should we use reasoning models?:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so CorePreservation is 1 by default as there are no qualifying additions to evaluate.
- `ga`: When should we use reasoning models?:
**1:** The generated section meets all requirements: it identifies tasks where reasoning models excel versus where they are overkill, catalogs the practical downsides, includes the specified image, and provides the transition. The prose-only word count is approximately 163 words, within the 160-word target's 135–185 range.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset3`

**Article text:**
```
## When should we use reasoning models?

Before diving into the technical details, it is important to know when reasoning models are truly needed. They deliver the highest returns on tasks that require decomposition or self-correction, such as puzzles, advanced mathematics, and competitive coding. However, they are often overkill for summarization, simple factual question-answering, or creative writing, where direct generation is sufficient.

Their practical downsides are significant. The verbose intermediate steps lead to higher latency and token costs [[3]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison), [[4]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o). For a basic task, a model like GPT-4o might respond in under a second, while a reasoning model like o1 could take minutes to "overthink" its way to the same answer [[4]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o). This increased verbosity can also frustrate users in conversational settings. Furthermore, there is a risk of "overthinking," where a model might invent unnecessary complications for a straightforward problem that a base model would have solved correctly in a single pass [[5]](https://arxiv.org/abs/2501.18585). This tendency to generate excessive tokens, even for simple problems, is a known side effect of optimizing for long chain-of-thought reasoning [[6]](https://papers.neurips.cc/paper_files/paper/2025/file/3e22bea3b170f4c2aebb9c48d98ae64d-Paper-Conference.pdf).![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)
Image 4: The key strengths and weaknesses of reasoning models.

Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.
```
**Grader reasoning:**
- `cc`: When should we use reasoning models?:
**1:** Both sections cover the same needed-vs-not-needed task split, the same practical downsides (latency/cost with a concrete GPT-4o-vs-o1 timing example, verbosity, overthinking), and the same closing strengths/weaknesses figure. The exploration-grounded 'known side effect of optimizing for long CoT' addition does not displace any expected idea.
- `fl`: When should we use reasoning models?:
**1:** The generated section follows the same progression as the expected one: needed-vs-not-needed framing, downsides (with its exploration-grounded addition carrying its own local lead-in), Image 4, then the transition.
- `de`: When should we use reasoning models?:
**1:** [instances=1; quality=standard] One qualifying depth addition: "this tendency to generate excessive tokens, even for simple problems, is a known side effect of optimizing for long chain-of-thought reasoning" [6], traceable to the exploration-phase 'thinking-optimal test-time scaling' source closely. This qualifies as 'limitations, criticisms, or failure modes of the core topic.' Classified as standard: a brief, single-sentence mention.
- `be`: When should we use reasoning models?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: When should we use reasoning models?:
**1:** depth_enhancement scored 1 for this section (one standard-tier overthinking addition). The addition is a single sentence within the existing downsides discussion and does not shift the section's focus away from when-to-use guidance. CorePreservation scores 1.
- `ga`: When should we use reasoning models?:
**1:** All required content elements are present. Prose-only word count is approximately 186 words against a 160-word target (±25 tolerance floor, range 135–185 words), 1 word above the upper bound — treated as negligible noise.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset3`

**Article text:**
```
## When should we use reasoning models?

Before diving into the technical details, it is important to know when reasoning models are truly needed. They deliver the highest returns on complex problems that require decomposition, logical deduction, or self-correction, such as puzzles, advanced mathematics, and competitive coding. However, they are often overkill for tasks like summarization, simple factual question-answering, or creative writing, where direct generation is sufficient.

The practical downsides are notable. The verbose intermediate steps lead to higher latency and token costs. This increased verbosity can also frustrate users in conversational settings who just want a quick answer. Furthermore, there is a risk of "overthinking," where the model invents unnecessary complications for straightforward problems. This can degrade not only efficiency but also accuracy, as models may fail to reliably identify their own errors or get stuck in reflective loops with diminishing returns [[2]](https://arxiv.org/abs/2501.18585), [[3]](https://papers.neurips.cc/paper_files/paper/2025/file/3e22bea3b170f4c2aebb9c48d98ae64d-Paper-Conference.pdf), [[4]](https://arxiv.org/html/2505.24726v1).![Image 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)
Image 4: The key strengths and weaknesses of reasoning models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.
```
**Grader reasoning:**
- `cc`: When should we use reasoning models?:
**1:** Both sections cover the same needed-vs-not-needed task split, the same practical downsides (latency/cost, verbosity, overthinking, extended here with exploration-grounded detail about self-error identification and diminishing returns).
- `fl`: When should we use reasoning models?:
**1:** The generated section follows the same progression as the expected one: needed-vs-not-needed framing, downsides (with its exploration-grounded addition carrying its own local lead-in), the figure, then the transition.
- `de`: When should we use reasoning models?:
**1:** [instances=1; quality=strong] One qualifying depth addition: "models may fail to reliably identify their own errors or get stuck in reflective loops with diminishing returns," traceable to an exploration-phase source on reflection effectiveness closely (which discusses "inability to reliably identify self-errors without oracles, diminishing returns from repeated reflection" nearly verbatim) and cited to it [4], alongside a co-citation [3] to a second exploration-phase source and a non-exploration citation [2] for the same sentence. This qualifies as 'limitations, criticisms, or failure modes of the core topic.' Classified as strong: a specific, multi-clause mechanism description rather than a generic mention.
- `be`: When should we use reasoning models?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: When should we use reasoning models?:
**1:** depth_enhancement scored 1 for this section (one strong addition). The addition is a contained clause within the existing downsides discussion and does not shift the section's focus away from when-to-use guidance. CorePreservation scores 1.
- `ga`: When should we use reasoning models?:
**1:** All required content elements are present. Prose-only word count is approximately 159 words against a 160-word target (±25 tolerance floor, range 135–185 words), within tolerance.

## Section: S6::section-6-thoughts-about-deepseek-r1  (weight=0.081, contribution=+0.0038 FOR standard)
Stored section rewards: standard=0.3436  deep=0.2974  (explore: standard=0.0000  deep=0.0000)

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
**1:** The generated section meets all requirements: it expresses appreciation for the open license and detailed report, compares R1 with o1 noting the training-heavy vs. inference-heavy trade-off, notes the limits of comparison due to OpenAI's secrecy, and discusses training cost realities. Target 350, tolerance ±35, range 315-385. Exact count: 319. Within range.

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

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset3`

**Article text:**
```
## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 series is a major moment for AI engineering. We appreciate not only the models themselves but also the open MIT license and the unusually detailed technical report that accompanied them. This level of transparency is rare and provides an invaluable blueprint for the community. The paper's demonstration that pure RL from a cold start can produce emergent reasoning and self-correction is a powerful proof of concept.

When comparing DeepSeek-R1 head-to-head with OpenAI's o1, the benchmarks show comparable quality on math and coding tasks. However, R1 appears to have superior inference efficiency, with API prices around 30 times lower than o1's [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1). This suggests different philosophical bets: DeepSeek invested heavily in a more efficient, training-intensive architecture, while o1 seems to lean more on expensive inference-time scaling to achieve its results.

However, any direct comparison is limited because OpenAI has disclosed very little about o1. We do not know its size, whether it uses a Mixture-of-Experts (MoE) architecture like DeepSeek, or the exact mix of training techniques. Without this information, attributing performance gaps is difficult, and a direct comparison is not entirely warranted.

There is also ambiguity around the training cost. The widely cited $6M figure for DeepSeek likely refers to the pre-training of the V3 base model, not the full R1 reasoning specialization [[18]](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1). The DeepSeek team has never disclosed the exact total GPU hours or full development cost for R1. While their paper provides some figures for specific training phases, these numbers exclude the extensive experimentation, data curation, and human annotation required, leaving the true incremental cost of reasoning specialization undisclosed [[5]](https://www.nature.com/articles/s41586-025-09422-z).

Despite these questions, DeepSeek-R1 stands as a milestone. It proves that high-level reasoning capabilities need not be the exclusive domain of closed labs. By providing both powerful models and a detailed recipe, DeepSeek has accelerated open research into all four of the core reasoning techniques we have discussed.
```
**Grader reasoning:**
- `cc`: Thoughts about DeepSeek R1:
**1:** Both sections provide a comparative analysis of DeepSeek-R1 and OpenAI's o1, discussing benchmark performance, inference efficiency, and the lack of transparency from OpenAI, and both address the ambiguity around training costs. The core arguments are the same.
- `fl`: Thoughts about DeepSeek R1:
**1:** Both sections follow a similar logical flow: general thoughts on the release, a direct comparison with o1, the efficiency and philosophical differences, and then the training cost ambiguity.
- `de`: Thoughts about DeepSeek R1:
**0:** [instances=0] No depth additions present. The section provides a good summary and comparison but does not introduce new technical details or limitations beyond what is covered in the expected output. The $6M/V3-base-model cost clarification is cited to ref [18], epoch.ai/gradient-updates/what-went-into-training-deepseek-r1, confirmed in research.md's exploitation-phase block (both as a Q&A source and a fully scraped article), not exploration — so even if treated as an addition, it would not qualify for the gate.
- `be`: Thoughts about DeepSeek R1:
**0:** [instances=0] No breadth additions present.
- `cp`: Thoughts about DeepSeek R1:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so CorePreservation is 1 by default as there are no qualifying additions to evaluate.
- `ga`: Thoughts about DeepSeek R1:
**1:** The generated section meets its substantive requirements — contrary to a prior pass's claim, it DOES mention the specific "$6M figure" and clarifies it likely refers to the V3 base model pre-training (line 139), matching the guideline's requirement. The actual disqualifying issue is word count: the prose-only word count is approximately 312 words, 3 words below the required 315–385 range (350-word target ±10%). Per the confirmed ruling that shortfalls of this size (single digits, well below the ~100+-word cases that do get penalized) do not warrant a penalty, GuidelineAdherence scores 1.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset3`

**Article text:**
```
## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 models marks a milestone for the AI community. We appreciate the team's commitment to openness, demonstrated by the permissive MIT license and the unusually detailed technical report that accompanies the models [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1). This transparency provides a valuable blueprint for researchers and engineers. Most importantly, the success of R1-Zero shows that pure RL from a cold start can produce emergent reasoning and self-correction, a finding that could accelerate research in this area.

When comparing DeepSeek-R1 to OpenAI's o1, the models show comparable performance on many reasoning benchmarks, particularly in math and coding [[8]](https://arxiv.org/abs/2501.12948). However, R1 appears to be more inference-efficient, with significantly lower API pricing [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1). This suggests different design philosophies: DeepSeek seems to have invested heavily in a training-heavy approach to bake reasoning into the model, while o1 may lean more on expensive inference-time scaling to achieve its results.

However, a direct comparison is difficult because so much about o1 remains unknown. We do not know its model size, whether it uses a Mixture-of-Experts (MoE) architecture, or the exact mix of training techniques employed [[26]](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1). The strength of the base model is also a critical, undisclosed factor. A more capable base model can make RL training far more effective by providing a better starting point and reducing the sparsity of initial reward signals. Without these details, attributing performance differences to specific methods is speculative.

There is also some ambiguity around the true training cost. While a figure of around $5.3 million has been associated with the DeepSeek-V3 base model, the incremental cost of the R1-specific RL and SFT stages is estimated to be around \$294,000 [[27]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18), [[26]](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1). The full development cost remains undisclosed, making it hard to assess the total investment required for such a project.

Despite these caveats, DeepSeek-R1 stands as a milestone. It proves that high-level reasoning capabilities need not be the exclusive domain of closed, proprietary labs. By providing an open, powerful reasoning model and a detailed recipe, DeepSeek has accelerated research and development for the entire community.
```
**Grader reasoning:**
- `cc`: Thoughts about DeepSeek R1:
**1:** Both sections cover the same appreciation points (open MIT license, detailed report, pure-RL emergent reasoning), the same o1 comparison (comparable benchmarks, R1 more inference-efficient, training-heavy vs. inference-scaling bet), the same limits to that comparison (o1's size/architecture/technique mix undisclosed), the same V3-pretraining-vs-R1-incremental cost distinction (via updated $5.3M/$294,000 figures), and the same milestone conclusion. The added base-model-strength elaboration is additional detail that does not displace any expected idea.
- `fl`: Thoughts about DeepSeek R1:
**1:** The generated section follows the same progression as the expected one: appreciation, o1 comparison, limits to that comparison, cost discussion, milestone close. No media to misplace.
- `de`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: Thoughts about DeepSeek R1:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: Thoughts about DeepSeek R1:
**1:** All required content elements are present, including the o1-disclosure limits and the V3-vs-R1 cost distinction. Prose-only word count is approximately 332 words against a 350-word target (±35 tolerance, range 315–385 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset3`

**Article text:**
```
## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 models is a notable moment for the open-weight AI community. We appreciate several aspects of this release: the open MIT license, which encourages broad use and experimentation; the unusually detailed technical report, which provides a valuable blueprint for other researchers; and the clear demonstration that pure RL from a cold start can produce emergent reasoning behaviors without a supervised warm-up.

When comparing DeepSeek-R1 to OpenAI's o1, the benchmarks show comparable performance on math, coding, and reasoning tasks. However, DeepSeek-R1 appears to have superior inference efficiency. This suggests different strategic bets. DeepSeek invested heavily in training-time compute to bake reasoning into the model, while o1 seems to lean more on expensive inference-time scaling to achieve its results [[41]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o).

However, any direct comparison is limited by the lack of transparency from OpenAI. We do not know the size of the o1 model, its architecture, or the exact mix of techniques used in its training. Without this information, it is difficult to definitively attribute performance differences to specific methods. A direct comparison is unwarranted until more details about o1 are disclosed.

There is also the reality of training costs. The widely cited figure of around $294,000 for DeepSeek-R1 likely refers to the final RL and SFT stages, not the full cost of pre-training the massive 671B DeepSeek-V3 base model, which was estimated to be around $5.3 million [[22]](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1). The DeepSeek team has not disclosed the exact GPU hours or total development cost for R1, so the true incremental cost of adding this reasoning specialization remains unclear.

Despite these caveats, DeepSeek-R1 stands as a milestone. It proves that high-level reasoning capabilities need not be the exclusive domain of closed-source labs, accelerating open research into all four of the techniques we have discussed.
```
**Grader reasoning:**
- `cc`: Thoughts about DeepSeek R1:
**1:** Both sections cover the same appreciation points (open MIT license, detailed report, pure-RL emergent reasoning), the same o1 comparison (comparable benchmarks, R1 more inference-efficient, training-heavy vs. inference-scaling bet), the same limits to that comparison (o1's size/architecture/technique mix undisclosed), the same V3-pretraining-vs-R1-incremental cost distinction (via updated $5.3M/$294,000 figures), and the same milestone conclusion.
- `fl`: Thoughts about DeepSeek R1:
**1:** The generated section follows the same progression as the expected one: appreciation, o1 comparison, limits to that comparison, cost discussion, milestone close. Neither section has media here.
- `de`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Thoughts about DeepSeek R1:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: Thoughts about DeepSeek R1:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: Thoughts about DeepSeek R1:
**0:** All required content elements are present. However, prose-only word count is approximately 293 words against a 350-word target (±35 tolerance, range 315–385 words), 22 words below the minimum — outside tolerance. [Noted on this review: this 22-word margin sits between the confirmed-trivial zone (up to 16 words) and the still-open zone (20-27 words), which has never been explicitly ruled on. Kept as a fail pending an explicit determination rather than assumed to inherit either neighboring ruling.]

## Section: S5::section-5-the-4-main-ways-to-build-and-improve-reasoning-models  (weight=0.453, contribution=+0.0050 FOR standard)
Stored section rewards: standard=0.6692  deep=0.7507  (explore: standard=0.3922  deep=0.5200)

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
**1:** [instances=4; quality=strong,strong,standard,standard] Candidates evaluated: (a) the "overthinking" inverted-U-curve finding, including the specific detail that the model may "flip" a correct answer to incorrect — ref [16], exploration-phase — QUALIFIES, strong. (b) The discussion of open challenges in distillation (loss of nuanced multi-step logic, architectural mismatches, hallucination) — ref [19], confirmed exploration-phase — QUALIFIES, strong. (c) The GRPO mechanics (no separate critic/value network, group-normalized rewards) — ref [18], confirmed exploration-phase — QUALIFIES, standard. (d) The claim that CoT prompting was later automated into self-directed reasoning within test-time scaling models — ref [17], confirmed exploration-phase — QUALIFIES, standard. On review, this belongs here rather than in breadth_enhancement: the core topic of this sub-section is inference-time scaling itself, and this sentence explains that inference-time/test-time scaling's own origin traces back to CoT prompting — that is 'motivation for the core topic — why it exists' / theoretical foundations, intensifying understanding of the section's own subject rather than reaching outward to an adjacent one. (Contrast with Section 2 below, where the same citation is used to explain *why the visible/invisible split exists* via the field's history — there, the core topic is the definitional split, not inference-time scaling, so the identical fact serves a breadth function instead. Same source, different relationship to each section's own core topic.) One candidate rejected: the GRPO length-bias/Dr. GRPO fix, ref [3] — confirmed exploitation-phase. Depth_enhancement scores 1.
- `be`: The 4 main ways to build and improve reasoning models:
**0:** [instances=0] No breadth-qualifying addition is present in this section. The CoT-automation claim (ref [17]) was reconsidered on review: here it explains the origin of the section's own core topic (inference-time scaling grew out of CoT prompting), which is depth, not breadth — see the note under depth_enhancement above. This differs from its treatment in Section 2, where the same fact serves a different, breadth-qualifying function relative to that section's different core topic.
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** The qualifying depth additions (the overthinking research in the inference-time-scaling sub-part, the GRPO mechanics in the pure-RL sub-part, and the distillation-limits discussion) are technical asides that together make up a modest portion of this roughly 1,560-word section spanning four major approaches. The expected output's core narrative — DeepSeek's specific four-technique case study — clearly remains the dominant focus throughout.
- `ga`: The 4 main ways to build and improve reasoning models:
**0:** The generated section covers all four approaches with the specified images and technical details, correctly proposes two additional table comparisons for the distillation sub-section (a model trained with the full SFT+RL hybrid on the same 32B architecture, and a non-distilled 32B baseline), and includes the transition. However, target 1950, tolerance ±195, range 1755-2145. Exact count: 1569. **186 words below the minimum.** This fails the word-count tolerance, so GuidelineAdherence scores 0. Confirmed per ruling: this shortfall is large enough to still result in a penalty.

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
**1:** All figures land in the same relative position as their expected counterparts: Figures 6 and 7 (CoT, search strategies), Figures 8 and 9 (reward mechanics, Aha moment), Figures 10 and 11 (SFT+RL stages, benchmark), and Figures 13 and 14 (distillation benchmarks) all match. Figure 12 is placed immediately after the method intro rather than after the classical-distillation-comparison paragraph that follows it in the expected section — the same narrow, single-paragraph-adjacent reordering already ruled too trivial to count as a placement failure. All exploration-grounded additions (GRPO detail, overthinking/negative-flip, distillation capacity limits) have their own local lead-ins and do not disrupt the surrounding idea order. Separately noted on this review: the expected section explains GRPO before describing the Aha-moment phenomenon it produced, while the generated section mentions the Aha-moment first (briefly) and explains GRPO afterward, with a critical-perspective addition after both. Both ideas are present and the reader has full context by the end either way, so this is not scored as a violation here, but it is a genuine idea-order difference (not a media-placement question) rather than an already-calibrated trivial case — flagged as borderline, see summary.
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

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset3`

**Article text:**
```
## The 4 main ways to build and improve reasoning models

There are four key techniques currently used to build and enhance reasoning in LLMs. While the exact workings of advanced models like OpenAI's o1 and o3 remain undisclosed, they are rumored to combine several of these training and inference-time methods.

### Inference-time scaling

Inference-time scaling refers to dedicating more computational resources during inference to improve a model's output. The analogy is simple: just as a human can produce a better answer when given more time to think, an LLM can improve its performance on complex tasks with additional "thinking time." This is also known as test-time compute scaling [[10]](https://arxiv.org/abs/2408.03314).

One of the most common methods is CoT prompting. By simply adding a phrase like "Let's think step by step" to the prompt, the model is encouraged to break down a problem into intermediate steps, which often leads to a more accurate final answer [[1]](https://arxiv.org/abs/2205.11916).![Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper.](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)

Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper [[1]](https://arxiv.org/abs/2205.11916).

More advanced techniques involve search strategies. **Best-of-N** or **majority voting** involves generating multiple responses and selecting the best one, either with a verifier model or by picking the most common answer. Other methods like **beam search** and **Monte Carlo Tree Search (MCTS)** explore a tree of possible reasoning steps, using a **Process Reward Model (PRM)** to score each intermediate step and guide the search toward the most promising path [[11]](https://arxiv.org/abs/2410.18982). A key distinction exists between PRMs and the more common Outcome Reward Models (ORMs). While ORMs evaluate only the final answer, providing a single, coarse-grained signal, PRMs assess each intermediate step in the reasoning chain. This step-level feedback allows for finer credit assignment and can guide search more effectively, though it requires more complex and expensive data collection [[12]](https://arxiv.org/html/2510.08049v3).![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer.](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)

Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source [LLM Test-Time Compute paper](https://arxiv.org/abs/2408.03314))

Interestingly, the DeepSeek-R1 paper categorizes PRMs and MCTS under "unsuccessful attempts," stating that the computational overhead they introduce during large-scale RL outweighs their benefits in their experiments [[5]](https://www.nature.com/articles/s41586-025-09422-z). This does not mean these methods are useless. It suggests that for their specific training setup, the trade-off was not favorable. DeepSeek may still use these techniques at the application layer, even if they were not part of the core training loop.

This brings us to the high cost of some reasoning models. OpenAI's o1 models, for instance, are more expensive than GPT-4o [[13]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). The o1 model costs $60 per million output tokens, compared to \$10 for GPT-4o. This price difference is likely due to the heavy inference-time compute o1 uses to "think" longer, a strategy that can lead to "overthinking." This involves expending excessive computation on simple problems [[14]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o), [[10]](https://arxiv.org/abs/2408.03314).

### Pure reinforcement learning (RL)

The second approach is pure RL, best exemplified by DeepSeek-R1-Zero. Unlike typical RL pipelines that start with a model already fine-tuned on human examples (SFT), pure RL is applied directly to the base model. This "cold-start" approach is designed to let the model discover reasoning paths on its own, without being biased by human-provided demonstrations [[6]](https://thelmbook.com/articles#!./DeepSeek-R1.md).![Figure 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)

Figure 8: The development process of DeepSeek-R1-Zero model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This process relies on a reward system that does not require a separate reward model trained on human preferences. Instead, it uses rule-based rewards. The DeepSeek-R1 paper details two main types [[5]](https://www.nature.com/articles/s41586-025-09422-z):

1.  **Accuracy rewards:** These are given if the model's final answer is correct. For math problems, this can be checked by comparing the final number. For code, it can be verified by running unit tests.
2.  **Format rewards:** These incentivize the model to follow a specific structure, such as enclosing its reasoning process within `<think>` and `</think>` tags. This makes the output more interpretable and stable.

One of the most interesting outcomes of this pure RL training was the emergence of an **"Aha moment."** The DeepSeek paper describes a point in training where the model spontaneously started generating long, reflective reasoning traces. It began using phrases like "Wait, wait. Wait. That's an aha moment" before re-evaluating its approach. This demonstrated that complex behaviors like self-correction can emerge from a simple, outcome-based reward signal without being explicitly taught [[5]](https://www.nature.com/articles/s41586-025-09422-z).![Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)

Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment [[5]](https://www.nature.com/articles/s41586-025-09422-z).

However, a growing body of research suggests this "Aha moment" is not created by RL but is instead an amplification of a latent capability. Studies show that self-reflection and self-correction behaviors emerge during pre-training, likely from exposure to extensive chain-of-thought data [[15]](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training). One analysis found that while a fine-tuned model exhibited self-reflection nearly 100% of the time, its pretrained base model already did so spontaneously, just far less frequently [[16]](https://arxiv.org/html/2506.12217v1). The pre-training data mixture is therefore a critical, though undisclosed, factor in the stability of cold-start RL [[17]](https://www.youtube.com/watch?v=SD5raqvYG-0). Regardless, R1-Zero was the first open model to show that it is possible to develop strong reasoning capabilities through pure RL.

### Supervised finetuning and reinforcement learning (SFT + RL)

The third method is a hybrid approach that combines SFT with RL, as seen in the main DeepSeek-R1 model. This multi-stage process is designed to create a model that is not only a strong reasoner but also more stable, readable, and aligned with human preferences than a pure RL model like R1-Zero.![Figure 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)

Figure 10: The development process of DeepSeek-R1 model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

The pipeline begins with a "cold-start" SFT stage, where the base model is fine-tuned on a few thousand examples of human-aligned reasoning traces. This initial step improves the readability of the model's output and prepares it for the more intensive RL phase [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

Next, the model undergoes large-scale RL training, similar to R1-Zero, using verifiable rewards. The use of verifiable rewards is where PRMs become powerful in an RL context. Instead of relying on a sparse, final-outcome signal, a PRM provides dense, step-by-step rewards. This fine-grained feedback helps stabilize RL training, offers more precise credit assignment for long chains of thought, and allows the policy to learn more efficiently [[12]](https://arxiv.org/html/2510.08049v3). An additional reward is introduced: a **language consistency reward**. This was added to address the issue of "language mixing," where R1-Zero would sometimes switch between English and Chinese mid-thought. This reward penalizes outputs that do not match the language of the input query, improving user experience even at the cost of a slight dip in raw task performance [[5]](https://www.nature.com/articles/s41586-025-09422-z).

The process then iterates through more SFT and RL stages. Rejection sampling is used to generate a large dataset of high-quality completions for both reasoning and general chat problems, which are then used for SFT. A final RL stage mixes verifiable rewards for reasoning tasks with preference-based rewards (from a trained reward model) for general helpfulness and harmlessness. This staged refinement results in a powerful, well-rounded model that excels on reasoning benchmarks while being a capable general-purpose assistant [[5]](https://www.nature.com/articles/s41586-025-09422-z).

On benchmarks, DeepSeek-R1 is highly competitive with OpenAI's o1 models, often matching or exceeding their performance in math and code, demonstrating the success of this hybrid approach.![Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models.](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)

Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

### Pure supervised finetuning (SFT) and distillation

To recap, inference-time scaling improves reasoning without changing the model, pure RL allows the model to discover reasoning on its own, and the SFT+RL hybrid refines this emergent behavior for production. The final approach, pure SFT and distillation, focuses on efficiently transferring these hard-won reasoning capabilities to smaller, more accessible models.

As we discussed, DeepSeek's distillation process is a form of SFT. Instead of traditional distillation that matches logits, they fine-tune smaller open-source models (like Qwen and Llama) on a large dataset of 800,000 high-quality reasoning traces generated by the powerful DeepSeek-R1 model. This process does not include an additional RL stage [[9]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)

Figure 12: The development process of DeepSeek-R1-Distill models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

DeepSeek created these distilled models for two main reasons. First, the 671B parameter R1 model is massive and requires considerable computational resources to run, making it inaccessible for many users and applications. Distillation makes its powerful reasoning accessible on consumer-grade hardware. Second, it provides a valuable resource for the research community to study the mechanisms of long-CoT reasoning models without needing access to the large model itself [[8]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).

The results are impressive. The distilled models outperform their original instruction-tuned counterparts and even strong closed-source models like GPT-4o on reasoning benchmarks. For example, the 1.5B distilled Qwen model surpasses non-reasoning baselines on mathematical tasks, a remarkable achievement for a model of its size [[5]](https://www.nature.com/articles/s41586-025-09422-z).![Figure 13: Benchmark comparison of distilled versus non-distilled models.](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)

Figure 13: Benchmark comparison of distilled versus non-distilled models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This raises a key question: is distillation more effective than pure RL for smaller models? The DeepSeek-R1 paper provides an answer by comparing a 32B distilled model to a 32B model trained with pure RL (Qwen2.5-32B-Zero). The distilled model outperformed the pure RL model across all benchmarks [[5]](https://www.nature.com/articles/s41586-025-09422-z).![Figure 14: Benchmark comparison distillation and RL on a smaller 32B model.](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)

Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This suggests two insights. First, for smaller models, distillation is a more economical and effective way to impart reasoning abilities than large-scale RL from scratch. Second, pushing the frontiers of AI intelligence likely still requires the massive scale of models like R1 to discover novel reasoning patterns, which can then be transferred to smaller models. The table above would have been more insightful if it also included a comparison to a non-reasoning base model and a model trained with SFT on human-generated data, to better isolate the impact of distillation.

After dissecting these four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the release's broader significance.
```
**Grader reasoning:**
- `cc`: The 4 main ways to build and improve reasoning models:
**1:** Both sections describe the same four key techniques: inference-time scaling, pure RL, SFT+RL, and distillation. The core concepts and examples for each technique are consistent, and the distillation sub-approach gives two genuinely distinct reasons for building the distilled models (accessibility on consumer hardware, and a resource for the research community to study long-CoT mechanisms), satisfying the guideline's requirement.
- `fl`: The 4 main ways to build and improve reasoning models:
**1:** Both sections follow the same logical flow, presenting the four techniques in the same order. Each sub-section introduces the technique, explains it, and provides relevant examples or figures. The depth additions (PRM/ORM distinction, the Aha-moment critical analysis) are integrated smoothly within their respective sub-sections without disrupting the overall narrative.
- `de`: The 4 main ways to build and improve reasoning models:
**1:** [instances=3; quality=strong,strong,strong] Three depth additions are present, all verified against research.md's exploration-phase blocks. (1) In "Inference-time scaling," the section adds a distinction between Process Reward Models (PRMs) and Outcome Reward Models (ORMs) — PRMs assess each intermediate step versus ORMs' single coarse-grained signal, at the cost of more complex/expensive data collection. This qualifies as "technical nuances" and "implementation challenges... or engineering realities." Traceable to ref [12], arxiv.org/html/2510.08049v3, confirmed inside the exploration-phase block (both as a Q&A source and a fully scraped article). Classified as strong: a specific mechanism contrast with a named trade-off. (2) In "Pure reinforcement learning," the section adds a critical analysis of the "Aha moment," citing research that self-reflection is a latent capability present before RL (with a specific comparison: a fine-tuned model showed self-reflection nearly 100% of the time versus its pretrained base model showing it spontaneously but far less frequently) and that the undisclosed pre-training data mixture is a critical factor in cold-start RL stability. This qualifies as "limitations... of the core topic." Traceable to ref [15] (magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training), ref [16] (arxiv.org/html/2506.12217v1), and ref [17] (youtube.com/watch?v=SD5raqvYG-0), all confirmed inside the exploration-phase block — treated as one combined instance since all three support the same continuous claim in the same paragraph. Classified as strong: a specific, quantified comparison finding plus a named undisclosed factor. (3) In "Supervised finetuning and reinforcement learning (SFT + RL)," the section adds a separate claim that PRMs stabilize RL training by providing dense, step-by-step rewards instead of a sparse outcome signal, improving credit assignment for long chains of thought. This qualifies as "technical nuances." Also traceable to ref [12], exploration-phase. This is treated as a distinct instance from (1) — despite sharing a source — because it appears under a different subheading and makes a different substantive claim (training-stabilization/credit-assignment value, versus (1)'s evaluation-granularity/cost tradeoff). Classified as strong: a specific mechanism (dense vs. sparse rewards) tied to a concrete training benefit. Since multiple instances qualify, depth_enhancement scores 1 for the section as a whole.
- `be`: The 4 main ways to build and improve reasoning models:
**0:** [instances=0] No breadth additions present. The section's additional material (PRM/ORM distinction, PRM's role in RL stabilization, the Aha-moment critical analysis) intensifies understanding of the same core topic rather than connecting it to an adjacent field, so it is evaluated under depth_enhancement instead.
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** The depth additions (the PRM/ORM distinction and the Aha-moment critical analysis) are well-integrated technical asides within their respective sub-sections and directly support the core explanations. The expected output's core narrative — the four-technique case study — clearly remains the dominant focus.
- `ga`: The 4 main ways to build and improve reasoning models:
**0:** The generated section meets its substantive requirements — contrary to a prior pass's claims, it DOES explain the DeepSeek R1 report's "unsuccessful attempts" categorization (line 72), DOES include one-sentence summaries of the first three approaches at the start of the distillation subsection (line 111), and DOES propose two additional table comparisons for Figure 14 (a non-reasoning base model and an SFT-only-trained model, line 127). The actual disqualifying issue, uncaught by the prior pass, is word count: the prose-only word count for this section is approximately 1,443 words, far short of the 1950-word target's required 1755–2145 range (±10%). This roughly 26% shortfall fails the word-count tolerance, so GuidelineAdherence scores 0.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset3`

**Article text:**
```
## The 4 main ways to build and improve reasoning models

Current techniques for enhancing LLM reasoning can be grouped into four main categories. While the exact workings of frontier models like OpenAI's o1 and o3 remain undisclosed, they are rumored to combine both inference-time and training-time methods [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

### 1) Inference-time scaling

Inference-time scaling refers to improving a model's performance by allocating more computational resources during inference, without altering the model's weights. The core idea is analogous to giving a human more time to think through a difficult problem. This approach is also known as test-time compute scaling, and research shows that performance on complex benchmarks often increases with more compute, whether at training time or test time [[13]](https://arxiv.org/abs/2408.03314).

One of the simplest methods is CoT prompting, where a phrase like "Let's think step by step" encourages the model to generate intermediate reasoning steps [[2]](https://arxiv.org/abs/2205.11916). This method has historical roots in symbolic AI systems, which relied on structured, step-by-step logical deduction to solve problems. CoT prompting elicits a similar pattern of structured thought from modern LLMs, bridging the gap between connectionist and symbolic approaches to reasoning [[14]](https://www.mdpi.com/2227-7390/13/11/1707). This naturally increases the number of generated tokens and, therefore, the inference cost.![Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)
Image 6: An example of classic CoT prompting from the 2022 *Large Language Models are Zero-Shot Reasoners* paper. (Source: [arxiv.org](https://arxiv.org/abs/2205.11916) [[2]](https://arxiv.org/abs/2205.11916))

More advanced techniques involve search strategies. These methods generate multiple potential solutions and use a verifier, or a Process Reward Model (PRM), to select the best one. A PRM provides fine-grained, step-level feedback, contrasting with an Outcome Reward Model (ORM), which only judges the final answer. This process-level supervision is essential for diagnosing intermediate errors and guiding complex reasoning. However, it also makes PRMs more resource-intensive to create, as they require correctness labels for every intermediate step, not just the final result [[15]](https://arxiv.org/html/2510.08049v3), [[16]](https://www.jonvet.com/blog/llm-test-time-compute).

The computational expense of training and running large PRMs has led to research into more efficient alternatives. These include lightweight verifiers that probe a model's internal states to estimate the credibility of a reasoning step without needing a separate, large reward model [[17]](https://arxiv.org/html/2511.06209v3). Common search strategies include:
*   **Best-of-N:** The model generates N full solutions, and a verifier selects the best one.
*   **Beam Search:** The model explores a limited number of top-k solutions at each step, pruning less promising paths.
*   **Lookahead Search / Monte Carlo Tree Search (MCTS):** This method builds on beam search by performing rollouts to estimate the future value of a particular reasoning step, allowing for more strategic exploration of the solution space [[13]](https://arxiv.org/abs/2408.03314).![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)
Image 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source: [arxiv.org](https://arxiv.org/abs/2408.03314) [[13]](https://arxiv.org/abs/2408.03314))

Interestingly, the DeepSeek R1 technical report categorized these common inference-time scaling methods under "unsuccessful attempts" during their training process [[8]](https://arxiv.org/abs/2501.12948). This suggests that their model's ability to generate long reasoning traces is an intrinsic property learned during training, rather than a result of explicit search algorithms at inference. However, this does not preclude DeepSeek from applying these techniques at the application layer to further boost performance.

The high cost of models like OpenAI's o1 compared to GPT-4o is likely due to this heavy use of inference-time compute. The o1 models are slower and more expensive, designed to spend more time "thinking" before responding, which makes them better at complex science, coding, and math problems [[18]](https://www.uctoday.com/unified-communications/chatgpt-4o-vs-o1-which-openai-model-is-best), [[3]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison), [[19]](https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c).

### 2) Pure reinforcement learning (RL)

The second approach, pure RL, is exemplified by DeepSeek-R1-Zero. Unlike typical RL pipelines that start with an SFT model, this method applies RL directly to a base model. Instead of using a reward model trained on human preferences, it uses simple, verifiable reward signals [[9]](https://thelmbook.com/articles#!./DeepSeek-R1.md), [[8]](https://arxiv.org/abs/2501.12948).![Figure 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)
Image 8: The development process of the DeepSeek-R1-Zero model. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

The reward structure in the DeepSeek R1 paper consists of two main components:
*   **Accuracy rewards:** A binary reward (e.g., 1 for correct, 0 for incorrect) based on whether the final answer is correct. This is possible for tasks with deterministic solutions, like math problems or coding challenges with unit tests [[9]](https://thelmbook.com/articles#!./DeepSeek-R1.md), [[20]](https://www.nature.com/articles/s41586-025-09422-z).
*   **Format rewards:** The model is rewarded for following specific formatting rules, such as enclosing its reasoning process within `<think>` and `</think>` tags. This encourages interpretability and structured output without constraining the content of the reasoning itself [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

During this pure RL training, the DeepSeek team observed an "Aha moment" [[21]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners), [[8]](https://arxiv.org/abs/2501.12948). The model spontaneously began to generate long, complex reasoning traces, including self-reflection and self-correction patterns, without being explicitly taught to do so. For example, it would generate phrases like "Wait, wait. Wait. That's an aha moment I can flag here," before re-evaluating its approach. This emergent behavior was accompanied by a steady increase in the average length of the model's responses during training [[8]](https://arxiv.org/abs/2501.12948).![Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)
Image 9: An example from the DeepSeek R1 technical report showing the "Aha moment" where the model learns to self-reflect. (Source: [arxiv.org](https://arxiv.org/abs/2501.12948) [[8]](https://arxiv.org/abs/2501.12948))

However, a growing body of research suggests this "Aha moment" is less about RL creating a new capability and more about it amplifying a latent one. Self-reflection and self-correction behaviors appear to emerge during pre-training and are already present, albeit rarely activated, in the base models [[38]](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training). Recent studies have shown that these models maintain distinct internal representations for reflective and non-reflective states, even before fine-tuning. This suggests that pure RL acts as a powerful amplifier, making these latent abilities more frequent and reliable, rather than creating them from scratch [[39]](https://arxiv.org/html/2506.12217v1). Nonetheless, R1-Zero was the first instance to show that it is possible to develop reasoning capabilities with pure RL, by having the model generate its own intermediate "thinking" steps.

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

The third approach is a hybrid model that combines SFT and RL, as seen in the full DeepSeek-R1 model. This multi-stage process aims to build upon the raw reasoning capabilities developed in R1-Zero while improving stability, readability, and general helpfulness [[8]](https://arxiv.org/abs/2501.12948). This is because pure RL from a cold start can be unstable and lead to issues like language mixing. A preliminary SFT stage provides a better-aligned starting point, which helps stabilize and accelerate the subsequent RL training [[22]](https://cameronrwolfe.substack.com/p/demystifying-reasoning-models).![Figure 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)
Image 10: The development process of the DeepSeek-R1 model. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

The pipeline involves several key steps. First, a **Cold-Start SFT** fine-tunes the base model on a small "cold-start" dataset of a few thousand high-quality, human-aligned reasoning examples. This initial step stabilizes the subsequent RL training and prevents issues like language mixing [[21]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners), [[23]](https://artgor.medium.com/paper-review-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning-edf4343dcf3a). While SFT is a common approach, other methods like Direct Preference Optimization (DPO) have also been explored for this warm-up phase. Using a DPO-based cold-start can sometimes lead to more stable RL convergence, as its objective is more aligned with the preference-based nature of RL [[24]](https://arxiv.org/html/2510.25801v3).

Second, the model undergoes **Reasoning-Oriented RL**, similar to R1-Zero, using verifiable rewards. At this stage, a **language consistency reward** is introduced. This reward, calculated as the proportion of words in the target language, penalizes the model for mixing languages. While this slightly degrades performance on some reasoning tasks, it significantly improves readability and user preference [[20]](https://www.nature.com/articles/s41586-025-09422-z).

Third, **Rejection Sampling and General SFT** are used to broaden the model's capabilities. Rejection sampling generates a large dataset (800K completions) for a final SFT stage, which includes both reasoning problems and general chat queries. This helps the model transition from a pure reasoner to a more general-purpose assistant [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

Finally, a **Final RL Polish** is applied. This last step is another round of RL that mixes verifiable reasoning tasks with standard preference tuning on general prompts. This stage uses model-based reward models to improve helpfulness and harmlessness, polishing the model for general use [[8]](https://arxiv.org/abs/2501.12948). This staged refinement process allows DeepSeek-R1 to achieve strong performance across a wide range of benchmarks, often comparable to or exceeding that of closed models like OpenAI's o1 [[8]](https://arxiv.org/abs/2501.12948).![Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)
Image 11: Benchmark comparison of OpenAI o1 and DeepSeek R1 models. (Source: [arxiv.org](https://arxiv.org/abs/2501.12948) [[8]](https://arxiv.org/abs/2501.12948))

### 4) Pure supervised finetuning (SFT) and distillation

To recap, inference-time scaling enhances reasoning without changing model weights, pure RL fosters emergent reasoning behaviors from scratch, and the SFT+RL hybrid method refines these capabilities for production readiness. The fourth approach, pure SFT and distillation, offers a more resource-efficient way to create reasoning models by transferring knowledge from a large, powerful model to smaller ones [[12]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).

DeepSeek's distillation process is straightforward: they used their powerful DeepSeek-R1 model to generate 800,000 high-quality reasoning samples. Then, they used this synthetic dataset to fine-tune smaller, existing open-source models like Qwen and Llama. This is different from traditional knowledge distillation, which often involves matching the output logits of the teacher model. Here, the student model simply learns to mimic the final text output (the reasoning trace) of the teacher through standard SFT [[25]](https://redwerk.com/blog/what-is-model-distillation), [[8]](https://arxiv.org/abs/2501.12948).![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)
Image 12: The development process of DeepSeek-R1-Distill models. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

DeepSeek created these distilled models for two key reasons. First, the full 671B parameter R1 model is computationally expensive and difficult to run on consumer-grade hardware. Distillation makes these powerful reasoning capabilities accessible to a wider audience [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d). Second, this process is much more efficient than training a smaller model from scratch with pure RL [[8]](https://arxiv.org/abs/2501.12948).

The results are impressive. Even the smallest distilled model, DeepSeek-R1-Distill-Qwen-1.5B, surpasses strong non-reasoning baselines like GPT-4o on mathematical benchmarks [[8]](https://arxiv.org/abs/2501.12948).![Figure 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)
Image 13: Benchmark comparison of distilled versus non-distilled models. (Source: [arxiv.org](https://arxiv.org/abs/2501.12948) [[8]](https://arxiv.org/abs/2501.12948))

The DeepSeek report also provides a direct comparison between distillation and pure RL on a smaller 32B model. They found that while pure RL did improve the model's reasoning, the distilled version performed significantly better across all benchmarks. This suggests that for smaller models, it is more effective to transfer knowledge from a larger, more capable teacher than to try to elicit reasoning from scratch through RL [[8]](https://arxiv.org/abs/2501.12948).![Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)
Image 14: Benchmark comparison of distillation and RL on a smaller 32B model. (Source: [arxiv.org](https://arxiv.org/abs/2501.12948) [[8]](https://arxiv.org/abs/2501.12948))

This insight is valuable: while advancing the frontier of AI may require massive base models and large-scale RL, distillation is a powerful and economical strategy for disseminating those capabilities. The comparison could have been more comprehensive if it had also included a model trained with the SFT+RL hybrid approach, or if the RL-trained models were given a "warm-up" with the distilled data before RL.

After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the broader significance and limitations of this release.
```
**Grader reasoning:**
- `cc`: The 4 main ways to build and improve reasoning models:
**1:** Across all four sub-approaches, the generated section covers inference-time scaling (CoT, search strategies including Best-of-N/beam/lookahead/PRM, the 'unsuccessful attempts' categorization, cost speculation, plus well-grounded additions on PRM-vs-ORM, lightweight verifiers, and CoT's symbolic-AI roots), pure RL (R1-Zero, both reward types, the verbatim Aha-moment quote, plus a well-grounded latent-capability-amplification caveat), SFT+RL (the four-stage pipeline, language-consistency reward, 800K rejection-sampling data, plus a well-grounded DPO-cold-start alternative), and distillation (mechanism, two reasons, benchmark comparisons, the 32B RL-vs-distillation result) with exceptional fidelity. As in other presets for this lesson, the expected section's specific 'additional comparisons' suggestion (Qwen-32B with SFT+RL; DeepSeek-V3 with pure SFT) is replaced with a different pair (an SFT+RL-trained comparison model; RL warm-started with distilled data) — a small, peripheral substitution inside an otherwise comprehensive section.
- `fl`: The 4 main ways to build and improve reasoning models:
**1:** All figures land in the same relative position as their expected counterparts, including Image 12 (placed after the classical-distillation-comparison explanation, exactly matching the expected section's own placement — no shift at all this time). Every exploration-grounded addition (symbolic-AI history, PRM/ORM, lightweight verifiers, latent-capability amplification, DPO cold-start) has its own local lead-in and does not disrupt the surrounding idea order.
- `de`: The 4 main ways to build and improve reasoning models:
**1:** [instances=4; quality=strong,strong,strong,strong] Four qualifying depth additions, each traceable to an exploration-phase source. (1) In inference-time scaling: the PRM-vs-ORM distinction — "contrasting with an Outcome Reward Model (ORM), which only judges the final answer" — traceable to two exploration sources (the PRM survey and jonvet.com) closely, cited [15], [16]. (2) Also in inference-time scaling: lightweight verifiers that "probe a model's internal states to estimate the credibility of a reasoning step without needing a separate, large reward model," traceable to an exploration source (ReProbe) verbatim, cited [17]. (3) In the Pure RL sub-section: the latent-capability-amplification discussion — self-reflection "already present, albeit rarely activated, in the base models" and RL as "a powerful amplifier" rather than a creator of new capability — traceable to two exploration sources (including a fully scraped dedicated paper) closely, cited [38], [39]. (4) In the SFT+RL sub-section: the DPO-based cold-start alternative — "can sometimes lead to more stable RL convergence" — traceable to an exploration source closely, cited [24]. Each is classified strong: a specific, multi-sentence technical mechanism or named alternative, not a generic mention.
- `be`: The 4 main ways to build and improve reasoning models:
**1:** [instances=1; quality=strong] One qualifying breadth addition: "this method has historical roots in symbolic AI systems, which relied on structured, step-by-step logical deduction... bridging the gap between connectionist and symbolic approaches to reasoning" [14], traceable to two exploration sources on the history of symbolic AI and CoT closely. This qualifies as 'historical context or evolution of the topic' and 'cross-domain analogies... from other fields.' Classified as strong: a specific, well-integrated historical account naming the connectionist/symbolic distinction, not a vague gesture at history.
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** depth_enhancement and breadth_enhancement both scored 1 for this section (four depth additions and one breadth addition). Each is a contained paragraph or pair of sentences placed at a natural point within its own sub-section, and the four techniques and the DeepSeek-R1 case study remain clearly the dominant focus throughout this large section — none of the additions individually or collectively overwhelm the core narrative. CorePreservation scores 1.
- `ga`: The 4 main ways to build and improve reasoning models:
**0:** Content-wise this section covers essentially everything the guideline requires across all four approaches, including the required 'at least two useful additional comparisons' (the guideline does not specify which two). However, prose-only word count is approximately 1,537 words against a 1,950-word target (±195 tolerance, range 1,755–2,145 words), about 218 words below the minimum — clearly outside tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset3`

**Article text:**
```
## The 4 main ways to build and improve reasoning models

The current key techniques to enhance LLM reasoning and build specialized reasoning models can be grouped into four main categories. While the exact workings of OpenAI's o1 and o3 models remain unknown, they are rumored to combine several of these training and inference techniques.

### Inference-time scaling

Inference-time scaling refers to dedicating more computational resources during inference to improve a model's output. The analogy is simple. Just as a human can produce a better answer when given more time to think, an LLM can improve its performance on complex tasks with additional "thinking time" [[29]](https://openai.com/index/learning-to-reason-with-llms/).

This can be achieved through several methods. The most basic is **Chain-of-Thought (CoT) prompting**, where a simple phrase like "Let's think step by step" encourages the model to generate intermediate reasoning steps before giving a final answer. This breaks down a complex problem into a sequence of simpler ones [[5]](https://arxiv.org/abs/2205.11916). This approach has roots in historical symbolic AI systems, which also relied on structured, step-by-step procedures to perform logical deduction. CoT prompting effectively elicits a similar symbolic-like behavior from modern neural networks [[6]](https://www.mdpi.com/2227-7390/13/11/1707).![Image 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper.](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)
Image 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper (Source [[5]](https://arxiv.org/abs/2205.11916)).

More advanced techniques involve search strategies. **Majority voting** or **best-of-N sampling** involves generating multiple responses and selecting the most common or highest-rated one using a verifier model. More sophisticated methods like **beam search** or **Monte Carlo Tree Search (MCTS)** explore a tree of possible reasoning paths, pruning unpromising branches and focusing computation on the most likely solutions. These search-based methods often rely on a **Process Reward Model (PRM)**, which evaluates the correctness of each intermediate step in a reasoning chain, providing a fine-grained signal to guide the search [[7]](https://arxiv.org/abs/2408.03314). This contrasts with an Outcome Reward Model (ORM), which only judges the final answer. By providing step-by-step feedback, PRMs enable finer-grained alignment for complex reasoning tasks [[8]](https://www.jonvet.com/blog/llm-test-time-compute).![Image 7: Different search-based methods rely on a process-reward-based model to select the best answer.](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)
Image 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

The development of PRMs typically follows a closed loop: generating process data (through human, automated, or hybrid annotation), training the PRM to evaluate steps, and then using the PRM to improve the reasoning model. This improved model can then generate even better data, continuing the cycle [[9]](https://arxiv.org/html/2510.08049v3). While powerful, PRM-based verification has its own drawbacks, primarily the high computational cost of training and running them. This has spurred research into more efficient alternatives, such as lightweight verifiers that probe a model's internal states to estimate the credibility of its reasoning steps without needing a separate, large reward model [[10]](https://arxiv.org/html/2511.06209v3).

Interestingly, the DeepSeek R1 technical report categorized common inference-time scaling methods like PRM-based search and MCTS under "unsuccessful attempts" [[15]](https://arxiv.org/abs/2501.12948). This suggests that their core model's reasoning ability relies more on its training than on complex inference-time search algorithms. However, it is plausible that DeepSeek could still apply these techniques at the application layer to further boost performance.

This trade-off between training-time and inference-time compute might explain why models like OpenAI's o1 are more expensive than models like GPT-4o. The higher cost likely reflects the additional computation required for the model to "think longer" before responding, a direct application of inference-time scaling [[11]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison).

### Pure reinforcement learning (RL)

Pure RL, as exemplified by DeepSeek-R1-Zero, represents a departure from the typical RLHF pipeline. Instead of starting with a model already fine-tuned on human demonstrations (SFT), this approach applies RL directly to the base model. While DeepSeek-R1-Zero demonstrates this is possible, a 'cold start' without any SFT is often less stable. An initial SFT phase on high-quality reasoning data provides a better starting policy for RL, allowing it to focus on refining reasoning quality rather than learning basic output formats. Some research even suggests using Direct Preference Optimization (DPO) for this initial phase to achieve smoother and more stable convergence during the subsequent RL training [[18]](https://arxiv.org/html/2510.25801v3). The reward signals are not derived from a reward model trained on human preferences, but from rule-based verifiers [[16]](https://www.nature.com/articles/s41586-025-09422-z).![Image 8: The development process of the DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)
Image 8: The development process of the DeepSeek-R1-Zero model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

In the DeepSeek-R1 paper, two main types of rewards are used:

1.  **Accuracy rewards:** The model receives a positive reward if its final answer is correct. This is straightforward for tasks with deterministic solutions, like math problems where the answer can be checked, or coding problems where test cases can be run [[17]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).
2.  **Format rewards:** The model is incentivized to follow specific formatting rules, such as enclosing its reasoning process within `<think>` and `</think>` tags. This ensures the output is structured and interpretable [[12]](https://thelmbook.com/articles#!./DeepSeek-R1.md).

One of the most inspiring results from this approach is the emergence of the **"Aha moment"**. During training, the model spontaneously starts generating longer, more complex reasoning traces. It begins to self-reflect, verify its work, and explore alternative solutions without being explicitly taught to do so. The DeepSeek paper highlights an instance where the model generates "Wait, wait. Wait. That's an aha moment I can flag here," before re-evaluating its approach [[15]](https://arxiv.org/abs/2501.12948).![Image 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)
Image 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment (Source [[15]](https://arxiv.org/abs/2501.12948)).

However, the term "emergence" might be misleading. Recent research suggests that these self-reflection capabilities are not created from scratch by RL. Instead, they appear to be latent abilities already present in the base model from pre-training, which are then amplified and made more frequent by the RL process. Probing studies have shown that while a fine-tuned model might use reflection constantly, the pretrained base model already exhibits the same behavior, just far more rarely [[19]](https://arxiv.org/html/2506.12217v1). This underscores how much the undisclosed pre-training data mixture can influence the stability and outcome of any RL-based fine-tuning. The behaviors that RL can amplify depend heavily on what patterns were already seeded in the base model [[20]](https://www.youtube.com/watch?v=SD5raqvYG-0). This demonstrates that sophisticated reasoning capabilities can emerge from pure RL, guided only by outcome-based rewards. It is the first major instance showing that it is possible to develop reasoning models this way, unlocking a new path for AI research.

### Supervised finetuning and reinforcement learning (SFT + RL)

The hybrid SFT + RL approach, used to create the final DeepSeek-R1 model, is a multi-stage process designed to combine the exploratory power of RL with the stability and alignment of SFT. This method addresses the shortcomings of pure RL, such as poor readability and language mixing, resulting in a model that is both a powerful reasoner and user-friendly [[13]](https://artgor.medium.com/paper-review-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning-edf4343dcf3a). By providing a strong "prior" through SFT, this approach eliminates much of the instability of a pure RL cold start, leading to faster and more reliable training.![Image 10: The development process of the DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)
Image 10: The development process of the DeepSeek-R1 model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

The process typically involves several stages:

1.  **Cold-Start Data Generation:** The process begins by using the R1-Zero model to generate a "cold-start" dataset of a few thousand reasoning traces. These traces are then refined by human annotators to ensure they are readable and follow a conversational style [[17]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).
2.  **Initial SFT:** The base model is fine-tuned on this small, high-quality dataset. This "warms up" the model, giving it a foundation in coherent, human-aligned reasoning before the more intensive RL phase begins.
3.  **RL with Consistency Rewards:** The model then undergoes large-scale RL, similar to R1-Zero. However, in addition to accuracy and format rewards, a **language consistency reward** is introduced. This reward penalizes the model for mixing languages within a response, which was a known issue with R1-Zero. While this might cause a slight dip in raw performance on some tasks, it improves user experience [[16]](https://www.nature.com/articles/s41586-025-09422-z).
4.  **Iterative Refinement:** The process can be iterative, with additional stages of SFT and RL to further polish the model's capabilities, incorporating data from both reasoning and general-purpose domains.

This staged refinement allows for a more controlled development process. The initial SFT provides stability, while the subsequent RL phases enhance reasoning capabilities in a targeted manner. The final DeepSeek-R1 model demonstrates performance on par with or even exceeding OpenAI's o1 on several key reasoning benchmarks, particularly in math and coding [[15]](https://arxiv.org/abs/2501.12948).![Image 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models.](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)
Image 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report (Source [[15]](https://arxiv.org/abs/2501.12948)).

### Pure supervised finetuning (SFT) and distillation

To recap, we have covered three primary methods for building reasoning models: inference-time scaling, which uses more compute at runtime; pure RL, which discovers reasoning from scratch; and the SFT+RL hybrid, which balances discovery with stability. The fourth approach, pure SFT and distillation, offers a more direct and often more efficient path to enhancing reasoning.

DeepSeek's approach to creating their distilled models is a practical example of this. Instead of the traditional method of knowledge distillation, which involves matching the output distributions (logits) of a student model to a teacher model, DeepSeek uses a simpler form of SFT. They generated a large dataset of 800,000 high-quality reasoning samples using their powerful R1 model and then fine-tuned smaller, existing open-source models (like Qwen and Llama) on this synthetic data [[21]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).![Image 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)
Image 12: The development process of DeepSeek-R1-Distill models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

There are two key reasons why DeepSeek developed these distilled models. First, it democratizes access to advanced reasoning. The massive 671B R1 model is impractical for most users to run, but smaller distilled models make these capabilities accessible on consumer-grade hardware. Second, it is highly efficient. This SFT-only process avoids the computational expense and complexity of RL, providing a straightforward way to transfer reasoning skills [[14]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).

The results are impressive. As shown in the benchmarks, even the smallest distilled models outperform powerful, non-reasoning-focused models like GPT-4o and Claude-3.5-Sonnet on mathematical tasks [[15]](https://arxiv.org/abs/2501.12948).![Image 13: Benchmark comparison of distilled versus non-distilled models.](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)
Image 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report (Source [[15]](https://arxiv.org/abs/2501.12948)).

The DeepSeek report also provides a crucial comparison: how does this distillation approach stack up against applying pure RL to smaller models? They trained a 32B model with the same pure RL process as R1-Zero and found that the distilled 32B model performed better across all benchmarks.![Image 14: Benchmark comparison of distillation and RL on a smaller 32B model.](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)
Image 14: Benchmark comparison of distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report (Source [[15]](https://arxiv.org/abs/2501.12948)).

This leads to two key insights. First, for smaller models, distillation is a more effective and economical strategy for imparting reasoning skills than pure RL. The emergent reasoning behavior seen in massive models does not seem to appear as readily at smaller scales. Second, while distillation is powerful, pushing the absolute frontier of AI reasoning likely still requires the combination of massive base models and large-scale reinforcement learning [[15]](https://arxiv.org/abs/2501.12948). It would have been interesting to see a comparison with a 32B model trained with the full SFT+RL pipeline, not just pure RL, to understand if that hybrid approach could close the gap with distillation. Also, a comparison with a 32B model simply fine-tuned on general instruction data would have provided a clearer baseline for the gains from reasoning-specific training.

After dissecting these four techniques, let's step back to evaluate the broader significance of the DeepSeek-R1 release.
```
**Grader reasoning:**
- `cc`: The 4 main ways to build and improve reasoning models:
**1:** Across all four sub-approaches, the generated section covers inference-time scaling (CoT, search strategies, PRM/ORM, the 'unsuccessful attempts' categorization, cost speculation, plus well-grounded additions on symbolic-AI history, PRM lifecycle, and lightweight verifiers), pure RL (R1-Zero, both reward types, the verbatim Aha-moment quote, plus well-grounded DPO-cold-start and latent-self-reflection caveats), SFT+RL (a four-stage pipeline covering cold-start data, initial SFT, consistency-reward RL, and iterative refinement), and distillation (mechanism, two reasons, benchmark comparisons, the 32B RL-vs-distillation result) with strong fidelity. One softer point: the SFT+RL pipeline's third and fourth expected stages (rejection-sampling-based general SFT with ~800K examples; a distinct final RL polish for helpfulness/harmlessness) are compressed into a single, less specific 'Iterative Refinement' item that gestures at the same process without naming rejection sampling or the 800K figure — the underlying idea is present but notably less precise, flagged as a borderline case rather than a clear gap (see summary). As in other presets for this lesson, the expected section's specific 'additional comparisons' suggestion is also replaced with a different pair.
- `fl`: The 4 main ways to build and improve reasoning models:
**1:** All figures land in the same relative position as their expected counterparts, including the distillation-process figure landing after the classical-distillation-comparison explanation exactly as the expected section has it. Every exploration-grounded addition (symbolic-AI history, PRM lifecycle, lightweight verifiers, DPO cold-start, latent self-reflection) has its own local lead-in and does not disrupt the surrounding idea order, including the DPO addition inserted before the reward-mechanics figure without changing its position relative to the expected section's own ideas.
- `de`: The 4 main ways to build and improve reasoning models:
**1:** [instances=4; quality=strong,strong,strong,strong] Four qualifying depth additions, each traceable to an exploration-phase source. (1) In inference-time scaling: the PRM development lifecycle — "generating process data..., training the PRM..., and then using the PRM to improve the reasoning model. This improved model can then generate even better data, continuing the cycle" [9], traceable to the exploration-phase PRM survey (a fully scraped dedicated paper) closely. (2) Also in inference-time scaling: lightweight verifiers that "probe a model's internal states to estimate the credibility of its reasoning steps without needing a separate, large reward model" [10], traceable to an exploration source (ReProbe) verbatim. (3) In the Pure RL sub-section: the DPO-based cold-start alternative — "achieve smoother and more stable convergence" [18], traceable to an exploration source closely. (4) Also in Pure RL: the latent-self-reflection/pretraining-mixture discussion — self-reflection as a pre-existing capability merely amplified by RL, and pretraining mixture as a key driver of RL stability — traceable to two exploration sources (including a fully scraped dedicated paper on probing self-reflection) closely, cited [19], [20]. Each is classified strong: a specific, multi-sentence technical mechanism or named alternative, not a generic mention.
- `be`: The 4 main ways to build and improve reasoning models:
**1:** [instances=1; quality=strong] One qualifying breadth addition: "this approach has roots in historical symbolic AI systems, which also relied on structured, step-by-step procedures to perform logical deduction. CoT prompting effectively elicits a similar symbolic-like behavior from modern neural networks" [6], traceable to an exploration-phase source on symbolic-AI history closely. This qualifies as 'historical context or evolution of the topic' and 'cross-domain analogies... from other fields.' Classified as strong: a specific, well-integrated historical account naming the symbolic/connectionist distinction.
- `cp`: The 4 main ways to build and improve reasoning models:
**1:** depth_enhancement and breadth_enhancement both scored 1 for this section (four depth additions and one breadth addition). Each is a contained paragraph or clause placed at a natural point within its own sub-section, and the four techniques and the DeepSeek-R1 case study remain clearly the dominant focus throughout this large section. CorePreservation scores 1.
- `ga`: The 4 main ways to build and improve reasoning models:
**0:** Content-wise this section covers nearly everything the guideline requires, including the required 'at least two useful additional comparisons,' with the one caveat that the third/fourth SFT+RL stages are compressed and less specific than the guideline's own level of detail (see CoreContent). Prose-only word count is approximately 1,653 words against a 1,950-word target (±195 tolerance, range 1,755–2,145 words), about 102 words below the minimum — outside tolerance.

## Section: S4::section-4-a-brief-look-at-the-deepseek-training-pipeline  (weight=0.070, contribution=+0.0052 FOR standard)
Stored section rewards: standard=0.3777  deep=0.3307  (explore: standard=0.0341  deep=0.0000)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset2`

**Article text:**
```
## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 series provides a transparent case study of how reasoning capabilities can be cultivated. The series includes three main variants, each built upon the last: R1-Zero, R1, and the distilled models [[1]](https://arxiv.org/abs/2501.12948).![A flowchart illustrating the development process of DeepSeek's three reasoning models: R1-Zero, R1, and R1-Distill.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)
Image 5: The development process for DeepSeek's three reasoning models as detailed in their technical report. (Source [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948))

**DeepSeek-R1-Zero** is the foundational model, created using a "cold-start" pure Reinforcement Learning (RL) process directly from the DeepSeek-V3 base model. This approach skips the conventional Supervised Fine-Tuning (SFT) stage that typically precedes RL. The model learns to reason by being rewarded for correct final answers on verifiable tasks, allowing reasoning patterns to emerge without being constrained by human-written examples [[4]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners). This was achieved using Group-wise Reward Policy Optimization (GRPO), an algorithm that avoids the need for a separate critic model. GRPO evaluates a group of model outputs for a given prompt, determines which are above or below average, and applies a PPO-like update. This reduces computational cost and memory usage during the RL phase [[18]](http://scalable-ai.eecs.berkeley.edu/assets/lecture_slides/lecture_15.pdf).

**DeepSeek-R1** is the flagship reasoning model, which refines the capabilities of R1-Zero. It undergoes additional training stages, including SFT and further RL, to improve the readability of its reasoning and its overall performance. This multi-stage process helps align the model's outputs with human preferences while retaining the strong reasoning abilities developed in the R1-Zero phase [[1]](https://arxiv.org/abs/2501.12948).

**DeepSeek-R1-Distill** models are smaller, more efficient versions created by transferring the capabilities of the large R1 model. This is not classical logit-based knowledge distillation. Instead, it involves using the high-quality, step-by-step reasoning outputs generated by R1 as a dataset for SFT on smaller, open-source models like Qwen and Llama. This allows the smaller models to inherit advanced reasoning patterns without undergoing the full, computationally expensive RL training process [[5]](https://redwerk.com/blog/what-is-model-distillation).

The DeepSeek pipeline incorporates all four main techniques we will now examine in depth, allowing a direct comparison of their mechanisms, emergent phenomena, and empirical outcomes.
```
**Grader reasoning:**
- `cc`: A brief look at the DeepSeek training pipeline:
**1:** Both sections accurately describe the DeepSeek R1 training pipeline, covering the three main variants (R1-Zero, R1, R1-Distill) and their development processes.
- `fl`: A brief look at the DeepSeek training pipeline:
**1:** Both sections follow the same order: the summary diagram is presented first in both the expected and generated sections, followed by the explanation of each of the three model variants. A prior pass's claim that the generated section reverses this order is incorrect — the diagram (Image 5) appears immediately after the introductory sentence in the generated section, before any of the three model descriptions, matching the expected output's order.
- `de`: A brief look at the DeepSeek training pipeline:
**1:** [instances=1; quality=standard] A depth addition is present: the generated section explains the mechanics of Group-wise Reward Policy Optimization (GRPO), noting that it evaluates a group of outputs, determines which are above or below average, and applies a PPO-like update, reducing computational cost and memory usage. This qualifies as "technical nuances." Traceable to ref [18], scalable-ai.eecs.berkeley.edu/.../lecture_15.pdf, exploration-phase. Classified as standard: describes the mechanism in general terms without quantified specifics (e.g., no variance/advantage formula, no concrete efficiency numbers).
- `be`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] No breadth additions present.
- `cp`: A brief look at the DeepSeek training pipeline:
**1:** The depth addition providing technical detail about GRPO deepens the explanation of the R1-Zero training process. This addition is well-integrated and supports the core narrative, which remains the dominant focus.
- `ga`: A brief look at the DeepSeek training pipeline:
**1:** The generated section meets all requirements: it introduces the three DeepSeek-R1 variants, includes the specified image, explains the cold-start pure-RL approach, the SFT+RL refinement, and the distillation nuance, and provides the transition. Target 300, tolerance ±30, range 270-330. Exact count: 294. Within range.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset2`

**Article text:**
```
## A brief look at the DeepSeek training pipeline

The release of DeepSeek-R1 provided the first detailed, open-source look into how a state-of-the-art reasoning model is built. The project introduced three related models, each representing a different stage or approach in the development process.![Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)

Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.

First is **DeepSeek-R1-Zero**, a model trained using a "cold-start" pure reinforcement learning (RL) approach. It was developed directly from the DeepSeek-V3 base model, skipping the conventional Supervised Fine-Tuning (SFT) stage that typically precedes RL. This method relies on verifiable reward signals, such as whether a math problem's final answer is correct or if a piece of code passes its unit tests. This is a significant departure from standard RLHF, which is expensive and slow due to its reliance on human annotators [[1]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners).

Next is **DeepSeek-R1**, the flagship reasoning model. It builds on R1-Zero by incorporating additional SFT stages and further RL training. This multi-stage refinement process is designed to improve the readability of the reasoning traces and enhance overall performance, making it more aligned with human preferences [[2]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

Finally, there are the **DeepSeek-R1-Distill** models. These are smaller, more efficient models created by training on the high-quality, step-by-step reasoning outputs generated by the full-scale R1 model. This is not classical, logit-based knowledge distillation. Instead, it is a form of SFT where smaller models learn to mimic the reasoning patterns of a more powerful "teacher" model by training on its textual outputs [[3]](https://redwerk.com/blog/what-is-model-distillation).

The DeepSeek pipeline incorporates all four main techniques for building reasoning models. This allows for a direct comparison of their mechanisms, emergent phenomena, and empirical outcomes, which we will now examine in depth.
```
**Grader reasoning:**
- `cc`: A brief look at the DeepSeek training pipeline:
**1:** Both sections introduce the three DeepSeek-R1 variants (R1-Zero, R1, R1-Distill) built on the V3 base, the cold-start/no-SFT framing for R1-Zero, the SFT+RL refinement for R1, and the non-classical distillation nuance for R1-Distill. No expected idea is missing.
- `fl`: A brief look at the DeepSeek training pipeline:
**1:** The generated section covers the three variants in the same relative order, and places Figure 5 immediately after the three-variant intro and before the detailed model-by-model breakdown, matching the expected section's own preview-diagram placement.
- `de`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: A brief look at the DeepSeek training pipeline:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: A brief look at the DeepSeek training pipeline:
**1:** All required content elements are present: the three variants, the cold-start framing, the SFT+RL refinement, the distillation nuance, and the figure. Prose-only word count is approximately 256 words against a 300-word target (±30 tolerance, range 270–330 words), 14 words below the lower bound — outside tolerance. [Revised: this section's 14-word shortfall was previously scored as a failure per an explicit ruling made in this article. That ruling has since been corrected — it was based on a typo-driven misreading of a different, smaller case (6 words on a 250 target) that was itself later corrected to pass. Per the corrected standard, this shortfall does not warrant a penalty. GuidelineAdherence scores 1.]

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset2`

**Article text:**
```
## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 series offers a transparent look into how reasoning capabilities can be cultivated. The series includes three main variants, each built upon the others, all stemming from the DeepSeek-V3 base model, a 671B parameter Mixture-of-Experts (MoE) architecture [[1]](https://arxiv.org/abs/2501.12948).![Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)
Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report. (Source [https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png))

First is **DeepSeek-R1-Zero**, a model produced via a "cold-start" pure Reinforcement Learning (RL) process. This approach is unconventional because it skips the standard Supervised Fine-Tuning (SFT) stage that usually precedes RL. The implication is that the model must discover reasoning pathways on its own, which requires strong, verifiable reward signals to guide it. This model represents a departure from conventional training approaches, demonstrating that sophisticated reasoning can emerge without supervised data [[29]](https://thelmbook.com/articles#!./DeepSeek-R1.md). This pure RL approach is data-efficient, as it replaces expensive human-annotated reasoning traces with automated checks, such as unit tests for code or numerical matches for math problems.

Next is **DeepSeek-R1**, the flagship reasoning model. It refines R1-Zero by adding iterative stages of SFT and further RL training. This hybrid approach aims to make the model's reasoning more stable, human-readable, and performant, addressing some of the "RL oddities" like language mixing found in R1-Zero [[14]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1). The initial SFT stage uses a small, curated dataset of high-quality reasoning traces, some generated by R1-Zero itself, to give the model a strong foundation before the more intensive RL phases.

Finally, there are the **DeepSeek-R1-Distill** models. These are smaller models that inherit the capabilities of the larger R1 model without undergoing the full, computationally expensive RL process. This is not classical, logit-based knowledge distillation. Instead, it is a form of SFT where smaller models are trained on the high-quality, step-by-step reasoning outputs generated by the large R1 model [[2]](https://redwerk.com/blog/what-is-model-distillation), [[3]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d). This makes the advanced reasoning patterns discovered by the large model accessible on more consumer-grade hardware.

The DeepSeek pipeline incorporates all four main techniques for building reasoning models, which we will now examine in depth. This allows for a direct comparison of their mechanisms, the phenomena that emerge, and their empirical outcomes.
```
**Grader reasoning:**
- `cc`: A brief look at the DeepSeek training pipeline:
**1:** Both sections introduce the three DeepSeek-R1 variants (R1-Zero, R1, R1-Distill) built on the V3 base, the cold-start/no-SFT framing for R1-Zero, the SFT+RL refinement for R1, and the non-classical distillation nuance for R1-Distill.
- `fl`: A brief look at the DeepSeek training pipeline:
**1:** The generated section covers the three variants in the same relative order, and places the figure immediately after the three-variant intro and before the detailed model-by-model breakdown, matching the expected section's own preview-diagram placement.
- `de`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: A brief look at the DeepSeek training pipeline:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: A brief look at the DeepSeek training pipeline:
**1:** All required content elements are present. Prose-only word count is approximately 324 words against a 300-word target (±30 tolerance, range 270–330 words), within tolerance.

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset3`

**Article text:**
```
## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 paper introduces three model variants that illustrate different approaches to building reasoning capabilities [[5]](https://www.nature.com/articles/s41586-025-09422-z). Understanding their relationships provides a clear map of the current landscape.![Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)

Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

First is **DeepSeek-R1-Zero**, a model created using a "cold-start" pure Reinforcement Learning (RL) process directly from the DeepSeek-V3 base model. This approach skips the conventional Supervised Fine-Tuning (SFT) stage that typically precedes RL. The idea is that by not pre-exposing the model to human-annotated reasoning paths, it can discover more novel and potentially more effective problem-solving strategies on its own. This requires strong, verifiable reward signals, such as checking the final answer in a math problem, to guide the model's learning [[6]](https://thelmbook.com/articles#!./DeepSeek-R1.md).

Next is **DeepSeek-R1**, the flagship reasoning model. It builds upon the insights from R1-Zero but follows a more refined, multi-stage training process. This pipeline starts with a small amount of "cold-start" SFT data to give the model a better initial grasp of generating readable, human-aligned thought processes. This is followed by large-scale RL and further SFT stages to enhance both reasoning and general abilities, making it more stable and user-friendly than the raw R1-Zero [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

Finally, we have the **DeepSeek-R1-Distill** models. These are smaller, more efficient models that inherit the reasoning capabilities of the large R1 model. This process is not classical knowledge distillation, where a student model mimics the teacher's output probabilities (logits). Instead, it is a form of SFT where smaller open-source models (like Llama and Qwen) are fine-tuned on a large dataset of 800,000 high-quality reasoning traces generated by DeepSeek-R1 [[8]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d), [[9]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).

The DeepSeek pipeline incorporates all four main techniques for building reasoning models. We will now examine each of these in depth to compare their mechanisms and outcomes.
```
**Grader reasoning:**
- `cc`: A brief look at the DeepSeek training pipeline:
**1:** Both sections accurately outline the DeepSeek R1 training pipeline, introducing the three main variants: DeepSeek-R1-Zero, DeepSeek-R1, and DeepSeek-R1-Distill, in the same order and with consistent descriptions of how each relates to the others.
- `fl`: A brief look at the DeepSeek training pipeline:
**1:** Both sections present the three model variants in the same order (Zero → R1 → Distill). A prior pass's claim that the orders differ was self-contradictory — it described both the expected and generated sequences identically as "Zero -> R1 -> Distill" while asserting they differ. I confirmed directly that the generated section's order ("First is DeepSeek-R1-Zero... Next is DeepSeek-R1... Finally, we have the DeepSeek-R1-Distill models") matches the expected output's order exactly.
- `de`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] No depth additions present. The section provides a high-level overview of the pipeline, consistent with the expected output, without adding deeper technical details or implementation challenges.
- `be`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] No breadth additions present.
- `cp`: A brief look at the DeepSeek training pipeline:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so CorePreservation is 1 by default as there are no qualifying additions to evaluate.
- `ga`: A brief look at the DeepSeek training pipeline:
**1:** The generated section meets all requirements: it introduces the three variants, includes the specified image, explains the cold-start pure-RL approach, the SFT+RL refinement, and the distillation nuance, and provides the transition. The prose-only word count is approximately 276 words, within the 300-word target's 270–330 range (a narrow margin, only 6 words above the floor, but within tolerance).

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset3`

**Article text:**
```
## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 series offers a transparent look into a state-of-the-art reasoning model pipeline. It consists of three main variants, each building on the last, to progressively refine reasoning capabilities while also making them more accessible [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1), [[8]](https://arxiv.org/abs/2501.12948).![Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)
Image 5: The development process of DeepSeek's three reasoning models. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

First is **DeepSeek-R1-Zero**, which is created using a "cold-start" pure Reinforcement Learning (RL) process directly from the DeepSeek-V3 base model. This approach bypasses the conventional Supervised Fine-Tuning (SFT) stage that typically precedes RL. The model, trained with Group Relative Policy Optimization (GRPO), learns to reason by being rewarded for correct final predictions on verifiable tasks. This allows reasoning traces to emerge naturally without being constrained by human-annotated examples, though it can lead to usability issues like language mixing [[9]](https://thelmbook.com/articles#!./DeepSeek-R1.md), [[8]](https://arxiv.org/abs/2501.12948).

Next is **DeepSeek-R1**, the flagship model. It refines R1-Zero through a multi-stage framework that integrates SFT and additional RL. It begins with a "cold-start" SFT on a small dataset of human-aligned reasoning traces to improve readability and stability. This is followed by large-scale RL with additional rewards for language consistency to address issues like language mixing that appeared in R1-Zero. The process also includes rejection sampling to generate a broader dataset for further SFT, making the model more of a general-purpose assistant [[10]](https://transitions.substack.com/p/the-laymans-introduction-to-deepseek), [[8]](https://arxiv.org/abs/2501.12948).

Finally, the **DeepSeek-R1-Distill** models are smaller, more efficient versions. Their creation is not classical logit-based knowledge distillation. Instead, smaller open-source models like Llama and Qwen are trained via SFT on a large dataset of 800,000 high-quality reasoning outputs generated by the full DeepSeek-R1 model [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d), [[12]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond). This transfers the reasoning capabilities to more accessible models without the need for a complex RL stage, making it a more efficient process for smaller models [[8]](https://arxiv.org/abs/2501.12948).

The DeepSeek pipeline incorporates all four main techniques we will now examine in depth, allowing direct comparison of their mechanisms, emergent phenomena, and empirical outcomes.
```
**Grader reasoning:**
- `cc`: A brief look at the DeepSeek training pipeline:
**1:** Both sections introduce the three DeepSeek-R1 variants (R1-Zero, R1, R1-Distill) built on the V3 base, the cold-start/no-SFT framing for R1-Zero, the SFT+RL refinement for R1, and the non-classical distillation nuance for R1-Distill. No expected idea is missing.
- `fl`: A brief look at the DeepSeek training pipeline:
**1:** The generated section covers the three variants in the same relative order, and places Image 5 immediately after the three-variant intro and before the detailed model-by-model breakdown, matching the expected section's own preview-diagram placement.
- `de`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: A brief look at the DeepSeek training pipeline:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: A brief look at the DeepSeek training pipeline:
**1:** All required content elements are present: the three variants, the cold-start framing, the SFT+RL refinement, the distillation nuance, and the figure. Prose-only word count is approximately 291 words against a 300-word target (±30 tolerance, range 270–330 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset3`

**Article text:**
```
## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 family of models provides an excellent case study for understanding how reasoning capabilities are developed. The pipeline involves three key variants, each building on the last. This multi-stage approach highlights the different strategies available for creating specialized reasoning models, from raw, emergent capabilities to polished, user-friendly systems.![Image 5: Development process of DeepSeek's three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)
Image 5: Development process of DeepSeek's three different reasoning models that are discussed in the DeepSeek R1 technical report. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

First, there is **DeepSeek-R1-Zero**. This model is created using a "cold-start" pure Reinforcement Learning (RL) process directly from the DeepSeek-V3 base model. Unlike standard RLHF, this approach skips the initial Supervised Fine-Tuning (SFT) stage. The idea is that by not constraining the model with human-defined reasoning patterns, it can explore and discover novel reasoning pathways on its own. This requires strong, verifiable reward signals, such as checking the correctness of a final answer in a math problem [[12]](https://thelmbook.com/articles#!./DeepSeek-R1.md).

Next is **DeepSeek-R1**, the flagship reasoning model. It refines R1-Zero through additional SFT stages and further RL training. This multi-stage process helps address some of the "RL oddities" found in R1-Zero, like poor readability or mixing languages, making the model more aligned with human preferences while retaining its strong reasoning abilities [[13]](https://artgor.medium.com/paper-review-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning-edf4343dcf3a).

Finally, there are the **DeepSeek-R1-Distill** models. This is not classical knowledge distillation where logits are transferred. Instead, it involves taking the high-quality, long chain-of-thought outputs generated by the powerful R1 model and using them as a dataset for SFT on smaller, open-source models like Llama and Qwen. This transfers the reasoning capabilities to more efficient models without repeating the expensive RL process from scratch [[14]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).

The DeepSeek pipeline incorporates all four main techniques for building reasoning models, which we will now examine in depth.
```
**Grader reasoning:**
- `cc`: A brief look at the DeepSeek training pipeline:
**1:** Both sections introduce the three DeepSeek-R1 variants (R1-Zero, R1, R1-Distill) built on the V3 base, the cold-start/no-SFT framing for R1-Zero, the SFT+RL refinement for R1, and the non-classical distillation nuance for R1-Distill.
- `fl`: A brief look at the DeepSeek training pipeline:
**1:** The generated section covers the three variants in the same relative order, and places the figure immediately after the three-variant intro and before the detailed model-by-model breakdown, matching the expected section's own preview-diagram placement.
- `de`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: A brief look at the DeepSeek training pipeline:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: A brief look at the DeepSeek training pipeline:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: A brief look at the DeepSeek training pipeline:
**1:** All required content elements are present. Prose-only word count is approximately 260 words against a 300-word target (±30 tolerance, range 270–330 words), 10 words below the lower bound — within the established noise range.

## Section: S1::section-1-methods-and-strategies-for-building-and-refining-reasoning-models  (weight=0.058, contribution=+0.0073 FOR standard)
Stored section rewards: standard=0.2452  deep=0.1974  (explore: standard=0.0683  deep=0.0000)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset2`

**Article text:**
```
Reasoning models are set to be the key LLM specialization trend of 2025. This evolution moves beyond familiar patterns like Retrieval-Augmented Generation (RAG) or domain-specific fine-tuning. Instead of injecting knowledge, reasoning specialization targets the emergence of robust, multi-step logical capabilities. This allows models to tackle complex problems that require more than simple information retrieval.![A diagram showing four stages of LLM development, with the fourth stage being specialization.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)
Image 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases. (Source [DeepSeek R1's recipe to replicate o1 and the future of reasoning LMs](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1))

This specialization is aimed at tasks like mathematical proofs, logical puzzles, and competitive programming. It does not replace general-purpose LLMs, which remain effective for everyday generation, summarization, or simple question-answering. However, these advanced reasoning capabilities come with trade-offs. The gains in logic are often accompanied by increased inference latency and cost due to longer, more detailed outputs. For instance, OpenAI's o1 models are slower and up to six times more expensive than GPT-4o for the same number of tokens, largely because they are designed to "think" longer before responding [[9]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison), [[2]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o). There is also a risk of "overthinking" on trivial tasks, where a specialized model might introduce unnecessary complexity that a standard model would handle correctly and efficiently. Recent research has begun to systematically study this phenomenon, finding that answer quality can follow an inverted U-shaped curve where too much reasoning hurts performance, especially on easier problems [[16]](https://arxiv.org/html/2604.10739v1).

In this article, we will explore the world of reasoning models. We will cover the following topics:

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we will now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.
```
**Grader reasoning:**
- `cc`: Introduction:
**1:** Both sections cover the same core ideas: introducing reasoning models as a key 2025 specialization trend, discussing their focus on complex tasks, mentioning the trade-offs like increased cost and latency, and presenting the six-item roadmap verbatim as a numbered list, matching the expected output exactly.
_(matched by ordinal position -- title text didn't match)_
- `fl`: Introduction:
**1:** Both sections follow the same logical flow: introducing the specialization trend, explaining the scope and trade-offs, and presenting the roadmap. The image placement is also consistent.
_(matched by ordinal position -- title text didn't match)_
- `de`: Introduction:
**1:** [instances=1; quality=strong] A depth addition is present: the generated section discusses the "overthinking" phenomenon, noting that answer quality can follow an inverted U-shaped curve where too much reasoning hurts performance on easier problems. This qualifies as "limitations, criticisms, or failure modes of the core topic." Traceable to ref [16], arxiv.org/html/2604.10739v1, confirmed inside research.md's exploration-phase block (both as a Q&A source and a fully scraped article). Classified as strong: a specific, named phenomenon (the inverted-U shape) from a documented study, not a vague mention.
_(matched by ordinal position -- title text didn't match)_
- `be`: Introduction:
**0:** [instances=0] No breadth additions present.
_(matched by ordinal position -- title text didn't match)_
- `cp`: Introduction:
**1:** The depth addition about the "overthinking" phenomenon is a well-integrated paragraph that enriches the discussion of trade-offs mentioned in the ground truth. The core narrative — introducing reasoning models and outlining the article — remains the dominant focus.
_(matched by ordinal position -- title text didn't match)_
- `ga`: Methods and Strategies for Building and Refining Reasoning Models:
**0:** The generated section meets the substantive requirements — it positions reasoning models as the 2025 trend, includes the specified image, clarifies scope and drawbacks, presents the 6-point roadmap verbatim as a numbered list (an exact match to the guideline), and provides the correct transition. Target 250, tolerance ±25, range 225-275. Exact count: 302. **27 words above the maximum.** This is an over-maximum case, not a shortfall — the recent ruling that small shortfalls (roughly single digits to ~10 words under) don't warrant a penalty was specifically about under-target margins; whether the same leniency extends to a 27-word overage is a new question this section raises rather than one already settled. Scoring 0 conservatively pending that determination — flagged as borderline, see summary.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset2`

**Article text:**
```
## Methods and Strategies for Building and Refining Reasoning Models

Reasoning models are set to be the key LLM specialization trend for 2025. This evolution extends beyond the patterns we already know, such as Retrieval-Augmented Generation (RAG) and domain-specific fine-tuning. Instead of just injecting knowledge, reasoning models aim to develop robust, multi-step logical capabilities.![Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)

Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.

This specialization targets complex tasks like mathematical proofs, logical puzzles, and competitive programming. It does not replace general-purpose LLMs for everyday generation, summarization, or simple QA. However, these advanced reasoning capabilities come with trade-offs. The gains are often accompanied by increased inference latency and cost due to longer outputs, a risk of overthinking simple tasks, and the reality that improving one capability can degrade performance in others. For instance, research has shown that forcing a model to "think" for too long on a simple problem can cause it to abandon a correct initial answer, a phenomenon known as "overthinking" [[19]](https://arxiv.org/html/2604.10739v1). This highlights a critical engineering challenge: balancing advanced reasoning with efficiency.

This article will serve as a guide to this new frontier. We will:

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.
```
**Grader reasoning:**
- `cc`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** Both sections position reasoning models as the 2025 specialization trend extending beyond RAG/fine-tuning, note it does not replace general-purpose LLMs, name the same drawbacks (latency/cost, overthinking, capability trade-offs across areas), and present the identical 6-item roadmap. The generated section's exploration-grounded overthinking citation is an addition layered on top of, not displacing, the expected ideas.
- `fl`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** The generated section follows the same progression as the expected one: trend framing, Figure 1 in the same relative position, scope/drawback discussion (with its exploration-grounded addition carrying its own local lead-in), then the roadmap. As with other presets for this lesson, the expected section's own ending is a casual sign-off rather than a bridging transition, so its absence here does not cost a required transition.
- `de`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** [instances=1; quality=standard] One qualifying depth addition: "research has shown that forcing a model to 'think' for too long on a simple problem can cause it to abandon a correct initial answer, a phenomenon known as 'overthinking'" [19], traceable to the exploration-phase "When More Thinking Hurts" source. This qualifies as 'limitations, criticisms, or failure modes of the core topic.' Classified as standard: a brief, single-clause mention rather than an elaborated mechanism explanation.
- `be`: Methods and Strategies for Building and Refining Reasoning Models:
**0:** [instances=0] research.md's exploration-phase sources include a depth-qualifying instance credited above, but no breadth-qualifying addition — one that connects outward to an adjacent field rather than deepening the core topic itself — is present in this section.
- `cp`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** depth_enhancement scored 1 for this section (one standard-tier overthinking addition). The addition is a single clause placed within the existing drawbacks discussion and does not shift the section's focus away from positioning reasoning models as the 2025 specialization trend. CorePreservation scores 1.
- `ga`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** The mandatory six-item roadmap is reproduced verbatim, no separate Introduction header is added above it, and all three named drawbacks are present. Prose-only word count is approximately 252 words against a 250-word target (±25 tolerance, range 225–275 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset2`

**Article text:**
```
Reasoning models are the key LLM specialization trend for 2025. This evolution extends beyond the patterns we already know, such as Retrieval-Augmented Generation (RAG) and domain-specific fine-tuning. Instead of just injecting knowledge, reasoning models aim to develop robust, multi-step logical capabilities.![Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)
Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases. (Source [https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png))

This specialization targets complex, multi-step tasks like mathematical proofs, logical puzzles, and competitive programming. It does not replace general-purpose LLMs for everyday generation, summarization, or simple question-answering. However, these advanced reasoning capabilities come with trade-offs. The most notable drawbacks are increased inference latency and cost due to longer, more detailed outputs. There is also the risk of "overthinking" on simple tasks, where the model might introduce unnecessary complexity. Recent studies have shown that accuracy can follow an inverted U-shaped curve with chain-of-thought length, where too much thinking hurts performance [[22]](https://arxiv.org/html/2604.10739v1). Finally, specialization is not free; improving capabilities in one area can sometimes degrade fluency or efficiency in others.

In this article, we will explore the world of reasoning models. We will cover:

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.
```
**Grader reasoning:**
- `cc`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** Both sections position reasoning models as the 2025 specialization trend extending beyond RAG/fine-tuning, note it does not replace general-purpose LLMs, and present the identical 6-item roadmap. As established for this lesson, the expected section defers detailed drawback discussion to Section 3, so the generated section's drawback mentions (including the exploration-grounded overthinking citation) are additions, not requirements.
- `fl`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** The generated section follows the same progression as the expected one: trend framing, the figure in the same relative position, drawback discussion (with its exploration-grounded addition carrying its own local lead-in), then the roadmap.
- `de`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** [instances=1; quality=standard] One qualifying depth addition: "accuracy can follow an inverted U-shaped curve with chain-of-thought length, where too much thinking hurts performance" [22], traceable to the exploration-phase 'When More Thinking Hurts' source closely. This qualifies as 'limitations, criticisms, or failure modes of the core topic.' Classified as standard: a brief, single-sentence mention.
- `be`: Methods and Strategies for Building and Refining Reasoning Models:
**0:** [instances=0] research.md's exploration-phase sources include a depth-qualifying instance credited above, but no breadth-qualifying addition — one that connects outward to an adjacent field — is present in this section.
- `cp`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** depth_enhancement scored 1 for this section (one standard-tier overthinking addition). The addition is a single sentence within the existing drawbacks discussion and does not shift the section's focus away from positioning reasoning models as the 2025 specialization trend. CorePreservation scores 1.
- `ga`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** All required content elements are present, including the verbatim roadmap. Prose-only word count is approximately 247 words against a 250-word target (±25 tolerance, range 225–275 words), within tolerance.

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset3`

**Article text:**
```
# Methods and Strategies for Building and Refining Reasoning Models

Reasoning models are the key LLM specialization trend for 2025. This evolution extends beyond patterns we already know, such as Retrieval-Augmented Generation (RAG) and domain-specific fine-tuning. Instead of just injecting knowledge, reasoning specialization targets the emergence of robust, multi-step logical capabilities, allowing models to *think* rather than just *know*. This focus on the process of deduction enables them to tackle complex tasks like mathematical proofs, logical puzzles, and competitive programming that were previously out of reach.![Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)

Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

This specialization does not replace general-purpose LLMs for everyday generation, summarization, or simple question-answering. However, these powerful reasoning abilities come with drawbacks. The gains are often accompanied by increased inference latency and cost due to longer, more detailed outputs. There is also a risk of "overthinking" on trivial tasks, where a model might introduce unnecessary complications that a base model would solve correctly in one pass. Specialization is not free; improving capability in one area can sometimes degrade fluency or efficiency in others. This trade-off means that while a reasoning model might excel at a complex calculus problem, it could be slower and more expensive for a simple summarization task, making the choice of model critical for production systems.

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we will now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.
```
**Grader reasoning:**
- `cc`: Introduction:
**1:** Both sections serve as an introduction, covering the rise of reasoning models as a specialization trend and outlining the article's structure via the six-item roadmap, presented verbatim as a numbered list in both. The core topics and ideas are the same.
_(matched by ordinal position -- title text didn't match)_
- `fl`: Introduction:
**1:** Both sections follow the same flow: introducing the topic, providing the numbered roadmap, and closing with a transition sentence. A prior pass claimed the generated section "omits the final transition sentence," but this is incorrect — the closing sentence ("Having set the context and roadmap, we will now establish a working definition of 'reasoning model'...") is present, immediately before the next H2 header.
_(matched by ordinal position -- title text didn't match)_
- `de`: Introduction:
**0:** [instances=0] No depth additions present. The section is a brief introduction without any theoretical foundations, technical nuances, or real-world case studies.
_(matched by ordinal position -- title text didn't match)_
- `be`: Introduction:
**0:** [instances=0] No breadth additions present.
_(matched by ordinal position -- title text didn't match)_
- `cp`: Introduction:
**1:** Both depth_enhancement and breadth_enhancement scored 0, so CorePreservation is 1 by default as there are no qualifying additions to evaluate.
_(matched by ordinal position -- title text didn't match)_
- `ga`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** The generated section meets the substantive requirements — the six-point roadmap is present, verbatim, as a numbered list; the section correctly positions reasoning models as the 2025 trend, includes the specified image, and provides the correct transition. Note on the exact count: the article's H1 is indented with 4 leading spaces ("    # Methods and..."), which in standard Markdown triggers an indented code block rather than a heading — under a strict reading it wouldn't render as a title at all. Consistent with how every other article's H1 is excluded from the section's own word count regardless of this formatting quirk, it is excluded here too. Target 250, tolerance ±25, range 225-275. Exact count: 281. **6 words above the maximum.** This is an over-maximum case, not a shortfall — the same open question flagged in the immediately preceding article (there, 20 and 27 words over): whether the confirmed shortfall-leniency threshold extends to overages in the same way. Per ruling, a 6-word margin against a 250-word target is trivial and does not warrant a penalty. GuidelineAdherence scores 1.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset3`

**Article text:**
```
Reasoning models are emerging as a key specialization trend for LLMs in 2025. This evolution moves beyond familiar patterns like Retrieval-Augmented Generation (RAG) or domain-specific fine-tuning. Instead of just injecting knowledge, reasoning specialization aims to cultivate robust, multi-step logical capabilities within the models themselves. This focus on the *process* of thinking, rather than just the final output, is what sets these models apart and makes them a critical component for the future of agentic AI.![Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)
Image 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

This specialization is tailored for complex tasks like mathematical proofs, logical puzzles, and competitive programming. It does not replace general-purpose LLMs for everyday tasks like generation, summarization, or simple question-answering. However, these advanced reasoning capabilities come with trade-offs. The gains are often accompanied by increased inference latency and cost due to longer, more detailed outputs. There is also a risk of "overthinking" on trivial tasks, where a model might introduce unnecessary complexity. Furthermore, specialization is not a free lunch; improving capability in one area can sometimes degrade fluency or efficiency in others.

In this article, we will cover the following topics:

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we will now establish a working definition of a "reasoning model" that you can use to evaluate future systems and research.
```
**Grader reasoning:**
- `cc`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** Both sections position reasoning models as the 2025 specialization trend extending beyond RAG/fine-tuning, note it does not replace general-purpose LLMs, name the same drawbacks (latency/cost, overthinking, capability trade-offs), and present the identical 6-item roadmap. The generated section's framing of this as a focus on the 'process of thinking' is an elaboration that does not displace any expected idea.
- `fl`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** The generated section follows the same progression as the expected one: trend framing, Image 1 in the same relative position, scope/drawback discussion, then the roadmap. As with other presets for this lesson, the expected section's own ending is a casual sign-off rather than a bridging transition, so its absence here does not cost a required transition.
- `de`: Methods and Strategies for Building and Refining Reasoning Models:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Methods and Strategies for Building and Refining Reasoning Models:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** All required content elements are present, including the verbatim roadmap and all three named drawbacks. Prose-only word count is approximately 263 words against a 250-word target (±25 tolerance, range 225–275 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset3`

**Article text:**
```
## Methods and Strategies for Building and Refining Reasoning Models

Reasoning models are the key 2025 LLM specialization trend. This approach extends beyond familiar patterns like Retrieval-Augmented Generation (RAG) or domain-specific fine-tuning. It targets the emergence of robust, multi-step logical capabilities rather than simply injecting external knowledge. This specialization is crucial for building the next generation of agentic AI systems that can tackle complex problems autonomously.![Image 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)
Image 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

This specialization is aimed at complex, multi-step tasks like mathematical proofs, logical puzzles, and competitive programming. It does not replace general-purpose LLMs for everyday generation, summarization, or simple QA. However, these reasoning gains come with drawbacks. They often introduce increased inference latency and cost due to longer outputs, a risk of overthinking trivial tasks, and the non-free nature of specialization where capability improvements in one area can degrade fluency or efficiency in others.

This article will cover the following topics:

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.
```
**Grader reasoning:**
- `cc`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** Both sections position reasoning models as the 2025 specialization trend extending beyond RAG/fine-tuning, note it does not replace general-purpose LLMs, and present the identical 6-item roadmap. All three named drawbacks (latency/cost, overthinking, non-free specialization) are explicit, matching the guideline's own list even though the expected section itself defers detailed drawback discussion to Section 3.
- `fl`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** The generated section follows the same progression as the expected one: trend framing, the figure in the same relative position, drawback discussion, then the roadmap.
- `de`: Methods and Strategies for Building and Refining Reasoning Models:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: Methods and Strategies for Building and Refining Reasoning Models:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: Methods and Strategies for Building and Refining Reasoning Models:
**1:** All required content elements are present, including the verbatim roadmap and all three named drawbacks. Prose-only word count is approximately 221 words against a 250-word target (±25 tolerance, range 225–275 words), 4 words below the lower bound — within the established noise range.

## Section: S2::section-2-how-do-we-define-reasoning-model  (weight=0.081, contribution=+0.0164 FOR standard)
Stored section rewards: standard=0.4889  deep=0.3534  (explore: standard=0.1452  deep=0.0227)

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
**1:** [instances=1; quality=strong] One depth addition is present: the claim that reasoning capabilities emerge as a function of model scale, with CoT prompting's benefits only materializing in models with roughly 100 billion parameters. This qualifies as "theoretical foundations" / technical nuances, traceable to ref [21], research.google/blog/language-models-perform-reasoning-via-chain-of-thought, confirmed exploration-phase. Classified as strong: a specific, quantified emergence threshold. [Reclassification note: a second candidate — CoT's shift from an explicit, user-prompted technique into an automated, internalized, self-directed mechanism (ref [17]) — was previously counted here as a depth instance. On review, the rubric's breadth bullet explicitly lists "historical context or evolution of the topic," and this content is literally describing CoT's own evolution over time from one form to another — it fits that bullet more directly than any depth bullet. Moved to breadth_enhancement below rather than double-counted here.]
- `be`: How do we define "reasoning model"?:
**1:** [instances=1; quality=standard] A breadth addition is present: the claim that CoT prompting evolved from an explicit, user-prompted technique into an automated, internalized mechanism that lets the model self-direct its reasoning without explicit prompting. This qualifies as "historical context or evolution of the topic" — the rubric's own bullet for this criterion describes exactly this pattern (the same mechanism's development over time), so this does not need to connect to a different field to qualify as breadth. Traceable to ref [17], nvidia.com/en-us/glossary/cot-prompting, confirmed exploration-phase. Classified as standard: a brief, single-sentence assertion without a fuller mechanism explanation or quantified detail. [Reclassified from depth_enhancement on review — see note there.]
- `cp`: How do we define "reasoning model"?:
**1:** The depth addition about reasoning as an emergent property of model scale is a concise, relevant technical detail that enhances the definition without overshadowing it. The ground truth core remains the primary focus of the section.
- `ga`: How do we define "reasoning model"?:
**1:** The generated section meets all requirements: it defines a reasoning model, provides a contrasting example, includes both required images, maps the reasoning spectrum, differentiates visible and invisible steps, and provides the transition. Target 350, tolerance ±35, range 315-385. Exact count: 363. Within range.

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

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/Understanding_Reasoning_LLMs__preset3`

**Article text:**
```
## How do we define "reasoning model"?

A reasoning model is an LLM designed to solve multi-step problems by generating intermediate thoughts. This process can be explicit, appearing as a visible chain of thought, or it can happen internally as hidden iterations. This contrasts with standard LLMs that often rely on direct factual recall or single-pass pattern matching for simpler prompts. For example, a basic question like "How far does a train go at 60 mph for 3 hours?" can be answered directly, while a more complex problem benefits from breaking it down into smaller, logical steps.![Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.)](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)

Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.) (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

The spectrum of reasoning is broad. All modern LLMs exhibit some basic reasoning, which can be improved with techniques like Chain-of-Thought (CoT) prompting [[1]](https://arxiv.org/abs/2205.11916). This step-by-step approach is not entirely new; it has roots in classic symbolic AI, which relied on structured, rule-based systems for logical deduction. Modern CoT prompting can be seen as an evolution of these ideas, where the LLM acts as a flexible symbolic reasoner, generating intermediate steps that mimic a logical proof or calculation [[2]](https://www.mdpi.com/2227-7390/13/11/1707), [[3]](https://www.youtube.com/watch?v=yo8HtAbUynA). However, specialized reasoning models are engineered for excellence on difficult benchmarks, such as math olympiad problems, formal proofs, or novel puzzles.

The intermediate steps in these models manifest in two primary ways. The first is through **visible thought traces**, where the model outputs a step-by-step reasoning process that the user can read and follow. This enhances transparency and allows for easier debugging. The second is through **invisible internal iterations**, like those rumored to be used in OpenAI's o1 model. In this approach, the model allocates more computation time at inference to "think" internally without necessarily exposing every step to the user. This can improve performance on complex tasks while presenting a clean, final answer, though it sacrifices the interpretability of a visible thought process.![Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)

Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.
```
**Grader reasoning:**
- `cc`: How do we define "reasoning model"?:
**1:** Both sections define a "reasoning model" as an LLM that solves multi-step problems by generating intermediate thoughts, contrasting it with standard LLMs. They both discuss the two ways these intermediate steps can manifest (explicit visible traces vs. internal iterations).
- `fl`: How do we define "reasoning model"?:
**1:** Both sections follow the same logical flow: a general definition, a simple example, discussion of the reasoning spectrum, and the two ways intermediate steps can appear. The breadth addition about symbolic AI is integrated smoothly and does not disrupt the main narrative.
- `de`: How do we define "reasoning model"?:
**0:** [instances=0] No depth additions present. The symbolic-AI connection in this section is a breadth addition (historical context from an adjacent field/paradigm), not a depth one, since it does not intensify understanding of the LLM reasoning process itself; it is evaluated under breadth_enhancement instead.
- `be`: How do we define "reasoning model"?:
**1:** [instances=1; quality=standard] A breadth addition is present: the section connects modern Chain-of-Thought prompting to its roots in classic symbolic AI, a genuinely prior/distinct paradigm of structured, rule-based logical deduction, framing modern CoT as an evolution of that older approach. This qualifies as "historical context or evolution of the topic." Traceable to ref [2] (mdpi.com/2227-7390/13/11/1707) and ref [3] (youtube.com/watch?v=yo8HtAbUynA), both confirmed inside the exploration-phase block, treated as one instance since both support the same historical-lineage claim in the same paragraph. Classified as standard: a brief, single-paragraph historical connection, comparable in depth of elaboration to other historical-lineage additions rated standard (e.g., a symbolic-AI-predecessor framing without further mechanism detail).
- `cp`: How do we define "reasoning model"?:
**1:** The breadth addition connecting Chain-of-Thought to its roots in symbolic AI is a concise, well-integrated paragraph that provides historical context without diluting or overshadowing the primary definition of a reasoning model.
- `ga`: How do we define "reasoning model"?:
**1:** The generated section meets all requirements: it defines a reasoning model, provides a contrasting example, includes both required images, maps the reasoning spectrum, differentiates visible and invisible steps, and provides the transition. The prose-only word count is approximately 318 words, within the 350-word target's 315–385 range (a narrow margin, only 3 words above the floor, but within tolerance).

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate1__preset3`

**Article text:**
```
## How do we define "reasoning model"?

A reasoning model is an LLM designed to solve multi-step problems by generating intermediate steps or structured "thought" processes. Unlike models that provide a direct answer, reasoning models either explicitly display their thought process or handle it internally. This allows them to perform better at complex tasks like puzzles, coding challenges, and mathematical problems [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling). For example, asking "How far does a train traveling at 60 mph for 3 hours go?" might get a direct answer from a standard LLM. A reasoning model, however, would first state the formula `distance = speed × time` before calculating the result.![Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)
Image 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

The spectrum of reasoning is broad. All modern LLMs exhibit some basic reasoning, which can be improved with techniques like Chain-of-Thought (CoT) prompting. This simple method involves adding a phrase like "Let's think step by step" to the prompt, which encourages the model to break down its thinking process [[2]](https://arxiv.org/abs/2205.11916). However, specialized reasoning models are engineered to achieve exceptional performance on difficult benchmarks, such as math olympiad problems or formal proofs, where simple prompting is not enough. This advanced capability is what truly distinguishes them from general-purpose models.

The intermediate steps in these models manifest in two primary ways.

First, there are **visible thought traces**, where the model generates step-by-step outputs that the user can read and follow. This is common in models like DeepSeek-R1, where the reasoning path is part of the final output. This transparency allows users to verify the logic and understand how the model arrived at its conclusion, which is crucial for building trust and for debugging complex reasoning failures.

Second, some models use **invisible internal iterations**. Here, the model allocates additional computation time at inference to "think" without exposing every token of its process. This technique is rumored to be used in models like OpenAI's o1. The model might explore multiple reasoning paths internally, self-correct, and refine its answer before presenting the final, polished result. This approach hides the messy parts of the reasoning process from the user, offering a cleaner output while still benefiting from extended deliberation.![Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)
Image 3: "Reasoning" can refer to the internal process of generating a response or the explicit explanation provided to the user. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.
```
**Grader reasoning:**
- `cc`: How do we define "reasoning model"?:
**1:** Both sections define a reasoning model via multi-step intermediate steps, use a comparable simple-vs-complex query contrast (with the formula shown explicitly), distinguish visible thought traces from invisible/o1-style internal iterations, and note that ordinary LLMs already do basic reasoning via CoT while specialized models excel on the hardest benchmarks. No expected idea is missing.
- `fl`: How do we define "reasoning model"?:
**1:** The generated section follows the same progression as the expected one: definition, example, Image 2, the CoT/basic-reasoning spectrum point, the two manifestations, Image 3, then the transition. Images 2 and 3 land in the same relative positions as the expected section.
- `de`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: How do we define "reasoning model"?:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: How do we define "reasoning model"?:
**1:** All required content elements are present. Prose-only word count is approximately 364 words against a 350-word target (±35 tolerance, range 315–385 words), within tolerance.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/Understanding_Reasoning_LLMs__replicate2__preset3`

**Article text:**
```
## How do we define "reasoning model"?

A reasoning model is an LLM designed to solve multi-step problems by generating intermediate steps, whether those steps are visible to the user or handled internally. Unlike a standard LLM that might provide a direct answer, a reasoning model breaks down the problem, showing its work or thinking through the process to arrive at a more reliable conclusion. This methodical approach is what separates simple pattern matching from genuine problem-solving.![Image 2: A regular LLM may only provide a short answer, whereas reasoning models typically include intermediate steps. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.)](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)
Image 2: A regular LLM may only provide a short answer, whereas reasoning models typically include intermediate steps. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.) (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

For example, asking "How far does a train travel at 60 mph for 3 hours?" is a simple calculation. A standard model might just output "180 miles." A reasoning model, however, would likely first state the formula `distance = speed × time` and then show the calculation, explaining how it arrived at the answer.

All modern LLMs exhibit some level of reasoning, which can be enhanced with techniques like Chain-of-Thought (CoT) prompting. However, specialized reasoning models are engineered to excel at difficult benchmarks, such as math olympiad problems or formal proofs, where multi-step logic is non-negotiable. These models are not just better at following instructions; they are better at thinking.

These intermediate steps can manifest in two primary ways:

1.  **Visible thought traces:** The model generates a step-by-step output that the user can read, similar to showing your work in a math problem. This approach makes the model's reasoning process transparent and interpretable, which is invaluable for debugging and building trust.
2.  **Invisible internal iterations:** The model allocates more computational resources at inference time to "think" internally without exposing every step. This is rumored to be part of the approach used for models like OpenAI's o1, where the model spends more time processing before delivering a final, polished answer. This method prioritizes performance on complex tasks over showing the intermediate work, which can be useful for proprietary systems where the reasoning process itself is a competitive advantage.![Image 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)
Image 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling) [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

With a clear definition established, let's now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.
```
**Grader reasoning:**
- `cc`: How do we define "reasoning model"?:
**1:** Both sections define a reasoning model via multi-step intermediate steps, use a comparable simple-vs-complex query contrast, distinguish visible thought traces from invisible/o1-style internal iterations, and note that ordinary LLMs already do basic reasoning while specialized models excel on the hardest benchmarks.
- `fl`: How do we define "reasoning model"?:
**1:** The generated section follows the same progression as the expected one: definition, example, the first figure, the CoT/basic-reasoning spectrum point, the two manifestations, the second figure, then the transition. Both figures land in the same relative positions as the expected section.
- `de`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `be`: How do we define "reasoning model"?:
**0:** [instances=0] research.md does contain exploration-phase sources for this episode, but this section draws on none of them, so no candidate addition can satisfy the source-attribution gate here.
- `cp`: How do we define "reasoning model"?:
**1:** Both depth_enhancement and breadth_enhancement scored 0 for this section — exploration-phase sources exist for this episode but this section does not draw on any of them. Per the mandatory default rule, CorePreservation scores 1 by default.
- `ga`: How do we define "reasoning model"?:
**1:** All required content elements are present. Prose-only word count is approximately 331 words against a 350-word target (±35 tolerance, range 315–385 words), within tolerance.
