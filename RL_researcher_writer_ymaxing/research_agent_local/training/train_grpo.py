"""
Offline GRPO + QLoRA Training for Exploration Strategy Selection

Trains Qwen3-4B to select optimal exploration presets (0-5) given
exploitation digests as context. Uses offline GRPO with precomputed rewards.

Usage (from research_agent_local/training/):
  uv run python train_grpo.py --dry-run       # verify setup
  uv run python train_grpo.py                  # full training
  uv run python train_grpo.py --epochs 200 --lr 5e-5 --beta 0.1
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

import torch
import torch.nn.functional as F
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from torch.utils.tensorboard import SummaryWriter
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

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
    "03_context_engineering",
    "05_workflow_patterns",
    "08_react_practice",
    "11_multimodal",
]

# Hold-out test articles (not used in training):
# "02_workflows_vs_agents", "06_tools", "09_RAG"

PRESET_ROUNDS = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}
NUM_PRESETS = 6

SYSTEM_PROMPT = """\
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

SECTION_SYSTEM_PROMPT = """\
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
    input_ids: torch.Tensor | None = None
    rewards: list[float] = field(default_factory=list)
    advantages: torch.Tensor | None = None
    ref_log_probs: torch.Tensor | None = None
    best_preset_idx: int = 0
    hit_sigma_floor: bool = False


# ---------------------------------------------------------------------------
# Reward computation
# ---------------------------------------------------------------------------
def compute_reward(scores: dict, preset_id: int) -> float:
    """Compute reward from scores.json using the finalized formula."""
    cc = scores["ground_truth_core_content"]
    fl = scores["ground_truth_flow"]
    de = scores["ground_truth_depth_enhancement"]
    be = scores["ground_truth_breadth_enhancement"]
    cp = scores["ground_truth_core_preservation"]
    ga = scores["user_intent_guideline_adherence"]
    ra = scores["user_intent_research_anchoring"]
    nr = PRESET_ROUNDS[preset_id]

    gt_base = 0.20 * cc + 0.20 * fl
    explore = cp * (0.60 * de + 0.40 * be) * 0.30
    user_intent = (0.50 * ga + 0.50 * ra) * 0.30
    cost = -0.02 * nr
    return gt_base + explore + user_intent + cost


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


# ---------------------------------------------------------------------------
# Data loading — article level
# ---------------------------------------------------------------------------
def load_groups(sigma_floor: float) -> list[Group]:
    """Load all training data and compute advantages."""
    groups: list[Group] = []

    for article in ARTICLES:
        digest_path = _BASES_DIR / article / "exploitation_digest.md"
        digest = digest_path.read_text(encoding="utf-8")
        group = Group(name=article, digest=digest)

        for p in range(NUM_PRESETS):
            ep_dir = _EPISODES_DIR / f"{article}__preset{p}"
            scores = json.loads((ep_dir / "scores.json").read_text(encoding="utf-8"))
            reward = compute_reward(scores, p)
            group.rewards.append(reward)

        # Within-group advantage normalization
        mean_r = sum(group.rewards) / len(group.rewards)
        raw_std = (sum((r - mean_r) ** 2 for r in group.rewards) / len(group.rewards)) ** 0.5
        group.hit_sigma_floor = raw_std < sigma_floor
        std_r = max(raw_std, sigma_floor)
        advantages = [(r - mean_r) / std_r for r in group.rewards]
        group.advantages = torch.tensor(advantages, dtype=torch.float32)
        group.best_preset_idx = group.rewards.index(max(group.rewards))

        groups.append(group)
        log.info(
            f"  {article}: R={[f'{r:.3f}' for r in group.rewards]} "
            f"best=P{group.best_preset_idx} ({max(group.rewards):.4f})"
        )

    return groups


# ---------------------------------------------------------------------------
# Data loading — section level
# ---------------------------------------------------------------------------
def load_section_groups(sigma_floor: float) -> list[Group]:
    """Load section-level GRPO groups from digest section excerpts.

    Each article section becomes its own GRPO group with 6 preset arms.
    Rewards are computed from per-section binary scores in reasoning.json.
    """
    groups: list[Group] = []

    for article in ARTICLES:
        digest_path = _BASES_DIR / article / "exploitation_digest.md"
        digest = digest_path.read_text(encoding="utf-8")
        digest_sections = _extract_digest_sections(digest)

        if not digest_sections:
            log.warning(f"  {article}: no digest sections found, skipping")
            continue

        for sec_idx, (sec_title, sec_excerpt) in enumerate(digest_sections):
            group = Group(
                name=f"{article}__S{sec_idx + 1}",
                digest=sec_excerpt,
            )

            for p in range(NUM_PRESETS):
                ep_dir = _EPISODES_DIR / f"{article}__preset{p}"
                reasons = json.loads(
                    (ep_dir / "reasoning.json").read_text(encoding="utf-8")
                )

                # Build per-section scores dict for the reward formula
                section_scores: dict[str, float] = {}
                for dim in _REWARD_DIMS:
                    if dim not in reasons:
                        section_scores[dim] = 0.0
                        continue
                    dim_sections = _parse_reasoning_sections(reasons[dim])
                    matched_score: int | None = None
                    for rname, rscore in dim_sections.items():
                        match_idx = _match_reasoning_to_digest(
                            rname, digest_sections
                        )
                        if match_idx == sec_idx:
                            matched_score = rscore
                            break
                    section_scores[dim] = float(
                        matched_score if matched_score is not None else 0
                    )

                reward = compute_reward(section_scores, p)
                group.rewards.append(reward)

            # Within-group advantage normalization
            mean_r = sum(group.rewards) / len(group.rewards)
            raw_std = (
                sum((r - mean_r) ** 2 for r in group.rewards) / len(group.rewards)
            ) ** 0.5
            group.hit_sigma_floor = raw_std < sigma_floor
            std_r = max(raw_std, sigma_floor)
            advantages = [(r - mean_r) / std_r for r in group.rewards]
            group.advantages = torch.tensor(advantages, dtype=torch.float32)
            group.best_preset_idx = group.rewards.index(max(group.rewards))

            groups.append(group)
            log.info(
                f"  {group.name} ({sec_title[:40]}): "
                f"R={[f'{r:.3f}' for r in group.rewards]} "
                f"best=P{group.best_preset_idx} ({max(group.rewards):.4f})"
                + (" [flat]" if group.hit_sigma_floor else "")
            )

    n_flat = sum(1 for g in groups if g.hit_sigma_floor)
    log.info(
        f"  Total section-level groups: {len(groups)} "
        f"({n_flat} flat / hit sigma_floor = {n_flat/len(groups):.0%})"
    )
    return groups


# ---------------------------------------------------------------------------
# Tokenization
# ---------------------------------------------------------------------------
def tokenize_groups(
    groups: list[Group], tokenizer, *, system_prompt: str = SYSTEM_PROMPT
) -> None:
    """Tokenize prompts for all groups using the chat template."""
    for group in groups:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": group.digest},
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
    """Find token IDs for single-digit strings '0' through '5'."""
    action_ids = []
    for digit in range(NUM_PRESETS):
        toks = tokenizer.encode(str(digit), add_special_tokens=False)
        if len(toks) != 1:
            sys.exit(f"ERROR: Digit '{digit}' tokenized to {len(toks)} tokens: {toks}")
        action_ids.append(toks[0])
        decoded = tokenizer.decode([toks[0]])
        log.info(f"  '{digit}' -> token_id={toks[0]} -> decoded='{decoded}'")

    return torch.tensor(action_ids, dtype=torch.long)


# ---------------------------------------------------------------------------
# Reference log-probs
# ---------------------------------------------------------------------------
def compute_ref_log_probs(
    model, groups: list[Group], action_token_ids: torch.Tensor, device: torch.device
) -> None:
    """Forward pass through the base model to cache reference log-probs."""
    log.info("Computing reference log-probs (base model, no LoRA)...")
    model.eval()
    action_ids = action_token_ids.to(device)

    with torch.no_grad():
        for group in groups:
            logits = model(group.input_ids.to(device)).logits[0, -1, :]
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

    # Optimizer
    trainable_params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(
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

            for group in groups:
                input_ids = group.input_ids.to(device)
                logits = model(input_ids).logits[0, -1, :]

                # Re-normalize over the 6 action logits only (consistent
                # across policy gradient, KL, and eval metrics).
                action_logits = logits.float()[action_ids]
                pi_lp_6 = F.log_softmax(action_logits, dim=-1)
                ref_lp_6 = F.log_softmax(group.ref_log_probs, dim=-1)

                # GRPO policy gradient loss
                loss_grpo = -(group.advantages * pi_lp_6).mean()

                # KL(π || π_ref) over the 6-action simplex (always ≥ 0).
                loss_kl = (pi_lp_6.exp() * (pi_lp_6 - ref_lp_6)).sum()

                # Entropy bonus H(π) — directly prevents collapse (always ≥ 0).
                loss_entropy = -(pi_lp_6.exp() * pi_lp_6).sum()

                # Combined, averaged across groups
                loss = (loss_grpo + args.beta * loss_kl - args.entropy_coef * loss_entropy) / num_groups
                loss.backward()

                epoch_loss_grpo += loss_grpo.item() / num_groups
                epoch_loss_kl += loss_kl.item() / num_groups
                epoch_loss_entropy += loss_entropy.item() / num_groups
                epoch_loss_total += loss.item()

                # --- per-group evaluation metrics (no grad) ---
                with torch.no_grad():
                    # Re-normalize over the 6 action logits for eval
                    probs_6 = F.softmax(logits.float()[action_ids], dim=-1)
                    rewards_t = torch.tensor(
                        group.rewards, device=device, dtype=torch.float32
                    )
                    entropy = -(probs_6 * probs_6.log()).sum().item()
                    expected_reward = (probs_6 * rewards_t).sum().item()
                    top1 = probs_6.argmax().item()

                    epoch_metrics[group.name] = {
                        "entropy": round(entropy, 4),
                        "expected_reward": round(expected_reward, 4),
                        "top1_preset": top1,
                        "top1_correct": top1 == group.best_preset_idx,
                        "action_probs": [round(p, 4) for p in probs_6.cpu().tolist()],
                        "kl": round(loss_kl.item(), 6),
                    }

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
                log.info(
                    f"Epoch {epoch:>4d}/{args.epochs} | "
                    f"loss={epoch_loss_total:.4f} "
                    f"(grpo={epoch_loss_grpo:.4f} kl={epoch_loss_kl:.4f} ent={epoch_loss_entropy:.4f}) | "
                    f"E[R]={mean_er:.4f} | top1={top1_acc:.0%} | "
                    f"H={mean_entropy:.3f} | "
                    f"‖g‖={grad_norm:.4f} | lr={current_lr:.2e} | "
                    f"{elapsed:.0f}s"
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

            if (epoch + 1) % 50 == 0:
                ckpt_dir = task_dir / f"epoch_{epoch + 1:04d}"
                ckpt_dir.mkdir(parents=True, exist_ok=True)
                model.save_pretrained(str(ckpt_dir))
                log.info(f"  Checkpoint → {ckpt_dir}")

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

    # Final save
    final_dir = task_dir / "final"
    final_dir.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(str(final_dir))
    log.info(f"Final model saved to {final_dir}")

    writer.close()
    elapsed_total = time.time() - t_start
    log.info(
        f"Training complete in {elapsed_total:.0f}s. "
        f"Best E[R]={best_expected_reward:.4f} "
        f"(uniform={uniform_er:.4f}, oracle={oracle_er:.4f})"
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
    parser.add_argument("--entropy-coef", type=float, default=0.05, help="Entropy bonus coefficient")
    parser.add_argument(
        "--sigma-floor", type=float, default=0.04,
        help="Minimum std for advantage normalization",
    )
    parser.add_argument("--warmup-epochs", type=int, default=10)
    parser.add_argument("--max-grad-norm", type=float, default=1.0)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--patience", type=int, default=30, help="Early stopping patience")
    parser.add_argument("--lora-r", type=int, default=8)
    parser.add_argument("--lora-alpha", type=int, default=8)
    parser.add_argument("--lora-dropout", type=float, default=0.05)
    parser.add_argument(
        "--granularity",
        choices=["article", "section"],
        default="article",
        help="Training granularity: article-level (5 groups) or "
        "section-level (~35 groups)",
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
        groups = load_section_groups(args.sigma_floor)
        active_system_prompt = SECTION_SYSTEM_PROMPT
    else:
        groups = load_groups(args.sigma_floor)
        active_system_prompt = SYSTEM_PROMPT

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
    tokenize_groups(groups, tokenizer, system_prompt=active_system_prompt)

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
            logits = model(g.input_ids.to(device)).logits[0, -1, :]
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
