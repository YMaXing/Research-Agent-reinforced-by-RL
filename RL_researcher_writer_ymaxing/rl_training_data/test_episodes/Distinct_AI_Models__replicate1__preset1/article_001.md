# The Platonic Representation Hypothesis: Are All AI Models Converging?

When you read a story about a dog, you remember it the next time you see one in a park. This is possible because you have a unified concept of "dog" that is not tied to words or images alone. Bulldog or border collie, barking or sleeping, a dog is a dog.

AI systems are not always so lucky. They often learn from data of a single type. Text for language models, images for computer vision systems. So, to what extent do a language model and a vision model have a shared understanding of a dog?

Researchers investigate such questions by peering inside AI systems and studying how they represent scenes and sentences. They have found that different AI models can develop similar internal representations, even if trained on different datasets or entirely different data types. What is more, several studies have suggested that these representations grow more similar as models become more capable. In a 2024 paper, four AI researchers at MIT argued that these hints of convergence are no fluke. Their idea, dubbed the Platonic representation hypothesis, has since inspired a lively debate and a series of follow-up studies [[1]](https://arxiv.org/abs/2310.13018), [[2]](https://arxiv.org/abs/2405.07987), [[3]](https://arxiv.org/abs/2502.16282), [[4]](https://arxiv.org/abs/2503.05283), [[5]](https://arxiv.org/abs/2512.03750), [[6]](https://arxiv.org/abs/2511.02767).

The hypothesis gets its name from Plato's 2,400-year-old allegory of the cave. In it, prisoners trapped inside a cave perceive the world only through shadows cast on a wall. Plato argued that we are all like those prisoners, and the objects we encounter are just pale shadows of ideal "forms" that exist in a transcendent realm.

The Platonic representation hypothesis is less abstract. In this version of the metaphor, the real world is outside the cave, casting machine-readable shadows as streams of data. The AI models are the prisoners. The MIT team claims that very different models, exposed only to these data streams, are beginning to converge on a shared "Platonic representation" of the world behind the data. As Phillip Isola, the senior author of the paper, puts it: "Why do the language model and the vision model align? Because they’re both shadows of the same world". This idea is related to the notion of "convergent realism" from the philosophy of science, which posits that scientific theories are progressively converging on a true description of reality [[2]](https://arxiv.org/abs/2405.07987), [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Not everyone is convinced. A key point of contention involves which representations to focus on. You cannot inspect a model’s internal state for every possible sentence or image. How do you decide which ones are representative? Where do you look for the representations, and how do you compare them across different models? A consensus is unlikely to arrive soon, but that does not bother Isola.

"Half the community says this is obvious, and the other half says this is obviously wrong," he said. "We were happy with that response" [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Having framed the hypothesis and its philosophical roots, we will now look at the precise geometric mechanism that makes such comparisons possible.

## The Company Being Kept

If AI researchers do not agree on Plato, they might find common ground with his predecessor Pythagoras, whose philosophy supposedly started from the premise "All is number." That is an apt description of neural networks. Their representations of words or pictures are just long lists of numbers, each indicating the activation of a specific artificial neuron [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Researchers typically focus on a single layer of a neural network, writing down the neuron activations as a geometric object called a vector. This is an arrow pointing in a particular direction in an abstract, high-dimensional space that is impossible to visualize directly. But vectors make it easy to compare a network’s representations: two are similar if their vectors point in similar directions.

Within a single model, similar inputs tend to have similar representations. In a language model, the vector for "dog" will be close to vectors for "pet," "bark," and "furry," and farther from "Platonic" and "molasses." This is an idea memorably expressed over 60 years ago by the British linguist John Rupert Firth: "You shall know a word by the company it keeps" [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

What about representations in different models? It does not make sense to directly compare activation vectors from separate networks. Instead, researchers have devised indirect ways to assess similarity. One popular approach embraces Firth's quote and measures whether two models’ representations of an input keep the same company.

Suppose you want to compare how two language models represent animals. First, you compile a list of words. For example, dog, cat, wolf, jellyfish, and so on. You then feed these words into both networks and record their representations. In each network, these representations form a cluster of vectors. You can then ask: how similar are the overall shapes of the two clusters?

“It can kind of be described as measuring the similarity of similarities,” said Ilia Sucholutsky, an AI researcher at New York University [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

However, these geometric comparisons face challenges in the high-dimensional spaces where representations live. Due to the "curse of dimensionality," distances can become less meaningful, and popular metrics like cosine similarity can saturate, failing to distinguish between genuinely different representations. The choice of similarity measure is therefore not trivial, as each has different conditions under which it performs reliably [[9]](https://khoury.northeastern.edu/home/pandey/courses/cs7800/spring26/papers/sshds.pdf), [[10]](https://arxiv.org/html/2407.08623v4), [[11]](https://arxiv.org/html/2602.05266v1).

In this example, you would expect some similarity. The "cat" vector would probably be close to the "dog" vector in both networks, while the "jellyfish" vector would point in a different direction. But the clusters probably will not look identical. Is "dog" more like "cat" than "wolf," or vice versa? If your models were trained on different datasets or have different architectures, they might not agree.

Researchers began exploring representational similarity in the mid-2010s and found that different models’ representations were often similar, though not identical. A few studies found that more powerful models seemed to have more similarities than weaker ones. One 2021 paper dubbed this the "Anna Karenina scenario," a nod to the opening line of the novel. Perhaps successful AI models are all alike, and every unsuccessful model is unsuccessful in its own way [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[8]](https://arxiv.org/abs/2106.07682).

That paper, like much of the early work on representational similarity, focused only on computer vision. The rise of powerful language models was an opportunity to see just how far this similarity could go. With these measurement tools in hand, we can now look at the hierarchy of experimental evidence showing that convergence strengthens as models scale.

## Convergent Evolution

The story of the Platonic representation hypothesis paper began in early 2023. ChatGPT had been released a few months before, and it was increasingly clear that simply scaling up AI models made them better at many different tasks. But it was unclear why. This rapid, unexplained progress led to a period of intense reflection within the AI community.

“Everyone in AI research was going through an existential life crisis,” said Minyoung Huh, an OpenAI researcher who was a graduate student in Isola’s lab at the time. He began meeting regularly with Isola and their colleagues Brian Cheung and Tongzhou Wang to discuss how scaling might affect internal representations [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Imagine multiple models trained on the same data, where stronger models learn more similar representations. This does not necessarily mean they are creating a more accurate likeness of the world. They could just be better at grasping quirks of the training dataset.

Now consider models trained on different datasets. If their representations also converge, that would be more compelling evidence that models are getting better at grasping shared features of the world behind the data. Convergence between models that learned from entirely different data types, such as language and vision models, would provide even stronger evidence. This mirrors findings in neuroscience, where researchers have recovered intrinsic, modality-independent "Platonic forms" of neuronal identity from brain activity [[15]](https://www.emergentmind.com/topics/platonic-representation-hypothesis).

A year after their initial conversations, Isola and his colleagues decided to write a paper reviewing the evidence for convergent representations and arguing for the Platonic representation hypothesis [[2]](https://arxiv.org/abs/2405.07987).

By then, other researchers had already found evidence of alignment between vision and language model representations. Huh conducted his own experiment, testing five vision models and 11 language models on a dataset of captioned pictures from Wikipedia. He fed the pictures into the vision models and the captions into the language models, then compared the vector clusters. He observed a steady increase in representational similarity as models became more powerful, exactly what the Platonic representation hypothesis predicted [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[12]](https://arxiv.org/abs/2209.15162), [[13]](https://arxiv.org/abs/2302.06555), [[14]](https://arxiv.org/abs/2401.05224).

After reviewing the evidence for convergence, we must examine a host of experimental choices with respect to the measurements of representational similarity that may affect the validity and generalizability of the result.

## Find the Universals

Measurements of representational similarity involve a host of experimental choices that can affect the outcome. Which layers do you look at? Which of the many similarity metrics do you use? And which representations do you measure in the first place?

“If you only test one dataset, you don’t necessarily know how [the result] generalizes,” said Christopher Wolfram, a researcher at the University of Chicago. “Who knows what would happen if you did some weirder dataset?”. Wolfram also critiques that observed similarities might just reflect "unavoidable structural constraints rather than meaningful representational convergence" [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[16]](https://arxiv.org/abs/2504.08775).

Isola acknowledged that the issue is far from settled. To him, cases where models do converge are more compelling than cases where they may not. “The endeavor of science is to find the universals,” Isola said. “We could study the ways in which models are different or disagree, but that somehow has less explanatory power than identifying the commonalities”. This search is not isolated to language and vision. In materials science, for instance, researchers have found that as physics-based AI models scale, their internal representations converge on a compatible geometric organization—another kind of Platonic representation emerging from physical constraints [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107), [[17]](https://www.nature.com/articles/s42256-026-01235-7).

Other researchers, like Alexei Efros at UC Berkeley, argue that it is more productive to focus on where models’ representations differ. “They’re all good friends and they’re all very, very smart people,” Efros said of the MIT team. “I think they’re wrong, but that’s what science is about.”

He noted that in Huh's Wikipedia dataset, the images and text contained very similar information by design. But most data we encounter has features that resist translation. “There is a reason why you go to an art museum instead of just reading the catalog,” he said [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

Any intrinsic sameness across models does not have to be perfect to be useful. Researchers have used this to translate internal representations of sentences from one language model to another. If language and vision model representations are somewhat interchangeable, that could lead to new ways to train models that learn from both data types, a possibility Isola and others explored in a recent paper. This principle is already being applied in robotics, where shared representations allow a single control policy to operate different robots, improving manipulation success rates and enabling skills to transfer across embodiments [[18]](https://arxiv.org/abs/2505.12540), [[19]](https://arxiv.org/abs/2510.08492), [[20]](https://arxiv.org/html/2506.14608v3), [[21]](https://www.emergentmind.com/topics/cross-embodiment-robot-data).

Despite these promising developments, some researchers think it is unlikely that a single theory will fully capture the behavior of modern AI. “You can’t reduce a trillion-parameter system to simple explanations,” said Jeff Clune, an AI researcher at the University of British Columbia. “The answers are going to be complicated” [[7]](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107).

## Conclusion

The Platonic Representation Hypothesis offers a compelling framework for understanding the internal workings of AI models. It suggests that despite their differences in architecture, training data, and even modality, powerful models are converging on a shared statistical model of reality. This convergence is not just a philosophical curiosity; it has practical implications for building more robust and interoperable AI systems.

As engineers, understanding this convergence helps us build better multimodal systems. It means we might not have to treat every model as a completely isolated black box. Instead, we can start to see them as different windows into the same underlying world, enabling us to translate representations, transfer knowledge, and build more unified AI agents. While the debate continues and the full picture is far from complete, the evidence for a shared "Platonic" reality within our models is a powerful idea that is already shaping the future of AI engineering.

## References

- [1]  https://arxiv.org/abs/2310.13018
- [2]  https://arxiv.org/abs/2405.07987
- [3]  https://arxiv.org/abs/2502.16282
- [4]  https://arxiv.org/abs/2503.05283
- [5]  https://arxiv.org/abs/2512.03750
- [6]  https://arxiv.org/abs/2511.02767
- [7]  https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107
- [8]  https://arxiv.org/abs/2106.07682
- [9]  https://khoury.northeastern.edu/home/pandey/courses/cs7800/spring26/papers/sshds.pdf
- [10]  https://arxiv.org/html/2407.08623v4
- [11]  https://arxiv.org/html/2602.05266v1
- [12]  https://arxiv.org/abs/2209.15162
- [13]  https://arxiv.org/abs/2302.06555
- [14]  https://arxiv.org/abs/2401.05224
- [15]  https://www.emergentmind.com/topics/platonic-representation-hypothesis
- [16]  https://arxiv.org/abs/2504.08775
- [17]  https://www.nature.com/articles/s42256-026-01235-7
- [18]  https://arxiv.org/abs/2505.12540
- [19]  https://arxiv.org/abs/2510.08492
- [20]  https://arxiv.org/html/2506.14608v3
- [21]  https://www.emergentmind.com/topics/cross-embodiment-robot-data

</article>