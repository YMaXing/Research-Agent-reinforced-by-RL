<digest_meta>
  <article_title>State_of_LLM_Reasoning</article_title>
  <total_sources>15</total_sources>
  <total_artefacts>53</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>72</n_orphan_anchors>
  <n_content_sections>19</n_content_sections>
  <external_evidence_policy>forbidden</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
</artefact_registry>

<sources>
<s slug="1-scaling-by-thinking-in-continuous-space" type="exploitation">A depth-recurrent transformer architecture enables test-time compute scaling by iterating a shared recurrent block in latent space rather than emitting additional tokens. The model partitions decoder-only transformer layers into a prelude block P that embeds inputs, a core recurrent block R that updates hidden states s_i via R(e, s_{i-1}), and a coda block C that produces next-token probabilities; the recurrence is initialized from N(0, σ²I) and receives the embedded input at every step to enforce path independence. Training samples recurrence count r from a log-normal Poisson distribution (mean r-bar = 32) and performs truncated back-propagation through the final k = 8 iterations.

The 3.5 B parameter model (shape (2,4,2), h = 5280) was pretrained for 800 B tokens on Frontier (4096 AMD MI250X GPUs) using a code- and math-heavy mixture tokenized with a 65 536-token BPE vocabulary; released artifacts are huggingface.co/tomg-group-umd/huginn-0125 and github.com/seal-rg/recurrent-pretraining. At inference the same weights support variable depth, zero-shot per-token early exits (KL threshold 5×10^{-4}), KV-cache sharing (budget of 4–16 steps), continuous CoT via state warm-starting, and self-speculative decoding without auxiliary heads.

On lm-eval-harness zero-shot tasks the model matches or exceeds OLMo-7B and Pythia-6.9 B while trailing later OLMo-2 variants; GSM8K flexible-match accuracy rises from ~10 % at r = 1 to 47.23 % (EMA checkpoint) at r = 64, and MATH and HumanEval likewise improve monotonically with recurrence. Saturation occurs earlier on OpenBookQA than on GSM8K or ARC-Challenge; performance gains are largest on reasoning-heavy tasks and when additional few-shot context is supplied. The non-recurrent baseline trained identically underperforms on ARC-Challenge and GSM8K.

The study includes Table 1 (lm-eval-harness results), Table 2 (math benchmarks), Table 4 (recurrent vs. non-recurrent comparison), Table 5 (open/closed QA), and multiple PCA trajectory visualizations (Figures 11–25) that document emergent orbits, sliders, and context-dependent convergence. Limitations include a single un-cooled training run, 800 B tokens on public data only, and absence of post-training or multi-stage recurrence ablations.</s>
<s slug="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS" type="exploitation">The paper examines how scaling inference-time compute in reasoning models improves adversarial robustness without adversarial training or attack-specific interventions. Experiments use OpenAI o1-preview, o1-mini, and o1-v on policy compliance tasks, measuring attack success probability against attacker resources (e.g., prompt tokens, optimization steps, queries) and defender compute levels.

Key findings show that for unambiguous tasks, attack success rates decline toward zero with more reasoning compute. This holds across static and adaptive attacks while also boosting clean performance. The work distinguishes unambiguous tasks (exact ground-truth checks) from ambiguous ones (policy interpretation with loopholes).

Concrete techniques and attacks include:
- Many-shot jailbreaking (Anil et al. 2024) on math problems (2-digit addition/multiplication, MATH dataset) with goals of forcing outputs like 42, x+1, or 7x.
- Soft-token attacks (norm-constrained and unconstrained) optimized via gradient descent on embeddings.
- Language Model Program (LMP) attacker running iterative black-box loops (up to 25 attempts) with feedback.
- Prompt injection on AdvSimpleQA (adapted SimpleQA with injected instructions on websites).
- StrongREJECT benchmark (35 jailbreaks + misuse prompts) evaluated via goodness@0.1.
- Human red-teaming and multimodal attacks on ImageNet-A and Attack-Bard (ℓ∞, ϵ=16/255).
- Novel attacks: "think-less" (reducing compute via prompts) and hypothesized "nerd-sniping" (inducing unproductive long reasoning loops).

Includes a 16-line table summarizing tasks, goals, and methods, plus a 7-line table on red-teaming results across five compute levels. Results indicate monotonic robustness gains on StrongREJECT and vision tasks, with success rates approaching zero above certain compute thresholds on AdvSimpleQA and many-shot math attacks.

Limitations include no coverage of policy specification, context parsing, or safety knowledge (only application to OOD instances); ineffectiveness on ambiguous tasks; vulnerability to think-less/nerd-sniping; and testing over limited compute ranges and attack types.</s>
<s slug="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback" type="exploitation">TPO (Test-Time Preference Optimization) aligns LLM outputs to human preferences at inference without parameter updates. It converts numerical reward-model scores into textual critiques ("textual loss") and refinement instructions ("textual gradients"), then iteratively revises responses, mirroring gradient descent on contextual variables while keeping model weights fixed.

The framework implements four components via prompts: variable definition (candidate responses), loss calculation with \(P_{\rm loss}\) (comparing chosen vs. rejected responses), gradient computation with \(P_{\rm grad}\), and variable optimization with \(P_{\rm update}\). It builds directly on the TextGrad framework (Yuksekgonul et al., 2024), customizes only the loss prompt for preference data, and runs inference via vLLM (temperature 0.7, top-p 0.95). Reward model is FsfairX-LLaMA3-RM-v0.1 for all models; an additional Llama-3.1-Tulu-3-8B-RM is tested on the SFT policy.

Policy models evaluated are Llama-3.1-70B-SFT (unaligned), Llama-3.1-70B-Instruct, Llama-3.1-70B-DPO (on-policy DPO baseline trained on UltraFeedback), and Mistral-Small-Instruct-2409 (22B). Benchmarks comprise AlpacaEval 2 (LC/WR), Arena-Hard (WR vs. GPT-4-0314), HH-RLHF (500 samples, RM score), BeaverTails-Evaluation, XSTest (WildGuard refusal accuracy), and MATH-500 (zero-shot CoT pass@1).

After two TPO iterations (N=5 samples), Llama-3.1-70B-SFT exceeds both Llama-3.1-70B-DPO and Llama-3.1-70B-Instruct on nearly all metrics, reaching 70.5 WR on Arena-Hard. Mistral-Small-Instruct-2409 with TPO attains 53.4 LC on AlpacaEval 2. Reward-model scores rise monotonically with depth; width scaling (N=5→20) accelerates convergence but depth compensates for smaller widths. TPO-D2-N5 outperforms BoN sampling at 30–60 candidates (GPT-4 win rates 65.2 % and 57.5 %). Compute comparison: training Llama-3.1-70B-DPO on 64k examples costs ~72 840 PFLOPs; one TPO query costs ~9.3 PFLOPs (<0.01 %).

The source includes test-time training curves (Figures 3, 5, 8–10), benchmark tables (Tables 1–2), inference-stability plots (Figure 4), and five detailed case studies with full query/chosen/rejected/textual-loss/gradient/optimized-response traces (Appendix D). It also supplies the exact \(P_{\rm loss}\) prompt used for TPO versus the revision baseline.

Limitations noted are dependence on strong instruction-following (Llama-3.1-8B-Instruct reward scores decline under TPO) and the requirement that the policy model can interpret and act on textual feedback; no specialized TPO fine-tuning data is used.</s>
<s slug="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs" type="exploitation">The paper identifies **underthinking** in o1-like LLMs (QwQ-32B-Preview, DeepSeek-R1-671B, DeepSeek-R1-Preview, DeepSeek-R1-Distill-Llama-70B, DeepSeek-R1-Distill-Qwen-32B), where models prematurely abandon promising reasoning paths via frequent thought switches (signaled by terms like "alternatively"), producing longer outputs without accuracy gains on hard tasks. This contrasts with conventional LLMs (Qwen-Math-72B, Llama3.3-70B) and differs from overthinking on simple problems.

Experiments use MATH500 (including MATH500-Hard Level 5), GPQA Diamond, and AIME2022–2024. Thoughts are segmented automatically via Llama-3.3-70B after manual pattern collection. On AIME2024, incorrect responses average 225% more tokens and 418% more switches than correct ones; >70% of incorrect outputs contain ≥1 correct early thought (assessed via distilled R1 models with 82.9%/81.8% verification accuracy). The underthinking metric \(\xi_{UT}\) quantifies token inefficiency in incorrect answers as \(1 - \hat{T}_i / T_i\), where \(\hat{T}_i\) ends at the first correct thought (or equals \(T_i\) if none exists). Results show substantial \(\xi_{UT}\) across models/datasets, varying by task (higher accuracy sometimes pairs with higher UT on MATH500-Hard/GPQA).

To mitigate, the authors introduce **TIP** (thought switching penalty) decoding: logits for switch tokens \(\hat{V}\) (e.g., "alternatively") are reduced by \(\alpha\) for the first \(\beta\) tokens after each thought start \(\Psi\). Grid search on AIME2022–2023 selects \(\alpha=3\), \(\beta=600\). On QwQ-32B-Preview, TIP raises Pass@1 across sets, cuts switch tokens (e.g., AIME2024: 13.8→5.7), and lengthens intervals (580.1→941.6). It improves Self-Consistency (Pass@4 43.7%→51.4% on AIME2024) and Laconic Decoding, outperforming a persistence prompt. Weighted underthinking \(\xi_{wUT}\) is reported over 32 samples per instance.

The source includes a 13-line table of model accuracy/UT scores, an 8-line \(\alpha/\beta\) ablation, a 17-line Pass@k table with switch counts, and a 21-line Best-of-N comparison. Coverage is limited to visible-CoT math/science benchmarks and decoding-only fixes (no training); hyperparameters were tuned on AIME subsets; generalization to non-math domains or closed models is untested.</s>
<s slug="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-" type="exploitation">Test-Time Scaling (TTS) improves LLM reasoning via additional inference compute. The paper examines external TTS (Best-of-N, beam search, Diverse Verifier Tree Search) guided by Process Reward Models (PRMs), analyzing how policy models, PRMs, and problem difficulty affect compute-optimal allocation. It formulates reasoning as an MDP and introduces a reward-aware compute-optimal TTS strategy that incorporates the reward function \(\mathcal{R}\) into the target distribution, contrasting with prior non-reward-aware approaches.

Policy models span Llama-3.1/3.2 and Qwen2.5 families (0.5B–72B Instruct variants). PRMs evaluated include Math-Shepherd-PRM-7B, RLHFlow-PRM-Mistral-8B, RLHFlow-PRM-Deepseek-8B, Skywork-PRM-1.5B/7B, and Qwen2.5-Math-PRM-7B/72B. Scoring uses PRM-Min, PRM-Last, PRM-Avg; voting uses Majority Vote, PRM-Max, PRM-Vote. Experiments run on MATH-500 and AIME24 via the OpenR framework with budgets \(\{4,16,64,256,512\}\), step division by `\n\n`, and temperature 0.0/0.7.

Key claims: compute-optimal TTS is policy-, PRM-, and difficulty-dependent (absolute Pass@1 thresholds define easy/medium/hard levels); PRMs exhibit length bias and OOD sensitivity; on MATH-500, Llama-3.2-1B-Instruct exceeds Llama-3.1-405B-Instruct, Qwen2.5-0.5B-Instruct surpasses GPT-4o, Llama-3.2-3B-Instruct beats the 405B model, and DeepSeek-R1-Distill-Qwen-7B outperforms o1/DeepSeek-R1; similar patterns hold on AIME24. TTS yields up to 154.6% gains over CoT and 256× efficiency versus majority voting, with 100–1000× lower total FLOPS. It outperforms rStar-Math, Eurus-2, SimpleRL, and Satori but trails distillation from stronger models on hard tasks.

Includes a 20-line table comparing small policy models (compute-optimal TTS) with frontier LLMs on MATH-500/AIME24, a 6-line FLOPS table, 9-line voting-method table, 4-line training-data statistics table, and multiple performance figures across difficulty levels and PRMs. Limitations: restricted to mathematical tasks; PRM generalization and bias issues persist across in- and out-of-distribution data.</s>
<s slug="chain-of-draft-thinking-faster-by-writing-less" type="exploitation">Chain of Draft (CoD) is a prompting strategy for LLMs that generates minimalistic intermediate reasoning steps (at most five words each) instead of verbose Chain-of-Thought (CoT) outputs. It is evaluated against Standard few-shot prompting and CoT on arithmetic, commonsense, and symbolic reasoning tasks using GPT-4o (gpt-4o-2024-08-06) and Claude 3.5 Sonnet (claude-3-5-sonnet-20240620). CoD draws from human shorthand drafting and is supplied via manually authored few-shot examples that enforce concise equations or abstractions.

Benchmarks include GSM8k for arithmetic reasoning, date understanding and sports understanding from BIG-bench for commonsense reasoning, and a 250-example synthetic coin-flip dataset for symbolic reasoning. On GSM8k, CoD reaches 91% accuracy for both models with ~40 output tokens versus CoT accuracies above 95% with ~200 tokens, cutting output tokens by 80% and latency by 76.2% (GPT-4o) and 48.4% (Claude 3.5 Sonnet). In sports understanding, Claude 3.5 Sonnet token counts fall from 189.4 to 14.3 (92.4% reduction). On coin flip, both models achieve 100% accuracy with CoD/CoT while CoD reduces tokens 68–86%. Tables report model, prompt, accuracy, token count, and latency for all tasks.

Related techniques named are OpenAI o1, Alibaba QwQ, DeepSeek R1, ReAct, Skeleton-of-Thought (SoT), Coconut, Concise Thoughts (CCoT), and token-budget-aware LLM reasoning (TALE). The source links to code and data at https://github.com/sileix/chain-of-draft and includes result tables (e.g., 8-line GSM8k table and 14-line small-model table).

Limitations shown are sharp accuracy drops in zero-shot settings (CoD improves Claude by only 3.6% over direct answers) and larger gaps versus CoT on models under 3B parameters (Qwen2.5 1.5B/3B instruct, Llama 3.2 3B instruct, Zoom SLM 2.3B). No evaluation on o1-style reasoning models or integration with tool-use frameworks appears.</s>
<s slug="coat-chain-of-associated-thoughts-framework-for-enhancing-la" type="exploitation">CoAT (Chain-of-Associated-Thoughts) is a reasoning framework that augments LLMs with “slow thinking” by combining an optimized Monte Carlo Tree Search (MCTS) algorithm and a real-time associative memory (AM) mechanism. The framework expands the search space beyond static single-pass generation by inserting an Association stage between Expansion and Evaluation in MCTS, allowing each tree node to retrieve or self-generate concise, non-redundant key information that is absent from prior trajectory content.

Associative memory is produced either by the LLM itself or via an optional External Brain (EB) component that can query knowledge graphs, vector databases, LLM agents, or web search. Generated content at node \(n_{i+1}\) is conditioned on the query \(Q\), the parent node’s generation \(\mathcal{G}(n_i)\), and all ancestral associative memories \(\mathcal{AM}(n_{1:i})\). Node value is computed as \(V(n)=\mathcal{F}_g(Q,\mathcal{G}(n))+\beta\cdot\mathcal{F}_a(\mathcal{G}(n),\mathcal{AM}(n))\) with \(\beta=0.1\); UCT selection uses exploration weight \(w=1.0\). Search terminates either by a Reward Model at the leaf or by a configurable depth limit \(D\).

Implementation is built on LangChain. Experiments compare CoAT against NativeRAG, IRCoT, HippoRAG, KAG, CoT-SC, ToT, GoT, LATS, RAP, and reasoning models including OpenAI-o1, o1-mini, o3-mini, and DeepSeek-R1. On 1 000-question subsets of HotpotQA, 2WikiMultiHopQA, and MuSiQue, CoAT with Qwen2.5-32B-Instruct yields EM gains of 13.0 %, 7.2 %, and 13.4 % and F1 gains of 2.1 %, 3.3 %, and 8.4 % over KAG using the same backbone. On the proprietary Comprehensive Reasoning Benchmark (CRB) containing 205 professionally scored multi-domain questions, CoAT improves Qwen2.5-32B-Instruct and 72B-Instruct by 22 % and 18 % relative score, respectively, and achieves the highest average pairwise win rate. Ablation shows that removing AM drops average CRB score by approximately 10 %; optimal performance occurs at \(\beta=0.1\).

The source includes a table of end-to-end multi-hop QA results (11 lines), a table of CRB model scores (13 lines), and an ablation table (8 lines). Limitations noted are increased inference latency due to expanded search and AM insertion, plus residual quality variation in the CRB dataset.</s>
<s slug="helpsteer3-human-annotated-feedback-and-edit-data-to-empower" type="exploitation">HelpSteer3 releases human-annotated feedback and edit data (CC-BY-4.0) from 7000+ annotators across 80+ regions to train dedicated Feedback and Edit models for inference-time scaling on open-ended general-domain tasks. The system generates an initial response, obtains 2–10 sentence free-text feedback (starting with “The response is {not/slightly/…/perfectly} helpful”), then produces an edited response; scaling occurs by increasing initial responses per prompt, effective feedback per response (re-ranked by constructive-criticism keywords), and edited responses per feedback set.

Prompts are drawn from WildChat (General/STEM) and ShareGPT (Coding/Multilingual), filtered for safety and PII; responses are generated at temperature 0, top-p 0.9, 3072 tokens from Nemotron-4-340B-Instruct, Mistral-Large-2, Mixtral-8x22B-Instruct, Gemma-2 variants, Phi-3 variants, IBM Granite and Snowflake Arctic via NVIDIA API Catalog. Multi-turn turns are regenerated with the same models. Annotators (specialist pools for STEM/Coding via Scale AI, multilingual via Translated) produce three-to-five feedbacks per response; edits are performed only on responses rated mostly/ partially helpful by the three most-agreeing annotators. Three derived datasets result: Feedback Demonstration (imitate human feedback), Edit Demonstration (apply linearized feedback permutations), and Edit Preference (good vs. bad/no-edit pairs, General/STEM only).

Training initializes from Llama-3.3-70B-Instruct. Feedback and Edit SFT run one epoch (global batch 128); Edit RM uses Bradley-Terry on Edit Preference (step 80 lowest validation loss); Edit RL applies REINFORCE Leave-One-Out guided by the RM (step 45). Inference generates 10–64 feedbacks (temperature 0.5–0.8) and up to 16 edits, scored by Llama-3.1-Nemotron-70B-Reward or Llama-3.3-Nemotron-70B-Select. On Arena Hard the optimally scaled 70B Feedback-Edit system reaches 92.7 (8 responses × 16 effective feedback), exceeding OpenAI o1-preview-2024-09-12 (90.4) and DeepSeek R1 (92.3); MT Bench and length-controlled AlpacaEval 2.0 also improve. Ablations show self-feedback/self-edit yields no Arena Hard gain, Edit-without-feedback drops Arena Hard below the base model, and RL eliminates the ~30 % “no-edit” failure mode of SFT-only Edit. Distillation of scaled Feedback-Edit outputs into Llama-3.3-70B-Instruct lifts Arena Hard from 62.4 to 88.8.

Tables report dataset statistics (mean feedback length 437.8 characters, coding 518.6, multilingual 339.2; 14 programming and 13 natural languages), Edit Preference lengths, model-benchmark scores, and scaling curves. Appendices include prompt templates for language identification, complexity scoring, feedback and edit generation, illustrative good/bad edits, and human-evaluation preference counts (16 improvements vs. 7 degradations on 44 General prompts).

Limitations noted are non-compute-optimal feedback sampling, prompts sourced before April 2024 with length caps, and potential misinterpretation that the Feedback-Edit loop is the sole inference-time scaling method.</s>
<s slug="inference-time-computations-for-llm-reasoning-and-planning-a-1" type="exploitation">Sys2Bench is a benchmark introduced to evaluate inference-time techniques for LLM reasoning and planning across eleven datasets in five categories: arithmetic reasoning (GSM8K, AQuA), logical reasoning (ProntoQA), common sense reasoning (StrategyQA, HotPotQA), algorithmic reasoning (Game of 24, Bin Packing), and planning (BlocksWorld, Rubik’s Cube, TripPlan, CalendarPlan). The benchmark tests seven models—LLaMA 3.1 (8B/70B/405B), GPT-4o, GPT-4o-mini, o1, and o1-mini—using four techniques plus input-output prompting for large reasoning models (LRMs).

Chain-of-Thought (CoT) uses five in-context examples for step-by-step decomposition. Self-Consistency (SC) generates five CoT paths and applies majority voting. Tree of Thoughts (ToT) performs beam search (size 5 or 10) with LLM self-rating on a 1-10 scale or logits. Reasoning as Planning (RAP) applies Monte Carlo Tree Search (MCTS, up to 10 rollouts) with the LLM as both agent and world model, implemented only on LLaMA 3.1 8B. The source includes Table 1 summarizing the 11 datasets [ARTEFACT_A34: table, 11 lines, topic=algorithmic,reasoning,planning] and Figure 1 overviewing the four techniques on Game of 24.

Experiments show SC improves arithmetic and commonsense accuracy over CoT as model size grows, but tree-search methods underperform on arithmetic and logical tasks because LLMs fail at self-verification of intermediate steps. ToT and RAP excel on algorithmic tasks for larger models yet degrade on planning as depth increases beyond 4 steps. o1 and o1-mini achieve state-of-the-art results on most tasks except Rubik’s Cube, where all models score near zero due to spatial reasoning gaps; o1 follows popular online move sequences ~20% of the time. The source includes Table 2 (31-line results across methods) [ARTEFACT_A35: table, 31 lines, topic=methods,algorithmic,reasoning,logical] and Table 3 (LRM results) [ARTEFACT_A36: table, 5 lines, topic=arithmetic,reasoning,logical,common,sense].

Key claims include persistent LLM bias toward popular paths that limits exhaustive search, performance-cost trade-offs (ToT/RAP generate far more tokens than CoT/SC, with GPT-4o+ToT costing ~$60 for 100 Game of 24 problems), and out-of-distribution failure on Rubik’s Cube. The source also includes Figure 2 (ToT decline with depth on TripPlan/BlocksWorld) and Figure 3 (move popularity analysis). Limitations noted are RAP’s restriction to a subset of tasks and absence of verifier-dependent scaling analysis for commonsense problems.</s>
<s slug="inner-thinking-transformer-leveraging-dynamic-depth-scaling-" type="exploitation">Inner Thinking Transformer (ITT) addresses LLM reasoning bottlenecks under fixed parameter budgets by treating each Transformer layer computation as an implicit “inner thinking” step on token hidden states. Critical tokens trigger gradient spikes (measured via gradient nuclear norm on GPT-2 attention matrices over AQuA easy/hard splits); ITT therefore allocates variable depth only to those tokens.

Core mechanisms are Adaptive Token Routing (ATR) via per-step linear weight predictors \(\mathcal{R}^{(t)}\) that select the top-\(\rho\) percentile of tokens, Residual Thinking Connections (RTC) that accumulate weighted layer outputs \(x^{(t)}=\sum_{i=1}^{t}(f(x^{(i-1)})\odot\phi^{(i)})\) with learnable Thinking Step Encoding vectors \(\phi^{(t)}\), and early-exit logic when loss falls below threshold \(\epsilon\). The resulting ITT layer is inserted every other layer in a LLaMA-2 backbone.

Models (162 M / 230 M / 466 M) were pretrained from scratch on the 50 B-token RedPajama corpus (sequence length 4096, global batch 256) using the Sheared-LLaMA codebase on Composer with eight A100-80 GB GPUs for 50 k steps. Evaluation used lm-evaluation-harness (0-shot SciQ/PIQA/WG/ARC-E/LogiQA/LAMBADA, 10-shot HellaSwag, 25-shot ARC-C, 32-shot BoolQ). ITT \(\times4\)-162 M reaches 96.5 % of the 466 M Transformer average while using 56.8 % of the training tokens and 70 % of the FLOPs of a comparable Loop baseline; ITT \(\times2\) already exceeds the 230 M dense model. Elastic inference allows post-training changes to selection ratios (e.g., 50/50/50 or 70/70/90) with <0.3 PPL degradation. Ablations quantify RTC (+0.77 PPL), Thinking Step Encoding (+0.31 PPL) and ATR (+0.19 PPL) contributions.

The source includes Table 1 (model, params, FLOPs, commonsense/reading scores), Table 2 (token-selection ratios vs. PPL), Table 3 (ablation PPL), Table 4 (extended-step PPL), Table 5 (architecture configs), and Figures 4–7 (loss/perplexity curves, router distributions, token visualizations). Limitations noted are fixed training routing patterns, restriction to ≤466 M models, extra backward-pass memory from RTC, and the need for richer temporal encodings.</s>
<s slug="s-superscript-s-italic-s-start-postsuperscript-end-postsuper" type="exploitation">S* is a hybrid test-time scaling framework for code generation that augments parallel sampling with sequential scaling via iterative debugging and introduces adaptive input synthesis for selection. It takes a coding problem P (natural language description plus public/private test cases) and model M to produce program X(·). Public tests (average 2.0 per CodeContests problem) are used for refinement and filtering; private tests (average 202.1) evaluate final correctness.

Stage 1 (Generation) generates N=16 samples in parallel at temperature 0.7, then applies up to R=2 rounds of iterative debugging: each sample executes on public tests via an interpreter; outputs or error messages are fed back to M for revision until all public tests pass or the round limit is reached. Stage 2 (Selection) applies public-test filtering, then adaptive input synthesis: an LLM synthesizes distinguishing inputs for pairwise cluster comparisons, executes them, and grounds decisions in the resulting outputs rather than model-predicted outputs (Algorithm 1). Prompts are produced automatically by DSPy; execution occurs in a sandbox.

Evaluations span 12 models on LiveCodeBench (v2: 511 problems) and CodeContests (165 problems) using Pass@1. Key results include: Qwen2.5-7B-Instruct + S* outperforms Qwen2.5-32B-Instruct by 10.1–10.7%; GPT-4o-mini + S* exceeds o1-preview by 3.7%; DeepSeek-R1-Distill-Qwen-32B + S* reaches 85.7% (approaching o1-high at 88.5%). S* outperforms majority voting (execution-based clustering) by up to 9.9% and self-debugging by up to 15.6% on the same models. On CodeContests, Qwen2.5-Coder-7B-Instruct + S* improves from 1.8% zero-shot to 9.1%. Ablations confirm moderate temperature (0.7) maximizes Pass@N, performance scales log-linearly with N up to 64, public-test-only debugging outperforms variants with generated tests or last-round context, and adaptive input synthesis exceeds LLM-as-a-judge and generated-tests baselines.

Related work positions S* against AlphaCode, AlphaCodium, and concurrent CodeMonkeys (SWE-Bench focus). It integrates with ICL retrieval (BM25 or pattern-based) but finds performance sensitive to example quality. The repository https://github.com/NovaSky-AI/SkyThought releases code, generations, and intermediates. The work covers only competition-level code generation, not software-engineering tasks such as SWE-Bench, and prioritizes accuracy over cost minimization. Includes tables comparing zero-shot/majority-voting/self-debugging/S* across Qwen-Coder and R1-Distill series, CodeContests results, and selection-policy accuracy.</s>
<s slug="s1 _  Simple test-time scaling" type="exploitation">s1 introduces a minimal recipe for test-time scaling in reasoning models via supervised finetuning on a 1,000-example dataset (s1K) followed by the budget-forcing decoding intervention. The work curates s1K from an initial 59K pool drawn from NuminaMATH, OlympicArena, OmniMath, AGIEval, historical AIME problems, s1-prob (Stanford probability qualifying-exam questions), and s1-teasers (PuzzledQuant “Hard” items). Traces are distilled with the Gemini Flash Thinking API; filtering applies quality (removal of formatting errors), difficulty (removal of items solved by Qwen2.5-7B/32B-Instruct), and diversity (MSC-domain classification via Claude 3.5 Sonnet plus length-weighted sampling) criteria, yielding 50 domains. The resulting s1-32B model is obtained by five-epoch SFT of Qwen2.5-32B-Instruct (26 min on 16 H100 GPUs with PyTorch FSDP, bfloat16, cosine LR schedule).

Budget forcing enforces sequential test-time compute by (I) appending the end-of-thinking delimiter (and optionally “Final Answer:”) to cap tokens or (II) suppressing the delimiter and appending “Wait” to extend reasoning. The method is compared against token-, step-, and class-conditional prompting as well as rejection sampling; metrics are Control (fraction of runs inside a pre-specified token budget), Scaling (average slope of the accuracy-vs-compute curve), and Performance (peak accuracy). On AIME24, s1-32B with budget forcing rises from 50 % to 57 %; on MATH500 and GPQA Diamond it exceeds o1-preview by up to 27 %. Parallel scaling baselines (majority voting, REBASE) are also evaluated. The source includes tables reporting model comparisons, data-ablation results, method metrics on AIME24, training-sequence-length ablations, and domain statistics, plus a 23-line Python tool-loop example and multiple full reasoning traces.

Notable limitations are eventual flattening of the scaling curve, context-window exhaustion, repetitive loops when “Wait” is appended too often, and non-deterministic evaluation scores under vLLM even with greedy sampling.</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-introduction | 3 | 2 | 0 |
| S2::section-2-implementing-and-improving-reasoning-in-llms-the-four-main-categories | 3 | 2 | 0 |
| S3::section-3-inference-time-compute-scaling-methods | 3 | 2 | 0 |
| S4::section-4-s1-simple-test-time-scaling | 3 | 2 | 0 |
| S5::section-5-other-noteworthy-research-papers-on-inference-time-compute-scaling | 3 | 2 | 0 |
| S6::section-6-test-time-preference-optimization | 3 | 2 | 0 |
| S7::section-7-thoughts-are-all-over-the-place | 3 | 2 | 0 |
| S8::section-8-trading-inference-time-compute-for-adversarial-robustness | 3 | 2 | 0 |
| S9::section-9-chain-of-associated-thoughts | 3 | 2 | 0 |
| S10::section-10-step-back-to-leap-forward | 3 | 2 | 0 |
| S11::section-11-scaling-up-test-time-compute-with-latent-reasoning | 2 | 2 | 0 |
| S12::section-12-can-a-1b-llm-surpass-a-405b-llm | 2 | 2 | 0 |
| S13::section-13-learning-to-reason-from-feedback-at-test-time | 2 | 2 | 0 |
| S14::section-14-inference-time-computations-for-llm-reasoning-and-planning | 2 | 2 | 0 |
| S15::section-15-inner-thinking-transformer | 2 | 2 | 0 |
| S16::section-16-test-time-scaling-for-code-generation | 2 | 2 | 0 |
| S17::section-17-chain-of-draft | 2 | 1 | 0 |
| S18::section-18-better-feedback-and-edit-models | 1 | 1 | 0 |
| S19::section-19-conclusion | 2 | 1 | 0 |
tavily_saturation=1.0
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-introduction" self_contained="no" sources="inference-time-computations-for-llm-reasoning-and-planning-a-1,can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-,s-superscript-s-italic-s-start-postsuperscript-end-postsuper" artefacts="">
  <intent>Establishes why stronger LLM reasoning is a top priority in 2025 for agentic systems and narrows focus to post-DeepSeek-R1 inference-time compute scaling papers.</intent>
  <depth_checklist depth_score="2">
    <item name="motivation" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="5" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We open by establishing why stronger LLM reasoning is a top priority in 2025: complex user tasks in agentic systems requ" bullet="motivation">Directly matches motivation item covered by benchmark sources.</orphan>
    <orphan route="depth" anchor="We describe the recent research surge that blends inference-time scaling, pure RL, RL plus SFT hybrids, and SFT with dis" bullet="latest_advancements">Matches latest_advancements item.</orphan>
    <orphan route="depth" anchor="We explicitly state the article's narrow focus on post-DeepSeek-R1 inference-time compute scaling papers." bullet="motivation">Aligns with motivation for scope.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph would illustrate metrics but no supporting evidence present.</orphan>
    <orphan route="depth" anchor="Transition to Section 2: We now examine each of the four categories in detail so the reader can understand how inference" bullet="theoretical_foundations">Transition requires theoretical foundations not present.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-implementing-and-improving-reasoning-in-llms-the-four-main-categories" self_contained="no" sources="chain-of-draft-thinking-faster-by-writing-less,Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs,1-scaling-by-thinking-in-continuous-space" artefacts="">
  <intent>Defines reasoning models versus direct-answer LLMs and details the four categories of reasoning model development with training versus inference compute distinctions.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="theoretical_foundations" present="yes" evidence="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs"/>
    <item name="technical_nuances" present="yes" evidence="chain-of-draft-thinking-faster-by-writing-less"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="7" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We define reasoning models as those that generate explicit or internal intermediate thought processes before producing a" bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
    <orphan route="depth" anchor="We contrast increasing training compute (modifying weights via RL or SFT) versus increasing inference compute (extra FLO" bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We explain that most practical systems combine heavy train-time preparation with test-time thinking to achieve best resu" bullet="motivation">Matches motivation item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
    <orphan route="depth" anchor="We break down the four categories in sequence, explaining each category with a paragraph: (1) Inference-time compute sca" bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="Transition to Section 3: With the four categories now mapped, we zoom in on the inference-time compute scaling branch th" bullet="technical_nuances">Transition requires technical_nuances not fully present.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-inference-time-compute-scaling-methods" self_contained="no" sources="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS,s1 _  Simple test-time scaling,Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback" artefacts="">
  <intent>Articulates core idea of extra inference compute for thinking longer and reviews classic prompt engineering plus search/voting strategies.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="theoretical_foundations" present="yes" evidence="s1 _  Simple test-time scaling"/>
    <item name="technical_nuances" present="yes" evidence="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="4" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We articulate the core idea that extra inference compute lets models "think longer," directly analogous to humans spendi" bullet="motivation">Matches motivation item.</orphan>
    <orphan route="depth" anchor="We review classic prompt engineering approaches such as chain-of-thought and their direct impact on token count, latency" bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
    <orphan route="depth" anchor="We cover search and voting strategies, specifically majority voting and beam search guided by process reward models, sho" bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-s1-simple-test-time-scaling" self_contained="no" sources="s1 _  Simple test-time scaling" artefacts="">
  <intent>Describes the s1 hybrid approach with curated 1k dataset, wait tokens, budget forcing, and empirical length-accuracy correlations.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="s1 _  Simple test-time scaling"/>
    <item name="theoretical_foundations" present="yes" evidence="s1 _  Simple test-time scaling"/>
    <item name="technical_nuances" present="yes" evidence="s1 _  Simple test-time scaling"/>
    <item name="latest_advancements" present="yes" evidence="s1 _  Simple test-time scaling"/>
    <item name="limitations_failure_modes" present="yes" evidence="s1 _  Simple test-time scaling"/>
    <item name="implementation_tradeoffs" present="yes" evidence="s1 _  Simple test-time scaling"/>
    <item name="case_studies_metrics" present="yes" evidence="s1 _  Simple test-time scaling"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="6" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We describe the hybrid approach in [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393) (31 Jan, 2025) that" bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We detail the mechanism of "wait" tokens that encourage self-verification and self-correction, contrasting them with sim" bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We explain budget forcing as a sequential scaling technique and contrast it with parallel methods such as majority votin" bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We report the observed correlation between generated response length and accuracy on reasoning benchmarks, citing the pa" bullet="case_studies_metrics">Matches case_studies_metrics item.</orphan>
    <orphan route="depth" anchor="We surface the paper's stated limitations and its call for future comparisons against beam search, lookahead search, com" bullet="limitations_failure_modes">Matches limitations_failure_modes item.</orphan>
    <orphan route="depth" anchor="We connect the technique to DeepSeek-R1's "Aha moment" and present the paper's empirical comparison of "Wait" versus "Hm" bullet="latest_advancements">Matches latest_advancements item.</orphan>
    <orphan route="depth" anchor="Insert the following graphs with the following online URL syntax in the appropriate places:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
    <orphan route="depth" anchor="Transition to Section 5: No transition needed." bullet="implementation_tradeoffs">Transition requires implementation_tradeoffs not present.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-other-noteworthy-research-papers-on-inference-time-compute-scaling" self_contained="no" sources="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS,helpsteer3-human-annotated-feedback-and-edit-data-to-empower,can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-" artefacts="">
  <intent>Explains rationale for brief summaries of high-volume papers and highlights common patterns of blending training with inference control.</intent>
  <depth_checklist depth_score="2">
    <item name="motivation" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We explain our rationale for keeping individual summaries brief given the high volume of recent papers, allowing the rea" bullet="motivation">Matches motivation item.</orphan>
    <orphan route="depth" anchor="We highlight the common pattern that many papers blend some training with explicit control of inference-time compute rat" bullet="latest_advancements">Matches latest_advancements item.</orphan>
    <orphan route="depth" anchor="We differentiate these regulated approaches from distillation or SFT approaches that merely produce longer outputs witho" bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
  </orphan_anchors>
</section>
<section id="S6::section-6-test-time-preference-optimization" self_contained="no" sources="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback" artefacts="">
  <intent>Describes the iterative on-the-fly alignment process in TPO that avoids weight changes using reward models and textual critiques.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback"/>
    <item name="theoretical_foundations" present="yes" evidence="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback"/>
    <item name="technical_nuances" present="yes" evidence="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback"/>
    <item name="latest_advancements" present="yes" evidence="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback"/>
    <item name="limitations_failure_modes" present="yes" evidence="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback"/>
    <item name="implementation_tradeoffs" present="yes" evidence="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback"/>
    <item name="case_studies_metrics" present="yes" evidence="Test-Time Preference Optimization _ On-the-Fly Alignment via Iterative Textual Feedback"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We describe the iterative on-the-fly alignment process in "Test-Time Preference Optimization: On-the-Fly Alignment via I" bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We detail the use of a reward model to select chosen and rejected responses, followed by generation of textual critiques" bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We walk through the four-step loop—generation, scoring, critique, and refinement—that repeats to progressively improve o" bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
  </orphan_anchors>
</section>
<section id="S7::section-7-thoughts-are-all-over-the-place" self_contained="no" sources="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs" artefacts="">
  <intent>Defines underthinking in o1-like models and presents the TIP decoding method that penalizes premature path switches at inference.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs"/>
    <item name="theoretical_foundations" present="yes" evidence="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs"/>
    <item name="technical_nuances" present="yes" evidence="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs"/>
    <item name="latest_advancements" present="yes" evidence="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs"/>
    <item name="limitations_failure_modes" present="yes" evidence="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs"/>
    <item name="implementation_tradeoffs" present="yes" evidence="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs"/>
    <item name="case_studies_metrics" present="yes" evidence="Thoughts Are All Over the Place _ On the Underthinking of o1-Like LLMs"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We define the underthinking phenomenon in o1-like models as in "Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs"(https://arxiv.org/abs/2501.18585) where frequent reasoning path switches reduce final accuracy." bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="We present the Thought Switching Penalty (TIP) method that modifies logits at inference time to discourage premature path transitions without any fine-tuning." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We report how this no-fine-tuning approach improves accuracy on challenging benchmarks by forcing deeper exploration of promising reasoning paths." bullet="case_studies_metrics">Matches case_studies_metrics item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
  </orphan_anchors>
</section>
<section id="S8::section-8-trading-inference-time-compute-for-adversarial-robustness" self_contained="no" sources="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS" artefacts="">
  <intent>Shows how increased inference-time compute reduces attack success rates and introduces novel attacks that counteract robustness gains.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="theoretical_foundations" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="technical_nuances" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="latest_advancements" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="limitations_failure_modes" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="implementation_tradeoffs" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="case_studies_metrics" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We show how increased inference-time compute, as in "Trading Inference-Time Compute for Adversarial Robustness"(https://arxiv.org/abs/2501.18841), generally reduces successful attack rates even without adversarial training, citing the paper's empirical trade-off curves." bullet="case_studies_metrics">Matches case_studies_metrics item.</orphan>
    <orphan route="depth" anchor="We highlight important exceptions where gains are limited, especially in policy ambiguity or loophole exploitation scenarios." bullet="limitations_failure_modes">Matches limitations_failure_modes item.</orphan>
    <orphan route="depth" anchor="We describe new attack strategies introduced in the paper—Think Less and Nerd Sniping—that can counteract robustness gains from scaling." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
  </orphan_anchors>
</section>
<section id="S9::section-9-chain-of-associated-thoughts" self_contained="no" sources="coat-chain-of-associated-thoughts-framework-for-enhancing-la" artefacts="">
  <intent>Describes the CoAT framework combining MCTS with associative memory for dynamic knowledge recall during inference-time search.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="coat-chain-of-associated-thoughts-framework-for-enhancing-la"/>
    <item name="theoretical_foundations" present="yes" evidence="coat-chain-of-associated-thoughts-framework-for-enhancing-la"/>
    <item name="technical_nuances" present="yes" evidence="coat-chain-of-associated-thoughts-framework-for-enhancing-la"/>
    <item name="latest_advancements" present="yes" evidence="coat-chain-of-associated-thoughts-framework-for-enhancing-la"/>
    <item name="limitations_failure_modes" present="yes" evidence="coat-chain-of-associated-thoughts-framework-for-enhancing-la"/>
    <item name="implementation_tradeoffs" present="yes" evidence="coat-chain-of-associated-thoughts-framework-for-enhancing-la"/>
    <item name="case_studies_metrics" present="yes" evidence="coat-chain-of-associated-thoughts-framework-for-enhancing-la"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We describe the combination of Monte Carlo Tree Search with an associative memory in "CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning"(https://arxiv.org/abs/2502.02390) that acts as a dynamic knowledge base during inference." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We explain the benefit of associative memory for recalling earlier reasoning paths and incorporating newly generated information without losing context." bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="We detail how the overall framework aids systematic exploration of reasoning pathways at test time." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
  </orphan_anchors>
</section>
<section id="S10::section-10-step-back-to-leap-forward" self_contained="no" sources="inner-thinking-transformer-leveraging-dynamic-depth-scaling-,can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-,coat-chain-of-associated-thoughts-framework-for-enhancing-la" artefacts="">
  <intent>Presents self-backtracking mechanism that teaches models to revise suboptimal paths using a learned backtrack token at inference.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="coat-chain-of-associated-thoughts-framework-for-enhancing-la"/>
    <item name="theoretical_foundations" present="yes" evidence="inner-thinking-transformer-leveraging-dynamic-depth-scaling-"/>
    <item name="technical_nuances" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="4" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We present the self-backtracking mechanism in "Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models"(https://arxiv.org/abs/2502.0440) that teaches models when and where to revise suboptimal paths using a learned backtrack token." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We contrast the training phase that uses the special backtrack token with the key inference-time contribution of tree-based search that leverages the learned ability." bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="We emphasize the advantage of not requiring external reward models, unlike standard process-reward-guided search." bullet="motivation">Matches motivation item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
    <orphan route="depth" anchor="We describe how the model can dynamically adjust search depth and breadth using its acquired backtracking skill." bullet="technical_nuances">Matches technical_nuances item.</orphan>
  </orphan_anchors>
</section>
<section id="S11::section-11-scaling-up-test-time-compute-with-latent-reasoning" self_contained="no" sources="1-scaling-by-thinking-in-continuous-space" artefacts="">
  <intent>Explains recurrent depth approach that iterates in latent space rather than producing additional output tokens.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="theoretical_foundations" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="technical_nuances" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="latest_advancements" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="limitations_failure_modes" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="implementation_tradeoffs" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="case_studies_metrics" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="2" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We explain the recurrent depth approach in "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"(https://arxiv.org/abs/2502.05171) that iterates in latent space rather than producing additional output tokens." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We describe the hidden-state-like behavior similar to RNNs that refines reasoning without increasing visible output length." bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="We discuss the major drawback: the absence of explicit reasoning steps that aid human interpretability and debugging." bullet="limitations_failure_modes">Matches limitations_failure_modes item.</orphan>
  </orphan_anchors>
</section>
<section id="S12::section-12-can-a-1b-llm-surpass-a-405b-llm" self_contained="no" sources="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-" artefacts="">
  <intent>Summarizes systematic study showing compute-optimal TTS allows small models to outperform larger unscaled models on math benchmarks.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="theoretical_foundations" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="technical_nuances" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="latest_advancements" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="limitations_failure_modes" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="implementation_tradeoffs" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="case_studies_metrics" present="yes" evidence="can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We summarize the systematic study of interactions in "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"(https://arxiv.org/abs/2502.06703) between inference-time scaling, process reward models, and problem difficulty." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We detail the compute-optimal scaling strategy that adapts the inference budget according to PRM choice, policy model size, and task complexity." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We report the evidence that a 1B model with proper scaling can outperform an unscaled 405B Llama 3 on the same benchmarks." bullet="case_studies_metrics">Matches case_studies_metrics item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
  </orphan_anchors>
</section>
<section id="S13::section-13-learning-to-reason-from-feedback-at-test-time" self_contained="no" sources="helpsteer3-human-annotated-feedback-and-edit-data-to-empower" artefacts="">
  <intent>Acknowledges OpTune method that updates weights during inference based on prior mistakes without storing failed attempts in context.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="theoretical_foundations" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="technical_nuances" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="latest_advancements" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="limitations_failure_modes" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="implementation_tradeoffs" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="case_studies_metrics" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We acknowledge the challenge of classifying the method in "Learning to Reason from Feedback at Test-Time"(https://www.arxiv.org/abs/2502.12521) as pure inference-time or training-time because it updates model weights during inference." bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="We describe the OpTune optimizer that adjusts model weights based on previous mistakes without storing failed attempts in the prompt context." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We contrast this weight-update approach with sequential revision (adding attempts to the prompt) and parallel sampling approaches." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We highlight the benefit of remembering errors via lightweight weight updates rather than growing context length indefinitely." bullet="limitations_failure_modes">Matches limitations_failure_modes item.</orphan>
  </orphan_anchors>
</section>
<section id="S14::section-14-inference-time-computations-for-llm-reasoning-and-planning" self_contained="no" sources="inference-time-computations-for-llm-reasoning-and-planning-a-1" artefacts="">
  <intent>Presents Sys2Bench benchmark evaluating CoT, ToT, RAP across arithmetic, logical, commonsense, algorithmic and planning tasks.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="theoretical_foundations" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="technical_nuances" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="latest_advancements" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="limitations_failure_modes" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="implementation_tradeoffs" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="case_studies_metrics" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We present the benchmark in "Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights"(https://www.arxiv.org/abs/2502.12521) that evaluates CoT, Tree-of-Thought, Reasoning as Planning, and additional techniques across eleven diverse tasks." bullet="case_studies_metrics">Matches case_studies_metrics item.</orphan>
    <orphan route="depth" anchor="We list the task categories covered: arithmetic, logical, commonsense, algorithmic reasoning, and planning domains." bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="We extract the key insight that no single inference-time technique dominates across all task types, forcing engineers to match methods to domains." bullet="limitations_failure_modes">Matches limitations_failure_modes item.</orphan>
    <orphan route="depth" anchor="We summarize the analysis of computational cost versus performance trade-offs provided in the paper." bullet="implementation_tradeoffs">Matches implementation_tradeoffs item.</orphan>
  </orphan_anchors>
</section>
<section id="S15::section-15-inner-thinking-transformer" self_contained="no" sources="inner-thinking-transformer-leveraging-dynamic-depth-scaling-" artefacts="">
  <intent>Introduces dynamic depth scaling via Adaptive Token Routing that allocates extra compute only to difficult tokens inside the model.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="inner-thinking-transformer-leveraging-dynamic-depth-scaling-"/>
    <item name="theoretical_foundations" present="yes" evidence="inner-thinking-transformer-leveraging-dynamic-depth-scaling-"/>
    <item name="technical_nuances" present="yes" evidence="inner-thinking-transformer-leveraging-dynamic-depth-scaling-"/>
    <item name="latest_advancements" present="yes" evidence="inner-thinking-transformer-leveraging-dynamic-depth-scaling-"/>
    <item name="limitations_failure_modes" present="yes" evidence="inner-thinking-transformer-leveraging-dynamic-depth-scaling-"/>
    <item name="implementation_tradeoffs" present="yes" evidence="inner-thinking-transformer-leveraging-dynamic-depth-scaling-"/>
    <item name="case_studies_metrics" present="yes" evidence="inner-thinking-transformer-leveraging-dynamic-depth-scaling-"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We introduce dynamic depth scaling in "Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking"(https://arxiv.org/abs/2502.13842) that avoids using a fixed transformer layer count for every token." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We detail Adaptive Token Routing, which sends difficult tokens through the same layer multiple times, selectively increasing the inference compute budget for harder tokens." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We explain how this mechanism allocates extra thinking effort exactly where it is needed without lengthening the output sequence." bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
  </orphan_anchors>
</section>
<section id="S16::section-16-test-time-scaling-for-code-generation" self_contained="no" sources="s-superscript-s-italic-s-start-postsuperscript-end-postsuper" artefacts="">
  <intent>Describes S* hybrid framework combining parallel candidate generation with sequential iterative debugging using execution feedback for code.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="s-superscript-s-italic-s-start-postsuperscript-end-postsuper"/>
    <item name="theoretical_foundations" present="yes" evidence="s-superscript-s-italic-s-start-postsuperscript-end-postsuper"/>
    <item name="technical_nuances" present="yes" evidence="s-superscript-s-italic-s-start-postsuperscript-end-postsuper"/>
    <item name="latest_advancements" present="yes" evidence="s-superscript-s-italic-s-start-postsuperscript-end-postsuper"/>
    <item name="limitations_failure_modes" present="yes" evidence="s-superscript-s-italic-s-start-postsuperscript-end-postsuper"/>
    <item name="implementation_tradeoffs" present="yes" evidence="s-superscript-s-italic-s-start-postsuperscript-end-postsuper"/>
    <item name="case_studies_metrics" present="yes" evidence="s-superscript-s-italic-s-start-postsuperscript-end-postsuper"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We describe the S* method in " S\*: Test Time Scaling for Code Generation"(https://arxiv.org/abs/2502.14382) specialized for code that combines parallel generation of candidate solutions with sequential iterative debugging." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
    <orphan route="depth" anchor="We break down the two-stage process: first, generation with execution feedback on public test cases; second, adaptive selection and repair of candidates." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We explain the use of execution results and errors to iteratively repair solutions and the technique of adaptive input synthesis that creates discriminating test cases to distinguish between passing solutions." bullet="technical_nuances">Matches technical_nuances item.</orphan>
  </orphan_anchors>
</section>
<section id="S17::section-17-chain-of-draft" self_contained="no" sources="chain-of-draft-thinking-faster-by-writing-less" artefacts="">
  <intent>Reports Chain of Draft prompting that generates minimal intermediate steps instead of verbose CoT for efficiency gains.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="chain-of-draft-thinking-faster-by-writing-less"/>
    <item name="theoretical_foundations" present="yes" evidence="chain-of-draft-thinking-faster-by-writing-less"/>
    <item name="technical_nuances" present="yes" evidence="chain-of-draft-thinking-faster-by-writing-less"/>
    <item name="latest_advancements" present="yes" evidence="chain-of-draft-thinking-faster-by-writing-less"/>
    <item name="limitations_failure_modes" present="yes" evidence="chain-of-draft-thinking-faster-by-writing-less"/>
    <item name="implementation_tradeoffs" present="yes" evidence="chain-of-draft-thinking-faster-by-writing-less"/>
    <item name="case_studies_metrics" present="yes" evidence="chain-of-draft-thinking-faster-by-writing-less"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We report the observation that humans often use concise drafts rather than verbose step-by-step explanations when solving problems internally." bullet="motivation">Matches motivation item.</orphan>
    <orphan route="depth" anchor="We present Chain of Draft prompting in "Chain of Draft: Thinking Faster by Writing Less"(https://arxiv.org/abs/2502.18600) that generates minimal yet informative intermediate steps instead of full natural-language reasoning." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
    <orphan route="depth" anchor="We quantify the efficiency gains from drastically reduced token count while retaining accuracy comparable to full chain-of-thought on reasoning benchmarks." bullet="case_studies_metrics">Matches case_studies_metrics item.</orphan>
  </orphan_anchors>
</section>
<section id="S18::section-18-better-feedback-and-edit-models" self_contained="no" sources="helpsteer3-human-annotated-feedback-and-edit-data-to-empower" artefacts="">
  <intent>Outlines dedicated Feedback and Edit models trained on human-annotated data to enable iterative refinement on open-ended tasks.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="theoretical_foundations" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="technical_nuances" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="latest_advancements" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="limitations_failure_modes" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="implementation_tradeoffs" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="case_studies_metrics" present="yes" evidence="helpsteer3-human-annotated-feedback-and-edit-data-to-empower"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="We outline the challenge of applying inference scaling to open-ended tasks that lack verifiable answers such as creative writing or high-level planning." bullet="motivation">Matches motivation item.</orphan>
    <orphan route="depth" anchor="We describe a specialized architecture in "Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks"(https://arxiv.org/abs/2503.04378) that decouples a generator model, a feedback model, and an edit model, each optimized for its role." bullet="technical_nuances">Matches technical_nuances item.</orphan>
    <orphan route="depth" anchor="We explain how the feedback and edit models are trained on large human-annotated datasets of responses, critiques, and revisions to produce higher-quality signals than a single model could." bullet="theoretical_foundations">Matches theoretical_foundations item.</orphan>
    <orphan route="depth" anchor="Insert a graph with the following online URL syntax:" bullet="case_studies_metrics">Graph insertion lacks supporting evidence.</orphan>
  </orphan_anchors>
</section>
<section id="S19::section-19-conclusion" self_contained="no" sources="inference-time-computations-for-llm-reasoning-and-planning-a-1,1-scaling-by-thinking-in-continuous-space,TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS" artefacts="">
  <intent>Positions inference-time compute scaling as a major 2025 direction and recaps techniques while noting caveats and future directions.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="theoretical_foundations" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="technical_nuances" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="latest_advancements" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="limitations_failure_modes" present="yes" evidence="TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS"/>
    <item name="implementation_tradeoffs" present="yes" evidence="1-scaling-by-thinking-in-continuous-space"/>
    <item name="case_studies_metrics" present="yes" evidence="inference-time-computations-for-llm-reasoning-and-planning-a-1"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0">
  </orphan_anchors>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction" need_depth="21" need_breadth="6" target_words="130" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S2::section-2-implementing-and-improving-reasoning-in-llms-the-four-main-categories" need_depth="26" need_breadth="6" target_words="870" mandatory_bullets="7" must_cover_depth="5" must_stay_brief="0"/>
  <section id="S3::section-3-inference-time-compute-scaling-methods" need_depth="17" need_breadth="6" target_words="200" mandatory_bullets="6" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S4::section-4-s1-simple-test-time-scaling" need_depth="19" need_breadth="6" target_words="450" mandatory_bullets="7" must_cover_depth="5" must_stay_brief="0"/>
  <section id="S5::section-5-other-noteworthy-research-papers-on-inference-time-compute-scaling" need_depth="15" need_breadth="6" target_words="150" mandatory_bullets="3" must_cover_depth="2" must_stay_brief="1"/>
  <section id="S6::section-6-test-time-preference-optimization" need_depth="10" need_breadth="6" target_words="150" mandatory_bullets="4" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S7::section-7-thoughts-are-all-over-the-place" need_depth="10" need_breadth="6" target_words="120" mandatory_bullets="3" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S8::section-8-trading-inference-time-compute-for-adversarial-robustness" need_depth="10" need_breadth="6" target_words="150" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S9::section-9-chain-of-associated-thoughts" need_depth="10" need_breadth="6" target_words="100" mandatory_bullets="3" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S10::section-10-step-back-to-leap-forward" need_depth="17" need_breadth="6" target_words="180" mandatory_bullets="4" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S11::section-11-scaling-up-test-time-compute-with-latent-reasoning" need_depth="7" need_breadth="6" target_words="120" mandatory_bullets="3" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S12::section-12-can-a-1b-llm-surpass-a-405b-llm" need_depth="10" need_breadth="6" target_words="160" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S13::section-13-learning-to-reason-from-feedback-at-test-time" need_depth="10" need_breadth="6" target_words="180" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S14::section-14-inference-time-computations-for-llm-reasoning-and-planning" need_depth="10" need_breadth="6" target_words="120" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S15::section-15-inner-thinking-transformer" need_depth="10" need_breadth="6" target_words="120" mandatory_bullets="3" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S16::section-16-test-time-scaling-for-code-generation" need_depth="10" need_breadth="6" target_words="440" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S17::section-17-chain-of-draft" need_depth="10" need_breadth="6" target_words="200" mandatory_bullets="4" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S18::section-18-better-feedback-and-edit-models" need_depth="10" need_breadth="6" target_words="150" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S19::section-19-conclusion" need_depth="1" need_breadth="6" target_words="700" mandatory_bullets="7" must_cover_depth="4" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S1::section-1-introduction, S2::section-2-implementing-and-improving-reasoning-in-llms-the-four-main-categories</weakest_sections>
    <strongest_sections>S19::section-19-conclusion, S11::section-11-scaling-up-test-time-compute-with-latent-reasoning</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>