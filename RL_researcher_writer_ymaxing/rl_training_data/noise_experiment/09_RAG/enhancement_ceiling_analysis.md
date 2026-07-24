# The enhancement ceiling and its word-count cost

*Analysis of presets 1, 3, and 5 (replicates 1-3), RAG lesson grading audit*

## What the from-scratch recount confirms

I re-parsed all 12 generated articles programmatically against each preset's
exploration-URL set (23 URLs for preset 1, 55 for preset 3, 103 for preset 5),
collapsing same-source adjacent citations into a single instance per the
counting rule specified. No audit recollection involved — this is a direct
recount from the source files. Three findings:

**1. The enhancement ceiling is absolute.** Across 54 body-sections in
presets 1/3/5: all 31 zero-instance sections score enh=0, and all 23 sections
with ≥1 instance score enh=1 — including every 6-instance section. There is
no example anywhere in the data of a second, third, or sixth instance buying
additional enhancement credit. The ceiling claim is exact.

**2. Instance count drives word-count overage (r = +0.56).** The mean
deviation from target climbs from −17 words (zero instances, slightly under
budget) up to +105 (four instances) and +93 (six instances). Surplus
instances convert into length, and length is what the guideline_adherence
metric polices.

| instances in section | mean words vs. target |
|---|---|
| 0 | −17.0 |
| 1 | +20.2 |
| 2 | +6.1 |
| 3 | +52.3 |
| 4 | +105.0 |
| 6 | +93.0 |

**3. The single-section proof is the cleanest cut.** Holding "Advanced RAG
Techniques" constant across all nine replicates: instance count ranges 2→6
and word overage ranges +47→+152, yet the enhancement score is 1 in every
single case.

| replicate | instances | word count | overage vs. 910-word target |
|---|---|---|---|
| p1r1 | 3 | 975 | +65 |
| p1r2 | 2 | 957 | +47 |
| p1r3 | 3 | 961 | +51 |
| p3r1 | 4 | 1021 | +111 |
| p3r2 | 2 | 967 | +57 |
| p3r3 | 4 | 1062 | +152 |
| p5r1 | 6 | 1043 | +133 |
| p5r2 | 6 | 995 | +85 |
| p5r3 | 6 | 971 | +61 |

The two heaviest-overage cases (p3r3 at +152, p5r1 at +133) are exactly the
ones that tipped into guideline_adherence *failure* — identical enhancement
reward, escalating length penalty.

## Where the original hypothesis was right, and where the recount corrects it

Per-preset aggregates:

| preset | total instances | enhancement (depth + breadth) | core_content | flow | guideline |
|---|---|---|---|---|---|
| 1 | 20 | 0.619 | 0.524 | 0.571 | 0.500 |
| 3 | 14 | 0.429 | 0.571 | 0.524 | 0.500 |
| 5 | 30 | 0.619 | 0.476 | 0.571 | **0.389** |

- **Ceiling half — confirmed and quantified.** Preset 5 inserted 30 instances
  to preset 1's 20, yet earned identical enhancement (0.619). The extra 10
  instances were pure dead weight, scoring-wise.
- **Cost half — confirmed, but the victim is specifically
  guideline_adherence.** Preset 5, the heaviest inserter, has by far the
  lowest guideline score (0.389) because its dense sections overran word
  budgets. Flow is flat (immune — insertions don't disturb ordering or media
  placement). Core_content runs *backwards* from the naive prediction:
  preset 3 (fewest instances) has the *highest* core_content, because
  core_content penalizes ground-truth *omissions*, which are additive-
  independent of enhancement content.
- **One correction to the original framing:** the recount shows preset 3 is
  the *lightest* inserter overall (14 instances), not a heavy one. Its
  exploration-heavy feel came from concentration — it dumped 3-4 instances
  into single sections (its Advanced RAG section hit +152 overage, the worst
  in the whole dataset) rather than spreading them across the article. So
  "extensive use" is better measured as per-section density than per-preset
  total, and on density preset 3 is genuinely competitive with preset 5 in
  the one section where it counts.

## Bottom line

Section-level binary scoring caps enhancement reward at the first valid
instance. Surplus instances convert not into higher enhancement scores but
into word-count overage (r ≈ +0.56) that penalizes guideline_adherence —
while leaving flow untouched and core_content independent, since additions
sit beside the ground-truth core rather than displacing it. Preset 5 is the
clearest victim of this trap at the whole-article level; preset 3 shows the
same trap operating locally in its densest section even with a low total
instance count.
