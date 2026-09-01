"""Guidance for the user-directed exploration-plan override (workflow step 3.4).

Pure, static, no-I/O helper: the actual "ask the user" interaction happens in whatever LLM/host
is driving the conversation (any MCP client), following the instruction in
research_instructions_prompt.py to call this tool before predict_exploration_preset when
settings.user_plan_override_allowed is True.
"""

from typing import Any, Dict

from ..config.settings import settings

_GUIDANCE = (
    "🎛️ The RL model is about to recommend how many exploration rounds to run and what each round "
    "should focus on. The user may override this instead of letting it decide automatically. To "
    "override, they can specify any of: 🔢 total round count, 🎯 each round's focus (depth / "
    "breadth / balanced), ⚖️ an optional depth-vs-breadth split for a balanced round (e.g. \"70% "
    "depth\"), and/or 🔍 a query count per round. They can give a full plan now, or wait and give "
    "a relative adjustment once they see the recommendation. 🚧 Requesting more rounds than the "
    "configured maximum is capped automatically."
)

_EXAMPLES = [
    "🔁 run 2 rounds: depth then breadth",
    "🎯 just 1 round, focus on breadth",
    "⏭️ skip exploration entirely",
    "⚖️ balanced round with a 70% depth / 30% breadth split",
    "🔁 run 3 rounds: round 1 at 80% depth / 20% breadth, round 2 at 30% depth / 70% breadth, "
    "round 3 pure depth",
    "🔍 use 6 queries per round instead of the default",
    "➕ add one more depth round (relative, after seeing the recommendation)",
    "➖ drop the last round (relative, after seeing the recommendation)",
]


def get_exploration_override_guidance_tool() -> Dict[str, Any]:
    """Return whether overrides are allowed, and if so, guidance/examples to show the user."""
    if not settings.user_plan_override_allowed:
        return {
            "status": "success",
            "override_allowed": False,
            "guidance": "",
            "examples": [],
            "message": (
                "🚫 User overrides are disabled (user_plan_override_allowed=False). Do not ask the "
                "user anything — proceed directly to predict_exploration_preset."
            ),
        }
    return {
        "status": "success",
        "override_allowed": True,
        "guidance": _GUIDANCE,
        "examples": _EXAMPLES,
        "message": (
            "👀 Show 'guidance' and 'examples' to the user now and wait for their response before "
            "deciding whether/how to call predict_exploration_preset."
        ),
    }
