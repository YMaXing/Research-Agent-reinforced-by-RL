# Research

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What information-theoretic limits cause LLMs to lack inherent planning capabilities?</summary>

Phase: [EXPLORATION]

### Source [36]: https://www.emergentmind.com/papers/2511.12869

Query: What information-theoretic limits cause LLMs to lack inherent planning capabilities?

Answer: Information-theoretic limits cause LLMs to lack inherent planning capabilities due to inherent noise, errors, and inability to distinguish truth from falsehood, leading to hallucinations and reasoning degradation.

-----

Phase: [EXPLORATION]

### Source [37]: https://arxiv.org/html/2511.12869v2

Query: What information-theoretic limits cause LLMs to lack inherent planning capabilities?

Answer: Information-theoretic limits cause LLMs to lack inherent planning capabilities due to inherent noise, errors, and inability to distinguish truth from falsehood, leading to hallucinations and reasoning degradation.

-----

Phase: [EXPLORATION]

### Source [38]: https://aclanthology.org/2025.acl-long.958.pdf

Query: What information-theoretic limits cause LLMs to lack inherent planning capabilities?

Answer: Information-theoretic limits cause LLMs to lack inherent planning capabilities due to inherent noise, errors, and inability to distinguish truth from falsehood, leading to hallucinations and reasoning degradation.

-----

Phase: [EXPLORATION]

### Source [39]: https://asu.elsevierpure.com/en/publications/on-the-planning-abilities-of-large-language-models-a-critical-inv-2

Query: What information-theoretic limits cause LLMs to lack inherent planning capabilities?

Answer: Information-theoretic limits cause LLMs to lack inherent planning capabilities due to inherent noise, errors, and inability to distinguish truth from falsehood, leading to hallucinations and reasoning degradation.

-----

Phase: [EXPLORATION]

### Source [40]: https://neurips.cc/virtual/2023/poster/71377

Query: What information-theoretic limits cause LLMs to lack inherent planning capabilities?

Answer: Information-theoretic limits cause LLMs to lack inherent planning capabilities due to inherent noise, errors, and inability to distinguish truth from falsehood, leading to hallucinations and reasoning degradation.

-----

</details>

<details>
<summary>What scalability limitations emerge in ReAct loops for long-horizon tasks?</summary>

Phase: [EXPLORATION]

### Source [41]: https://www.agentengineering.io/topics/articles/react-loop-unpacked

Query: What scalability limitations emerge in ReAct loops for long-horizon tasks?

Answer: Long-horizon tasks reveal ReAct loop scalability issues due to context rot and diminishing relevance of early steps. Performance drops significantly as context window fills. Current models struggle with long-horizon reasoning. The ReAct loop appends every thought, action, and observation to the running context. On a 5-step task this is fine. On a 30-step task, you have accumulated thousands of tokens of intermediate history that the model must attend to on every new thought generation. Two things happen. First, relevant information from early in the trace gets diluted by later content. Chroma Research (2025) measured this directly across 18 frontier models: GPT-4o accuracy dropped from 98.1% to 64.1% as the context window filled — "Context Rot." Second, the model's attention drifts toward recency. Early objectives, constraints, and tool results stop influencing generation as effectively as they should. The failure modes — long-horizon drift, irreversible actions, thought-action divergence, brittle error recovery — are structural. They won't be patched by a better prompt.

-----

Phase: [EXPLORATION]

### Source [42]: https://openreview.net/pdf?id=dAn82lpLx4

Query: What scalability limitations emerge in ReAct loops for long-horizon tasks?

Answer: Models such as ‘GPT-5’, ‘o3’, and ‘o1’ demonstrate high accuracy on short-horizon tasks. In contrast, ‘GPT-4o”'s performance deteriorates rapidly even on tasks with very few steps. Model performance follows a consistent hierarchy. ‘GPT-5’ achieves the highest accuracy, followed by ‘o3’ and ‘o1’, while ‘GPT-4o’ lags significantly behind. The operational horizon of even the strongest model, ‘GPT-5’, shrinks dramatically. While it remains competent on standard tasks with more than 100 operations, its accuracy on LORE-Hard falls below reliability after only about 12 operations. This steep decline highlights a critical limitation of current state-of-the-art agents: they are not yet capable of handling long-horizon reasoning when individual steps involve complex, realistic operations. Agent performance collapses after fewer than 15 steps on more challenging benchmark variants.

-----

Phase: [EXPLORATION]

### Source [43]: https://huggingface.co/papers?q=long-horizon

Query: What scalability limitations emerge in ReAct loops for long-horizon tasks?

Answer: Long-horizon reinforcement learning (RL) for large language models faces critical scalability challenges from unbounded context growth, leading to context folding methods that compress interaction history during task execution. However, existing approaches treat summary actions as standard actions, overlooking that summaries fundamentally modify the agent's future observation space, creating a policy-dependent, non-stationary observation distribution that violates core RL assumptions. This introduces three fundamental challenges: (1) gradient dilution where summary tokens receive insufficient training signal, (2) self-conditioning where policy updates change summary distributions, creating a vicious cycle of training collapse, and (3) computational cost from processing unique contexts at each training step. Long-horizon agents face the challenge of growing context size during interaction with environment, which degrades the performance and stability. LLM-based web agents show immense promise for information seeking, yet their effectiveness on long-horizon tasks is hindered by a fundamental trade-off in context management. Prevailing ReAct-based agents suffer from context saturation as they accumulate noisy, raw histories, while methods that fixedly summarize the full history at each step risk the irreversible loss of critical details.

-----

Phase: [EXPLORATION]

### Source [44]: https://www.emergentmind.com/topics/react-loop-architecture

Query: What scalability limitations emerge in ReAct loops for long-horizon tasks?

Answer: Empirical results indicate that simply increasing step limits (e.g., “ReAct-100”) provides minimal gains; architectural design and controlled planning are central for robust performance. Despite clear advantages, ReAct loops are susceptible to new classes of failure: uninformative search results can induce non-terminating loops, and agent context management remains challenging in low-resource and privacy-sensitive enterprise settings. Mitigations such as early stopping, dynamic re-planning, and previewed context storage are active areas of refinement.

-----

</details>

<details>
<summary>How do private thinking streams in o3 models reduce hallucination rates theoretically?</summary>

Phase: [EXPLORATION]

### Source [46]: https://techcrunch.com/2025/04/18/openais-new-reasoning-ai-models-hallucinate-more

Query: How do private thinking streams in o3 models reduce hallucination rates theoretically?

Answer: “Our hypothesis is that the kind of reinforcement learning used for o-series models may amplify issues that are usually mitigated (but not fully erased) by standard post-training pipelines,” said Neil Chowdhury, a Transluce researcher and former OpenAI employee, in an email to TechCrunch.

Sarah Schwettmann, co-founder of Transluce, added that o3’s hallucination rate may make it less useful than it otherwise would be.

Kian Katanforoosh, a Stanford adjunct professor and CEO of the upskilling startup Workera, told TechCrunch that his team is already testing o3 in their coding workflows, and that they’ve found it to be a step above the competition. However, Katanforoosh says that o3 tends to hallucinate broken website links. The model will supply a link that, when clicked, doesn’t work. [...] According to OpenAI’s internal tests, o3 and o4-mini, which are so-called reasoning models, hallucinate more often than the company’s previous reasoning models — o1, o1-mini, and o3-mini — as well as OpenAI’s traditional, “non-reasoning” models, such as GPT-4o.

Perhaps more concerning, the ChatGPT maker doesn’t really know why it’s happening.

In its technical report for o3 and o4-mini, OpenAI writes that “more research is needed” to understand why hallucinations are getting worse as it scales up reasoning models. O3 and o4-mini perform better in some areas, including tasks related to coding and math. But because they “make more claims overall,” they’re often led to make “more accurate claims as well as more inaccurate/hallucinated claims,” per the report. [...] OpenAI found that o3 hallucinated in response to 33% of questions on PersonQA, the company’s in-house benchmark for measuring the accuracy of a model’s knowledge about people. That’s roughly double the hallucination rate of OpenAI’s previous reasoning models, o1 and o3-mini, which scored 16% and 14.8%, respectively. O4-mini did even worse on PersonQA — hallucinating 48% of the time.

Third-party testing by Transluce, a nonprofit AI research lab, also found evidence that o3 has a tendency to make up actions it took in the process of arriving at answers. In one example, Transluce observed o3 claiming that it ran code on a 2021 MacBook Pro “outside of ChatGPT,” then copied the numbers into its answer. While o3 has access to some tools, it can’t do that.

-----

Phase: [EXPLORATION]

### Source [48]: https://arxiv.org/html/2505.23646v1

Query: How do private thinking streams in o3 models reduce hallucination rates theoretically?

Answer: While post-training is mainly conducted on formal reasoning tasks, e.g., math reasoning, logic reasoning, and coding, whose answers are formally verifiable, it is widely believed that LRMs can generalize their reasoning abilities to non-formal tasks.
It is expected that the long CoT reasoning also helps to reduce hallucination.
For example, DeepSeek-R1 reports its improved performance on SimpleQA , a fact-seeking question answering benchmark, after post-training.
On the contrary, OpenAI observes even severer hallucination on more powerful LRMs OpenAI-o3 v.s. OpenAI-o1, .
Thus, there remains a lack of systematic understanding regarding whether and how this form of reasoning contributes to more reliable factual inference. [...] Recently evolved large reasoning models (LRMs) show powerful performance in solving complex tasks with the help of long chain-of-thought (CoT) reasoning capability.
As these LRMs are mostly developed by post-training on formal reasoning tasks, whether they generalize the reasoning capability to help reduce hallucination in fact-seeking tasks remains unclear and debated.
For instance, DeepSeek-R1 reports increased performance on SimpleQA, a fact-seeking benchmark, while OpenAI-o3 observes even severer hallucination.
This discrepancy naturally raises the following research question:
Are reasoning models more prone to hallucination?
This paper addresses the question from three perspectives.
(1) We first conduct a holistic evaluation for the hallucination in LRMs.

-----

Phase: [EXPLORATION]

### Source [49]: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1622292/full

Query: How do private thinking streams in o3 models reduce hallucination rates theoretically?

Answer: Other strategies like Self-Consistency decoding (Wang et al., 2022), ReAct prompting (Yao et al., 2022), and Instruct-tuning (Ouyang et al., 2022) have also been shown to reduce hallucination rates by influencing how the model organizes its internal generation paths. Still, these methods are heuristic in nature and do not universally prevent hallucinations across domains or tasks.

### 3.2 Model behavior and architecture-level causes [...] Recent work has attempted to reduce hallucinations using improved prompting techniques, such as chain-of-thought prompting (Wei et al., 2022), self-consistency decoding (Wang et al., 2022), retrieval-augmented generation (Lewis et al., 2020; Shuster et al., 2022), and verification-based refinement (Kadavath et al., 2022). Simultaneously, efforts at the model level focus on supervised fine-tuning (SFT), reinforcement learning from human feedback (RLHF) (Ouyang et al., 2022), contrastive decoding (Li et al., 2022), and grounded pretraining (Zhang et al., 2023). However, the interplay between prompt quality and model internals remains poorly addressing. [...] Few-shot prompting reduced hallucination rates but was dependent on high-quality demonstrations.

Instruction-based prompting worked well for structured tasks but did not fully eliminate factual inconsistencies.

Vague or misleading prompts induced high hallucination rates across all models, confirming the risk of prompt underspecification.

-----

Phase: [EXPLORATION]

### Source [50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12518350

Query: How do private thinking streams in o3 models reduce hallucination rates theoretically?

Answer: Other strategies like Self-Consistency decoding (Wang et al., 2022), ReAct prompting (Yao et al., 2022), and Instruct-tuning (Ouyang et al., 2022) have also been shown to reduce hallucination rates by influencing how the model organizes its internal generation paths. Still, these methods are heuristic in nature and do not universally prevent hallucinations across domains or tasks.

### 3.2 Model behavior and architecture-level causes [...] Recent work has attempted to reduce hallucinations using improved prompting techniques, such as chain-of-thought prompting (Wei et al., 2022), self-consistency decoding (Wang et al., 2022), retrieval-augmented generation (Lewis et al., 2020; Shuster et al., 2022), and verification-based refinement (Kadavath et al., 2022). Simultaneously, efforts at the model level focus on supervised fine-tuning (SFT), reinforcement learning from human feedback (RLHF) (Ouyang et al., 2022), contrastive decoding (Li et al., 2022), and grounded pretraining (Zhang et al., 2023). However, the interplay between prompt quality and model internals remains poorly addressing. [...] ### 6.2 Prompt-type impact on hallucination

Figure 3 compares hallucination rates across prompt strategies, demonstrating that vague prompts yield the highest hallucinations (38.3%), while Chain-of-Thought (CoT) prompts significantly reduce hallucinations (18.1%). This highlights the crucial role of prompt clarity in minimizing hallucination occurrence, underscoring CoT as the most effective approach across evaluated LLMs.

Figure 3
Image 17: Figure 3

Open in a new tab

Mean ± SD across 3 seeds × 5 prompt variants; _n_ = 100 examples/model. CoT reduces hallucinations most consistently.

### 6.3 Prompt sensitivity (PS) and model variability (MV)

The comparison of prompt sensitivity and model variability is shown in Table 5.

Table 5

-----

</details>

<details>
<summary>What open challenges remain in formalizing self-correction guarantees for agent planning?</summary>

Phase: [EXPLORATION]

### Source [51]: https://apxml.com/courses/agentic-llm-memory-architectures/chapter-4-complex-planning-tool-integration/self-correction-plan-refinement

Query: What open challenges remain in formalizing self-correction guarantees for agent planning?

Answer: Open challenges include tool execution failures, environmental changes, and balancing correction attempts with computational cost and latency. Self-correction remains unreliable due to inherent model biases. Formal methods integration is needed for robust guarantees.

-----

Phase: [EXPLORATION]

### Source [52]: https://openreview.net/forum?id=wkisIZbntD

Query: What open challenges remain in formalizing self-correction guarantees for agent planning?

Answer: Open challenges include tool execution failures, environmental changes, and balancing correction attempts with computational cost and latency. Self-correction remains unreliable due to inherent model biases. Formal methods integration is needed for robust guarantees.

-----

Phase: [EXPLORATION]

### Source [53]: https://arxiv.org/html/2606.05976v1

Query: What open challenges remain in formalizing self-correction guarantees for agent planning?

Answer: Open challenges include tool execution failures, environmental changes, and balancing correction attempts with computational cost and latency. Self-correction remains unreliable due to inherent model biases. Formal methods integration is needed for robust guarantees.

-----

Phase: [EXPLORATION]

### Source [54]: https://openreview.net/forum?id=vx0luAhOGl

Query: What open challenges remain in formalizing self-correction guarantees for agent planning?

Answer: Open challenges include tool execution failures, environmental changes, and balancing correction attempts with computational cost and latency. Self-correction remains unreliable due to inherent model biases. Formal methods integration is needed for robust guarantees.

-----

Phase: [EXPLORATION]

### Source [55]: https://www.turingpost.com/p/aia11

Query: What open challenges remain in formalizing self-correction guarantees for agent planning?

Answer: Open challenges include tool execution failures, environmental changes, and balancing correction attempts with computational cost and latency. Self-correction remains unreliable due to inherent model biases. Formal methods integration is needed for robust guarantees.

-----

</details>

<details>
<summary>How did symbolic AI planning influence modern LLM agents like ReAct?</summary>

Phase: [EXPLORATION]

### Source [57]: https://arxiv.org/html/2407.08516v5

Query: How did symbolic AI planning influence modern LLM agents like ReAct?

Answer: Neuro-symbolic AI combines the strengths of neural networks and symbolic reasoning, producing decision-making processes that are both explicit and interpretable. In autonomous agents enhanced by LLMs, the latest advancements in deep neural networks are harnessed, while task decomposition and planning are guided by symbolic AI principles — breaking complex tasks into discrete, logical steps that can be systematically analyzed and reasoned through. This fusion of symbolic structures and deep neural networks creates a powerful synergy, significantly boosting the capabilities of these agents. The emergence of LLM-empowered Autonomous Agents (LAAs) signifies a pivotal juncture in the development of AI, embodying the convergence of symbolic and connectionist paradigms.

-----

Phase: [EXPLORATION]

### Source [59]: https://arxiv.org/html/2601.01743v1

Query: How did symbolic AI planning influence modern LLM agents like ReAct?

Answer: An important recent shift is that capability gains increasingly come from system design rather than only from bigger backbones. Modern deployments treat the LLM as a planner/controller inside a budgeted loop: the agent is constrained by explicit limits on time, tokens, tool calls, and permissible side effects, and it dynamically allocates “thinking” (deliberation) only when the task is hard or risky. This connects directly to test-time compute scaling: self-consistency, reranking, backtracking, and tree-style search can improve reliability without retraining, but must be used selectively to avoid runaway cost and latency (Wang et al., 2022; Yao et al., 2023a). Relatedly, agents increasingly rely on structured action spaces (typed tool schemas and structured outputs) as the primary.

-----

Phase: [EXPLORATION]

### Source [60]: https://www.ibm.com/think/topics/react-agent

Query: How did symbolic AI planning influence modern LLM agents like ReAct?

Answer: First introduced by Yao and others in the 2023 paper, “ReACT: Synergizing Reasoning and Acting in Language Models,” ReAct can be understood most generally as a machine learning (ML) paradigm to integrate the reasoning and action-taking capabilities of LLMs. More specifically, ReAct is a conceptual framework for building AI agents that can interact with their environment in a structured but adaptable way, by using an LLM as the agent’s “brain” to coordinate anything from simple retrieval augmented generation (RAG) to intricate multiagent workflows. The ReAct framework is inspired by the way humans can intuitively use natural language—often through our own inner monologue—in the step-by-step planning and execution of complex tasks. Rather than implementing rule-based or otherwise predefined workflows, ReAct agents rely on their LLM’s reasoning capabilities to dynamically adjust their approach based on new information or the results of previous steps.

-----

</details>

<details>
<summary>What control theory lessons apply to LLM agent self-correction loops?</summary>

Phase: [EXPLORATION]

### Source [61]: https://arxiv.org/html/2605.17305v1

Query: What control theory lessons apply to LLM agent self-correction loops?

Answer: Cybernetics provides foundational principles for self-regulating systems. Classical control theory concepts including error signals, proportional-integral-derivative (PID) controllers, stability analysis, and convergence criteria have been applied to robotics, autonomous systems, and recently to neural network training dynamics. The SMC community has long studied human-in-the-loop control and adaptive systems where feedback drives system improvement. CyberCorrect formalizes LLM self-correction as a closed-loop control system. The key insight is that self-correction is fundamentally a feedback control problem: the LLM generator is the plant, errors in its output are the disturbance, the correction prompt is the control input, and the correction process should converge to a stable (correct) output. By making this mapping explicit, we import principled solutions from control theory—typed error signals, adaptive control inputs, stability-based convergence criteria, and bounded overshoot—into the LLM self-correction domain. Table mapping: Plant G = LLM generator; Setpoint = Error-free output (implicit); Output yt = Generated answer at iteration t; Sensor E = Error Detector (tri-modal); Error signal et = Detected error (type + severity + location); Controller C = Correction Controller (type-directed); Control input ut = Targeted correction prompt; Convergence = |st - st-1| < ε; Overshoot = Correction degrades correct content; Oscillation = Output alternates between versions.

-----

Phase: [EXPLORATION]

### Source [64]: https://www.nature.com/articles/s44387-025-00057-z

Query: What control theory lessons apply to LLM agent self-correction loops?

Answer: At the core of MCP-SIM lies a Plan → Act → Reflect → Revise control loop that enables self-correcting and interpretable simulation synthesis. Upon receiving a vague or incomplete user prompt, the Input Clarifier Agent infers essential simulation details like domain geometry, governing PDE (e.g., Navier–Stokes), and boundary conditions using domain knowledge and language understanding. These inferred attributes are stored in global memory as the canonical problem specification. Corrections are communicated to other agents as structured hints for subsequent revision. If the issue stems from high-level ambiguity in the user prompt, the Input Rewriter Agent semantically revises the instruction, and the control loop restarts from clarification. All agents are orchestrated by a memory-centric controller that stores clarifications, parsed data, code versions, execution logs, and applied fixes, thereby enabling reproducibility and the iterative Plan → Act → Reflect → Revise loop underpinning MCP-SIM’s self-correcting behavior.

-----

Phase: [EXPLORATION]

### Source [65]: https://pub.towardsai.net/autonomy-loops-reflection-evaluation-correction-execution-2e2fb0398bf1

Query: What control theory lessons apply to LLM agent self-correction loops?

Answer: Evaluation: Objective assessment of performance against success criteria using metrics, validators, or LLM-based judgment. Correction: Based on evaluation results, the agent modifies its approach, parameters, or strategy. Execution: The agent runs the corrected approach and the cycle repeats until success criteria are met or max iterations reached. Purpose: Make agents self-aware, Improve decisions over time, Reduce hallucinations, Enable long-running autonomy, Produce verified and corrected output. Core Architecture: Reflection → Evaluation → Correction → Execution.

-----

</details>

<details>
<summary>How are multimodal models expanding planning in research-style agents?</summary>

Phase: [EXPLORATION]

### Source [66]: https://arxiv.org/html/2603.16777v1

Query: How are multimodal models expanding planning in research-style agents?

Answer: To develop multimodal agentic models capable of looking ahead, two major directions have been explored. Model-free reinforcement learning (RL) trains agents through step-level action correctness and designed rewards for subgoals or sparse final outcomes. Model-based planning equips agents with a world model that simulates future action sequences and evolving environment states, enabling them to reason about possible outcomes before acting. Yet both approaches face fundamental obstacles: constructing world models over visually rich and interactive environments is notoriously difficult, and defining reasoning-oriented rewards that generalize across diverse and open-ended tasks remains an open challenge. The ability to use external tools is a defining aspect of intelligent multimodal agents, allowing them to perform complex, visually grounded tasks beyond direct perception and reasoning. One line of research enhances this capability through large-scale multimodal instruction tuning, where models learn tool selection and composition from synthetic or curated trajectories. Another line builds end-to-end architectures that couple vision–language models with real executable tools or interactive environments, enabling stepwise control and adaptive reasoning. These methods substantially improve tool invocation and multimodal integration but primarily emphasize execution reliability or reactive coordination. They emphasize precise action execution based on instructions over trajectory-level planning, whereas our work directly trains large multimodal models to acquire anticipatory planning through RL.

-----

Phase: [EXPLORATION]

### Source [67]: https://www.ijcai.org/proceedings/2024/0015.pdf

Query: How are multimodal models expanding planning in research-style agents?

Answer: Our evaluation of recent foundation models highlights the superior performance of text-based models over their visual or multimodal counterparts in tasks related to embodied planning. Moreover, our newly proposed metrics, LC and RDI, offer valuable insights into agents’ action generation and cognitive planning capabilities. These insights serve as crucial guidance for future research in multimodal embodied agent planning. We envision MuEP as a pivotal benchmark, contributing to the advancement of embodied agents in higher-level reasoning and planning abilities. In the future, we plan to expand the benchmark in terms of scale, diversity, and complexity. Additionally, we aim to investigate the disparity between textual and visual modalities in embodied planning tasks. Emerging trends in AI research show the extension of foundation models from basic language tasks to embodied decision-making. Recent research utilizes LLMs for grounding in embodied planning tasks within interactive environments. Some approaches like React and Reflexion integrate chain-of-thought into embodied agents, enabling them to formulate autonomous problem-solving procedures. Many researchers also propose to refine agent capabilities of reasoning and decision-making in embodied environments through fine-tuning with pre-collected data. Foundation models with the great emergent abilities have demonstrated significant performance improvements when adopted for downstream tasks, including fluent interaction, sophisticated literary works creation, image captioning, and code generation. These advancements hold great promise for enhancing the reasoning and planning abilities of advanced embodied agents. Motivated by this, numerous recent studies have utilized foundation models, such as large language models (LLMs) and large multimodal models (LMMs), across a range of tasks as embodied agents, including environmental grounding.

-----

Phase: [EXPLORATION]

### Source [69]: https://cset.georgetown.edu/article/multimodality-tool-use-and-autonomous-agents

Query: How are multimodal models expanding planning in research-style agents?

Answer: In this explainer, we described how LLMs and related systems are already much more than conversationalists, and can be used to generate executable code, analyze images, control robots, and more. We also covered the rapidly developing research into AI agents that plan and execute actions on their own. These research areas, many of which are still in development but which are rapidly coming into production, raise new questions of governance that conversational LLMs do not. While the goal of this paper is not to create an exhaustive list of such issues, we will list a few for illustrative purposes: higher overall failure rates, especially if the LLM cannot recover from failure. Researchers are working to improve on this, including by prompting LLMs to write out their reasoning for choosing an action, critique their own plans, and delegate actions to other (perhaps specialized) LLM agents. These kinds of prompts are often built into the same scaffolding software that allows the LLMs to browse the web and take other actions. Breaking a goal down into sub-steps is a well-established area of computer science, known as planning. But pre-LLM approaches to planning typically require either a mathematical specification of the task, or reams of data showing how it can be accomplished. The promise of LLM agents lies in the hope that LLMs can be used to select and carry out actions in environments that are too complex or open-ended to represent formally, without needing large amounts of task-specific data to train a dedicated system “from scratch.” If LLMs could be used to operate autonomously in those settings—in other words, in most real-world environments—they would become much more valuable.

-----

</details>

<details>
<summary>What applications do planning agents have in automated legal reasoning?</summary>

Phase: [EXPLORATION]

### Source [73]: https://www.salesforce.com/ap/agentforce/what-is-agentic-ai/agentic-reasoning

Query: What applications do planning agents have in automated legal reasoning?

Answer: Planning: The system identifies a complex objective and breaks it into manageable sub-tasks. This iterative planning ensures the agent has a roadmap before it begins execution. Tool Use: An agent is not limited to its internal knowledge. It can identify and call external APIs, query databases, or use specialised software to find real-time information. Reflection: This serves as an “inner monologue”. The agent evaluates its own draft output against the original goal, performing reflection and refinement to catch errors before the user ever sees them.

-----

Phase: [EXPLORATION]

### Source [74]: https://www.ibm.com/think/topics/ai-agent-planning

Query: What applications do planning agents have in automated legal reasoning?

Answer: Planning in multiagent systems can be centralized, where a single entity or controller—likely an LLM agent—generates the plan for the entire system. Each agent receives instructions or plans from this central authority. It can also be decentralized, where agents generate their own plans but work collaboratively to help ensure that they align with each other and contribute to global objectives, often requiring communication and negotiation. This collaborative decision-making process enhances efficiency, reduces biases in task execution, helps to avoid hallucinations through cross-validation and consensus-building and encourages the agents to work toward a common goal.

-----

Phase: [EXPLORATION]

### Source [75]: https://legal.thomsonreuters.com/blog/how-agentic-ai-systems-think-learn-and-collaborate-with-legal-professionals

Query: What applications do planning agents have in automated legal reasoning?

Answer: Agentic AI systems advance beyond traditional legal AI by using a controller-coordinator architecture to manage specialized sub-agents, enabling dynamic, multi-step planning for complex legal tasks like case analysis and litigation strategy. Training these systems requires proprietary datasets that codify the nuanced steps of professional legal reasoning, while sophisticated evaluation methods test for true comprehension over simple pattern matching. Building trust requires interactive, human-centered workflows that help professionals navigate AI's uneven capabilities and acknowledge its limitations in empathy, ensuring the human-in-the-loop remains central to legal practice.

-----

</details>

<details>
<summary>How does CoT entropy constrain self-correction in agent planning loops?</summary>

Phase: [EXPLORATION]

### Source [77]: https://arxiv.org/html/2510.00568v1

Query: How does CoT entropy constrain self-correction in agent planning loops?

Answer: This issue was particularly acute in our framework due to the long and complex Chain-of-Thought (CoT) reasoning paths. We observed that after an initial learning phase, the PPO policy would abruptly degrade, characterized by a simultaneous and rapid drop in both the reward signal and the policy’s entropy. This collapse rendered the model unable to perform the task, as it began generating repetitive or nonsensical outputs. In contrast, GRPO demonstrated significantly greater training stability, successfully navigating the long CoT trajectories without collapsing and achieving steady performance gains. This inherent robustness makes GRPO a far more suitable and reliable algorithm for our complex reasoning task, explaining its superior final performance.

-----

Phase: [EXPLORATION]

### Source [78]: https://arxiv.org/html/2602.04234v6

Query: How does CoT entropy constrain self-correction in agent planning loops?

Answer: Mediation analysis further reveals that round-1 inter-agent entropy dispersion transmits 30–33% of its causal effect on correctness through round-2 entropy, causally supporting the first-round dominance finding: early misalignment compounds into the subsequent round rather than self-correcting. Base-model entropy exerts its causal effect primarily through direct pathways rather than through sample-level mediators, indicating that base-model uncertainty directly shapes the multi-agent output distribution. Together, these confirm that entropy is a causal driver of MAS performance, operating through hierarchical, multi-round mechanisms. Both families show performance dropping sharply when entropy exceeds 100. Despite this shared trend, entropy scales differ: LLaMA operates in low-entropy ranges (0-100) but achieves lower accuracy, while Qwen uses higher entropy (100-1,000) yet performs better. This reflects divergent reasoning styles, as Qwen verifies and refines its answers before finalizing, generating self-correcting trajectories that suppress error propagation in MAS despite higher entropy, whereas LLaMA tends to reuse others’ answers without verification, leading to uncontrolled error propagation. We treat entropy primarily as a predictive feature for MAS correctness.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="the-react-loop-unpacked-reasoning-acting-in-practice-agenten.md">
<details>
<summary>The ReAct Loop Unpacked: Reasoning + Acting in Practice | AgentEngineering</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.agentengineering.io/topics/articles/react-loop-unpacked>

# The ReAct Loop Unpacked: Reasoning + Acting in Practice | AgentEngineering

If you've built agents with [tool use](https://www.agentengineering.io/topics/articles/tool-use-patterns) or worked through [multi-agent orchestration](https://www.agentengineering.io/topics/articles/multi-agent-orchestration), you've already used ReAct — almost certainly without calling it that. Every agent framework's default loop, every "I need to search for X, then check Y" trace you've seen in a run log, every structured `Thought → Action → Observation` block in a prompt template: that's ReAct.

The glossary definition — "interleave reasoning and acting" — is accurate but useless for production work. What you need is the execution-level model: exactly how the loop runs, precisely why it beats chain-of-thought, and specifically where it hits walls. Then you can make an informed choice about when to reach past it.

## The Execution Model

[ReAct (Yao et al., ICLR 2023)](https://arxiv.org/abs/2210.03629) defines an agent loop with three token types interleaved in a single prompt context:

- **Thought** — the model's internal monologue. Decomposes the goal, tracks progress, plans the next action.
- **Action** — a structured call to a tool from a predefined set (e.g., `Search[query]`, `Lookup[keyword]`, `Finish[answer]`).
- **Observation** — the tool's returned output, appended to the context verbatim.

The loop continues until the agent emits a terminal action (`Finish`) or hits a budget constraint. Here is a real trace from the HotpotQA experiments in the original paper:

```
Question: Aside from the Apple Remote, what other devices can control
the program Apple Remote was originally designed to interact with?

Thought 1: I need to search Apple Remote and find the program it was
originally designed to interact with.
Action 1: Search[Apple Remote]
Observation 1: The Apple Remote is a remote control device originally
designed to interact with the Front Row media center program...

Thought 2: The program is Front Row. I need to search Front Row and
find what other devices can control it.
Action 2: Search[Front Row (software)]
Observation 2: Front Row is controlled by the Apple Remote or the
keyboard function keys.

Thought 3: Front Row can be controlled by the Apple Remote or keyboard
function keys. So the answer is keyboard function keys.
Action 3: Finish[keyboard function keys]
```

Notice what the Thought steps are doing. They are not decorative. `Thought 1` decomposes a two-hop question into a concrete first retrieval target. `Thought 2` synthesizes what was just learned and formulates the second sub-query. `Thought 3` draws the conclusion from both observations. This is the "grounding" mechanism: each thought is constrained by what the previous observations actually said, not by what the model believes from pretraining.

### Why This Works

The mechanism of improvement over pure Chain-of-Thought (CoT) is precise. CoT generates reasoning traces from parametric knowledge alone — knowledge baked into model weights during training. That knowledge can be wrong, outdated, or hallucinated. On HotpotQA, CoT-only agents failed due to hallucination in 56% of cases. ReAct reduced that to near-zero by inserting external, verified data as observations between reasoning steps.

The mechanism of improvement over Act-only (no reasoning traces) is equally precise. Without thoughts, the agent lacks a mechanism to synthesize information across multiple observations. It cannot explain to itself why a particular search failed and adjust. A pure action sequence is a reflex; ReAct is a deliberate loop.

Decision-making tasks make this concrete. In the ALFWorld household simulation benchmark, ReAct needed to find a mug, locate a lamp, and use the lamp to examine the mug. The agent searched two cabinets before finding the mug, then navigated to a desk to find the lamp:

```
Thought 1: I need to find a mug. I'll check cabinet 1.
Action 1: go to cabinet 1
Observation 1: On cabinet 1, you see a plate and a spoon.

Thought 2: No mug here. I will try cabinet 2.
Action 2: go to cabinet 2
Observation 2: On cabinet 2, you see a mug 1.

Action 3: take mug 1 from cabinet 2

Thought 4: Now I have the mug. I need to find a lamp and turn it on.
Action 4: go to desk 1
Observation 4: On desk 1, you see a desk lamp 1.

Action 5: use desk lamp 1
```

`Thought 2` is the critical step: the agent registers failure, updates its world model ("no mug in cabinet 1"), and plans a recovery. Act-only agents in this benchmark had no such mechanism — they achieved 45% success rate. ReAct reached 71%, and it did so with just 2-shot prompting.

### Empirical Baselines

The original paper evaluated on PaLM-540B across four benchmarks:

| Benchmark | ReAct | Best Baseline | Gap |
| --- | --- | --- | --- |
| HotpotQA (multi-hop QA) | 27.4 EM | 29.4 (CoT self-consistency) | −2.0 |
| FEVER (fact verification) | 60.9% | 56.3% (CoT) | +4.6 |
| ALFWorld (household sim) | 71% SR | 45% (Act-only) | +26 |
| WebShop (e-commerce nav) | 40% SR | 30.1% (Act-only) | +9.9 |

The HotpotQA deficit vs. CoT self-consistency is worth noting: for pure knowledge tasks with stable training-time facts, CoT with sampling can outperform ReAct. The advantage of ReAct is clearest where retrieval is mandatory (FEVER) and where environment interaction requires sequential adaptation (ALFWorld, WebShop).

## Where ReAct Breaks

ReAct is a solid default. It is not a reliable foundation for every production deployment. The failure modes below are structural — they arise from the loop's design, not from model quality or prompt engineering.

### 1\. Long-Horizon Drift

The ReAct loop appends every thought, action, and observation to the running context. On a 5-step task this is fine. On a 30-step task, you have accumulated thousands of tokens of intermediate history that the model must attend to on every new thought generation.

Two things happen. First, relevant information from early in the trace gets diluted by later content. Chroma Research (2025) measured this directly across 18 frontier models: GPT-4o accuracy dropped from 98.1% to 64.1% as the context window filled — "Context Rot." Second, the model's attention drifts toward recency. Early objectives, constraints, and tool results stop influencing generation as effectively as they should.

A compounding error rate of even 1% per step reaches ~60% success probability at step 50, ~36% at step 100. CORAL (2025) terms this “cognitive overload” — the agent’s working memory becomes cluttered with irrelevant intermediate reasoning, and planning coherence collapses. [CMU’s TheAgentCompany benchmark (2025)](https://arxiv.org/abs/2412.14161) found state-of-the-art agents failing ~70% of multi-step office simulation tasks, largely due to this drift.

### 2\. Irreversible Actions

The ReAct loop has no native concept of action reversibility. When the next action in the loop is `send_email`, `delete_file`, or `execute_payment`, the model generates it the same way it generates `Search[query]`. The loop does not pause to assess downstream consequences. There is no built-in rollback.

This is not hypothetical. Production incident reports include agents that deleted production databases, posted sensitive data to public forums, and executed financial transactions based on misunderstood commands. In each case, the action was irreversible and the exposure window was measured in minutes to hours.

The standard mitigation — gating high-stakes actions behind human approval — breaks the autonomous loop. That's a deliberate choice, but it must be made explicitly at design time, not discovered after an incident.

### 3\. Thought-Action Divergence

The Thought token and the Action token are generated sequentially by the same model in the same pass. Ideally, the thought causally produces the action. In practice, fine-tuning on ReAct-formatted data can create a structural bias: the model generates the action it "expects" to come next in the pattern, regardless of what the thought actually concluded.

The observable symptom is a model that reasons correctly — "I should not delete this file" — and then generates `delete_file` as the next action. The format pulls the generation. Research on prompt injection (2025) found that once a malicious action is injected into an agent's thought process, the agent executes it 95% of the time without re-evaluating — it has learned to follow the format.

### 4\. Error Recovery Limits

When a tool call fails — wrong parameters, rate limit, network error — the standard ReAct loop handles it via the Observation: the error message gets appended and the agent generates a new Thought. For transient failures this often works. For structural failures (hallucinated tool names, non-existent API endpoints), it does not.

A 2026 analysis found that 90.8% of retries in standard ReAct agents were spent on errors that could never succeed. The loop kept iterating until the token budget was exhausted. ReAct's reactive correction mechanism handles the cases where correction is possible; it has no way to classify the cases where it is not.

## Alternatives Positioned by What They Fix

These are not replacements for ReAct. They are architectural responses to specific failure modes. You should understand which failure mode you are actually hitting before reaching for an alternative.

### Reflexion: Self-Critique Across Episodes

[Reflexion (Shinn et al., 2023)](https://arxiv.org/abs/2303.11366) extends ReAct by adding a meta-loop around the intra-episode loop. When a full task attempt fails, a Self-Reflection model analyzes the failed trajectory and generates a verbal summary of what went wrong. This summary is stored in an episodic memory buffer and prepended to the next attempt.

The architecture has three components:

- **Actor** — a standard ReAct agent
- **Evaluator** — a success/failure signal (heuristic, unit tests, or LLM judge)
- **Self-Reflection model** — an LLM that generates natural-language post-mortems

| Feature | ReAct | Reflexion |
| --- | --- | --- |
| Loop type | Intra-episode: corrects the next step | Inter-episode: corrects the next _attempt_ |
| Memory scope | Current trace only | Accumulated reflections across failures |
| Correction granularity | Local (last observation → next action) | Global (full trajectory → strategy revision) |

**What it fixes:** Accuracy-critical tasks where one failed attempt provides enough signal for a meaningful strategy change. On HumanEval (coding), Reflexion with GPT-4 achieved 91% pass@1 vs. 80% for the base model. On ALFWorld it improved 22% over the ReAct baseline.

**What it does not fix:** Context rot within a single episode. It also requires an accurate evaluator — if the evaluator produces false signals, the reflections are built on wrong premises. And self-critique from a weak model can actively hurt a stronger actor.

**Cost profile:** Token usage compounds with each failed attempt. A three-attempt Reflexion run can cost 3–5x a single ReAct run. For coding tasks the unit-test evaluator is free; for open-ended tasks the LLM-judge evaluator adds cost.

### Tree-of-Thought: Search Over Reasoning Paths

[ToT (Yao et al., 2023)](https://arxiv.org/abs/2305.10601) replaces the linear Thought → Action chain with a search tree. At each step the model generates multiple candidate thoughts (branches), a State Evaluator rates each branch's promise, and a search algorithm (BFS or DFS) selects which branches to expand.

The State Evaluator is the key structural addition. Instead of greedily following the most recently generated thought, ToT can prune "Impossible" branches early and backtrack from dead ends — something ReAct's linear loop cannot do.

**When it outperforms ReAct:** Tasks with combinatorial structure where greedy choices commit to wrong paths. On Game of 24 (use four numbers to reach 24), ReAct-style CoT achieves 4% success; ToT achieves 74%. On 5×5 mini crosswords, CoT approaches 0% on full solutions; ToT solves ~60% of letters. For knowledge-retrieval tasks, ToT's search overhead outweighs any benefit.

**Cost profile:** Multiple LLM calls per reasoning step. A ToT run is typically 5–10x more expensive in tokens and latency than an equivalent ReAct run. [Graph-of-Thought (Besta et al., 2023)](https://arxiv.org/abs/2308.09687) extends the tree into a directed acyclic graph, allowing merging of branches — 62% better sorting quality than ToT at 31% lower cost through node reuse.

The [LATS hybrid (Zhou et al., 2023)](https://arxiv.org/abs/2310.04406) combines ToT-style MCTS with ReAct's tool use, using tool call results as node evaluation signals. For tasks that require both search over reasoning paths and real environment interaction, LATS is the current state of the art, at the cost of significant implementation complexity.

### Plan-and-Execute: Decouple Planning from Action

Plan-and-Execute architectures solve the token bloat problem structurally by separating the planning LLM call from the execution calls. A Planner generates a complete task graph upfront. Workers (often smaller, cheaper models) execute each step against only the sub-task context — not the full history.

[ReWOO (Xu et al., 2023)](https://arxiv.org/abs/2305.18323) makes this explicit: the Planner generates a blueprint with placeholders (`#E1`, `#E2`) for future tool outputs. The Worker executes all tool calls. The Solver receives the completed plan to generate the final answer. The LLM reasons exactly once; it does not re-attend to the full history on every step.

[LLMCompiler (Kim et al., 2024)](https://arxiv.org/abs/2312.04511) extends this to parallel execution: it generates a DAG of tasks, identifies independent nodes, and dispatches them to an executor simultaneously. On movie recommendation tasks requiring multiple independent database lookups, LLMCompiler showed 3.74x speedup and 6.73x cost reduction versus ReAct.

| Metric | ReAct | ReWOO | LLMCompiler |
| --- | --- | --- | --- |
| Token usage | 1× (baseline) | ~5× reduction | Up to 6.7× reduction |
| Latency | Sequential | Parallelizable | Up to 3.7× speedup |
| Accuracy (HotpotQA) | Baseline | +4.4% | Up to +9% |

**What it fixes:** Long-horizon token accumulation and sequential bottlenecks. Zup's internal coding agent moved from ReAct to Plan-and-Execute and increased accuracy on multi-file edits from 40% to 75%, because isolating file context in sub-tasks eliminated cross-contamination from accumulated observations.

**What it does not fix:** Tasks where the next step genuinely depends on what the previous step returned. A plan generated without observations can be structurally wrong. Reflexion's inter-episode correction is better suited for iterative refinement; Plan-and-Execute is better suited for stable, repeatable pipelines.

## Choosing in Practice

The decision is not about which pattern is "better" — it's about which failure mode you're actually encountering.

| Your situation | Architecture |
| --- | --- |
| Short task (< 5 steps), dynamic next steps, reversible actions | ReAct — start here |
| Task keeps drifting after step 10, context fills up | Plan-and-Execute (ReWOO / LLMCompiler) |
| Multi-attempt iterative task, good success signal available | Reflexion |
| Combinatorial search, strategy requires lookahead + backtracking | Tree-of-Thought (or LATS with tools) |
| High-stakes irreversible actions involved | Any architecture + gated HITL approval |

A few practical constraints that the decision matrix above doesn't capture:

**Latency.** ReAct returns a first response immediately. ToT and Reflexion require multiple LLM calls before producing an answer. If users are waiting, that matters.

**Evaluator availability.** Reflexion requires a reliable success signal. Unit tests and exact-match graders are good evaluators. "Did the user seem satisfied" is not.

**Horizon is observable at runtime.** The most common production pattern in 2025 is agent-gated workflow: use deterministic code for 90% of the logic, invoke a ReAct agent only for the ambiguous sub-tasks where the path is genuinely unknown. This is more reliable than any pure-agent architecture because the deterministic wrapper constrains the search space.

**Reasoning models change the equation.** Models like o1 and o3 internalize the CoT loop. They function as implicit Plan-and-Execute systems — the reasoning trace is hidden, but the model is effectively planning before acting. For tasks where these models are available and cost-acceptable, they shift the tradeoff: you get long-horizon stability without implementing a separate planner.

## What to Take Away

ReAct's core contribution is the mechanism that grounds reasoning in environmental feedback. Every time you see a thought that references what an observation actually said, that's the mechanism working. It is the single most important pattern in production agents precisely because it solves hallucination-in-reasoning without requiring retrieval infrastructure or multi-attempt loops.

The failure modes — long-horizon drift, irreversible actions, thought-action divergence, brittle error recovery — are structural. They won't be patched by a better prompt. Recognizing them early determines whether you reach for Reflexion, Plan-and-Execute, or ToT because the alternative fits your specific constraint, not because it's newer or has a better benchmark number.

The [next piece](https://www.agentengineering.io/topics/articles/prompt-engineering-for-agent-roles) covers the craft layer that sits on top of any of these patterns: system prompts that make agent behavior consistent across tasks and across iterations.

</details>

</research_source>

