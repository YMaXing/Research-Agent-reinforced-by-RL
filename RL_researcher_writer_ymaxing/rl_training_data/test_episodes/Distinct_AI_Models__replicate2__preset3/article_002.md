# The Platonic Representation Hypothesis: Are All AI Models Secretly Alike?

When you read a story about dogs, you remember it the next time you see one in a park. This happens because you have a unified concept of "dog" that is not tied to words or images alone. A bulldog or a border collie, barking or getting its belly rubbed, can be many things while still being a dog.

As AI engineers, we know our systems are not always so lucky. They typically learn from data of a single type. For example, language models train on text, and computer vision systems train on images. This raises a fundamental question we have to tackle when building multimodal systems: to what extent do these specialized models have a shared understanding of the same concept, like a dog?

Researchers have been digging into this by peering inside AI systems and studying how they represent scenes and sentences. They have found that different models can develop similar internal representations, even if trained on different datasets or data types. Furthermore, some studies suggest these representations grow more similar as the models become more capable. This idea, known as the Platonic representation hypothesis, has sparked a lively debate, with a flurry of papers exploring its implications and limitations [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[2]](https://arxiv.org/abs/2310.13018), [[3]](https://phillipi.github.io/prh), [[4]](https://arxiv.org/abs/2106.07682), [[5]](https://arxiv.org/abs/2504.08775), [[6]](https://arxiv.org/abs/2505.12540), [[7]](https://arxiv.org/abs/2510.08492).

The hypothesis gets its name from Plato's 2,400-year-old Allegory of the Cave [[9]](https://en.wikipedia.org/wiki/Allegory_of_the_cave). In his story, prisoners trapped in a cave see only shadows cast on a wall and mistake them for reality. Plato argued that we are all like those prisoners, and the objects we see are just pale shadows of ideal "forms" in a transcendent reality.

The AI version of this allegory is more concrete. The real world is outside the cave, and it casts machine-readable shadows as streams of data [[10]](https://www.alignmentforum.org/posts/kFCu3batN8k8mwtmh/the-cave-allegory-revisited-understanding-gpt-s-worldview). Our AI models are the prisoners. The hypothesis claims that as these models get better, they converge on a shared "Platonic representation" of the world behind the data [[8]](https://arxiv.org/html/2507.01201v5). As Phillip Isola, a key researcher in this area, puts it, "Why do the language model and the vision model align? Because they’re both shadows of the same world" [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Of course, not everyone is on board. A major point of contention is how to even compare these representations. You cannot just inspect a model's internal state for every possible sentence or image. This leads to practical questions: Which representations do you choose? Where in the model do you look? And how do you compare them across completely different architectures? A consensus is unlikely anytime soon. "Half the community says this is obvious, and the other half says this is obviously wrong," Isola said. "We were happy with that response" [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Now that we have framed the hypothesis, let's look at the geometric tools that make these comparisons possible, by examining how representations are compared through the company their vectors keep.

## The Company Being Kept

If you are an engineer, you might appreciate the philosophy of Pythagoras, who supposedly said, “All is number.” This idea was later echoed by Gottfried Wilhelm von Leibniz, who imagined a system where all concepts could be broken down into elementary parts and assigned a unique number, turning philosophical debates into mathematical calculations [[11]](https://web.eecs.utk.edu/~bmaclenn/papers/HistoryAIBeforeComputers.pdf).

This is a perfect description of how neural networks operate. Their representations of words or pictures are just long lists of numbers, or vectors, indicating the activation of artificial neurons. To make sense of this, we usually look at the activations from a single layer. These activations form a high-dimensional vector, an arrow pointing in a specific direction in an abstract space. While we cannot visualize these spaces directly, we can compare representations by checking if their vectors point in similar directions.

Inside a single model, similar inputs produce similar representations. In a language model, the vector for “dog” will be close to vectors for “pet” and “furry,” but far from “Platonic” or “molasses.” This is a geometric take on a principle from the linguist John Rupert Firth: “You shall know a word by the company it keeps.” This idea of distributional semantics is not just for linguists. It is the foundation for how we compare representations across different systems, a technique known in neuroscience as Representational Similarity Analysis (RSA) [[2]](https://arxiv.org/abs/2310.13018).

But what about comparing representations in different models? You cannot directly compare activation vectors from separate networks. Instead, we use indirect methods. One popular approach is to take Firth’s principle literally and measure whether a concept keeps the same "company" in both models.

Suppose you want to compare how two language models represent animals. You would feed a list of words—dog, cat, wolf, jellyfish—into both and record their representations. In each model, these vectors form a cluster. The question then becomes: how similar are the overall shapes of these two clusters? It is not about matching coordinates but about matching the relational geometry. As AI researcher Ilia Sucholutsky put it, "It can kind of be described as measuring the similarity of similarities" [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107). These geometric models define similarity as a contrast between common and distinctive features, not just a simple distance [[12]](https://cogsci.ucsd.edu/~coulson/203/tvgati.pdf).

Researchers started exploring this in the mid-2010s and found that different models often had similar, though not identical, representations. A key finding was that more powerful models seemed to have more in common.

A 2021 paper called this the “Anna Karenina scenario,” referencing the novel's famous opening line [[4]](https://arxiv.org/abs/2106.07682). The idea is that all successful models are alike in their internal structure, while every unsuccessful model is unsuccessful in its own way. This suggests there is a single "correct" structure for models to find.

Much of this early work was focused on computer vision. When powerful language models emerged, it created an opportunity to see how far this similarity could go. However, extending these methods was not simple. Early attempts to translate word embeddings between languages often needed overlapping vocabularies, which does not work when comparing entire sentences or different modalities like text and images [[6]](https://arxiv.org/abs/2505.12540). This pushed the field toward more sophisticated, geometry-based techniques that could work without direct one-to-one mappings.

With these measurement tools in hand, we can now look at the hierarchy of experimental evidence showing that convergence strengthens as models scale.

## Convergent Evolution

The story of the Platonic representation hypothesis paper began in early 2023. ChatGPT had been out for a few months, and it was clear that scaling up AI models made them better at many tasks. But why? Were they just memorizing more data, or were they building a better model of the world? One theory is that simplicity bias plays a role. Deep networks tend to find simple solutions, and this bias gets stronger as they get bigger, pushing them toward a shared, compact solution space [[13]](https://3dvar.com/Huh2024The.pdf).

“Everyone in AI research was going through an existential life crisis,” said Minyoung Huh, an OpenAI researcher who was a graduate student in Isola’s lab at the time. He started meeting with Isola and their colleagues Brian Cheung and Tongzhou Wang to discuss how scaling might affect internal representations [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

The team laid out a hierarchy of evidence. If models trained on the same data converge, it could just be that they are good at picking up the same dataset quirks. More compelling evidence would be if models trained on different datasets also converge. The strongest evidence, however, would be convergence between models trained on entirely different data types, like vision and language models.

A year later, Isola and his colleagues published a paper reviewing the evidence and making their case for the hypothesis [[3]](https://phillipi.github.io/prh). By then, other researchers had already found signs of alignment between vision and language models.

Huh ran his own experiment, testing vision and language models of different sizes on a dataset of captioned pictures. He fed the images to the vision models and the captions to the language models, then compared the resulting vector clusters. He found a steady increase in similarity as the models became more powerful, which was exactly what the Platonic representation hypothesis predicted [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

After reviewing the evidence for convergence, we must examine the experimental choices that could affect the validity of these results.

## Find the Universals

Of course, things are never that simple. Measuring representational similarity depends on many experimental choices. Which layers do you compare? Which similarity metric do you use? And what data do you test on? Newer metrics like topological representation alignment, which focus on preserving local neighborhood geometry, are being developed to address some of these challenges [[14]](https://arxiv.org/html/2502.18710v3).

“If you only test one dataset, you don’t necessarily know how [the result] generalizes,” said researcher Christopher Wolfram. “Who knows what would happen if you did some weirder dataset?” [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[5]](https://arxiv.org/abs/2504.08775).

Isola acknowledges the issue is not settled. For him, the cases where models do converge are more interesting than the cases where they do not. “The work of science is to find the universals,” he said. “We could study the ways in which models are different or disagree, but that somehow has less explanatory power than identifying the commonalities” [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Other researchers believe it is more useful to focus on where models differ. One of them is Alexei Efros, a researcher at UC Berkeley. “They’re all good friends and they’re all very, very smart people,” Efros said. “I think they’re wrong, but that’s what science is about” [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107). He pointed out that in Huh’s experiment, the images and text were designed to contain similar information. But in the real world, data often has features that do not translate easily across modalities, a known challenge in multimodal fusion where models can struggle with non-overlapping information [[15]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11926988). “There is a reason why you go to an art museum instead of just reading the catalog,” he said.

Even if the alignment is not perfect, it can still be useful. There are practical benefits to even partial alignment. Researchers have developed methods to translate internal representations from one language model to another [[6]](https://arxiv.org/abs/2505.12540). If language and vision representations are somewhat interchangeable, it could lead to better ways to train models that learn from both data types [[7]](https://arxiv.org/abs/2510.08492). Still, there are open questions about how to make these partially aligned systems robust and scalable, especially for complex agentic systems [[16]](https://www.mdpi.com/1424-8220/26/8/2330).

Ultimately, some researchers think it is unlikely that a single theory will fully explain modern AI. As AI researcher Jeff Clune said, “You can’t reduce a trillion-parameter system to simple explanations... The answers are going to be complicated” [[1]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107). This gets to the core of the issue: while the hypothesis provides a clean story, real models may be too complex for such elegant explanations. Convergence might be happening, but it could be coexisting with large areas of model-specific behavior.

## Conclusion

The Platonic representation hypothesis suggests that as AI models grow more capable, their internal representations are converging toward a shared statistical model of reality. Evidence from cross-modal experiments shows that this alignment strengthens with model scale, hinting at a universal structure that transcends specific architectures and data types.

While the debate continues, with valid critiques questioning the methodology and scope of these findings, the practical implications are already emerging. For AI engineers, this convergence is not just a philosophical curiosity. It underpins the potential for more robust multimodal systems, enabling seamless translation of representations and more efficient joint training. Understanding this shared "world model" is becoming essential for building the next generation of integrated and agentic AI.

## References

- [1] [Distinct AI Models Seem To Converge On How They Encode Reality](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107)
- [2] [GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT](https://arxiv.org/abs/2310.13018)
- [3] [The Platonic Representation Hypothesis](https://phillipi.github.io/prh)
- [4] [Revisiting Model Stitching to Compare Neural Representations](https://arxiv.org/abs/2106.07682)
- [5] [Layers at Similar Depths Generate Similar Activations Across LLM Architectures](https://arxiv.org/abs/2504.08775)
- [6] [Harnessing the Universal Geometry of Embeddings](https://arxiv.org/abs/2505.12540)
- [7] [Better Together: Leveraging Unpaired Multimodal Data for Stronger Unimodal Models](https://arxiv.org/abs/2510.08492)
- [8] [Escaping Plato’s Cave: JAM for Aligning Independently Trained Vision and Language Models](https://arxiv.org/html/2507.01201v5)
- [9] [Allegory of the cave - Wikipedia](https://en.wikipedia.org/wiki/Allegory_of_the_cave)
- [10] [The Cave Allegory Revisited: Understanding GPT's Worldview](https://www.alignmentforum.org/posts/kFCu3batN8k8mwtmh/the-cave-allegory-revisited-understanding-gpt-s-worldview)
- [11] [A History of AI Before Computers](https://web.eecs.utk.edu/~bmaclenn/papers/HistoryAIBeforeComputers.pdf)
- [12] [Features of Similarity](https://cogsci.ucsd.edu/~coulson/203/tvgati.pdf)
- [13] [The Platonic Representation Hypothesis](https://3dvar.com/Huh2024The.pdf)
- [14] [Topological Alignment of Cross-Modal Representations](https://arxiv.org/html/2502.18710v3)
- [15] [A Review of Multimodal Data Fusion in Cancer: Methods, Challenges, and Future Directions](https://pmc.ncbi.nlm.nih.gov/articles/PMC11926988)
- [16] [A Comprehensive Survey of Recent Advancements in Vision-Language Pre-Training](https://www.mdpi.com/1424-8220/26/8/2330)
</article>