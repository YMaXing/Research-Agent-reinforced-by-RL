# Dataset

add the three variants of lesson 10 - memory

# Metric (Partly done, training set scores repaired,LLM judges improved but far from perfect)

repair metric and LLM judge flaws

# Reward (Done, no extra term added, 6 -> 4 presets, minimal variant's reward formula modified)

implement updated reward, breaking ties

# Digest (Done, along with the input to RL extracted from digests)

improve digest generation pipeline (see CHECKPOINT INFERENCE AND COMPRESSION)

# Section-level (Done, no need to pursue extreme section-level accuracy)

improve section-level accuracy by upgrading the training data and pipeline

# Article-level

downstream LLM pipeline aggregating section-level signals (see PHASE 0).

Detailed plan: [article_level_aggregator_plan.md](RL_researcher_writer_ymaxing/research_agent_local/training/article_level_aggregator_plan.md) + allowed / required as external_evidence_policy in "guideline_features.json".

Potential complements to the plan: extract helpful information from digests

# Guideline generation

need to be generalized beyond lesson articles