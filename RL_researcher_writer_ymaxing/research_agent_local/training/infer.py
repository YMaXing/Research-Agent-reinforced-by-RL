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
  uv run python infer.py --digest path/to/exploitation_digest.md
  uv run python infer.py --digest path/to/exploitation_digest.md --verbose
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
_DEFAULT_ADAPTER_DIR = _REPO_ROOT / "rl_training_data" / "checkpoints" / "tasks" / "task_20260420_223150" / "best"

# ---------------------------------------------------------------------------
# System prompt — must match train_grpo.py exactly
# ---------------------------------------------------------------------------
_SYSTEM_PROMPT = """\
You are a research exploration strategy selector for an AI course article.

Given an exploitation digest describing current research coverage, source \
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

Given an exploitation digest excerpt describing current research coverage, \
source inventory, and gap analysis for a specific article section, select \
the optimal exploration preset (0-5).

Presets:
0: No exploration (baseline)
1: 1 round, balanced
2: 2 rounds, balanced then depth
3: 2 rounds, depth then breadth
4: 3 rounds, balanced then depth then breadth
5: 3 rounds, depth then breadth then depth

Respond with ONLY the preset number (0-5)."""

_NUM_PRESETS = 6
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

    def predict(self, digest: str) -> int:
        """
        Predict the best exploration preset for the given digest.

        Uses section-level aggregation when the digest contains Per-Section
        headings (``### S<n> — <title>``), otherwise falls back to treating
        the full digest as a single context (article-level mode).

        Args:
            digest: Exploitation digest text (content of exploitation_digest.md).

        Returns:
            int: Chosen preset ID (0-5).
        """
        preset, _ = self.predict_article(digest)
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
    ) -> tuple[int, list[float]]:
        """
        Predict the best article-level preset via per-section weighted vote
        with two safety corrections:

          #1  Max-preset floor — the article preset can never be lower than
              the most demanding section's individual prediction.  This
              prevents intro-section dominance from burying strong signals
              from technical sections.

        Algorithm:
          1. Split the digest into per-section excerpts.
          2. For each section, run ``_predict_section``; weight by word count.
          3. Normalise the summed probability vector → section aggregate.
          4. chosen = max(section_argmax, section_max_floor)

        Falls back to the full-digest article-level prompt when the digest
        contains no Per-Section headings (e.g. legacy digest format).

        Args:
            digest: Full exploitation digest text.

        Returns:
            tuple[int, list[float]]:
                (chosen_preset, aggregated_probabilities_over_0_to_5)
        """
        preset, agg_normalised, _, _meta = self._aggregate(digest, verbose=False)
        return preset, agg_normalised

    def predict_article_verbose(
        self,
        digest: str,
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
                ``weight``      — word-count weight applied

            The ``chosen_preset`` already incorporates the max-preset floor
            (#1) and article-level cross-check (#4).  Callers can inspect
            ``section_details[i]["chosen"]`` to see individual section calls.
        """
        preset, probs, details, _meta = self._aggregate(digest, verbose=True)
        return preset, probs, details, _meta

    def _aggregate(
        self,
        digest: str,
        *,
        verbose: bool,
    ) -> tuple[int, list[float], list[dict]]:
        """
        Core aggregation logic shared by predict_article and
        predict_article_verbose.

        Applies one correction after the section-weighted vote:
          #1  max-preset floor from the most demanding section prediction,
              but only when the aggregate vote is P0–P2.  When the vote
              is already ≥ P3 the floor is skipped to avoid outlier sections
              causing systematic over-exploration.
        """
        sections = _extract_digest_sections(digest)

        if not sections:
            # Legacy digest without section headings — fall back to article-level
            preset, probs = self.predict_with_probs(digest)
            return preset, probs, [], {}

        # --- Section-level weighted vote ---
        agg = [0.0] * _NUM_PRESETS
        details: list[dict] = []
        section_max_floor = 0  # #1: highest individual section preset
        for title, excerpt in sections:
            sec_chosen, sec_probs = self._predict_section(excerpt)
            weight = max(len(excerpt.split()), 1)
            for i, p in enumerate(sec_probs):
                agg[i] += p * weight
            section_max_floor = max(section_max_floor, sec_chosen)
            if verbose:
                details.append({
                    "title": title,
                    "excerpt": excerpt,
                    "probs": sec_probs,
                    "chosen": sec_chosen,
                    "weight": weight,
                })

        total = sum(agg)
        agg_normalised = [v / total for v in agg]
        section_chosen = int(agg_normalised.index(max(agg_normalised)))

        # --- Final decision: #1 max-preset floor ---
        # Only apply the floor when the aggregate vote is in the
        # under-exploration zone (P0–P2).  When the vote is already ≥ P3
        # the model has committed to 2+ rounds; letting one outlier section
        # drag it higher causes systematic over-shooting.
        if section_chosen <= 2:
            chosen = max(section_chosen, section_max_floor)
        else:
            chosen = section_chosen

        _meta = {
            "section_vote": section_chosen,
            "section_floor": section_max_floor,
        }
        return chosen, agg_normalised, details, _meta

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _predict_section(self, excerpt: str) -> tuple[int, list[float]]:
        """Run predict_with_probs with the section-level system prompt."""
        input_ids = self._build_input_ids(excerpt, system_prompt=_SECTION_SYSTEM_PROMPT)
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
    section_vote: int | None = None,
    section_floor: int | None = None,
) -> None:
    # Build correction annotation if any correction fired
    corrections: list[str] = []
    if section_vote is not None and section_floor is not None:
        # Floor only fires when vote was ≤ P2 (under-exploration guard)
        floor_applied = section_vote <= 2 and section_floor > section_vote
        if floor_applied:
            corrections.append(f"#1 floor: P{section_vote}→P{section_floor} (section max)")
    correction_str = "  [" + ", ".join(corrections) + "]" if corrections else ""
    print(f"\nChosen preset: {preset} — {_PRESET_NAMES[preset]}{correction_str}")
    if verbose:
        if section_details:
            print(f"\nPer-section breakdown ({len(section_details)} sections):")
            for d in section_details:
                bar = "  ".join(
                    f"P{i}={d['probs'][i]:.3f}{'*' if i == d['chosen'] else ' '}"
                    for i in range(_NUM_PRESETS)
                )
                print(f"  [{d['weight']:4d} words]  {d['title']}")
                print(f"              {bar}")
        print("\nAggregated preset probabilities (section vote):")
        for i, name in _PRESET_NAMES.items():
            markers = []
            if section_vote is not None and i == section_vote:
                markers.append("vote")
            if section_floor is not None and i == section_floor and section_floor > (section_vote or 0):
                markers.append("floor")
            if i == preset:
                markers.append("chosen")
            suffix = "  <-- " + ", ".join(markers) if markers else ""
            print(f"  P{i} ({name}): {probs[i]:.4f}{suffix}")


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
        preset, probs, sections, meta = selector.predict_article_verbose(digest)
        _print_result(preset, probs, sections, verbose=True, **meta)


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
                else:
                    digest = body.get("digest", "")
                    if not digest:
                        self._send_json({"error": "Missing 'digest' field"}, 400)
                        return

                if verbose:
                    preset, probs, sections, meta = selector.predict_article_verbose(digest)
                    result = {
                        "preset": preset,
                        "preset_name": _PRESET_NAMES[preset],
                        "probs": probs,
                        "sections": sections,
                        "corrections": meta,
                    }
                else:
                    preset, probs = selector.predict_article(digest)
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
        help="Path to exploitation_digest.md (or '-' for stdin). Required unless --serve or --interactive.",
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

    if not args.serve and not args.interactive and not args.digest:
        parser.error("--digest is required unless --serve or --interactive is used.")

    print("Loading model (this takes ~90s on first run)...")
    selector = ExplorationStrategySelector(
        model_dir=args.model_dir,
        adapter_dir=args.adapter_dir,
    )

    if args.serve:
        _run_serve(selector, args.port)
    elif args.interactive:
        _run_interactive(selector)
    else:
        if args.digest == "-":
            digest = sys.stdin.read()
        else:
            digest_path = Path(args.digest)
            if not digest_path.exists():
                sys.exit(f"ERROR: digest file not found: {digest_path}")
            digest = digest_path.read_text(encoding="utf-8")

        if args.verbose:
            preset, probs, section_details, meta = selector.predict_article_verbose(digest)
        else:
            preset, probs = selector.predict_article(digest)
            section_details, meta = [], {}

        _print_result(preset, probs, section_details, verbose=args.verbose, **meta)


if __name__ == "__main__":
    main()
