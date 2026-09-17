#!/usr/bin/env python3
"""reformat_arxiv.py – Clean firecrawl-scraped arxiv PDF markdown.

Paragraph lines fragmented by PDF column-width rendering are reflowed into
full-width prose.  Tables whose rows are concatenated into raw scraped text
are re-parsed via citation anchors ([NN]) and rebuilt as proper markdown
tables.

Usage
-----
    python reformat_arxiv.py INPUT.md [-o OUTPUT.md] [--schemas SCHEMAS.json]

SCHEMAS.json (optional)
    Maps table numbers (string keys) to column-header lists, e.g.:

        {
            "2": ["Benchmark", "Year", "Evaluation Focus", "Key Features"],
            "7": ["Application", "Year", "Category", "Details"]
        }

    Any table whose number is absent falls back to the default 4-column
    headers: ["Name / Reference", "Year", "Category", "Details"]
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ── Defaults ──────────────────────────────────────────────────────────────────
DEFAULT_HEADERS = ["Name / Reference", "Year", "Category", "Details"]

# ── Low-level helpers ─────────────────────────────────────────────────────────

def jl(lst):
    """Join a list of strings into a single space-normalised string."""
    return " ".join(" ".join(s.split()) for s in lst if s.strip())


def mrow(*cols):
    """Format values as a markdown table row."""
    return "| " + " | ".join(str(c).strip() for c in cols) + " |"


def msep(n):
    """Return a markdown table separator row with *n* columns."""
    return "|" + "|".join(["---"] * n) + "|"


# ── Citation-row parser ───────────────────────────────────────────────────────

# Verbs that open a "description" sentence.  Used to detect where the short
# category label ends and the longer free-text description begins when scanning
# forward through the detail lines that follow a citation anchor.
_DS = re.compile(
    r"^(Contains|Comprises|Features|Evaluates|Uses|A step|Consists|Leverages|"
    r"Designed|Focuses|Baseline|Developed|Provides|Targets|Demonstrates|"
    r"Highlights|Indicates|Addresses|Automates|Enhances|Improves|Manages|"
    r"Enables|Structures|Defines|Facilitates|Sequentially|Hierarchically|"
    r"Utilizes|Applies|Generates|Translates|Coordinates|Replaces|Introduces|"
    r"Proposes|Combines|Diagnoses|Implements|Achieves|Outperforms|Presents|"
    r"Builds|Creates|Supports|Transforms|Analyzes|Processes|Integrates|"
    r"Orchestrates|Employs|Handles|Performs|Trains|Tests|Validates|Simulates|"
    r"Develops|Extracts|Deploys|Constructs|Incorporates|Establishes|Discovers|"
    r"Mimics|Offers|Wraps|Ranks|Represents|Conducts|Decomposes)"
)


def _name_line(s: str) -> bool:
    """Return True if *s* looks like a short paper/tool name fragment."""
    return (
        len(s) <= 35
        and not s.endswith(".")
        and not s.endswith(",")
        and not s.endswith(";")
        and not s.endswith(":")
        and bool(re.match(r"^[A-Z0-9(]", s))
    )


def parse_citation_rows(lines: list[str]) -> list[tuple]:
    """Parse raw scraped lines that contain citation anchors and return rows.

    Returns a list of ``(name, year, category, details)`` tuples.

    Three citation-anchor patterns are handled:

    * **A** – standalone ``[NN]`` on its own line; name is on the preceding
      lines.
    * **B** – inline-end ``"Prefix [NN]"`` with the year on the very next
      line.
    * **C** – inline-year ``"Name [NN]2025 …"`` where the year immediately
      follows the bracket.
    """
    ci: list[tuple[int, str]] = []
    for j, s in enumerate(lines):
        if re.match(r"^\[\d+\]$", s):
            ci.append((j, "A"))
        elif re.search(r"\[\d+\]\d{4}", s):
            ci.append((j, "C"))
        elif (
            re.search(r"\[\d+\]\s*$", s)
            and j + 1 < len(lines)
            and re.match(r"^\d{4}", lines[j + 1])
        ):
            ci.append((j, "B"))

    if not ci:
        return []

    seen_nums: set[str] = set()
    rows: list[tuple] = []

    for k, (cp, ct) in enumerate(ci):
        # Skip citations that have already appeared (prose summaries after a
        # table repeat the same [NN] anchors; we only want the first occurrence).
        cnum_m = re.search(r"\[([0-9]+)\]", lines[cp])
        if cnum_m:
            cnum = cnum_m.group(1)
            if cnum in seen_nums:
                continue
            seen_nums.add(cnum)

        cl = lines[cp]
        pcp = ci[k - 1][0] if k > 0 else -1

        if ct == "A":
            ref, pfx, ds = cl, "", cp + 1
        elif ct == "B":
            m = re.match(r"^(.*?)(\[\d+\])\s*$", cl)
            ref = m.group(2) if m else re.search(r"\[\d+\]", cl).group()
            pfx = m.group(1).strip() if m else ""
            ds = cp + 1
        else:  # C
            m = re.match(r"^(.*?)(\[\d+\])(.*)", cl)
            pfx = m.group(1).strip() if m else ""
            ref = m.group(2) if m else "[?]"
            yl = m.group(3) if m else ""
            ds = cp

        # Scan backward for short name-like lines that precede the citation
        ns = cp
        for j in range(cp - 1, pcp, -1):
            if _name_line(lines[j]):
                ns = j
            else:
                break

        np2 = list(lines[ns:cp])
        if pfx:
            np2.append(pfx)
        name = (jl(np2) + " " if np2 else "") + ref

        # Determine the end of this citation's detail lines
        if k + 1 < len(ci):
            ncp, nt = ci[k + 1]
            if nt == "A":
                de = ncp
                for j in range(ncp - 1, cp, -1):
                    if _name_line(lines[j]):
                        de = j
                    else:
                        break
            else:
                de = ncp
        else:
            de = len(lines)

        dl = ([yl] if ct == "C" and yl.strip() else []) + list(
            lines[cp + 1 if ct == "C" else ds : de]
        )

        year, cat, det = "-", "", ""
        if dl:
            first = dl[0].strip()
            m = re.match(r"^(\d{4})\s*(.*)", first)
            if m:
                year, cr = m.group(1), m.group(2).strip()
            else:
                cr = first
            cp3, di = [cr] if cr else [], 1
            for j in range(1, min(len(dl), 4)):
                c = dl[j].strip()
                t = jl(cp3 + [c])
                if len(t) <= 35 and not _DS.match(c):
                    cp3.append(c)
                    di = j + 1
                else:
                    break
            cat = jl(cp3)
            det = jl(dl[di:])

        rows.append((name, year, cat, det))

    return rows


# ── Generic table formatter ───────────────────────────────────────────────────

def _fmt_gen(raw_lines: list[str], hdrs: list[str]) -> str:
    """Reformat raw scraped table lines into a markdown table.

    *hdrs* must have exactly 4 elements (Name/Ref, Year, Category, Details).
    If a paper uses different column semantics, pass the appropriate labels via
    *hdrs*; the underlying citation-anchor parsing is column-agnostic.
    """
    result = [mrow(*hdrs), msep(4)]
    stripped = [l.strip() for l in raw_lines if l.strip()]

    # Drop any residual column-header row at the top of the raw block
    fc = next(
        (j for j, s in enumerate(stripped) if re.search(r"\[\d+\]", s)), None
    )
    if fc and fc > 0:
        he = 0
        for j, s in enumerate(stripped[:fc]):
            if re.search(
                r"Year|Evaluation|Features|Benchmark\s*/?$|Framework|"
                r"Workflow|Application|Agent\s*/|Use\s*Case|Primary|"
                r"Core\s*Idea|Key\s*Advantage|Category|Objective|Method",
                s,
                re.IGNORECASE,
            ):
                he = j + 1
        stripped = stripped[he:]

    for nm, yr, cat, det in parse_citation_rows(stripped):
        result.append(mrow(nm, yr, cat, det))

    return "\n".join(result)


# ── Table dispatcher ──────────────────────────────────────────────────────────

def format_table_block(n: int, raw: list[str], schemas: dict) -> str:
    """Format a raw table block using headers from *schemas* (or default)."""
    hdrs = schemas.get(str(n), DEFAULT_HEADERS)
    return _fmt_gen(raw, hdrs)


# ── Paragraph reflow ──────────────────────────────────────────────────────────

_SP = re.compile(
    r"^(?:#{1,5}\s|\*\*Table\s\d+|\*Figure\s\d+|\*\*[A-Z*]|\||Phase:|>)"
)


def _is_special(line: str) -> bool:
    s = line.strip()
    return not s or bool(_SP.match(s))


def reflow_paragraphs(lines: list[str]) -> list[str]:
    """Join short PDF-column-width lines into full-width prose paragraphs."""
    result: list[str] = []
    para: list[str] = []

    def flush() -> None:
        if para:
            result.append(" ".join(para))
            para.clear()

    for line in lines:
        s = line.rstrip("\n") if isinstance(line, str) else line
        if _is_special(s):
            flush()
            result.append(s)
        else:
            w = s.strip()
            if w:
                para.append(w)

    flush()
    return result


# ── Main pipeline ─────────────────────────────────────────────────────────────

def process(text: str, schemas: dict | None = None) -> str:
    """Transform raw firecrawl-scraped arxiv markdown into clean markdown."""
    if schemas is None:
        schemas = {}

    lines = text.split("\n")
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        m = re.match(r"^\*\*Table (\d+):", line)
        if m:
            tn = int(m.group(1))
            out.append(line)
            i += 1
            # Preserve blank line that sometimes follows the table title
            if i < len(lines) and not lines[i].strip():
                out.append("")
                i += 1
            # Collect raw table lines until the next heading or table title
            raw: list[str] = []
            while i < len(lines):
                tl = lines[i]
                if re.match(r"^#{1,5}\s", tl) or re.match(
                    r"^\*\*Table \d+:", tl
                ):
                    break
                raw.append(tl)
                i += 1
            while raw and not raw[-1].strip():
                raw.pop()
            out.append("")
            out.extend(format_table_block(tn, raw, schemas).split("\n"))
            out.append("")
        else:
            out.append(line)
            i += 1

    return "\n".join(reflow_paragraphs(out))


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Clean firecrawl-scraped arxiv PDF markdown.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("input", help="Input .md file (firecrawl scrape)")
    ap.add_argument(
        "-o",
        "--output",
        help="Output .md file (default: <input stem>-CLEAN.md alongside input)",
    )
    ap.add_argument(
        "--schemas",
        metavar="FILE",
        help=(
            "JSON file mapping table numbers to column-header lists, e.g. "
            '\'{"2": ["Benchmark","Year","Focus","Details"]}\''
        ),
    )

    args = ap.parse_args()

    inp = Path(args.input)
    if not inp.exists():
        sys.exit(f"Error: input file not found: {inp}")

    out = (
        Path(args.output)
        if args.output
        else inp.parent / (inp.stem + "-CLEAN.md")
    )

    schemas: dict = {}
    if args.schemas:
        schemas_path = Path(args.schemas)
        if not schemas_path.exists():
            sys.exit(f"Error: schemas file not found: {schemas_path}")
        schemas = json.loads(schemas_path.read_text(encoding="utf-8"))

    src = inp.read_text(encoding="utf-8")
    res = process(src, schemas)
    out.write_text(res, encoding="utf-8")

    print(f"Done → {out}")
    print(f"  Input:  {len(src.splitlines()):,} lines")
    print(f"  Output: {len(res.splitlines()):,} lines")


if __name__ == "__main__":
    main()
