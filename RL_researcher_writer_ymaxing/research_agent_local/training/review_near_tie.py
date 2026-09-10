"""review_near_tie.py -- helper for the human near-tie review workflow (A.16.9).

For a flagged near-tie article, locates and prints (or writes to a file) the
drafted text + grader's reasoning for the section(s) driving the ambiguity
(per the margin decomposition), across ALL replicated draws (production +
however many replicates that article has -- N varies per article, e.g. N=3
or N=5, read from section_oracle_averaged.json, not hardcoded) for BOTH
contending arms (winner and runner-up) -- so a reviewer doesn't have to
manually hunt through several directories and cross-reference article.md
against reasoning.json by hand each time.

Reuses generate_episode_oracles.py's own title-normalization
(_normalize/_sec_id_to_norm) and measure_replicate_noise.py's arm/episode
conventions (_arm_presets_for/_TEST_ARTICLES) rather than re-implementing
them, so section/title matching stays consistent with how the rest of the
pipeline already does it.

Usage (from research_agent_local/training/):
    python3 review_near_tie.py --article HNSW
    python3 review_near_tie.py --article HNSW --top-n 1
    python3 review_near_tie.py --article HNSW --sections "foundations of hnsw"
    python3 review_near_tie.py --article HNSW --save
        -> writes rl_training_data/oracle_review/HNSW.md (auto-named, one file per article)
    python3 review_near_tie.py --article HNSW --output ../../rl_training_data/oracle_review.md --append
    python3 review_near_tie.py --article 29_evaluation_metrics --arms standard deep
        -> compares any two arms directly, instead of the default oracle_arm vs runner_up_arm
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))
import generate_episode_oracles as geo  # noqa: E402
import measure_replicate_noise as mrn  # noqa: E402

_REPO_ROOT = _THIS_DIR.parent.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_TEST_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "test_episodes"
_NOISE_EXPERIMENT_DIR = _REPO_ROOT / "rl_training_data" / "noise_experiment"
_REVIEW_OUTPUT_DIR = _REPO_ROOT / "rl_training_data" / "oracle_review"

# The only reasoning.json dimensions the current C2 reward formula actually
# reads (ra/structure/golden_source_priority exist in the file but are dead
# weight -- see generate_episode_oracles.py::_section_reward_components()).
_REVIEW_DIMS = [
    ("ground_truth_core_content", "cc"),
    ("ground_truth_flow", "fl"),
    ("ground_truth_depth_enhancement", "de"),
    ("ground_truth_breadth_enhancement", "be"),
    ("ground_truth_core_preservation", "cp"),
    ("user_intent_guideline_adherence", "ga"),
]


def _episode_dir(article: str, draw: int, preset: int) -> Path:
    """draw: 0=production, 1..N=replicate index."""
    if draw == 0:
        root = _TEST_EPISODES_DIR if article in mrn._TEST_ARTICLES else _EPISODES_DIR
        return root / f"{article}__preset{preset}"
    return _NOISE_EXPERIMENT_DIR / f"{article}__replicate{draw}__preset{preset}"


def _n_draws_for(article: str) -> int:
    """How many draws (production + replicates) exist for this article, per
    merge_replicate_oracles.py's section_oracle_averaged.json -- NOT hardcoded
    to 3, since articles are now replicated to different N (e.g. N=5)."""
    avg_path = _BASES_DIR / article / "section_oracle_averaged.json"
    if not avg_path.exists():
        return 1
    return json.loads(avg_path.read_text(encoding="utf-8")).get("n_draws_per_arm", 1)


def _section_contributions(article: str, winner: str, runner_up: str) -> list[tuple[float, str, str, dict]]:
    """[(contribution, sec_id, normalized_title, avg_section_info), ...], most
    negative (most AGAINST winner) first. Mirrors compute_article_oracle.py's
    _compute_r_w() weighting exactly (target-words-weighted "rest" +
    simple-mean "explore")."""
    avg = json.loads((_BASES_DIR / article / "section_oracle_averaged.json").read_text(encoding="utf-8"))["sections"]
    feat = json.loads((_BASES_DIR / article / "guideline_features.json").read_text(encoding="utf-8"))["sections"]
    total_w = sum(int(feat.get(sid, {}).get("target_words", 100)) for sid in avg)
    n_sections = len(avg)

    contribs = []
    for sec_id, info in avg.items():
        tw = int(feat.get(sec_id, {}).get("target_words", 100))
        rewards, explore = info["rewards"], info.get("explore", {})
        rest_delta = (rewards[winner] - explore.get(winner, 0.0)) - (rewards[runner_up] - explore.get(runner_up, 0.0))
        explore_delta = explore.get(winner, 0.0) - explore.get(runner_up, 0.0)
        contribution = tw * rest_delta / total_w + explore_delta / n_sections
        contribs.append((contribution, sec_id, geo._sec_id_to_norm(sec_id), info))
    contribs.sort(key=lambda c: c[0])
    return contribs, total_w


def _extract_article_section(article_md_text: str, target_norm: str, is_first_section: bool = False) -> str | None:
    heads = list(re.finditer(r"^## (.+)$", article_md_text, re.MULTILINE))
    for i, m in enumerate(heads):
        if geo._normalize(m.group(1)) == target_norm:
            start = m.start()
            end = heads[i + 1].start() if i + 1 < len(heads) else len(article_md_text)
            return article_md_text[start:end].strip()
    if is_first_section:
        # Some drafts write the intro right after the H1 title with no "## "
        # heading of its own (occasionally nested under "### " subheadings
        # instead) -- fall back to "everything before the first real '## '
        # section" rather than reporting not-found for a section that's
        # actually right there, just unlabeled.
        h1 = re.search(r"^# .+$", article_md_text, re.MULTILINE)
        start = h1.end() if h1 else 0
        end = heads[0].start() if heads else len(article_md_text)
        if end > start:
            return article_md_text[start:end].strip()
    return None


def _extract_reasoning_blocks(reasoning_json: dict, target_norm: str, ordinal_idx: int) -> dict[str, str]:
    """{dim_short: raw_block_text} for the section matching target_norm.

    3-tier fallback mirrors generate_episode_oracles.py::_get_score()'s own
    lookup strategy (exact -> substring -> ordinal), since inspection confirmed
    a real cause of title mismatch: some dimensions (cc/fl/de/be/cp) store a
    SHORTENED section-title prefix ("Introduction:") while others (ga) store
    the full title ("Introduction: The Avascular Retina Paradox:") in the same
    reasoning.json -- an exact match against the full normalized title then
    fails for the shortened ones even though both refer to the same section.
    """
    out = {}
    for dim_key, dim_short in _REVIEW_DIMS:
        text = reasoning_json.get(dim_key)
        if not text:
            continue
        blocks: list[tuple[str, str]] = []  # (norm_title, full_block_text), in appearance order
        for part in text.split("\n\n"):
            part = part.strip()
            m = re.match(r"^(.+?):\n\*\*([01]):\*\*(.*)$", part, re.DOTALL)
            if m:
                blocks.append((geo._normalize(m.group(1).strip()), part))
        if not blocks:
            continue
        match = next((b for n, b in blocks if n == target_norm), None)          # 1. exact
        if match is None:
            match = next((b for n, b in blocks if target_norm in n or n in target_norm), None)  # 2. substring
        if match is None and 0 <= ordinal_idx < len(blocks):
            match = blocks[ordinal_idx][1] + "\n_(matched by ordinal position -- title text didn't match)_"  # 3. ordinal
        if match is not None:
            out[dim_short] = match
    return out


def _load_json(path: Path) -> dict | None:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def render_summary_table(contribs: list[tuple], winner: str, runner_up: str, total_margin: float) -> str:
    """ALL sections, sorted most-against-winner first, with a running cumulative
    total -- so a reviewer sees whether sections outside the detailed top-N
    below offset or reinforce what's shown, instead of having to infer it."""
    lines = [
        f"## All sections ({winner} vs {runner_up}), most-against-{winner} first",
        "| section | weight | contribution | running total |",
        "|---|---:|---:|---:|",
    ]
    running = 0.0
    for contribution, sec_id, _norm, info in contribs:
        running += contribution
        title = sec_id.split("::")[-1][:50]
        lines.append(f"| {title} | {info.get('_weight_frac', float('nan')):.3f} | {contribution:+.4f} | {running:+.4f} |")
    lines.append(f"\n(stored article margin = {total_margin:+.4f} -- should match the running total's final row to ~4 decimals)\n")
    return "\n".join(lines)


def render_section_review(article: str, sec_id: str, target_norm: str, winner: str, runner_up: str,
                           contribution: float, weight_frac: float, avg_info: dict) -> str:
    arm_presets = mrn._arm_presets_for(article)
    direction = "AGAINST" if contribution < 0 else "FOR"
    ordinal_match = re.match(r"^S(\d+)::", sec_id)
    ordinal_idx = int(ordinal_match.group(1)) - 1 if ordinal_match else -1
    lines = [
        f"## Section: {sec_id}  (weight={weight_frac:.3f}, contribution={contribution:+.4f} {direction} {winner})",
        f"Stored section rewards: {winner}={avg_info['rewards'][winner]:.4f}  {runner_up}={avg_info['rewards'][runner_up]:.4f}"
        f"  (explore: {winner}={avg_info.get('explore', {}).get(winner, 0.0):.4f}  {runner_up}={avg_info.get('explore', {}).get(runner_up, 0.0):.4f})\n",
    ]
    for arm in (winner, runner_up):
        preset = arm_presets[arm][0]
        lines.append(f"### Arm: {arm} (preset{preset})\n")
        for draw in range(_n_draws_for(article)):
            draw_label = "production" if draw == 0 else f"replicate{draw}"
            ep_dir = _episode_dir(article, draw, preset)
            lines.append(f"#### Draw: {draw_label}  `{ep_dir}`\n")
            article_md = ep_dir / "article.md"
            if not article_md.exists():
                lines.append("_(article.md not found)_\n")
                continue
            is_first_section = sec_id.startswith("S1::")
            text = _extract_article_section(article_md.read_text(encoding="utf-8"), target_norm, is_first_section)
            lines.append("**Article text:**")
            lines.append("```\n" + (text or "(section not found by title match)") + "\n```")
            reasoning = _load_json(ep_dir / "reasoning.json")
            if reasoning is None:
                lines.append("_(reasoning.json not found)_\n")
                continue
            blocks = _extract_reasoning_blocks(reasoning, target_norm, ordinal_idx)
            lines.append("**Grader reasoning:**")
            for _, dim_short in _REVIEW_DIMS:
                block = blocks.get(dim_short, "(no matching block found)")
                lines.append(f"- `{dim_short}`: {block}")
            lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--article", required=True)
    parser.add_argument("--arms", nargs=2, metavar=("ARM_A", "ARM_B"), default=None,
                         help="Compare these two arms directly (any of skip/light/standard/deep) "
                              "instead of the default oracle_arm vs runner_up_arm.")
    parser.add_argument("--sections", nargs="+", default=None,
                         help="Section title(s) to review (fuzzy substring match). Default: auto-select.")
    parser.add_argument("--top-n", type=int, default=2,
                         help="How many sections to auto-select FROM EACH SIDE (most-against-winner "
                              "and most-for-winner), default 2 -- so up to 2*top_n sections total, "
                              "deduplicated. Ensures a large FOR-winner section (e.g. an Introduction "
                              "that decides the article) is never silently dropped just because it "
                              "happens to favor the winner rather than the runner-up.")
    parser.add_argument("--output", type=Path, default=None, help="Write to this file instead of stdout.")
    parser.add_argument("--save", action="store_true",
                         help=f"Write to {_REVIEW_OUTPUT_DIR}/<article>.md (auto-named, one file per article). "
                              "Ignored if --output is also given.")
    parser.add_argument("--append", action="store_true", help="Append to --output instead of overwriting.")
    args = parser.parse_args()

    oracle_path = _BASES_DIR / args.article / "article_oracle.json"
    if not oracle_path.exists():
        print(f"ERROR: no article_oracle.json for {args.article}")
        return
    oracle = json.loads(oracle_path.read_text(encoding="utf-8"))

    if args.arms:
        winner, runner_up = args.arms
        valid_arms = {"skip", "light", "standard", "deep"}
        if winner not in valid_arms or runner_up not in valid_arms:
            print(f"ERROR: --arms must be two of {sorted(valid_arms)}, got {args.arms!r}")
            return
        margin = oracle["r_w_rewards"][winner] - oracle["r_w_rewards"][runner_up]
    else:
        winner = oracle["oracle_arm"]
        runner_up = oracle.get("runner_up_arm")
        if runner_up is None:
            print(f"ERROR: {args.article} has no runner_up_arm (manual override or forbidden policy) -- nothing to review.")
            return
        margin = oracle["margin"]

    output_path = args.output
    if output_path is None and args.save:
        _REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        suffix = f"__{winner}_vs_{runner_up}" if args.arms else ""
        output_path = _REVIEW_OUTPUT_DIR / f"{args.article}{suffix}.md"

    contribs, total_w = _section_contributions(args.article, winner, runner_up)
    feat = json.loads((_BASES_DIR / args.article / "guideline_features.json").read_text(encoding="utf-8"))["sections"]
    for _contribution, sec_id, _norm, info in contribs:
        info["_weight_frac"] = int(feat.get(sec_id, {}).get("target_words", 100)) / total_w

    if args.sections:
        targets = []
        for want in args.sections:
            want_norm = geo._normalize(want)
            match = next((c for c in contribs if want_norm in c[2] or c[2] in want_norm), None)
            if match is None:
                print(f"WARNING: no section matched {want!r}; skipping.")
                continue
            targets.append(match)
    else:
        # contribs is sorted ascending (most-against-winner first) -- pull
        # top_n from EACH tail so a big FOR-winner section is never dropped
        # just because most-against-winner happens to fill the quota first.
        most_against = contribs[: args.top_n]
        most_for = list(reversed(contribs[-args.top_n:]))
        seen: set[str] = set()
        targets = []
        for c in most_against + most_for:
            if c[1] not in seen:
                seen.add(c[1])
                targets.append(c)

    out_lines = [f"# Near-tie review: {args.article}  ({winner} vs {runner_up}, margin={margin:+.4f})\n"]
    out_lines.append(render_summary_table(contribs, winner, runner_up, margin))
    for contribution, sec_id, norm, avg_info in targets:
        tw = int(feat.get(sec_id, {}).get("target_words", 100))
        out_lines.append(render_section_review(args.article, sec_id, norm, winner, runner_up, contribution, tw / total_w, avg_info))

    report = "\n".join(out_lines)
    if output_path:
        mode = "a" if args.append else "w"
        with output_path.open(mode, encoding="utf-8") as f:
            if args.append:
                f.write("\n\n---\n\n")
            f.write(report)
        print(f"Wrote {'(appended) ' if args.append else ''}review to {output_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
