"""Stage 0 of the "deeper Grok redesign" plan: residual-error feature audit.

Question: using ONLY data already on disk (no new corpus, no new LLM calls),
is there any cheaply-extractable feature that separates the articles where the
current RL+guards pipeline errs from the ones where it's exact? If yes, that
feature is a concrete design target for a redesigned Grok stage. If no, a
prompt/architecture redesign has no evidence-backed target to aim at yet.

Reuses the post-`_read_oracle()`-fix RL+guards TEST/TRAIN report (same source
`_run31_run33_failure_analysis.py` uses) plus each article's on-disk
`guideline_features.json` / `article_oracle(_averaged).json` / raw guideline
& digest text -- nothing here required a new inference run.

Usage:
    python3 _stage0_residual_error_feature_audit.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_BASES_DIR = _HERE.parent.parent / "rl_training_data" / "bases"
_REPORT = _HERE / "rl_guard_only_train_and_test_results_run33_averaged_confidence_epoch81.md"

_BLOCK_RE = re.compile(r"^ {2}Variant : (\S+)\s+\[(TRAIN|TEST)\]\s*$", re.M)
_POLICY_RE = re.compile(r"^ {2}Policy\s+: (\w+)\s*$", re.M)
_CHOSEN_RE = re.compile(r"^ {2}-> Chosen\s+: P(\d)\b", re.M)
_ORACLE_RE = re.compile(r"^ {2}Oracle\s+: P(\d)\b", re.M)
_RW_RE = re.compile(
    r"^ {2}R_w\s+: P0/skip:(-?[\d.]+)\s+P1/light:(-?[\d.]+)\s+"
    r"P2/standard:(-?[\d.]+)\s+P3/deep:(-?[\d.]+)\s*$", re.M
)
_THEORY_RE = re.compile(r"Theory / Practice Ratio\s*\n+\s*\**(\d+)%\s*theory", re.I)

_FEATURES = [
    "guideline_words", "digest_words", "n_sections", "total_target_words",
    "total_mandatory_bullets", "total_must_cover_depth", "total_must_stay_brief",
    "depth_brief_ratio", "margin", "abs_margin", "reward_spread", "theory_pct",
]


def _load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def build_table() -> list[dict]:
    text = _REPORT.read_text(encoding="utf-8")
    starts = [(m.start(), m.group(1), m.group(2)) for m in _BLOCK_RE.finditer(text)]
    rows = []
    for i, (pos, variant, split) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        chunk = text[pos:end]
        policy = _POLICY_RE.search(chunk).group(1)
        chosen = int(_CHOSEN_RE.search(chunk).group(1))
        oracle = int(_ORACLE_RE.search(chunk).group(1))
        rw = [float(_RW_RE.search(chunk).group(k)) for k in (1, 2, 3, 4)]

        vdir = _BASES_DIR / variant
        gf = _load_json(vdir / "guideline_features.json") or {}
        ao = _load_json(vdir / "article_oracle_averaged.json") or _load_json(vdir / "article_oracle.json") or {}
        secs = gf.get("sections", {})
        total_must_stay_brief = sum(s.get("must_stay_brief", 0) for s in secs.values())
        total_must_cover_depth = sum(s.get("must_cover_depth", 0) for s in secs.values())

        guideline_text = (vdir / "article_guideline.md").read_text(encoding="utf-8", errors="replace")
        digest_text = (vdir / "research_digest.md").read_text(encoding="utf-8", errors="replace")
        theory_m = _THEORY_RE.search(guideline_text)

        d = abs(chosen - oracle)
        verdict = "exact" if d == 0 else ("near" if d == 1 else "miss")
        regret = round(rw[oracle] - rw[chosen], 4) if policy != "forbidden" else None
        margin = ao.get("margin")

        rows.append({
            "variant": variant, "split": split, "policy": policy,
            "verdict": verdict, "abs_err": d, "regret": regret,
            "oracle": oracle, "chosen": chosen,
            "guideline_words": len(guideline_text.split()),
            "digest_words": len(digest_text.split()),
            "n_sections": len(secs),
            "total_target_words": sum(s.get("target_words", 0) for s in secs.values()),
            "total_mandatory_bullets": sum(s.get("mandatory_bullets", 0) for s in secs.values()),
            "total_must_cover_depth": total_must_cover_depth,
            "total_must_stay_brief": total_must_stay_brief,
            "depth_brief_ratio": round(total_must_cover_depth / (total_must_stay_brief + 1), 3),
            "margin": round(margin, 4) if margin is not None else None,
            "abs_margin": round(abs(margin), 4) if margin is not None else None,
            "reward_spread": round(ao.get("reward_spread"), 4) if ao.get("reward_spread") is not None else None,
            "theory_pct": int(theory_m.group(1)) if theory_m else None,
        })
    return rows


def _spearman(xs: list[float], ys: list[float]) -> float:
    def rankify(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        ranks = [0.0] * len(vals)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg_rank = (i + j) / 2 + 1
            for k in range(i, j + 1):
                ranks[order[k]] = avg_rank
            i = j + 1
        return ranks

    rx, ry = rankify(xs), rankify(ys)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sx = sum((a - mx) ** 2 for a in rx) ** 0.5
    sy = sum((b - my) ** 2 for b in ry) ** 0.5
    return cov / (sx * sy) if sx > 0 and sy > 0 else 0.0


def audit(rows: list[dict]) -> None:
    exact = [r for r in rows if r["verdict"] == "exact"]
    not_exact = [r for r in rows if r["verdict"] != "exact"]
    print(f"exact n={len(exact)}  not_exact(near+miss) n={len(not_exact)}\n")

    print("--- range overlap (exact vs error group) ---")
    for feat in _FEATURES:
        ev = sorted(r[feat] for r in exact if r[feat] is not None)
        nv = sorted(r[feat] for r in not_exact if r[feat] is not None)
        overlap = not (ev[-1] < nv[0] or nv[-1] < ev[0])
        print(f"  {feat:25s} exact=[{ev[0]:.2f},{ev[-1]:.2f}]  error=[{nv[0]:.2f},{nv[-1]:.2f}]  "
              f"{'OVERLAP' if overlap else '*** SEPARATED ***'}")

    print("\n--- Spearman rho vs abs_err (n=40) / vs regret (n=non-forbidden) ---")
    reg_rows = [r for r in rows if r["regret"] is not None]
    for feat in _FEATURES:
        xs, ys = zip(*[(r[feat], r["abs_err"]) for r in rows if r[feat] is not None])
        rho_err = _spearman(list(xs), list(ys))
        xs2, ys2 = zip(*[(r[feat], r["regret"]) for r in reg_rows if r[feat] is not None])
        rho_reg = _spearman(list(xs2), list(ys2))
        print(f"  {feat:25s} rho_vs_abs_err={rho_err:+.3f}  rho_vs_regret={rho_reg:+.3f}")


if __name__ == "__main__":
    audit(build_table())
