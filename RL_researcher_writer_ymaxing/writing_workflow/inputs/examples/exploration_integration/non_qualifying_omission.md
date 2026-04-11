## Exploration Integration Example: Non-Qualifying Source (Correctly Omitted)

This example demonstrates correctly identifying that an exploration source adds no genuine depth or
breadth beyond what the exploitation sources already cover — and omitting it entirely.

---

### Exploration Source

```xml
<research_source phase="exploration" type="tavily" url="https://example-blog.io/fine-tuning-vs-prompting">
Fine-tuning and prompt engineering are two complementary approaches for guiding large language model
behaviour. Fine-tuning updates the model's weights on a domain-specific dataset, adapting its internal
representations to the target task so the model can perform it without lengthy instructions in the prompt.

Prompt engineering, by contrast, leaves the model's weights unchanged and instead crafts the input text
to elicit the desired output. It is faster to iterate on, requires no labelled data, and allows a single
base model to serve many different applications.

The choice between them depends on task complexity, data availability, and latency requirements. For most
enterprise use cases, starting with prompt engineering is recommended; fine-tuning should be reserved for
cases where prompt engineering has already been exhausted.
</research_source>
```

### Assessment

**Does not qualify.** The core article's exploitation sources already provide a thorough comparison of
fine-tuning and prompt engineering, including when to use each, their resource trade-offs, and the
recommendation to exhaust prompt engineering before fine-tuning. This exploration source covers the same
ground at a higher level and introduces no new specifics — no additional data points, failure modes,
alternative perspectives, or adjacent concepts not already present in the article. It adds no depth or
breadth beyond what is written.

---

### Core Section (Before Integration)

**When to Fine-Tune vs. Prompt Engineer**

Fine-tuning adapts the model's weights to a specific domain by training on a curated labelled dataset.
This produces a specialized model that can perform the target task without verbose instructions, lowering
latency and per-call token cost. The trade-off is significant upfront investment: collecting and
labelling data, running training jobs, and managing model versions.

Prompt engineering leaves the base model unchanged and guides it entirely through input design. It
requires no labelled data and iterates in hours rather than weeks. For most production use cases,
investing first in context engineering and prompt design delivers faster results at lower cost than
fine-tuning. Reserve fine-tuning for tasks where prompt engineering has reached a hard ceiling —
typically narrow, repetitive tasks with ample high-quality labelled data.

---

### Integrated Section (After Integration)

*(No changes. The article remains identical to the core section above.)*

---

### Explanation

The source was correctly omitted. Every claim it makes — the definition of fine-tuning, the definition
of prompt engineering, the recommendation to exhaust prompt engineering first — is already explicitly
present in the exploitation-source content reflected in the core article. Integrating this source would
duplicate existing content, adding no value to the reader.
