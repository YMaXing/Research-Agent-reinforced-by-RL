## Context of the Article

### What We Are Planning to Share

We are planning to share a comprehensive theory-first examination of reasoning LLMs as the major specialization trend for 2025, defining them around multi-step intermediate thinking (visible or hidden) that enables reliable performance on complex tasks such as advanced math, puzzles, and coding. Using DeepSeek-R1's training pipeline—cold-start RL (R1-Zero), SFT+RL iterations (R1), and distillation to smaller models—as the central detailed case study, we contrast the four primary building approaches: inference-time scaling, pure RL, SFT+RL hybrids, and pure SFT/distillation. We address precisely when reasoning models deliver value versus when they introduce inefficiency, catalog their strengths and weaknesses with concrete contrasts to standard LLMs, compare DeepSeek-R1 head-to-head with o1 on benchmarks and efficiency, and detail budget-conscious methods including small-scale distillation (Sky-T1), pure RL at 3B scale (TinyZero), and journey learning that incorporates error paths.

### Why We Think It's Valuable

Reasoning capabilities are central to agentic AI systems that must decompose complex goals, self-correct, and handle multi-step problems reliably. AI engineers need to understand the tradeoffs in training versus inference techniques, emergence phenomena, and cost-effective distillation to select or build appropriate models rather than defaulting to expensive proprietary options. By dissecting DeepSeek-R1 alongside o1 and open budget projects, readers gain concrete blueprints for matching techniques to constraints, recognizing when specialization costs outweigh benefits, and anticipating hybrid approaches that will dominate production agent deployments.

### Expected Length of the Article

**4,300 words**

### Theory / Practice Ratio

100% theory - 0% practice

## Article Outline

1. Methods and Strategies for Building and Refining Reasoning Models
2. How do we define "reasoning model"?
3. When should we use reasoning models?
4. A brief look at the DeepSeek training pipeline
5. The 4 main ways to build and improve reasoning models
6. Thoughts about DeepSeek R1
7. Developing reasoning models on a limited budget
8. Conclusion

## Section 1 - Methods and Strategies for Building and Refining Reasoning Models

- This is the introduction section, do NOT generate a separate introdution above this section.
- Position reasoning models as the key 2025 LLM specialization trend that extends beyond patterns readers already know — RAG and domain fine-tuning—by targeting the emergence of robust multi-step logical capabilities rather than retrieval or domain knowledge injection.
- Insert a graph with the following online URL syntax:
![Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)
- Clarify that reasoning specialization is aimed at complex multi-step tasks (mathematical proofs, logical puzzles, competitive programming) and does not replace or diminish the utility of general-purpose LLMs for everyday generation, summarization, or simple QA. Then, briefly mention the core drawbacks that accompany reasoning gains: increased inference latency and cost due to longer outputs, risk of overthinking on trivial tasks, and the non-free nature of specialization where capability improvements in one area can degrade fluency or efficiency in others.
- Present the following article roadmap verbatim:

    1. Explain the meaning of "reasoning model"
    2. Discuss the advantages and disadvantages of reasoning models
    3. Outline the methodology behind DeepSeek R1
    4. Describe the four main approaches to building and improving reasoning models
    5. Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
    6. Provide tips for developing reasoning models on a tight budget

- Transition to Section 2: Having set the context and roadmap, we now establish a working definition of "reasoning model" that readers can use to evaluate future systems and research.

- **Section length:** 250 words

## Section 2 - How do we define "reasoning model"?

- Define a reasoning model as one that generates multi-step intermediate thinking—either explicit token traces or hidden internal iterations—for complex queries, in contrast to direct factual recall or single-pass pattern matching that suffices for simpler prompts. Raise a simple example of contrasting a question that requires some simple reasoning against a question that doesn't.
- Insert a graph with the following online URL syntax:
![Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)
- Map the full spectrum: all modern LLMs exhibit basic reasoning improved by CoT prompting, while specialized reasoning models achieve excellence on hard benchmarks such as math olympiad problems, formal proofs, or novel puzzle solving.
- Differentiate the two primary manifestations of intermediate steps in reasoning models: visible thought traces (step-by-step outputs the user can read) versus invisible internal iterations (o1-style hidden chain-of-thought that allocates test-time compute without exposing every token).
- Insert a graph with the following online URL syntax:
![Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)
- Transition to Section 3: With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.

- **Section length:** 350 words

## Section 3 - When should we use reasoning models?

- Before diving into technical details, it is important to consider when reasoning models are needed: reasoning models deliver the highest returns on puzzles, advanced mathematics, competitive coding, and problems requiring decomposition or self-correction, but are overkill for summarization, simple factual QA, or creative writing where direct generation suffices.
- Catalog practical downsides with concrete examples: significantly higher latency and token costs from verbose intermediate steps, increased verbosity that frustrates users in conversational settings, and the risk of overthinking errors (e.g., inventing unnecessary complications on straightforward arithmetic that a base model would solve correctly in one pass).
- Insert a graph with the following online URL syntax:
![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)
- Transition to Section 4: Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.

- **Section length:** 160 words

## Section 4 - A brief look at the DeepSeek training pipeline

- Introduce the three DeepSeek-R1 variants and their relationships: R1-Zero produced via cold-start pure RL from the V3 base, the refined R1 that adds SFT+RL iterations, and the smaller distilled models that transfer capabilities without repeating the full RL process.
- Insert a graph with the following online URL syntax to summarize the development process of these models:
![Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)
- Introduce the first model - DeepSeek-R1-Zero: Contrast the cold-start concept—skipping the conventional SFT stage before RL—with the standard RLHF pipeline, explaining implications for emergence of reasoning traces and the necessity of strong verifiable reward signals.
- Introduce the second model - DeepSeek-R1: Deepseek's flagship reasoning model refined with addtional SFT stages and further RL training, and is an improvement on the cold-started R1-Zero model.
- Introduce the third model - DeepSeek-R1-Distill, clarify the distillation nuance: it is not classical logit-based knowledge distillation but rather SFT of smaller models on high-quality CoT outputs generated by the large reasoning model.
- Transition to Section 5: The DeepSeek pipeline incorporates all four main techniques we will now examine in depth, allowing direct comparison of their mechanisms, emergent phenomena, and empirical outcomes.

- **Section length:** 300 words

## Section 5 - The 4 main ways to build and improve reasoning models

- Write a brief section opening telling readers that current key techniques to enhance LLM reasoning and build speciaized reasoning models will be outlines. Add a note that exact workings of o1 and o3 remain unknown as of date, but they are rumored to combine both inference and training techniques.

### **1) Inference-time scaling**

- Detail inference-time scaling first: make it clear that it refers to increasing inference-time computational resources in this specific context, draw the analogy to giving a human extra thinking time and connect to test-time compute scaling laws.
- Introduce methods including CoT prompting, majority voting, beam search, MCTS, and process reward models. Insert the following two images into appropriate places:
![Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)
![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)
- Explain how the DeepSeek R1 technical report catergorizes common inference-time scaling methods under "unsuccessful attempts" and what it suggests. Speculate the scenario that DeepSeek may still apply inference-time scaling techniques at the application layer.
- Investigate inference-time scaling as the possible reasoning for why OpenAI's o1 and o3 models are relatively more expensive than models like GPT-4o.

### **2) Pure reinforcement learning (RL)**

- Explain pure RL (exemplified by R1-Zero in contrast to typical RL pipeliens involving a SFT model applied before RL): instead of a reward model trained on human preferences, it applies accuracy and format rewards directly on the base model without any prior SFT. Expand on how these two rewards are defined in the R1 Paper.
- Insert a graph with the following online URL syntax:
![Figure 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)
- Describe the emergence of the "Aha" moment, shown in the DeepSeek R1 paper where the model spontaneously generates reasoning traces and self-correction patterns.
- Insert a graph with the following online URL syntax:
![Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)
- Stress that R1-Zero demonstrating reasoning capabitlities by intermediate "thinking" steps is the first instance showing it is possible to develope reasoning models with pure RL.

### **3) Supervised finetuning and reinforcement learning (SFT + RL)**

- Cover the SFT+RL hybrid approach (exemplified by R1) phase by phase: generate cold-start data, apply consistency rewards alongside verifiable RL signals, and iterate through multiple SFT+RL stages; emphasize benefits of this staged refinement over pure RL for stability and performance; insert the following two images in the most appropriate places:
![Figure 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)
![Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)

### **4) Pure supervised finetuning (SFT) and distillation**

- First, for each of the three approaches covered to building and improving reasoning models, write an one-sentence summary.
- Introduce, in detail, how DeepSeek trained smaller models via distillation - transfer reasoning by training smaller models on high-quality CoT datasets produced by larger reasoning models - and contrast how their distillation process is different from the traditional distillation process.
- Insert a graph with the following online URL syntax to clarify their distillation process:
![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)
- Write at least two key reasons why DeepSeek developed the distilled models.
- Insert a graph with the following online URL syntax to compares the performance of these distilled models against other popular models:
![Figure 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)
- Compare effectiveness across approaches based on the DeepSeek-R1 technical report: distillation is noticeably weaker than the larger reasoning model DeepSeek-R1, but outperforms pure RL when applied to smaller models; cite benchmark insights from the DeepSeek report to present the results of testing whether the emergent reasoning behavior could also appear in smaller models.

![Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)

- Discuss the insights on the effectness of distillation versus pure RL and SFT on small models that can be drawn from the results.
- Put forward at least two useful addtional comparisons that could have been in the inserted table above.
- Transition to Section 6: After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we step back to evaluate the release's broader significance and limitations.

- **Section length:** 1950 words

## Section 6 - Thoughts about DeepSeek R1

- Express appreciation for the DeepSeek-R1 models: the open MIT license, the unusually detailed technical report, and the demonstration that pure RL from a cold start can produce emergent reasoning traces and self-correction without supervised warm-up.
- Compare DeepSeek-R1 head-to-head with o1: comparable benchmark quality on math, coding, and reasoning suites yet superior inference efficiency, suggesting DeepSeek placed a training-heavy bet while o1 leans more on inference-time scaling.
- Outline limits to any comparison due to that OpenAI hasn't disclosed much about o1: unknown o1 model size, possible MoE architecture, undisclosed exact mix of techniques, and differences in base model strength that prevent definitive attribution of performance gaps. Stress that a direct comparison between DeepSeek-R1 and o1 is unwarranted unless those things are known.
- Discuss training cost realities: the publicized $6M figure most likely refers to the V3 base model rather than the full R1 RL process, leaving the true incremental cost of reasoning specialization undisclosed. Stress that DeepSeek team has never disclosed the exact GPU hours or development cost for R1.
- Position DeepSeek-R1 as a milestone for open-weight reasoning models, proving that high-level reasoning capabilities need not remain the exclusive domain of closed labs and thereby accelerating research into the four techniques.

- **Section length:** 350 words

## Section 7 - Developing reasoning models on a limited budget

- Start the section by stressing the development cost of reasoning models, even starting with an open-weight model, is discouraging for researchers or engineers with a limited budget.
- Detail the practicality of distillation via the Sky-T1 project: 17K carefully curated samples, roughly $450 budget, and performance approaching o1 on several reasoning benchmarks, illustrating how previous-lesson distillation concepts scale down effectively.
- Insert a table with the following online URL syntax for Sky-T1:
![Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)
- Describe pure RL at small scale with the TinyZero 3B model: trained for under $30, it exhibits emergent self-verification and reasoning traces, reinforcing that cold-start RL can produce useful behaviors even without massive compute.
- Insert a table with the following online URL syntax for TinyZero:
![Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)
- Introduce the journey learning concept: explain journey training on full trajectories that include incorrect paths, self-corrections, and final success rather than only golden solutions (termed shortcut learning) by contrasting journey learning with shortcut learning.
- Explain how exposure to mistakes in SFT data reinforces self-correction mechanisms, contrasting failure modes of shortcut-only datasets (brittle behavior on novel errors) with the robustness gained from journey-style data.
- Insert a table with the following online URL syntax:
![Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. Annotated figure from the O1 Replication Journey: A Strategic Progress Report – Part 1](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)
- Outline future directions: combining insights from these budget projects (Sky-T1 distillation, TinyZero RL, journey learning) with the DeepSeek techniques to create hybrid pipelines that balance cost, emergence, and reliability.

- **Section length:** 600 words

## Section 8 - Conclusion

- Recap the four approaches with crisp characterizations: inference-time scaling (no training cost but high serving cost), pure RL (research insight that unlocks emergent behavior), SFT+RL (production-ready blueprint with verifiable rewards), and distillation (efficient transfer but ultimately derivative).
- Forecast a hybrid future in which the most capable systems combine SFT+RL pipelines with inference-time scaling—precisely the pattern we suspect underlies o1 and will appear in future o3-class models.
- Deliver strategic guidance for AI engineers: match the chosen technique to concrete constraints (budget, performance targets, innovation needs, deployment latency) rather than defaulting to the largest proprietary model; reference the decision heuristic and task-complexity framework introduced earlier.

- **Section length:** 340 words

## Golden Sources

<!-- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) -->
"DeepSeek-R1 _ Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.md"

<!-- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) -->
"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters.md"

<!-- [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982) -->
"O1 Replication Journey _ A Strategic Progress Report -- Part 1.md"

<!-- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) -->
"Large Language Models are Zero-Shot Reasoners.md"