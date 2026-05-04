"""
Inference wrapper for the GRPO-trained exploration strategy selector.

Loads Qwen3-4B + LoRA adapter once and predicts the best exploration
preset (0-5) given an exploitation digest.

Usage:
  # As a module:
  from training.infer import ExplorationStrategySelector
  selector = ExplorationStrategySelector()          # loads model once
  preset = selector.predict(digest_text)            # returns int 0-5

  # As CLI (useful for testing):
  uv run python infer.py --digest path/to/research_digest.md
  uv run python infer.py --digest path/to/research_digest.md --verbose
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import torch
import torch.nn.functional as F

# ---------------------------------------------------------------------------
# Paths (relative to this file)
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent          # RL_researcher_writer_ymaxing/
_LOCAL_MODEL_DIR = _REPO_ROOT / "models" / "Qwen3-4B"
# Fall back to HuggingFace Hub when the local weights are not present
# (e.g. after a fresh clone — the base model is too large for git).
_DEFAULT_MODEL_DIR: Path | str = _LOCAL_MODEL_DIR if _LOCAL_MODEL_DIR.exists() else "Qwen/Qwen3-4B"
_DEFAULT_ADAPTER_DIR = _REPO_ROOT / "rl_training_data" / "checkpoints" / "tasks" / "task_20260502_123123" / "best"

# ---------------------------------------------------------------------------
# System prompt — must match train_grpo.py exactly
# ---------------------------------------------------------------------------
_SYSTEM_PROMPT = """\
You are a research exploration strategy selector for an AI course article.

Given a digest excerpt describing current research coverage, source \
inventory, and gap analysis, select the optimal exploration preset (0-5).

Presets:
0: No exploration (baseline)
1: 1 round, balanced
2: 2 rounds, balanced then depth
3: 2 rounds, depth then breadth
4: 3 rounds, balanced then depth then breadth
5: 3 rounds, depth then breadth then depth

Respond with ONLY the preset number (0-5)."""

# Section-level system prompt — must match SECTION_SYSTEM_PROMPT in train_grpo.py exactly
_SECTION_SYSTEM_PROMPT = """\
You are a research exploration strategy selector for a section of an AI course article.

Given the section guideline (what the section must cover and how it should be written) \
and a digest excerpt describing current research coverage, source inventory, and gap \
analysis for that section, select the optimal exploration preset (0-5).

Presets:
0: No exploration (baseline)
1: 1 round, balanced
2: 2 rounds, balanced then depth
3: 2 rounds, depth then breadth
4: 3 rounds, balanced then depth then breadth
5: 3 rounds, depth then breadth then depth

Respond with ONLY the preset number (0-5)."""

_NUM_PRESETS = 6
# Minimum confidence (top − second probability) used in the confidence-gated
# soft vote.  Prevents total erasure of a section's signal when the model is
# nearly uniform over its top two choices, while still down-weighting genuine
# uncertainty relative to decisive sections.
_MIN_CONFIDENCE = 0.05
_PRESET_NAMES = {
    0: "baseline (no exploration)",
    1: "single_balanced (1 round, balanced)",
    2: "balanced_then_depth (2 rounds)",
    3: "depth_then_breadth (2 rounds)",
    4: "balanced_depth_breadth (3 rounds)",
    5: "depth_breadth_depth (3 rounds)",
}


# ---------------------------------------------------------------------------
# Digest section parser (mirrors train_grpo._extract_digest_sections)
# ---------------------------------------------------------------------------

def _extract_digest_sections(digest: str) -> list[tuple[str, str]]:
    """Extract (title, excerpt_text) pairs from the Per-Section Coverage Analysis.

    Each section starts with a heading matching ``### S<n> — <title>``.
    The excerpt runs until the next such heading (or the Overall Gap Profile
    subsection, whichever comes first).
    """
    pattern = r'^### S(\d+) — (.+)$'
    matches = list(re.finditer(pattern, digest, re.MULTILINE))
    sections: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        title = m.group(2).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(digest)
        excerpt = digest[start:end].strip()
        # Drop the Overall Gap Profile if it bleeds into the last block
        gap_idx = excerpt.find('\n## 3.')
        if gap_idx != -1:
            excerpt = excerpt[:gap_idx].strip()
        sections.append((title, excerpt))
    return sections


def _extract_guideline_preamble(guideline: str) -> str:
    """Return the text of ``article_guideline.md`` that precedes the first
    ``## Section N`` header — the global context block that carries the total
    word target, variant scope note, audience description, and course anchoring.

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
    identical function in ``train_grpo.py``.
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


def _extract_guideline_sections(
    guideline: str,
    digest_sections: list[tuple[str, str]],
) -> list[str]:
    """Slice article_guideline.md into per-section blocks aligned to digest sections.

    Mirrors train_grpo._extract_guideline_sections.  Uses positional alignment
    when counts match, falls back to title substring-matching otherwise.
    Returns a list of the same length as ``digest_sections``; empty string
    when no match is found for a section.
    """
    header_re = re.compile(r'^## Section \d+ ?[-:] ?(.+)$', re.MULTILINE)
    matches = list(header_re.finditer(guideline))
    if not matches:
        return [""] * len(digest_sections)

    guideline_blocks: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(guideline)
        guideline_blocks.append((title, guideline[start:end].strip()))

    n_g = len(guideline_blocks)
    n_d = len(digest_sections)
    result: list[str] = [""] * n_d

    if n_g == n_d:
        for i, (_, block) in enumerate(guideline_blocks):
            result[i] = block
        return result

    # Fuzzy fallback: three-pass substring matching
    for d_idx, (d_title, _) in enumerate(digest_sections):
        rn = d_title.lower().strip()
        # Pass 1: exact
        for g_title, block in guideline_blocks:
            if rn == g_title.lower().strip():
                result[d_idx] = block
                break
        else:
            # Pass 2: substring containment
            for g_title, block in guideline_blocks:
                g = g_title.lower().strip()
                if rn in g or g in rn:
                    result[d_idx] = block
                    break
            else:
                # Pass 3: strip "the " prefix and punctuation
                rn_norm = re.sub(r'^the\s+', '', rn).replace(',', '')
                for g_title, block in guideline_blocks:
                    g_norm = re.sub(r'^the\s+', '', g_title.lower().strip()).replace(',', '')
                    if rn_norm in g_norm or g_norm in rn_norm:
                        result[d_idx] = block
                        break
    return result


class ExplorationStrategySelector:
    """
    Wraps the trained Qwen3-4B + LoRA adapter for single-call inference.

    Model and tokenizer are loaded once at construction and reused across
    calls — suitable for use inside a long-running MCP server process.

    Args:
        model_dir: Path to the base Qwen3-4B model directory.
        adapter_dir: Path to the LoRA adapter directory (best/ checkpoint).
        device: CUDA device string, e.g. "cuda" or "cuda:0". Auto-detected
                if None.
    """

    def __init__(
        self,
        model_dir: str | Path = _DEFAULT_MODEL_DIR,
        adapter_dir: str | Path = _DEFAULT_ADAPTER_DIR,
        device: str | None = None,
    ) -> None:
        from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
        from peft import PeftModel

        model_dir = Path(model_dir)
        adapter_dir = Path(adapter_dir)

        if not model_dir.exists():
            raise FileNotFoundError(f"Model directory not found: {model_dir}")
        if not adapter_dir.exists():
            raise FileNotFoundError(
                f"LoRA adapter directory not found: {adapter_dir}\n"
                "Run training first: uv run python train_grpo.py"
            )

        self.device = torch.device(
            device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        )

        # --- Tokenizer ---
        self._tokenizer = AutoTokenizer.from_pretrained(
            str(model_dir), trust_remote_code=True
        )

        # Cache action token IDs for digits 0-5
        self._action_ids: list[int] = []
        for digit in range(_NUM_PRESETS):
            toks = self._tokenizer.encode(str(digit), add_special_tokens=False)
            if len(toks) != 1:
                raise RuntimeError(
                    f"Digit '{digit}' tokenized to {len(toks)} tokens. "
                    "Tokenizer mismatch — verify model is Qwen3."
                )
            self._action_ids.append(toks[0])

        self._action_ids_t = torch.tensor(self._action_ids, dtype=torch.long)

        # --- Base model (NF4 quantized) ---
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )
        base_model = AutoModelForCausalLM.from_pretrained(
            str(model_dir),
            quantization_config=bnb_config,
            device_map="cuda",
            dtype=torch.bfloat16,
            attn_implementation="sdpa",
        )
        base_model.config.use_cache = True  # enable KV cache for inference

        # --- LoRA adapter ---
        self._model = PeftModel.from_pretrained(base_model, str(adapter_dir))
        self._model.eval()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def predict(self, digest: str, guideline: str = "") -> int:
        """
        Predict the best exploration preset for the given digest.

        Uses section-level aggregation when the digest contains Per-Section
        headings (``### S<n> — <title>``), otherwise falls back to treating
        the full digest as a single context (article-level mode).

        Args:
            digest: Research digest text (content of research_digest.md).
            guideline: Optional article_guideline.md text.  When provided,
                each section call receives its matching guideline block,
                matching the training-time input distribution exactly.

        Returns:
            int: Chosen preset ID (0-5).
        """
        preset, _ = self.predict_article(digest, guideline=guideline)
        return preset

    def predict_with_probs(self, digest: str) -> tuple[int, list[float]]:
        """
        Predict preset and return action probabilities for all 6 presets.

        This is the low-level single-context call used internally by
        ``predict_article``.  Pass a section excerpt to get section-level
        probabilities, or the full digest for article-level probabilities.

        Args:
            digest: Exploitation digest text (or a section excerpt).

        Returns:
            tuple[int, list[float]]: (chosen_preset, probabilities over 0-5)
        """
        input_ids = self._build_input_ids(digest)

        with torch.no_grad():
            logits = self._model(input_ids.to(self.device)).logits[0, -1, :]
            probs = F.softmax(logits.float()[self._action_ids_t.to(self.device)], dim=-1)

        probs_list = probs.cpu().tolist()
        chosen = int(probs.argmax().item())
        return chosen, probs_list

    def predict_article(
        self,
        digest: str,
        guideline: str = "",
    ) -> tuple[int, list[float]]:
        """
        Predict the best article-level preset via per-section weighted vote.

        Algorithm:
          1. Split the digest into per-section excerpts.
          2. For each section, run ``_predict_section``; weight by word count.
          3. Normalise the summed probability vector → section aggregate.
          4. chosen = argmax of the aggregate.

        Falls back to the full-digest article-level prompt when the digest
        contains no Per-Section headings (e.g. legacy digest format).

        Args:
            digest: Full exploitation digest text.
            guideline: Optional article_guideline.md text.  When provided,
                each section call receives its matching guideline block,
                reproducing the training-time input distribution exactly.

        Returns:
            tuple[int, list[float]]:
                (chosen_preset, aggregated_probabilities_over_0_to_5)
        """
        preset, agg_normalised, _, _meta = self._aggregate(digest, guideline=guideline, verbose=False)
        return preset, agg_normalised

    def predict_article_verbose(
        self,
        digest: str,
        guideline: str = "",
    ) -> tuple[int, list[float], list[dict]]:
        """
        Like ``predict_article`` but also returns per-section detail.

        Returns:
            tuple[int, list[float], list[dict]]:
                (chosen_preset, aggregated_probs, section_details)

            Each element of ``section_details`` is a dict with keys:
                ``title``       — section heading string
                ``excerpt``     — section text fed to the model
                ``probs``       — probability vector (list[float] length 6)
                ``chosen``      — argmax preset for this section alone
                ``word_count``  — raw word count of the section excerpt
                ``margin``      — top_prob − second_prob (raw confidence signal)
                ``confidence``  — max(margin, _MIN_CONFIDENCE)
                ``weight``      — effective_weight = word_count × confidence

            The ``chosen_preset`` is the argmax of the section-weighted
            aggregate probability vector.  Callers can inspect
            ``section_details[i]["chosen"]`` to see individual section calls.
        """
        preset, probs, details, _meta = self._aggregate(digest, guideline=guideline, verbose=True)
        return preset, probs, details, _meta

    def _aggregate(
        self,
        digest: str,
        *,
        guideline: str = "",
        verbose: bool,
    ) -> tuple[int, list[float], list[dict], dict]:
        """
        Core aggregation logic shared by predict_article and
        predict_article_verbose.

        Section probabilities are weighted by word count, normalised, and
        the argmax of the aggregate is returned directly.

        When ``guideline`` is provided, each section call receives its
        matching guideline block (positional or fuzzy-matched), reproducing
        the training-time input format exactly.
        """
        sections = _extract_digest_sections(digest)

        if not sections:
            # Legacy digest without section headings — fall back to article-level
            preset, probs = self.predict_with_probs(digest)
            return preset, probs, [], {}

        # Per-section guideline blocks (empty strings when no guideline provided)
        guideline_blocks = (
            _extract_guideline_sections(guideline, sections)
            if guideline
            else [""] * len(sections)
        )

        # Compact article context (word target + theory/practice ratio + scope
        # constraint) extracted once and reused for every section.  The full
        # preamble is distilled to ~3 lines to avoid burying the section
        # guideline in thousands of preamble tokens (lost-in-the-middle risk).
        guideline_preamble = (
            _extract_compact_preamble(_extract_guideline_preamble(guideline))
            if guideline
            else ""
        )

        # --- Section-level confidence-gated soft vote ---
        # Each section's contribution is scaled by:
        #   effective_weight = word_count × confidence
        # where confidence = max(top_prob − second_prob, _MIN_CONFIDENCE).
        # This preserves the full soft probability distribution (no hard-vote
        # information loss) while down-weighting sections where the model is
        # nearly uniform over its top two choices.  Decisive sections (large
        # margin) dominate; near-tied sections contribute proportionally less.
        agg = [0.0] * _NUM_PRESETS
        details: list[dict] = []
        for (title, excerpt), g_block in zip(sections, guideline_blocks):
            sec_chosen, sec_probs = self._predict_section(
                excerpt, guideline_block=g_block, guideline_preamble=guideline_preamble
            )
            word_count = max(len(excerpt.split()), 1)
            sorted_probs = sorted(sec_probs, reverse=True)
            margin = sorted_probs[0] - sorted_probs[1]
            confidence = max(margin, _MIN_CONFIDENCE)
            effective_weight = word_count * confidence
            for i, p in enumerate(sec_probs):
                agg[i] += p * effective_weight
            if verbose:
                details.append({
                    "title": title,
                    "excerpt": excerpt,
                    "probs": sec_probs,
                    "chosen": sec_chosen,
                    "word_count": word_count,
                    "margin": margin,
                    "confidence": confidence,
                    "weight": effective_weight,
                })

        total = sum(agg)
        agg_normalised = [v / total for v in agg]
        chosen = int(agg_normalised.index(max(agg_normalised)))

        _meta: dict = {}
        return chosen, agg_normalised, details, _meta

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _predict_section(
        self,
        excerpt: str,
        guideline_block: str = "",
        guideline_preamble: str = "",
    ) -> tuple[int, list[float]]:
        """Run inference for one section with the section-level system prompt.

        When ``guideline_block`` is provided the user message is a composite
        of the guideline and the digest excerpt, exactly matching the
        training-time tokenization in ``train_grpo.tokenize_groups``.

        Input ordering (lost-in-the-middle mitigation):
          1. Section guideline  — task definition; front-loaded for strong attention
          2. Article context    — compact variant signal (~3 lines) in the middle
          3. Research coverage  — evidence; last, immediately before generation

        ``guideline_preamble`` must already be the *compact* form produced by
        ``_extract_compact_preamble`` (done once in ``_aggregate``).
        """
        if guideline_block:
            article_ctx = (
                f"## Article context\n{guideline_preamble}\n\n"
                if guideline_preamble
                else ""
            )
            user_content = (
                "## Section guideline\n"
                f"{guideline_block}\n\n"
                f"{article_ctx}"
                "## Current research coverage for this section\n"
                f"{excerpt}"
            )
        else:
            user_content = excerpt
        input_ids = self._build_input_ids(user_content, system_prompt=_SECTION_SYSTEM_PROMPT)
        with torch.no_grad():
            logits = self._model(input_ids.to(self.device)).logits[0, -1, :]
            probs = F.softmax(logits.float()[self._action_ids_t.to(self.device)], dim=-1)
        probs_list = probs.cpu().tolist()
        chosen = int(probs.argmax().item())
        return chosen, probs_list

    def _build_input_ids(
        self, digest: str, *, system_prompt: str = _SYSTEM_PROMPT
    ) -> torch.Tensor:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": digest},
        ]
        prompt_str = self._tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=False,
            enable_thinking=False,
        )
        token_ids = self._tokenizer.encode(prompt_str, add_special_tokens=False)
        return torch.tensor([token_ids], dtype=torch.long)


# ---------------------------------------------------------------------------
# Shared output helper
# ---------------------------------------------------------------------------

def _print_result(
    preset: int,
    probs: list[float],
    section_details: list[dict],
    *,
    verbose: bool = True,
) -> None:
    print(f"\nChosen preset: {preset} — {_PRESET_NAMES[preset]}")
    if verbose:
        if section_details:
            print(f"\nPer-section breakdown ({len(section_details)} sections):")
            for d in section_details:
                bar = "  ".join(
                    f"P{i}={d['probs'][i]:.3f}{'*' if i == d['chosen'] else ' '}"
                    for i in range(_NUM_PRESETS)
                )
                word_c = d.get('word_count', int(d.get('weight', 0)))
                conf_s = f"  m={d['margin']:.2f}" if 'margin' in d else ''
                print(f"  [{word_c:4d}w{conf_s}]  {d['title']}")
                print(f"              {bar}")
        print("\nAggregated preset probabilities:")
        for i, name in _PRESET_NAMES.items():
            suffix = "  <-- chosen" if i == preset else ""
            print(f"  P{i} ({name}): {probs[i]:.4f}{suffix}")


# ---------------------------------------------------------------------------
# Batch mode  (--batch)
# ---------------------------------------------------------------------------

def _run_batch(
    selector: ExplorationStrategySelector,
    batch_file: str,
    verbose: bool,
    output_json: str | None,
) -> None:
    """Run inference over a batch of digest/guideline pairs without reloading
    the model.

    ``batch_file`` is either:

    * A **JSON file** — an array of objects, each with:
        ``"digest"``    (required) path to research_digest.md
        ``"guideline"`` (optional) path to article_guideline.md
        ``"label"``     (optional) human-readable name printed in output

    * A **plain-text file** — alternating lines:
        Line 1: path to digest
        Line 2: path to guideline (or empty line to skip)
        (repeat for each article)

    If ``output_json`` is given, results are also written as a JSON array.
    """
    import json as _json

    path = Path(batch_file)
    if not path.exists():
        sys.exit(f"ERROR: batch file not found: {path}")

    raw = path.read_text(encoding="utf-8").strip()

    # Parse batch entries
    entries: list[dict] = []
    if raw.startswith("[") or raw.startswith("{"):
        data = _json.loads(raw)
        if isinstance(data, dict):
            data = [data]
        for item in data:
            entries.append({
                "digest": item.get("digest", ""),
                "guideline": item.get("guideline", ""),
                "label": item.get("label", item.get("digest", "")),
            })
    else:
        lines = [ln.rstrip() for ln in raw.splitlines()]
        i = 0
        while i < len(lines):
            digest_line = lines[i].strip()
            i += 1
            guideline_line = lines[i].strip() if i < len(lines) else ""
            if guideline_line and not Path(guideline_line).exists():
                # treat as another digest line — no guideline was given
                guideline_line = ""
                i -= 1  # rewind
            else:
                i += 1
            if digest_line:
                entries.append({
                    "digest": digest_line,
                    "guideline": guideline_line,
                    "label": digest_line,
                })

    if not entries:
        sys.exit("ERROR: batch file contains no entries.")

    print(f"Batch mode — {len(entries)} article(s), model already loaded.\n")
    results = []

    for idx, entry in enumerate(entries, 1):
        d_path = Path(entry["digest"])
        g_path = Path(entry["guideline"]) if entry["guideline"] else None
        label = entry["label"]

        print(f"[{idx}/{len(entries)}] {label}")

        if not d_path.exists():
            print(f"  ERROR: digest not found: {d_path}\n")
            results.append({"label": label, "error": f"digest not found: {d_path}"})
            continue

        digest = d_path.read_text(encoding="utf-8")
        guideline = ""
        if g_path:
            if g_path.exists():
                guideline = g_path.read_text(encoding="utf-8")
            else:
                print(f"  WARNING: guideline not found: {g_path}, running without it")

        preset, probs, section_details, _meta = selector.predict_article_verbose(
            digest, guideline=guideline
        )
        _print_result(preset, probs, section_details, verbose=verbose)
        print()
        print()

        rec: dict = {
            "label": label,
            "digest": str(d_path),
            "guideline": str(g_path) if g_path else "",
            "preset": preset,
            "preset_name": _PRESET_NAMES[preset],
            "probs": probs,
        }
        if verbose:
            rec["sections"] = [
                {
                    "title": s["title"],
                    "chosen": s["chosen"],
                    "probs": s["probs"],
                    "word_count": s.get("word_count", 0),
                    "margin": s.get("margin", 0.0),
                    "confidence": s.get("confidence", 0.0),
                    "weight": s["weight"],
                }
                for s in section_details
            ]
        results.append(rec)

    print(f"Done. {sum(1 for r in results if 'error' not in r)}/{len(results)} succeeded.")

    if output_json:
        out = Path(output_json)
        out.write_text(_json.dumps(results, indent=2), encoding="utf-8")
        print(f"Results written to {out}")


# ---------------------------------------------------------------------------
# Interactive REPL mode  (--interactive)
# ---------------------------------------------------------------------------

def _run_interactive(selector: ExplorationStrategySelector) -> None:
    print("Interactive mode — model loaded. Enter digest paths one at a time.")
    print("Type 'quit' or press Ctrl+C to exit.\n")
    while True:
        try:
            raw = input("Digest path: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        if raw.lower() in ("quit", "exit", "q", ""):
            if raw.lower() in ("quit", "exit", "q"):
                break
            continue
        digest_path = Path(raw)
        if not digest_path.exists():
            print(f"  ERROR: file not found: {digest_path}")
            continue
        digest = digest_path.read_text(encoding="utf-8")

        # Optionally accept a guideline path to match training-time input
        try:
            g_raw = input("Guideline path (Enter to skip): ").strip()
        except (EOFError, KeyboardInterrupt):
            g_raw = ""
        guideline = ""
        if g_raw and Path(g_raw).exists():
            guideline = Path(g_raw).read_text(encoding="utf-8")
        elif g_raw:
            print(f"  WARNING: guideline not found: {g_raw}, running without it")

        preset, probs, sections, meta = selector.predict_article_verbose(digest, guideline=guideline)
        _print_result(preset, probs, sections, verbose=True)
        print()
        print()


# ---------------------------------------------------------------------------
# HTTP server mode  (--serve)
# ---------------------------------------------------------------------------

def _run_serve(selector: ExplorationStrategySelector, port: int) -> None:
    import json
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class _Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args) -> None:  # silence default access log
            pass

        def _send_json(self, data: dict, status: int = 200) -> None:
            body = json.dumps(data).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _read_json(self) -> dict:
            length = int(self.headers.get("Content-Length", 0))
            return json.loads(self.rfile.read(length)) if length else {}

        def do_GET(self):  # noqa: N802
            if self.path == "/health":
                self._send_json({"status": "ok"})
            else:
                self._send_json({"error": "Not found"}, 404)

        def do_POST(self):  # noqa: N802
            body = self._read_json()
            verbose = bool(body.get("verbose", True))

            if self.path not in ("/predict", "/predict-file"):
                self._send_json({"error": "Not found"}, 404)
                return

            try:
                if self.path == "/predict-file":
                    fpath = Path(body.get("path", ""))
                    if not fpath.exists():
                        self._send_json({"error": f"File not found: {fpath}"}, 400)
                        return
                    digest = fpath.read_text(encoding="utf-8")
                    g_path = body.get("guideline_path", "")
                    guideline = Path(g_path).read_text(encoding="utf-8") if g_path and Path(g_path).exists() else ""
                else:
                    digest = body.get("digest", "")
                    if not digest:
                        self._send_json({"error": "Missing 'digest' field"}, 400)
                        return
                    guideline = body.get("guideline", "")

                if verbose:
                    preset, probs, sections, _meta = selector.predict_article_verbose(digest, guideline=guideline)
                    result = {
                        "preset": preset,
                        "preset_name": _PRESET_NAMES[preset],
                        "probs": probs,
                        "sections": sections,
                    }
                else:
                    preset, probs = selector.predict_article(digest, guideline=guideline)
                    result = {
                        "preset": preset,
                        "preset_name": _PRESET_NAMES[preset],
                        "probs": probs,
                    }
                self._send_json(result)
            except Exception as exc:  # noqa: BLE001
                self._send_json({"error": str(exc)}, 500)

    server = HTTPServer(("127.0.0.1", port), _Handler)
    print(f"Inference server ready on http://127.0.0.1:{port}")
    print("  POST /predict       {\"digest\": \"<text>\", \"verbose\": true}")
    print("  POST /predict-file  {\"path\": \"path/to/digest.md\", \"verbose\": true}")
    print("  GET  /health")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Predict optimal exploration preset from an exploitation digest.",
    )
    parser.add_argument(
        "--digest",
        help="Path to research_digest.md (or '-' for stdin). Required unless --serve or --interactive.",
    )
    parser.add_argument(
        "--guideline",
        default=None,
        help="Path to article_guideline.md.  When provided, section calls use the "
             "guideline+digest composite input that matches training exactly.",
    )
    parser.add_argument(
        "--model-dir", default=str(_DEFAULT_MODEL_DIR),
        help=f"Path to base Qwen3-4B model (default: {_DEFAULT_MODEL_DIR})",
    )
    parser.add_argument(
        "--adapter-dir", default=str(_DEFAULT_ADAPTER_DIR),
        help=f"Path to LoRA adapter checkpoint (default: {_DEFAULT_ADAPTER_DIR})",
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Show per-section breakdown and all preset probabilities.",
    )
    parser.add_argument(
        "--batch",
        default=None,
        metavar="BATCH_FILE",
        help=(
            "Path to a batch file (JSON array or plain-text pairs) listing "
            "digest/guideline paths. Model is loaded once for the whole batch. "
            "See _run_batch docstring for format details."
        ),
    )
    parser.add_argument(
        "--batch-output",
        default=None,
        metavar="OUTPUT_JSON",
        help="Write batch results to this JSON file (only used with --batch).",
    )
    parser.add_argument(
        "--interactive", action="store_true",
        help="Load model once, then accept digest paths interactively.",
    )
    parser.add_argument(
        "--serve", action="store_true",
        help="Start an HTTP inference server (model loaded once, accepts POST requests).",
    )
    parser.add_argument(
        "--port", type=int, default=8787,
        help="Port for --serve mode (default: 8787).",
    )
    args = parser.parse_args()

    if not args.serve and not args.interactive and not args.batch and not args.digest:
        parser.error("--digest is required unless --serve, --interactive, or --batch is used.")

    print("Loading model (this takes ~90s on first run)...")
    selector = ExplorationStrategySelector(
        model_dir=args.model_dir,
        adapter_dir=args.adapter_dir,
    )

    if args.serve:
        _run_serve(selector, args.port)
    elif args.interactive:
        _run_interactive(selector)
    elif args.batch:
        _run_batch(selector, args.batch, verbose=args.verbose, output_json=args.batch_output)
    else:
        if args.digest == "-":
            digest = sys.stdin.read()
        else:
            digest_path = Path(args.digest)
            if not digest_path.exists():
                sys.exit(f"ERROR: digest file not found: {digest_path}")
            digest = digest_path.read_text(encoding="utf-8")

        guideline = ""
        if args.guideline:
            g_path = Path(args.guideline)
            if not g_path.exists():
                sys.exit(f"ERROR: guideline file not found: {g_path}")
            guideline = g_path.read_text(encoding="utf-8")

        if args.verbose:
            preset, probs, section_details, meta = selector.predict_article_verbose(digest, guideline=guideline)
        else:
            preset, probs = selector.predict_article(digest, guideline=guideline)
            section_details, meta = [], {}

        _print_result(preset, probs, section_details, verbose=args.verbose)


if __name__ == "__main__":
    main()
