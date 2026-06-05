"""Prototype: complementary signals for the 4-preset article-level oracle.

Goal
----
The target-words-weighted reward (R_w) is a strong baseline for choosing the
article-level exploration preset (skip / light / standard / deep), but it is
built purely from per-section *binary* judge scores.  It is therefore blind to
article-level phenomena: whether an extra exploration round actually changed the
article (marginal value), redundancy/bloat, objective structural compliance, and
run-to-run stability.

This script prototypes the complementary extractors discussed in the design
review and shows, per article-variant, whether they would FLIP the reward-only
oracle.  It is deliberately self-contained and read-only — it writes nothing.

Signals
-------
  R_w  reward-only baseline   target_words-weighted section_oracle.json v2 rewards
  S1   marginal knee          semantic novelty added by each exploration round
  S2   intra-article redundancy   near-duplicate paragraph fraction
  S3   length bloat           article words vs guideline target words
  S4   structural compliance  bullets / depth markers vs guideline_features.json
  S5   run-to-run stability   variance across the 3 generation runs
  S6   research utilization   grounding + source-coverage (embeddings)
  S7   concept coverage       guideline bullet concepts present in article (embeddings)

Embedding backend
-----------------
S1, S2, S6, S7 need a text-similarity function.  The backend is pluggable via
``--embedder``:

  * ``hf`` (default)  mean-pooled BAAI/bge-small-en-v1.5 embeddings (semantic).
    Captures paraphrase and conceptual similarity.  Requires torch + transformers
    (present in the training venv).  Model is ~90 MB and cached after first run.
  * ``tfidf``  pure-numpy TF-IDF cosine.  Zero downloads, deterministic, runs
    anywhere numpy is present.  Lexical proxy only: captures verbatim overlap
    well but under-detects paraphrase.

Usage (from research_agent_local/training/, training venv):
    .venv/bin/python prototype_oracle_signals.py                 # 3 sample variants + summary
    .venv/bin/python prototype_oracle_signals.py --article 09_RAG__var_demanding
    .venv/bin/python prototype_oracle_signals.py --all           # all 21 variants
    .venv/bin/python prototype_oracle_signals.py --embedder tfidf
    .venv/bin/python prototype_oracle_signals.py --model BAAI/bge-large-en-v1.5
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _THIS_DIR.parent
_REPO_ROOT = _AGENT_DIR.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"

# ---------------------------------------------------------------------------
# Preset vocabulary  (4-preset scheme; episode preset id -> arm)
# ---------------------------------------------------------------------------
ARMS = ["skip", "light", "standard", "deep"]
ARM_EPISODE = {"skip": 0, "light": 1, "standard": 3, "deep": 5}  # archived: 2, 4
ARM_ROUNDS = {"skip": 0, "light": 1, "standard": 2, "deep": 3}

# ---------------------------------------------------------------------------
# Decision constants  (documented, tunable)
# ---------------------------------------------------------------------------
EPS_BAND = 0.02          # arms within EPS of max R_w form the near-tie band
KNEE_TAU_TFIDF = 0.08    # marginal novelty below this => extra round "not worth it"
KNEE_TAU_HF = 0.04       # semantic embeddings: deltas are smaller, lower threshold
REDUNDANT_SIM = 0.85     # paragraph cosine above this => near-duplicate (semantic)
REDUNDANT_SIM_TFIDF = 0.55  # TF-IDF cosines run lower; looser duplicate threshold
S4_BULLET_W = 0.6        # structural-compliance weight: bullets vs depth markers
S4_DEPTH_W = 0.4

# Minimum meaningful signal difference to act on in tie-breakers.
# If the best and worst band-member differ by less than this on a signal,
# that signal is too noisy to decide — fall through to the next.
MIN_DELTA_S4 = 0.05      # S4 structural-compliance gap must be >= this to prefer
MIN_DELTA_S3 = 0.10      # S3 bloat ratio gap must be >= this to prefer
MIN_DELTA_S2 = 0.10      # S2 redundancy fraction gap >= this to prefer
MIN_DELTA_S5 = 0.05      # S5 stability gap >= this to prefer

# A variant is flagged needs_review when it enters a near-tie AND
# every tie-breaking signal falls within its MIN_DELTA threshold (genuinely
# ambiguous) OR when TF-IDF and HF backends produced a different winner.
NEEDS_REVIEW_BAND_THRESHOLD = EPS_BAND  # same as tie-break entry condition


# ===========================================================================
# Embedding backends  (pluggable;  embed(texts) -> L2-normalized np.ndarray)
# ===========================================================================
class TfidfEmbedder:
    """Pure-numpy TF-IDF cosine.  Corpus-relative; build one per comparison set."""

    name = "tfidf"
    knee_tau = KNEE_TAU_TFIDF
    redundant_sim = REDUNDANT_SIM_TFIDF

    _TOKEN = re.compile(r"[a-z0-9]+")

    def embed(self, texts: list[str]) -> np.ndarray:
        toks = [self._TOKEN.findall(t.lower()) for t in texts]
        vocab: dict[str, int] = {}
        for tk in toks:
            for w in tk:
                if w not in vocab:
                    vocab[w] = len(vocab)
        n, v = len(texts), len(vocab)
        if v == 0:
            return np.zeros((n, 1), dtype=np.float64)
        tf = np.zeros((n, v), dtype=np.float64)
        for i, tk in enumerate(toks):
            for w in tk:
                tf[i, vocab[w]] += 1.0
        df = (tf > 0).sum(axis=0)
        idf = np.log((1.0 + n) / (1.0 + df)) + 1.0
        x = tf * idf
        norms = np.linalg.norm(x, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return x / norms


class HFEmbedder:
    """Mean-pooled transformer embeddings (semantic).  Optional backend."""

    def __init__(self, model_name: str):
        import torch
        from transformers import AutoModel, AutoTokenizer

        self.name = f"hf:{model_name}"
        self.knee_tau = KNEE_TAU_HF
        self.redundant_sim = REDUNDANT_SIM
        self._torch = torch
        self._tok = AutoTokenizer.from_pretrained(model_name)
        self._model = AutoModel.from_pretrained(model_name)
        self._model.eval()
        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        self._model.to(self._device)

    def embed(self, texts: list[str]) -> np.ndarray:
        torch = self._torch
        out: list[np.ndarray] = []
        with torch.no_grad():
            for i in range(0, len(texts), 16):
                batch = texts[i : i + 16]
                enc = self._tok(
                    batch, padding=True, truncation=True, max_length=512,
                    return_tensors="pt",
                ).to(self._device)
                hidden = self._model(**enc).last_hidden_state  # (B, T, H)
                mask = enc["attention_mask"].unsqueeze(-1).float()
                pooled = (hidden * mask).sum(1) / mask.sum(1).clamp(min=1e-9)
                pooled = torch.nn.functional.normalize(pooled, dim=-1)
                out.append(pooled.cpu().numpy())
        return np.vstack(out) if out else np.zeros((0, 1))


# ===========================================================================
# Text helpers
# ===========================================================================
_BULLET_RE = re.compile(r"^\s*([-*+]|\d+[.)])\s+\S", re.MULTILINE)
_HEADING_RE = re.compile(r"^(#{1,6})\s+\S", re.MULTILINE)
_SUBHEAD_RE = re.compile(r"^#{3,6}\s+\S", re.MULTILINE)
_CODEFENCE_RE = re.compile(r"```")


def _read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return p.read_text(encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        return ""


def _para_chunks(text: str, min_words: int = 15) -> list[str]:
    parts = [p.strip() for p in re.split(r"\n\s*\n", text)]
    return [p for p in parts if len(p.split()) >= min_words]


def _window_chunks(text: str, size: int = 400, cap: int = 200) -> list[str]:
    words = text.split()
    chunks = [" ".join(words[i : i + size]) for i in range(0, len(words), size)]
    return chunks[:cap]


def _guideline_bullets(text: str, cap: int = 60) -> list[str]:
    """Extract bullet-point requirement strings from article_guideline.md."""
    out: list[str] = []
    for m in re.finditer(r"^\s*[-*+]\s+(.+)$", text, re.MULTILINE):
        s = m.group(1).strip()
        if len(s.split()) >= 3:
            out.append(s)
    return out[:cap]


def _word_count(text: str) -> int:
    return len(text.split())


# ===========================================================================
# Data container
# ===========================================================================
@dataclass
class ArmData:
    arm: str
    article: str = ""              # final article.md text
    runs: list[str] = field(default_factory=list)  # article_000/001/002.md
    research: str = ""             # research.md (source corpus)
    present: bool = False


@dataclass
class VariantData:
    name: str
    variant_level: str
    section_rewards: dict[str, dict[str, float]]   # sec_id -> arm -> reward
    target_words: dict[str, int]                   # sec_id -> target words
    mandatory_bullets: int
    must_cover_depth: int
    guideline_bullets: list[str]
    arms: dict[str, ArmData]


# ===========================================================================
# Loading
# ===========================================================================
def _variant_level(article: str) -> str:
    if "__var_minimal" in article:
        return "minimal"
    if "__var_demanding" in article:
        return "demanding"
    return "standard"


def load_variant(article: str) -> VariantData | None:
    base = _BASES_DIR / article
    so_path = base / "section_oracle.json"
    gf_path = base / "guideline_features.json"
    if not so_path.exists() or not gf_path.exists():
        return None

    so = json.loads(_read(so_path))
    gf = json.loads(_read(gf_path))
    sec_rewards = {sid: info["rewards"] for sid, info in so.get("sections", {}).items()}
    gf_secs = gf.get("sections", {})
    target_words = {sid: int(s.get("target_words", 0)) for sid, s in gf_secs.items()}
    mand = sum(int(s.get("mandatory_bullets", 0)) for s in gf_secs.values())
    depth = sum(int(s.get("must_cover_depth", 0)) for s in gf_secs.values())
    g_bullets = _guideline_bullets(_read(base / "article_guideline.md"))

    arms: dict[str, ArmData] = {}
    for arm, ep in ARM_EPISODE.items():
        ep_dir = _EPISODES_DIR / f"{article}__preset{ep}"
        ad = ArmData(arm=arm)
        final = ep_dir / "article.md"
        if final.exists():
            ad.article = _read(final)
            ad.runs = [
                _read(ep_dir / f"article_{i:03d}.md")
                for i in range(3)
                if (ep_dir / f"article_{i:03d}.md").exists()
            ]
            ad.research = _read(ep_dir / "research.md")
            ad.present = bool(ad.article.strip())
        arms[arm] = ad

    return VariantData(
        name=article,
        variant_level=_variant_level(article),
        section_rewards=sec_rewards,
        target_words=target_words,
        mandatory_bullets=mand,
        must_cover_depth=depth,
        guideline_bullets=g_bullets,
        arms=arms,
    )


# ===========================================================================
# R_w  — reward-only baseline (target-words-weighted)
# ===========================================================================
def reward_only(v: VariantData) -> dict[str, float]:
    total = sum(v.target_words.get(sid, 0) for sid in v.section_rewards) or 1
    out: dict[str, float] = {}
    for arm in ARMS:
        acc = 0.0
        for sid, rew in v.section_rewards.items():
            w = v.target_words.get(sid, 0)
            acc += w * float(rew.get(arm, 0.0))
        out[arm] = acc / total
    return out


# ===========================================================================
# S1 — marginal knee  (semantic novelty added per exploration round)
# ===========================================================================
def s1_marginal_knee(v: VariantData, emb) -> dict:
    docs, present_arms = [], []
    for arm in ARMS:
        ad = v.arms[arm]
        if ad.present:
            docs.append(ad.article)
            present_arms.append(arm)
    if len(docs) < 2:
        return {"deltas": {}, "cheapest_sufficient": present_arms[-1] if present_arms else "skip"}

    X = emb.embed(docs)
    deltas: dict[str, float] = {}
    for i in range(1, len(present_arms)):
        cos = float(np.dot(X[i], X[i - 1]))
        deltas[present_arms[i]] = round(1.0 - cos, 4)  # novelty vs previous arm

    # Cheapest arm past which every subsequent round adds < tau novelty.
    cheapest = present_arms[-1]
    for i in range(1, len(present_arms)):
        if all(deltas[present_arms[j]] < emb.knee_tau for j in range(i, len(present_arms))):
            cheapest = present_arms[i - 1]
            break
    return {"deltas": deltas, "cheapest_sufficient": cheapest}


# ===========================================================================
# S2 — intra-article redundancy  (near-duplicate paragraph fraction)
# ===========================================================================
def s2_redundancy(v: VariantData, emb) -> dict[str, float]:
    out: dict[str, float] = {}
    for arm in ARMS:
        ad = v.arms[arm]
        if not ad.present:
            out[arm] = float("nan")
            continue
        chunks = _para_chunks(ad.article)
        if len(chunks) < 3:
            out[arm] = 0.0
            continue
        X = emb.embed(chunks)
        sim = X @ X.T
        np.fill_diagonal(sim, 0.0)
        max_off = sim.max(axis=1)
        out[arm] = round(float((max_off > emb.redundant_sim).mean()), 4)
    return out


# ===========================================================================
# S3 — length bloat  (article words vs guideline target words)
# ===========================================================================
def s3_bloat(v: VariantData) -> dict[str, float]:
    total_target = sum(v.target_words.values()) or 1
    out: dict[str, float] = {}
    for arm in ARMS:
        ad = v.arms[arm]
        out[arm] = round(_word_count(ad.article) / total_target, 3) if ad.present else float("nan")
    return out


# ===========================================================================
# S4 — structural compliance  (bullets + depth markers vs guideline_features)
# ===========================================================================
def s4_structure(v: VariantData) -> dict[str, float]:
    exp_b = max(v.mandatory_bullets, 1)
    exp_d = max(v.must_cover_depth, 1)
    out: dict[str, float] = {}
    for arm in ARMS:
        ad = v.arms[arm]
        if not ad.present:
            out[arm] = float("nan")
            continue
        found_b = len(_BULLET_RE.findall(ad.article))
        depth_markers = (
            len(_SUBHEAD_RE.findall(ad.article))
            + (len(_CODEFENCE_RE.findall(ad.article)) // 2)
        )
        bullet_score = min(1.0, found_b / exp_b)
        depth_score = min(1.0, depth_markers / exp_d)
        out[arm] = round(S4_BULLET_W * bullet_score + S4_DEPTH_W * depth_score, 4)
    return out


# ===========================================================================
# S5 — run-to-run stability  (variance across the 3 generation runs)
# ===========================================================================
def _cv(values: list[float]) -> float:
    arr = np.asarray(values, dtype=np.float64)
    m = arr.mean()
    return float(arr.std() / m) if m > 0 else 0.0


def s5_stability(v: VariantData) -> dict[str, float]:
    out: dict[str, float] = {}
    for arm in ARMS:
        ad = v.arms[arm]
        if not ad.present or len(ad.runs) < 2:
            out[arm] = float("nan")
            continue
        wc = [_word_count(r) for r in ad.runs]
        hc = [len(_HEADING_RE.findall(r)) for r in ad.runs]
        bc = [len(_BULLET_RE.findall(r)) for r in ad.runs]
        mean_cv = np.mean([_cv(wc), _cv(hc), _cv(bc)])
        out[arm] = round(float(max(0.0, 1.0 - mean_cv)), 4)
    return out


# ===========================================================================
# S6 — research utilization  (grounding + source coverage via embeddings)
# ===========================================================================
def s6_research(v: VariantData, emb) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for arm in ARMS:
        ad = v.arms[arm]
        if not ad.present or not ad.research.strip():
            out[arm] = {"grounding": float("nan"), "utilization": float("nan")}
            continue
        art_chunks = _para_chunks(ad.article)
        res_chunks = _window_chunks(ad.research, size=400, cap=200)
        if not art_chunks or not res_chunks:
            out[arm] = {"grounding": float("nan"), "utilization": float("nan")}
            continue
        joint = emb.embed(art_chunks + res_chunks)  # shared vocab/space
        A = joint[: len(art_chunks)]
        R = joint[len(art_chunks) :]
        sim = A @ R.T                                # (n_art, n_res)
        grounding = float(sim.max(axis=1).mean())    # are article chunks supported?
        utilization = float(sim.max(axis=0).mean())  # is collected research used?
        out[arm] = {"grounding": round(grounding, 4), "utilization": round(utilization, 4)}
    return out


# ===========================================================================
# S7 — concept coverage  (guideline bullet concepts present in article)
# ===========================================================================
def s7_concept_coverage(v: VariantData, emb) -> dict[str, float]:
    out: dict[str, float] = {}
    if not v.guideline_bullets:
        return {arm: float("nan") for arm in ARMS}
    for arm in ARMS:
        ad = v.arms[arm]
        if not ad.present:
            out[arm] = float("nan")
            continue
        art_chunks = _para_chunks(ad.article)
        if not art_chunks:
            out[arm] = float("nan")
            continue
        joint = emb.embed(v.guideline_bullets + art_chunks)
        C = joint[: len(v.guideline_bullets)]
        A = joint[len(v.guideline_bullets) :]
        sim = C @ A.T                                # (n_concept, n_art)
        out[arm] = round(float(sim.max(axis=1).mean()), 4)  # mean best-match per concept
    return out


# ===========================================================================
# Tiered decision
# ===========================================================================
def _has_actionable_delta(band: list[str], signal: dict[str, float], min_delta: float) -> bool:
    """Return True iff the best and worst band-member differ by >= min_delta.

    If not, the signal is within noise and should be skipped as a decider.
    """
    vals = [signal[a] for a in band if signal[a] == signal[a]]  # drop NaN
    if len(vals) < 2:
        return False
    return (max(vals) - min(vals)) >= min_delta


def decide(v: VariantData, emb) -> dict:
    rw = reward_only(v)
    present = [a for a in ARMS if v.arms[a].present]
    if not present:
        return {"error": "no episodes present"}

    reward_oracle = max(present, key=lambda a: rw[a])
    best = rw[reward_oracle]
    band = [a for a in present if best - rw[a] <= EPS_BAND]

    s1 = s1_marginal_knee(v, emb)
    s2 = s2_redundancy(v, emb)
    s3 = s3_bloat(v)
    s4 = s4_structure(v)
    s5 = s5_stability(v)
    s6 = s6_research(v, emb)
    s7 = s7_concept_coverage(v, emb)

    def _safe(x: float, default: float) -> float:
        return default if (x != x) else x  # NaN guard

    if len(band) == 1:
        final, reason = band[0], "unique reward winner (no near-tie)"
        needs_review = False
    else:
        knee = s1["cheapest_sufficient"]

        # Determine which signals have enough spread across band arms to act on.
        s4_active = _has_actionable_delta(band, s4, MIN_DELTA_S4)
        s3_active = _has_actionable_delta(band, s3, MIN_DELTA_S3)
        s2_active = _has_actionable_delta(band, s2, MIN_DELTA_S2)
        s5_active = _has_actionable_delta(band, s5, MIN_DELTA_S5)
        any_active = s4_active or s3_active or s2_active or s5_active

        # Assign tie-break priority scores per arm.  Inactive signals contribute
        # a constant (no discrimination); active signals contribute their value.
        def key(arm: str):
            return (
                0 if arm == knee else 1,                         # S1: cheapest-sufficient (always used)
                -(_safe(s4[arm], 0.0) if s4_active else 0.0),   # S4: higher compliance (if active)
                (_safe(s3[arm], 9.9) if s3_active else 0.0),    # S3: lower bloat (if active)
                (_safe(s2[arm], 9.9) if s2_active else 0.0),    # S2: lower redundancy (if active)
                -(_safe(s5[arm], 0.0) if s5_active else 0.0),   # S5: higher stability (if active)
                ARMS.index(arm),                                 # cheaper preset on full tie
            )

        final = min(band, key=key)

        # needs_review: genuinely ambiguous — no signal had actionable delta,
        # meaning all tie-breakers are within noise on this variant.
        needs_review = not any_active

        active_labels = [
            s for s, flag in [
                ("S1-knee", True),
                (f"S4(Δ≥{MIN_DELTA_S4})", s4_active),
                (f"S3(Δ≥{MIN_DELTA_S3})", s3_active),
                (f"S2(Δ≥{MIN_DELTA_S2})", s2_active),
                (f"S5(Δ≥{MIN_DELTA_S5})", s5_active),
            ] if flag
        ]
        inactive_labels = [
            s for s, flag in [
                ("S4", not s4_active), ("S3", not s3_active),
                ("S2", not s2_active), ("S5", not s5_active),
            ] if flag
        ]
        bits = [f"active=[{', '.join(active_labels)}]"]
        if inactive_labels:
            bits.append(f"below-delta=[{', '.join(inactive_labels)}]")
        bits.append(f"S4={_safe(s4[final],0):.3f}")
        bits.append(f"S3={_safe(s3[final],0):.3f}")
        reason = f"tie-break among {band}: " + "  ".join(bits)
        if needs_review:
            reason = f"[NEEDS REVIEW — all tie-breakers within noise]  band={band}"

    return {
        "rw": rw,
        "reward_oracle": reward_oracle,
        "margin": round(best - max((rw[a] for a in present if a != reward_oracle), default=best), 4),
        "band": band,
        "final": final,
        "flip": final != reward_oracle,
        "needs_review": needs_review,
        "reason": reason,
        "S1": s1, "S2": s2, "S3": s3, "S4": s4, "S5": s5, "S6": s6, "S7": s7,
    }


# ===========================================================================
# Reporting
# ===========================================================================
def _fmt_row(label: str, d: dict[str, float]) -> str:
    cells = []
    for a in ARMS:
        x = d.get(a, float("nan"))
        cells.append(f"{a[:4]:>4}={'  n/a' if x != x else f'{x:6.3f}'}")
    return f"  {label:<22} " + "  ".join(cells)


def report(v: VariantData, res: dict) -> None:
    print("=" * 78)
    print(f"{v.name}   (variant={v.variant_level})")
    print("-" * 78)
    if "error" in res:
        print("  ", res["error"])
        return
    print(_fmt_row("R_w (reward-only)", res["rw"]))
    print(f"  reward-only oracle : {res['reward_oracle']:<9}  margin={res['margin']:+.4f}  band={res['band']}")
    print()
    print(_fmt_row("S3 bloat (×target)", res["S3"]))
    print(_fmt_row("S4 structure [0-1]", res["S4"]))
    print(_fmt_row("S5 stability [0-1]", res["S5"]))
    print(_fmt_row("S2 redundancy frac", res["S2"]))
    print(_fmt_row("S6 grounding", {a: res["S6"][a]["grounding"] for a in ARMS}))
    print(_fmt_row("S6 utilization", {a: res["S6"][a]["utilization"] for a in ARMS}))
    print(_fmt_row("S7 concept cover", res["S7"]))
    s1 = res["S1"]
    print(f"  S1 novelty deltas  : {s1['deltas']}   knee→ cheapest_sufficient={s1['cheapest_sufficient']}")
    print()
    flip_tag = "  >>> FLIP" if res["flip"] else "  (no flip)"
    review_tag = "  *** NEEDS REVIEW ***" if res.get("needs_review") else ""
    print(f"  FINAL ORACLE       : {res['final']:<9}{flip_tag}{review_tag}")
    print(f"  reason             : {res['reason']}")


# ===========================================================================
# Main
# ===========================================================================
_DEFAULT_SAMPLES = [
    "03_context_engineering__var_standard",
    "02_workflows_vs_agents__var_minimal",
    "09_RAG__var_demanding",
]

_ALL_ARTICLES = [
    f"{base}__{var}"
    for base in [
        "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
        "06_tools", "08_react_practice", "09_RAG", "10_memory_knowledge_access",
        "11_multimodal",
    ]
    for var in ["var_minimal", "var_standard", "var_demanding"]
]


_DEFAULT_HF_MODEL = "BAAI/bge-small-en-v1.5"


def build_embedder(kind: str, model: str | None):
    if kind == "tfidf":
        return TfidfEmbedder()
    # Default: semantic HF embedder.
    return HFEmbedder(model or _DEFAULT_HF_MODEL)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article", help="single article-variant")
    ap.add_argument("--all", action="store_true", help="detailed report for every variant")
    ap.add_argument("--embedder", choices=["tfidf", "hf"], default="hf",
                    help="embedding backend (default: hf)")
    ap.add_argument("--model", help=f"HF model name (default: {_DEFAULT_HF_MODEL})")
    args = ap.parse_args()

    emb = build_embedder(args.embedder, args.model)
    print(f"embedder = {emb.name}\n")

    if args.article:
        targets = [args.article]
    elif args.all:
        targets = _ALL_ARTICLES
    else:
        targets = _DEFAULT_SAMPLES

    flips = 0
    reviews = 0
    band_sizes: list[int] = []
    evaluated = 0
    for art in targets:
        v = load_variant(art)
        if v is None:
            print(f"(skip {art}: missing section_oracle/guideline_features)")
            continue
        res = decide(v, emb)
        report(v, res)
        print()
        if "error" not in res:
            evaluated += 1
            band_sizes.append(len(res["band"]))
            flips += int(res["flip"])
            reviews += int(res.get("needs_review", False))

    if evaluated:
        print("=" * 78)
        print(f"SUMMARY  evaluated={evaluated}  flips={flips} "
              f"({100*flips/evaluated:.0f}%)  "
              f"near_ties(band>1)={sum(b > 1 for b in band_sizes)}  "
              f"needs_review={reviews}")


if __name__ == "__main__":
    main()
