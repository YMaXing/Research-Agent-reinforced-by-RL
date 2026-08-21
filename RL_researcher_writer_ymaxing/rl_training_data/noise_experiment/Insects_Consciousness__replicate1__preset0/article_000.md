# Animal Consciousness and the AI Mirror: Lessons from the 2024 New York Declaration

As AI engineers, we often debate the inner lives of our models. But while we focus on the emergent abilities of large language models, a quiet revolution has been happening in biology. It started for me with a 2022 study that found bumblebees voluntarily rolling small wooden balls, not for food or any immediate reward, but seemingly just for fun [[35]](https://www.scientificamerican.com/article/ball-rolling-bumble-bees-just-wanna-have-fun?ref=refind), [[38]](https://www.sciencedirect.com/science/article/pii/S0003347222002366). This behavior, so decoupled from survival, points toward complex affective states in a brain with only a million neurons.

This finding is part of a wave of research that has reshaped our understanding of animal minds. For decades, scientists broadly agreed that animals similar to us, like other mammals and birds, are conscious. Recently, however, evidence has mounted for consciousness in creatures far more alien to us. This shift was formalized on April 19, 2024, with the release of the New York Declaration on Animal Consciousness [[52]](http://www.nydeclaration.com/). It states that “the empirical evidence indicates at least a realistic possibility of conscious experience in all vertebrates (including all reptiles, amphibians, and fishes) and many invertebrates (including, at minimum, cephalopod mollusks, decapod crustaceans, and insects)” [[52]](http://www.nydeclaration.com/).

The declaration was unveiled at a conference at New York University and spearheaded by philosopher Kristin Andrews, environmental scientist Jeff Sebo, and philosopher Jonathan Birch [[40]](https://www.kimmela.org/2024/05/05/a-new-declaration-on-animal-consciousness), [[42]](https://www.theatlantic.com/science/archive/2024/04/animal-consciousness-declaration-new-york/678223). It was signed by a prominent group of neuroscientists, psychologists, and philosophers, including Anil Seth, Christof Koch, David Chalmers, and Peter Godfrey-Smith [[42]](https://www.theatlantic.com/science/archive/2024/04/animal-consciousness-declaration-new-york/678223). The document carefully focuses on phenomenal consciousness, the subjective character of experience. It asks if there is "something that it is like to be that organism," a question originally posed by philosopher Thomas Nagel in his 1974 essay, “What Is It Like to Be a Bat?” [[43]](https://www.informationphilosopher.com/solutions/philosophers/nagelt), [[44]](https://www.cs.ox.ac.uk/activities/ieg/e-library/sources/nagel_bat.pdf). This is distinct from higher-order capacities like self-awareness or metacognition.

This growing consensus around animal sentience provides a critical mirror for our own field. It highlights an important distinction between biological consciousness and artificial intelligence. As neuroscientist Anil Seth notes, the declaration should galvanize "an understanding and appreciation that we have much more in common with other animals than we do with things like ChatGPT” [[1]](https://www.theatlantic.com/science/archive/2024/04/animal-consciousness-declaration-new-york/678223). While LLMs excel at linguistic tasks, they show no evidence of the play, pain avoidance, or anxiety-like states now being documented across the animal kingdom.

```mermaid
flowchart LR
    %% Horizontal arrow labeled with years
    start_point(( )) -- "Years" --> Y2012["2012"]
    Y2012 -- "Time Progression" --> Y2024["2024"]
    Y2024 -- "Future" --> end_point(( ))

    %% Declarations
    CD["Cambridge Declaration"]
    NYD["New York Declaration"]

    Y2012 --> CD
    Y2024 --> NYD

    %% Widening circle of species
    subgraph "Species Considered Possibly Conscious"
        S_2012(("mammals & birds<br/>(2012)"))
        S_2024(("all vertebrates + cephalopods,<br/>decapods, insects (2024)"))
    end

    CD --> S_2012
    NYD --> S_2024

    S_2012 -- "expands to include" --> S_2024

    %% Callouts for terminology shift
    subgraph "Terminology Shift"
        Term_Old[""consciousness""]
        Term_New[""realistic possibility of<br/>phenomenal consciousness""]
    end

    S_2012 -. "initial concept" .-> Term_Old
    S_2024 -. "evolved concept" .-> Term_New

    Term_Old --> Term_New
```
Image 1: A conceptual timeline illustrating the shift in understanding of consciousness from the 2012 Cambridge Declaration to the 2024 New York Declaration, showing the expansion of species considered possibly conscious and the evolution of terminology.

The 2024 Declaration is the formal culmination of a rapid accumulation of behavioral evidence gathered over the last 15 years. The next section examines that evidence in detail, explains why the field moved to a public declaration, and dismantles the old neural-complexity barrier.

## A Growing Awareness

The New York Declaration builds on over a decade of findings that challenge old assumptions about animal minds. This evidence comes not from one domain but from across a wide spectrum of species, revealing complex behaviors in creatures previously thought to be simple automatons.

One of the most compelling lines of evidence comes from studies on pain. In 2021, research on octopuses used a conditioned place preference test, a standard for assessing pain in lab rats. After an injection of acetic acid in their preferred chamber, octopuses developed a lasting aversion to it. When later given an anesthetic in a different chamber, they developed a preference for that new location, suggesting the drug provided relief [[53]](https://sites.google.com/nyu.edu/nydeclaration/background?authuser=0). This indicates not just a reflexive response to injury, but an affective, pain-like experience.

Evidence for complex memory has also been found in invertebrates. Cuttlefish have demonstrated a form of episodic-like memory, recalling not just what, where, and when a past event occurred, but also how they experienced it. In a 2020 study, they could remember whether they had previously seen or smelled a specific prey item, a capacity known as source memory [[53]](https://sites.google.com/nyu.edu/nydeclaration/background?authuser=0).

In the world of fish, cleaner wrasse have been shown to pass a version of the mirror-mark test. After being familiarized with a mirror, a colored mark was placed on their bodies. Upon seeing their reflection, the fish attempted to scrape the mark off, a behavior often interpreted as a form of self-recognition [[53]](https://sites.google.com/nyu.edu/nydeclaration/background?authuser=0). These findings have been supported by similar results in zebrafish, which also show signs of curiosity, voluntarily exploring new objects without any external reward [[53]](https://sites.google.com/nyu.edu/nydeclaration/background?authuser=0).

Insects, too, have displayed behaviors indicative of inner states. Beyond the bumblebee play behavior, studies have found that fruit flies exhibit distinct active and quiet sleep phases, similar to REM and slow-wave sleep in humans, and that their sleep patterns are disrupted by social isolation [[53]](https://sites.google.com/nyu.edu/nydeclaration/background?authuser=0). Further studies on crayfish have revealed anxiety-like states. When exposed to electric shocks, they become more averse to bright, open spaces. This behavior is reversed when they are given benzodiazepines, the same class of anti-anxiety drugs used in humans [[53]](https://sites.google.com/nyu.edu/nydeclaration/background?authuser=0).

This accumulation of evidence created a consensus among specialists that was not being communicated to the public or policymakers. Jeff Sebo, one of the declaration's organizers, noted that the goal was to formalize this agreement to encourage reflection on animal welfare [[32]](https://sites.google.com/nyu.edu/nydeclaration/background). The declaration aims to ensure that when a "realistic possibility" of consciousness exists, it is considered in decisions affecting that animal [[22]](https://jeffsebo.net).

This represents a significant evolution from the 2012 Cambridge Declaration on Consciousness. That document asserted that mammals and birds possess the "neurological substrates that generate consciousness" [[54]](http://fcmconference.org/img/CambridgeDeclarationOnConsciousness.pdf). The 2024 New York Declaration expands this scope to all vertebrates and many invertebrates, while deliberately using the more cautious phrasing "realistic possibility of conscious experience" [[52]](http://www.nydeclaration.com/). This careful wording reflects the scientific humility required when studying subjective experience, a point emphasized by signatories like Anil Seth [[2]](https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419).

A long-standing barrier to accepting invertebrate consciousness was the assumption that their nervous systems were too simple. However, the bee brain’s million neurons, while a fraction of our 86 billion, are incredibly complex and densely interconnected, sufficient for play and social learning [[31]](https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419). Furthermore, nervous systems can be organized in radically different ways. An octopus has a highly distributed nervous system, with two-thirds of its neurons in its arms [[10]](https://neuroscience.stanford.edu/news/octopus-brains). A severed arm can continue to perform complex actions, like grasping and avoidance, demonstrating that sophisticated motor control does not require a centralized brain [[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988249).

The final objection, the lack of a cerebral cortex, has also been dismantled. As philosopher Kristin Andrews points out, we may not need "nearly as much equipment as we thought we did" for consciousness [[31]](https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419). Birds, reptiles, and fish have different brain structures that perform cortex-like functions, such as the avian pallium [[48]](https://en.wikipedia.org/wiki/Avian_pallium), [[49]](https://asknature.org/strategy/bird-brains-use-unique-structure-to-support-high-intelligence). Similarly, the octopus vertical lobe serves as a center for memory and learning, proving that intelligence requires the right circuitry, not a specific anatomy [[47]](https://asknature.org/strategy/complex-memory-processing-in-the-cephalopod-vertical-lobe). Philosopher Peter Godfrey-Smith argues that consciousness can arise from electrical oscillations in living brains, a feature not dependent on a specific architecture and observable in invertebrates [[27]](https://iai.tv/articles/studies-on-animal-minds-suggest-consciousness-is-not-computation-auid-3535). He notes that consciousness "can exist in an architecture that looks completely alien" to our own [[31]](https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419).

The evidentiary and architectural arguments have now shifted the scientific default. This pivot leads to downstream ethical obligations, practical tensions, and policy implications that follow once we accept the realistic possibility of consciousness in these creatures.

## Mindful Relations

Accepting that there is a realistic possibility of consciousness in a wide range of animals forces us to reconsider our relationship with them. The ethical obligations extend beyond merely preventing suffering. As Jeff Sebo argues, it is not enough to prevent pain; we must also provide "the kinds of enrichment and opportunities that allow them to express their instincts and explore their environments and engage in social systems and otherwise be the kinds of complex agents they are" [[31]](https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419).

However, this raises practical tensions, particularly with insects. As Peter Godfrey-Smith points out, our relationship with species like mosquitoes is "inevitably a somewhat antagonistic one" [[31]](https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419). Acknowledging their potential for experience does not eliminate the need to control disease vectors or protect crops. It does, however, force a more explicit and considered ethical calculus rather than a blanket dismissal of their welfare.

This new understanding also exposes a significant welfare gap in laboratory research. While vertebrates used in experiments are protected by animal care committees, invertebrates like *Drosophila* fruit flies are not, despite their use in countless neuroscience studies [[19]](https://www.thetransmitter.org/policy/knowledge-gaps-in-cephalopod-care-could-stall-welfare-standards). This stands in contrast to the growing oversight for cephalopods, highlighting an inconsistency in our current standards.

Policy can, and does, adapt to new scientific consensus. In the UK, a government-commissioned review of over 300 scientific studies concluded there was strong evidence of sentience in decapod crustaceans and cephalopod molluscs [[6]](https://www.eurogroupforanimals.org/news/uk-sentience-bill-passes-final-stages-recognise-decapod-and-cephalopod-sentience-law), [[7]](https://www.eurogroupforanimals.org/news/decapods-and-cephalopods-be-recognised-sentient-beings-under-uk-law). This led to their inclusion in the Animal Welfare (Sentience) Bill, legally recognizing animals like crabs, lobsters, and octopuses as sentient beings [[5]](https://naturewatch.org/study-confirms-animal-sentience-in-crustaceans), [[8]](https://researchbriefings.files.parliament.uk/documents/CBP-9423/CBP-9423.pdf). This provides a clear pathway for how scientific findings can translate into concrete legal protections.

For AI engineers, this shift in biology offers a cautionary tale. While Sebo and others agree that "current AI systems are very unlikely to be conscious," the rapid evolution of our understanding of animal minds "does give me pause and makes me want to approach the topic with caution and humility" [[31]](https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419). The criteria being used to identify consciousness in animals—affective states, play, and complex decision-making—are currently absent in AI. This provides a grounding framework for future debates on machine consciousness.

The path forward is clear: more research is needed. Kristin Andrews has called for scientists to use the resources they already have. "All these nematode worms and fruit flies that are in almost every university—study consciousness in them," she urges. "You already have them. Somebody in your lab is going to need a project. Make that project a consciousness project. Imagine that!” [[31]](https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419). By studying simpler models, we can make progress on one of science's oldest questions and, in doing so, better understand our place among the other minds of this world [[14]](https://www.multiverses.xyz/podcast/animal-minds-kristin-andrews-on-assuming-consciousness-in-other-species).

## References

- [1] [Animal consciousness: why the declaration of a new consensus is needed](https://www.theatlantic.com/science/archive/2024/04/animal-consciousness-declaration-new-york/678223)
- [2] [Insects and Other Animals Have Consciousness, Experts Declare](https://www.quantamagazine.org/insects-and-other-animals-have-consciousness-experts-declare-20240419)
- [3] [Revisiting Animal Consciousness](https://advancedconsciousness.org/revisiting-animal-consciousness)
- [4] [Does sentience legislation help animals?](https://www.animalask.org/post/does-sentience-legislation-help-animals)
- [5] [Study confirms animal sentience in crustaceans and molluscs - Naturewatch Foundation](https://naturewatch.org/study-confirms-animal-sentience-in-crustaceans)
- [6] [UK Sentience Bill passes final stages to recognise decapod and cephalopod sentience in law | Eurogroup for Animals](https://www.eurogroupforanimals.org/news/uk-sentience-bill-passes-final-stages-recognise-decapod-and-cephalopod-sentience-law)
- [7] [Decapods and cephalopods to be recognised as sentient beings under UK law | Eurogroup for Animals](https://www.eurogroupforanimals.org/news/decapods-and-cephalopods-be-recognised-sentient-beings-under-uk-law)
- [8] [Animal Welfare (Sentience) Bill](https://researchbriefings.files.parliament.uk/documents/CBP-9423/CBP-9423.pdf)
- [9] [Octopus Arms Are Controlled by a Nervous System That's Like No Other : ScienceAlert](https://www.sciencealert.com/octopus-arms-are-controlled-by-a-nervous-system-thats-like-no-other)
- [10] [The Octopus Brain | Stanford Neurosciences Institute](https://neuroscience.stanford.edu/news/octopus-brains)
- [11] [The Mind of an Octopus - YouTube](https://www.youtube.com/watch?v=W9Gnw7B7oGM)
- [12] [The segmented nervous system of the octopus arm | Nature Communications](https://www.nature.com/articles/s41467-024-55475-5)
- [13] [Where Is It Like to Be an Octopus?](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988249/)
- [14] [Animal Minds — Kristin Andrews on assuming consciousness in other species - multiverses](https://www.multiverses.xyz/podcast/animal-minds-kristin-andrews-on-assuming-consciousness-in-other-species)
- [15] [Knowledge gaps in cephalopod care could stall welfare standards](https://www.thetransmitter.org/policy/knowledge-gaps-in-cephalopod-care-could-stall-welfare-standards)
- [16] [Jeff Sebo on animal consciousness, AI consciousness, and The New York Declaration - YouTube](https://www.youtube.com/watch?v=ak3WuQhtoW4)
- [17] [Jeff Sebo](https://jeffsebo.net)
- [18] [A New Declaration on Animal Consciousness | The Kimmela Center for Animal Advocacy](https://www.kimmela.org/2024/05/05/a-new-declaration-on-animal-consciousness)
- [19] [Peter Godfrey-Smith: Other Minds: The Octopus, the Sea, and the Deep Origins of Consciousness - YouTube](https://www.youtube.com/watch?v=Mi4-EOThAIc)
- [20] [Living on Earth: Notes to Chapter 6 - Peter Godfrey-Smith](https://petergodfreysmith.com/living-on-earth-notes-to-chapter-6)
- [21] [Studies on animal minds suggest consciousness is not computation](https://iai.tv/articles/studies-on-animal-minds-suggest-consciousness-is-not-computation-auid-3535)
- [22] [Peter Godfrey-Smith: The Evolution of Consciousness - YouTube](https://www.youtube.com/watch?v=RkWvrt9GXsc)
- [23] [Cephalopods and the Evolution of the Mind](https://petergodfreysmith.com/wp-content/uploads/2013/06/Cephalopods_PGS_PacConBio_2013.pdf)
- [24] [Frontiers | Should we provide positive enrichment for invertebrates?](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1700354/full)
- [25] [The Background of the New York Declaration](https://sites.google.com/nyu.edu/nydeclaration/background)
- [26] [Can an AI Deserve Protection? A Philosopher on the Ethics of Living with Non-Human Intelligence - Next Big Idea Club](https://nextbigideaclub.com/magazine/ai-deserve-protection-philosopher-ethics-living-non-human-intelligence-bookbite/54074)
- [27] [Jeff Sebo on using evidence and reason to help animals - The Effective Altruism Forum](https://www.effectivealtruism.org/stories/jeff-sebo)
- [28] [Ball-Rolling Bumble Bees Just Wanna Have Fun](https://www.scientificamerican.com/article/ball-rolling-bumble-bees-just-wanna-have-fun?ref=refind)
- [29] [Bumblebees get a buzz out of playing with balls, study finds | Bees | The Guardian](https://www.theguardian.com/science/2022/oct/27/bumblebees-playing-wooden-balls-bees-study)
- [30] [First-ever study shows bumble bees ‘play’ - Queen Mary University of London](https://www.qmul.ac.uk/news/latest-news/2022/se/first-ever-study-shows-bumble-bees-play.html)
- [31] [Do bumble bees play? - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0003347222002366)
- [32] [Bumblebees socially learn behaviour too complex to innovate alone | Nature](https://www.nature.com/articles/s41586-024-07126-4)
- [33] [Hundreds of Experts Sign New York Declaration on Animal Consciousness](https://thebrooksinstitute.org/animal-law-digest/us/issue-259/hundreds-experts-sign-new-york-declaration-animal-consciousness)
- [34] [Thomas Nagel - Information Philosopher](https://www.informationphilosopher.com/solutions/philosophers/nagelt)
- [35] [What Is It Like to Be a Bat?](https://www.cs.ox.ac.uk/activities/ieg/e-library/sources/nagel_bat.pdf)
- [36] [What Is It Like to Be a Bat? - Wikipedia](https://en.wikipedia.org/wiki/What_Is_It_Like_to_Be_a_Bat%3F)
- [37] [Thomas Nagel’s Bat and Ours – The Philosophical Salon](https://thephilosophicalsalon.com/thomas-nagels-bat-and-ours)
- [38] [Complex memory processing in the cephalopod vertical lobe • AskNature](https://asknature.org/strategy/complex-memory-processing-in-the-cephalopod-vertical-lobe)
- [39] [Avian pallium - Wikipedia](https://en.wikipedia.org/wiki/Avian_pallium)
- [40] [Bird brains use unique structure to support high intelligence • AskNature](https://asknature.org/strategy/bird-brains-use-unique-structure-to-support-high-intelligence)
- [41] [A cortex-like canonical circuit in the avian forebrain](https://pmc.ncbi.nlm.nih.gov/articles/PMC10940863/)
- [42] [The micro-circuitry of the octopus vertical lobe](https://elifesciences.org/articles/84257)
- [43] [The New York Declaration on Animal Consciousness](https://sites.google.com/nyu.edu/nydeclaration/background?authuser=0)
- [44] [The Cambridge Declaration on Consciousness](http://fcmconference.org/img/CambridgeDeclarationOnConsciousness.pdf)
- [45] [What Is It Like to Be a Bat?](https://www.sas.upenn.edu/~cavitch/pdf-library/Nagel_Bat.pdf)