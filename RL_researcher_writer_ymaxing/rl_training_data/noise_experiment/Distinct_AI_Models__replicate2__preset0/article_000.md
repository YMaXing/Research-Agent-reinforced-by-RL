# The Platonic Representation Hypothesis

If you read a story about a dog, you might remember it the next time you see one in a park. This is possible because you have a unified concept of "dog" that is not tied to words or images alone. We humans navigate a multimodal world, seamlessly connecting what we see, hear, and read into a coherent understanding.

AI systems, however, are not always so lucky. They often learn from data of a single type. A language model trains on text, while a computer vision system trains on images. This raises a fundamental question: to what extent do these specialized models, trained in their separate digital worlds, develop a shared understanding of a concept like "dog"?

Researchers investigate this by peering inside AI systems to study how they represent scenes and sentences. Their findings are pointing toward a fascinating conclusion. First, models with different architectures, trained on different datasets or even entirely different data types, can develop remarkably similar internal representations [[1]](https://phillipi.github.io/prh), [[2]](https://arxiv.org/html/2504.08775v1). Second, these representations become more similar as the models grow more capable [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[4]](https://arxiv.org/html/2507.01201v5). This idea, dubbed the Platonic representation hypothesis, has inspired a lively debate and a wave of follow-up research [[5]](https://arxiv.org/html/2511.12121v4), [[6]](https://www.emergentmind.com/topics/multimodal-alignment).

The hypothesis gets its name from Plato's 2,400-year-old Allegory of the Cave [[7]](https://www.alignmentforum.org/posts/kFCu3batN8k8mwtmh/the-cave-allegory-revisited-understanding-gpt-s-worldview). In the allegory, prisoners trapped in a cave perceive the world only through shadows cast on a wall, mistaking these projections for reality. The Platonic representation hypothesis adapts this for AI. The real world outside the cave casts machine-readable shadows as data streams. AI models are the prisoners, exposed only to these streams. The hypothesis claims that as different models become more sophisticated, their internal interpretations of these shadows—their representations—begin to converge on a shared understanding of the world behind the data [[1]](https://phillipi.github.io/prh).

```mermaid
flowchart LR
  %% True Reality
  subgraph "True Reality"
    TR["True Reality<br/>(Actual World)"]
  end

  %% Data Streams (Shadows)
  subgraph "Data Streams"
    DS["Data Streams<br/>(Images, Text, Audio)"]
  end

  %% AI Models (Prisoners)
  subgraph "AI Models"
    AIM["AI Models<br/>(Prisoners)"]
  end

  %% Internal Activations (Interpretations)
  subgraph "Internal Activations"
    IA["Internal Activations<br/>(Interpretations)"]
  end

  %% Flow
  TR -- "casts shadows" --> DS
  DS -- "observed by" --> AIM
  AIM -- "forms" --> IA

  %% Platonic Representation Hypothesis (Convergence)
  IA -. "converge towards shared understanding<br/>(Platonic Representation Hypothesis)" .-> TR

  %% Visual grouping
  classDef reality stroke-width:3px
  classDef data stroke-dasharray:5,5
  classDef processor stroke-width:2px
  classDef interpretation stroke-dasharray:1,1

  class TR reality
  class DS data
  class AIM processor
  class IA interpretation
```
Image 1: Mermaid diagram illustrating Plato's Cave Allegory adapted for AI, showing the flow from True Reality to Data Streams, AI Models, and Internal Activations, with a hypothesis of Platonic Representation leading to convergence of interpretations.

Not everyone is convinced. A key point of contention is how to define and compare these representations. You cannot inspect a model’s representation for every possible sentence or image, so how do you decide which ones are representative? It is unlikely researchers will reach a consensus soon, but that does not bother Phillip Isola, a senior author of the paper that formalized the hypothesis. "Half the community says this is obvious, and the other half says this is obviously wrong," he said. "We were happy with that response" [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Having framed the hypothesis and its philosophical roots, we will now look at the geometric mechanism that makes these comparisons possible.

## The Company Being Kept

If researchers do not agree on Plato, they might find common ground with his predecessor Pythagoras, whose philosophy started from the premise "All is number." This perfectly describes the neural networks that power AI models. Their representations of words or pictures are just long lists of numbers, each indicating the activation of an artificial neuron [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Researchers typically focus on a single layer of a network, writing down the neuron activations as a geometric object called a vector. Modern AI models have thousands of neurons per layer, so their representations are high-dimensional vectors impossible to visualize directly. However, vectors make it easy to compare representations: two are similar if their vectors point in similar directions [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Within a single model, similar inputs tend to have similar representations. The vector for "dog" will be close to vectors for "pet" and "furry," but far from "molasses." This reflects a principle expressed over 60 years ago by linguist John Rupert Firth: "You shall know a word by the company it keeps" [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

But what about representations in different models? Directly comparing activation vectors from separate networks is not meaningful because their coordinate systems are arbitrary. Instead, researchers use indirect methods. One popular approach embraces Firth's quote and measures whether two models' representations of an input keep the same company [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Imagine you want to compare how two language models represent animals. You feed a list of words—dog, cat, wolf, jellyfish—into both and record their representations. In each network, these representations form a cluster of vectors. The question then becomes: how similar are the overall shapes of the two clusters? "It can kind of be described as measuring the similarity of similarities," said Ilia Sucholutsky, an AI researcher at New York University [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107). This technique avoids direct vector comparison by focusing on relational geometry [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Researchers began exploring this in the mid-2010s and found that representations were often similar, though not identical. Intriguingly, a few studies found that more powerful models had more similarities than weaker ones. One 2021 paper dubbed this the "Anna Karenina scenario," a nod to the opening line of Tolstoy's novel. Perhaps successful AI models are all alike, while every unsuccessful model is unsuccessful in its own way [[9]](https://aiscientist.substack.com/p/musing-38-the-platonic-representation), [[10]](https://arxiv.org/html/2507.01201v5).

Much of this early work focused only on computer vision. The rise of powerful language models presented an opportunity to see just how far representational similarity could go [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107). With these measurement tools in hand, we can now look at the hierarchy of experimental evidence suggesting that this convergence strengthens as models scale.

## Convergent Evolution

The story of the Platonic representation hypothesis paper began in early 2023. ChatGPT had been released a few months prior, and it was clear that simply scaling up AI models made them better at many tasks. But it was unclear why. This created an existential question for the field: when performance improves with scale, are models just memorizing dataset quirks, or are they getting better at approximating a true world model?

"Everyone in AI research was going through an existential life crisis," said Minyoung Huh, an OpenAI researcher who was a graduate student in Isola’s lab at the time. He began meeting with Isola and their colleagues to discuss how scaling might affect internal representations [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Their discussions led to a hierarchy of potential evidence for the hypothesis, ordered by increasing strength. The weakest evidence is when models trained on identical data converge. Stronger evidence comes from models trained on different datasets within the same modality. The most compelling evidence would be convergence between models trained on entirely different data types, like vision and language models [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

```mermaid
graph TD
    A["Level 1: Models trained on identical data converge.<br/>(Weakest Evidence)"]
    B["Level 2: Models trained on different data but the same modality still converge.<br/>(Intermediate Evidence)"]
    C["Level 3: Vision models looking at images converge with language models reading only the corresponding captions.<br/>(Strongest Evidence)"]

    A -- "Progression to" --> B
    B -- "Progression to" --> C

    subgraph Strength
        S1["Weakest"]
        S2["Intermediate"]
        S3["Strongest"]
    end

    A -.-> S1
    B -.-> S2
    C -.-> S3

    classDef evidenceNode fill:#fff,stroke:#333,stroke-width:2px
    class A,B,C evidenceNode

    classDef strengthLabel fill:#f9f,stroke:#333,stroke-dasharray: 5 5
    class S1,S2,S3 strengthLabel
```
Image 2: Hierarchy of potential convergence evidence for the Platonic representation hypothesis, ordered by increasing strength.

A year after their initial conversations, Isola and his colleagues wrote a paper reviewing the evidence and arguing for the hypothesis [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107). By then, other researchers had already found evidence of alignment between vision and language models [[1]](https://phillipi.github.io/prh). Huh conducted his own experiment, testing five vision models and eleven language models on a dataset of captioned pictures. He fed the pictures to the vision models and the captions to the language models, then compared the vector clusters. He observed a steady increase in representational similarity as models became more powerful, exactly as the hypothesis predicted [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

After reviewing this evidence, we must also examine the experimental choices that can affect the validity of these results.

## Find the Universals

Of course, it is never so simple. Measurements of representational similarity involve a host of experimental choices that can affect the outcome. Which layers do you compare in each network? Which of the many available metrics do you use? And which representations do you measure in the first place [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)?

"If you only test one dataset, you don’t necessarily know how [the result] generalizes," said Christopher Wolfram, a researcher who has studied representational similarity. "Who knows what would happen if you did some weirder dataset?" [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107). His critique highlights the challenge of distinguishing fundamental properties from arbitrary ones that might reflect structural constraints rather than meaningful convergence [[11]](https://www.preprints.org/manuscript/202601.1018), [[12]](https://arxiv.org/html/2504.08775v1).

This uncertainty has led to two complementary scientific attitudes. One, associated with Isola, actively seeks the universals that models appear to share. "The endeavor of science is to find the universals," he said. "We could study the ways in which models are different or disagree, but that somehow has less explanatory power than identifying the commonalities" [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

The other attitude, held by researchers like Alexei Efros, argues it is more productive to focus on where models differ. Efros noted that in the dataset Huh used, the images and text contained very similar information by design. But much of the data we encounter has features that resist translation. "There is a reason why you go to an art museum instead of just reading the catalog," he said [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Even if perfect, any intrinsic sameness across models can be useful. Last summer, researchers used this partial alignment to translate internal representations of sentences from one language model to another [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[13]](https://arxiv.org/html/2504.08775v1). If language and vision representations are interchangeable to some extent, it could lead to new ways to train models that learn from both data types, enabling more efficient multimodal systems [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[14]](https://www.emergentmind.com/topics/multimodal-alignment), [[5]](https://arxiv.org/html/2511.12121v4).

Despite these promising developments, other researchers think it is unlikely any single theory will fully capture the behavior of modern AI. "You can’t reduce a trillion-parameter system to simple explanations," said Jeff Clune, an AI researcher. "The answers are going to be complicated" [[3]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

## Conclusion

The Platonic representation hypothesis offers a compelling framework for understanding the inner workings of AI. It suggests that as models become more capable, they are not just memorizing data but are converging on a shared, fundamental understanding of the world. This convergence is observed across different architectures, training objectives, and even data modalities, from vision to language.

We have seen how researchers measure this alignment not by direct vector comparison, but by analyzing the "company" that concepts keep within their respective geometric spaces. Evidence is mounting that this alignment increases with model scale and competence, suggesting we are moving toward a unified "world model." However, the hypothesis is not without its critics, who rightly point out the methodological challenges and the importance of studying where models diverge.

For AI engineers, this is more than a philosophical debate. The reality of representational convergence has practical implications. It underpins our ability to build more robust multimodal systems, translate knowledge between models, and create AI that can reason across different data types with greater fidelity. While the full picture is still emerging, understanding this trend is key to designing the next generation of intelligent systems.

## References

- [1] Huh, M., Cheung, B., Wang, T., & Isola, P. (2024). The Platonic Representation Hypothesis. https://phillipi.github.io/prh
- [2] Wolfram, C., & Schein, A. (2025). Layers at Similar Depths Generate Similar Activations Across LLM Architectures. https://arxiv.org/html/2504.08775v1
- [3] Brubaker, B. (2026). Distinct AI Models Seem To Converge On How They Encode Reality. Quanta Magazine. https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107
- [4] Yoon, L. H., Yue, Y., & Kim, B. (2025). Escaping Plato’s Cave: JAM for Aligning Independently Trained Vision and Language Models. https://arxiv.org/html/2507.01201v5
- [5] Fang, W., Zhang, T., & Chan, A. (2025). To Align or Not to Align: Strategic Multimodal Representation Alignment for Optimal Performance. https://arxiv.org/html/2511.12121v4
- [6] Multimodal Alignment. (2025). EmergentMind. https://www.emergentmind.com/topics/multimodal-alignment
- [7] The Cave Allegory Revisited: Understanding GPT's Worldview. (n.d.). Alignment Forum. https://www.alignmentforum.org/posts/kFCu3batN8k8mwtmh/the-cave-allegory-revisited-understanding-gpt-s-worldview
- [8] Sucholutsky, I. (n.d.). Quote on measuring similarity of similarities. Quanta Magazine. https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107
- [9] Musing 38: The Platonic Representation Hypothesis. (2024). AI Scientist. https://aiscientist.substack.com/p/musing-38-the-platonic-representation
- [10] Bansal, Y., Nakkiran, P., & Barak, B. (2021). Revisiting Model Stitching to Compare Neural Representations. https://arxiv.org/html/2106.07682v3
- [11] Christopher Wolfram's critique of representational similarity generalizability. (2026). https://www.preprints.org/manuscript/202601.1018
- [12] Wolfram, C. (n.d.). Critique on representational similarity. https://openreview.net/forum?id=8wKec6faAT
- [13] Jha, R., Zhang, C., Shmatikov, V., & Morris, J. X. (2025). Harnessing the Universal Geometry of Embeddings. https://arxiv.org/html/2505.12540v1
- [14] Gupta, S., Sundaram, S., Wang, C., Jegelka, S., & Isola, P. (2025). Better Together: Leveraging Unpaired Multimodal Data for Stronger Unimodal Models. https://arxiv.org/html/2510.08492v1