# The Platonic Ideal of AI: Are All Models Converging to the Same Reality?

Read a story about dogs, and you may remember it the next time you see one bounding through a park. This is only possible because you have a unified concept of "dog" that is not tied to words or images alone. Bulldog or border collie, barking or getting its belly rubbed, a dog can be many things while still remaining a dog.

Artificial intelligence systems are not always so lucky. These systems often learn from data of a single type. Text for language models, images for computer vision systems, and other exotic data for specialized tasks. This raises a fundamental question: to what extent do language and vision models have a shared understanding of a dog?

Researchers investigate such questions by peering inside AI systems and studying how they represent scenes and sentences. They have found that different AI models can develop similar representations, even if they are trained using different datasets or entirely different data types. What is more, studies have suggested that those representations grow more similar as models become more capable. In a paper from the Massachusetts Institute of Technology, four AI researchers argued that these hints of convergence are no fluke. Their idea, dubbed the Platonic representation hypothesis, has inspired a lively debate among researchers and a series of follow-up studies [[1], [2], [3], [4], [5], [6], [7]].

The team’s hypothesis gets its name from a 2,400-year-old allegory by the Greek philosopher Plato. In it, prisoners trapped inside a cave perceive the world only through shadows cast on a wall by objects outside. The prisoners mistake these two-dimensional projections for the entirety of reality, never knowing the true, three-dimensional forms that create them [[8]]. Plato maintained that we are all like those prisoners. The objects we encounter are pale shadows of ideal "forms" that reside in a transcendent realm beyond our senses [[8]]. This idea echoes through the history of science, from philosopher Hilary Putnam’s theory of “convergent realism,” which posits that scientific theories converge on truth, to modern arguments that some representation learning algorithms recover statistical models of the latent causes behind our observations [[9]].

The Platonic representation hypothesis is less abstract. In this version of the metaphor, the real world is what’s outside the cave, and it casts machine-readable shadows as streams of data. AI models are the prisoners. The MIT team’s claim is that very different models, exposed only to these data streams, are beginning to converge on a shared “Platonic representation” of the world behind the data [[1]]. As Phillip Isola, the senior author of the paper, puts it, "Why do the language model and the vision model align? Because they’re both shadows of the same world" [[10]].

Not everyone is convinced. One of the main points of contention involves which representations to focus on. You cannot inspect a language model’s internal representation of every sentence or a vision model’s representation of every image. So how do you decide which ones are representative? Where do you look for them, and how do you compare them across different models? It is unlikely that researchers will reach a consensus on the hypothesis anytime soon, but that does not bother Isola. "Half the community says this is obvious, and the other half says this is obviously wrong,” he said. “We were happy with that response" [[10]].

Having framed the Platonic representation hypothesis and its philosophical roots, we need to look at the precise geometric mechanism that makes such comparisons possible. We will start by examining how representations are compared through the company their vectors keep.

## The Company Being Kept

If AI researchers do not agree on Plato, they might find more common ground with his predecessor Pythagoras, whose philosophy supposedly started from the premise “All is number.” That is an apt description of the neural networks that power AI models. Their representations of words or pictures are just long lists of numbers, each indicating the degree of activation of a specific artificial neuron [[10]].

To simplify the math, researchers typically focus on a single layer of a neural network, which is like taking a snapshot of brain activity in a specific region at a specific moment. They write down the neuron activations in this layer as a geometric object called a vector, an arrow pointing in a particular direction in an abstract space. Modern AI models have thousands of neurons in each layer, so their representations are high-dimensional vectors that are impossible to visualize directly. But vectors make it easy to compare a network’s representations: two are similar if their vectors point in similar directions [[10]].

To make these comparisons rigorous, we need a formal language. A **representation** is a function that maps an input, like an image or a word, to a feature vector. A **kernel** characterizes how that representation measures similarity between any two inputs, typically using their inner product. Finally, a **kernel-alignment metric** measures the similarity between two kernels, telling us how similarly two different models structure their understanding of the world. Examples of these metrics include Centered Kernel Alignment (CKA) and Singular Vector Canonical Correlation Analysis (SVCCA) [[1]].

Within a single AI model, similar inputs tend to have similar representations. In a language model, the vector for “dog” will be close to vectors for “pet,” “bark,” and “furry,” and farther from “Platonic” and “molasses.” This is a modern interpretation of an idea expressed over 60 years ago by the British linguist John Rupert Firth: “You shall know a word by the company it keeps” [[10]]. This principle also applies to how neural networks handle information. For a neural network, a concept is defined by its relationships to other concepts, which can be measured by the proximity of their vector representations [[11]].

But what about representations in different models? It does not make sense to directly compare activation vectors from separate networks, as their internal coordinate systems are arbitrary. However, researchers have devised indirect ways to assess representational similarity. One popular approach embraces Firth's quote and measures whether two models’ representations of an input keep the same company [[10]].

Suppose you want to compare how two language models represent words for animals. You would feed a list of words—dog, cat, wolf, jellyfish—into both networks and record their representations. In each network, these representations form a cluster of vectors. You can then ask: how similar are the overall shapes of the two clusters? This technique measures the similarity of similarities. As AI researcher Ilia Sucholutsky said, "It can kind of be described as measuring the similarity of similarities" [[2], [10]]. More advanced techniques push this further, using graph-based methods to explicitly align not just the concepts (nodes) but also the higher-order relational geometries between them (edges), ensuring that structural dependencies are preserved across modalities [[12]].

In this example, you would expect some similarity. The “cat” vector would probably be close to the “dog” vector in both networks, and the “jellyfish” vector would point in a different direction. But the clusters probably will not look exactly the same. Is “dog” more like “cat” than “wolf,” or vice versa? If your models were trained on different datasets or have different architectures, they might not agree [[10]].

Researchers began exploring representational similarity with this approach in the mid-2010s and found that different models’ representations were often similar but not identical [[10]]. A few studies found that more powerful models seemed to have more similarities in their representations than weaker ones [[1]]. One 2021 paper dubbed this the “Anna Karenina scenario,” a nod to the opening line of Tolstoy's novel [[2]]. Perhaps successful AI models are all alike, and every unsuccessful model is unsuccessful in its own way [[2]].

That paper, like much of the early work, focused only on computer vision. The rise of powerful language models was an opportunity to see just how far representational similarity could go [[10]]. With these measurement tools in hand, we can now look at the hierarchy of experimental evidence showing that convergence strengthens as models scale.

## Convergent Evolution

The story of the Platonic representation hypothesis paper began in early 2023. ChatGPT had been released a few months before, and it was increasingly clear that simply scaling up AI models made them better at many tasks. But it was unclear why [[10]]. This trend continues, with recent research exploring new scaling laws specifically for multimodal systems [[13]].

“Everyone in AI research was going through an existential life crisis,” said Minyoung Huh, an OpenAI researcher who was a graduate student in Isola’s lab at the time. He began meeting regularly with Isola and their colleagues Brian Cheung and Tongzhou Wang to discuss how scaling might affect internal representations [[10]]. When performance improves with scale, are models simply memorizing more dataset quirks, or are they getting better at approximating a true underlying world model? One proposed driver is the “Contravariance Principle”: as models must solve more tasks, the space of viable internal representations shrinks, forcing them to converge [[9]].

The team outlined a hierarchy of evidence that would support the Platonic hypothesis, in increasing order of strength. First, if models trained on the same data converge, it is a weak sign, as they could just be learning the same dataset-specific patterns. A more compelling case would be if models trained on different datasets but the same modality still converge. This would suggest they are learning about the world, not just the data. The strongest evidence would come from convergence between models trained on entirely different data types, such as vision and language models [[10]].

A year after their initial conversations, Isola and his colleagues decided to write a paper reviewing the evidence and presenting their argument [[10]]. By then, other researchers had already found evidence of alignment between vision and language model representations [[14], [15], [16]]. Huh conducted his own experiment, testing five vision models and 11 language models of varying sizes on captioned pictures from Wikipedia. He would feed the pictures into the vision models and the captions into the language models, then compare the vector clusters. He observed a steady increase in representational similarity as models became more powerful, exactly what the Platonic representation hypothesis predicted [[10]].

This evidence seems compelling. However, we must examine a host of experimental choices regarding the measurements of representational similarity that may affect the validity and generalizability of the result.

## Find the Universals

Measurements of representational similarity involve a host of experimental choices that can affect the outcome. Which layers do you look at in each network? Once you have a cluster of vectors, which of the many available metrics do you use to compare them [[17], [18], [19]]? And which representations do you measure in the first place?

Christopher Wolfram, a researcher at the University of Chicago, has studied this problem and critiques the generalizability of results from a single dataset: “If you only test one dataset, you don’t necessarily know how [the result] generalizes. Who knows what would happen if you did some weirder dataset?” [[3], [10]]. The challenge lies in distinguishing arbitrary properties of representations from fundamental ones [[3]]. Indeed, convergence can be limited by many-to-many relationships between concepts, scalability issues, and modality-specific information that fails to generalize [[20]].

Isola acknowledged that the issue is far from settled, but he argues that cases where models do converge are more compelling than cases where they may not. “The endeavor of science is to find the universals,” Isola said. “We could study the ways in which models are different or disagree, but that somehow has less explanatory power than identifying the commonalities” [[10]].

Other researchers argue that it is more productive to focus on where models’ representations differ. Among them is Alexei Efros, a researcher at UC Berkeley. “They’re all good friends and they’re all very, very smart people,” Efros said of the MIT team. “I think they’re wrong, but that’s what science is about” [[10]]. Efros noted that in the Wikipedia dataset Huh used, the images and text contained very similar information by design. But much of the data we encounter has features that resist translation. “There is a reason why you go to an art museum instead of just reading the catalog,” he said [[10]]. This aligns with research seeking to isolate the "bimodal basis" supporting alignment from unimodal features unique to one data type [[21]].

Any intrinsic sameness across models does not have to be perfect to be useful. Even with only partial alignment, there are immediate practical payoffs. Last summer, researchers used this partial alignment to translate internal representations of sentences from one language model to another [[6]]. If language and vision representations are to some extent interchangeable, it could lead to new ways to train models that learn from both data types, a technique Isola and others explored in a recent paper [[5]]. This could allow for more efficient multimodal training and help build agentic systems, for instance, enabling a robot to ground a language command to a 3D point-cloud and manipulate a novel object [[22]].

Despite these promising developments, other researchers think it is unlikely that any single theory will fully capture the behavior of modern AI models. “You can’t reduce a trillion-parameter system to simple explanations,” said Jeff Clune, an AI researcher at the University of British Columbia. “The answers are going to be complicated” [[10]]. While the Platonic hypothesis offers a clean philosophical story, real models contain so many interacting parts that full convergence may coexist with vast regions of model-specific idiosyncrasy. This is captured by the Fractured Entangled Representation (FER) hypothesis, which suggests that even high-performing models can have messy, disorganized internals, like "spaghetti code," where concepts are redundantly represented and entangled in counterintuitive ways [[11]].

## References

- [1] https://arxiv.org/abs/2405.07987
- [2] https://arxiv.org/abs/2106.07682
- [3] https://arxiv.org/abs/2504.08775
- [4] https://arxiv.org/abs/2502.16282
- [5] https://arxiv.org/abs/2510.08492
- [6] https://arxiv.org/abs/2505.12540
- [7] https://arxiv.org/abs/2503.05283
- [8] https://en.wikipedia.org/wiki/Allegory_of_the_cave
- [9] https://phillipi.github.io/prh
- [10] https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107
- [11] https://arxiv.org/html/2505.11581v1
- [12] https://openaccess.thecvf.com/content/CVPR2026/papers/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.pdf
- [13] https://arxiv.org/html/2409.06754v4
- [14] https://arxiv.org/abs/2209.15162
- [15] https://arxiv.org/abs/2302.06555
- [16] https://arxiv.org/abs/2401.05224
- [17] https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full
- [18] https://arxiv.org/abs/1905.00414
- [19] https://arxiv.org/abs/2305.06329
- [20] https://arxiv.org/html/2401.13898v2
- [21] https://arxiv.org/html/2602.06218v2
- [22] https://arxiv.org/html/2411.05036v1
- [23] https://arxiv.org/abs/2310.13018
</article>