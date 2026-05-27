"""
Offline GRPO + QLoRA Training for Exploration Strategy Selection

Trains Qwen3-4B to select the optimal exploration preset
(skip / light / standard / deep) given exploitation digests as context.
Uses offline GRPO with oracle-based rewards derived from section_oracle.json.

Usage (from research_agent_local/training/):
    uv run python train_grpo.py --dry-run       # verify setup
    uv run python train_grpo.py                 # full training
    uv run python train_grpo.py --epochs 200 --lr 5e-5 --beta 0.1
    uv run python train_grpo.py --init-adapter ../../rl_training_data/checkpoints/tasks/task_id/best
    uv run python train_grpo.py --init-adapter ../../rl_training_data/checkpoints/tasks/task_id/latest
"""

import argparse
import json
import logging
import math
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import bitsandbytes as bnb
import torch
import torch.nn.functional as F
from peft import (
    LoraConfig,
    PeftModel,
    TaskType,
    get_peft_model,
    prepare_model_for_kbit_training,
)
from torch.utils.tensorboard import SummaryWriter
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# Shared preset vocabulary, system prompt, and per-section input builder.
# Imported here rather than duplicated; _rl_preset.py has no heavy dependencies.
from _rl_preset import (
    _RL_INPUT_SYSTEM,
    NUM_PRESETS,
    PRESET_NAMES,
    PRESET_ORDER,
    PRESET_ROUNDS,
    build_rl_input,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _THIS_DIR.parent               # research_agent_local/
_REPO_ROOT = _AGENT_DIR.parent              # RL_researcher_writer_ymaxing/
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_MODEL_DIR = _REPO_ROOT / "models" / "Qwen3-4B"
_OUTPUT_DIR = _REPO_ROOT / "rl_training_data" / "checkpoints"
_EVAL_DIR = _REPO_ROOT / "writing_workflow" / "inputs" / "evals" / "dataset" / "data"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
ARTICLES = [
    "02_workflows_vs_agents__var_minimal",
    "02_workflows_vs_agents__var_standard", "02_workflows_vs_agents__var_demanding",
    "03_context_engineering__var_minimal",
    "03_context_engineering__var_standard", "03_context_engineering__var_demanding",
    "05_workflow_patterns__var_minimal",
    "05_workflow_patterns__var_standard", "05_workflow_patterns__var_demanding",
    "06_tools__var_minimal",
    "06_tools__var_standard", "06_tools__var_demanding",
    "08_react_practice__var_minimal",
    "08_react_practice__var_standard", "08_react_practice__var_demanding",
    "09_RAG__var_minimal",
    "09_RAG__var_standard", "09_RAG__var_demanding",
    "10_memory_knowledge_access__var_minimal",
    "10_memory_knowledge_access__var_standard", "10_memory_knowledge_access__var_demanding",
    "11_multimodal__var_minimal",
    "11_multimodal__var_standard", "11_multimodal__var_demanding",
]

# Preset vocabulary and system prompt are imported from _rl_preset (see above):
#   NUM_PRESETS = 4
#   PRESET_NAMES  = {0: "skip", 1: "light", 2: "standard", 3: "deep"}
#   PRESET_ORDER  = {"skip": 0, "light": 1, "standard": 2, "deep": 3}
#   PRESET_ROUNDS = {"skip": 0, "light": 1, "standard": 2, "deep": 3}
#   _RL_INPUT_SYSTEM   — single KV-cache-friendly system prompt for all groups
#   build_rl_input(digest, sec_id)  — per-section user-message builder

# Active episode presets: 0=baseline(skip), 1=single_balanced(light),
# 3=depth_then_breadth(standard), 5=depth_breadth_depth(deep).
# Presets 2 (balanced_then_depth) and 4 (balanced_depth_breadth) are archived.
_EPISODE_PRESET_ROUNDS: dict[int, int] = {0: 0, 1: 1, 3: 2, 5: 3}
_EPISODE_NUM_PRESETS = 4

# Dimensions used in the reward formula (shared by both granularities)
_REWARD_DIMS = [
    "ground_truth_core_content",
    "ground_truth_flow",
    "ground_truth_depth_enhancement",
    "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation",
    "user_intent_guideline_adherence",
    "user_intent_research_anchoring",
]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class Group:
    """One article = one GRPO group with 6 preset samples."""

    name: str
    digest: str
    # Per-section guideline text extracted from article_guideline.md.
    # Empty for article-level groups; populated by load_section_groups().
    # Included in the model input to distinguish variant oracle signals.
    section_guideline: str = ""
    # Compact article context (word target + theory/practice + scope note).
    # Extracted from the preamble of article_guideline.md; empty string when
    # no guideline is available.  Stored here so tokenize_groups can assemble
    # the correct input format without re-reading the guideline file.
    guideline_preamble: str = ""
    input_ids: torch.Tensor | None = None
    rewards: list[float] = field(default_factory=list)
    advantages: torch.Tensor | None = None
    ref_log_probs: torch.Tensor | None = None
    best_preset_idx: int = 0
    hit_sigma_floor: bool = False
    # Preset indices whose reward is within sigma_floor of max(R).  Any of
    # these is an acceptable model prediction (near-tie acceptance).  Used in
    # top1_correct instead of exact best_preset_idx match.  Populated by
    # load_groups / load_section_groups.
    acceptable_idxs: list[int] = field(default_factory=list)
    # Loss weight for this group.  Set by load_groups / load_section_groups so
    # the training loop mirrors the word-count-weighted inference aggregation:
    #   article-level  -> equal (1 / num_articles)
    #   section-level  -> controlled by --section-weight (see load_section_groups)
    word_weight: float = 1.0
    # Raw reward std before sigma-floor clamping. Stored here so the weight
    # normalizer can use it for 'variance' and 'hybrid' weighting modes.
    raw_reward_std: float = 0.0
    # Expected regret of uniform-random preset selection: max(R) - mean(R).
    # Answers "how much does it matter that the policy learns the right preset
    # for this section?"  Unlike std, this is upside-aware: a section where
    # one preset is uniquely great scores higher than one with symmetric spread.
    # Used by the 'regret-hybrid' weighting mode.
    raw_reward_regret: float = 0.0


# ---------------------------------------------------------------------------
# Reward computation
# ---------------------------------------------------------------------------
def _compute_episode_reward(
    scores: dict,
    preset_id: int,
    variant_level: str = "standard",
    ) -> float:
    """Compute reward from scores.json using the variant-aware formula.

    Legacy function used by load_groups() for the old 6-preset episode-based
    training.  New section-level training uses compute_oracle_reward() instead.

    ``variant_level`` must be one of ``"minimal"``, ``"standard"``,
    ``"demanding"``.  Each variant emphasises different output properties:

    * **minimal** — the article must be a concise conceptual overview (~1500w).
      Guideline adherence (``ga``) is the dominant signal; depth/breadth
      enhancements are irrelevant (de=be=0) because the variant explicitly
      forbids external examples/code; cost is unchanged.

    * **standard** (default) — the balanced formula used in Phase 2b grading.

    * **demanding** — the article must meet extended requirements (4000–4500w,
      production code, named case studies, per-section industry anchors).
      Depth/breadth enhancement weight is boosted; research-query cost is
      halved to encourage thorough exploration.
    """
    cc = scores["ground_truth_core_content"]
    fl = scores["ground_truth_flow"]
    de = scores["ground_truth_depth_enhancement"]
    be = scores["ground_truth_breadth_enhancement"]
    cp = scores["ground_truth_core_preservation"]
    ga = scores["user_intent_guideline_adherence"]
    ra = scores["user_intent_research_anchoring"]
    nr = _EPISODE_PRESET_ROUNDS[preset_id]

    if variant_level == "minimal":
        # Conceptual overview: ga dominant, small exploration signal, cost standard.
        gt_base     = 0.05 * cc + 0.05 * fl
        explore     = cp * (0.60 * de + 0.40 * be) * 0.10
        user_intent = 0.70 * ga + 0.10 * ra
        cost        = -0.02 * nr
    elif variant_level == "demanding":
        # Extended article: boost depth/breadth, quarter exploration cost.
        # At -0.01/round cost(-0.07) overwhelms explore gains at P5;
        # -0.005/round makes deep presets competitive.
        gt_base     = 0.12 * cc + 0.08 * fl
        explore     = cp * (0.55 * de + 0.35 * be) * 0.50
        user_intent = (0.60 * ga + 0.40 * ra) * 0.25
        cost        = -0.005 * nr
    else:  # "standard"
        gt_base     = 0.20 * cc + 0.20 * fl
        explore     = cp * (0.60 * de + 0.40 * be) * 0.30
        user_intent = (0.50 * ga + 0.50 * ra) * 0.30
        cost        = -0.02 * nr

    return gt_base + explore + user_intent + cost


def compute_oracle_reward(oracle_preset: str, action_preset: str) -> float:
    """Compute ordinal-distance reward for oracle-based GRPO training.

    Returns 1.0 for exact match, decreasing linearly to 0.0 at maximum
    ordinal distance (3 steps for skip↔deep).

    Args:
        oracle_preset: Ground-truth preset name from section_oracle.json.
        action_preset: One of "skip", "light", "standard", "deep".

    Returns:
        float in [0.0, 1.0].
    """
    oracle_idx = PRESET_ORDER[oracle_preset]
    action_idx = PRESET_ORDER[action_preset]
    distance = abs(action_idx - oracle_idx)
    return 1.0 - distance / (NUM_PRESETS - 1)


# ---------------------------------------------------------------------------
# Section-level parsing helpers
# ---------------------------------------------------------------------------
def _parse_reasoning_sections(text: str) -> dict[str, int]:
    """Parse per-section binary scores from a reasoning.json dimension value.

    Each dimension value is formatted as:
        SectionTitle:
        **1:** reason text

        NextSection:
        **0:** reason text
    """
    sections: dict[str, int] = {}
    for part in text.split("\n\n"):
        part = part.strip()
        if not part:
            continue
        m = re.match(r'^(.+?):\s*\n\*\*(\d):\*\*', part)
        if m:
            sections[m.group(1).strip()] = int(m.group(2))
    return sections


def _extract_digest_sections(digest: str) -> list[tuple[str, str]]:
    """Extract (title, excerpt_text) pairs from a digest's Per-Section Coverage Analysis."""
    pattern = r'^### S(\d+) — (.+)$'
    matches = list(re.finditer(pattern, digest, re.MULTILINE))
    sections: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        title = m.group(2).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(digest)
        excerpt = digest[start:end].strip()
        # Stop at "## 3. Overall Gap Profile" if it appears within the block
        gap_idx = excerpt.find('\n## 3.')
        if gap_idx != -1:
            excerpt = excerpt[:gap_idx].strip()
        sections.append((title, excerpt))
    return sections


def _match_reasoning_to_digest(
    reasoning_name: str,
    digest_sections: list[tuple[str, str]],
) -> int | None:
    """Match a reasoning section name to a digest section index.

    Reasoning section names (from LLM judge) may be abbreviated, have
    different casing, or carry prefixes like "The " compared to digest
    section titles.  Three-pass matching: exact → substring → normalized.
    """
    rn_lower = reasoning_name.lower().strip()
    # Pass 1: exact match
    for i, (title, _) in enumerate(digest_sections):
        if title.lower() == rn_lower:
            return i
    # Pass 2: substring containment (either direction)
    for i, (title, _) in enumerate(digest_sections):
        tl = title.lower()
        if rn_lower in tl or tl in rn_lower:
            return i
    # Pass 3: strip common prefixes ("The ") and punctuation, then retry
    rn_norm = re.sub(r'^the\s+', '', rn_lower).replace(',', '')
    for i, (title, _) in enumerate(digest_sections):
        tl_norm = re.sub(r'^the\s+', '', title.lower()).replace(',', '')
        if rn_norm in tl_norm or tl_norm in rn_norm:
            return i
    return None


def _extract_guideline_sections(
    guideline: str,
    digest_sections: list[tuple[str, str]],
) -> list[str]:
    """Slice ``article_guideline.md`` into per-section text blocks aligned to
    the digest sections returned by :func:`_extract_digest_sections`.

    Guideline sections are delimited by ``## Section N - Title`` or
    ``## Section N: Title`` headers.  Each block runs from its header up to
    (but not including) the next ``## Section`` header or end-of-file.

    Matching is done in two stages:

    1. **Positional** — if both lists have the same length, use index alignment
       directly (guideline section *i* → digest section *i*).  This is the
       common case because :func:`generate_digests._extract_content_sections`
       reads the same guideline to produce digest section titles, so the two
       orderings are guaranteed to agree.

    2. **Title fuzzy-fallback** — for any digest section that has no positional
       match (e.g., guideline and digest have different section counts due to
       merging or splitting), the same three-pass fuzzy match used in
       :func:`_match_reasoning_to_digest` is applied against each guideline
       block's extracted title.

    Returns a ``list[str]`` of length ``len(digest_sections)``.  Each entry is
    the full ``## Section N`` block text for the matched guideline section, or
    an empty string if no match was found.
    """
    # --- Step 1: split guideline by ## Section N headers ---
    header_re = re.compile(r'^## Section \d+ ?[-:] ?(.+)$', re.MULTILINE)
    matches = list(header_re.finditer(guideline))
    if not matches:
        log.warning("_extract_guideline_sections: no '## Section N' headers found in guideline")
        return [""] * len(digest_sections)

    guideline_blocks: list[tuple[str, str]] = []  # (title, full_block_text)
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        # Strip inline subsection prefix like "Introduction: " for matching
        # (e.g., "Introduction: When prompt engineering breaks" → keep both)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(guideline)
        block = guideline[start:end].strip()
        guideline_blocks.append((title, block))

    n_g = len(guideline_blocks)
    n_d = len(digest_sections)

    result: list[str] = [""] * n_d

    # --- Step 2a: positional alignment when counts match ---
    if n_g == n_d:
        for i, (_, block) in enumerate(guideline_blocks):
            result[i] = block
        return result

    # --- Step 2b: title fuzzy-match fallback ---
    log.warning(
        f"_extract_guideline_sections: guideline has {n_g} sections, "
        f"digest has {n_d} — falling back to title matching"
    )
    for d_idx, (d_title, _) in enumerate(digest_sections):
        match_idx = _match_reasoning_to_digest(d_title, guideline_blocks)
        if match_idx is not None:
            result[d_idx] = guideline_blocks[match_idx][1]
        else:
            # Last resort: use positional if within range
            if d_idx < n_g:
                result[d_idx] = guideline_blocks[d_idx][1]
            log.warning(
                f"  _extract_guideline_sections: no match for digest section "
                f"'{d_title}' (d_idx={d_idx}); {'used positional fallback' if d_idx < n_g else 'left empty'}"
            )
    return result


def _extract_guideline_preamble(guideline: str) -> str:
    """Return the text of ``article_guideline.md`` that precedes the first
    ``## Section N`` header — the global context block that carries the total
    word target, variant scope note, and audience description.

    Returns an empty string when no section headers are found.
    """
    header_re = re.compile(r'^## Section \d+ ?[-:] ?', re.MULTILINE)
    m = header_re.search(guideline)
    if m:
        return guideline[:m.start()].strip()
    return ""


def _extract_compact_preamble(preamble: str) -> str:
    """Distil the key variant-signal fields from the full guideline preamble.

    Returns a compact 2–3 line string containing only:
    - Expected length (total word target)
    - Theory / practice ratio
    - Scope constraint sentence (minimal variant only; absent for standard/demanding)

    This replaces the full preamble blob (~2000-4400 tokens) in the model input
    so the section guideline is not buried in preamble noise.  Mirrors the
    identical function in ``infer.py``.
    """
    lines: list[str] = []

    # Expected Length of the Lesson → word count line
    m = re.search(r'### Expected Length[^\n]*\n+(.*?)(?=\n###|\n##|\Z)', preamble, re.DOTALL)
    if m:
        first_line = next((l for l in m.group(1).split('\n') if l.strip()), '')
        lines.append(f"Expected length: {first_line}")

    # Theory / Practice Ratio → ratio line
    m = re.search(r'### Theory[^\n]*\n+(.*?)(?=\n###|\n##|\Z)', preamble, re.DOTALL)
    if m:
        first_line = next((l for l in m.group(1).split('\n') if l.strip()), '')
        lines.append(f"Theory / practice: {first_line}")

    # Scope constraint (minimal only): search full preamble for the distinctive
    # phrase — appears in different subsections depending on the article.
    m = re.search(r'surface-level treatment[^.!?]*[.!?]', preamble, re.IGNORECASE)
    if m:
        lines.append(f"Scope: {m.group(0).strip()}")

    return '\n'.join(lines)


def _article_variant_level(article: str) -> str:
    """Infer the guideline variant level from the article directory name.

    Standard articles (e.g. ``"03_context_engineering"``) return
    ``"standard"``.  Variant articles generated by
    ``generate_guideline_variants.py`` use the suffix ``__var_{level}``
    (e.g. ``"03_context_engineering__var_minimal"``).
    """
    if "__var_minimal" in article:
        return "minimal"
    if "__var_demanding" in article:
        return "demanding"
    return "standard"


# ---------------------------------------------------------------------------
# Data loading — article level
# ---------------------------------------------------------------------------
def load_groups(sigma_floor: float) -> list[Group]:
    """Load all training data and compute advantages."""
    groups: list[Group] = []

    for article in ARTICLES:
        digest_path = _BASES_DIR / article / "research_digest.md"
        digest = digest_path.read_text(encoding="utf-8")
        group = Group(name=article, digest=digest)

        variant_level = _article_variant_level(article)
        for p in _EPISODE_PRESET_ROUNDS:
            ep_dir = _EPISODES_DIR / f"{article}__preset{p}"
            scores = json.loads((ep_dir / "scores.json").read_text(encoding="utf-8"))
            reward = _compute_episode_reward(scores, p, variant_level)
            group.rewards.append(reward)

        # Drop flat groups: when the full reward margin is below sigma_floor
        # the oracle assignment is unreliable and the group adds only noise.
        _max_r = max(group.rewards)
        if _max_r - min(group.rewards) < sigma_floor:
            log.info(f"  {article}: dropped (flat, max-min < sigma_floor)")
            continue

        # Near-tie acceptance: arms within sigma_floor of max share the best
        # advantage so the gradient never penalises an equivalent choice.
        group.acceptable_idxs = [
            i for i, r in enumerate(group.rewards) if r >= _max_r - sigma_floor
        ]
        adj_rewards = [
            _max_r if r >= _max_r - sigma_floor else r for r in group.rewards
        ]

        # Within-group advantage normalization (on adjusted rewards)
        mean_r = sum(adj_rewards) / len(adj_rewards)
        raw_std = (sum((r - mean_r) ** 2 for r in adj_rewards) / len(adj_rewards)) ** 0.5
        group.hit_sigma_floor = raw_std < sigma_floor
        std_r = max(raw_std, sigma_floor)
        advantages = [(r - mean_r) / std_r for r in adj_rewards]
        group.advantages = torch.tensor(advantages, dtype=torch.float32)
        group.best_preset_idx = group.rewards.index(_max_r)

        groups.append(group)
        log.info(
            f"  {article}: R={[f'{r:.3f}' for r in group.rewards]} "
            f"best=P{group.best_preset_idx} ({_max_r:.4f}) "
            f"accept={group.acceptable_idxs}"
        )

    # Equal weight per article (article-level granularity has no word-count signal).
    equal_w = 1.0 / len(groups)
    for g in groups:
        g.word_weight = equal_w
    return groups


# ---------------------------------------------------------------------------
# Data loading — section level
# ---------------------------------------------------------------------------
def load_section_groups(
    sigma_floor: float,
    section_weight: str = "hybrid",
) -> list[Group]:
    """Load section-level GRPO groups from section_oracle.json.

    Each section entry in the oracle becomes its own GRPO group with
    NUM_PRESETS=4 arms.  Rewards come directly from the per-arm reward
    vectors stored in section_oracle.json (version 2), which are derived
    from actual episode runs via generate_episode_oracles.py.

    For legacy version-1 oracle files (``presets`` key only, no per-arm
    rewards), falls back to the ordinal-distance proxy from
    ``compute_oracle_reward``.

    ``section_weight`` controls how each section's loss contribution is
    weighted within an article.  Each article always contributes equally
    overall (its sections' weights sum to ``1 / num_articles``).

    Modes:
    * ``wordcount``     — weight by guideline target_words.
    * ``variance``      — weight by std(R) across the 4 arms.
    * ``hybrid``        — wordcount × std(R).
    * ``regret-hybrid`` — wordcount × (max(R) − mean(R)).  Preferred: upside-aware.
    * ``uniform``       — equal weight per section.
    """
    groups: list[Group] = []

    for article in ARTICLES:
        oracle_path = _BASES_DIR / article / "section_oracle.json"
        if not oracle_path.exists():
            log.warning(f"  {article}: section_oracle.json not found, skipping")
            continue

        oracle_data = json.loads(oracle_path.read_text(encoding="utf-8"))
        oracle_version = oracle_data.get("version", 1)

        # Version 2+: use pre-computed per-arm rewards from episode runs.
        # Version 1 (legacy): fall back to ordinal-distance proxy.
        if oracle_version >= 2:
            sections_v2: dict[str, dict] = oracle_data.get("sections", {})
            if not sections_v2:
                log.warning(f"  {article}: oracle sections empty, skipping")
                continue
            # Build (sec_id -> oracle_preset, sec_id -> [r_skip, r_light, r_std, r_deep])
            oracle_presets: dict[str, str] = {
                sid: info["oracle"] for sid, info in sections_v2.items()
            }
            oracle_rewards: dict[str, list[float]] = {
                sid: [info["rewards"].get(PRESET_NAMES[i], 0.0) for i in range(NUM_PRESETS)]
                for sid, info in sections_v2.items()
            }
        else:
            # Legacy format
            oracle_presets = oracle_data.get("presets", {})
            if not oracle_presets:
                log.warning(f"  {article}: oracle is empty, skipping")
                continue
            oracle_rewards = {}  # will compute from compute_oracle_reward below

        digest_path = _BASES_DIR / article / "research_digest.md"
        if not digest_path.exists():
            log.warning(f"  {article}: research_digest.md not found, skipping")
            continue
        digest = digest_path.read_text(encoding="utf-8")

        # Some variant digests were truncated during generation: section_coverage
        # has fewer entries than the article actually has.  When build_rl_input
        # can't find a sec_id in the digest, it returns "(not found)" — giving
        # the model a meaningless input.  Fall back to the base dir digest and
        # patch in the variant's external_evidence_policy so the policy signal
        # (forbidden / allowed / required) stays correct.
        missing_ids = [sid for sid in oracle_presets if f'id="{sid}"' not in digest]
        if missing_ids:
            policy_m = re.search(
                r"<external_evidence_policy>([^<]+)</external_evidence_policy>", digest
            )
            variant_policy = policy_m.group(1).strip() if policy_m else None
            base_article = re.sub(r"__var_\w+$", "", article)
            base_digest_path = _BASES_DIR / base_article / "research_digest.md"
            if base_digest_path.exists():
                base_digest = base_digest_path.read_text(encoding="utf-8")
                base_missing = [sid for sid in oracle_presets if f'id="{sid}"' not in base_digest]
                if len(base_missing) < len(missing_ids):
                    log.info(
                        f"  {article}: variant digest missing {len(missing_ids)} sec_ids; "
                        "using base dir digest"
                    )
                    digest = base_digest
                    if variant_policy:
                        digest = re.sub(
                            r"<external_evidence_policy>[^<]+</external_evidence_policy>",
                            f"<external_evidence_policy>{variant_policy}</external_evidence_policy>",
                            digest,
                        )
                else:
                    log.warning(
                        f"  {article}: digest missing sec_ids {missing_ids}; "
                        f"base dir also incomplete (missing {base_missing})"
                    )
            else:
                log.warning(
                    f"  {article}: digest missing sec_ids {missing_ids}; no base dir fallback"
                )

        feat_path = _BASES_DIR / article / "guideline_features.json"
        feat_sections: dict[str, dict] = {}
        if feat_path.exists():
            feat_data = json.loads(feat_path.read_text(encoding="utf-8"))
            feat_sections = feat_data.get("sections", {})

        article_groups: list[Group] = []
        for sec_id, oracle_preset in sorted(oracle_presets.items()):
            rl_input = build_rl_input(digest, sec_id)
            user_message = rl_input["user"]

            raw_word_weight = max(
                feat_sections.get(sec_id, {}).get("target_words", 1), 1
            )

            if oracle_version >= 2:
                rewards = oracle_rewards[sec_id]
            else:
                rewards = [
                    compute_oracle_reward(oracle_preset, PRESET_NAMES[i])
                    for i in range(NUM_PRESETS)
                ]

            group = Group(
                name=f"{article}__{sec_id}",
                digest=user_message,
                section_guideline="",
                guideline_preamble="",
                word_weight=float(raw_word_weight),
                rewards=rewards,
            )

            # Drop flat groups: choice doesn't matter, gradient is pure noise.
            _max_r = max(rewards)
            if _max_r - min(rewards) < sigma_floor:
                log.info(
                    f"  {article}__{sec_id}: dropped "
                    f"(flat, max-min={_max_r - min(rewards):.4f} < sigma_floor)"
                )
                continue

            # Original-reward stats for section weighting (pre-flattening).
            _orig_mean = sum(rewards) / len(rewards)
            group.raw_reward_std    = (
                sum((r - _orig_mean) ** 2 for r in rewards) / len(rewards)
            ) ** 0.5
            group.raw_reward_regret = _max_r - _orig_mean

            # Near-tie acceptance: flatten near-tie arms to max before advantage
            # normalization so no gradient penalises an equivalent choice.
            group.acceptable_idxs = [
                i for i, r in enumerate(rewards) if r >= _max_r - sigma_floor
            ]
            adj_rewards = [
                _max_r if r >= _max_r - sigma_floor else r for r in rewards
            ]

            mean_r  = sum(adj_rewards) / len(adj_rewards)
            raw_std = (
                sum((r - mean_r) ** 2 for r in adj_rewards) / len(adj_rewards)
            ) ** 0.5
            group.hit_sigma_floor = raw_std < sigma_floor
            std_r = max(raw_std, sigma_floor)
            advantages = [(r - mean_r) / std_r for r in adj_rewards]
            group.advantages = torch.tensor(advantages, dtype=torch.float32)
            group.best_preset_idx = rewards.index(_max_r)

            article_groups.append(group)
            log.info(
                f"  {group.name} (oracle={oracle_preset}"
                + ("" if oracle_version >= 2 else " [proxy]")
                + f"): R={[f'{r:.3f}' for r in rewards]} "
                f"best={PRESET_NAMES[group.best_preset_idx]} "
                f"accept={group.acceptable_idxs}"
            )

        if not article_groups:
            continue

        if section_weight == "variance":
            raw_weights = [g.raw_reward_std for g in article_groups]
        elif section_weight == "hybrid":
            raw_weights = [g.word_weight * g.raw_reward_std for g in article_groups]
        elif section_weight == "regret-hybrid":
            raw_weights = [g.word_weight * g.raw_reward_regret for g in article_groups]
        elif section_weight == "uniform":
            raw_weights = [1.0] * len(article_groups)
        else:  # "wordcount" — matches inference aggregation
            raw_weights = [g.word_weight for g in article_groups]

        # Variant-stratified 3× reweighting: upweight anti-variant failure cells
        # where the model tends to anchor on the variant label instead of the
        # coverage signals.
        #   minimal  + oracle ∈ {standard, deep}  → model anchors "brief" prior
        #   demanding + oracle ∈ {skip, light}    → model anchors "thorough" prior
        _variant = _article_variant_level(article)
        _anti_oracles: set[str] = (
            {"standard", "deep"}  if _variant == "minimal"
            else {"skip", "light"} if _variant == "demanding"
            else set()
        )
        raw_weights = [
            rw * (3.0 if PRESET_NAMES[g.best_preset_idx] in _anti_oracles else 1.0)
            for g, rw in zip(article_groups, raw_weights)
        ]

        total_w = sum(raw_weights)
        if total_w == 0.0:
            log.warning(
                f"  {article}: all raw_weights=0 under mode '{section_weight}'; "
                "falling back to uniform within this article."
            )
            total_w = len(article_groups)
            raw_weights = [1.0] * len(article_groups)
        for g, rw in zip(article_groups, raw_weights):
            g.word_weight = rw / total_w / len(ARTICLES)
        groups.extend(article_groups)

    n_clamped = sum(1 for g in groups if g.hit_sigma_floor)
    if groups:
        log.info(
            f"  Total section-level groups: {len(groups)} "
            f"({n_clamped} clamped to sigma_floor after near-tie flattening)"
        )
    else:
        log.warning(
            "  No section-level groups loaded. "
            "Check that section_oracle.json exists under "
            "rl_training_data/bases/<article>/."
        )
    return groups


# ---------------------------------------------------------------------------
# Tokenization
# ---------------------------------------------------------------------------
def tokenize_groups(
    groups: list[Group], tokenizer, *, system_prompt: str = _RL_INPUT_SYSTEM
) -> None:
    """Tokenize prompts for all groups using the chat template.

    For new-format section-level groups the user message is already the
    full pre-composed RL input produced by ``build_rl_input``; the
    ``section_guideline`` and ``guideline_preamble`` fields are empty and
    unused.  The function still supports the legacy composite layout (non-
    empty ``section_guideline``) so that article-level groups loaded from
    the old episode format continue to work.
    """
    for group in groups:
        if group.section_guideline:
            article_ctx = (
                f"## Article context\n{group.guideline_preamble}\n\n"
                if group.guideline_preamble
                else ""
            )
            user_content = (
                "## Section guideline\n"
                f"{group.section_guideline}\n\n"
                f"{article_ctx}"
                "## Current research coverage for this section\n"
                f"{group.digest}"
            )
        else:
            user_content = group.digest

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]
        prompt_str = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=False,
            enable_thinking=False,
        )
        token_ids = tokenizer.encode(prompt_str, add_special_tokens=False)
        group.input_ids = torch.tensor([token_ids], dtype=torch.long)
        log.info(f"  {group.name}: {group.input_ids.shape[1]} tokens")


def find_action_token_ids(tokenizer) -> torch.Tensor:
    """Find token IDs for the four preset words: skip, light, standard, deep.

    Verifies that each preset name tokenizes to exactly one token with the
    provided tokenizer.  Exits with an error message if any name is split
    (indicates model / tokenizer mismatch — should never happen with Qwen3).
    """
    action_ids = []
    for i in range(NUM_PRESETS):
        name = PRESET_NAMES[i]
        toks = tokenizer.encode(name, add_special_tokens=False)
        if len(toks) != 1:
            sys.exit(
                f"ERROR: Preset '{name}' tokenized to {len(toks)} tokens: {toks}. "
                "Verify that the tokenizer matches Qwen3."
            )
        action_ids.append(toks[0])
        decoded = tokenizer.decode([toks[0]])
        log.info(f"  '{name}' -> token_id={toks[0]} -> decoded='{decoded}'")
    return torch.tensor(action_ids, dtype=torch.long)


# ---------------------------------------------------------------------------
# Reference log-probs
# ---------------------------------------------------------------------------
def _get_last_logits(model, input_ids: torch.Tensor) -> torch.Tensor:
    """Return logits for the last input token only.

    Avoids materialising the full ``[1, T, vocab_size]`` tensor that
    ``model(input_ids).logits`` produces.  At T≈2 500 tokens and
    vocab_size=151 936 in bfloat16 that tensor is ~760 MB; with only a few
    hundred MB of VRAM headroom the CUDA allocator thrashes on every forward
    pass, making each group take minutes instead of seconds.

    Strategy: call the transformer body (``base_lm.model``) to get hidden
    states, slice the last position, then apply the LM head to that single
    row.  Result: ``[1, 1, vocab_size]`` → ``[vocab_size]`` (≈ 304 KB).

    Works for both a plain ``Qwen3ForCausalLM`` (pre-LoRA, used during
    reference log-prob computation) and a PEFT-wrapped model (training).
    LoRA adapters inside the transformer body are applied correctly because
    they are injected into the sub-modules, not the top-level forward.
    """
    # Unwrap PEFT if present: PeftModel.base_model.model is the raw causal LM.
    base_lm = model.base_model.model if isinstance(model, PeftModel) else model
    # base_lm.model  → Qwen3Model (transformer body, has LoRA injected)
    # base_lm.lm_head → nn.Linear(hidden_size, vocab_size)
    last_hidden = base_lm.model(input_ids).last_hidden_state[:, -1:, :]  # [1,1,H]
    return base_lm.lm_head(last_hidden)[0, 0, :]  # [vocab_size]


def compute_ref_log_probs(
    model, groups: list[Group], action_token_ids: torch.Tensor, device: torch.device
) -> None:
    """Forward pass through the base model to cache reference log-probs."""
    log.info("Computing reference log-probs (base model, no LoRA)...")
    model.eval()
    action_ids = action_token_ids.to(device)

    with torch.no_grad():
        for group in groups:
            logits = _get_last_logits(model, group.input_ids.to(device))
            log_probs = F.log_softmax(logits.float(), dim=-1)
            group.ref_log_probs = log_probs[action_ids].cpu()

            probs = group.ref_log_probs.exp()
            log.info(
                f"  {group.name}: ref_probs={[f'{p:.4f}' for p in probs.tolist()]}"
            )


def _collect_trainable_state_dict(model) -> dict[str, torch.Tensor]:
    """Collect only trainable parameters (LoRA adapters) for compact checkpoints."""
    trainable_names = {name for name, p in model.named_parameters() if p.requires_grad}
    model_state = model.state_dict()
    return {
        name: tensor.detach().cpu()
        for name, tensor in model_state.items()
        if name in trainable_names
    }


def _move_optimizer_state_to_device(optimizer, device: torch.device) -> None:
    """Move optimizer state tensors to target device after loading from disk."""
    for state in optimizer.state.values():
        for key, value in state.items():
            if torch.is_tensor(value):
                state[key] = value.to(device)


def _save_resume_state(
    *,
    state_path: Path,
    task_id: str,
    granularity: str,
    model,
    optimizer,
    scheduler,
    next_epoch: int,
    best_expected_reward: float,
    patience_counter: int,
) -> None:
    """Persist full resumable training state for a specific task id."""
    state = {
        "task_id": task_id,
        "granularity": granularity,
        "next_epoch": next_epoch,
        "best_expected_reward": best_expected_reward,
        "patience_counter": patience_counter,
        "optimizer": optimizer.state_dict(),
        "scheduler": scheduler.state_dict(),
        "lora_state_dict": _collect_trainable_state_dict(model),
        "saved_at_unix": time.time(),
    }
    torch.save(state, state_path)


def _load_resume_state(state_path: Path) -> dict[str, Any]:
    """Load resumable training state from disk."""
    return torch.load(state_path, map_location="cpu", weights_only=False)


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------
def train(
    model,
    groups: list[Group],
    action_token_ids: torch.Tensor,
    device: torch.device,
    args: argparse.Namespace,
    *,
    task_id: str,
    task_dir: Path,
    resume_state: dict[str, Any] | None = None,
) -> None:
    """Main offline GRPO training loop."""
    _OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    task_dir.mkdir(parents=True, exist_ok=True)
    run_name = time.strftime("run_%Y%m%d_%H%M%S")
    log_dir = task_dir / "runs" / run_name
    log_dir.mkdir(parents=True, exist_ok=True)
    writer = SummaryWriter(log_dir=str(log_dir))
    log.info(f"TensorBoard log dir: {log_dir.resolve()}")
    log.info(f"  Task id: {task_id}")
    log.info(f"  Launch with: tensorboard --logdir {(task_dir / 'runs').resolve()}")
    jsonl_path = task_dir / "training_log.jsonl"
    state_path = task_dir / "resume_state.pt"

    action_ids = action_token_ids.to(device)
    num_groups = len(groups)

    # Move pre-computed tensors to device
    for g in groups:
        g.advantages = g.advantages.to(device)
        g.ref_log_probs = g.ref_log_probs.to(device)

    # Optimizer — 8-bit paged AdamW halves FP32 moment memory and pages to
    # CPU under pressure; critical on 16 GB VRAM with gradient checkpointing.
    trainable_params = [p for p in model.parameters() if p.requires_grad]
    optimizer = bnb.optim.PagedAdamW8bit(
        trainable_params, lr=args.lr, weight_decay=args.weight_decay
    )

    # Cosine LR with linear warmup
    def lr_lambda(epoch: int) -> float:
        if epoch < args.warmup_epochs:
            return epoch / max(args.warmup_epochs, 1)
        progress = (epoch - args.warmup_epochs) / max(
            args.epochs - args.warmup_epochs, 1
        )
        return 0.5 * (1 + math.cos(math.pi * progress))

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

    # Baselines for comparison
    uniform_er = sum(sum(g.rewards) / len(g.rewards) for g in groups) / num_groups
    oracle_er = sum(max(g.rewards) for g in groups) / num_groups
    log.info(f"Uniform-random E[R] = {uniform_er:.4f}")
    log.info(f"Oracle E[R]          = {oracle_er:.4f}")
    log.info(
        f"Training: {args.epochs} epochs, lr={args.lr}, "
        f"β={args.beta}, patience={args.patience}"
    )

    start_epoch = 0
    best_expected_reward = -float("inf")
    patience_counter = 0
    if resume_state is not None:
        start_epoch = int(resume_state.get("next_epoch", 0))
        best_expected_reward = float(
            resume_state.get("best_expected_reward", best_expected_reward)
        )
        patience_counter = int(resume_state.get("patience_counter", 0))
        optimizer.load_state_dict(resume_state["optimizer"])
        scheduler.load_state_dict(resume_state["scheduler"])
        _move_optimizer_state_to_device(optimizer, device)
        log.info(
            f"Resumed task '{task_id}' from epoch {start_epoch} "
            f"(best E[R]={best_expected_reward:.4f}, patience={patience_counter})"
        )
        if start_epoch >= args.epochs:
            log.info(
                f"Nothing to train: resume epoch {start_epoch} >= target epochs {args.epochs}."
            )
            writer.close()
            return

    t_start = time.time()

    log_mode = "a" if resume_state is not None and jsonl_path.exists() else "w"
    with open(jsonl_path, log_mode, encoding="utf-8") as log_file:
        for epoch in range(start_epoch, args.epochs):
            model.train()
            optimizer.zero_grad()

            epoch_loss_grpo = 0.0
            epoch_loss_kl = 0.0
            epoch_loss_entropy = 0.0
            epoch_loss_total = 0.0
            epoch_metrics: dict[str, dict] = {}

            t_epoch_start = time.time()
            for g_idx, group in enumerate(groups, 1):
                t_group_start = time.time()
                input_ids = group.input_ids.to(device)
                logits = _get_last_logits(model, input_ids)

                # Re-normalize over the action logits only (consistent
                # across policy gradient, KL, and eval metrics).
                action_logits = logits.float()[action_ids]
                pi_lp = F.log_softmax(action_logits, dim=-1)
                ref_lp = F.log_softmax(group.ref_log_probs, dim=-1)

                # GRPO policy gradient loss
                loss_grpo = -(group.advantages * pi_lp).mean()

                # KL(π || π_ref) over the action simplex (always ≥ 0).
                loss_kl = (pi_lp.exp() * (pi_lp - ref_lp)).sum()

                # Entropy bonus H(π) — directly prevents collapse (always ≥ 0).
                loss_entropy = -(pi_lp.exp() * pi_lp).sum()

                # Weighted sum across groups: word-count weight mirrors the
                # word-count-weighted vote used at inference (section granularity)
                # or equal weight per article (article granularity).
                loss = (loss_grpo + args.beta * loss_kl - args.entropy_coef * loss_entropy) * group.word_weight
                loss.backward()

                epoch_loss_grpo += loss_grpo.item() * group.word_weight
                epoch_loss_kl += loss_kl.item() * group.word_weight
                epoch_loss_entropy += loss_entropy.item() * group.word_weight
                epoch_loss_total += loss.item()

                # --- per-group evaluation metrics (no grad) ---
                with torch.no_grad():
                    # Re-normalize over the action logits for eval
                    probs = F.softmax(logits.float()[action_ids], dim=-1)
                    rewards_t = torch.tensor(
                        group.rewards, device=device, dtype=torch.float32
                    )
                    # Use log_softmax for entropy to avoid 0*log(0)=NaN when
                    # any action probability is numerically zero.
                    lp_eval = F.log_softmax(logits.float()[action_ids], dim=-1)
                    entropy = -(probs * lp_eval).sum().item()
                    expected_reward = (probs * rewards_t).sum().item()
                    top1 = probs.argmax().item()

                    epoch_metrics[group.name] = {
                        "entropy": round(entropy, 4),
                        "expected_reward": round(expected_reward, 4),
                        "top1_preset": top1,
                        "top1_correct": top1 in group.acceptable_idxs,
                        "action_probs": [round(p, 4) for p in probs.cpu().tolist()],
                        "kl": round(loss_kl.item(), 6),
                        "group_time_s": round(time.time() - t_group_start, 2),
                    }
                    log.info(
                        f"  [ep {epoch + 1}] group {g_idx}/{num_groups} "
                        f"({group.name}): "
                        f"E[R]={expected_reward:.4f} "
                        f"top1={'OK' if top1 in group.acceptable_idxs else '--'} "
                        f"kl={loss_kl.item():.4f} "
                        f"({epoch_metrics[group.name]['group_time_s']}s)"
                    )

            # Gradient clipping
            grad_norm = torch.nn.utils.clip_grad_norm_(
                trainable_params, args.max_grad_norm
            ).item()

            optimizer.step()
            current_lr = scheduler.get_last_lr()[0]
            scheduler.step()

            # ---------- aggregate metrics ----------
            mean_er = (
                sum(m["expected_reward"] for m in epoch_metrics.values()) / num_groups
            )
            top1_acc = (
                sum(m["top1_correct"] for m in epoch_metrics.values()) / num_groups
            )
            mean_entropy = (
                sum(m["entropy"] for m in epoch_metrics.values()) / num_groups
            )
            mean_kl = sum(m["kl"] for m in epoch_metrics.values()) / num_groups

            epoch_wall_s = time.time() - t_epoch_start

            # ---------- TensorBoard ----------
            writer.add_scalar("train/loss_total", epoch_loss_total, epoch)
            writer.add_scalar("train/loss_grpo", epoch_loss_grpo, epoch)
            writer.add_scalar("train/loss_kl", epoch_loss_kl, epoch)
            writer.add_scalar("train/loss_entropy", epoch_loss_entropy, epoch)
            writer.add_scalar("train/mean_kl", mean_kl, epoch)
            writer.add_scalar("train/grad_norm", grad_norm, epoch)
            writer.add_scalar("train/lr", current_lr, epoch)
            sigma_floor_frac = sum(1 for g in groups if g.hit_sigma_floor) / num_groups
            writer.add_scalar("eval/mean_expected_reward", mean_er, epoch)
            writer.add_scalar("eval/top1_accuracy", top1_acc, epoch)
            writer.add_scalar("eval/mean_entropy", mean_entropy, epoch)
            writer.add_scalar("eval/sigma_floor_fraction", sigma_floor_frac, epoch)

            for gname, gm in epoch_metrics.items():
                writer.add_scalar(
                    f"eval/expected_reward/{gname}", gm["expected_reward"], epoch
                )
                writer.add_scalar(f"eval/entropy/{gname}", gm["entropy"], epoch)

            # ---------- JSONL ----------
            log_entry = {
                "task_id": task_id,
                "epoch": epoch,
                "epoch_wall_s": round(epoch_wall_s, 1),
                "loss_total": round(epoch_loss_total, 6),
                "loss_grpo": round(epoch_loss_grpo, 6),
                "loss_kl": round(epoch_loss_kl, 6),
                "loss_entropy": round(epoch_loss_entropy, 6),
                "mean_kl": round(mean_kl, 6),
                "grad_norm": round(grad_norm, 6),
                "lr": current_lr,
                "mean_expected_reward": round(mean_er, 4),
                "top1_accuracy": round(top1_acc, 4),
                "mean_entropy": round(mean_entropy, 4),
                "sigma_floor_fraction": round(sigma_floor_frac, 4),
                "per_group": epoch_metrics,
            }
            log_file.write(json.dumps(log_entry) + "\n")
            log_file.flush()

            # ---------- console (every 10 epochs + last) ----------
            if epoch % 10 == 0 or epoch == args.epochs - 1:
                elapsed = time.time() - t_start
                vram_mb = torch.cuda.memory_allocated() / 1024**2
                log.info(
                    f"Epoch {epoch:>4d}/{args.epochs} | "
                    f"loss={epoch_loss_total:.4f} "
                    f"(grpo={epoch_loss_grpo:.4f} kl={epoch_loss_kl:.4f} ent={epoch_loss_entropy:.4f}) | "
                    f"E[R]={mean_er:.4f} | top1={top1_acc:.0%} | "
                    f"H={mean_entropy:.3f} | "
                    f"‖g‖={grad_norm:.4f} | lr={current_lr:.2e} | "
                    f"epoch={epoch_wall_s:.0f}s | total={elapsed:.0f}s | "
                    f"VRAM={vram_mb:.0f}MB"
                )

            # ---------- checkpointing ----------
            if mean_er > best_expected_reward:
                best_expected_reward = mean_er
                patience_counter = 0
                best_dir = task_dir / "best"
                best_dir.mkdir(parents=True, exist_ok=True)
                model.save_pretrained(str(best_dir))
                log.info(
                    f"  ★ New best E[R]={best_expected_reward:.4f} — saved to {best_dir}"
                )
            else:
                patience_counter += 1

            # Overwrite latest/ every epoch so there is always a recoverable
            # PEFT adapter for the most recently completed epoch.
            latest_dir = task_dir / "latest"
            latest_dir.mkdir(parents=True, exist_ok=True)
            model.save_pretrained(str(latest_dir))

            _save_resume_state(
                state_path=state_path,
                task_id=task_id,
                granularity=args.granularity,
                model=model,
                optimizer=optimizer,
                scheduler=scheduler,
                next_epoch=epoch + 1,
                best_expected_reward=best_expected_reward,
                patience_counter=patience_counter,
            )

            # ---------- early stopping ----------
            if patience_counter >= args.patience:
                log.info(
                    f"Early stopping at epoch {epoch} "
                    f"(no improvement for {args.patience} epochs)"
                )
                break

    writer.close()
    elapsed_total = time.time() - t_start
    log.info(
        f"Training complete in {elapsed_total:.0f}s. "
        f"Best E[R]={best_expected_reward:.4f} "
        f"(uniform={uniform_er:.4f}, oracle={oracle_er:.4f}). "
        f"Checkpoints: best={task_dir / 'best'}, latest={task_dir / 'latest'}"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Offline GRPO + QLoRA training for preset selection"
    )
    parser.add_argument("--epochs", type=int, default=200)
    parser.add_argument("--lr", type=float, default=5e-5)
    parser.add_argument("--beta", type=float, default=0.1, help="KL penalty coefficient")
    parser.add_argument("--entropy-coef", type=float, default=0.15, help="Entropy bonus coefficient")
    parser.add_argument(
        "--sigma-floor", type=float, default=0.04,
        help="Minimum std for advantage normalization",
    )
    parser.add_argument("--warmup-epochs", type=int, default=10)
    parser.add_argument("--max-grad-norm", type=float, default=0.5)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--patience", type=int, default=30, help="Early stopping patience")
    parser.add_argument("--lora-r", type=int, default=8)
    parser.add_argument("--lora-alpha", type=int, default=8)
    parser.add_argument("--lora-dropout", type=float, default=0.0)
    parser.add_argument(
        "--granularity",
        choices=["article", "section"],
        default="article",
        help="Training granularity: article-level (5 groups) or "
        "section-level (~35 groups)",
    )
    parser.add_argument(
        "--section-weight",
        choices=["wordcount", "variance", "hybrid", "regret-hybrid", "uniform"],
        default="hybrid",
        help=(
            "How to weight section groups in the loss (section granularity only). "
            "'wordcount': proportional to section length (matches inference). "
            "'variance': proportional to reward std (upweights exploration-critical sections). "
            "'hybrid': wordcount x reward_std (combines length and variance signals). "
            "'regret-hybrid': wordcount x regret where regret=max(R)-mean(R); "
            "upside-aware — focuses gradient on sections where one clear winner exists, "
            "not just sections with high symmetric spread (recommended). "
            "'uniform': equal weight per section (original behaviour)."
        ),
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Load model and data, run one forward pass, then exit",
    )
    parser.add_argument("--model-dir", type=str, default=str(_MODEL_DIR))
    parser.add_argument(
        "--task-id", type=str, default=None,
        help="Unique task identifier for training artifacts (auto-generated if omitted)",
    )
    parser.add_argument(
        "--resume", action="store_true",
        help="Resume training from the saved state of --task-id",
    )
    parser.add_argument(
        "--init-adapter",
        type=Path,
        default=None,
        help=(
            "Initialize LoRA weights from an existing PEFT adapter directory "
            "(for example a previous task's best/ checkpoint), then start a "
            "fresh optimizer and LR schedule. Do not combine with --resume."
        ),
    )
    args = parser.parse_args()

    log.info("=" * 65)
    log.info("  Offline GRPO + QLoRA Training Pipeline")
    log.info("=" * 65)

    # ------------------------------------------------------------------
    # CUDA check
    # ------------------------------------------------------------------
    if not torch.cuda.is_available():
        sys.exit("ERROR: CUDA not available. Check PyTorch CUDA installation.")

    device = torch.device("cuda")
    vram_total = torch.cuda.mem_get_info()[1] / 1024**3
    vram_free = torch.cuda.mem_get_info()[0] / 1024**3
    log.info(f"GPU: {torch.cuda.get_device_name(0)}")
    log.info(f"VRAM: {vram_total:.1f} GB total, {vram_free:.1f} GB free")

    task_id = args.task_id or time.strftime("task_%Y%m%d_%H%M%S")
    task_dir = _OUTPUT_DIR / "tasks" / task_id
    state_path = task_dir / "resume_state.pt"
    if args.resume and args.task_id is None:
        sys.exit("ERROR: --resume requires --task-id.")
    if args.resume and not state_path.exists():
        sys.exit(
            f"ERROR: No saved state found for task '{task_id}' at {state_path}."
        )
    if args.resume and args.init_adapter is not None:
        sys.exit("ERROR: --resume and --init-adapter are mutually exclusive.")
    if args.init_adapter is not None and not args.init_adapter.exists():
        sys.exit(f"ERROR: init adapter not found: {args.init_adapter}")
    if not args.resume and task_dir.exists():
        log.warning(
            f"Task directory already exists: {task_dir}. "
            "Starting a fresh run may overwrite metrics in this task id."
        )

    # ------------------------------------------------------------------
    # Step 1: Load training data
    # ------------------------------------------------------------------
    log.info(f"\n--- Step 1: Load training data (granularity={args.granularity}) ---")
    if args.granularity == "section":
        groups = load_section_groups(args.sigma_floor, section_weight=args.section_weight)
    else:
        groups = load_groups(args.sigma_floor)

    # ------------------------------------------------------------------
    # Step 2: Load tokenizer & find action token IDs
    # ------------------------------------------------------------------
    log.info("\n--- Step 2: Load tokenizer ---")
    tokenizer = AutoTokenizer.from_pretrained(args.model_dir)
    action_token_ids = find_action_token_ids(tokenizer)

    # ------------------------------------------------------------------
    # Step 3: Tokenize prompts
    # ------------------------------------------------------------------
    log.info("\n--- Step 3: Tokenize prompts ---")
    tokenize_groups(groups, tokenizer)

    # ------------------------------------------------------------------
    # Step 4: Load model (NF4 quantized)
    # ------------------------------------------------------------------
    log.info("\n--- Step 4: Load model (NF4 quantized) ---")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.model_dir,
        quantization_config=bnb_config,
        device_map="cuda",
        dtype=torch.bfloat16,
        attn_implementation="sdpa",
    )
    model.config.use_cache = False  # disable KV cache for training

    vram_model = torch.cuda.memory_allocated() / 1024**3
    log.info(f"Model loaded. VRAM used: {vram_model:.2f} GB")

    # ------------------------------------------------------------------
    # Step 5: Compute reference log-probs (BEFORE LoRA)
    # ------------------------------------------------------------------
    log.info("\n--- Step 5: Compute reference log-probs ---")
    compute_ref_log_probs(model, groups, action_token_ids, device)
    torch.cuda.empty_cache()  # free inference cache before training setup

    # ------------------------------------------------------------------
    # Step 6: Apply LoRA adapters
    # ------------------------------------------------------------------
    log.info("\n--- Step 6: Apply LoRA adapters ---")
    model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True)
    if args.init_adapter is not None:
        log.info(f"Loading initial LoRA adapter from: {args.init_adapter}")
        model = PeftModel.from_pretrained(
            model,
            str(args.init_adapter),
            is_trainable=True,
        )
    else:
        lora_config = LoraConfig(
            task_type=TaskType.CAUSAL_LM,
            r=args.lora_r,
            lora_alpha=args.lora_alpha,
            lora_dropout=args.lora_dropout,
            target_modules=[
                "q_proj", "k_proj", "v_proj", "o_proj",
                "gate_proj", "up_proj", "down_proj",
            ],
            bias="none",
        )
        model = get_peft_model(model, lora_config)
    # use_reentrant=False avoids peft/autograd compatibility issues
    model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
    model.print_trainable_parameters()

    resume_state: dict[str, Any] | None = None
    if args.resume:
        resume_state = _load_resume_state(state_path)
        saved_task = resume_state.get("task_id")
        if saved_task != task_id:
            sys.exit(
                f"ERROR: Resume state task id mismatch: expected '{task_id}', "
                f"found '{saved_task}'."
            )
        saved_granularity = resume_state.get("granularity")
        if saved_granularity is not None and saved_granularity != args.granularity:
            sys.exit(
                f"ERROR: Resume state granularity mismatch: saved='{saved_granularity}', "
                f"requested='{args.granularity}'. Pass --granularity {saved_granularity} to resume."
            )
        missing, unexpected = model.load_state_dict(
            resume_state["lora_state_dict"], strict=False
        )
        log.info(
            "Loaded LoRA weights from resume state "
            f"(missing={len(missing)}, unexpected={len(unexpected)})."
        )

    vram_lora = torch.cuda.memory_allocated() / 1024**3
    log.info(f"VRAM after LoRA: {vram_lora:.2f} GB")

    # ------------------------------------------------------------------
    # Dry-run: single forward pass, then exit
    # ------------------------------------------------------------------
    if args.dry_run:
        log.info("\n--- DRY RUN: single forward pass test ---")
        model.eval()
        with torch.no_grad():
            g = groups[0]
            logits = _get_last_logits(model, g.input_ids.to(device))
            probs = F.softmax(logits.float()[action_token_ids.to(device)], dim=-1)
            log.info(
                f"  {g.name}: action_probs="
                f"{[f'{p:.4f}' for p in probs.tolist()]}"
            )
        log.info("Dry-run complete — everything works. Run without --dry-run to train.")
        return

    # ------------------------------------------------------------------
    # Step 7: Train
    # ------------------------------------------------------------------
    log.info("\n--- Step 7: GRPO Training ---")
    train(
        model,
        groups,
        action_token_ids,
        device,
        args,
        task_id=task_id,
        task_dir=task_dir,
        resume_state=resume_state,
    )


if __name__ == "__main__":
    main()
