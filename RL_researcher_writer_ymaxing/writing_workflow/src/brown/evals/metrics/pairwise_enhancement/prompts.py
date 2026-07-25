"""Prompt template for the pairwise depth/breadth-enhancement comparison metric."""

_SYSTEM_PROMPT = """You are an expert evaluator comparing two renderings of the SAME article section,
produced by two different research-and-writing pipelines (labeled A and B). Both renderings are
meant to cover the same guideline demand for this section; they differ only in how much (and how
well) additional research-derived content was integrated beyond the core topic.

Your task: judge which document, A or B, contains MORE distinct, substantive, source-attributed
enhancement content, separately for TWO dimensions:

- **depth**: goes DEEPER into a topic the section already covers -- e.g. a specific mechanism,
  technical limitation, edge case, or quantitative detail that adds rigor to an existing point,
  rather than covering new topic ground.
- **breadth**: covers a genuinely NEW, adjacent sub-topic, example, or application the section's
  core coverage does not touch, broadening the section's scope rather than deepening an existing
  point.

## What counts as a qualifying instance (either dimension)

- The instance must be traceable to specific, concrete information (a named study, statistic,
  technical mechanism, named framework/tool, or comparable specific claim) -- not vague statements
  ("this is an active area of research") or restatements of the section's core topic in different
  words.
- Two instances that make essentially the same point (even if worded differently) count as ONE
  instance, not two.

## Instructions

1. Read the section's guideline demand (what this section is supposed to cover) for context on
   what counts as "core" vs. "beyond the core."
2. Read document A. For EACH dimension (depth, breadth) separately, list every distinct qualifying
   instance you find, in your own words (brief phrases, not full quotes).
3. Read document B. Do the same, for each dimension separately.
4. For each dimension, compare the two lists directly:
   - Any instance in A's list not equivalent to something in B's list goes in that dimension's
     `a_instances`.
   - Any instance in B's list not equivalent to something in A's list goes in that dimension's
     `b_instances`.
   - Instances present in both lists (even if worded differently) do NOT appear in either output
     list -- they are shared coverage, not a differentiator.
5. For each dimension, decide `preference` based on the RELATIVE size and substantiveness of
   `a_instances` vs. `b_instances`:
   - `tie`: both lists are empty, or both have a similar number of comparably substantive instances.
   - `b_more` / `a_more`: one side has more instances, or clearly more substantive ones, but the
     difference is modest.
   - `b_much_more` / `a_much_more`: one side has substantially more instances, or dramatically more
     substantive ones (e.g. B has 3+ genuinely new instances A entirely lacks).
6. `tie` is a normal, expected, frequent outcome for BOTH dimensions independently -- do not force
   a preference when the two documents are genuinely comparable. Most sections in this corpus have
   ZERO qualifying instances in either document for one or both dimensions; that is correctly a
   `tie` for that dimension.
7. depth and breadth are judged INDEPENDENTLY -- a section can tie on depth while one document
   clearly leads on breadth, or vice versa.

## Output

Return a `depth` judgment and a `breadth` judgment (each with `preference`, `a_instances`,
`b_instances`), plus one overall `reasoning` string covering both dimensions.
"""


def get_pairwise_prompt(
    section_guideline: str,
    doc_a: str,
    doc_b: str,
) -> str:
    """Build the pairwise comparison prompt for one section (both dimensions in one call).

    Args:
        section_guideline: The guideline's demand text for this specific section
            (e.g. target words + key points/bullets), for context on what's "core."
        doc_a: Document A's rendering of this section (plain section body text).
        doc_b: Document B's rendering of this section (plain section body text).
    """
    return f"""{_SYSTEM_PROMPT}

<section_guideline>
{section_guideline}
</section_guideline>

<document_a>
{doc_a}
</document_a>

<document_b>
{doc_b}
</document_b>
"""
