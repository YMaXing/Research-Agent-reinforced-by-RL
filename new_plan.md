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

# Article-level (First Draft Done, ready for test data)

downstream LLM pipeline aggregating section-level signals (see PHASE 0).

Detailed plan: [article_level_aggregator_plan.md](RL_researcher_writer_ymaxing/research_agent_local/training/article_level_aggregator_plan.md) + allowed / required as external_evidence_policy in "guideline_features.json".

Potential complements to the plan: extract helpful information from digests

# Guideline generation

need to be generalized beyond lesson articles (12 articles)

Candidates from TowardsAI's agentic course: 
1. Lesson 4: Structured Outputs
2. Lesson 7: Reasoning Planing
3. Lesson 13: Agent Frameworks Overview & Comparison
4. Lesson 14: LLM Agent System Design Considerations and Framework  
5. Lesson 29: Defining the Evaluation Processes and Metrics Theory
6. Lesson 31: Continuous Integration for AI Engineering

Candidates from Pinecone:
1. Hierarchical Navigable Small Worlds (HNSW) (https://www.pinecone.io/learn/series/faiss/hnsw/)

Candidates from QuantaMagazine:
1. Is Gravity Just Entropy Rising? Long-Shot Idea Gets Another Look. (https://www.quantamagazine.org/is-gravity-just-entropy-rising-long-shot-idea-gets-another-look-20250613/)
2. How Space and Time Could Be a Quantum Error-Correcting Code (https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103/#comments)
3. How the Bird Eye Was Pushed to an Evolutionary Extreme (https://www.quantamagazine.org/how-the-bird-eye-was-pushed-to-an-evolutionary-extreme-20260513/)
4. Insects and Other Animals Have Consciousness, Experts Declare (https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419/)
5. Two Twisty Shapes Resolve a Centuries-Old Topology Puzzle (https://www.quantamagazine.org/two-twisty-shapes-resolve-a-centuries-old-topology-puzzle-20260120/)