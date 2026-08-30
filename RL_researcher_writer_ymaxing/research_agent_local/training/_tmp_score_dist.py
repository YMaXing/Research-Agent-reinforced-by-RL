import sys
import json
import statistics
from pathlib import Path

sys.path.insert(0, '/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/research_agent_local/training')
import generate_episode_oracles as geo
import measure_replicate_noise as mrn

ARTICLE = 'Bird_Eye_Extreme'
BASES = mrn._BASES_DIR
TEST_EP = geo._TEST_EPISODES_DIR
NOISE = mrn._NOISE_EXPERIMENT_DIR

_raw_sec_ids = mrn._production_sec_ids(ARTICLE)
# digest lists each section twice (see measure_replicate_noise docstring); dedupe
# to the 4 real sections, preserving order, for a clean per-section tally.
prod_sec_ids = list(dict.fromkeys(_raw_sec_ids))
sec_norms = [geo._sec_id_to_norm(s) for s in prod_sec_ids]
arm_presets = mrn._arm_presets_for(ARTICLE)  # {'skip':[0],'light':[1],'standard':[2],'deep':[3]}

DIMS = ['ground_truth_core_content', 'ground_truth_flow', 'ground_truth_depth_enhancement',
        'ground_truth_breadth_enhancement', 'ground_truth_core_preservation', 'user_intent_guideline_adherence']
DIM_SHORT = {'ground_truth_core_content': 'cc', 'ground_truth_flow': 'fl',
             'ground_truth_depth_enhancement': 'de', 'ground_truth_breadth_enhancement': 'be',
             'ground_truth_core_preservation': 'cp', 'user_intent_guideline_adherence': 'ga'}

def episode_dir(draw, preset):
    if draw == 0:
        return TEST_EP / f"{ARTICLE}__preset{preset}"
    return NOISE / f"{ARTICLE}__replicate{draw}__preset{preset}"

# scores[arm][dim_short] = list of 12 binary scores (4 sections x 3 draws)
scores = {arm: {DIM_SHORT[d]: [] for d in DIMS} for arm in ('standard', 'light')}

for arm in ('standard', 'light'):
    preset = arm_presets[arm][0]
    for draw in (0, 1, 2):
        ep_dir = episode_dir(draw, preset)
        episode = geo._load_episode(ep_dir)
        for dim in DIMS:
            entries = episode.get(dim, [])
            for sec_idx, (sec_id, sec_norm) in enumerate(zip(prod_sec_ids, sec_norms)):
                sc = geo._get_score(entries, sec_norm, sec_idx)
                scores[arm][DIM_SHORT[dim]].append(sc)

print(f"Per-dimension binary-score summary, {ARTICLE} (n=12 per arm: 4 sections x 3 draws)\n")
print(f"{'dim':4s} {'standard mean':>14s} {'light mean':>11s} {'delta (std-light)':>18s}")
for short in ['cc', 'fl', 'de', 'be', 'cp', 'ga']:
    sm = statistics.mean(scores['standard'][short])
    lm = statistics.mean(scores['light'][short])
    print(f"{short:4s} {sm:14.3f} {lm:11.3f} {sm-lm:+18.3f}")
    print(f"     standard: {scores['standard'][short]}")
    print(f"     light:    {scores['light'][short]}")
