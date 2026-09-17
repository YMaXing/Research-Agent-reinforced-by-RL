# The Cosmic Code: How Space-Time Protects Itself with Quantum Error Correction

## Introduction

In 1994, the mathematician Peter Shor developed an algorithm that had a major impact on the worlds of computing and cryptography. He proved that a hypothetical quantum computer could factor large numbers exponentially faster than any known classical computer, rendering much of modern cryptography obsolete. This generated immense excitement, but it was tempered by widespread skepticism. The very properties that make quantum computers powerful also make them incredibly fragile. It seemed impossible that any physical system could maintain the required quantum coherence long enough to perform a useful computation.

Then, in a remarkable turn, the solution to this formidable engineering challenge appeared to hold the key to one of the deepest mysteries in fundamental physics: the nature of space-time itself. In 2014, physicists Ahmed Almheiri, Xi Dong, and Daniel Harlow proposed that the holographic principle, which describes how a bendy, gravitational space-time can emerge from a flat, quantum theory on its boundary, works exactly like a quantum error-correcting code [[1]](https://arxiv.org/abs/1411.7041). This discovery suggested that the fabric of reality is woven from the same mathematical principles needed to build a fault-tolerant quantum computer.

This article explores this unexpected unity. You will learn how the quest to protect fragile quantum information led to a framework that explains the intrinsic robustness of space-time. We examine the toy models that make this connection concrete and see how the analogy breaks down at the edge of black holes, revealing deep truths about quantum gravity. Ultimately, this article explains that entanglement is not just a strange feature of quantum mechanics; it is the very glue holding space-time together, organized by the logic of error correction.

## The Quantum Computing Challenge and the Discovery of a Cosmic Connection

The power of a quantum computer comes from its fundamental unit of information: the qubit. A classical n-bit register can store only one of 2ⁿ possible numbers at a time. In contrast, an n-qubit register can exist in a coherent superposition of all 2ⁿ basis states simultaneously, enabling a form of exponential parallelism. Shor's algorithm masterfully exploits this, reducing the problem of factoring large integers to finding the period of a function evaluated in superposition [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

However, this power comes at the cost of extreme fragility. Widespread skepticism initially met the promise of quantum computing, as any physical qubit would inevitably interact with its environment and "decohere," losing its quantum properties long before a complex circuit could finish running. Qubits are highly susceptible to errors. The slightest environmental disturbance, such as a stray magnetic field or a microwave pulse, can corrupt their delicate state. These errors come in two main flavors: bit-flips, which swap the probabilities of |0⟩ and |1⟩, and phase-flips, which invert the mathematical relationship between the two states. Even worse, you cannot simply measure the qubits to check for errors. Any direct measurement collapses the superposition, destroying the very quantum computation you are trying to protect. For years, this seemed like a fatal flaw [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

In 1995, just a year after his factoring algorithm, Shor delivered another breakthrough: a proof that quantum error-correcting codes (QEC) could exist [[3]](https://en.wikipedia.org/wiki/Quantum_error_correction), [[4]](https://people.eecs.berkeley.edu/~jswright/quantumcodingtheory24/scribe%20notes/lecture01.pdf). A year later, researchers including Dorit Aharonov, Michael Ben-Or, Emanuel Knill, Raymond Laflamme, and Wojciech Zurek independently proved the threshold theorem. This theorem states that if the error rate of individual physical components is below a certain constant threshold, active error correction can suppress errors faster than they accumulate, making arbitrarily long quantum computations possible [[5]](https://en.wikipedia.org/wiki/Threshold_theorem), [[6]](https://www.quantinuum.com/blog/quantinuum-with-partners-princeton-and-nist-deliver-seminal-result-in-quantum-error-correction). As quantum computer scientist Scott Aaronson noted, this was "the central discovery in the ’90s that convinced people that scalable quantum computing should be possible at all." The challenge was no longer one of fundamental impossibility, but "merely a staggering problem of engineering." The effort to design better codes to cope with the daunting error rates of real qubits remains "one of the major thrusts of the field" [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

For nearly two decades, QEC remained the domain of quantum computing. But in 2014, a trio of young quantum gravity researchers—Ahmed Almheiri, Xi Dong, and Daniel Harlow—made a significant connection. They realized that the emergence of space-time in holographic theories, specifically the Anti-de Sitter/Conformal Field Theory (AdS/CFT) correspondence, works just like a QEC code. Their seminal paper triggered a wave of activity, suggesting that space-time itself is a code, at least in these theoretical universes [[1]](https://arxiv.org/abs/1411.7041).

John Preskill, a theoretical physicist at Caltech, argues that this connection explains the "intrinsic robustness" of space-time. Despite being woven from fragile quantum entanglement, the geometry of our universe does not feel delicate. "We’re not walking on eggshells to make sure we don’t make the geometry fall apart," Preskill said. "I think this connection with quantum error correction is the deepest explanation we have for why that’s the case." In this view, the macroscopic geometry is a protected logical property, immune to small, local errors in the underlying quantum state [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

This discovery opened a two-way street of inspiration. Researchers hope that the highly efficient codes implemented by space-time could point the way to scalable quantum computing. As Almheiri put it, "Space-time is a lot smarter than us." Conversely, the language of QEC provides a new toolkit for probing the deepest mysteries of quantum gravity, especially the paradoxes surrounding black holes [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

With the Almheiri-Dong-Harlow conjecture establishing that holographic space-time behaves as a quantum error-correcting code, we now examine the concrete mechanics of how such codes protect logical information in simple qubit systems. This will allow us to recognize the same mathematical signatures when they reappear in the bulk geometry of AdS.

## How Quantum Error-Correcting Codes Work

The trick to protecting information in jittery qubits is to store it not in individual qubits, but in patterns of entanglement among many. Instead of trusting one fragile physical qubit, a logical qubit is encoded across a larger set of physical qubits in a highly entangled state. This non-local encoding ensures that no single physical qubit holds any information about the logical state, making the information resilient to local errors.

As a simple example, consider the three-qubit bit-flip code. While not a fully practical code because it cannot protect against phase-flips, it is an instructive first step [[3]](https://en.wikipedia.org/wiki/Quantum_error_correction). To protect one logical qubit, we use three physical qubits. The logical state `|0⟩` is encoded as `|000⟩` (all three physical qubits are `|0⟩`), and the logical state `|1⟩` is encoded as `|111⟩`. A general logical state `α|0⟩ + β|1⟩` becomes the entangled state `α|000⟩ + β|111⟩` [[7]](https://www.cl.cam.ac.uk/teaching/1920/QuantComp/Quantum_Computing_Lecture_13.pdf), [[8]](https://learn.microsoft.com/en-us/azure/quantum/concepts-error-correction).

Now, suppose a bit-flip error corrupts one of the physical qubits. How do we detect and correct it without measuring the qubits directly and collapsing the logical state? The solution is to perform parity-check measurements. We use two auxiliary "ancilla" qubits to check the parity—whether they are the same or different—of two pairs of physical qubits: (qubit 1, qubit 2) and (qubit 1, qubit 3) [[7]](https://www.cl.cam.ac.uk/teaching/1920/QuantComp/Quantum_Computing_Lecture_13.pdf), [[9]](https://astro.pas.rochester.edu/~aquillen/phy265/lectures/QI_E.pdf).

The measurement of these ancilla qubits yields an "error syndrome" that reveals which qubit, if any, has flipped:
*   **No flips (`|000⟩` or `|111⟩`):** Both pairs match. Syndrome: (match, match).
*   **Qubit 1 flips (`|100⟩` or `|011⟩`):** Both pairs do not match. Syndrome: (do not match, do not match).
*   **Qubit 2 flips (`|010⟩` or `|101⟩`):** The first pair does not match, the second does. Syndrome: (do not match, match).
*   **Qubit 3 flips (`|001⟩` or `|110⟩`):** The first pair matches, the second does not. Syndrome: (match, do not match).

Each syndrome uniquely identifies the error. We can then apply a corrective operation (a bit-flip) to the corresponding qubit, restoring the original encoded state. This entire process is a non-demolition measurement; it extracts information about the error without revealing anything about the logical state `α` or `β`, thus preserving the quantum computation [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

Image 1: A flowchart illustrating the three-qubit bit-flip code, showing encoding and non-demolition syndrome extraction.
```mermaid
flowchart LR
  %% Initial Qubits for Encoding
  subgraph "Initial Qubits for Encoding"
    LQ_init["Logical Qubit |ψ⟩"]
    AQ1_enc["Ancilla Qubit 1 |0⟩"]
    AQ2_enc["Ancilla Qubit 2 |0⟩"]
  end

  %% Encoding Process
  Encoding_Process["Encoding Circuit<br/>(2 CNOT gates:<br/>LQ->AQ1, LQ->AQ2)"]

  LQ_init --> "control" --> Encoding_Process
  AQ1_enc --> "target" --> Encoding_Process
  AQ2_enc --> "target" --> Encoding_Process

  %% Encoded Qubits
  subgraph "Encoded Logical Qubit |ψ_L⟩"
    EQ1["Physical Qubit 1"]
    EQ2["Physical Qubit 2"]
    EQ3["Physical Qubit 3"]
  end

  Encoding_Process -- "Qubit 1" --> EQ1
  Encoding_Process -- "Qubit 2" --> EQ2
  Encoding_Process -- "Qubit 3" --> EQ3

  %% Ancilla Qubits for Syndrome Extraction
  subgraph "Ancilla Qubits for Syndrome"
    SA1_init["Ancilla A |0⟩"]
    SA2_init["Ancilla B |0⟩"]
  end

  %% Parity Check 1
  PC1_Process["Parity Check 1<br/>(CNOTs: Q1->SA1, Q2->SA1)"]
  EQ1 --> "input" --> PC1_Process
  EQ2 --> "input" --> PC1_Process
  SA1_init --> "target" --> PC1_Process

  %% Parity Check 2
  PC2_Process["Parity Check 2<br/>(CNOTs: Q1->SA2, Q3->SA2)"]
  EQ1 --> "input" --> PC1_Process
  EQ3 --> "input" --> PC1_Process
  SA2_init --> "target" --> PC2_Process

  %% Syndrome Measurement
  Syndrome_Output["Syndrome Measurement<br/>(Ancilla A, Ancilla B)"]

  PC1_Process -- "Ancilla A State" --> Syndrome_Output
  PC2_Process -- "Ancilla B State" --> Syndrome_Output

  %% Logical Qubit (post-syndrome) - non-demolition
  subgraph "Logical Qubit (post-syndrome)"
    EQ1_post["Qubit 1"]
    EQ2_post["Qubit 2"]
    EQ3_post["Qubit 3"]
  end

  EQ1 --> "continues" --> EQ1_post
  EQ2 --> "continues" --> EQ2_post
  EQ3 --> "continues" --> EQ3_post
```

A key feature of the best QEC codes is that they can recover the complete logical information from slightly more than half of the physical qubits, even if the rest are entirely lost. This "majority rules" property is precisely what hinted to Almheiri, Dong, and Harlow that quantum error correction was at play in holography [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

Equipped with the concrete mechanics and the "slightly more than half" correctability signature of qubit-based codes, we now show how the holographic principle implements precisely the same structure on a gravitational stage, with AdS geometry emerging from entangled boundary degrees of freedom.

## The Holographic Principle and Space-Time Emerges as a Quantum Error-Correcting Code

To understand the connection to gravity, we first need to visit the theoretical playground where it was discovered: Anti-de Sitter (AdS) space. Our universe is described by a "de Sitter" geometry, which has a positive vacuum energy causing it to expand. In contrast, AdS space has a negative vacuum energy, giving it a hyperbolic geometry like one of M.C. Escher's *Circle Limit* woodcuts. In these designs, figures shrink as they approach the circular boundary. Similarly, AdS space has a boundary where space-time ends [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103), [[10]](https://www.youtube.com/watch?v=IIHucC-HPz0).

https://www.quantamagazine.org/wp-content/uploads/2019/01/Escher_1000.jpg 
Image 2: The hyperbolic geometry in M.C. Escher’s 1959 woodcut, Circle Limit III, is also a feature of anti-de Sitter space. (Source [https://en.wikipedia.org/wiki/Circle_Limit_III#/media/File:Escher_Circle_Limit_III.jpg](https://en.wikipedia.org/wiki/Circle_Limit_III#/media/File:Escher_Circle_Limit_III.jpg))

This boundary is crucial. In 1997, Juan Maldacena discovered the AdS/CFT correspondence, a powerful conjecture stating that a theory of quantum gravity within an AdS universe is perfectly equivalent (or "dual") to a standard quantum field theory without gravity living on its boundary. This is often a "strong-weak" duality, where a complex problem on one side maps to a simple one on the other. Everything that happens in the gravitational "bulk" is a holographic projection of information encoded in the entangled particles on the lower-dimensional boundary [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103), [[10]](https://www.youtube.com/watch?v=IIHucC-HPz0).

Almheiri and his colleagues noticed a striking parallel: any point in the interior of AdS space could be reconstructed from just over half of the boundary, exactly mirroring the property of an optimal QEC code [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103). In their 2014 paper, they introduced a "three-qutrit toy code" to make this analogy precise [[11]](https://errorcorrectionzoo.org/list/holographic). In this model, a single logical qutrit (a three-state particle) at the center of a 2D disk represents a point in bulk space-time. This logical information is encoded in the entanglement of three physical qutrits on the circular boundary. The code is constructed such that the logical qutrit is protected against the erasure of any one of the three physical qutrits; you can always reconstruct the bulk point from the remaining two [[12]](https://research.engineering.nyu.edu/~jbain/Talks/ST_QECC.pdf). This simple system acts as a minimal 2D hologram, where bulk information is non-locally stored in boundary entanglement.

Image 3: A diagram illustrating the Three-qutrit toy code as a minimal 2D hologram.
```mermaid
graph TD
    %% Central Logical Qutrit (Bulk)
    LQ["Logical Qutrit<br/>(Bulk Space-time Point)"]

    %% Boundary Physical Qutrits
    subgraph "Boundary: Three Physical Qutrits"
        PQ1["Physical Qutrit 1"]
        PQ2["Physical Qutrit 2"]
        PQ3["Physical Qutrit 3"]
    end

    %% Encoding Relationship
    LQ -- "encoded into" --> PQ1
    LQ -- "encoded into" --> PQ2
    LQ -- "encoded into" --> PQ3

    %% Protection and Hologram Concept
    Note["'Three-qutrit toy code'<br/>Protects Logical Qutrit against erasure of any one Physical Qutrit.<br/>Minimal 2D Hologram: Bulk info encoded non-locally in boundary entanglement."]

    LQ -.-> Note

    %% Visual grouping for boundary
    classDef boundaryGroup stroke-dasharray:5,5
    class PQ1,PQ2,PQ3 boundaryGroup
```

To model a full space-time, Fernando Pastawski, Beni Yoshida, Daniel Harlow, and John Preskill developed the HaPPY code in 2015. It uses a tensor network of "perfect tensors" arranged on a hyperbolic tiling of pentagons, which mimics the geometry of an AdS slice [[13]](https://ncatlab.org/nlab/show/HaPPY+code). Each tensor represents a bulk point, with its legs connecting to neighbors. Uncontracted legs at the network's edge are the physical boundary qubits, while internal dangling legs represent logical bulk qubits [[14]](https://errorcorrectionzoo.org/c/happy).

As Stanford's Patrick Hayden described them, the tiles are like "little Tinkertoys" that build the geometry. The network's connections define the bulk, and its structure naturally creates overlapping "entanglement wedges." Any bulk information inside a wedge can be reconstructed from the corresponding boundary region. The fact that a single bulk point lies in multiple overlapping wedges means it can be reconstructed from different subsets of boundary qubits—the defining feature of a QEC code [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

Image 4: A diagram illustrating the HaPPY tensor-network code, showing pentagonal tiles as bulk points with logical indices, connected to physical boundary indices, and the emergent holographic properties.
```mermaid
graph TD
    %% HaPPY Tensor Network - Core Structure
    subgraph "HaPPY Tensor Network: AdS₂ Hyperbolic Tiling"
        direction LR

        subgraph "Bulk Tiles"
            T_Center["Pentagonal Tile (Center)<br/>(Perfect Tensor, Bulk Point)"]
            LBI_Center(( "Logical Bulk Index<br/>(Red Dot)" ))
            T_Center -- "contains" --> LBI_Center

            T_N1["Pentagonal Tile (Neighbor 1)"]
            LBI_N1(( "Logical Bulk Index<br/>(Red Dot)" ))
            T_N1 -- "contains" --> LBI_N1

            T_N2["Pentagonal Tile (Neighbor 2)"]
            LBI_N2(( "Logical Bulk Index<br/>(Red Dot)" ))
            T_N2 -- "contains" --> LBI_N2

            T_N3["Pentagonal Tile (Neighbor 3)"]
            LBI_N3(( "Logical Bulk Index<br/>(Red Dot)" ))
            T_N3 -- "contains" --> LBI_N3
        end

        %% Connections between tiles
        T_Center --- T_N1
        T_Center --- T_N2
        T_Center --- T_N3

        %% Outer edges connecting to Physical Boundary Indices
        subgraph "Boundary Indices"
            PBI_A(( "Physical Boundary Index<br/>(White Dot)" ))
            PBI_B(( "Physical Boundary Index<br/>(White Dot)" ))
            PBI_C(( "Physical Boundary Index<br/>(White Dot)" ))
            PBI_D(( "Physical Boundary Index<br/>(White Dot)" ))
            PBI_E(( "Physical Boundary Index<br/>(White Dot)" ))
            PBI_F(( "Physical Boundary Index<br/>(White Dot)" ))
        end

        T_N1 -- "connects to" --> PBI_A
        T_N1 -- "connects to" --> PBI_B
        T_N2 -- "connects to" --> PBI_C
        T_N2 -- "connects to" --> PBI_D
        T_N3 -- "connects to" --> PBI_E
        T_N3 -- "connects to" --> PBI_F
    end

    %% Emergent Holographic Properties
    subgraph "Holographic Code Properties"
        BulkGeometry["Emergent Bulk Geometry<br/>(from contracting tensor network)"]
        EntanglementWedges["Overlapping Entanglement Wedges<br/>(consistent overlap)"]
        BulkOperatorPush["Bulk Operators pushed to Boundary<br/>(along different minimal surfaces)"]
        QuantumErrorCorrection["Quantum Error-Correcting Property"]
        HolographicCode["Holographic Code Concept<br/>(Bulk from Entanglement Patterns)"]
    end

    "HaPPY Tensor Network: AdS₂ Hyperbolic Tiling" -- "defines" --> BulkGeometry
    BulkGeometry -- "leads to" --> EntanglementWedges
    EntanglementWedges -- "enables" --> BulkOperatorPush
    BulkOperatorPush -- "demonstrates" --> QuantumErrorCorrection
    QuantumErrorCorrection -- "is a core feature of" --> HolographicCode
```

The general lesson is that QEC provides the ideal language for describing how a smooth, classical geometry emerges from a quantum boundary theory. "Quantum error correction gives us a more general way of thinking about geometry in this code language," said Preskill. He believes this language "ought to be applicable... to more general situations," including a universe like ours [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

For now, researchers are sticking with AdS spaces, which are simpler than our de Sitter universe but share many key properties, most importantly, black holes. "The most fundamental property of gravity is that there are black holes," said Harlow. "That’s what makes gravity different from all the other forces. That’s why quantum gravity is hard" [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103). The same QEC structure that protects smooth AdS geometry fails in the presence of black holes; we now examine the sharp breakdown of correctability at their horizons and the resulting paradoxes that any consistent theory of quantum gravity must resolve.

## Black Holes: Where Correctability Breaks Down

The language of quantum error correction provides a new way of describing black holes. As Patrick Hayden explains, the presence of a black hole is defined by "the breakdown of correctability." When errors become so overwhelming that you can no longer track what is happening in the bulk space-time, "you get a black hole. It’s like a sink for your ignorance" [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

This ignorance is at the heart of Stephen Hawking's 1974 discovery that black holes radiate heat and eventually evaporate. His calculations suggested this "Hawking radiation" is thermal, meaning it carries no information about what fell in. This leads to the infamous information paradox: if a pure quantum state collapses to form a black hole, which then evaporates into a mixed thermal state, information is lost and a fundamental tenet of quantum mechanics—unitarity—is violated. A complete theory of quantum gravity must explain how this information gets out [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

The QEC framework sharpens this problem. In a normal AdS universe, information in the bulk can be reconstructed from just over half the boundary. However, for an evaporating black hole, this reconstruction threshold shifts dramatically. To reconstruct information about the black hole's interior, you need access to roughly three-quarters of the boundary qubits. Almheiri notes that why this specific fraction comes up "is still an open question," but it signals a fundamental change in the properties of the holographic code once a horizon forms [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

Image 5: A diagram showing the shift in the reconstruction threshold for an evaporating black hole in AdS space.
```mermaid
flowchart LR
    subgraph "AdS Universe"
        AdS_Boundary(("AdS Boundary"))
        BH_Interior["Black Hole Interior"]
        AdS_Boundary -- "encloses" --> BH_Interior
    end

    subgraph "Scenario 1: Normal AdS Space"
        Normal_Boundary_Access["Boundary Access<br/>(51-60% of total boundary)"]
        Normal_EW["Entanglement Wedge<br/>(Normal AdS)"]
        Normal_Boundary_Access -- "forms part of" --> Normal_EW
    end

    subgraph "Scenario 2: Evaporating Black Hole"
        Evap_Boundary_Access["Boundary Access<br/>(approx. 75% of total boundary)"]
        Evap_EW["Entanglement Wedge<br/>(Evaporating BH)"]
        Evap_Boundary_Access -- "forms part of" --> Evap_EW
    end

    Normal_EW -- "reconstructs" --> BH_Interior
    Evap_EW -- "reconstructs" --> BH_Interior

    Normal_EW -- "Shift in Reconstruction Threshold<br/>(QEC Code Properties Change)" --> Evap_EW
    Evap_EW -- "Requires increased boundary access" --> Evap_Boundary_Access
```

This leads to the firewall paradox, first proposed in 2012 by Almheiri and his collaborators. The paradox arises from a sharp conflict between three seemingly reasonable assumptions: (i) the process of black hole evaporation is unitary, meaning the Hawking radiation is in a pure state and entangled with the black hole's past; (ii) low-energy effective field theory is valid outside the horizon; and (iii) an infalling observer experiences nothing unusual at the horizon (the "no drama" principle). The monogamy of entanglement forbids a single quantum system (the late radiation) from being fully entangled with two separate systems (the early radiation and the interior partner modes) at once. This contradiction implies that one of the assumptions must be false, leading to the radical suggestion of a "firewall" of high-energy particles at the horizon [[15]](https://arxiv.org/html/2507.06046v1).

Quantum error correction offers a way out. Almheiri now thinks QEC is what stops firewalls from forming by protecting information as it crosses the horizon. In a 2018 paper, he reported that QEC is "essential for maintaining the smoothness of space-time at the horizon" of a wormhole. The idea is that strands of entanglement between the inside and outside of a black hole can be viewed as miniature wormholes (an idea known as ER=EPR), and QEC is how information escapes through them without violating locality at the horizon. This would resolve Hawking's paradox while keeping the horizon smooth [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

## Conclusion

The deep connection between holographic gravity and quantum error correction has sparked interest beyond theoretical physics. The U.S. Department of Defense is funding research into holographic codes, hoping that their geometric structure might lead to more efficient and robust QEC schemes for practical quantum computers [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

On the physics side, a major challenge remains: lifting these insights from the theoretical sandbox of AdS space to a realistic description of our own de Sitter universe. "The whole connection is known for a world that is manifestly not our world," as Scott Aaronson points out. Our universe has a positive cosmological constant and therefore lacks the clean spatial boundary that makes AdS holography so tractable. While researchers are making progress on primitive holographic descriptions of de Sitter space, the work is far less developed [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

Despite these challenges, the central lesson remains powerful. As John Preskill summarizes, entanglement is the fundamental ingredient that holds space together. "If you want to weave space-time together out of little pieces, you have to entangle them in the right way," he said. "And the right way is to build a quantum error-correcting code." This insight reframes our understanding of quantum information and the fabric of the cosmos, revealing a deep and unexpected connection [[2]](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103).

## References

- [1] [Bulk Locality and Quantum Error Correction in AdS/CFT](https://arxiv.org/abs/1411.7041)
- [2] [How Space and Time Could Be a Quantum Error-Correcting Code](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103)
- [3] [Quantum error correction - Wikipedia](https://en.wikipedia.org/wiki/Quantum_error_correction)
- [4] [Lecture 1: Introduction to Quantum Error Correction](https://people.eecs.berkeley.edu/~jswright/quantumcodingtheory24/scribe%20notes/lecture01.pdf)
- [5] [Threshold theorem - Wikipedia](https://en.wikipedia.org/wiki/Threshold_theorem)
- [6] [Quantinuum with partners Princeton and NIST deliver seminal result in quantum error correction](https://www.quantinuum.com/blog/quantinuum-with-partners-princeton-and-nist-deliver-seminal-result-in-quantum-error-correction)
- [7] [Quantum Computing Lecture 13](https://www.cl.cam.ac.uk/teaching/1920/QuantComp/Quantum_Computing_Lecture_13.pdf)
- [8] [Quantum error correction concepts](https://learn.microsoft.com/en-us/azure/quantum/concepts-error-correction)
- [9] [Quantum Error Correction: Bit-flip code](https://astro.pas.rochester.edu/~aquillen/phy265/lectures/QI_E.pdf)
- [10] [Albert Einstein, Holograms and Quantum Gravity](https://www.youtube.com/watch?v=IIHucC-HPz0)
- [11] [Holographic codes | Error Correction Zoo](https://errorcorrectionzoo.org/list/holographic)
- [12] [Quantum error correction and subregion duality](https://research.engineering.nyu.edu/~jbain/Talks/ST_QECC.pdf)
- [13] [HaPPY code - nLab](https://ncatlab.org/nlab/show/HaPPY+code)
- [14] [Pastawski-Yoshida-Harlow-Preskill (HaPPY) code](https://errorcorrectionzoo.org/c/happy)
- [15] [Black Holes: Complementarity or Firewalls?](https://arxiv.org/html/2507.06046v1)
</article>