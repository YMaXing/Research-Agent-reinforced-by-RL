# The Platonic Representation Hypothesis: Are All AI Models Converging?

If you read a story about a dog, you might remember it the next time you see one bounding through a park. This is possible because you have a unified concept of "dog" that is not tied to words or images alone. Whether it is a bulldog or a border collie, whether you hear it barking or see it getting its belly rubbed, a dog remains a dog.

AI systems are not always so lucky. These systems learn by ingesting vast amounts of data in a process called training. Often, that data is of a single type. For example, text for language models, images for computer vision systems, or more exotic data for systems designed to predict the smell of molecules. This raises a fundamental question: to what extent do language and vision models have a shared understanding of a dog?

Researchers investigate such questions by peering inside AI systems and studying how they represent scenes and sentences. A growing body of work has found that different AI models can develop similar internal representations, even if they are trained on different datasets or entirely different data types [[1]](https://arxiv.org/abs/2310.13018). Furthermore, a few studies have suggested that these representations grow more similar as the models become more capable [[2]](https://arxiv.org/abs/2405.07987). In a 2024 paper, four AI researchers at the Massachusetts Institute of Technology argued that these hints of convergence are no fluke. Their idea, dubbed the Platonic representation hypothesis, has inspired a lively debate and a series of follow-up papers [[3]](https://arxiv.org/abs/2502.16282), [[4]](https://arxiv.org/abs/2503.05283), [[5]](https://arxiv.org/abs/2512.03750), [[6]](https://arxiv.org/abs/2511.02767).

The hypothesis gets its name from a 2,400-year-old allegory by the Greek philosopher Plato. In it, prisoners trapped inside a cave perceive the world only through shadows cast by outside objects. Plato maintained that we are all like those prisoners. The objects we encounter are merely pale shadows of ideal "forms" that exist in a transcendent realm. The Platonic representation hypothesis adapts this for AI. In this version, the real world is outside the cave, casting machine-readable shadows as streams of data. AI models are the prisoners. The MIT team’s claim is that very different models, exposed only to these data streams, are beginning to converge on a shared “Platonic representation” of the world behind the data [[2]](https://arxiv.org/abs/2405.07987).

This idea is also related to the concept of “convergent realism” from the philosophy of science, which posits that scientific theories are progressively converging on a true description of reality [[7]](https://3dvar.com/Huh2024The.pdf).

One of the main points of contention involves which representations to focus on. You cannot inspect a language model’s internal representation of every sentence or a vision model’s representation of every image. This makes it difficult to decide which ones are truly representative. Where do you look for the representations, and how do you compare them across different models? It is unlikely that researchers will reach a consensus on the Platonic representation hypothesis anytime soon. Phillip Isola, the senior author of the paper, is not bothered by this. “Half the community says this is obvious, and the other half says this is obviously wrong,” he said. “We were happy with that response” [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Having framed the hypothesis and its philosophical roots, we can now examine the precise geometric mechanism that makes such comparisons possible, by looking at the company their vectors keep.

## The Company Being Kept

If AI researchers do not agree on Plato, they might find more common ground with his predecessor Pythagoras, whose philosophy supposedly started from the premise “All is number.” This is an apt description of the neural networks that power AI models. Their representations of words or pictures are just long lists of numbers, each indicating the activation level of a specific artificial neuron [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

To simplify the math, researchers typically focus on a single layer of a neural network in isolation. They write down the neuron activations in this layer as a geometric object called a vector, an arrow pointing in a particular direction in an abstract space. Modern AI models have thousands of neurons in each layer, so their representations are high-dimensional vectors that are impossible to visualize directly. However, vectors make it easy to compare a network’s representations. Two representations are similar if their corresponding vectors point in similar directions [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Within a single AI model, similar inputs tend to have similar representations. In a language model, the vector for "dog" will be relatively close to vectors for "pet," "bark," and "furry," and farther from "Platonic" and "molasses." This reflects a principle expressed over 60 years ago by the British linguist John Rupert Firth: “You shall know a word by the company it keeps” [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

But what about representations in different models? It does not make sense to directly compare activation vectors from separate networks. Instead, researchers have devised indirect ways to assess representational similarity. A popular approach is to measure whether two models’ representations of an input keep the same company [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[9]](https://www.emergentmind.com/topics/representational-similarity-analysis-rsa). Imagine you want to compare how two language models represent words for animals. You compile a list of words—dog, cat, wolf, jellyfish—and feed them into both networks. In each network, the representations will form a cluster of vectors. You can then ask how similar the overall shapes of the two clusters are. “It can kind of be described as measuring the similarity of similarities,” said Ilia Sucholutsky, an AI researcher at New York University [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

In this example, you would expect some similarity. The "cat" vector would likely be close to the "dog" vector in both networks, and the "jellyfish" vector would point in a different direction. However, the clusters probably will not look identical. If your models were trained on different datasets or have different architectures, they might not agree on whether "dog" is more like "cat" or "wolf" [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Researchers began studying representational similarity in the mid-2010s and found that different models' representations were often similar, though not identical [[10]](https://arxiv.org/abs/1511.07543). Intriguingly, some studies found that more powerful models had more similarities in their representations. One 2021 paper dubbed this the "Anna Karenina scenario," a nod to the opening line of the novel [[11]](https://arxiv.org/abs/2106.07682). Perhaps successful AI models are all alike, and every unsuccessful model is unsuccessful in its own way.

That paper, like much of the early work, focused only on computer vision. The rise of powerful language models presented an opportunity to see just how far representational similarity could go. With these measurement tools in hand, we can now look at the hierarchy of experimental evidence showing that convergence strengthens as models scale.

## Convergent Evolution

The section’s title is a direct analogy to a concept from evolutionary biology. In biology, convergent evolution describes how unrelated species independently evolve similar traits to solve similar problems—like wings in birds, bats, and insects. The argument, extended to AI, is that when highly dissimilar systems like a biological brain and a silicon neural network arrive at similar representational strategies, it suggests those strategies are effective, perhaps even necessary, solutions for processing information about the world [[12]](https://www.pnas.org/doi/10.1073/pnas.2319709121).

The story of the Platonic representation hypothesis paper began in early 2023. ChatGPT had been released a few months prior, and it was increasingly clear that simply scaling up AI models made them better at many tasks. But it was unclear why. “Everyone in AI research was going through an existential life crisis,” said Minyoung Huh, an OpenAI researcher who was a graduate student in Isola’s lab at the time [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107). He began meeting with Isola and their colleagues to discuss how scaling might affect internal representations.

If multiple models trained on the same data learn more similar representations as they get stronger, it is not necessarily because they are creating a more accurate likeness of the world. They could just be getting better at grasping quirks of the training data. However, if their representations also converge when trained on different datasets, that would be more compelling evidence that models are grasping shared features of the world. Convergence between models that learned from entirely different data types, such as language and vision models, would provide even stronger evidence [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

A year after their initial conversations, Isola and his colleagues wrote a paper reviewing the evidence for convergent representations and arguing for the Platonic representation hypothesis [[2]](https://arxiv.org/abs/2405.07987). By then, other researchers had already found similarities between vision and language model representations [[13]](https://arxiv.org/abs/2209.15162), [[14]](https://arxiv.org/abs/2302.06555), [[15]](https://arxiv.org/abs/2401.05224). Huh conducted his own experiment, testing five vision models and 11 language models on a dataset of captioned pictures from Wikipedia. He fed the pictures into the vision models and the captions into the language models, then compared the vector clusters. He observed a steady increase in representational similarity as models became more powerful, exactly as the hypothesis predicted [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

After reviewing the evidence for convergence, we must examine the host of experimental choices that can affect the validity and generalizability of the results.

## Find the Universals

Of course, it is never so simple. Measurements of representational similarity involve a host of experimental choices that can affect the outcome. Which layers do you look at in each network? Which of the many available metrics do you use to compare the vector clusters [[16]](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full), [[17]](https://arxiv.org/abs/1905.00414), [[18]](https://arxiv.org/abs/2305.06329)? And which representations do you measure in the first place?

“If you only test one dataset, you don’t necessarily know how [the result] generalizes,” said Christopher Wolfram, a researcher at the University of Chicago who has studied these issues [[19]](https://arxiv.org/abs/2504.08775). “Who knows what would happen if you did some weirder dataset?” Isola acknowledged that the issue is far from settled, but to him, cases where models exhibit convergence are more compelling than cases where they may not. “The endeavor of science is to find the universals,” Isola said. “We could study the ways in which models are different or disagree, but that somehow has less explanatory power than identifying the commonalities” [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

This search for universals is not unique to vision and language. In physics-informed AI, models that incorporate physical laws as constraints also converge more reliably, suggesting that grounding representations in external, objective truths is a general principle for building more robust systems [[20]](https://arxiv.org/html/2506.13777v1).

Other researchers argue that it is more productive to focus on where models’ representations differ. Among them is Alexei Efros, a researcher at the University of California, Berkeley. “They’re all good friends and they’re all very, very smart people,” Efros said of the MIT team. “I think they’re wrong, but that’s what science is about” [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107). Efros noted that in the Wikipedia dataset Huh used, the images and text contained very similar information by design. However, most data we encounter in the world has features that resist translation. “There is a reason why you go to an art museum instead of just reading the catalog,” he said [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Any intrinsic sameness across models does not have to be perfect to be useful. In 2025, researchers showed it was possible to translate internal representations of sentences from one language model to another [[21]](http://arxiv.org/abs/2505.12540). If language and vision model representations are to some extent interchangeable, that could lead to new ways to train models that learn from both data types, a possibility Isola and others explored in a recent paper [[22]](https://arxiv.org/abs/2510.08492). This principle is already being applied in robotics, where fusing data from cameras, LiDAR, and radar into a unified representation is essential for robust navigation [[23]](https://www.emergentmind.com/topics/multi-modal-sensor-fusion). Future work may extend this to more complex agentic reasoning by developing neuro-symbolic architectures that leverage this cross-modal understanding [[24]](https://arxiv.org/html/2407.08516v5).

Despite these promising developments, some researchers think it is unlikely that any single theory will fully capture the behavior of modern AI models. “You can’t reduce a trillion-parameter system to simple explanations,” said Jeff Clune, an AI researcher at the University of British Columbia. “The answers are going to be complicated” [[8]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

The hypothesis continues to be tested and refined. For instance, the UReason benchmark (Yang et al., 2026) was developed to diagnose cross-modal alignment in models that generate images from textual reasoning. Their findings suggest a gap: a model’s textual reasoning about an image does not always align with the final pixels it generates, indicating that shared representations might be fragile [[25]](https://arxiv.org/html/2602.08336v2). Other new benchmarks are also emerging to probe alignment in different domains, from image editing with KRIS-Bench to genomics with the GENEB benchmark, which tests representations from dozens of genomic foundation models [[25]](https://arxiv.org/html/2602.08336v2), [[26]](https://rewire.it/blog/genomic-foundation-models-in-2026).

This tension between elegant Platonic explanations and irreducible complexity highlights that while the hypothesis offers a clean philosophical story, real models may contain vast regions of model-specific idiosyncrasy alongside any convergent structures. The debate continues, fueled by new architectures and ever-larger datasets, pushing the boundaries of how we understand intelligence, both artificial and our own.

## References

- [1] https://arxiv.org/abs/2310.13018
- [2] https://arxiv.org/abs/2405.07987
- [3] https://arxiv.org/abs/2502.16282
- [4] https://arxiv.org/abs/2503.05283
- [5] https://arxiv.org/abs/2512.03750
- [6] https://arxiv.org/abs/2511.02767
- [7] https://3dvar.com/Huh2024The.pdf
- [8] https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107
- [9] https://www.emergentmind.com/topics/representational-similarity-analysis-rsa
- [10] https://arxiv.org/abs/1511.07543
- [11] https://arxiv.org/abs/2106.07682
- [12] https://www.pnas.org/doi/10.1073/pnas.2319709121
- [13] https://arxiv.org/abs/2209.15162
- [14] https://arxiv.org/abs/2302.06555
- [15] https://arxiv.org/abs/2401.05224
- [16] https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full
- [17] https://arxiv.org/abs/1905.00414
- [18] https://arxiv.org/abs/2305.06329
- [19] https://arxiv.org/abs/2504.08775
- [20] https://arxiv.org/html/2506.13777v1
- [21] http://arxiv.org/abs/2505.12540
- [22] https://arxiv.org/abs/2510.08492
- [23] https://www.emergentmind.com/topics/multi-modal-sensor-fusion
- [24] https://arxiv.org/html/2407.08516v5
- [25] https://arxiv.org/html/2602.08336v2
- [26] https://rewire.it/blog/genomic-foundation-models-in-2026