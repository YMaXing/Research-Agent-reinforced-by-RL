"""
Batch runner for the research agent.

Processes multiple sample directories in sequence while keeping the MCP server
alive for the entire batch.  Each sample gets a **fresh** conversation history
so that LLM context from one sample never bleeds into another.

After the initial batch (if any) the runner enters an interactive REPL where
new batches can be submitted without restarting the agent or re-importing heavy
packages.  Use --non-interactive to disable the REPL (useful for CI / scripts).

Usage:
    # Start interactively with no initial batch — specify batches at the prompt
    uv run python -m mcp_client.src.batch_runner

    # Process an initial batch, then stay alive for more batches
    uv run python -m mcp_client.src.batch_runner --samples-dir data/batch

    # Explicit sample list
    uv run python -m mcp_client.src.batch_runner \
        --sample data/sample_1 --sample data/sample_2

    # Two-variant mode (exploitation-only + full) for initial batch
    uv run python -m mcp_client.src.batch_runner --samples-dir data/batch --two-variants

    # Non-interactive: process initial batch and exit (CI/script usage)
    uv run python -m mcp_client.src.batch_runner --samples-dir data/batch --non-interactive

    # Dry-run: just list what would be processed
    uv run python -m mcp_client.src.batch_runner --samples-dir data/batch --dry-run

Interactive prompt commands (once the agent is running):
    /path/to/parent_dir              → auto-discover all samples inside it
    /path/to/sample_A /path/to/B     → space-separated explicit sample dirs
    --two-variants /path/to/dir      → enable two-variant mode for this batch
    --no-two-variants /path/to/dir   → disable two-variant mode for this batch
    --no-thinking /path/to/dir       → disable LLM thinking for this batch
    --thinking /path/to/dir          → re-enable LLM thinking for this batch
    /quit                            → shut down the agent and exit
"""

import argparse
import asyncio
import logging
import shlex
import sys
import time
from pathlib import Path
from typing import List, Tuple

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.config import get_settings as get_mcp_settings

from .settings import settings
from .utils.command_utils import handle_command, handle_prompt_command, handle_resource_command
from .utils.handle_agent_loop_utils import handle_agent_loop, make_user_message
from .utils.logging_utils import configure_logging
from .utils.mcp_startup_utils import get_capabilities_from_mcp_client, print_startup_info
from .utils.opik_handler import configure_opik
from .utils.parse_message_utils import parse_user_input
from .utils.types import InputType

configure_logging()

# --------------------------------------------------------------------------- #
# MCP app (created once, reused across all samples)
# --------------------------------------------------------------------------- #
_mcp_settings = get_mcp_settings(str(Path(__file__).parent / "mcp_agent.config.yaml"))
_mcp_settings.mcp.servers["research_agent"].args = [
    "--directory", str(settings.server_main_path),
    "run", "python", "-m", "src.server", "--transport", "stdio",
]
app = MCPApp(name="ResearchClient", settings=_mcp_settings)

ARTICLE_GUIDELINE_FILENAME = "article_guideline.md"

# Names matching mcp_server/src/config/constants.py
_RESEARCH_OUTPUT_FOLDER = ".research"
_RESEARCH_MD_FILE = "research.md"
_DEDUPLICATED_RESEARCH_FILE = "deduplicated_research.md"
_NO_EXPLORATION_SUFFIX = "_no_exploration"

# Kickoff suffix injected for each variant
_KICKOFF_NO_EXPLORATION = (
    "Please execute the full workflow now without asking for confirmation.\n"
    "IMPORTANT OVERRIDE: Use 0 exploration rounds — skip step 4 (the entire "
    "exploration phase) and proceed directly from step 3 to step 5."
)

_KICKOFF_EXPLORATION_ONLY = (
    "The exploitation phase is already complete — steps 1, 2, and 3 have been "
    "run and all intermediate files are present in the .research/ subdirectory.\n"
    "Please start from step 4 (the exploration phase) and continue through "
    "steps 5 to 8 without asking for confirmation, using the n_max_round value "
    "specified in the workflow instructions above."
)

_KICKOFF_FULL = (
    "Please execute the full workflow now without asking for confirmation."
)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def discover_samples(samples_dir: Path) -> List[Path]:
    """Return sorted list of sub-dirs that contain an article_guideline.md."""
    if not samples_dir.is_dir():
        raise FileNotFoundError(f"Samples directory not found: {samples_dir}")
    found = sorted(
        d for d in samples_dir.iterdir()
        if d.is_dir() and (d / ARTICLE_GUIDELINE_FILENAME).exists()
    )
    return found


def _rename_no_exploration_outputs(sample_dir: Path) -> None:
    """
    After the exploitation-only run, rename the two output files so that the
    subsequent exploration run can write fresh versions with the default names.

    Renames:
        research.md                         → research_no_exploration.md
        .research/deduplicated_research.md  → .research/deduplicated_research_no_exploration.md
    """
    research_md = sample_dir / _RESEARCH_MD_FILE
    if research_md.exists():
        dest = sample_dir / (_RESEARCH_MD_FILE.replace(".md", f"{_NO_EXPLORATION_SUFFIX}.md"))
        research_md.rename(dest)
        logging.info(f"Renamed {research_md.name} → {dest.name}")

    dedup_md = sample_dir / _RESEARCH_OUTPUT_FOLDER / _DEDUPLICATED_RESEARCH_FILE
    if dedup_md.exists():
        dest = dedup_md.parent / _DEDUPLICATED_RESEARCH_FILE.replace(
            ".md", f"{_NO_EXPLORATION_SUFFIX}.md"
        )
        dedup_md.rename(dest)
        logging.info(f"Renamed {dedup_md.name} → {dest.name}")


async def _run_variant(
    sample_dir: Path,
    agent: Agent,
    tools: list,
    prompt_content: str,
    kickoff_suffix: str,
    thinking_enabled: bool,
    label: str,
    context_history: list | None = None,
) -> bool:
    """
    Run the research workflow for one variant of a sample directory.

    Each call starts with a copy of context_history (the pre-batch conversation
    established between the user and the agent), then appends the sample-specific
    kickoff message.  This lets any natural-language instructions the user gave
    before the batch take effect without any special encoding.

    Returns True on success, False on failure.
    """
    conversation_history: list = list(context_history or [])
    kickoff_message = (
        f"{prompt_content}\n\n"
        f"The research directory is: {sample_dir.resolve()}\n"
        f"{kickoff_suffix}"
    )
    conversation_history.append(make_user_message(kickoff_message))

    try:
        await handle_agent_loop(conversation_history, tools, agent, thinking_enabled)
        return True
    except Exception:
        logging.exception(f"[{label}] Failed processing sample: {sample_dir}")
        return False


async def run_single_sample(
    sample_dir: Path,
    agent: Agent,
    tools: list,
    prompt_content: str,
    thinking_enabled: bool,
    two_variants: bool = False,
    context_history: list | None = None,
) -> bool:
    """
    Run the research workflow for one sample directory.

    When two_variants=True:
      1. Run exploitation-only (step 4 skipped, 0 exploration rounds).
      2. Rename research.md → research_no_exploration.md and
         .research/deduplicated_research.md → …_no_exploration.md.
      3. Run exploration-only (starts at step 4, reuses existing intermediates)
         which re-executes steps 5-8 and writes the final research.md.

    context_history is forwarded to every _run_variant call as a conversation
    prefix (see _run_variant for details).

    Returns True only if all required variant runs succeed.
    """
    if not two_variants:
        return await _run_variant(
            sample_dir, agent, tools, prompt_content,
            _KICKOFF_FULL, thinking_enabled, label="full",
            context_history=context_history,
        )

    # --- Variant 1: exploitation only ---
    print(f"    → Variant 1/2: exploitation only (no exploration rounds)")
    ok1 = await _run_variant(
        sample_dir, agent, tools, prompt_content,
        _KICKOFF_NO_EXPLORATION, thinking_enabled, label="no-exploration",
        context_history=context_history,
    )
    if not ok1:
        return False

    _rename_no_exploration_outputs(sample_dir)

    # --- Variant 2: exploration phase + re-run steps 5–8 ---
    print(f"    → Variant 2/2: exploration phase (continues from existing .research/)")
    ok2 = await _run_variant(
        sample_dir, agent, tools, prompt_content,
        _KICKOFF_EXPLORATION_ONLY, thinking_enabled, label="with-exploration",
        context_history=context_history,
    )
    return ok2


# --------------------------------------------------------------------------- #
# Batch execution helpers
# --------------------------------------------------------------------------- #

def _dedup_paths(paths: List[Path]) -> List[Path]:
    """De-duplicate a list of paths while preserving order."""
    seen: set = set()
    result: List[Path] = []
    for p in paths:
        resolved = p.resolve()
        if resolved not in seen:
            seen.add(resolved)
            result.append(p)
    return result


async def _run_batch(
    sample_dirs: List[Path],
    agent: Agent,
    tools: list,
    prompt_content: str,
    thinking_enabled: bool,
    two_variants: bool,
    context_history: list | None = None,
) -> List[Tuple[Path, str, float]]:
    """Process a list of sample directories and return (path, status, elapsed) tuples."""
    results: List[Tuple[Path, str, float]] = []
    for idx, sample_dir in enumerate(sample_dirs, 1):
        print(f"\n{'─'*60}")
        print(f"  [{idx}/{len(sample_dirs)}] Processing: {sample_dir}")
        print(f"{'─'*60}\n")
        t0 = time.time()
        success = await run_single_sample(
            sample_dir=sample_dir,
            agent=agent,
            tools=tools,
            prompt_content=prompt_content,
            thinking_enabled=thinking_enabled,
            two_variants=two_variants,
            context_history=context_history,
        )
        elapsed = time.time() - t0
        status = "OK" if success else "FAILED"
        results.append((sample_dir, status, elapsed))
        print(f"\n  [{idx}/{len(sample_dirs)}] {status} in {elapsed:.1f}s — {sample_dir}\n")
    return results


def _print_batch_summary(results: List[Tuple[Path, str, float]]) -> None:
    print(f"\n{'='*60}")
    print("  Batch Summary")
    print(f"{'='*60}")
    for sample_dir, status, elapsed in results:
        print(f"  {status:>6}  {elapsed:>7.1f}s  {sample_dir}")
    n_ok = sum(1 for _, s, _ in results if s == "OK")
    print(f"\n  {n_ok}/{len(results)} succeeded")
    print(f"{'='*60}\n")


# --------------------------------------------------------------------------- #
# Interactive REPL helpers
# --------------------------------------------------------------------------- #

def _resolve_paths_to_samples(tokens: List[str], quiet: bool = False) -> List[Path]:
    """
    Resolve a list of path strings into sample directories.

    - If the path itself contains article_guideline.md → treat as a sample dir.
    - Otherwise if it is a directory → auto-discover samples within it.

    quiet=True suppresses all warnings, used when probing whether input is
    path-like before falling back to NORMAL_MESSAGE handling.
    """
    sample_dirs: List[Path] = []
    for token in tokens:
        p = Path(token)
        if not p.exists():
            if not quiet:
                print(f"  ⚠  Path not found, skipping: {p}")
            continue
        if (p / ARTICLE_GUIDELINE_FILENAME).exists():
            sample_dirs.append(p)
        elif p.is_dir():
            discovered = discover_samples(p)
            if not discovered and not quiet:
                print(f"  ⚠  No samples found in: {p}")
            sample_dirs.extend(discovered)
        else:
            if not quiet:
                print(f"  ⚠  Not a directory, skipping: {p}")
    return sample_dirs


def _parse_interactive_input(
    line: str,
    current_two_variants: bool,
    current_thinking: bool,
    quiet: bool = False,
) -> Tuple[List[Path], bool, bool, bool]:
    """
    Parse a line of interactive input.

    Returns (sample_dirs, two_variants, thinking_enabled, should_quit).
    Flags (--two-variants etc.) update the sticky settings for the session;
    paths are resolved to sample directories.

    quiet=True suppresses path-not-found warnings; used when probing input
    to decide whether to treat it as a batch or a NORMAL_MESSAGE.
    """
    try:
        tokens = shlex.split(line)
    except ValueError as exc:
        if not quiet:
            print(f"  ⚠  Parse error: {exc}")
        return [], current_two_variants, current_thinking, False

    if not tokens:
        return [], current_two_variants, current_thinking, False

    if tokens[0] in ("/quit", "quit", "exit", "/exit"):
        return [], current_two_variants, current_thinking, True

    two_variants = current_two_variants
    thinking = current_thinking
    path_tokens: List[str] = []

    for tok in tokens:
        if tok == "--two-variants":
            two_variants = True
        elif tok == "--no-two-variants":
            two_variants = False
        elif tok == "--thinking":
            thinking = True
        elif tok == "--no-thinking":
            thinking = False
        else:
            path_tokens.append(tok)

    sample_dirs = _resolve_paths_to_samples(path_tokens, quiet=quiet)
    return sample_dirs, two_variants, thinking, False


async def _interactive_loop(
    agent: Agent,
    tools: list,
    resources: list,
    prompts: list,
    prompt_content: str,
    thinking_enabled: bool,
    two_variants: bool,
) -> None:
    """
    Interactive REPL: accept new batch specifications without restarting the agent.

    The agent and MCP server stay alive between batches.  Each batch still gets
    fresh conversation histories, so no cross-batch context leakage occurs.

    Sticky flags (--two-variants, --no-thinking, etc.) persist across prompts
    within the session until explicitly changed.
    """

    current_two_variants = two_variants
    current_thinking = thinking_enabled
    repl_conversation_history: list = []

    while True:

        print(f"\n{'='*60}")
        print("  Interactive mode — agent is running, server stays alive.")
        print("  Specify the next batch, chat with the agent, or use a command.")
        print()
        print("  Batch input formats:")
        print("    /path/to/parent_dir            → auto-discover samples inside")
        print("    /path/A /path/B                → explicit sample dirs")
        print("    --two-variants /path/to/dir    → enable two-variant mode")
        print("    --no-two-variants /path/to/dir → disable two-variant mode")
        print("    --no-thinking /path/to/dir     → disable LLM thinking")
        print("    --thinking /path/to/dir        → re-enable LLM thinking")
        print()
        print("  Natural language:")
        print("    Any other text is sent to the agent as a normal message")
        print("    and the reply is shown here.")
        print()
        print("  Info commands:")
        print("    /tools                         → list available tools")
        print("    /resources                     → list available resources")
        print("    /prompts                       → list available prompts")
        print("    /resource/<uri>                → print resource content")
        print("    /prompt/<name>                 → print prompt content")
        print("    /quit                          → shut down")
        print(f"{'='*60}\n")

        indicators = []
        if current_two_variants:
            indicators.append("two-variants")
        if not current_thinking:
            indicators.append("no-thinking")
        indicator_str = f" [{', '.join(indicators)}]" if indicators else ""

        try:
            line = input(f"Please enter either 📂 Next batch, or 🤖 commands{indicator_str}: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            logging.info("Interrupted. Goodbye!")
            break

        if not line:
            continue

        # --- Check for slash-commands first (reuse the client's parser) ---
        parsed = parse_user_input(line)

        if parsed.input_type == InputType.TERMINATE:
            logging.info("Shutting down. Goodbye!")
            break

        if parsed.input_type in (
            InputType.COMMAND_INFO_TOOLS,
            InputType.COMMAND_INFO_RESOURCES,
            InputType.COMMAND_INFO_PROMPTS,
        ):
            handle_command(parsed, tools, resources, prompts)
            print("  (When you're ready, please provide a batch directory to start the agent.)\n")
            continue

        if parsed.input_type == InputType.COMMAND_RESOURCE:
            await handle_resource_command(parsed.resource_uri, resources, agent)
            print("  (When you're ready, please provide a batch directory to start the agent.)\n")
            continue

        if parsed.input_type == InputType.COMMAND_PROMPT:
            await handle_prompt_command(parsed.prompt_name, prompts, agent)
            print("  (When you're ready, please provide a batch directory to start the agent.)\n")
            continue

        if parsed.input_type == InputType.COMMAND_UNKNOWN:
            print(f"  Unknown command: '{line}'")
            print(
                "  Commands: /tools, /resources, /prompts, "
                "/resource/<uri>, /prompt/<name>, /quit"
            )
            continue

        # --- Not a slash-command: probe as batch path input first ---
        sample_dirs, new_two_variants, new_thinking, should_quit = \
            _parse_interactive_input(line, current_two_variants, current_thinking, quiet=True)

        if should_quit:
            logging.info("Shutting down. Goodbye!")
            break

        if not sample_dirs:
            # Nothing resolved to valid sample dirs → treat as NORMAL_MESSAGE
            repl_conversation_history.append(make_user_message(line))
            try:
                await handle_agent_loop(
                    repl_conversation_history, tools, agent, current_thinking
                )
            except KeyboardInterrupt:
                print("\n  Interrupted.\n")
            continue

        # Batch input confirmed — apply any flag changes now
        current_two_variants, current_thinking = new_two_variants, new_thinking

        sample_dirs = _dedup_paths(sample_dirs)
        print(f"\n  Queued {len(sample_dirs)} sample(s):")
        for i, d in enumerate(sample_dirs, 1):
            print(f"    {i:>3}. {d}")
        print()

        # --- Optional pre-batch message to the agent ---
        batch_context: list = []
        try:
            pre_msg = input(
                "💬 Message to agent before batch to apply to the incoming batch (Enter to skip): "
            ).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            logging.info("Interrupted. Goodbye!")
            break
        if pre_msg:
            batch_context.append(make_user_message(pre_msg))
            try:
                await handle_agent_loop(batch_context, tools, agent, current_thinking)
            except KeyboardInterrupt:
                print("\n  Interrupted.\n")

        try:
            results = await _run_batch(
                sample_dirs, agent, tools, prompt_content,
                current_thinking, current_two_variants,
                context_history=batch_context or None,
            )
            _print_batch_summary(results)
        except KeyboardInterrupt:
            print(
                "\n  Batch cancelled (Ctrl+C). "
                "The agent is still running — enter a new batch or /quit.\n"
            )




async def main() -> None:
    parser = argparse.ArgumentParser(description="Batch research agent runner")
    parser.add_argument(
        "--samples-dir",
        type=Path,
        default=None,
        help="Root directory whose sub-directories each contain an article_guideline.md",
    )
    parser.add_argument(
        "--sample",
        type=Path,
        action="append",
        default=[],
        help="Explicit sample directory (can be repeated). Combined with --samples-dir.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List samples that would be processed without actually running them.",
    )
    parser.add_argument(
        "--two-variants",
        action="store_true",
        help=(
            "For each sample, generate two research files: "
            "(1) research_no_exploration.md — exploitation phase only; "
            "(2) research.md — full workflow including the exploration phase. "
            "Both are written to the same sample directory."
        ),
    )
    parser.add_argument(
        "--thinking",
        action="store_true",
        default=True,
        help="Enable LLM thinking/reasoning (default: enabled).",
    )
    parser.add_argument(
        "--no-thinking",
        action="store_true",
        help="Disable LLM thinking/reasoning.",
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help=(
            "Exit after processing the initial batch instead of entering "
            "interactive mode.  Useful for CI / scripted pipelines."
        ),
    )
    args = parser.parse_args()

    thinking_enabled = not args.no_thinking

    # Collect initial sample directories from CLI (all optional)
    initial_dirs: List[Path] = list(args.sample)
    if args.samples_dir:
        initial_dirs.extend(discover_samples(args.samples_dir))
    initial_dirs = _dedup_paths(initial_dirs)

    if args.dry_run:
        variant_label = " [two-variants]" if args.two_variants else ""
        if initial_dirs:
            print(f"\n  Would process {len(initial_dirs)} sample(s){variant_label}:")
            for i, d in enumerate(initial_dirs, 1):
                print(f"    {i:>3}. {d}")
        else:
            print("  No initial samples specified.")
        print("\nDry-run complete. No processing performed.")
        return

    if args.non_interactive and not initial_dirs:
        print("No sample directories specified. Use --samples-dir or --sample.")
        sys.exit(1)

    # ----- Start the MCP server ONCE -----
    async with app.run():
        if configure_opik():
            logging.info("📊 Opik monitoring enabled")
        else:
            logging.info("📊 Opik monitoring disabled (missing configuration)")

        agent = Agent(
            name="research_agent",
            instruction="You are a research agent. Use the provided tools, resources, and prompts to solve complex queries.",
            server_names=["research_agent"],
        )

        async with agent:
            tools, resources, prompts = await get_capabilities_from_mcp_client(agent)
            print_startup_info(tools, resources, prompts)

            # Load the research prompt template once
            prompt_name = "research_agent_full_research_instructions_prompt"
            matching = [p for p in prompts if p.name == prompt_name]
            if not matching:
                logging.error(
                    f"Prompt '{prompt_name}' not found on server. "
                    f"Available: {[p.name for p in prompts]}"
                )
                sys.exit(1)
            prompt_result = await agent.get_prompt(prompt_name)
            prompt_content = prompt_result.messages[0].content.text

            # ----- Process initial CLI batch if any -----
            if initial_dirs:
                print(f"\n{'='*60}")
                print(f"  Batch Research Agent — {len(initial_dirs)} initial sample(s)")
                print(f"{'='*60}")
                for i, d in enumerate(initial_dirs, 1):
                    print(f"  {i:>3}. {d}")
                print()
                results = await _run_batch(
                    initial_dirs, agent, tools, prompt_content,
                    thinking_enabled, args.two_variants,
                )
                _print_batch_summary(results)

            if args.non_interactive:
                return

            # ----- Interactive mode: accept more batches without restarting -----
            await _interactive_loop(
                agent, tools, resources, prompts, prompt_content,
                thinking_enabled, args.two_variants,
            )


if __name__ == "__main__":
    asyncio.run(main())
