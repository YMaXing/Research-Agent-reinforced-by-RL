# Are All AIs Secretly the Same?

If you read a story about dogs, you will likely remember it the next time you see one bounding through a park. This is possible because you have a unified concept of "dog" that is not tied to words or images alone. AI systems are not always so lucky. They often learn from data of a single type. For example, text for language models or images for computer vision systems. This raises a fundamental question: to what extent do language and vision models have a shared understanding of a "dog"?

Researchers investigate such questions by peering inside AI systems and studying how they represent scenes and sentences. They have found that different AI models can develop similar representations, even if trained on different datasets or entirely different data types [[1](https://arxiv.org/html/2504.08775v1)]. Furthermore, these representations grow more similar as models become more capable [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)]. In a 2024 paper, four AI researchers at the Massachusetts Institute of Technology (MIT) argued that these hints of convergence are no accident [[3](https://phillipi.github.io/prh)]. Their idea, dubbed the Platonic representation hypothesis, has since inspired a lively debate among researchers, with follow-up work exploring everything from explicit alignment mechanisms to the performance of multimodal systems [[4](https://arxiv.org/html/2507.01201v5)], [[5](https://arxiv.org/html/2511.12121v4)], [[6](https://www.emergentmind.com/topics/multimodal-alignment)], [[7](https://www.emergentmind.com/topics/platonic-representation-hypothesis)].

The hypothesis gets its name from Plato's 2,400-year-old Allegory of the Cave, where prisoners trapped inside perceive the world only through shadows cast on a wall. Plato argued that we are all like those prisoners, and the objects we encounter are just pale shadows of ideal "forms" that exist in a realm beyond our senses [[8](https://www.alignmentforum.org/posts/kFCu3batN8k8mwtmh/the-cave-allegory-revisited-understanding-gpt-s-worldview)].

The Platonic representation hypothesis adapts this for AI. The real world outside the cave casts machine-readable "shadows" as streams of data. AI models are the prisoners, and their internal activations are their interpretations of these shadows. The hypothesis claims that as different models become more sophisticated, their interpretations converge on a shared "Platonic representation" of the world behind the data. Phillip Isola, a senior author of the paper, puts it this way: "Why do the language model and the vision model align? Because they’re both shadows of the same world" [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)].

```mermaid
flowchart LR
  %% External Reality
  TR["True Reality"]:::reality

  %% The Allegory of AI & Reality
  subgraph "The Allegory of AI & Reality"
    DS["Data Streams<br/>(Images, Text, Audio)<br/>(Shadows on the Cave Wall)"]:::shadows
    AIM["AI Models<br/>(Prisoners)"]
    IA["Internal Activations<br/>(Prisoners' Interpretations)"]
  end

  %% Flow of information
  TR -- "projects" --> DS
  DS -- "observed by" --> AIM
  AIM -- "generates" --> IA

  %% Hypothesis Note
  note right of IA
    Hypothesis: Internal Activations converge
    as models become more sophisticated,
    due to shared origin in True Reality.
  end

  %% Visual grouping
  classDef reality stroke-width:3px,stroke-dasharray: 5 5
  classDef shadows stroke-dasharray: 3 3
```
Image 1: A conceptual diagram illustrating Plato's Cave allegory adapted for AI and the Platonic representation hypothesis.

Not everyone is convinced. A key point of contention involves which representations to focus on and how to compare them across different models, especially concerning the choice of layers and similarity metrics. A consensus on the hypothesis is unlikely anytime soon. Still, this does not bother Isola, who said, "Half the community says this is obvious, and the other half says this is obviously wrong. We were happy with that response" [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)].

Having framed the hypothesis and its philosophical roots, let's explore the geometric mechanism that makes such comparisons possible by examining how representations are compared through the company their vectors keep.

## The Company Being Kept

If AI researchers do not agree on Plato, they might find more common ground with his predecessor Pythagoras, whose philosophy started from the premise "All is number." This is an apt description of the neural networks that power AI models. Their representations of words or pictures are just long lists of numbers, each indicating the activation of a specific artificial neuron. These representations are high-dimensional vectors. They are like arrows pointing in an abstract space that are impossible to visualize directly.

This geometric foundation provides a basis for comparison. Within a single AI model, similar inputs tend to have similar representations. The vector for "dog" will be close to vectors for "pet" and "furry" but far from "molasses." This reflects the principle expressed by linguist John Rupert Firth: "You shall know a word by the company it keeps" [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)]. The meaning of any concept inside a model is defined by its relationships—proximity, opposition, clustering—to all other concepts. We can therefore compare models by asking whether "dog" sits in the same relational neighborhood relative to "mammal," "animal," "pet," and "furniture" in both spaces.

But what about representations in different models? Directly comparing activation vectors from separate networks is ill-posed because their coordinate systems are incompatible. Instead, researchers use indirect methods. One popular approach is to measure whether two models' representations of an input keep the same company. Imagine comparing how two models represent animals. You would feed words like "dog," "cat," and "jellyfish" into both networks and record their vector representations. Then, you would compare the overall shapes of the two resulting vector clusters.

Ilia Sucholutsky, an AI researcher at New York University, described this process as "measuring the similarity of similarities" [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)]. You would expect some similarity; "cat" and "dog" vectors would likely be close in both models, while "jellyfish" would be farther away. But the clusters will not be identical. Is "dog" more like "cat" or "wolf"? Models trained on different datasets might not agree. This technique allows us to assign a scalar score indicating how much relational structure is preserved across models.

Early studies in the mid-2010s found that different models' representations were often similar but not identical [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)]. Notably, a few studies found that more powerful models had more similar representations than weaker ones. A 2021 paper dubbed this the "Anna Karenina scenario," a nod to the opening line of the novel. Perhaps all successful AI models are alike, while every unsuccessful model is unsuccessful in its own way [[9](https://aiscientist.substack.com/p/musing-38-the-platonic-representation)]. This pattern mirrors the hypothesis that there is a single "correct" structure for high-performing models to discover.

Much of this early work focused on computer vision, which was then the most popular branch of AI research. These studies typically compared different Convolutional Neural Network (CNN) architectures trained on datasets like ImageNet. However, the methods developed for vision models had inherent limitations when researchers tried to extend them to language models. The nature of text data and the architectures of early language models were different, and large-scale paired vision-language datasets were not yet available to bridge the gap. The rise of powerful language models and multimodal systems presented a new opportunity to see just how far representational similarity could go.

With these measurement tools in hand, we can now look at the hierarchy of experimental evidence showing that this convergence strengthens as models scale.

## Convergent Evolution

The story of the Platonic representation hypothesis paper began in early 2023, a turbulent time for AI researchers. ChatGPT had been released a few months prior, and it was clear that simply scaling up AI models made them better at many tasks. But it was unclear why. This created an existential question: when performance improves with scale, are models just memorizing more dataset quirks, or are they getting better at approximating a true underlying world model?

"Everyone in AI research was going through an existential life crisis," said Minyoung Huh, an OpenAI researcher who was a graduate student in Isola’s lab at the time. He began meeting with Isola and colleagues Brian Cheung and Tongzhou Wang to discuss how scaling might affect internal representations [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)].

To answer this, they considered a hierarchy of evidence for convergence. The weakest evidence would be if models trained on identical data converge. Stronger evidence would be if models trained on different data within the same modality still converge. The most striking evidence would be if models trained on entirely different data types, like vision and language, also converge.

A year after their initial conversations, Isola and his colleagues wrote a paper reviewing the evidence and presenting their argument for the hypothesis [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)]. By then, other researchers had already found evidence of alignment between vision and language model representations [[4](https://arxiv.org/html/2507.01201v5)].

Huh conducted his own experiment to test cross-modal convergence. He used a set of five vision models and 11 language models of varying sizes, testing them on a dataset of captioned pictures from Wikipedia. He would feed the pictures into the vision models and the captions into the language models, then compare the resulting vector clusters. He observed a steady increase in representational similarity as models became more powerful, exactly as the Platonic representation hypothesis predicted [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)].

After reviewing the evidence for convergence, we must examine the experimental choices related to measuring representational similarity that may affect the validity and generalizability of the results.

## Find the Universals

Of course, it is never so simple. Measurements of representational similarity involve a host of experimental choices that can affect the outcome. Which layers do you look at in each network? Which of the many similarity metrics do you use? And which representations do you measure in the first place? As Christopher Wolfram, a researcher at the University of Chicago, noted, "If you only test one dataset, you don’t necessarily know how [the result] generalizes. Who knows what would happen if you did some weirder dataset?" [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)], [[10](https://openreview.net/forum?id=8wKec6faAT)], [[11](https://www.preprints.org/manuscript/202601.1018)]. These similarities may reflect unavoidable structural constraints rather than meaningful convergence [[11](https://openreview.net/forum?id=8wKec6faAT)].

This debate highlights two complementary scientific attitudes. One, associated with Isola, actively seeks the universals that models appear to share. "The endeavor of science is to find the universals," he said. "We could study the ways in which models are different or disagree, but that somehow has less explanatory power than identifying the commonalities" [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)].

The other attitude, associated with Alexei Efros at the University of California, Berkeley (UC Berkeley), argues it is more productive to focus on where models' representations differ. "They’re all good friends and they’re all very, very smart people," Efros said of the MIT team. "I think they’re wrong, but that’s what science is about" [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)]. Efros noted that in the Wikipedia dataset Huh used, the images and text contained very similar information by design. However, most data we encounter has features that resist translation. "There is a reason why you go to an art museum instead of just reading the catalog," he remarked [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)].

Despite these debates, even partial alignment has immediate practical payoffs. Last summer, researchers used this property to translate internal representations of sentences from one language model to another [[12](https://arxiv.org/html/2505.12540v1)]. If language and vision model representations are somewhat interchangeable, it could lead to new ways to train models that learn from both data types, a possibility Isola and others explored in a recent paper [[13](https://arxiv.org/abs/2510.08492)]. The practical benefits also extend to real-world multimodal systems, where alignment can improve unimodal encoder performance, especially when redundant information exists across modalities [[5](https://arxiv.org/html/2511.12121v4)], [[6](https://www.emergentmind.com/topics/multimodal-alignment)], [[14](https://ojs.aaai.org/index.php/AAAI/article/view/39248/43209)], [[15](https://arxiv.org/html/2411.17040v1)], [[16](https://www.itm-conferences.org/articles/itmconf/pdf/2025/09/itmconf_cseit2025_04036.pdf)].

Still, some researchers think it is unlikely that a single theory will fully capture the behavior of modern AI models. "You can’t reduce a trillion-parameter system to simple explanations," said Jeff Clune, an AI researcher at the University of British Columbia. "The answers are going to be complicated" [[2](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)]. While the Platonic representation hypothesis offers a clean philosophical story, real models contain so many interacting parts that full convergence may coexist with vast regions of model-specific idiosyncrasy.

## References

- [1] [Layers at Similar Depths Generate Similar Activations Across LLM Architectures](https://arxiv.org/html/2504.08775v1)
- [2] [Distinct AI Models Seem To Converge On How They Encode Reality](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)
- [3] [The Platonic Representation Hypothesis](https://phillipi.github.io/prh)
- [4] [Escaping Plato’s Cave: JAM for Aligning Independently Trained Vision and Language Models](https://arxiv.org/html/2507.01201v5)
- [5] [To Align or Not to Align: Strategic Multimodal Representation Alignment for Optimal Performance](https://arxiv.org/html/2511.12121v4)
- [6] [multimodal-alignment](https://www.emergentmind.com/topics/multimodal-alignment)
- [7] [platonic-representation-hypothesis](https://www.emergentmind.com/topics/platonic-representation-hypothesis)
- [8] [The Cave Allegory Revisited: Understanding GPT's Worldview](https://www.alignmentforum.org/posts/kFCu3batN8k8mwtmh/the-cave-allegory-revisited-understanding-gpt-s-worldview)
- [9] [Musing 38: The Platonic Representation Hypothesis](https://aiscientist.substack.com/p/musing-38-the-platonic-representation)
- [10] [Review of "The Platonic Representation Hypothesis"](https://openreview.net/forum?id=8wKec6faAT)
- [11] [The Platonic Representation Hypothesis](https://www.preprints.org/manuscript/202601.1018)
- [12] [Harnessing the Universal Geometry of Embeddings](https://arxiv.org/html/2505.12540v1)
- [13] [Better Together: Leveraging Unpaired Multimodal Data for Stronger Unimodal Models](https://arxiv.org/abs/2510.08492)
- [14] [To Align or Not to Align: Strategic Multimodal Representation Alignment for Optimal Performance](https://ojs.aaai.org/index.php/AAAI/article/view/39248/43209)
- [15] [A Survey on Multimodal Alignment and Fusion: From a Feature and Instance Perspective](https://arxiv.org/html/2411.17040v1)
- [16] [Research on Multimodal Alignment and Fusion Technology Based on Large Models](https://www.itm-conferences.org/articles/itmconf/pdf/2025/09/itmconf_cseit2025_04036.pdf)
</article>