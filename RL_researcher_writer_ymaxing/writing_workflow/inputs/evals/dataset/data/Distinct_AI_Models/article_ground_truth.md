# Distinct AI Models Seem To Converge On How They Encode Reality

Read a story about dogs, and you may remember it the next time you see one bounding through a park. That’s only possible because you have a unified concept of “dog” that isn’t tied to words or images alone. Bulldog or border collie, barking or getting its belly rubbed, a dog can be many things while still remaining a dog.

Artificial intelligence systems aren’t always so lucky. These systems learn by ingesting [vast troves of data](https://www.quantamagazine.org/how-can-ai-id-a-cat-an-illustrated-guide-20250430/) in a process called training. Often, that data is all of the same type — text for language models, images for computer vision systems, and more exotic kinds of data for systems designed to predict the [odor of molecules](https://www.quantamagazine.org/ai-model-links-smell-molecules-with-metabolic-processes-20221010/) or the [structure of proteins](https://www.quantamagazine.org/how-ai-revolutionized-protein-science-but-didnt-end-it-20240626/). So to what extent do language models and vision models have a shared understanding of dogs?

Researchers investigate such questions by peering inside AI systems and studying how they represent scenes and sentences. A [growing body of research (opens a new tab)](http://arxiv.org/abs/2310.13018) has found that different AI models can develop similar representations, even if they’re trained using different datasets or entirely different data types. What’s more, a few studies have suggested that those representations are growing more similar as models grow more capable. In a [2024 paper (opens a new tab)](https://arxiv.org/abs/2405.07987), four AI researchers at the Massachusetts Institute of Technology argued that these hints of convergence are no fluke. Their idea, dubbed the Platonic representation hypothesis, has inspired a lively debate among researchers and a [slew (opens a new tab)](http://arxiv.org/abs/2502.16282) [of (opens a new tab)](https://arxiv.org/abs/2503.05283) [follow-up (opens a new tab)](https://arxiv.org/abs/2512.03750) [work (opens a new tab)](http://arxiv.org/abs/2511.02767).

The team’s hypothesis gets its name from a 2,400-year-old allegory by the Greek philosopher Plato. In it, prisoners trapped inside a cave perceive the world only through shadows cast by outside objects. Plato maintained that we’re all like those unfortunate prisoners. The objects we encounter in everyday life, in his view, are pale shadows of ideal “forms” that reside in some transcendent realm beyond the reach of the senses.

The Platonic representation hypothesis is less abstract. In this version of the metaphor, what’s outside the cave is the real world, and it casts machine-readable shadows in the form of streams of data. AI models are the prisoners. The MIT team’s claim is that very different models, exposed only to the data streams, are beginning to converge on a shared “Platonic representation” of the world behind the data.

“Why do the language model and the vision model align? Because they’re both shadows of the same world,” said [Phillip Isola (opens a new tab)](https://web.mit.edu/phillipi/), the senior author of the paper.

Not everyone is convinced. One of the main points of contention involves which representations to focus on. You can’t inspect a language model’s internal representation of every conceivable sentence, or a vision model’s representation of every image. So how do you decide which ones are, well, representative? Where do you look for the representations, and how do you compare them across very different models? It’s unlikely that researchers will reach a consensus on the Platonic representation hypothesis anytime soon, but that doesn’t bother Isola.

“Half the community says this is obvious, and the other half says this is obviously wrong,” he said. “We were happy with that response.”

## **The Company Being Kept**

If AI researchers don’t agree on Plato, they might find more common ground with his predecessor Pythagoras, whose philosophy supposedly started from the premise “All is number.” That’s an apt description of the neural networks that power AI models. Their representations of words or pictures are just long lists of numbers, each indicating the degree of activation of a specific artificial neuron.

To simplify the math, researchers typically focus on a single layer of a neural network in isolation, which is akin to taking a snapshot of brain activity in a specific region at a specific moment in time. They write down the neuron activations in this layer as a geometric object called a vector — an arrow that points in a particular direction in an abstract space. Modern AI models have many thousands of neurons in each layer, so their representations are high-dimensional vectors that are impossible to visualize directly. But vectors make it easy to compare a network’s representations: Two representations are similar if the corresponding vectors point in similar directions.

Within a single AI model, similar inputs tend to have similar representations. In a language model, for instance, the vector representing the word “dog” will be relatively close to vectors representing “pet,” “bark,” and “furry,” and farther from “Platonic” and “molasses.” It’s a [precise mathematical realization](https://www.quantamagazine.org/how-embeddings-encode-what-words-mean-sort-of-20240918/) of an idea memorably expressed more than 60 years ago by the British linguist John Rupert Firth: “You shall know a word by the company it keeps.”

What about representations in different models? It doesn’t make sense to directly compare activation vectors from separate networks, but researchers have devised indirect ways to assess representational similarity. One popular approach is to embrace the lesson of Firth’s pithy quote and measure whether two models’ representations of an input keep the same company.

Imagine that you want to compare how two language models represent words for animals. First, you’ll compile a list of words — dog, cat, wolf, jellyfish, and so on. You’ll then feed these words into both networks and record their representations of each word. In each network, the representations will form a cluster of vectors. You can then ask: How similar are the overall shapes of the two clusters?

“It can kind of be described as measuring the similarity of similarities,” said [Ilia Sucholutsky (opens a new tab)](https://ilia10000.github.io/), an AI researcher at New York University.

Mark Belan/ _Quanta Magazine_

In this simple example, you’d expect some similarity between the two models — the “cat” vector would probably be close to the “dog” vector in both networks, for instance, and the “jellyfish” vector would point in a different direction. But the two clusters probably won’t look exactly the same. Is “dog” more like “cat” than “wolf,” or vice versa? If your models were trained on different datasets, or built on different network architectures, they might not agree.

Researchers [began to explore (opens a new tab)](https://arxiv.org/abs/1511.07543) representational similarity among AI models with this approach in the mid-2010s and found that different models’ representations of the same concepts were often similar, though far from identical. Intriguingly, a few studies found that more powerful models seemed to have more similarities in their representations than weaker ones. One 2021 paper dubbed this the “ [Anna Karenina scenario (opens a new tab)](https://arxiv.org/abs/2106.07682),” a nod to the opening line of the [classic Tolstoy novel (opens a new tab)](https://www.gutenberg.org/files/1399/1399-h/1399-h.htm). Perhaps successful AI models are all alike, and every unsuccessful model is unsuccessful in its own way.

That paper, like much of the early work on representational similarity, focused only on computer vision, which was then the most popular branch of AI research. The advent of powerful language models was about to change that. For Isola, it was also an opportunity to see just how far representational similarity could go.

## **Convergent Evolution**

The story of the Platonic representation hypothesis paper began in early 2023, a turbulent time for AI researchers. ChatGPT had been released a few months before, and it was increasingly clear that simply scaling up AI models — training larger neural networks on more data — made them better at many different tasks. But it was unclear why.

“Everyone in AI research was going through an existential life crisis,” said [Minyoung Huh (opens a new tab)](https://minyoungg.github.io/me/), an OpenAI researcher who was a graduate student in Isola’s lab at the time. He began meeting regularly with Isola and their colleagues [Brian Cheung (opens a new tab)](https://briancheung.github.io/) and [Tongzhou Wang (opens a new tab)](https://www.tongzhouwang.info/) to discuss how scaling might affect internal representations.

https://www.quantamagazine.org/wp-content/uploads/2026/01/Phillip-Isola-Mosaic.webp

Clockwise from top right: Minyoung Huh, Brian Cheung, Tongzhou Wang, and Phillip Isola proposed that different AI models are converging toward a shared “Platonic representation” of the world behind their training data.

From top right: Anna Decker; @by.h\_official; Jiaxi Chen; Kris Brewer

Imagine a case where multiple models are trained on the same data, and the stronger models learn more similar representations. This isn’t necessarily because these models are creating a more accurate likeness of the world. They could just be better at grasping quirks of the training dataset.

Now consider models trained on different datasets. If their representations also converge, that would be more compelling evidence that models are getting better at grasping shared features of the world behind the data. Convergence between models that learned from entirely different data types, such as language and vision models, would provide even stronger evidence.

A year after their initial conversations, Isola and his colleagues decided to write a paper reviewing the evidence for convergent representations and presenting an argument for the Platonic representation hypothesis.

By then, other researchers had [started (opens a new tab)](https://arxiv.org/abs/2209.15162) [studying (opens a new tab)](https://arxiv.org/abs/2302.06555) [similarities (opens a new tab)](https://arxiv.org/abs/2401.05224) between vision and language model representations. Huh conducted his own experiment, in which he tested a set of five vision models and 11 language models of varying sizes on a dataset of captioned pictures from Wikipedia. He would feed the pictures into the vision models and the captions into the language models, and then compare clusters of vectors in the two types. He observed a steady increase in representational similarity as models became more powerful. It was exactly what the Platonic representation hypothesis predicted.

## **Find the Universals**

Of course, it’s never so simple. Measurements of representational similarity invariably involve a host of experimental choices that can affect the outcome. Which layers do you look at in each network? Once you have a cluster of vectors from each model, which of the [many (opens a new tab)](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full) [mathematical (opens a new tab)](https://arxiv.org/abs/1905.00414) [methods (opens a new tab)](https://arxiv.org/abs/2305.06329) do you use to compare them? And which representations do you measure in the first place?

“If you only test one dataset, you don’t necessarily know how \[the result\] generalizes,” said Christopher Wolfram, a researcher at the University of Chicago who has studied [representational similarity in language models (opens a new tab)](https://arxiv.org/abs/2504.08775). “Who knows what would happen if you did some weirder dataset?”

Isola acknowledged that the issue is far from settled. It’s not a question that any one paper can resolve: In principle, you can measure models’ representations of any picture or any sentence. To him, cases where models do exhibit convergence are more compelling than cases where they may not.

https://www.quantamagazine.org/wp-content/uploads/2026/01/Alexei-Efros-cr.PeterDaSilve.webp

Alexei Efros argues that the differences between AI models reveal more than the similarities.

Peter DaSilva for _Quanta Magazine_

“The endeavor of science is to find the universals,” Isola said. “We could study the ways in which models are different or disagree, but that somehow has less explanatory power than identifying the commonalities.”

Other researchers argue that it’s more productive to focus on where models’ representations differ. Among them is [Alexei Efros](https://www.quantamagazine.org/the-computing-pioneer-helping-ai-see-20231024/), a researcher at the University of California, Berkeley, who has been an adviser to three of the four members of the MIT team.

“They’re all good friends and they’re all very, very smart people,” Efros said. “I think they’re wrong, but that’s what science is about.”

Efros noted that in the Wikipedia dataset that Huh used, the images and text contained very similar information by design. But most data we encounter in the world has features that resist translation. “There is a reason why you go to an art museum instead of just reading the catalog,” he said.

Any intrinsic sameness across models doesn’t have to be perfect to be useful. Last summer, researchers [devised a method (opens a new tab)](http://arxiv.org/abs/2505.12540) to translate internal representations of sentences from one language model to another. And if language and vision model representations are to some extent interchangeable, that could lead to new ways to train models that learn from both data types. Isola and others explored [one such training scheme (opens a new tab)](https://arxiv.org/abs/2510.08492) in a recent paper.

Despite these promising developments, other researchers think it’s unlikely that any single theory will fully capture the behavior of modern AI models.

“You can’t reduce a trillion-parameter system to simple explanations,” said [Jeff Clune (opens a new tab)](http://jeffclune.com/), an AI researcher at the University of British Columbia. “The answers are going to be complicated.”