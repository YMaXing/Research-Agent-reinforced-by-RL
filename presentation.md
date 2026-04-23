# RL-Guided Exploration Planning — Presentation Notes

## 1. Problem framing

A research agent must decide how aggressively to explore the web before drafting an article. Too few rounds → thin coverage; too many → wasted budget and noisy sources. We frame this as a **6-way preset selection** problem:

| Preset | Rounds | Schedule |
|--------|:------:|----------|
| P0 | 0 | No exploration |
| P1 | 1 | balanced |
| P2 | 2 | balanced → depth |
| P3 | 2 | depth → breadth |
| P4 | 3 | balanced → depth → breadth |
| P5 | 3 | depth → breadth → depth |

The policy is a fine-tuned LLM that reads a structured **exploitation digest** (gap profile + per-section coverage analysis) and outputs a preset distribution.

## 2. Data — and the elephant in the room

| Split | Articles | Episodes |
|-------|:---:|:---:|
| Train | 4 (`03_context_engineering`, `05_workflow_patterns`, `08_react_practice`, `11_multimodal`) | 4 × 6 = 24 |
| Test  | 3 (`02_workflows_vs_agents`, `06_tools`, `09_RAG`)                                        | 3 × 6 = 18 |

### Article characteristics

**Training set**

| Lesson | Topic | Theory / Practice | Word Count | Distinct Concepts |
|--------|-------|:-----------------:|:----------:|:-----------------:|
| 3 | Context Engineering | 70% / 30% | 3,300 | 12 |
| 5 | Workflow Patterns (Chaining, Routing, Orchestrator-Worker) | 20% / 80% | 5,500 | 6 |
| 8 | Implementing ReAct from Scratch | 0% / 100% | 3,000 | 8 |
| 11 | Multimodal Processing (LLMs, RAG & Agents) | 30% / 70% | 5,200 | 10 |

**Test set**

| Lesson | Topic | Theory / Practice | Word Count | Distinct Concepts |
|--------|-------|:-----------------:|:----------:|:-----------------:|
| 2 | LLM Workflows vs. AI Agents | 60% / 40% | 3,900 | 10 |
| 6 | Agent Tools & Function Calling | 20% / 80% | 3,600 | 10 |
| 9 | RAG (Retrieval-Augmented Generation) | 100% / 0% | 3,200 | 12 |

This is **tiny**. Each "article" produces 6 episodes (one per preset) with a graded oracle reward. We deliberately do per-section inference (≈8 sections per article) so that the effective number of training examples is ~30× larger than the article count, but the underlying article diversity remains the bottleneck.

## 3. Reward function

For an article rendered with preset $p$:

$$
R(s, p) = \underbrace{0.20\,c_{c} + 0.20\,f_{l}}_{\text{ground-truth quality}}
       + \underbrace{0.30 \cdot c_{p} \cdot \left(0.60\,d_{e} + 0.40\,b_{e}\right)}_{\text{exploration value, gated by core preservation}}
       + \underbrace{0.30 \cdot \left(0.50\,g_{a} + 0.50\,r_{a}\right)}_{\text{user-intent adherence}}
       - \underbrace{0.02\,n_{r}(p)}_{\text{round cost}}
$$

| Symbol | Meaning |
|--------|---------|
| $c_c$ | core content fidelity vs. ground truth |
| $f_l$ | narrative flow score |
| $d_e, b_e$ | depth / breadth enhancement from exploration |
| $c_p$ | core preservation (multiplicative gate so exploration can't help if it dilutes the core) |
| $g_a, r_a$ | guideline adherence / research anchoring |
| $n_r(p)$ | rounds in preset $p$ ($\{0,1,2,2,3,3\}$) |

The oracle preset for an article is $p^\star = \arg\max_p R(s, p)$.

**Honest caveat**: the round cost coefficient ($0.02$) is small relative to typical coverage gains. If the grader over-weights coverage, the oracle systematically prefers more rounds — and conversely, if it under-weights it, the policy looks "over-exploratory" by comparison. Section 7 shows this matters.

## 4. Policy model and GRPO objective

**Backbone**: `Qwen3-4B`, **NF4 quantisation**, **QLoRA** adapter (rank 8, $\alpha = 8$, dropout 0.05) on attention + MLP projections. The base model is frozen; only ~6 M LoRA parameters are trained — a deliberately small adapter chosen to limit memorisation capacity given the tiny dataset.

**Training**: GRPO (Group Relative Policy Optimisation) — a critic-free variant of PPO that estimates advantages from intra-group reward dispersion.

For each prompt $x_g$ (one digest section) we have a fixed group of $G = 6$ pre-rolled episodes — one per preset — with offline rewards $\{R_{g,k}\}_{k=0}^{5}$. The single-token action is the next token $a \in \{\texttt{"0"}, \dots, \texttt{"5"}\}$, and the policy distribution over the 6 actions is obtained by re-normalising the LM head logits restricted to those six token IDs. Group-relative advantages are computed once at data-load time:

$$
\hat A_{g,k} = \frac{R_{g,k} - \mu_g}{\max(\sigma_g,\,\sigma_{\text{floor}})}, \quad
\mu_g = \tfrac{1}{6}\sum_j R_{g,j}, \quad
\sigma_g = \sqrt{\tfrac{1}{6}\sum_j (R_{g,j} - \mu_g)^2}
$$

with $\sigma_{\text{floor}} = 0.04$ to prevent advantage explosion on flat-reward groups (sections where all six presets score nearly identically).

### 4.1 Textbook GRPO loss (as published)

$$
\mathcal{L}_{\text{GRPO}}^{\text{full}}(\theta) = -\,\mathbb{E}\!\left[\,\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|y_i|}\sum_{t=1}^{|y_i|}
\min\!\bigl(\rho_{i,t}\hat A_i,\;\operatorname{clip}(\rho_{i,t},\,1-\epsilon,\,1+\epsilon)\,\hat A_i\bigr)\right]
\;+\;\beta\,\mathrm{KL}\!\bigl[\pi_\theta\,\Vert\,\pi_{\text{ref}}\bigr]
$$

with per-token importance ratio $\rho_{i,t}(\theta) = \pi_\theta(y_{i,t}\mid x, y_{i,<t}) / \pi_{\theta_{\text{old}}}(y_{i,t}\mid x, y_{i,<t})$ and PPO clip $\epsilon = 0.2$.

### 4.2 Our actual loss (single-token, no clip, with entropy bonus)

For each group $g$ with current policy $\pi_\theta(\cdot\mid x_g) \in \Delta^5$ over the six action tokens and reference policy $\pi_{\text{ref}}$ (the frozen base model, also restricted to the 6-action simplex):

$$
\mathcal{L}_g(\theta) = w_g \cdot \Bigl[\;
\underbrace{-\,\tfrac{1}{6}\sum_{k=0}^{5} \hat A_{g,k}\,\log\pi_\theta(k\mid x_g)}_{\mathcal{L}_{\text{PG}}^g}
\;+\;\beta\,\underbrace{\sum_{k=0}^{5}\pi_\theta(k\mid x_g)\bigl(\log\pi_\theta(k\mid x_g) - \log\pi_{\text{ref}}(k\mid x_g)\bigr)}_{\mathrm{KL}(\pi_\theta\,\Vert\,\pi_{\text{ref}})}
\;-\;\alpha\,\underbrace{\bigl(-\!\sum_{k=0}^{5}\pi_\theta(k\mid x_g)\log\pi_\theta(k\mid x_g)\bigr)}_{H(\pi_\theta)}
\;\Bigr]
$$

$$
\mathcal{L}(\theta) = \sum_{g} \mathcal{L}_g(\theta), \qquad \beta = 0.05,\ \alpha = 0.15,\ \sum_g w_g = 1
$$

### 4.3 Differences and why they are deliberate

| Component | Textbook GRPO (4.1) | Ours (4.2) | Why we deviate |
|---|---|---|---|
| Action space | $\|y_i\|$-token sequences | Single token (one of `"0"`…`"5"`) | Our action *is* a single digit; reasoning text is suppressed via `enable_thinking=False`. No autoregressive credit assignment needed. |
| Importance ratio $\rho$ | Per-token, vs. last-snapshot $\pi_{\theta_{\text{old}}}$ | None (set $\rho \equiv 1$) | The dataset is **offline and fixed** — we re-evaluate all 24 prompts every epoch. With no behaviour-policy mismatch and a single update per epoch, there is no $\theta_{\text{old}}$ to correct against. |
| PPO clip $\epsilon$ | $\operatorname{clip}(\rho, 1\pm\epsilon)$ | None | With $\rho \equiv 1$, the clip is a no-op. We rely on `max_grad_norm` (0.5) instead. |
| KL term | $\mathrm{KL}\!\bigl[\pi_\theta \Vert \pi_{\text{ref}}\bigr]$ over full vocab | Same form, but over the 6-action simplex only | Restricting the support to action tokens makes the KL signal a direct anti-collapse regulariser on the policy we actually deploy, not on token-level fluency. |
| Entropy bonus | Not standard | $-\alpha\,H(\pi_\theta)$ added | **The single most important change.** Without it the policy collapses to near-determinism around epoch 60–70 (observed $H \to 0.04$ in run 2). The bonus pulls entropy back to $H \in [0.10, 0.15]$ and recovers another ~0.01 E[R]. |
| Per-group weighting $w_g$ | None | $w_g = $ section-level mix (current run: simple normalised average per section, equal across articles) | Section-level training requires a choice; the simple average is the lowest-variance option for our 29-section dataset. See §12.1 for the regret-hybrid alternative. |

**Why the simpler form is the right choice *for this dataset*.** Each of the textbook components — importance ratio, clip, value head, sequence-level loss — exists to handle a specific failure mode of large-scale online RL (off-policy bias, exploding policy steps, high-variance returns, long-horizon credit). With $G = 6$ pre-rolled deterministic actions per group and 29 groups total, **none of those failure modes apply**, and each extra term contributes variance without benefit. The two regularisers we *do* keep (KL to reference, entropy bonus) target the failure mode that actually occurred in our training runs: deterministic collapse on a tiny action space.

**Hyperparameter history.** Run 1 ($\beta=0.10,\ \alpha=0.05$): trained-set E[R] $= 0.775$, but $H$ collapsed to $0.05$ at epoch 70 and never recovered. Run 2 ($\beta=0.05,\ \alpha=0.15$): $H$ collapsed at the same epoch but recovered to $0.10$–$0.15$, final E[R] $= 0.7765$ (91.2 % of uniform→oracle gap closed). Best checkpoint: `task_20260422_114127/best`. Section 8 documents what that headline number does *not* tell you.

**Why GRPO and not PPO**: with only ~29 training groups, training a value head is a recipe for variance. Group-relative advantages are zero-mean by construction and need no critic.

## 5. Inference pipeline — Stage 1 (RL aggregator)

The article digest is split into sections; each section gets its own inference pass. Per-section preset distributions $\mathbf{q}^{(s)} \in \Delta^5$ are aggregated by **word-count-weighted vote**:

$$
\mathbf{p}_{\text{agg}} = \frac{\sum_s w_s\,\mathbf{q}^{(s)}}{\sum_s w_s}, \qquad
w_s = \text{wordcount}(s), \qquad
p_{\text{vote}} = \arg\max_k\,p_{\text{agg},k}
$$

Confidence and uncertainty:

$$
\text{conf} = \max_k p_{\text{agg},k}, \qquad
H = -\!\sum_k p_{\text{agg},k}\log_2\bigl(p_{\text{agg},k} + \varepsilon\bigr)\ \text{[bits]}
$$

with thresholds $H_{\text{high}} = 1.5$, $H_{\text{low}} = 0.5$, $\text{conf}_{\text{strong}} = 0.70$.

### Entropy-gated floor correction

Short intro sections were dominating the vote and pulling the aggregate toward P0–P2 even when a deep technical section clearly demanded more exploration. We add a floor only when the model is **also confident**:

$$
p_{\text{floor}} = \max_s\,\arg\max_k q_k^{(s)}
$$

$$
p_{\text{final}} =
\begin{cases}
\max(p_{\text{vote}},\, p_{\text{floor}}) & \text{if } p_{\text{vote}} \le 2 \ \text{and}\ p_{\text{floor}} > p_{\text{vote}} \ \text{and}\ H \le 1.5 \\
p_{\text{vote}} & \text{otherwise}
\end{cases}
$$

The entropy gate prevents the floor from over-firing when the model is genuinely uncertain — in that regime we'd rather defer to Stage 2.

## 6. Inference pipeline — Stage 2 (Grok 4.2 planner)

The RL output by itself is a 6-way distribution over a categorical preset; it has no native way to read the article guideline. We chain a **Grok 4.2 reasoning** call inside the same MCP tool. Grok sees:

1. The RL aggregate (preset, confidence, entropy, floor flag, per-section signals).
2. The full `article_guideline.md`.
3. The `## 3. Overall Gap Profile` section extracted from the exploitation digest.

It is instructed to (a) explicitly state agreement/disagreement with the RL preset, (b) only override when the guideline or gap profile gives a concrete reason, and (c) emit a fenced JSON block: `{preset, name, reasoning, override, override_reason}`. The tool returns `grok_recommendation` as the authoritative field, with a graceful fallback to `rl_recommendation` if the API key is missing or JSON parsing fails.

We tried Grok-4.1-fast as an outer mcp-agent orchestrator first — it returned `None` on long contexts, so we moved the planner inside the tool and switched to Grok 4.2, which handles the longer prompt reliably.

## 7. Test-set results

Three held-out articles, evaluated end-to-end (digest → RL → Grok):

| Article | RL preset | RL conf | RL H | Grok preset | Override? | Chosen | Oracle | Verdict |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| `02_workflows_vs_agents` | P3 | 39 % | 1.94 | P3 | no | P3 | **P4** | NEAR (–1) |
| `06_tools`               | P2 | 84 % | 0.71 | P2 | no | P2 | **P1** | NEAR (+1) |
| `09_RAG`                 | P2 | 51 % | 1.76 | P2 | no | P2 | **P1** | NEAR (+1) |

**Aggregate**:

$$
\text{Exact} = 0/3 = 0\%,\qquad
\text{Exact + Near} = 3/3 = 100\%,\qquad
\overline{|\,p_{\text{chosen}} - p^\star\,|} = 1.0
$$

Per-preset rewards for the RL+Grok pipeline — `02_workflows_vs_agents` and `09_RAG` miss by ≤0.032, but `06_tools` carries a 0.163 penalty:

| Article | $R(p^\star)$ | $R(p_{\text{chosen}})$ | $\Delta R$ |
|---------|:--:|:--:|:--:|
| `02_workflows_vs_agents` | 0.7571 (P4) | 0.7400 (P3) | 0.017 |
| `06_tools`               | 0.6513 (P1) | 0.4880 (P2) | 0.163 |
| `09_RAG`                 | 0.6264 (P1) | 0.5943 (P2) | 0.032 |

### Grok-only baseline — test set (3-way mode comparison)

A post-hoc `--grok-only` experiment bypasses Stage 1 entirely: Grok 4.2 reasons from the article guideline and gap profile with no RL signal. Each mode was run as a separate end-to-end invocation; article `02_workflows_vs_agents` shows within-run RL variance ($H = 1.94$, near-uniform between P3 and P4 across runs).

| Article | Oracle | RL-only | RL+Grok | Grok-only |
|---------|:------:|:-------:|:-------:|:---------:|
| `02_workflows_vs_agents` | P4 | P4 (Δ 0) | P3 (Δ −0.017) | P3 (Δ −0.017) |
| `06_tools`               | P1 | P2 (Δ −0.163) | P2 (Δ −0.163) | **P5** (Δ −0.105) |
| `09_RAG`                 | P1 | P2 (Δ −0.032) | P2 (Δ −0.032) | **P1** (Δ 0) |

| Mode | avg $\Delta R$ | worst $\Delta R$ |
|------|:--------------:|:----------------:|
| RL-only   | −0.065 | −0.163 |
| RL+Grok   | −0.071 | −0.163 |
| Grok-only | **−0.041** | **−0.105** |

### Grok-only baseline — training set

The same `--grok-only` run was also applied to all four training articles to check whether Grok's apparent test-set advantage holds in-distribution. Grok-only choices and oracle presets:

| Article | Oracle | $R(p^\star)$ | Grok-only | $R(p_{\text{Grok}})$ | $\Delta R$ | Verdict |
|---------|:------:|:------------:|:---------:|:--------------------:|:----------:|:-------:|
| `03_context_engineering` | P1 | 0.6692 | P3 | 0.5213 | −0.148 | **MISS** (gap=2) |
| `05_workflow_patterns`   | P2 | 0.7012 | P3 | 0.6427 | −0.059 | NEAR |
| `08_react_practice`      | P2 | 0.5702 | P3 | 0.4950 | −0.075 | NEAR |
| `11_multimodal`          | P3 | 0.7336 | P2 | 0.5386 | −0.195 | NEAR |

Grok-only reasoning summaries:
- **`03_context_engineering`** (P3 chosen): "18 depth gaps vs 15 breadth, hands-on needs (Mermaid diagrams, healthcare prompts, LangGraph) require depth-first then breadth." — Over-explored by 2 presets vs oracle P1.
- **`05_workflow_patterns`** (P3 chosen): "Depth gaps dominate implementation specifics (Gemini SDK, asyncio, routing); strong query saturation suggests 2 rounds sufficient." — 1 over.
- **`08_react_practice`** (P3 chosen): "18 depth gaps (notebook setup, outputs) + 15 breadth; key insight calls for 2–3 new queries; depth-first then breadth matches clustered gaps." — 1 over.
- **`11_multimodal`** (P2 chosen): "22 depth vs 17 breadth concentrated in visuals/notebooks/GCS; balanced round first then depth." — 1 under. Despite being only a 1-preset miss, the reward gap (ΔR = −0.195) is the single worst result in the entire dataset because the 3rd exploration round delivers outsized value for this article.

**Combined Grok-only summary across all 7 articles:**

| Split | EXACT | NEAR | MISS | avg $\Delta R$ | worst $\Delta R$ |
|-------|:-----:|:----:|:----:|:--------------:|:----------------:|
| TRAIN (4) | 0 | 3 | 1 | −0.119 | −0.195 |
| TEST  (3) | 1 | 2 | 0 | −0.041 | −0.105 |
| **ALL (7)** | **1** | **5** | **1** | **−0.086** | **−0.195** |

The test-set advantage for Grok-only (avg −0.041) does not generalise: across all 7 articles its average ΔR is −0.086, worse than RL-only (−0.065) and comparable to RL+Grok (−0.071). The test set happened to contain `09_RAG` — an unusually easy P1 case with a self-describing "already saturated" gap profile — which inflated Grok-only's apparent performance. The **consistent pattern across both splits** is that Grok over-explores P1-oracle articles with alarming gap profiles (`03_context_engineering` MISS gap=2; `06_tools` MISS gap=4), while the RL anchor keeps all RL-based modes within 1 preset of oracle on every article.

## 8. Section-level metric signal analysis

The nine sub-scores composing the reward $R(s, p)$ were recorded independently for every episode (`episodes/*/scores.json`). The analysis below covers all 42 episodes — 24 training (L03, L05, L08, L11) and 18 test (L02, L06, L09).

### 8.1 Per-lesson means

| Lesson | Set | core\_content | flow | structure | depth\_enh | breadth\_enh | core\_pres | guideline\_adh | research\_anch | golden\_src |
|---|---|---|---|---|---|---|---|---|---|---|
| L02 | TEST  | 0.952 | 0.738 | 0.286 | 0.476 | 0.262 | 0.976 | 0.833 | 1.000 | 1.000 |
| L03 | TRAIN | 0.874 | 0.565 | 0.270 | 0.293 | 0.180 | 0.930 | 0.813 | 0.979 | 1.000 |
| L05 | TRAIN | 0.983 | 0.567 | 0.583 | 0.467 | 0.233 | 1.000 | 0.901 | 0.979 | 1.000 |
| L06 | TEST  | 0.850 | 0.550 | 0.433 | 0.383 | 0.167 | 1.000 | 0.537 | 0.944 | 1.000 |
| L08 | TRAIN | 0.758 | 0.439 | 0.212 | 0.273 | 0.106 | 0.803 | 0.840 | 1.000 | 1.000 |
| L09 | TEST  | 0.905 | 0.405 | 0.429 | 0.452 | 0.095 | 1.000 | 0.722 | 0.944 | 1.000 |
| L11 | TRAIN | 0.926 | 0.778 | 0.630 | 0.444 | 0.185 | 1.000 | 0.646 | 0.958 | 1.000 |

Set aggregates and deltas:

| Split | core\_content | flow | structure | depth\_enh | breadth\_enh | core\_pres | guideline\_adh | research\_anch | golden\_src |
|---|---|---|---|---|---|---|---|---|---|
| TRAIN (24) | 0.885 | 0.587 | 0.424 | 0.369 | 0.176 | 0.933 | 0.800 | 0.979 | 1.000 |
| TEST (18)  | 0.902 | 0.564 | 0.383 | 0.437 | 0.175 | 0.992 | 0.698 | 0.963 | 1.000 |
| Δ test−train | +0.017 | −0.023 | −0.041 | **+0.068** | −0.001 | **+0.059** | **−0.102** | −0.016 | 0.000 |

Per-lesson within-preset standard deviations (σ across 6 presets):

| Lesson | Set | core\_content | flow | structure | depth\_enh | breadth\_enh | core\_pres | guideline\_adh | research\_anch |
|---|---|---|---|---|---|---|---|---|---|
| L02 | TEST  | 0.074 | 0.229 | **0.286** | 0.195 | 0.190 | 0.058 | 0.211 | 0.000 |
| L03 | TRAIN | 0.079 | 0.089 | 0.144 | 0.095 | 0.162 | 0.084 | 0.131 | 0.051 |
| L05 | TRAIN | 0.041 | 0.266 | **0.293** | 0.197 | 0.163 | 0.000 | 0.086 | 0.051 |
| L06 | TEST  | 0.123 | 0.198 | 0.151 | 0.194 | 0.163 | 0.000 | 0.237 | 0.093 |
| L08 | TRAIN | 0.110 | 0.106 | 0.074 | 0.163 | 0.106 | 0.037 | 0.145 | 0.000 |
| L09 | TEST  | 0.074 | 0.058 | **0.000** | **0.292** | 0.117 | 0.000 | 0.228 | 0.136 |
| L11 | TRAIN | 0.091 | 0.099 | 0.240 | 0.122 | 0.219 | 0.000 | 0.279 | 0.065 |

### 8.2 Core fidelity (`core_content` + `core_preservation`)

Near-saturated on both sets — not a useful differentiator. `core_content` is high everywhere (TRAIN 0.885, TEST 0.902); the test advantage is an artefact of L08, the only lesson below 0.85 (0.758), being in the training set. `core_preservation` approaches 1.000 in the test set (0.992); train is pulled down by L08 alone (0.803). **L08 is a systematic outlier on both core fidelity metrics** — the L08 guideline imposes more demanding or atomic content requirements than all other lessons.

`golden_source_priority` is 1.000 with σ = 0.000 everywhere — **entirely saturated, zero RL training signal**.

### 8.3 Structural quality (`flow` + `structure`)

Highest noise, widest variance, primary area of underperformance. `flow` is statistically tied across sets (0.587 train, 0.564 test), but the failure modes differ sharply:

- **L09 (RAG)**: flow = 0.405, σ = 0.058 — low *and* stable across all 6 presets, implying the failure is structural to the topic rather than generation noise.
- **L02 (Workflows)**: flow = 0.738 — the strongest flow score in the dataset, comparable to the best training lesson (L11: 0.778).
- **L08**: flow = 0.439, consistent with its overall underperformance pattern.

`structure` is the weakest absolute metric across both sets (TRAIN 0.424, TEST 0.383) and the noisiest within-lesson signal:

- L02 structure σ = 0.286 — highest within-lesson variance of any metric × lesson combination; preset4 scored 0.857 while five others averaged 0.143.
- L05 structure σ = 0.293 — range 0.3–1.0; preset1 achieved a perfect 1.0.
- **L09 structure**: σ = 0.000 — every preset scored exactly 0.4286. This lock-step behaviour implies the RAG rubric fixes the structure score independent of exploration choice, making it non-informative as an RL signal for that topic.
- **L11** is the structural high-water mark in training (0.630, σ = 0.240).

### 8.4 Enhancement signals (`depth_enh` + `breadth_enh`)

`depth_enh` is the only metric where test meaningfully outperforms train (+0.068). `breadth_enh` is a universal weak spot.

**`depth_enhancement`** (TEST 0.437 vs. TRAIN 0.369): the gap is driven by L02 (0.476) and L09 (0.452) outpacing L03 (0.293) and L08 (0.273). Within L09 the variance is extreme (σ = 0.292): preset5 scored 0.857 — the highest depth score in the entire dataset — while preset0 scored 0.0. This is the most unpredictable metric in the dataset.

**`breadth_enhancement`**: universally low (~0.175) with **no meaningful gap between train and test** (−0.001). Every lesson in every split produces scores clustered near or below 0.25. This is the most consistently underperformed metric and the clearest signal of a **systematic capability gap** that is independent of topic — it is a model behaviour, not a rubric artefact.

### 8.5 User intent (`guideline_adh` + `research_anch` + `golden_src`)

`guideline_adherence` shows the **largest train/test delta in the dataset** (−0.102):

- **L06 (Tools)**: guideline_adh = 0.537, σ = 0.237 — the weakest lesson overall. Preset3 scored 0.222, the lowest guideline adherence score in the entire dataset. High variance means occasional strong episodes exist but the behaviour is unreliable.
- **L11 (Multimodal, training)**: 0.646, σ = 0.279 — despite being a training lesson, presets 2 and 5 scored 0.25 and 0.50 respectively. The model has not robustly learned guideline adherence for this topic.
- **L05** is the guideline adherence leader (TRAIN 0.901).

`research_anchoring` is high and stable (TRAIN 0.979, TEST 0.963); the test-set drop is driven by a single L09 episode scoring 0.667.

`golden_source_priority`: 1.000, σ = 0.000 everywhere. Saturated — no RL signal.

### 8.6 Signal quality summary

| Finding | Metrics involved | Severity |
|---|---|---|
| L08 systematic underperformance — both core fidelity metrics below all other lessons | `core_content`, `core_preservation`, `flow` | High — may need more L08-type training examples or revised reward shaping |
| `breadth_enh` universal failure — near-zero variance across all 42 episodes | `breadth_enh` | High — current reward signal does not differentiate good vs. bad breadth behaviour |
| `guideline_adh` train/test gap (−10 pp) — better calibrated on seen topics | `guideline_adh` | Medium — expected generalisation gap; L06 (0.537) is concerningly low for a test article |
| `structure` + `depth_enh` have highest within-lesson variance — noisy RL signal | `structure`, `depth_enh` | Medium — episodes within the same lesson diverge widely; RL updates are high-variance |
| L09 lock-step structure scores (σ = 0.000) across all presets | `structure` | Low-medium — RAG rubric may be too narrow; no discriminative signal between presets |
| `golden_src` + `core_pres` (test) saturated — zero differentiation | `golden_src`, `core_pres` | Low — consider harder negatives or upweighting under-utilised metrics |

## 9. Honest analysis

### 9.1 The headline metric was misleading

During training the model reached E[R] = 0.7765 against an oracle ceiling of 0.7907 — a 91.2 % gap closure that looks impressive. A direct **section-level top-1 accuracy** evaluation against the per-section oracle tells a very different story:

| Split | Section accuracy | Article accuracy (raw section vote) |
|---|:---:|:---:|
| Train (4 articles, 29 sections) | **19/29 = 66 %** | 1/4 = 25 % |
| Test  (3 articles, 20 sections) | **1/20 = 5 %**  | 0/3 = 0 % |
| Random baseline (1/6) | 16.7 % | 16.7 % |

Test section accuracy is **below the random baseline** (5 % vs. 16.7 %). The 91.2 % E[R] number measured how well the policy reproduced the *training* reward distribution — a quantity the model has enough capacity to memorise outright (29 × 6 = 174 reward values vs. ~6 M trainable LoRA parameters).

The end-to-end pipeline still produced 100 % NEAR on the test set (Section 7) because **two downstream stages cushion section-level errors**: (a) the word-count-weighted vote averages over 6–8 sections, smearing individual mistakes, and (b) the Grok planner sometimes overrides. Both effects are real, and both make the system look better than its underlying section-level policy actually is.

### 9.2 The smoking gun: `06_tools`

On `06_tools` the model emitted **P2 for 7 of 8 sections regardless of content** (the final survey section fell to P0, but the word-count-weighted article vote still returned P2 by plurality). P2 was the most common section-level oracle in the training set; the model collapsed to a frequency prior the moment it left the training distribution. This is a textbook overfit signature, not a calibration issue — and it is exactly what a 6 M-parameter adapter with 29 distinct training prompts is expected to do.

### 9.3 Where the article-level error budget actually goes

- **Bias direction**: 2 of 3 article-level errors are **over-exploration** (chose 1 round more than oracle). The cost term $-0.02\,n_r$ may be under-weighting the budget penalty relative to the grader's coverage-quality terms; equally plausibly, training-set distribution skew (zero P0/P1-oracle articles) has shifted the prior.
- **`06_tools` is the worst case** (Δ = 0.163). RL was confident (84 %, $H = 0.71$) and Grok deferred — exactly the configuration where Stage 2 cannot rescue a confident-but-wrong Stage 1.
- **`02_workflows_vs_agents`** under-explored by 1 round; RL was uncertain ($H = 1.94$), Grok confirmed P3 anyway. The floor heuristic didn't fire (vote was already P3). A higher-entropy regime where Grok is empowered to bump up by one round would likely have caught this.
- **RL is a variance reducer for Grok**: on the test set Grok-only had the best average ΔR (−0.041), but this advantage disappears when training articles are included (all-7 avg −0.086 for Grok-only vs −0.065 for RL-only). The test set happened to contain `09_RAG`, an unusually easy P1 case. Across the full 7 articles Grok produces 2 catastrophic misses (gap=2 and gap=4) on P1-oracle articles where the gap profile reads "alarming"; RL anchors near P2 on the same articles, keeping the worst-case ΔR bounded.

### 9.4 What "the model is barely above random per-section" reveals

It does **not** invalidate the pipeline. It clarifies what the pipeline is doing: the RL stage has learned a coarse, distribution-aware *prior* (cluster around P2–P3 with section-length sensitivity), and the aggregation + Grok stages convert that prior into article-level decisions that are reliably within 1 of oracle. This is a useful piece of infrastructure — but calling it a "learned policy" overstates what the gradients actually accomplished. The honest framing: **we have a well-engineered ensemble whose RL component is approximately a frequency prior**.

- **Sample size**: $n=3$ test articles is not statistically meaningful. The 100 % near-accuracy claim is real but should be reported with that caveat front and centre.
- **No exact hits on the test set** (the one training exact hit — `11_multimodal` P3→P3 — reflects in-distribution memorisation): the end-to-end pipeline returns P3/P2/P2 for the three test articles and misses all three P1-oracle articles by 1–2 presets. With train articles biased toward depth-heavy content (`react_practice`, `multimodal`), the systematic over-exploration toward P2–P3 is consistent with the prior-collapse interpretation above.

## 10. Regret-hybrid ablation — loss weighting improves sections, not articles

§9 traced the train/test gap to a 6 M-parameter LoRA adapter memorising 29 training prompts. A natural counter-argument is that the loss is at fault — the simple per-section average over-spends gradient on uninformative sections (§12.1 sketches the alternative). We ran a controlled ablation with `--section-weight regret-hybrid` (loss weight $\propto \text{wordcount}(g) \cdot (\max_k R_{g,k} - \mu_g)$, see §12.1) on the same training data, same epochs, same hyperparameters. Hypothesis: focusing gradient on high-regret sections should improve generalisation by spending capacity where preset choice actually matters.

**Result: section-level metrics improved; article-level test accuracy did not.**

| Split | Section accuracy | Article accuracy | Trained E[R] | Gap closed |
|---|:---:|:---:|:---:|:---:|
| Simple average (§9.1)        | 19/29 train, 1/20 test | 1/4 train, 0/3 test | 0.7765 | 91.2 % |
| Regret–hybrid (this section) | 23/29 train, 4/20 test | 2/4 train, 0/3 test | 0.7862 | 97.2 % |

Regret-hybrid improved every metric except article-level test accuracy, which remained at 0/3.

### 10.1 Per-article breakdown — failure mode preserved

| Article | Split | Sec acc | Article (oracle → predicted) |
|---|:---:|:---:|:---:|
| `03_context_engineering` | TRAIN | 7/8 (88 %) | P1 → P3 ✗ |
| `05_workflow_patterns`   | TRAIN | 5/7 (71 %) | P2 → P2 ✓ |
| `08_react_practice`      | TRAIN | 4/6 (67 %) | P2 → P4 ✗ |
| `11_multimodal`          | TRAIN | 7/8 (88 %) | P3 → P3 ✓ |
| `02_workflows_vs_agents` | TEST  | 2/6 (33 %) | P4 → P2 ✗ |
| `06_tools`               | TEST  | **0/8 (0 %)** | P1 → P2 ✗ |
| `09_RAG`                 | TEST  | 2/6 (33 %) | P1 → P3 ✗ |

The two signature failures are preserved exactly:

- **`06_tools` collapse to all-P2** (8/8 sections), the same frequency-prior emission documented in §9.2.
- **Systematic over-exploration on P1-oracle articles**: `03_context_engineering` (P1→P3, gap=2), `09_RAG` (P1→P3, gap=2), `06_tools` (P1→P2, gap=1). Three of three P1-oracle articles miss in the same over-shoot direction.

**Comparison with the simple-average baseline (§9.1):**

| Article | Split | Simple avg sec acc | Regret-hybrid sec acc | Article-level change |
|---|:---:|:---:|:---:|:---|
| `03_context_engineering` | TRAIN | 4/8 (50 %) | 7/8 (88 %) | P1→P3 ✗ in both |
| `05_workflow_patterns`   | TRAIN | 5/7 (71 %) | 5/7 (71 %) | **P2→P4 ✗ → P2→P2 ✓** (only flip) |
| `08_react_practice`      | TRAIN | 4/6 (67 %) | 4/6 (67 %) | P2→P4 ✗ in both |
| `11_multimodal`          | TRAIN | 6/8 (75 %) | 7/8 (88 %) | P3→P3 ✓ in both |
| `02_workflows_vs_agents` | TEST  | 0/6 (0 %)  | 2/6 (33 %) | both ✗ (P4→P3 vs P4→P2) |
| `06_tools`               | TEST  | 0/8 (0 %)  | 0/8 (0 %)  | P1→P2 ✗ in both |
| `09_RAG`                 | TEST  | 1/6 (17 %) | 2/6 (33 %) | P1→P5 ✗ → **P1→P3 ✗** (gap 4→2) |

The most striking contrast is `09_RAG`: the simple-average model's word-count-weighted vote was pulled to P5 (gap=4 — the worst single miss in the dataset) because the high-word-count Introduction section emitted P5; regret-hybrid reduced this to P3 (gap=2). Conversely, regret-hybrid is marginally worse on `06_tools`: simple averaging produced 7/8 P2 predictions with one P0 outlier in the final survey section; regret-hybrid collapses uniformly to all-P2.

### 10.2 What this tells us about loss weighting and data

**Loss weighting matters — at the section level.** Concentrating gradient mass on high-regret, content-rich sections produced genuine improvements: train section accuracy rose 13 pp (66 %→79 %), test section accuracy rose 15 pp (5 %→20 %), and E[R] improved by 0.01 (91.2 %→97.2 % gap closed). Two concrete changes stand out: `05_workflow_patterns` flipped from incorrect (P2→P4) to correct (P2→P2) at the article level — the only article-level flip between the two models — and `09_RAG`'s extreme P5 prediction (gap=4, worst miss in the dataset) pulled back to P3 (gap=2), halving the over-exploration penalty.

**But section-level gains do not propagate to article-level test accuracy.** Despite the improvements, the article-level test outcome is unchanged: 0/3. Getting more individual sections right is necessary but not sufficient to flip a test article when the model's frequency prior still dominates the word-count-weighted majority vote. All three test articles remain wrong, with the same directional bias: every P1-oracle test article is predicted above oracle. `06_tools` deepened its collapse (7/8 P2 → 8/8 P2 uniform), confirming that focused gradient weight on a high-regret training section accelerates memorisation of that pattern, not generalisation from it.

**The data bottleneck is still the binding constraint.** The root cause is unchanged: $n_{\text{train}} = 4$ topics with zero P0/P1-oracle articles (§9.3). Better loss weighting reshapes *how* the model fails within the distributional gap — less extreme section-level errors, better vote aggregation on some articles — but cannot eliminate the gap itself. No loss formulation can provide the gradient signal needed to generalise to P1-oracle test articles when such articles are absent from training.

**Cautionary note on interpreting the test improvement.** The 15 pp gain in test section accuracy corresponds to 3 additional correct sections across 20, concentrated on `02_workflows_vs_agents` (+2) and `09_RAG` (+1). The training curve shows E[R] making a sharper step around epoch 50 under regret-hybrid (vs. a smoother trajectory under simple averaging), suggesting the improvement may partly reflect sharper memorisation of the few high-weight training sections rather than deeper generalisation. The `06_tools` deepening is consistent with this interpretation.

**Decision.** Regret-hybrid is strictly better by every section-level metric and carries sound theoretical motivation (§12.1). Switch it to the active default (`--section-weight regret-hybrid`). The "roll back to simple averaging" conclusion from an earlier draft was based on the erroneous belief that both models produced identical results; with correct data, regret-hybrid is the better configuration. The article-level failure pattern is still the binding problem, and closing it requires more P0/P1-oracle training articles (§12, items 1 and 7) — not better loss design.

## 11. What's defensible vs. what isn't

**Defensible**:
- The two-stage architecture (RL aggregator + LLM planner) is well-motivated: the RL stage produces a calibrated *prior* over presets that anchors Grok's reasoning; Grok contextualises that anchor against the article guideline.
- Word-count weighting + entropy-gated floor is principled and ablation-friendly. The aggregation pipeline measurably reduces worst-case ΔR (Section 7) regardless of how good the underlying section-level policy is.
- The reward formula is explicit, the oracle is reproducible from `episodes/*/scores.json`, and the loss (§4.2) is implemented in ~10 lines without hidden machinery.
- Within-distribution **article-level** behaviour is conservative (always within 1 preset of oracle). The system does what it claims to do at the article level.
- The training procedure is reproducible end-to-end from a single command, with full resume state and per-epoch JSONL logs.

**Not yet defensible** — be upfront:
- $n_{\text{train}} = 4$, $n_{\text{test}} = 3$. We cannot claim generalisation from this.
- **The RL stage's section-level policy is approximately a frequency prior** (§9.1: 5 % test accuracy vs. 16.7 % random — *below* chance). The training E[R] of 0.7765 measured memorisation, not learning. The pipeline works because aggregation and Grok mask this; the underlying gradient updates have not produced a policy that generalises section-by-section.
- We have not run cross-validation across articles; train/test were chosen by topic intuition, not stratified sampling.
- The reward function's coefficients (especially the round cost $0.02$) were not swept; we don't know how sensitive the oracle ranking is to that choice.
- The Grok stage was added *after* training. The 3-way comparison (Section 7) shows RL+Grok does not improve over RL-only on this test set ($n=3$); the value of Stage 2 is Grok's ability to read the article guideline, but this cannot be evaluated at scale without more test articles.
- Both training runs collapsed to $H \approx 0.05$ at epoch 60–70 before the entropy bonus pulled them back. We don't know whether the recovery is robust or whether it depends on the exact $\alpha = 0.15$ value; we did not seed-sweep.

## 12. Roadmap

1. **More articles** — *the only fix that matters first.* §9.1 makes clear that no loss tweak, no coefficient sweep, and no architecture change will move the underlying section-level policy off random until the data bottleneck is broken. §10 confirms this empirically: regret-hybrid improves section accuracy (train 66 %→79 %, test 5 %→20 %) and E[R] (91.2 %→97.2 %), but article-level test accuracy remains 0/3 — the data bottleneck is binding at the metric that matters. Targets: 12–15 train + 5–7 test articles, ideally with stratified P0/P1 oracle coverage. Even 8 train + 4 test would let us run leave-one-out CV.
2. **Synthesised digests** as a stop-gap. The reward formula is deterministic given seven binary judge scores; if we can synthesise plausible digest+score pairs (e.g., by perturbing existing reasoning JSON), we can grow the dataset without re-running the expensive episode pipeline. Risk: the model learns the perturbation distribution rather than the underlying policy. Useful only as a regulariser, not as a primary signal.
3. **Reward sensitivity sweep**: vary the round-cost coefficient over $\{0.01, 0.02, 0.05, 0.10\}$ and check oracle stability. With current data this is a 7-article sensitivity check, not a tuning experiment.
4. ~~**A/B Grok vs. no-Grok**~~ **Done — extended to 3-way comparison across all 7 articles** (RL-only / RL+Grok / Grok-only, see Section 7). Grok-only's test-set advantage (avg −0.041) does not hold across the full dataset (avg −0.086); it produces 2 catastrophic misses on P1-oracle articles. RL-only is the best all-7-article mode by average ΔR and worst-case ΔR is bounded by the RL anchor on every article.
5. **Calibration**: check whether `confidence` correlates with empirical accuracy across articles. With $n=7$ this is descriptive only.
6. **Targeted fix for `06_tools`-style cases**: have Grok step *down* from a high-confidence RL recommendation when the gap profile reports `query_saturation = high` and `depth_gaps ≤ breadth_gaps`. This is a hand-coded rule, not learning — appropriate at $n = 7$.
7. **Address P0/P1 training coverage gap.** The training set contains zero P0- or P1-oracle articles; the systematic over-exploration bias traces directly to this distribution mismatch. Candidate articles for augmentation: those with `query_saturation = high` and `depth_gaps ≤ breadth_gaps` in their digest. Adding even 2–3 such articles is the highest-leverage next experiment before any further hyperparameter or architecture changes.

### 12.1 Section weighting — the regret–hybrid alternative

The current section-level training treats every section equally within an article (simple average of $\mathcal{L}_g$, normalised so each article contributes $1/N_{\text{articles}}$). An obvious extension is a per-section weight that combines two independent signals:

1. *How much does this section represent the article?* — natural proxy is **word count** $\ell_g$.
2. *How much does the preset choice actually matter for this section?* — answered by **expected regret** of uniform-random selection, $\Delta_g = \max_k R_{g,k} - \mu_g$.

The proposed hybrid weight is

$$
w_g^{\text{rh}} \;\propto\; \ell_g \cdot \Delta_g, \qquad \sum_{g \in \text{article}\,a} w_g^{\text{rh}} = \frac{1}{N_{\text{articles}}}
$$

**Why regret rather than reward variance.** A symmetric measure like $\sigma_g$ over-weights sections where one preset is uniquely *bad*; regret is upside-aware and measures only the gain from picking right over picking uniformly — exactly what GRPO optimises. A section where every preset is mediocre carries weight $\approx 0$; a section with one clear winner carries high weight even if it is short.

**Empirical result (§10).** The controlled ablation shows regret-hybrid is strictly better by every section-level metric: train section accuracy 66 %→79 %, test section accuracy 5 %→20 %, E[R] 91.2 %→97.2 % gap closed. The one article-level flip is `05_workflow_patterns` (P2→P4 ✗ → P2→P2 ✓), and `09_RAG`'s worst-case miss shrank from P5 (gap=4) to P3 (gap=2). However, article-level test accuracy is unchanged at 0/3: the data bottleneck prevents section-level gains from aggregating to article-level generalisation. The `06_tools` uniform P2 collapse deepened slightly (7/8 → 8/8), consistent with concentrated gradient accelerating memorisation of high-regret training sections in the small-data regime.

**Current status**: regret-hybrid is the active default (`--section-weight regret-hybrid`). Its advantage over simple averaging will become more pronounced as $N_{\text{train articles}}$ grows and high-regret sections diversify beyond the current 4-article training set.

---

## 13. Default LLM model inventory

All model strings below are the *defaults* at time of writing; each can be overridden via environment variables or YAML config.

### 13.1 Research agent MCP server (`research_agent_local/mcp_server/`)

Configured in `config/settings.py` and the `_DIGEST_MODEL` / `_PLANNER_MODEL` constants in `tools/predict_exploration_preset_tool.py`.

| Role | Settings field / constant | Default model key | Resolved model ID |
|------|--------------------------|:-----------------:|-------------------|
| Query generation & deduplication | `query_generation_model` | `grok-4.20-reasoning` | `xai:grok-4.20-0309-reasoning` |
| Source selection (keep / scrape) | `source_selection_model` | `grok-4.20-reasoning` | `xai:grok-4.20-0309-reasoning` |
| Tavily search enhancement | `search_enhancement_model` | `grok-4-1-fast-non-reasoning` | `xai:grok-4-1-fast-non-reasoning` |
| Content deduplication | `content_dedup_model` | `grok-4-1-fast-reasoning` | `xai:grok-4-1-fast-reasoning` |
| Web scraping + cleaning (all 3 scrape tools) | `scraping_model` | `gemini-2.5-flash` | `google_genai:gemini-2.5-flash` |
| YouTube transcription | `youtube_transcription_model` | `gemini-2.5-flash` | `google_genai:gemini-2.5-flash` |
| Exploitation digest summariser (preset tool) | `_DIGEST_MODEL` | `grok-4-1-fast-reasoning` | `xai:grok-4-1-fast-reasoning` |
| RL preset predictor — Stage 1 | local model | Qwen3-4B + LoRA (NF4) | local inference subprocess |
| Grok planner — Stage 2 | `_PLANNER_MODEL` | `grok-4.20-0309-reasoning` | `xai:grok-4.20-0309-reasoning` |

### 13.2 Writing workflow nodes (`writing_workflow/`, default config `configs/course.yaml`)

| Node (config key) | Role | Default model ID | Temperature |
|-------------------|------|-----------------|:-----------:|
| `generate_media_items` | MediaGeneratorOrchestrator — plans diagrams/media | `google_genai:gemini-2.5-flash` | 0.0 |
| `generate_media_items → mermaid_diagram_generator` | MermaidDiagramGenerator (tool node) | `google_genai:gemini-2.5-flash` | 0.0 |
| `write_article` | ArticleWriter — initial draft | `google_genai:gemini-2.5-pro` | 0.7 |
| `integrate_exploration` | ArticleWriter — exploration integration pass | `google_genai:gemini-2.5-pro` | 0.7 |
| `review_article` | ArticleReviewer — full-article review | `google_genai:gemini-2.5-pro` | 0.0 |
| `edit_article` | ArticleEditor — guided revision | `google_genai:gemini-2.5-pro` | 0.1 |
| `review_selected_text` | ArticleReviewer — section-level review | `google_genai:gemini-2.5-pro` | 0.0 |
| `edit_selected_text` | ArticleEditor — section-level edit | `google_genai:gemini-2.5-pro` | 0.1 |

### 13.3 Writing workflow evaluation metrics (`writing_workflow/src/brown/evals/metrics/`)

Both metric classes default to `SupportedModels.GOOGLE_GEMINI_25_FLASH` (`google_genai:gemini-2.5-flash`).

| Metric class | JSON prefix | Sub-scores | Default model |
|---|---|---|---|
| `FollowsGTMetric` | `ground_truth_` | `core_content`, `flow`, `structure`, `depth_enhancement`, `breadth_enhancement`, `core_preservation` | `google_genai:gemini-2.5-flash` |
| `UserIntentMetric` | `user_intent_` | `guideline_adherence`, `research_anchoring`, `golden_source_priority` | `google_genai:gemini-2.5-flash` |

Note: `structure` and `golden_source_priority` are graded but are **not** terms in the reward formula $R(s, p)$ (§3); they are available as diagnostic signals only.