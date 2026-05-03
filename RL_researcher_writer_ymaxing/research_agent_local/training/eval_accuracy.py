"""
Section-level and article-level accuracy evaluation for the trained preset selector.

Computes oracle presets from the offline reward data, runs model inference,
and reports top-1 accuracy for train and test article sets.

Usage (from research_agent_local/):
  # Current best (4-article training set)
  uv run python training/eval_accuracy.py

  # Ablation: 5-article training set (includes 06_tools)
  uv run python training/eval_accuracy.py \
      --checkpoint rl_training_data/checkpoints/tasks/task_20260420_182715/best \
      --train-articles 03_context_engineering,05_workflow_patterns,06_tools,08_react_practice,11_multimodal \
      --label "5-article (incl. 06_tools)" \
      --er 0.7707
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _THIS_DIR.parent                # research_agent_local/
_REPO_ROOT = _AGENT_DIR.parent               # RL_researcher_writer_ymaxing/
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_DEFAULT_CHECKPOINT = (
    _REPO_ROOT / "rl_training_data" / "checkpoints" / "tasks"
    / "task_20260420_223150" / "best"
)

# ---------------------------------------------------------------------------
# Article sets
# ---------------------------------------------------------------------------
ALL_ARTICLES = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
    "09_RAG",
    "11_multimodal",
]
_DEFAULT_TRAIN_ARTICLES = [
    "03_context_engineering",
    "05_workflow_patterns",
    "08_react_practice",
    "11_multimodal",
]

# ---------------------------------------------------------------------------
# Reward constants (must mirror train_grpo.py exactly)
# ---------------------------------------------------------------------------
_PRESET_ROUNDS = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}
_NUM_PRESETS = 6
_REWARD_DIMS = [
    "ground_truth_core_content",
    "ground_truth_flow",
    "ground_truth_depth_enhancement",
    "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation",
    "user_intent_guideline_adherence",
    "user_intent_research_anchoring",
]
_PRESET_NAMES = {
    0: "P0 baseline",
    1: "P1 single_balanced",
    2: "P2 balanced_depth",
    3: "P3 depth_breadth",
    4: "P4 bal_depth_breadth",
    5: "P5 depth_breadth_depth",
}


def _compute_reward(scores: dict, preset_id: int) -> float:
    cc = scores["ground_truth_core_content"]
    fl = scores["ground_truth_flow"]
    de = scores["ground_truth_depth_enhancement"]
    be = scores["ground_truth_breadth_enhancement"]
    cp = scores["ground_truth_core_preservation"]
    ga = scores["user_intent_guideline_adherence"]
    ra = scores["user_intent_research_anchoring"]
    nr = _PRESET_ROUNDS[preset_id]
    gt_base = 0.20 * cc + 0.20 * fl
    explore = cp * (0.60 * de + 0.40 * be) * 0.30
    user_intent = (0.50 * ga + 0.50 * ra) * 0.30
    cost = -0.02 * nr
    return gt_base + explore + user_intent + cost


def _parse_reasoning_sections(text: str) -> dict[str, int]:
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
    pattern = r'^### S(\d+) — (.+)$'
    matches = list(re.finditer(pattern, digest, re.MULTILINE))
    sections: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        title = m.group(2).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(digest)
        excerpt = digest[start:end].strip()
        gap_idx = excerpt.find('\n## 3.')
        if gap_idx != -1:
            excerpt = excerpt[:gap_idx].strip()
        sections.append((title, excerpt))
    return sections


def _match_reasoning_to_digest(
    reasoning_name: str,
    digest_sections: list[tuple[str, str]],
) -> int | None:
    rn_lower = reasoning_name.lower().strip()
    for i, (title, _) in enumerate(digest_sections):
        if title.lower() == rn_lower:
            return i
    for i, (title, _) in enumerate(digest_sections):
        tl = title.lower()
        if rn_lower in tl or tl in rn_lower:
            return i
    rn_norm = re.sub(r'^the\s+', '', rn_lower).replace(',', '')
    for i, (title, _) in enumerate(digest_sections):
        tl_norm = re.sub(r'^the\s+', '', title.lower()).replace(',', '')
        if rn_norm in tl_norm or tl_norm in rn_norm:
            return i
    return None


# ---------------------------------------------------------------------------
# Oracle computation
# ---------------------------------------------------------------------------

def compute_oracle_section_presets(article: str) -> list[tuple[str, int, list[float]]]:
    """Return [(section_title, oracle_preset, rewards[0..5])] for each section."""
    digest = (_BASES_DIR / article / "research_digest.md").read_text(encoding="utf-8")
    digest_sections = _extract_digest_sections(digest)
    results = []
    for sec_idx, (sec_title, _) in enumerate(digest_sections):
        rewards = []
        for p in range(_NUM_PRESETS):
            ep_dir = _EPISODES_DIR / f"{article}__preset{p}"
            reasons = json.loads((ep_dir / "reasoning.json").read_text(encoding="utf-8"))
            section_scores: dict[str, float] = {}
            for dim in _REWARD_DIMS:
                if dim not in reasons:
                    section_scores[dim] = 0.0
                    continue
                dim_sections = _parse_reasoning_sections(reasons[dim])
                matched: int | None = None
                for rname, rscore in dim_sections.items():
                    idx = _match_reasoning_to_digest(rname, digest_sections)
                    if idx == sec_idx:
                        matched = rscore
                        break
                section_scores[dim] = float(matched if matched is not None else 0)
            rewards.append(_compute_reward(section_scores, p))
        oracle = int(rewards.index(max(rewards)))
        results.append((sec_title, oracle, rewards))
    return results


def compute_oracle_article_preset(article: str) -> tuple[int, list[float]]:
    """Return (oracle_preset, rewards[0..5]) from article-level scores.json."""
    rewards = []
    for p in range(_NUM_PRESETS):
        ep_dir = _EPISODES_DIR / f"{article}__preset{p}"
        scores = json.loads((ep_dir / "scores.json").read_text(encoding="utf-8"))
        rewards.append(_compute_reward(scores, p))
    oracle = int(rewards.index(max(rewards)))
    return oracle, rewards


# ---------------------------------------------------------------------------
# Main evaluation
# ---------------------------------------------------------------------------

def evaluate(
    checkpoint: Path,
    train_articles: list[str],
    label: str,
    er_trained: float,
) -> None:
    # Import here so model only loads when needed
    sys.path.insert(0, str(_THIS_DIR))
    from infer import ExplorationStrategySelector

    test_articles = [a for a in ALL_ARTICLES if a not in train_articles]

    print(f"\n{'#'*70}")
    print(f"  Run: {label}")
    print(f"  Checkpoint: {checkpoint}")
    print(f"  Train articles ({len(train_articles)}): {', '.join(train_articles)}")
    print(f"  Test  articles ({len(test_articles)}): {', '.join(test_articles)}")
    print(f"{'#'*70}")

    print(f"\nLoading model...")
    selector = ExplorationStrategySelector(adapter_dir=checkpoint)

    all_results: dict[str, dict] = {}  # article -> stats dict

    for split_name, articles in [("TRAIN", train_articles), ("TEST", test_articles)]:
        print(f"\n{'='*70}")
        print(f"  {split_name} ARTICLES")
        print(f"{'='*70}")

        for article in articles:
            print(f"\n--- {article} ---")
            digest = (_BASES_DIR / article / "research_digest.md").read_text(encoding="utf-8")

            # Oracle per section
            oracle_sections = compute_oracle_section_presets(article)
            oracle_article, article_rewards = compute_oracle_article_preset(article)

            # Model predictions per section (raw section call, no aggregation)
            digest_sections = _extract_digest_sections(digest)
            sec_correct = 0
            sec_total = len(digest_sections)

            print(f"\n  {'Section':<50} {'Oracle':>6}  {'Model':>6}  {'Match':>5}")
            print(f"  {'-'*50} {'-'*6}  {'-'*6}  {'-'*5}")

            section_preds = []
            for (title, excerpt), (_, oracle_p, _) in zip(digest_sections, oracle_sections):
                # Direct section-level call (bypasses aggregation heuristic)
                pred_p, _ = selector._predict_section(excerpt)
                match = pred_p == oracle_p
                if match:
                    sec_correct += 1
                marker = "✓" if match else "✗"
                section_preds.append(pred_p)
                short_title = title[:48] + ".." if len(title) > 48 else title
                print(f"  {short_title:<50} P{oracle_p:>5}  P{pred_p:>5}  {marker:>5}")

            sec_acc = sec_correct / sec_total if sec_total else 0.0

            # Article-level: run full aggregation pipeline
            pred_article, agg_probs, _, meta = selector.predict_article_verbose(digest)
            article_match = pred_article == oracle_article

            print(f"\n  Section top-1 accuracy: {sec_correct}/{sec_total} = {sec_acc:.1%}")
            print(f"  Article oracle: P{oracle_article} ({_PRESET_NAMES[oracle_article]})")
            print(f"  Article predicted: P{pred_article} ({_PRESET_NAMES[pred_article]}) {'✓' if article_match else '✗'}")
            print(f"  Article rewards: {[f'{r:.3f}' for r in article_rewards]}")

            all_results[article] = {
                "split": split_name,
                "sec_correct": sec_correct,
                "sec_total": sec_total,
                "sec_acc": sec_acc,
                "oracle_article": oracle_article,
                "pred_article": pred_article,
                "article_match": article_match,
            }

    # ---------------------------------------------------------------------------
    # Summary table
    # ---------------------------------------------------------------------------
    print(f"\n{'='*70}")
    print("  SUMMARY")
    print(f"{'='*70}")
    print(f"\n  {'Article':<35} {'Split':>5}  {'Sec Acc':>8}  {'Article':>9}")
    print(f"  {'-'*35} {'-'*5}  {'-'*8}  {'-'*9}")

    train_sec_c = train_sec_t = train_art_c = train_art_t = 0
    test_sec_c = test_sec_t = test_art_c = test_art_t = 0

    for article, r in all_results.items():
        art_str = f"P{r['oracle_article']}→P{r['pred_article']} {'✓' if r['article_match'] else '✗'}"
        print(
            f"  {article:<35} {r['split']:>5}  "
            f"{r['sec_correct']}/{r['sec_total']} ({r['sec_acc']:.0%}){'':<2}  {art_str}"
        )
        if r["split"] == "TRAIN":
            train_sec_c += r["sec_correct"]
            train_sec_t += r["sec_total"]
            train_art_c += int(r["article_match"])
            train_art_t += 1
        else:
            test_sec_c += r["sec_correct"]
            test_sec_t += r["sec_total"]
            test_art_c += int(r["article_match"])
            test_art_t += 1

    print(f"\n  {'TRAIN totals':<35} {'':>5}  "
          f"{train_sec_c}/{train_sec_t} ({train_sec_c/train_sec_t:.0%})    "
          f"{train_art_c}/{train_art_t} ({train_art_c/train_art_t:.0%})")
    print(f"  {'TEST totals':<35} {'':>5}  "
          f"{test_sec_c}/{test_sec_t} ({test_sec_c/test_sec_t:.0%})    "
          f"{test_art_c}/{test_art_t} ({test_art_c/test_art_t:.0%})")
    all_sec_c = train_sec_c + test_sec_c
    all_sec_t = train_sec_t + test_sec_t
    all_art_c = train_art_c + test_art_c
    all_art_t = train_art_t + test_art_t
    print(f"  {'ALL totals':<35} {'':>5}  "
          f"{all_sec_c}/{all_sec_t} ({all_sec_c/all_sec_t:.0%})    "
          f"{all_art_c}/{all_art_t} ({all_art_c/all_art_t:.0%})")

    # E[R] reference numbers
    uniform_er = 0.6299
    oracle_er  = 0.7907
    gap_closed = (er_trained - uniform_er) / (oracle_er - uniform_er)
    print(f"\n  E[R] reference:")
    print(f"    Uniform random baseline : {uniform_er:.4f}")
    print(f"    Trained model (train)   : {er_trained:.4f}  (from training log)")
    print(f"    Oracle ceiling          : {oracle_er:.4f}")
    print(f"    Gap closed              : {gap_closed:.1%} of uniform→oracle")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate section- and article-level preset accuracy.")
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=_DEFAULT_CHECKPOINT,
        help="Path to LoRA adapter checkpoint directory (default: latest best).",
    )
    parser.add_argument(
        "--train-articles",
        type=str,
        default=None,
        help=(
            "Comma-separated list of training article names. "
            "Test articles are derived as the complement from ALL_ARTICLES. "
            f"Default: {','.join(_DEFAULT_TRAIN_ARTICLES)}"
        ),
    )
    parser.add_argument(
        "--label",
        type=str,
        default=None,
        help="Human-readable label for this run (used in output header).",
    )
    parser.add_argument(
        "--er",
        type=float,
        default=0.7765,
        help="E[R] of trained model from training log (default: 0.7765 for 4-article best).",
    )
    args = parser.parse_args()

    if not args.checkpoint.exists():
        sys.exit(f"ERROR: checkpoint not found: {args.checkpoint}")

    train_articles = (
        [a.strip() for a in args.train_articles.split(",")]
        if args.train_articles
        else _DEFAULT_TRAIN_ARTICLES
    )
    # Validate
    for a in train_articles:
        if a not in ALL_ARTICLES:
            sys.exit(f"ERROR: unknown article '{a}'. Valid choices: {ALL_ARTICLES}")

    label = args.label or f"{len(train_articles)}-article training set"

    evaluate(args.checkpoint, train_articles=train_articles, label=label, er_trained=args.er)


if __name__ == "__main__":
    main()
