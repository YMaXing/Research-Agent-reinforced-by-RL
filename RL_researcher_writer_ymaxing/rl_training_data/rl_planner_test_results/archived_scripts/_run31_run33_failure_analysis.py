"""Failure-mode analysis of the run31/run33 RL-only checkpoints (A.17).

Parses the saved `rl_only_train_and_test_results_*.md` reports, re-derives every
headline metric from the per-article blocks (self-check against the report's own
footer), then characterises the failure modes and scores candidate downstream
corrections.

Discipline (per A.16 / §60.12):
  * All corrections are FIT ON TRAIN ONLY. TEST is scored held-out, never fit.
  * All model numbers are reported baseline-relative against the trivial
    majority-class predictor for that exact split.
  * Regret aggregates exclude forbidden-policy articles (their P1+ R_w is
    tainted), matching test_grok_planner.py's own convention.

Usage:
    python3 _run31_run33_failure_analysis.py
"""

from __future__ import annotations

import re
import statistics
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_BASES_DIR = _HERE.parent.parent / "rl_training_data" / "bases"

_REPORTS = {
    "run31/ep109": _HERE / "rl_only_train_and_test_results_run31_averaged_confidence_epoch109.md",
    "run33/ep81": _HERE / "rl_only_train_and_test_results_run33_averaged_confidence_epoch81.md",
}

_NAMES = {0: "skip", 1: "light", 2: "standard", 3: "deep"}

_BLOCK_RE = re.compile(r"^ {2}Variant : (\S+)\s+\[(TRAIN|TEST)\]\s*$", re.M)
_POLICY_RE = re.compile(r"^ {2}Policy\s+: (\w+)\s*$", re.M)
_RL_RE = re.compile(r"^ {2}RL model\s+: P(\d)\s+\S+\s+conf=(\d+)%\s+H=([\d.]+)bits(.*)$", re.M)
_ORACLE_RE = re.compile(r"^ {2}Oracle\s+: P(\d)\b", re.M)
_RW_RE = re.compile(
    r"^ {2}R_w\s+: P0/skip:(-?[\d.]+)\s+P1/light:(-?[\d.]+)\s+"
    r"P2/standard:(-?[\d.]+)\s+P3/deep:(-?[\d.]+)\s*$",
    re.M,
)


def parse(path: Path) -> list[dict]:
    """Parse one report into per-article records."""
    text = path.read_text(encoding="utf-8")
    starts = [(m.start(), m.group(1), m.group(2)) for m in _BLOCK_RE.finditer(text)]
    records = []
    for i, (pos, variant, split) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        chunk = text[pos:end]
        rl = _RL_RE.search(chunk)
        oracle = _ORACLE_RE.search(chunk)
        rw = _RW_RE.search(chunk)
        policy = _POLICY_RE.search(chunk)
        if not (rl and oracle and rw and policy):
            raise ValueError(f"Incomplete block for {variant} in {path.name}")
        records.append(
            {
                "variant": variant,
                "split": split,
                "policy": policy.group(1),
                "rl": int(rl.group(1)),
                "conf": int(rl.group(2)) / 100.0,
                "H": float(rl.group(3)),
                "floor": "floor applied" in rl.group(4),
                "oracle": int(oracle.group(1)),
                "r_w": [float(rw.group(k)) for k in (1, 2, 3, 4)],
            }
        )
    return records


def _corrected_r_w(variant: str) -> list[float] | None:
    """Read R_w directly from article_oracle.json. As of A.16 (2026-08-25),
    that file's own r_w_rewards_list already IS the mean-R_w across every
    available draw -- the article_oracle_averaged.json sibling file this
    used to prefer has been retired. Returns None if the file is missing
    (should not happen for corpus articles)."""
    import json as _json

    single = _BASES_DIR / variant / "article_oracle.json"
    if single.exists():
        return _json.loads(single.read_text(encoding="utf-8"))["r_w_rewards_list"]
    return None


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------
def score(records: list[dict], pick) -> dict:
    """Score a decision function `pick(rec) -> preset` over a record set."""
    exact = near = miss = 0
    abs_err = []
    regrets = []
    for r in records:
        p = pick(r)
        d = abs(p - r["oracle"])
        abs_err.append(d)
        if d == 0:
            exact += 1
        elif d == 1:
            near += 1
        else:
            miss += 1
        if r["policy"] != "forbidden":
            regrets.append(round(r["r_w"][r["oracle"]] - r["r_w"][p], 4))
    n = len(records)
    return {
        "n": n,
        "exact": exact,
        "near": near,
        "miss": miss,
        "exact_pct": 100.0 * exact / n,
        "mae": sum(abs_err) / n,
        "regret_mean": statistics.fmean(regrets) if regrets else 0.0,
        "regret_max": max(regrets) if regrets else 0.0,
        "n_regret": len(regrets),
    }


def guards(preset: int, policy: str) -> int:
    """Deterministic hard-constraint clamp (mirrors preset_planner_handler)."""
    if policy == "forbidden":
        return 0
    if policy == "required":
        return max(1, preset)
    return preset


def majority_class(records: list[dict]) -> int:
    return Counter(r["oracle"] for r in records).most_common(1)[0][0]


def escalation_guard(preset: int, rl_preset: int) -> int:
    """Current production hard block: never escalate a P0/P1 RL pick to P2+."""
    return 1 if (rl_preset <= 1 and preset >= 2) else preset


def is_unimodal(r_w: list[float]) -> bool:
    """True if R_w rises monotonically to its peak then falls (the planner
    prompt's stated 'single-peaked reward curve' assumption)."""
    peak = max(range(4), key=lambda k: r_w[k])
    up = all(r_w[i] <= r_w[i + 1] for i in range(peak))
    down = all(r_w[i] >= r_w[i + 1] for i in range(peak, 3))
    return up and down


#: A.15.1 margin risk tiers (top-2 R_w gap), reproduced here for error tagging.
def margin_tier(gap: float) -> str:
    if gap < 0.02:
        return "CRITICAL"
    if gap < 0.05:
        return "HIGH"
    if gap < 0.10:
        return "MODERATE"
    return "COMFORTABLE"


def fmt(label: str, s: dict) -> str:
    return (
        f"  {label:<34} exact={s['exact']:>2}/{s['n']:<2} ({s['exact_pct']:>4.1f}%)  "
        f"near={s['near']:>2}  miss={s['miss']:>2}  MAE={s['mae']:.3f}  "
        f"regret mean={s['regret_mean']:+.4f} max={s['regret_max']:+.4f}"
    )


# ---------------------------------------------------------------------------
def main() -> None:
    data = {k: parse(p) for k, p in _REPORTS.items()}

    for run, recs in data.items():
        print("=" * 100)
        print(f"  {run}")
        print("=" * 100)
        for split in ("TRAIN", "TEST"):
            sub = [r for r in recs if r["split"] == split]
            maj = majority_class(sub)
            print(f"\n[{split}]  n={len(sub)}   majority class = P{maj} ({_NAMES[maj]})")
            print(fmt("RL-only (as reported)", score(sub, lambda r: r["rl"])))
            print(fmt("majority-class baseline", score(sub, lambda r, m=maj: m)))
            print(fmt("RL + policy guards", score(sub, lambda r: guards(r["rl"], r["policy"]))))

        # ---- failure-mode taxonomy -------------------------------------
        print("\n--- failure modes (signed error = pick - oracle) ---")
        for split in ("TRAIN", "TEST"):
            sub = [r for r in recs if r["split"] == split]
            for scope, sel in (
                ("all", lambda r: True),
                ("policy=forbidden", lambda r: r["policy"] == "forbidden"),
                ("policy!=forbidden", lambda r: r["policy"] != "forbidden"),
            ):
                rows = [r for r in sub if sel(r)]
                if not rows:
                    continue
                errs = [r["rl"] - r["oracle"] for r in rows]
                over = sum(1 for e in errs if e > 0)
                under = sum(1 for e in errs if e < 0)
                print(
                    f"  {split:<5} {scope:<18} n={len(rows):>2}  "
                    f"over={over:>2}  exact={len(errs) - over - under:>2}  under={under:>2}  "
                    f"mean signed={statistics.fmean(errs):+.3f}"
                )

        # ---- prediction concentration ---------------------------------
        print("\n--- prediction concentration ---")
        for split in ("TRAIN", "TEST"):
            sub = [r for r in recs if r["split"] == split]
            c = Counter(r["rl"] for r in sub)
            o = Counter(r["oracle"] for r in sub)
            print(f"  {split} predicted: " + "  ".join(f"P{k}={c.get(k, 0)}" for k in range(4)))
            print(f"  {split} oracle   : " + "  ".join(f"P{k}={o.get(k, 0)}" for k in range(4)))

        # ---- vs-baseline decomposition on TEST -------------------------
        test = [r for r in recs if r["split"] == "TEST"]
        maj = majority_class(test)
        gained = [r["variant"] for r in test if r["rl"] == r["oracle"] and r["oracle"] != maj]
        lost = [r["variant"] for r in test if r["oracle"] == maj and r["rl"] != maj]
        agree = sum(1 for r in test if r["rl"] == maj)
        print(f"\n--- TEST vs majority baseline (P{maj}) ---")
        print(f"  predictions identical to baseline : {agree}/{len(test)} ({100 * agree / len(test):.0f}%)")
        print(f"  gained (non-P{maj} article got right): {gained}")
        print(f"  lost   (P{maj} article got wrong)    : {lost}")

        # ---- label-vs-reward disagreement ------------------------------
        print("\n--- articles where oracle != argmax(R_w)  [manual overrides] ---")
        for r in recs:
            am = max(range(4), key=lambda k: r["r_w"][k])
            if am != r["oracle"] and r["policy"] != "forbidden":
                print(
                    f"  {r['split']:<5} {r['variant']:<45} oracle=P{r['oracle']} "
                    f"argmax(R_w)=P{am}  RL=P{r['rl']}  "
                    f"regret={r['r_w'][r['oracle']] - r['r_w'][r['rl']]:+.4f}"
                )

        # ---- TEST error detail ----------------------------------------
        print("\n--- TEST errors, RL+guards applied ---")
        for r in test:
            p = guards(r["rl"], r["policy"])
            if p == r["oracle"]:
                continue
            margin = sorted(r["r_w"], reverse=True)
            print(
                f"  {r['variant']:<32} RL=P{p} oracle=P{r['oracle']} "
                f"({'over ' if p > r['oracle'] else 'under'} by {abs(p - r['oracle'])})  "
                f"conf={r['conf']:.0%} H={r['H']:.2f}  "
                f"regret={r['r_w'][r['oracle']] - r['r_w'][p]:+.4f}  "
                f"R_w top-2 margin={margin[0] - margin[1]:.4f}"
            )
        print()

    # -----------------------------------------------------------------------
    # Cross-run stability
    # -----------------------------------------------------------------------
    print("=" * 100)
    print("  CROSS-RUN STABILITY (run31/ep109 vs run33/ep81)")
    print("=" * 100)
    a = {r["variant"]: r for r in data["run31/ep109"]}
    b = {r["variant"]: r for r in data["run33/ep81"]}
    for split in ("TRAIN", "TEST"):
        keys = [k for k in a if a[k]["split"] == split]
        same = sum(1 for k in keys if a[k]["rl"] == b[k]["rl"])
        print(f"  {split}: identical predictions on {same}/{len(keys)} ({100 * same / len(keys):.0f}%)")
        for k in keys:
            if a[k]["rl"] != b[k]["rl"]:
                print(
                    f"     {k:<45} run31=P{a[k]['rl']}  run33=P{b[k]['rl']}  oracle=P{a[k]['oracle']}"
                )

    # -----------------------------------------------------------------------
    # TRAIN-fit correction rules, scored held-out on TEST
    # -----------------------------------------------------------------------
    print()
    print("=" * 100)
    print("  TRAIN-FIT CORRECTION RULES  (fit on TRAIN only; TEST is held out)")
    print("=" * 100)

    def rule_guards(r):
        return guards(r["rl"], r["policy"])

    def rule_guards_plus_lowconf_demote(r, thr):
        """After guards: a low-confidence P2+ pick steps down one level."""
        p = guards(r["rl"], r["policy"])
        if r["policy"] != "forbidden" and p >= 2 and r["conf"] < thr:
            return p - 1
        return p

    def rule_guards_plus_lowconf_escalate(r, thr):
        """After guards: a low-confidence P1 pick steps up one level."""
        p = guards(r["rl"], r["policy"])
        if r["policy"] != "forbidden" and p == 1 and r["conf"] < thr:
            return p + 1
        return p

    for run, recs in data.items():
        train = [r for r in recs if r["split"] == "TRAIN"]
        test = [r for r in recs if r["split"] == "TEST"]
        print(f"\n### {run}")
        print("  [TRAIN fit]")
        print(fmt("guards only", score(train, rule_guards)))
        best = {}
        for thr in (0.30, 0.40, 0.50, 0.60, 0.70):
            s_d = score(train, lambda r, t=thr: rule_guards_plus_lowconf_demote(r, t))
            s_e = score(train, lambda r, t=thr: rule_guards_plus_lowconf_escalate(r, t))
            print(fmt(f"guards + demote P2+ if conf<{thr:.2f}", s_d))
            print(fmt(f"guards + escal. P1  if conf<{thr:.2f}", s_e))
            best[("demote", thr)] = s_d
            best[("escal", thr)] = s_e
        winner = max(best.items(), key=lambda kv: (kv[1]["exact"], -kv[1]["mae"]))
        base_train = score(train, rule_guards)
        print(f"  -> best TRAIN rule: {winner[0]}  (exact {winner[1]['exact']} vs guards-only {base_train['exact']})")
        print("  [TEST held-out]")
        print(fmt("guards only", score(test, rule_guards)))
        kind, thr = winner[0]
        f = rule_guards_plus_lowconf_demote if kind == "demote" else rule_guards_plus_lowconf_escalate
        print(fmt(f"best TRAIN rule ({kind} conf<{thr:.2f})", score(test, lambda r, t=thr: f(r, t))))

    # -----------------------------------------------------------------------
    # Reward-curve shape: does the planner prompt's "single-peaked" claim hold?
    # -----------------------------------------------------------------------
    print()
    print("=" * 100)
    print("  REWARD-CURVE DIAGNOSTICS  (R_w is checkpoint-independent; computed once)")
    print("=" * 100)
    recs = data["run33/ep81"]
    for split in ("TRAIN", "TEST"):
        sub = [r for r in recs if r["split"] == split and r["policy"] != "forbidden"]
        uni = [r for r in sub if is_unimodal(r["r_w"])]
        print(f"  {split}: single-peaked R_w curve in {len(uni)}/{len(sub)} "
              f"({100 * len(uni) / len(sub):.0f}%) non-forbidden articles")
        for r in sub:
            if not is_unimodal(r["r_w"]):
                print(f"     NOT unimodal: {r['variant']:<42} "
                      + " ".join(f"P{k}={r['r_w'][k]:+.3f}" for k in range(4)))

    print("\n  --- TEST margin-risk tier of every article (A.15.1 reproduction) ---")
    for r in [x for x in recs if x["split"] == "TEST"]:
        srt = sorted(r["r_w"], reverse=True)
        gap = srt[0] - srt[1]
        print(f"     {r['variant']:<34} margin={gap:.4f}  {margin_tier(gap)}")

    # -----------------------------------------------------------------------
    # Regret-budget concentration + escalation-guard blocking
    # -----------------------------------------------------------------------
    print()
    print("=" * 100)
    print("  WHERE THE REGRET ACTUALLY LIVES, AND WHAT THE ESCALATION GUARD BLOCKS")
    print("=" * 100)
    for run, recs in data.items():
        test = [r for r in recs if r["split"] == "TEST"]
        rows = []
        for r in test:
            if r["policy"] == "forbidden":
                continue
            p = guards(r["rl"], r["policy"])
            rows.append((r["variant"], r["r_w"][r["oracle"]] - r["r_w"][p], p, r))
        total = sum(x[1] for x in rows)
        rows.sort(key=lambda x: -x[1])
        print(f"\n### {run}   total TEST regret (after guards) = {total:+.4f} over n={len(rows)}")
        for name, g, p, r in rows:
            if abs(g) < 1e-9:
                continue
            blocked = escalation_guard(r["oracle"], p) != r["oracle"]
            print(
                f"   {name:<34} regret={g:+.4f} ({100 * g / total:+5.1f}% of budget)  "
                f"RL=P{p}->oracle=P{r['oracle']}  "
                f"{'BLOCKED by escalation guard' if blocked else 'reachable by Grok'}"
            )

    # -----------------------------------------------------------------------
    # Fittability: how much TRAIN error signal exists to fit a corrector on?
    # -----------------------------------------------------------------------
    print()
    print("=" * 100)
    print("  FITTABILITY OF A TRAIN-FIT DOWNSTREAM CORRECTOR")
    print("=" * 100)
    for run, recs in data.items():
        print(f"\n### {run}")
        for split in ("TRAIN", "TEST"):
            sub = [r for r in recs if r["split"] == split]
            errs = [
                r for r in sub
                if guards(r["rl"], r["policy"]) != r["oracle"] and r["policy"] != "forbidden"
            ]
            trans = Counter(
                (guards(r["rl"], r["policy"]), r["oracle"]) for r in errs
            )
            n_nf = sum(1 for r in sub if r["policy"] != "forbidden")
            print(
                f"  {split}: {len(errs)} correctable errors out of {n_nf} non-forbidden "
                f"articles  (this is the ENTIRE corpus a downstream rule can be fit on)"
            )
            for (p, o), c in sorted(trans.items()):
                print(f"       P{p} -> P{o}   x{c}")

    # -----------------------------------------------------------------------
    # Significance of RL+guards vs the trivial baseline (McNemar exact, n=16)
    # -----------------------------------------------------------------------
    print()
    print("=" * 100)
    print("  IS 'RL + GUARDS' SIGNIFICANTLY BETTER THAN THE TRIVIAL BASELINE ON TEST?")
    print("=" * 100)
    from math import comb

    for run, recs in data.items():
        test = [r for r in recs if r["split"] == "TEST"]
        maj = majority_class(test)
        b = sum(
            1 for r in test
            if guards(r["rl"], r["policy"]) == r["oracle"] and maj != r["oracle"]
        )
        c = sum(
            1 for r in test
            if guards(r["rl"], r["policy"]) != r["oracle"] and maj == r["oracle"]
        )
        n = b + c
        p_one = sum(comb(n, k) for k in range(b, n + 1)) / (2 ** n) if n else 1.0
        print(
            f"  {run:<14} model-right/baseline-wrong={b}  baseline-right/model-wrong={c}  "
            f"exact binomial one-sided p={p_one:.3f}  "
            f"{'SIGNIFICANT' if p_one < 0.05 else 'NOT significant at n=16'}"
        )

    # -----------------------------------------------------------------------
    # Corrected regret: re-derive R_w the way the fixed _read_oracle() does
    # (prefer article_oracle_averaged.json), keep everything else (RL picks,
    # oracle labels, policy) as reported. No new inference needed -- the
    # model's choices don't change, only which R_w they're scored against.
    # -----------------------------------------------------------------------
    print()
    print("=" * 100)
    print("  CORRECTED REGRET (R_w sourced from article_oracle_averaged.json when present)")
    print("=" * 100)
    for run, recs in data.items():
        print(f"\n### {run}")
        for split in ("TRAIN", "TEST"):
            sub = [r for r in recs if r["split"] == split]
            corrected = []
            n_missing = 0
            for r in sub:
                cr = _corrected_r_w(r["variant"])
                if cr is None:
                    n_missing += 1
                    cr = r["r_w"]
                corrected.append({**r, "r_w": cr})
            s_before = score(sub, lambda r: guards(r["rl"], r["policy"]))
            s_after = score(corrected, lambda r: guards(r["rl"], r["policy"]))
            tag = f" ({n_missing} article(s) had no on-disk oracle file, kept as-reported)" if n_missing else ""
            print(
                f"  {split}: regret mean {s_before['regret_mean']:+.4f} -> {s_after['regret_mean']:+.4f}   "
                f"max {s_before['regret_max']:+.4f} -> {s_after['regret_max']:+.4f}{tag}"
            )
            for r, cr in zip(sub, corrected):
                if r["policy"] == "forbidden":
                    continue
                p = guards(r["rl"], r["policy"])
                before = r["r_w"][r["oracle"]] - r["r_w"][p]
                after = cr["r_w"][r["oracle"]] - cr["r_w"][p]
                if abs(before - after) > 0.005:
                    print(f"     {r['variant']:<42} regret {before:+.4f} -> {after:+.4f}")


if __name__ == "__main__":
    main()
