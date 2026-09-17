# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What is Shor's 1995 quantum error-correcting code and threshold theorem?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://en.wikipedia.org/wiki/Threshold_theorem

Query: What is Shor's 1995 quantum error-correcting code and threshold theorem?

Answer: In quantum computing, the threshold theorem states that a quantum computer with a physical error rate below a certain threshold can suppress the logical error rate to arbitrarily low levels through quantum error correction. This result was proven independently by groups including Dorit Aharonov and Michael Ben-Or; Emanuel Knill, Raymond Laflamme, and Wojciech Zurek; and Alexei Kitaev. These results built on a paper of Peter Shor, which proved a weaker version of the threshold theorem. Surprisingly, the quantum threshold theorem shows that if the error to perform each gate is a small enough constant, one can perform arbitrarily long quantum computations to arbitrarily good precision, with only some small added overhead in the number of gates.

-----

Phase: [EXPLOITATION]

### Source [2]: https://en.wikipedia.org/wiki/Quantum_error_correction

Query: What is Shor's 1995 quantum error-correcting code and threshold theorem?

Answer: The Shor code, published in 1995, is the first quantum code that corrects a single Pauli error. It corrects for both bit flip and sign flip (phase flip) errors on a logical qubit. The Shor code uses 9 physical qubits to encode 1 logical qubit with distance 3. It can correct arbitrary single-qubit errors by handling combinations of bit or phase errors on a single qubit. The encoding uses three groups of qubits for bit flip correction and additional qubits for sign flip correction.

-----

Phase: [EXPLOITATION]

### Source [3]: https://people.eecs.berkeley.edu/~jswright/quantumcodingtheory24/scribe%20notes/lecture01.pdf

Query: What is Shor's 1995 quantum error-correcting code and threshold theorem?

Answer: In 1995, Shor discovered the 9-qubit code, which encodes a single logical qubit into 9 physical qubits to protect against noise. This gave a proof-of-concept that quantum noise could be overcome with error correction. One year later, Shor showed how to error-correct an entire quantum computation by compiling a general T-gate ideal quantum computation into a quantum circuit with poly(T) gates resilient to noise. In 1996/7, Kitaev, Aharonov and Ben-Or, and Knill, Laflamme, and Zurek improved on Shor’s result and proved the fault-tolerance/threshold theorem, showing compilation into a circuit of T · polylog(T) gates that can correct against constant levels of noise. The error rate p below which error correction kicks in is known as the threshold.

-----

Phase: [EXPLOITATION]

### Source [4]: https://www.quantinuum.com/blog/quantinuum-with-partners-princeton-and-nist-deliver-seminal-result-in-quantum-error-correction

Query: What is Shor's 1995 quantum error-correcting code and threshold theorem?

Answer: Peter Shor was the first to hypothesize a way forward in the form of quantum error correction. Building on his results, Dorit Aharanov and Michael Ben-Or proved that by concatenating quantum error correcting codes, a sufficiently high-quality quantum computer can suppress error rates arbitrarily at the cost of a very modest increase in the required number of qubits. Their results, now widely referred to as the “threshold theorem”, laid the foundation for realizing fault-tolerant quantum computing. The threshold theorem made clear that large scale quantum computing is a realistic possibility.

-----

Phase: [EXPLOITATION]

### Source [5]: https://errorcorrectionzoo.org/c/qecc

Query: What is Shor's 1995 quantum error-correcting code and threshold theorem?

Answer: The Shor code is the first quantum error-correcting code. It is listed as the Shor nine-qubit code, which corrects a single Pauli error using 9 qubits to encode 1 logical qubit with distance 3.

-----

</details>

<details>
<summary>How does the three-qubit bit-flip code encode logical states and extract syndromes?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://en.wikipedia.org/wiki/Quantum_error_correction

Query: How does the three-qubit bit-flip code encode logical states and extract syndromes?

Answer: The three-qubit bit-flip code, first proposed by Asher Peres in 1985, encodes the logical information of a single qubit into a highly entangled state of multiple physical qubits using entanglement and syndrome measurements to correct errors in a manner analogous to the classical repetition code. A phase-flip code is similarly constructed and is equivalent to the bit-flip code up to transversal Hadamard gates.

-----

Phase: [EXPLOITATION]

### Source [7]: https://www.cl.cam.ac.uk/teaching/1920/QuantComp/Quantum_Computing_Lecture_13.pdf

Query: How does the three-qubit bit-flip code encode logical states and extract syndromes?

Answer: The three-qubit bit-flip code encodes the computational basis states: |0⟩→|000⟩ |1⟩→|111⟩, achieved using a circuit that acts on an arbitrary qubit state (α |0⟩+ β |1⟩) |0⟩⊗2 →α |000⟩+ β |111⟩. To detect and recover errors, two ancillas are used for error detection via parity-check measurements. The syndrome extraction identifies single bit-flip errors without disturbing the logical state.

-----

Phase: [EXPLOITATION]

### Source [8]: https://learn.microsoft.com/en-us/azure/quantum/concepts-error-correction

Query: How does the three-qubit bit-flip code encode logical states and extract syndromes?

Answer: The three-qubit code encodes a single logical qubit into three physical qubits by repeating the qubit three times. The logical basis states are |0_L⟩ = |000⟩ and |1_L⟩ = |111⟩, so an arbitrary state |ϕ⟩ = α |0⟩ + β |1⟩ is encoded as |ϕ_L⟩ = α |000⟩ + β |111⟩. Two auxiliary qubits in |00⟩ are used to extract error information via CNOT gates for syndrome measurement without measuring the logical state directly.

-----

Phase: [EXPLOITATION]

### Source [9]: https://textbook.riverlane.com/en/latest/notebooks/ch2-classical-to-quantum-repcodes/bit-flip-repetition-codes.html

Query: How does the three-qubit bit-flip code encode logical states and extract syndromes?

Answer: A 3-qubit quantum repetition code encodes logical states similarly to classical: |0⟩_L = |000...⟩ and |1⟩_L = |111...⟩. Encoding uses a circuit with CNOT gates. Syndrome measurement is performed using additional syndrome qubits, applying CNOTs from data to syndrome qubits to detect bit-flip errors, followed by measurement of syndrome qubits to obtain the error syndrome.

-----

Phase: [EXPLOITATION]

### Source [10]: https://astro.pas.rochester.edu/~aquillen/phy265/lectures/QI_E.pdf

Query: How does the three-qubit bit-flip code encode logical states and extract syndromes?

Answer: The 3-bit bit-flip quantum error code encodes |0⟩ as |000⟩ and |1⟩ as |111⟩. A bit-flip error is described by Pauli-X operations. Syndrome measurement uses a circuit with two ancilla qubits, transforming |x0,x1,x2,0,0⟩ → |x0,x1,x2,x1+x2,x0+x2⟩. The bottom two ancilla qubits are measured to give the syndrome identifying which single bit flip occurred.

-----

</details>

<details>
<summary>What is the HaPPY tensor network code with pentagonal tiles for AdS geometry?</summary>

Phase: [EXPLOITATION]

### Source [11]: https://errorcorrectionzoo.org/c/happy

Query: What is the HaPPY tensor network code with pentagonal tiles for AdS geometry?

Answer: The HaPPY tensor network code uses pentagonal tiles for AdS geometry, encoding a holographic quantum error-correcting code based on perfect tensors. It models aspects of the AdS/CFT holographic duality and exhibits discretized Ryu-Takayanagi formula for entanglement entropy. To construct the encoding, one first uniformly tiles the hyperbolic AdS/CFT disc using pentagons and hexagons. Then, one places a 6-legged five-qubit encoding tensor at each hexagon and pentagon, contracting legs between neighboring shapes and leaving one leg uncontracted at each pentagon. This construction forms an encoding isometry from the uncontracted legs in the bulk to the uncontracted legs at the boundary. The single-qubit HaPPY code has a central pentagon encoding one bulk operator and hexagons tiling all other layers. The pentagon-hexagon HaPPY code has alternating layers of pentagons and hexagons in the tiling. The pentagon HaPPY code (a.k.a. the hyperbolic pentagon code, or HyPeC) consists of a purely pentagonal tiling.

-----

Phase: [EXPLOITATION]

### Source [12]: https://ncatlab.org/nlab/show/HaPPY+code

Query: What is the HaPPY tensor network code with pentagonal tiles for AdS geometry?

Answer: The hyperbolic pentagon code or HaPPY code is a quantum error correction code (a class of such codes really, indexed by a “cutoff” natural number) which is thought to exhibit characteristic properties akin to the encoding of bulk-quantum states by boundary-states expected in the AdS/CFT correspondence. In particular, the HaPPY code (or rather the tensor network that defines it) exhibits a discretized form of the Ryu-Takayanagi formula for holographic entanglement entropy. Concretely, the the HaPPY code subspace is the image of the linear map formed by: picking a perfect tensor of rank 6; picking a finite cutoff of the pentagonal tesselation of the hyperbolic plane; regarding its Poincaré dual graph as a tensor network (string diagram in finite-dimensional vector spaces) by assigning to each vertex at the center of the pentagons (show in blue), with 5 of its indices contracted with its neighbours in the hyperbolic plane, and its 6th uncontracted index remaining as an input (shown in red); regading the uncontrated edges at the cutoff boundary as output (shown in white) and thus as a linear map form the tensor product over the bulk-vertices to the tensor product over the edges sticking out over the boundary.

-----

Phase: [EXPLOITATION]

### Source [13]: https://real.mtak.hu/153229/1/2004.04173v4.pdf

Query: What is the HaPPY tensor network code with pentagonal tiles for AdS geometry?

Answer: the effective central charge of the boundary state, which leads to the restricted class of “allowed” discretized symmetry trans-formation described here. We expect qCFTs to appear on the boundary of all tensor network models on a regular bulk geometry [21, 25, 30, 39, 40], potentially including p-adic AdS/CFT models [41, 42]. From their construction on reg-ular tilings, these models necessarily inherit the discretely broken conformal symmetries we discussed, thus falling into the rubric of our proposed AdS/qCFT correspondence. The HaPPY pentagon code, studied here in its Majorana dimer form, shows that qCFTs are closely related to strongly disor-dered critical models, which have been extensively studied in the condensed matter literature [37, 43–47]. As the HaPPY code is a model of quantum error correction, we find that AdS/qCFT includes exact holographic codes, rather than the approximate codes found in AdS/MERA models . The similarity to strongly disordered models also suggests that boundary dynamics can be described by an effective local (though not nearest-neighbor) Hamiltonian, which would al-low for dynamical AdS/qCFT models. Further work should also explore the role of qCFT excitations, where the regu-lar symmetries of the tensor network are (locally) broken.

-----

Phase: [EXPLOITATION]

### Source [14]: https://www.nature.com/articles/s41467-023-42743-z

Query: What is the HaPPY tensor network code with pentagonal tiles for AdS geometry?

Answer: tiling with q > 3, such as the {4, 5} hyperbolic pentagon code introduced in Ref. 12."). HaPPY codes reproduce the AdS/CFT property of complementary recovery (Fig. 1) in that the greedy algorithm applied to a boundary region A and its complement Ac will terminate at the same cut through the tiling – the discretized Ryu-Takayanagi surface γA – for almost all choices of A. The union of the bulk regions a and ac that are recoverable from A and Ac, respectively, then fills the entire bulk. As described above, exact complementary recovery is expected from AdS/CFT at N → ∞, but creates problems for discrete holographic codes where code states are supposed to be related to CFTs and hence exhibit smoothly decaying correlation functions. A related problem arises when considering HaPPY codes from [...] dimensions (i.e., with qudits instead of qubits). While this model reproduces the quantum error correction properties of AdS/CFT up to bulk discretization artifacts, the boundary code space does not contain states that can be readily associated with physical CFT states. While the entanglement entropy scaling agrees with results for critical states12."),13."), the expected smooth polynomial decay of n-point correlation functions with distance is precluded by the code properties of the model; for example, simple spin-spin correlation functions such as \(\langle {X}\_{j}{X}\_{k}\rangle\) of Pauli X operators between sites j, k always vanish in the {4, 5} pentagon code, the standard example of a HaPPY code, as such operators are equivalent to correctable errors whose measurement cannot reveal [...] where \({{{{{{{{\mathcal{O}}}}}}}}}\_{A,B}\) are arbitrary Hermitian operators acting on A and B, respectively. In continuum AdS/CFT, physical correlation functions are restored by the subdominant bulk entropy term Sa into (1). In the HaPPY code picture, a nonzero bulk term requires logical bulk states with long-distance entanglement, resembling the entanglement structure of bulk quantum fields. However, due the discretization of the bulk space, such entanglement is not resolved on sizes below the curvature radius (the size of a single tile), while in continuum AdS/CFT this sub-cutoff entanglement would become part of the area term16."). As a result of this discretization, the code’s resilience against small errors makes logical bulk states inaccessible to small boundary operators,

-----

Phase: [EXPLOITATION]

### Source [15]: https://arxiv.org/html/2512.19452v3

Query: What is the HaPPY tensor network code with pentagonal tiles for AdS geometry?

Answer: Recently, a continuous network as a perfect tessellation of the background AdS geometry was constructed using the so-called partial-entanglement-entropy (PEE) threads Lin:2023rxc ; Lin:2024dho , which are bulk geodesics with a particular density distribution determined by the PEE structure of the boundary CFT. In such a network, the number of cuts along a surface exactly reproduces the area of this surface. In this work, we will develop three toy models of tensor network based on the PEE threads (or the PEE tensor network for short) in dd-dimensional Poincaré AdS space. The first one is the factorized PEE tensor network constructed via tensor product of EPR pairs. The second one is a HaPPY-like (Harlow-Pastawski-Preskill-Yoshida, Pastawski:2015qua ) tensor network constructed from perfect [...] The advantage of our HaPPY-like PEE tensor network is that, the greedy algorithm is performed exactly in the AdS space instead of some discrete graph, and the minimal homologous surface exactly matches the RT surface. Nevertheless, as in the HaPPY code, the above arguments only works for connected regions and for a time slice of AdS3.

-----

</details>

<details>
<summary>What is Preskill's robustness argument that space-time geometry is protected by QEC?</summary>

Phase: [EXPLOITATION]

### Source [16]: https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103

Query: What is Preskill's robustness argument that space-time geometry is protected by QEC?

Answer: John Preskill, a theoretical physicist at the California Institute of Technology, says quantum error correction explains how space-time achieves its “intrinsic robustness,” despite being woven out of fragile quantum stuff. “We’re not walking on eggshells to make sure we don’t make the geometry fall apart,” Preskill said. “I think this connection with quantum error correction is the deepest explanation we have for why that’s the case.” [...] “Quantum error correction gives us a more general way of thinking about geometry in this code language,” said Preskill, the Caltech physicist. The same language, he said, “ought to be applicable, in my opinion, to more general situations” — in particular, to a de Sitter universe like ours. But de Sitter space, lacking a spatial boundary, has so far proven much harder to understand as a hologram. [...] On the physics side, it remains to be seen whether de Sitter universes like ours can be described holographically, in terms of qubits and codes. “The whole connection is known for a world that is manifestly not our world,” Aaronson said. In a paper last summer, Dong, who is now at the University of California, Santa Barbara, and his co-authors Eva Silverstein and Gonzalo Torroba took a step in the de Sitter direction, with an attempt at a primitive holographic description. Researchers are still studying that particular proposal, but Preskill thinks the language of quantum error correction will ultimately carry over to actual space-time.

-----

Phase: [EXPLOITATION]

### Source [17]: https://www.youtube.com/watch?v=MuklWupCvWU

Query: What is Preskill's robustness argument that space-time geometry is protected by QEC?

Answer: that the holographic correspondence is a type of quantum error correcting code that when I think of a local operator in the bulk deep inside the ball which can be described on the boundary as a very nominal operator that corresponds to this feature of quantum codes that if I want to protect some encoded qubit using the code I should encode it in a very highly entangled form so the bulk degree of freedom which can be observed locally corresponds to some highly entangled encoding on the boundary which is very robust against error so the bulk geometry actually deep inside the bulk remains intact even if we introduce errors on the boundary there's a redundancy in the encoding which makes the geometry very robust and part of the reason I think that's exciting is that

-----

</details>

<details>
<summary>How does the reconstruction threshold shift to three-quarters at black-hole horizons per Almheiri?</summary>

Phase: [EXPLOITATION]

### Source [18]: https://indico.ift.uam-csic.es/event/9/attachments/26/36/Wall_Black_Hole_Thermodynamics.pdf

Query: How does the reconstruction threshold shift to three-quarters at black-hole horizons per Almheiri?

Answer: A. Almheiri, X. Dong, and D. Harlow, “Bulk Locality and Quantum Error Correction in AdS/CFT,” JHEP 04 (2015) 163, arXiv:1411.7041 [hep-th]. This paper discusses bulk locality and quantum error correction in AdS/CFT, foundational for understanding reconstruction thresholds at horizons. The reconstruction threshold shifts due to quantum error correction properties in the AdS/CFT correspondence, where the horizon acts as a boundary affecting operator reconstruction.

-----

Phase: [EXPLOITATION]

### Source [19]: https://www.osti.gov/pages/biblio/1803745

Query: How does the reconstruction threshold shift to three-quarters at black-hole horizons per Almheiri?

Answer: Bulk locality and quantum error correction in AdS/CFT163) Almheiri, Ahmed; Dong, Xi; Harlow, Daniel Journal of High Energy Physics, Vol. 2015, Issue 4 | journal | April 2015. This reference points to the Almheiri-Dong-Harlow work on quantum error correction, which explains shifts in reconstruction thresholds at black hole horizons to three-quarters due to entanglement wedge considerations.

-----

Phase: [EXPLOITATION]

### Source [20]: https://www2.yukawa.kyoto-u.ac.jp/~extremeuniverse/wpsite/wp-content/uploads/2022/10/KyotoOct2022.pdf

Query: How does the reconstruction threshold shift to three-quarters at black-hole horizons per Almheiri?

Answer: Reconstruction in AdS/CFT? AdS/CFT is a quantum error correcting code see work beginning with Almheiri, Dong, Harlow. How much of the bulk can we reconstruct from the state ρbdy of the nongravitational dual? The reconstruction threshold shifts in the context of entanglement wedges and quantum extremal surfaces near horizons.

-----

Phase: [EXPLOITATION]

### Source [21]: https://rojefferson.blog/2021/07/05/islands-behind-the-horizon

Query: How does the reconstruction threshold shift to three-quarters at black-hole horizons per Almheiri?

Answer: A. Almheiri, N. Engelhardt, D. Marolf, and H. Maxfield, “The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole,” JHEP 12 (2019) 063, arXiv:1905.08762. Discusses entanglement wedges at horizons, relevant to reconstruction thresholds shifting to three-quarters.

-----

Phase: [EXPLOITATION]

### Source [22]: https://arxiv.org/html/2507.06046v1

Query: How does the reconstruction threshold shift to three-quarters at black-hole horizons per Almheiri?

Answer: This setup with its null initial data is now simply the Python’s lunch of the partially evaporated black hole Brown et al. (2020); Engelhardt et al. (2022), so we are again consistent with principle 2. References Almheiri et al. (2013) on firewalls, but reconstruction involves non-isometric codes and complementarity at horizons.

-----

</details>

<details>
<summary>What is the three-qutrit toy code as minimal 2D hologram in Almheiri-Dong-Harlow 2014?</summary>

Phase: [EXPLOITATION]

### Source [23]: https://errorcorrectionzoo.org/list/holographic

Query: What is the three-qutrit toy code as minimal 2D hologram in Almheiri-Dong-Harlow 2014?

Answer: The three-qutrit toy code is a minimal 2D holographic model in the Almheiri-Dong-Harlow 2014 paper, representing a quantum error-correcting code. It encodes one logical qutrit in three physical qutrits, protecting against erasure of one qutrit. It is a [_3] Three-qutrit code, a prime-qudit CSS code that is the smallest qutrit stabilizer code to detect a single-qutrit error. It has stabilizer generators ZZZ and XXX. The code defines a quantum secret-sharing scheme and serves as a minimal model for the AdS/CFT holographic duality. It is also the smallest non-trivial instance of a quantum maximum distance separable code (QMDS), saturating the quantum Singleton bound.

-----

Phase: [EXPLOITATION]

### Source [24]: https://research.engineering.nyu.edu/~jbain/Talks/ST_QECC.pdf

Query: What is the three-qutrit toy code as minimal 2D hologram in Almheiri-Dong-Harlow 2014?

Answer: Example: 3 qutrit code (k = 1, n = 3, m = 2) - Encodes one logical qutrit in three physical qutrits. - Protects against erasure of one of the three physical qutrits by representing 3-qutrit operators that act entirely on HC as 2-qutrit operators. Almheiri et al. (2015) R1 R2 UR  R |ψ⟩ (k) |χ⟩ (n−k) (m−k) (n−m) Erasure-Protection QECC (i) n-qudit "physical" Hilbert space H(n)=HR (m)⊗H  R (n−m), where HR (m) and H  R (n−m) consist of m- and (n−m)-qudit states with support in R and  R. (ii) Map that encodes k "logical" qudits in "encoded logical" qudits of a "codespace" HC ⊂ H(n) in such a way that the former can be recovered if access is limited to some set R of m< n of the latter. Erasure-Protection QECC 9/15 2. ...and the QECC Interpretation Necessary and sufficient conditions for (ii) (a) QECC Condition: Any (n−m)-qudit operator on  R acts like a multiple of the identity on HC.

-----

Phase: [EXPLOITATION]

### Source [25]: https://ncatlab.org/nlab/show/quantum+error+correction

Query: What is the three-qutrit toy code as minimal 2D hologram in Almheiri-Dong-Harlow 2014?

Answer: A 3-qutrit code The following is a simple illustrative example from Cleve, Gottesman & Lo 99, p. 1-2: Consider a quantum system with a 3-dimensional space of quantum states: and consider a code space inside 3 copies of this space given by the following linear map This code corrects errors consisting of the loss of one of the three copies, in the following sense: There is a linear operator acting only on two of the three copies, explicitly given (ADH 14 (3.6)) by such that

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What mathematical barriers block lifting AdS holographic QEC to de Sitter cosmologies?</summary>

Phase: [EXPLORATION]

### Source [26]: https://beuke.org/ads-cft

Query: What mathematical barriers block lifting AdS holographic QEC to de Sitter cosmologies?

Answer: A fundamental limitation of the AdS/CFT correspondence is right in its name - the “AdS.” Our real universe, as far as observations indicate, has a positive cosmological constant and is expanding (accelerating, in fact), which means its large-scale geometry is closer to de Sitter (dS) space, not Anti-de Sitter. In de Sitter space, there is no timelike boundary at spatial infinity where one could easily imagine a CFT living; instead, de Sitter has horizons and a future boundary that is a moment in time. This raises the question: Does a correspondence like AdS/CFT exist for de Sitter space? And if not, what does that mean for applying holography to our cosmos? So far, AdS/CFT has been firmly established only for negatively curved spacetimes. It is not proven whether a similar duality exists for de Sitter space, and attempts to construct one face significant mathematical and conceptual challenges. Without a solid “gravity side” to start from, it’s hard to find the dual field theory. Another issue is that any would-be CFT dual to dS might have strange properties: for instance, studies indicate it might have an imaginary central charge (related to being non-unitary), suggesting that the usual rules of unitary quantum field theory might not apply. In other words, a naive dS/CFT dual could be a non-unitary CFT, which is a significant departure from the well-behaved unitary CFTs in AdS/CFT. These and other technical obstacles mean dS/CFT remains a conjectural, much less developed idea.

-----

Phase: [EXPLORATION]

### Source [27]: https://aayushayh.github.io/dSnote.pdf

Query: What mathematical barriers block lifting AdS holographic QEC to de Sitter cosmologies?

Answer: The case of AdS is somewhat more straightforward, partly due to the presence of a conformal boundary where one can study the bulk-boundary correspondence. In the case of de Sitter, such a conformal timelike boundary does not exist at spatial infinity – rather, the current statement of dS/CFT is that of some notion of holography from some Euclidean field theories that are live on some conformal boundaries in the late time slices; this presents some issues in regard to the quantities that were famously given a holographic description in the case of AdS/CFT, in particular that of entanglement entropy. To construct Hilbert space of de Sitter, we need to realize what are the (quantum) solutions of Wheeler-de Witt (WDW) equations for some asymptotically de Sitter with boundary conditions. The idea of Hilbert space being finite-dimensional is unique to de Sitter, as in flat-spacetime or AdS black hole, the Hilbert space is infinite-dimensional. One can argue that because of the phase space of gravitational solutions for not-so-precise boundary conditions in asymptotically de Sitter is compact. This results in the finite-dimensional Hilbert space. For symmetries in de Sitter, out first sight is the (bulk) isometry group for de Sitter metric, which is a semi-simple Lie group SO(D, 1).

-----

Phase: [EXPLORATION]

### Source [28]: https://physics.stackexchange.com/questions/364858/holography-on-non-ads-spacetime

Query: What mathematical barriers block lifting AdS holographic QEC to de Sitter cosmologies?

Answer: One can also study extrapolate to dS by analytically continuing \(\ell^2 \to - \ell^2\). This has also been done in some interesting cases, but there are several issue with taking this too seriously. The holographic principle is in principle independent of AdS. The AdS/CFT correspondence is just a realization of it. So one might hope that it holds beyond AdS. I think that the questions of whether it is possible to formulate holography in flat or dS spacetime should receive much more attention than what it does now.

-----

</details>

<details>
<summary>How does operator algebra QEC precisely protect bulk geometry from Planck-scale boundary fluctuations?</summary>

Phase: [EXPLORATION]

### Source [30]: https://people.tamu.edu/~monicak/talks.html

Query: How does operator algebra QEC precisely protect bulk geometry from Planck-scale boundary fluctuations?

Answer: I will present a novel operator-algebraic formalism that captures how the algebra of local operators in a quantum field theory encodes (geometric) information about spacetime regions. In AdS/CFT, bulk reconstruction and relative entropy conservation can be rephrased in this algebraic framework, highlighting their relations, and finds the quantum error correcting structure in the holographic spacetime. Motivated by a kink transform conjecture of Bousso et. al. on the bulk AdS description of boundary cocycle flow, I will characterize (approximate) complementary recovery in terms of (approximate) intertwining of bulk and boundary cocycle derivatives. This suggests that from algebraic perspective, the kink transform is precisely the bulk cocycle flow, which provides the bulk geometry via geometric modular action and the notion of time. I will further show using this new formalism that the aforementioned complementary recovery holds for Weyl algebras of Klein-Gordon fields in AdS wedges, yielding an operator algebraic version of subregion-subregion duality.

-----

</details>

<details>
<summary>Why do discrete holographic codes generically violate expected smooth CFT correlation functions?</summary>

Phase: [EXPLORATION]

### Source [34]: https://www.nature.com/articles/s41467-023-42743-z

Query: Why do discrete holographic codes generically violate expected smooth CFT correlation functions?

Answer: Discrete holographic codes violate expected smooth CFT correlation functions due to their non-local, error-correcting nature, which prevents smooth decay of correlations. This discrepancy arises because holographic codes are designed for error correction, not smooth polynomial decay typical of CFTs.

-----

Phase: [EXPLORATION]

### Source [35]: https://authors.library.caltech.edu/records/exhqw-01m91

Query: Why do discrete holographic codes generically violate expected smooth CFT correlation functions?

Answer: Discrete holographic codes violate expected smooth CFT correlation functions due to their non-local, error-correcting nature, which prevents smooth decay of correlations. This discrepancy arises because holographic codes are designed for error correction, not smooth polynomial decay typical of CFTs.

-----

</details>

<details>
<summary>What new tensor-network constructions from holographic principles yield higher fault-tolerant thresholds than stabilizer codes?</summary>

Phase: [EXPLORATION]

### Source [36]: https://arxiv.org/html/2408.06232v3

Query: What new tensor-network constructions from holographic principles yield higher fault-tolerant thresholds than stabilizer codes?

Answer: Holographic tensor networks, specifically hyperinvariant tensor networks (HTN), yield higher fault-tolerant thresholds than stabilizer codes. HTNs achieve this by producing correct boundary correlation functions and enabling fault-tolerant logical operations. Holographic codes exhibit high resilience against various noise channels. It was first shown that holographic quantum error correction codes exhibit high thresholds against the quantum erasure channel; subsequently, several works have shown the high thresholds of holographic codes against depolarizing noise. The most widely studied instances of holographic codes also fall into the category of stabilizer codes, despite some restrictions on their representation of holographic dualities and the possibility to construct more sophisticated non-stabilizer or even approximate holographic codes. We shall therefore limit ourselves to stabilizer versions of holographic codes in the present work. Recent work has also made progress on lowering the computational complexity of decoding itself using tensor-network schemes. These techniques, along with the high thresholds of holographic codes, make them promising candidates for practical quantum error correction.

-----

Phase: [EXPLORATION]

### Source [37]: https://www.nature.com/articles/s41467-023-42743-z

Query: What new tensor-network constructions from holographic principles yield higher fault-tolerant thresholds than stabilizer codes?

Answer: Holographic codes from hyperinvariant tensor networks. As HTN codes break exact complementary recovery, it will be interesting to explore whether restrictions on HaPPY codes regarding fault-tolerant logical operations using boundary transversal gates still apply in this new setting. A holographic code relating local boundary to local bulk time evolution, potentially realizable by an HTN code, would also have a number of useful features regarding non-local quantum computation. Another interesting question is whether HTN codes also support non-stabilizer subsystem codes such as those constructed in Ref. 20, and how this affects state dependence. Holographic quantum-error correcting codes are models of bulk/boundary dualities such as the anti-de Sitter/conformal field theory (AdS/CFT) correspondence, where a higher-dimensional bulk geometry is associated with the code’s logical degrees of freedom. Previous discrete holographic codes based on tensor networks have reproduced the general code properties expected from continuum AdS/CFT, such as complementary recovery. However, the boundary states of such tensor networks typically do not exhibit the expected correlation functions of CFT boundary states. In this work, we show that a new class of exact holographic codes, extending the previously proposed hyperinvariant tensor networks into quantum codes, produce the correct boundary correlation functions. This approach yields a dictionary between logical states in the bulk and the critical renormalization group flow of boundary states. Furthermore, these codes exhibit a number of useful features regarding non-local quantum computation.

-----

Phase: [EXPLORATION]

### Source [38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10640591

Query: What new tensor-network constructions from holographic principles yield higher fault-tolerant thresholds than stabilizer codes?

Answer: Holographic codes from hyperinvariant tensor networks. For the case of tensor networks without logical degrees of freedom, i.e., representations of holographic states rather than codes, the problem of non-trivial primary operators was resolved in Ref. 22 with the introduction of hyperinvariant tensor networks (HTN). This class of tensor networks has the same geometry as HaPPY codes, i.e., are constructed on a regular {p, q} hyperbolic tiling, with a q-leg vertex tensor A placed on each vertex. In addition, for each edge a 2-leg edge tensor B is contracted between two vertex tensors. For the choice of perfect A and a splittable B = U U T with unitary U (in particular, B = U = 1), this construction just corresponds to a HaPPY code with the logical bulk projected onto a product state. However, HTNs allow for more general choices of A. Holographic quantum-error correcting codes are models of bulk/boundary dualities such as the anti-de Sitter/conformal field theory (AdS/CFT) correspondence, where a higher-dimensional bulk geometry is associated with the code’s logical degrees of freedom. Previous discrete holographic codes based on tensor networks have reproduced the general code properties expected from continuum AdS/CFT, such as complementary recovery. However, the boundary states of such tensor networks typically do not exhibit the expected correlation functions of CFT boundary states. In this work, we show that a new class of exact holographic codes, extending the previously proposed hyperinvariant tensor networks into quantum codes, produce the correct boundary correlation functions. This approach yields a dictionary between logical states in the bulk and the critical renormalization group flow of boundary states. Furthermore, these codes exhibit a number of useful features regarding non-local quantum computation.

-----

</details>

<details>
<summary>Connections between holographic QEC and quantum spin liquids?</summary>

Phase: [EXPLORATION]

### Source [39]: https://indico.global/event/15522/contributions/140949/attachments/65726/127087/ISM%20talk%20Jahn.pdf

Query: Connections between holographic QEC and quantum spin liquids?

Answer: Holographic quantum error-correcting codes model finite-N holography and feature error thresholds, tunable rates, and logical fault tolerance protocols. Connections include bulk gauge-fixing to code rates, state dependence to non-stabilizer codes, and bulk inhomogeneity to fault tolerance. The HaPPY code uses perfect tensors, such as the five-qubit Laflamme code for 6-leg tensors, where each tensor acts as a QEC code. These models explore quantum information in quantum gravity contexts.

-----

Phase: [EXPLORATION]

### Source [43]: https://quantum-journal.org/papers/q-2025-08-08-1826

Query: Connections between holographic QEC and quantum spin liquids?

Answer: References discuss holographic quantum error-correcting codes, including Majorana dimers and holographic QEC codes, Calderbank-Shor-Steane holographic codes, and reviews on holographic tensor network models and QEC. Related works cover approximate Bacon-Shor codes and holography, linking tensor networks to error correction in holographic contexts.

-----

</details>

<details>
<summary>Historical path from black hole thermodynamics to holographic QEC?</summary>

Phase: [EXPLORATION]

### Source [44]: https://arxiv.org/html/2507.03778v2

Query: Historical path from black hole thermodynamics to holographic QEC?

Answer: Between 1972 and 1975, Jacob Bekenstein proposed that black holes possess entropy proportional to their horizon area, and Stephen Hawking derived this relationship from semiclassical quantum field theory in curved spacetime, predicting thermal radiation from black holes. These developments established black hole thermodynamics as a formal framework connecting general relativity, quantum mechanics, and statistical physics. However, this synthesis rests on approximations whose validity remains unproven in regimes where quantum gravitational effects become important. This article provides a detailed overview of the historical development from 1972 to 1975 and surveys modern proposals, such as the holographic principle and gravitational path integrals.

-----

Phase: [EXPLORATION]

### Source [45]: https://rojefferson.blog/2020/03/07/black-hole-thermodynamics-quantum-puzzles-and-the-holographic-principle

Query: Historical path from black hole thermodynamics to holographic QEC?

Answer: Classically, black hole thermodynamics is a formal analogy between black holes and statistical thermodynamics. It was originally put forth by Jacob Bekenstein in his landmark 1973 paper, in which he proposed treating black holes thermodynamically, and argued that the entropy should be proportional to the area of the event horizon. The most remarkable and far-reaching consequence of the black hole investigations is the holographic principle. Put forth by ‘t Hooft, and given a formulation in terms of string theory by Susskind, this is essentially the statement that the ultimate theory of quantum gravity must exhibit a dimensional reduction in the number of fundamental degrees of freedom. This developed from the arguments of Bekenstein, that the black hole entropy represents a bound on the amount of information that can be localized within any given region.

-----

Phase: [EXPLORATION]

### Source [46]: https://www.physics.umd.edu/grt/taj/776b/lectures.pdf

Query: Historical path from black hole thermodynamics to holographic QEC?

Answer: Classical black hole physics cries out for the incorporation of ħ effects, so the thermodynamic “analogy” can become true thermodynamics. Since general relativity is relativistic, it is not quantum mechanics but relativistic quantum field theory that is called for. An alternate semiclassical approach—and historically the first— is to consider quantum fields in a fixed black hole background. The historical route to Hawking’s discovery is worth mentioning. After the Penrose process was invented, it was only a short step to consider a similar process using waves rather than particles, a phenomenon dubbed “super-radiance”. Quantum mechanically, super-radiance corresponds to stimulated emission, so it was then natural to ask whether a rotating black hole would spontaneously radiate.

-----

Phase: [EXPLORATION]

### Source [47]: https://indico.global/event/15522/contributions/140949/attachments/65726/127087/ISM%20talk%20Jahn.pdf

Query: Historical path from black hole thermodynamics to holographic QEC?

Answer: Holographic QEC The first such model was the HaPPY code. [Harlow/Pastawski/Preskill/Yoshida ’15] We can build finite-dimensional models of holographic codes using a tensor networks (TN) with hyperbolic geometry. With bulk and boundary legs, the TN defines an encoding V : |ψbdy⟨= V |Φbulk⟨. Each tensor Tijklmn is chosen as a perfect tensor: Any inner product over at least half the indices yields the identity. For the example of 6-leg tensors and spins/qubits, each tensor is itself a QEC code: The five-qubit Laflamme code. A holographic code is defined from the isometry V : Hbulk → Hbdy, where Hbulk is restricted to low-energy bulk states around semiclassical AdS.

-----

Phase: [EXPLORATION]

### Source [48]: https://en.wikipedia.org/wiki/Black_hole_thermodynamics

Query: Historical path from black hole thermodynamics to holographic QEC?

Answer: The fact that the black hole entropy is also the maximal entropy that can be obtained by the Bekenstein bound (wherein the Bekenstein bound becomes an equality) was the main observation that led to the holographic principle. This area relationship was generalized to arbitrary regions via the Ryu–Takayanagi formula, which relates the entanglement entropy of a boundary conformal field theory to a specific surface in its dual gravitational theory. In the early 1990's Gerard 't Hooft and Leonard Susskind generalized the relationship between a black hole's surface area and its entropy, applying to all of spacetime. This was an early form of the holographic principle, a universal relationship between geometry and information.

-----

</details>

<details>
<summary>Influence of holographic QEC on quantum sensing and metrology?</summary>

Phase: [EXPLORATION]

### Source [49]: https://www.phys.ethz.ch/news-and-events/d-phys-news/2022/04/the-side-effects-of-quantum-error-correction-and-how-to-cope-with-them.html

Query: Influence of holographic QEC on quantum sensing and metrology?

Answer: Holographic quantum error correction (QEC) enhances quantum sensing and metrology by suppressing noise and improving precision, though it can introduce biases that need correction. It enables practical high-precision quantum sensors. In applying QEC to quantum sensing, errors are repeatedly corrected as the sensor acquires information about the target quantity. The benefits of error-corrected quantum sensing come with major potential side effects. In realistic settings QEC can distort the output of quantum sensors and might even lead to unphysical results. This QEC-induced bias matters. If unaccounted for, estimates for the minimum signal that the quantum sensor can detect might end up being overly optimistic. The team provides an escape route to overcome the bias. The amount of bias introduced by the finite-rate QEC can be calculated, and through appropriate measures be rectified in post-processing so that the sensor output makes again perfect sense. Factoring in that the QEC can give rise to systematic bias can help to devise the ideal sensing protocol ahead of the measurement.

-----

Phase: [EXPLORATION]

### Source [53]: https://ncatlab.org/nlab/show/quantum+error+correction

Query: Influence of holographic QEC on quantum sensing and metrology?

Answer: There are a number of reasons to suspect that holographic codes may be of practical use for quantum computing. Quantum error correction ensures robustness of quantum computation against noise and quantum decoherence by correcting errors as they occur at runtime. Further discussion of holographic quantum error correcting codes.

-----

</details>

<details>
<summary>Links between holographic QEC and categorical quantum mechanics?</summary>

Phase: [EXPLORATION]

### Source [56]: https://arxiv.org/html/2410.22861v1

Query: Links between holographic QEC and categorical quantum mechanics?

Answer: A quantum error correction (QEC) code is a technique used to protect information at the level of physical qubits (or qudits) from deleterious environmental noise effects. Such protection is accomplished by redundantly mapping physical qubit states into subspaces of a larger, multipartite Hilbert space; this description at the level of an encoding isometry effectively defines a QEC code. Holographic codes are a recent class of QEC subsystem codes derived from holographic bulk/boundary dualities. In addition to exploring the physics of such dualities, these codes possess useful QEC properties such as tunable encoding rates, distance scaling competitive with topological codes, and excellent recovery thresholds. Holographic quantum codes are a recently introduced class of quantum error correction codes, derived as models of bulk/boundary dualities in theoretical physics, in particular the AdS/CFT correspondences. The main idea for these codes lies in the fact that bulk degrees of freedom, which are associated with logical qubits in d dimensions, are mapped to a (d-1)-dimensional boundary, with the hyperbolic structure of the bulk ensuring that the physical Hilbert space is larger than its logical counterpart.

-----

Phase: [EXPLORATION]

### Source [57]: https://arxiv.org/abs/1503.06237

Query: Links between holographic QEC and categorical quantum mechanics?

Answer: Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence. Comments: 40 Pages + 25 Pages of Appendices. 38 figures. Subjects: High Energy Physics - Theory (hep-th); Quantum Physics (quant-ph). Journal reference: JHEP 06 (2015) 149.

-----

Phase: [EXPLORATION]

### Source [58]: https://ncatlab.org/nlab/show/quantum+error+correction

Query: Links between holographic QEC and categorical quantum mechanics?

Answer: Quantum error correction is concerned with ensuring the robustness of quantum computation against noise (as in classical error correction) and particularly against quantum noise and quantum decoherence (e.g. against bit flip errors), by “correcting errors as they occur” at runtime. Via holographic tensor networks. Relation of quantum error correcting codes to the Monster vertex operator algebra and more generally to 2d SCFT and string theory: Jeffrey A. Harvey, Gregory W. Moore, Moonshine, Superconformal Symmetry, and Quantum Error Correction, J. High Energ. Phys. 2020, 146 (2020). (arXiv:2003.13700). In relation to the large N limit: Alexey Milekhin, Quantum error correction and large N (arXiv:2008.12869). In relation to renormalization group flow: Keiichiro Furuya, Nima Lashkari, Mudassir Moosa, Renormalization group and approximate error correction (arXiv:2112.05099). In relation to fixed-point path integrals.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="beuke-org.md">
<details>
<summary>beuke.org</summary>

Phase: [EXPLORATION]

**Source URL:** <https://beuke.org/ads-cft>

# beuke.org

AdS/CFT Correspondence

A Non-Perturbative Formulation of String Theory

The AdS/CFT correspondence is a conjectured equivalence (duality) between two very different types of physical theories: a gravitational theory in a higher-dimensional Anti-de Sitter (AdS) spacetime, and a conformal field theory (CFT) living on the boundary of that AdS space.[\[5\]](https://beuke.org/ads-cft/#fn:5) In simple terms, it asserts that physics inside a bulk AdS universe (with gravity) is exactly equivalent to the physics of a lower-dimensional quantum field theory without gravity defined on the boundary of that universe. This duality is often called a gauge/gravity duality or holographic duality, because a gauge theory (like a Yang-Mills CFT) on the boundary is dual to a gravity theory in the bulk.[\[3\]](https://beuke.org/ads-cft/#fn:3) The correspondence provides a dictionary between the two: every object or phenomenon in the AdS bulk (e.g. a particle or a black hole) corresponds to some entity in the boundary CFT, and vice versa. Despite the theories living in different numbers of dimensions and looking very different, they contain the same information and physical content - they are in fact identical in all their predictions when the duality holds.

AdS/CFT is a concrete realization of the holographic principle in physics. The holographic principle, first suggested by Gerard 't Hooft and Leonard Susskind in the 1990s, posits that all the information contained in a volume of space can be described by data on the boundary of that space.[\[6\]](https://beuke.org/ads-cft/#fn:6) An analogy is a ordinary optical hologram: a 2D film can encode a fully three-dimensional image. Similarly, in AdS/CFT the CFT on the two-dimensional boundary encodes everything about the three-dimensional (or higher-dimensional) AdS bulk. In fact, AdS/CFT is often described as a “holographic duality” because the relationship between the bulk and boundary is like that of a 3D object and its 2D hologram. The boundary theory is like a hologram that captures information about the higher-dimensional bulk gravity theory. In short, gravity in AdS spacetime is holographically encoded by a field theory on the boundary. This idea revolutionizes how we think about space and gravity: the correspondence suggests that the familiar concept of a spatial volume with gravity can emerge from a lower-dimensional, gravity-free quantum system. The AdS/CFT duality gave a precise example of holography at work, showing that the number of degrees of freedom in a region of space truly scales with the area of its boundary and not its volume (exactly as 't Hooft and Susskind had anticipated).

A useful way to visualize AdS spacetime is as a cylindrical shape, where the upward direction represents the progression of time, and each horizontal cross-section corresponds to a spatial snapshot at a specific moment. In this representation, the associated conformal field theory (CFT) can be thought of as residing on the boundary of the cylinder. Notably, this boundary has one dimension less than the interior, often referred to as the “bulk.”[\[7\]](https://beuke.org/ads-cft/#fn:7)

https://beuke.org/images/boundary.png

### Historical and Theoretical Context

The AdS/CFT correspondence was first proposed by Argentine physicist Juan Maldacena in 1997 (published early 1998) in a groundbreaking paper that has since become one of the most influential in theoretical physics.[\[4\]](https://beuke.org/ads-cft/#fn:4) Maldacena’s work was inspired by earlier ideas of holography and by results in string theory. He considered a specific scenario in string theory and conjectured a duality between a 5-dimensional AdS spacetime and a 4-dimensional CFT on its boundary. In particular, he showed that under certain conditions (including a high degree of supersymmetry), Type IIB string theory on an AdS5 × S5 background is dual to a 4D CFT (known as N=4 supersymmetric Yang-Mills theory) living on that AdS boundary.[\[3\]](https://beuke.org/ads-cft/#fn:3) This was the first concrete example of a “holographic universe.” Maldacena’s proposal had an immediate and enormous impact: it provided a tangible framework to unite quantum field theory and quantum gravity. The discovery was so remarkable that it kicked off an explosion of research; indeed, Maldacena’s paper is among the most highly cited physics papers ever. By the 2010s, many physicists regarded AdS/CFT as one of the most exciting discoveries in modern theoretical physics. It not only advanced string theory but also offered new tools to tackle problems in other areas of physics.

The AdS/CFT idea emerged from developments in string theory and black hole thermodynamics in the 1990s. In the 1970s, studies of black hole entropy by Bekenstein and Hawking revealed that a black hole’s entropy is proportional to the area of its event horizon, not its volume, hinting that the information content of a region might reside on its surface. Building on this, 't Hooft and Susskind formulated the holographic principle: the maximal information (or entropy) inside a volume scales with the area of its boundary.[\[6\]](https://beuke.org/ads-cft/#fn:6) This principle suggested a radical way to reconcile quantum mechanics and gravity by reducing the effective degrees of freedom. Meanwhile, string theorists had found that certain configurations of [D-branes](https://beuke.org/branes) could be used to count the microstates of black holes, reproducing the Bekenstein-Hawking entropy formula - a major success indicating that string theory knows about black hole thermodynamics. Maldacena’s insight was to consider the low-energy physics of a stack of D3-branes in two complementary ways: one way yields a gauge theory (a type of CFT) on the branes, and the other yields a supergravity (gravity) solution in the near-horizon region of those branes, which is AdS5 × S5.[\[2\]](https://beuke.org/ads-cft/#fn:2) He realized that these two descriptions must actually be the same physics - hence a duality between the gravity theory and the gauge theory. In essence, the holographic principle was realized in the context of string theory, tying together stringy descriptions of black holes and quantum field theories. Maldacena’s 1997 proposal thus grew directly out of attempts to understand black holes in string theory and gave precise form to Susskind’s holographic ideas. Leonard Susskind himself later remarked that Maldacena’s result brought the holographic principle “to center stage” by providing an actual working example.

AdS/CFT became a crucial element in the broader web of string theory dualities. In the mid-1990s, string theorists discovered that the five distinct string theories were related by dualities and were all part of a single 11-dimensional framework dubbed M-theory. The holographic duality fits naturally into this picture. For one, the AdS/CFT correspondence often involves M-theory backgrounds as well - for example, one version of AdS/CFT states that M-theory on AdS7 × S4 is dual to a 6-dimensional CFT (the so-called (2,0) theory). Another involves M-theory on AdS4 × S7 dual to a 3D superconformal field theory (known as the ABJM theory).[\[4\]](https://beuke.org/ads-cft/#fn:4) These examples show that the correspondence isn’t limited to the specific case Maldacena originally studied, but extends to other dimensions and systems, including those arising from M-theory. More generally, the success of AdS/CFT reinforced the idea that all consistent formulations of quantum gravity (such as string theories and M-theory) obey holographic dualities, differing perhaps only in details. It also hinted at a unifying principle: if every quantum gravity theory has an equivalent lower-dimensional description, holography might be a fundamental organizing principle of M-theory itself. Many theorists now suspect that the holographic principle is a fundamental pillar of M-theory and that AdS/CFT is one manifestation of a more general holographic framework uniting all string theories.

### Conceptual Mechanics

Anti-de Sitter space is a model of a universe with constant negative curvature (the opposite of the positively curved de Sitter space that approximates our universe). In practice, AdS can be visualized in lower dimensions to build intuition. For example, a 2D AdS space can be thought of as a hyperbolic disk - a geometric surface where distances are defined in a funny way so that the edge of the disk is infinitely far away. If you “stack” such disks to add a time dimension, you get a cylinder-like AdS spacetime.[\[3\]](https://beuke.org/ads-cft/#fn:3) A key feature of AdS is that it has a boundary at spatial infinity. In AdS, unlike flat Minkowski space, signals or objects can reach the boundary in finite time, and the boundary acts like a timelike surface encasing the bulk. Intuitively, AdS space behaves somewhat like a gravitational “box” - its negative curvature tends to focus light and pull things back inward. A photon emitted from the center of AdS will travel outwards but eventually slow and return, as if there were reflecting walls at infinity. In contrast, Minkowski space (the flat spacetime of special relativity with zero curvature) has no boundary at infinity - an object can travel arbitrarily far away. And de Sitter (dS) space, with positive curvature (like an expanding sphere), doesn’t have a spatial boundary at infinity; instead it has horizons - one can only see out to a certain distance before space recedes too quickly. In de Sitter space (which resembles our universe with a positive cosmological constant), you cannot send a signal to “infinity” and back, whereas in AdS you effectively can due to its curved geometry. The exotic nature of AdS - a space where time and space are curved in strange ways - is crucial: it provides that outer boundary on which a dual CFT can live. In summary, AdS is a gravitational spacetime with a finite boundary that sits at infinity, enabling the peculiar setup of a holographic dual theory living on that boundary. Our real universe, by contrast, seems to be more like a de Sitter space, which is one reason why applying AdS/CFT to reality is non-trivial.

A conformal field theory is a type of quantum field theory (QFT) with extra symmetry: it is invariant under conformal transformations, which are essentially shape-preserving (angle-preserving) transformations including scaling. This means a CFT has no inherent length scale - if you zoom in or out, the physics looks the same. Such theories arise in various contexts: for example, the theory describing a system exactly at a critical phase transition in condensed matter physics is often a CFT (where it has scale invariance). In high-energy physics, an important example of a CFT is N=4 supersymmetric Yang-Mills theory in 4 dimensions, which is the prototype CFT in Maldacena’s duality.[\[5\]](https://beuke.org/ads-cft/#fn:5) It’s a gauge theory (somewhat like an idealized version of QCD without a scale that breaks conformal symmetry) and has a high degree of symmetry (super-symmetry and conformal symmetry). CFTs are “nice” QFTs in that they are often mathematically well-behaved and highly symmetric. In string theory, 2D conformal field theories also describe the worldsheet dynamics of strings. In AdS/CFT, the conformal field theory typically has one fewer spatial dimension than the AdS bulk. For instance, a 5D AdS bulk corresponds to a 4D CFT on its boundary. The significance of the CFT side is that it does not contain gravity - it’s an ordinary quantum field theory (e.g. a theory of particles and fields similar to the Standard Model, though with special symmetries). This is part of the magic: the correspondence says a quantum theory without gravity can be equivalent to a gravity theory, provided the spacetime is AdS. Importantly, many calculations that are hard to do directly in a strongly interacting field theory can become easier via the dual gravity description, and vice versa - the two sides complement each other.

The heart of AdS/CFT is the bulk-boundary correspondence: every phenomenon in the AdS bulk spacetime has a corresponding description on the boundary and vice versa. One useful analogy is to think of the boundary CFT as a kind of optical hologram of the bulk. Just as a 2D holographic plate encodes a 3D image, the 2D (or lower-dimensional) CFT encodes the 3D (or higher-dimensional) bulk physics.[\[7\]](https://beuke.org/ads-cft/#fn:7) To illustrate, Juan Maldacena described the duality in terms of “shadows”: the string theory in the interior of AdS has a “shadow” on the boundary which is the field theory. “Every fundamental particle in the interior has its counterpart on the boundary, and every interaction between interior particles corresponds exactly to an interaction between boundary particles,” Maldacena explains. If you drop an apple in the AdS bulk, an observer equipped with the boundary CFT could describe the apple’s fall entirely in boundary terms. In fact, one could “ignore the interior altogether without losing any information at all - this world is a true hologram.” The bulk gravity (including possibly curving spacetime, black holes forming, etc.) is encoded in the patterns of quantum fields on the boundary. The boundary is where the CFT lives, and it serves as the screen on which the bulk is projected. This means that if you know the state of the CFT exactly, you know everything about the AdS bulk state. Gravity, particles, even spacetime geometry in the AdS can be “read off” from the boundary data. In Maldacena’s toy model universe, gravity is an emergent illusion - it emerges for an observer in the bulk, but fundamentally all the dynamics can be described by a gravity-free quantum theory on the boundary. This bulk-boundary mapping is precise and quantitative in AdS/CFT. For example, one can compute how a disturbance in the CFT (say, injecting some energy at a certain point) corresponds to creating a particle that propagates in the AdS bulk.[\[2\]](https://beuke.org/ads-cft/#fn:2) Correlation functions in the CFT are related to interactions in the bulk, and the geometry of AdS itself is reflected in properties of the CFT. In short, the AdS/CFT correspondence provides a holographic “dictionary” translating bulk physics to boundary physics. This idea has deep implications: it suggests spacetime and gravity can be built out of more fundamental non-gravitational degrees of freedom on a lower-dimensional boundary. It’s a striking realization of the holographic principle and offers an entirely new perspective on what spacetime means in quantum gravity.

### Physical Implications and Applications

AdS/CFT is a major step toward reconciling quantum mechanics with general relativity because it gives a concrete example of a quantum theory of gravity. On the AdS side, we have a gravity theory (often a low-energy limit of string theory) which is conjecturally exactly equivalent to the CFT, a standard quantum field theory. This means any question about quantum gravity (usually a very hard problem) can in principle be translated to a question about quantum field theory (which we understand much better in many cases).[\[5\]](https://beuke.org/ads-cft/#fn:5) It provides a non-perturbative definition of a quantum gravity theory: instead of trying to quantize gravity directly (which historically led to problems), AdS/CFT says “here is a gravity theory - it’s nothing but this well-defined quantum field theory, just rewritten.” In Maldacena’s model, the boundary CFT is a complete quantum description of everything happening in the bulk, including gravity. This example strongly suggests that gravity (at least in a negatively curved universe) does not contradict quantum mechanics - instead, it emerges from quantum mechanics in one lower dimension. For theoretical physicists, this was a proof-of-concept that the long-sought unification of quantum mechanics and general relativity is possible: one can have a theory that is simultaneously a quantum theory and equivalent to a classical gravity theory (in different regimes). It’s often said that in AdS/CFT, the gravitational force and spacetime curvature in the bulk are “coded” into the quantum behavior of the boundary fields, demonstrating how geometry can emerge from quantum degrees of freedom. This has fueled the idea that spacetime itself is emergent and fundamentally holographic. While AdS/CFT is a model and not our real universe, it offers a testing ground for quantum gravity ideas - a place where one can safely study and resolve conceptual problems that arise when combining GR and QM.

One of the most celebrated implications of AdS/CFT is in understanding black holes. In the duality, a black hole in the AdS bulk corresponds to a certain high-energy state (a thermal state) in the boundary CFT.[\[3\]](https://beuke.org/ads-cft/#fn:3) Thus, the mysterious thermodynamic properties of black holes can be translated into ordinary statistical physics of the CFT. For instance, the Bekenstein-Hawking entropy of a black hole (proportional to the horizon area) should equal the entropy of the corresponding ensemble of states in the CFT. Indeed, in many cases researchers have shown that the number of degrees of freedom in the CFT matches the area law, providing a microscopic explanation for black hole entropy. Rather than viewing a black hole as a breakdown of physics where information might be lost, AdS/CFT assures us that no information is actually lost. The black hole information paradox - the puzzle of whether information that falls into a black hole can ever get out - finds a natural resolution in AdS/CFT. From the boundary perspective, everything is manifestly unitary (quantum evolution on the boundary respects information conservation), so the formation and evaporation of a black hole in AdS must also be unitary.[\[6\]](https://beuke.org/ads-cft/#fn:6) As one physicist put it, “there is a dual description in which unitary evolution is automatic,” meaning that even though Hawking’s original calculations suggested information destruction, the dual CFT cannot lose information, so neither can the black hole. This convinced many that black holes do not actually destroy information and that any paradox is an artifact of viewing the process only from the gravity side. However, AdS/CFT does more than resolve the yes/no question of information loss - it provides tools to compute how information might be encoded in Hawking radiation in principle. Recent cutting-edge research into black hole evaporation and quantum entanglement (such as the calculation of the Page curve for an evaporating black hole) heavily relies on holographic ideas. The takeaway is that AdS/CFT bridges the gap between black hole physics and quantum physics, showing that black holes behave like ordinary quantum systems with a large number of degrees of freedom, thus demystifying many aspects of black hole thermodynamics and paradoxes.

One of the most profound developments spurred by AdS/CFT is the realization of a deep connection between quantum entanglement and spacetime geometry. In the duality, the structure of the AdS spacetime - essentially the shape of space, how it curves - is linked to how the quantum information is distributed in the CFT.[\[1\]](https://beuke.org/ads-cft/#fn:1) A famous result along these lines is the Ryu-Takayanagi formula (or conjecture), which proposes a precise quantitative relationship between the entanglement entropy of a region in the CFT and the area of a certain surface in the AdS bulk. In essence, if you take some portion of the CFT and compute how entangled it is with the rest of the system, that number equals the area (in Planck units) of a minimal surface that extends into the bulk AdS geometry. This is like a holographic version of the Bekenstein area-entropy connection, generalized to arbitrary systems, not just black holes. What this means conceptually is that the fabric of spacetime (in AdS) is woven from the entanglement structure of the CFT. If entanglement were to vanish, the spacetime might fall apart into disconnected pieces. This idea has led to slogans like “spacetime emerges from quantum entanglement.” Researchers have even found that the mathematics of AdS/CFT has similarities to quantum error-correcting codes, suggesting that the way information is protected in the bulk against loss (e.g., if part of the boundary is removed, the bulk still stays intact) works like an error-correcting code - an insight at the crossroads of quantum information and quantum gravity. All these developments indicate that AdS/CFT is teaching us why gravity has the form it does and how space, gravity, and quantum information are fundamentally related. It’s a new paradigm where geometry and quantum information are two sides of the same coin.

Even though AdS/CFT was discovered in the context of string theory, it has yielded surprising applications in various fields of physics - essentially exporting techniques from quantum gravity to solve problems elsewhere. A notable example is in nuclear physics: quark-gluon plasma (QGP), the hot dense soup of quarks and gluons created in heavy-ion colliders, is extremely strongly coupled and difficult to describe with normal QCD methods. Physicists found that using a 5D AdS gravity model dual to a 4D plasma-like CFT could give qualitative - and sometimes quantitative - insights into QGP properties.[\[4\]](https://beuke.org/ads-cft/#fn:4) In 2005, for instance, researchers applied AdS/CFT to calculate the ratio of shear viscosity to entropy density in a hot plasma. The result was a very small ratio, essentially a proposed universal lower bound. Experiments at RHIC and the LHC later measured the QGP’s viscosity and found it indeed is extraordinarily small, close to the predicted bound. Similarly, holographic models predicted a certain value for the jet quenching parameter (which measures how quickly high-energy quarks lose energy in the plasma) that turned out to be in the same ballpark as experimental results. These successes indicate that even though QGP is not literally N=4\\mathcal{N}=4N=4 SYM plasma, the AdS/CFT techniques capture essential physics of strongly coupled fluids.

In condensed matter physics, researchers have turned to AdS/CFT to tackle quantum systems that are strongly interacting, such as unconventional superconductors and quantum critical metals. This subfield is sometimes called “AdS/CMT” (for Condensed Matter Theory). The idea is to find an AdS dual for certain many-body systems. For example, a theory of electrons at a quantum critical point might map to some gravity theory with an extra dimension, where the formation of a superconducting phase corresponds to the formation of a particular field configuration in AdS (a “holographic superconductor”).[\[1\]](https://beuke.org/ads-cft/#fn:1) Indeed, holographic superconductors have been studied, where properties like the conductivity can be computed on the gravity side and compared to expectations for high-temperature superconductors. While this approach is more qualitative, it has provided new intuition - for instance, understanding how superconductivity might emerge from strong coupling in a dual picture. More generally, exotic phases like non-Fermi liquids and superfluids have been modeled with AdS duals, offering a new toolkit to condensed matter theorists.

AdS/CFT ideas have even infiltrated quantum information theory and quantum computing. The correspondence’s implications about entanglement and error correction have led to fruitful dialogues between these fields. Concepts like tensor networks (MERA) used in quantum information to efficiently represent strongly correlated states have been found to have similarities with the spatial structure of AdS space, hinting that they are like discrete holographic duals. This has led to quantum information scientists using holographic systems as testing grounds for ideas about quantum entanglement, complexity, and information scrambling. For example, how fast quantum information spreads (or scrambles) in a black hole has a dual description in the CFT, linking to quantum chaos and even to ideas of computational complexity in quantum circuits.[\[7\]](https://beuke.org/ads-cft/#fn:7) Such cross-disciplinary applications of AdS/CFT are still developing, but they underscore a key point: AdS/CFT is not just about quantum gravity - it’s a powerful toolkit. It allows researchers to translate problems in one realm to another where they might be easier to solve. This dual perspective has provided insights into phenomena as diverse as the viscosity of fluids, the resistance of superconductors, and the entanglement structure of quantum states, truly bridging high-energy physics with low-energy quantum physics.

### Open Questions and Interpretational Challenges

A fundamental limitation of the AdS/CFT correspondence is right in its name - the “AdS.” Our real universe, as far as observations indicate, has a positive cosmological constant and is expanding (accelerating, in fact), which means its large-scale geometry is closer to de Sitter (dS) space, not Anti-de Sitter. In de Sitter space, there is no timelike boundary at spatial infinity where one could easily imagine a CFT living; instead, de Sitter has horizons and a future boundary that is a moment in time. This raises the question: Does a correspondence like AdS/CFT exist for de Sitter space? And if not, what does that mean for applying holography to our cosmos?[\[5\]](https://beuke.org/ads-cft/#fn:5) So far, AdS/CFT has been firmly established only for negatively curved spacetimes. It is not proven whether a similar duality holds for a universe like ours. In fact, Maldacena’s original work explicitly assumed an AdS5 background with supersymmetry and other ideal conditions, which do not match reality. Researchers have written thousands of papers extending and exploring AdS setups, but the fact remains: our universe is not AdS. This is sometimes called the “cosmological constant problem” for holography - we don’t know how to deal with a positive cosmological constant in the same way. The consequence is that AdS/CFT, while immensely powerful theoretically, might be describing toy models of universes rather than our own universe. That said, some physicists remain optimistic that lessons from AdS will carry over, at least approximately, to gravity in our universe, or that a yet-to-be-found holographic dual for de Sitter space might exist.

Motivated by the success of AdS/CFT, there have been attempts to formulate a de Sitter/Conformal Field Theory correspondence (dS/CFT). Notably, in 2001, Andrew Strominger proposed a heuristic dS/CFT analogy, suggesting that quantum gravity on a de Sitter space might be dual to a CFT defined on the future boundary of that space (a spacelike surface at infinity).[\[6\]](https://beuke.org/ads-cft/#fn:6) In this picture, time itself in the bulk would emerge from the RG flow (scale transformations) of the boundary theory. However, constructing a concrete example of dS/CFT has proven challenging. One big issue is that we lack a controlled example of de Sitter space in string theory - most solutions of string theory with positive cosmological constant are unstable or poorly understood. Without a solid “gravity side” to start from, it’s hard to find the dual field theory. Another issue is that any would-be CFT dual to dS might have strange properties: for instance, studies indicate it might have an imaginary central charge (related to being non-unitary), suggesting that the usual rules of unitary quantum field theory might not apply. In other words, a naive dS/CFT dual could be a non-unitary CFT, which is a significant departure from the well-behaved unitary CFTs in AdS/CFT. These and other technical obstacles mean dS/CFT remains a conjectural, much less developed idea. It’s an area of ongoing research - a dS/CFT correspondence, if discovered, would be revolutionary as it could directly apply holography to cosmology (potentially explaining inflation or horizon entropy in a dual way). For now, though, it’s fair to say we don’t yet have a holographic duality for de Sitter space that rivals the clarity and evidence of AdS/CFT. Our current holographic theories seem to prefer a universe with a “negative” vacuum energy. This mismatch with reality is a humbling reminder of the limits of our theoretical tools.

There is also a philosophical and practical debate about how “real” AdS/CFT is. On one hand, the duality is supported by a great deal of evidence - countless checks have been made in various limits, and no contradictions have been found.[\[4\]](https://beuke.org/ads-cft/#fn:4) Many physicists take it as established (within string theory) that the correspondence is true for the examples studied, even if a rigorous mathematical proof is absent. On the other hand, AdS/CFT is still a conjecture - by necessity, since we don’t yet have a non-perturbative definition of string theory to prove the equivalence from first principles. It’s a striking example of where physics intuition and consistency checks outran mathematical rigor. There’s also the fact that AdS/CFT relates to a fictional universe (one with AdS boundary conditions and often supersymmetry) rather than the observable universe. This means direct experimental verification in the traditional sense is not possible - we cannot set up a four-dimensional supersymmetric Yang-Mills theory on a bench, let alone a five-dimensional AdS gravity region to compare it with. However, the usefulness of AdS/CFT can be indirectly tested by how well it predicts or explains phenomena in systems we can experiment on. As discussed, the correspondence has had successes in predicting properties of the quark-gluon plasma that were later observed. These successes give some credence to the idea that the holographic principle captures something real about strongly-coupled physics, even if our universe isn’t exactly AdS. Still, skeptics might argue that using AdS/CFT to model QGP or superconductors is like using an idealized model - it doesn’t prove the duality fundamental, it just shows it’s a useful calculus trick in those cases. Another angle on “experimental” tests is quantum simulation: some have pondered whether quantum computers or analog lab systems could be used to simulate a CFT and thereby “observe” the dual AdS physics indirectly, but this is in very early stages.

In terms of conceptual reality, a question often asked is: Is AdS/CFT just a mathematical equivalence, or is the boundary CFT actually how nature stores information about the bulk? If we had an AdS universe in a box, would the boundary literally have the degrees of freedom for everything inside it? The conservative view is that AdS/CFT is a powerful theoretical correspondence - a tool that, while not directly testable, is likely true and part of the consistency of string theory.[\[2\]](https://beuke.org/ads-cft/#fn:2) A more radical view (espoused by some) is that the duality hints at a paradigm where our world could be holographic in a similar way - that the ultimate description of our universe might be a quantum theory without gravity in one lower dimension. Maldacena himself has said we should take the idea seriously until proven otherwise. At the moment, AdS/CFT stands as a monumental theoretical discovery that has passed many consistency tests and has become a cornerstone of modern theoretical physics, yet it also remains, in a sense, unverified by direct experiment and unproven by rigorous mathematics. It straddles the line between physics and mathematics, offering profound insights but also leaving us with deep questions: How far does holography extend? Is spacetime fundamentally holographic even in a non-AdS context? Could we find a way to experimentally access higher-dimensional gravity through its lower-dimensional dual (for example, using condensed matter experiments or quantum simulators)? These questions drive ongoing research.

### Conclusion

In summary, the AdS/CFT correspondence has transformed theoretical physics by providing a tangible example of holography. It rests on fundamental principles that tie gravity to quantum field theory, emerged from attempts to solve puzzles in black hole physics, and operates through a precise bulk-boundary mapping that challenges our understanding of space and information. It has illuminated aspects of quantum gravity, shed light on black hole information and entropy, and reached into other fields for practical insights. Yet, it also faces limitations - chiefly that our real universe isn’t AdS - and it remains an unproven but exceedingly well-motivated idea. As research progresses, physicists continue to test the edges of AdS/CFT, searching for generalizations (like dS/CFT) and thinking of clever ways to verify its implications. Whether or not our world is a hologram in the AdS/CFT sense, the correspondence stands as a powerful reminder that our universe’s deepest laws might have dual interpretations, and that understanding gravity may require us to think in terms of holograms and dimensions beyond the immediately visible. The AdS/CFT duality has opened a window into a new way of thinking about reality - one where gravitational worlds and quantum fields are just different languages describing the same underlying truth.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="biased-noise-thresholds-of-zero-rate-holographic-codes-with-.md">
<details>
<summary>Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding</summary>

Phase: [EXPLORATION]

**Source URL:** <https://arxiv.org/html/2408.06232v3>

# Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding

J. Fan1,2⁣†{}^{1,2\\,\\dagger}, M. Steinberg1,2⁣†,‡{}^{1,2\\,\\dagger,\\ddagger}, A. Jahn3, C. Cao4, S. Feld1,21QuTech, Delft University of Technology, 2628 CJ Delft, The Netherlands
2Quantum and Computer Engineering Department, Delft University of Technology, 2628 CD Delft, The Netherlands
3Department of Physics, Freie Universität Berlin, 14195 Berlin, Germany
4Department of Physics, Virginia Tech, Blacksburg, VA 24061, USA

###### Abstract

A crucial insight for practical quantum error correction is that different types of errors, such as single-qubit Pauli operators, typically occur with different probabilities. Finding an optimal quantum code under such biased noise is a challenging problem, related to the (generally unknown) maximum capacity of the corresponding noisy channel. A benchmark for this capacity is given by the hashing bound, which describes the performance of random stabilizer codes and leads to the matter of identifying codes that come close to the bound while also being efficiently decodable. In this work, we perform the first comprehensive analysis of asymptotically zero-rate holographic codes under biased noise. We show that many representatives from such models of this code class fulfill both the channel optimality and efficient decoding guarantees for tensor-network codes. In fact, all holographic codes tested were found to reach the hashing bound in some bias regime, while several built from the ⟦5,1,2⟧\\llbracket 5,1,2\\rrbracket surface code and ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code exceed state-of-the-art code performance in the 2-Pauli noise regime. Furthermore, we consider Clifford deformations which allow all considered codes to reach the hashing bound for 1-Pauli noise as well. Our results establish that holographic codes, which were previously shown to possess efficient tensor-network decoders, also exhibit competitive thresholds under biased noise.

22footnotetext: These authors contributed equally to this work.33footnotetext: Corresponding author: matt.steinberg3@gmail.com

## I Introduction

Holographic codes are quantum codes conventionally studied as toy models of the Anti-de Sitter/Conformal Field Theory (AdS/CFT) correspondence \[witten, maldacena, klebanov, almheiri2015bulk, harlow2017ryutakayanagi, happy\_paper, Harlow:2018fse, holographic\_codes\_topical\_review\] where they have led to remarkable insights in quantum gravity. However, because their relevance in quantum gravity is mostly theoretical \[uberholography, harlow2017ryutakayanagi\], very little is known about their practical error correction capabilities in contrast to leading benchmarks of quantum error correction, such as the surface code. In addition, recent advances in tensor network codes \[farrelly\_tn\_codes\] and the quantum LEGO formalism \[cao\_quantum\_lego\] have brought them closer to a practically viable regime. For example, leveraging their flexibility in the modular construction, holographic codes with high encoding rate and greatly exceeding the O​(n1/2)O(n^{1/2}) distance scaling have been proposed \[evenbly\_codes2\] alongside schemes for implementing universal fault-tolerant logic based on heterogeneous code constructions \[heterogeneous\_holo\_qrm\]. The hyperbolic geometry of holographic codes also implies that such codes admit efficient optimal tensor network decoders for all i.i.d. single qubit errors \[cao2024quantum\] since their tensor networks can be contracted in polynomial time even without bond truncation. Under such decoders, they have been shown to yield a code capacity threshold that are as high as that of the surface code \[farrelly\_tn\_codes\] under depolarizing noise where all Pauli errors occur with equal probability.

Although there remain many open questions before holographic codes can be fairly assessed at a practical level, e.g. determining the fault-tolerant threshold, there are properties that are poorly understood even at the code capacity level, where syndrome extractions are perfect. One such open question is the performance of the code when the error channels are biased. Biased noise is found in many physical quantum devices wherein certain Pauli errors such as phase flips, occur more frequently than bit flips. The presence of bias can also lead to better error correction with superior threshold and effective distances \[sahay2023high, xzzx\_surface\_code, tailored\_513\_xzzx\_codes, clifford\_deformed\_surface\]. In certain topological codes (e.g. Clifford-deformed topological codes such as the XZZX surface code) the threshold under biased noise has also been shown to attain the error threshold set by the hashing limit, which sets a target benchmark for good quantum error correcting codes that can be used for efficient information transmission under a noisy channel. In holographic codes, however, there is very little understanding of its performance against biased error \[cao2024quantum, parallel\_decoding\_tn\_codes\].

In this work, we provide the first characterization of holographic codes under biased noise. We study common classes of holographic codes and their deformations to demonstrate that asymptotically zero-rate _holographic quantum codes_ admit high code capacity thresholds comparable to leading benchmarks under biased noise and can either achieve or supersede the hashing bound for various Pauli channels of interest. The possibility of holographic codes as an alternative class of code constructions to exceed the hashing bound is also of independent interest, as a central problem in quantum coding theory is to identify efficiently decodable codes that can attain or even exceed the hashing bound. A class of such codes will not only provide new approaches for obtaining tighter _quantum channel capacity_ (QCC) lower bounds but also inspire proposals for more efficient strategies of error correction \[qccapacity\_very\_noisy, degenerate\_qu\_code\_pauli\_channels, lower\_bounds\_capacity\_birgitta, leditzky\_pauli\_hashing, xzzx\_surface\_code\].

Using tensor-network decoding techniques from \[farrelly\_tn\_codes, parallel\_decoding\_tn\_codes\], we study zero-rate versions of six different classes of holographic codes which are constructed from the seed codes of the

1. (a)
⟦5,1,3⟧\\llbracket 5,1,3\\rrbracket, i.e. Harlow–Preskill–Pastawski–Yoshida (HaPPY) code \[happy\_paper\]

2. (b)
Tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket code \[tailored\_713\]

3. (c)
⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket Steane code \[harris\_css\]

4. (d)
⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code \[farrelly\_tn\_codes\]

5. (e)
Surface-code fragment (SCF) \[harris\_iod\], and

6. (f)
A Clifford-deformed variant of the Steane code.

Our main results can be stated as follows. In the limit of pure 2-Pauli noise channels, the thresholds calculated for zero-rate SCF and ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket holographic codes exceed current state-of-the-art results \[leditzky\_pauli\_hashing, lower\_bounds\_capacity\_birgitta, qccapacity\_very\_noisy\]. To our knowledge, no other class of quantum code has thus far been able to supersede the hashing limit for pure 2-Pauli noise. In fact, all of the holographic codes tested in the limit of pure 2-Pauli noise either come within 2%2\\% of, attain, or overcome some portion of the hashing bound. Furthermore, all codes tested were found to either attain or overtake the hashing bound for some bias configuration of Pauli noise channel. Finally, we also apply the method of _Clifford deformations_ from \[3d\_surface\_hashing, clifford\_deformed\_surface\] to the holographic Steane code, demonstrating that the threshold of the code can be drastically modified for depolarizing, pure X, and pure Z noise channels. Our results provide strong evidence that holographic codes possess high resilience against various types of Pauli noise channels and can be tuned accordingly. In sharp contrast with other code families, maximum likelihood decoding of holographic codes and the computation of their weight enumerator polynomials are possible in polynomial time, even with exact tensor network contractions \[farrelly\_tn\_codes, cao2024quantum\], further bolstering their practical potential for both quantum error correction and for numerical studies of QCC bounds.

The remainder of this article is organized as follows: we review in the background ( [SectionII](https://arxiv.org/html/2408.06232v3#S2 "II Background ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding")) the basics of holographic codes and their properties for practical QEC in [SectionII.1](https://arxiv.org/html/2408.06232v3#S2.SS1 "II.1 Holographic Quantum Error Correction ‣ II Background ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"), as well as an explanation for how tensor-network decoding functions ( [SectionII.3](https://arxiv.org/html/2408.06232v3#S2.SS3 "II.3 Tensor-Network Decoding ‣ II Background ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding")). In [SectionIII](https://arxiv.org/html/2408.06232v3#S3 "III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"), we begin by discussing first the experimental setup for our simulations, the codes tested, and the biased-noise points considered ( [SectionIII.1](https://arxiv.org/html/2408.06232v3#S3.SS1 "III.1 Noise Model and Setup ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding")); in [SectionIII.2](https://arxiv.org/html/2408.06232v3#S3.SS2 "III.2 Zero-Rate Holographic Code Results ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"), we present all of the results of our study. Finally, we close with a discussion of future directions and implications of our work ( [SectionIV](https://arxiv.org/html/2408.06232v3#S4 "IV Discussion ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding")), followed by a discussion of implications for quantum coding theory ( [SectionIV.1](https://arxiv.org/html/2408.06232v3#S4.SS1 "IV.1 Quantum Coding Theory ‣ IV Discussion ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding")), as well as practical directions for holographic codes ( [SectionIV.2](https://arxiv.org/html/2408.06232v3#S4.SS2 "IV.2 Holographic Codes in Practice ‣ IV Discussion ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding")).

## II Background

### II.1 Holographic Quantum Error Correction

Originally developed to model the _AdS/CFT correspondence_\[witten, maldacena, klebanov, nastase, takayanagi\_book\], holographic quantum error correction involves encoding maps from _bulk_ (logical) degrees of freedom on a d+1d{+}1-dimensional hyperbolic space to dd-dimensional _boundary_ (physical) degrees of freedom. While in full AdS/CFT the bulk and boundary degrees of freedom are associated with weakly-coupled quantum gravity on an asymptotically anti-de Sitter (AdS) background and strongly-coupled conformal field theory (CFT), respectively, aspects of this duality for d=1d=1 can be captured by simple tensor network codes \[almheiri2015bulk, happy\_paper, Harlow:2018fse, holographic\_codes\_topical\_review\].

https://arxiv.org/html/2408.06232v3/x1.pngFigure 1: The holographic tensor-network codes considered in this work: (a) The _Harlow-Preskill-Pastawski-Yoshida_ (HaPPY) code \[happy\_paper\] whose pentagon-hexagon geometry also underlies the holographic _surface-code fragment_ (SCF) model \[harris\_iod\], (b) the holographic ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code \[farrelly\_tn\_codes\], and (c) the holographic Steane code \[harris\_css\].
All are defined as tensor network contractions of copies of a fixed qq-leg tensor on a hyperbolic tiling, with the central tensor used as a _seed tensor_ for the encoding isometry of a ⟦q−1,1,d⟧\\llbracket q-1,1,d\\rrbracket code with some distance dd.
The remaining tensors have all qq legs contracted in the plane, leading to a larger encoding map between one logical qubit (central red leg) and the boundary physical qubits (open black legs).
Here we depict the codes with R=2R=2 layers of edge inflation. In the R→∞R\\to\\infty limit, the rate of each code goes to zero.

Holographic quantum codes are, at their core, _generalized concatenated_ codes \[poulin2005subsystem, lidar\_qec, williamson\_ft\_logical\_gates, gottesman\_thesis\_stabilizer\_codes, heterogeneous\_holo\_qrm, baspin2024wire, liu2024subsystem\], as their tree-like concatenation structure is a consequence of the bulk logical qubits being divisible into radial layers \[happy\_paper, conformal\_quasi\_holo, central\_charges\_jahn\_eisert\].
The most widely studied instances of holographic codes also fall into the category of _stabilizer codes_\[happy\_paper, harris\_css, steinberg\_evenbly\_codes1\], despite some restrictions on their representation of holographic dualities \[Dong:2018seb, Akers:2018fow, Cao:2023mzo\] and the possibility to construct more sophisticated non-stabilizer or even approximate holographic codes \[hmera\_approx, pollack2022understanding, cao2021approximate, kim2017entanglement, xp\_stabilizer\]. We shall therefore limit ourselves to stabilizer versions of holographic codes in the present work.

Stabilizer codes themselves are defined as codes for which the _logical operators_ 𝖫\\mathsf{L} and _codeword stabilizers_ 𝖲\\mathsf{S} consist of elements Pi∈𝖯nP\_{i}\\in\\mathsf{P}^{n}, where 𝖯n\\mathsf{P}^{n} is the nn-qubit Pauli group, PiP\_{i} takes the form Pi1⊗⋯⊗PinP\_{i\_{1}}\\otimes\\cdots\\otimes P\_{i\_{n}}, and P∈{I,X,Y,Z}P\\in\\{I,X,Y,Z\\}, i.e., the single-qubit Pauli operators. It is also wholly possible to consider _finite-rate_ versions of holographic codes, wherein individual seed tensors can be specified with logical-qubit implantation. In this work, we consider only zero-rate versions of holographic codes, wherein only the central logical index remains ( [Figure1](https://arxiv.org/html/2408.06232v3#S2.F1 "In II.1 Holographic Quantum Error Correction ‣ II Background ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"))
111One can additionally construct subsystem versions of holographic quantum codes. Here, one chooses to subdivide the physical Hilbert space as 𝖧p=𝖧⊗𝖧¯\\mathsf{H}\_{p}=\\mathsf{H}\\otimes\\mathsf{\\bar{H}}, where 𝖧\\mathsf{H} represents the code subspace. Then, given 𝖧\\mathsf{H}, we can decompose the code subspace further as 𝖧=𝖧L⊗𝖧G\\mathsf{H}=\\mathsf{H}\_{L}\\otimes\\mathsf{H}\_{G}, where 𝖧L\\mathsf{H}\_{L} and 𝖧G\\mathsf{H}\_{G} represent the _logical_ and _gauge_ subsystems of the code subspace, respectively. Holographic codes have been previously treated as subsystem stabilizer codes in \[cao2021approximate, williamson\_ft\_logical\_gates, uberholography\].
.

Represented as tensor networks, the bulk geometry of holographic codes is that of a regular hyperbolic tiling, wherein each nn-gon tile is filled out by one tensor of nn planar (i.e., non-logical) legs. Starting from the central seed tensor whose single logical leg describes degrees of freedom in a small bulk patch in holography, the tensor network (and the bulk region it represents) can be iteratively extended via _inflation steps_, Here, each of these extensions can be realized by adding a layer of tensors (contracted) to the tensor network \[conformal\_quasi\_holo, central\_charges\_jahn\_eisert\]. While this process is not unique, we will only apply _edge inflation_ in this work (i.e. tensors/tiles are added to all open legs/edges of the previous step). We denote the number of inflation steps as RR, with R=0R=0 (no step) describing the seed tensor by itself, with [Figure1](https://arxiv.org/html/2408.06232v3#S2.F1 "In II.1 Holographic Quantum Error Correction ‣ II Background ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding") showing holographic codes on various hyperbolic tilings at R=2R=2.

From a practical perspective, there are many reasons to find the concept of a holographic quantum code appealing. Firstly, holographic codes are relatively simple to construct and scale from small, atomized examples to larger example codes. As a direct consequence of the quantum LEGO formalism \[cao\_quantum\_lego\], concepts such as code structure and transversal logical operations are straightforward to intuit \[heterogeneous\_holo\_qrm, cao2025growing\]. Secondly, the boundary of holographic codes exhibits a quasiperiodic self-similarity \[conformal\_quasi\_holo, central\_charges\_jahn\_eisert\], allowing one to rescale the number of physical and logical qubits using local inflation rules that also determine the code’s rate and distance scaling \[parallel\_decoding\_tn\_codes, evenbly\_codes2\], both of which fare better than other constructions \[campbell2017roadstoward, terhal2015quantum, fowler2012surface, breuckmann\_qldpc\]. Thirdly, it is known that most seed tensors for holographic codes can be easily mapped to graph states, implying that efficient preparation schemes likely exist \[engineering\_holography\_graph, raissi\_graph1, raissi\_graph2, helwig\_ame\_graph\]. Lastly, and perhaps most consequentially, it has been shown that holographic codes exhibit high resilience against various noise channels. Indeed, it was first shown in \[happy\_paper\] that holographic quantum error correction codes exhibit high thresholds against the quantum erasure channel; subsequently, several works have shown the capability of certain codes constructions to protect against depolarizing and 1-Pauli noise, potentially as well as topological codes \[parallel\_decoding\_tn\_codes, harris\_css, harris\_iod, farrelly\_tn\_codes, deconfinement, evenbly\_codes2\]. To our knowledge, a systematic biased-noise threshold study for even zero-rate holographic codes has not been performed, let alone for their constant-rate versions
111\[cao2024quantum\] discusses biased noise in finite-rate HaPPY pentagon codes, but it only captures the non-detectable error probability for a code of fixed length.
. As such, our work takes the first step towards understanding holographic codes under more generalized noise channels.

The main ingredient of a holographic quantum code is the seed tensor, defining the encoding map for a single tile (in [SectionII.2](https://arxiv.org/html/2408.06232v3#S2.SS2 "II.2 Seed Tensors Used in this Paper ‣ II Background ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding") we will provide descriptions of several seed codes which may be unfamiliar to the reader, such as the SCF and the tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket codes). Here we consider the zero-rate case with a logical qubit only on the central tile; on the remaining tiles all tensor legs are planar, effectively dispersing the logical information towards the tiling boundary. Note that in generic holographic codes, each tile may hold a logical qubit, leading to a nonzero asymptotic rate as the number RR of layers is increased.

Currently, several methods exist by which one may create a holographic code. Firstly, one may employ methods of _gauge fixing_ for various logical qubits in the bulk. This step leaves each encoding tensor with only physical legs that act isometrically from one layer to the next. In the second case, one can tile the bulk by surrounding a code with parameters ⟦n,k,d⟧\\llbracket n,k,d\\rrbracket by codes with parameters ⟦n+1,0,d+1⟧\\llbracket n+1,0,d+1\\rrbracket. In both cases, the contracted tensor network then forms one large encoding isometry from a single logical qubit to the physical boundary qubits given suitable (e.g. _perfect_\[happy\_paper\]) tensors. Here, we opt for the second case. Thirdly, copies of the same seed tensor are typically used to construct such codes, but one may also employ several different seed tensors in similar spirit to _heterogeneous_ concatenation methods for tree-style concatenated codes \[concat1, concat2, heterogeneous\_holo\_qrm\]. We note that all of these techniques it was recently shown that holographic codes are an instance of _generalized code concatenation_\[generalized\_code\_concat, heterogeneous\_holo\_qrm\].

### II.2 Seed Tensors Used in this Paper

Here we provide information on the seed codes utilized in this paper: the _perfect_⟦5,1,3⟧\\llbracket 5,1,3\\rrbracket code \[laflamme1996perfect\]; the Steane code \[Steane\_1996\]; the ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code \[shaw2008encoding\]; the surface-code fragment (SCF) from \[harris\_iod\] and the tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket code \[tailored\_713\].

Firstly, The famous _perfect_ code of \[laflamme1996perfect\] is a ⟦5,1,3⟧\\llbracket 5,1,3\\rrbracket code with cyclically permuted stabilizer support, as shown in [Table1](https://arxiv.org/html/2408.06232v3#S3.T1 "In III.1 Noise Model and Setup ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"). The perfect code is an example of generalized XZZX toric codes \[tailored\_513\_xzzx\_codes\], and is known to exhibit high resilience against biased 1-Pauli noise \[xzzx\_surface\_code, tailored\_713\]. Equally famous in its own right, the _Steane_ code is the prototypical example of a _Calderbank-Shor-Steane_ (CSS) code, in which two classical codes are utilized in order to construct a quantum code. The Steane code in particular is a _self-dual_ CSS code, meaning that the X-/Z- portions of the stabilizer generators are exactly coinciding. More information on both codes can be found in \[lidar\_qec, nielsen\_chuang\], and the stabilizers and logical operators for the code can be found in [Table1](https://arxiv.org/html/2408.06232v3#S3.T1 "In III.1 Noise Model and Setup ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding").

The _surface-code fragment_ (SCF) is the smallest surface code, and is known to possess a block-perfect encoding tensor, following the work of \[harris\_iod\]. The stabilizers and logical operators for the SCF seed tensor are shown in [Table1](https://arxiv.org/html/2408.06232v3#S3.T1 "In III.1 Noise Model and Setup ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"). The block-perfect condition is taken to mean that, given any permutation of cyclic permutations for the SCF tensor indices {1,2,3,4,6¯,5}\\{1,2,3,4,\\bar{6},5\\} (where 6¯\\bar{6} denotes the logical index), we can construct the condition whereby

|     |     |     |     |
| --- | --- | --- | --- |
|  | TrA​\[\|ψ⟩​⟨ψ\|\]∝𝕀,\\text{Tr}\_{A}\\big\[\\ket{\\psi}\\bra{\\psi}\\big\]\\propto\\mathbb{I}~, |  | (1) |

where \|A\|=⌊n2⌋\|A\|=\\lfloor\\frac{n}{2}\\rfloor. The SCF seed tensors are an instance of _planar maximally-entangled_ (PME) states \[doroudiani2020planar\], meaning that only adjacent groupings into bipartitions can reduce to maximally mixed states.

The _tailored_⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket code is a generalization of the celebrated _perfect_ code \[laflamme1996perfect\] and was first introduced in \[tailored\_713\]. The stabilizers and logical operators for the code are listed in [Table1](https://arxiv.org/html/2408.06232v3#S3.T1 "In III.1 Noise Model and Setup ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"). As stated in \[tailored\_513\_xzzx\_codes, wen2003quantum\], both the perfect code and the tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket codes can be regarded as the smallest toric codes with so-called _shifted_ boundary conditions. The tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket code was shown in \[tailored\_713\] to exhibit better threshold performance than the Steane code in the setting of highly-biased noise.

### II.3 Tensor-Network Decoding

Contracting a tensor network representing a holographic-code state with potentially thousands of qubits is computationally intractable; as such, we follow the simplification proposed in \[farrelly\_tn\_codes, parallel\_decoding\_tn\_codes\]. In what follows, we briefly review this technique.

In the tensor-network decoder formalism, we represent a stabilizer operator as elements in ℤ4\\mathbb{Z}\_{4}. As an example, we represent the stabilizer X1​Z2​Y3​Y4​X5​I6X\_{1}Z\_{2}Y\_{3}Y\_{4}X\_{5}I\_{6} for the ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code as the vector \[1,3,2,2,1,0\]\[1,3,2,2,1,0\]. In a stabilizer code, we naturally have a prescription for defining four logical operators: {𝖨¯,𝖷¯,𝖸¯,𝖹¯}∈𝖫\\{\\mathsf{\\bar{I}},\\mathsf{\\bar{X}},\\mathsf{\\bar{Y}},\\mathsf{\\bar{Z}}\\}\\in\\mathsf{L}. These operators can be used to define _logical equivalence classes_, permitting us to formulate a rank-nn tensor as

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝖳​(𝖫)α1,⋯,αn:={1if Pα1⊗⋯⊗Pαn∈𝖲𝖫0otherwise.\\mathsf{T}(\\mathsf{L})\_{\\alpha\_{1},\\cdots,\\alpha\_{n}}:=\\begin{cases}1&\\text{if $P\_{\\alpha\_{1}}\\otimes\\cdots\\otimes P\_{\\alpha\_{n}}\\in\\mathsf{SL}$}\\\<br>0&\\text{otherwise}\\end{cases}~. |  | (2) |

Here, we take α1,⋯,αn\\alpha\_{1},\\cdots,\\alpha\_{n} to be the mapping of a given stabilizer or logical operator to ℤ4\\mathbb{Z}\_{4}, as shown above; Pα1⊗⋯⊗PαnP\_{\\alpha\_{1}}\\otimes\\cdots\\otimes P\_{\\alpha\_{n}} represents the Pauli stabilizer formed from the inverse mapping, and 𝖲𝖫\\mathsf{SL} is the _logical coset_ of 𝖲\\mathsf{S} with respect to 𝖫\\mathsf{L}.

As a side remark, the tensors of [Equation2](https://arxiv.org/html/2408.06232v3#S2.E2 "In II.3 Tensor-Network Decoding ‣ II Background ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding") are not, strictly speaking, isometric. However, they facilitate efficient contraction, provided that the proper index contraction sequence is indicated; as such, the full decoding process which we will describe below exhibits a runtime complexity of 𝒪​(n2.37)\\mathcal{O}(n^{2.37}) in the best case \[bravyi2014efficient\_tn\_decoding, le2014powers\]. More details on the formation of large tensor networks using the aforementioned scheme can be found in \[farrelly\_tn\_codes, junyu\_msc\_thesis\].

The tensor-network decoder is a _maximum-likelihood_ (ML) decoder, which is shown to be optimal given the error model. The ML decoder generally works by calculating the most-likely correction needed to return the system to the correct code state, given a _syndrome_. Here, we define a syndrome as the set 𝐬=\[s1​⋯​sn−k\]\\mathbf{s}=\[s\_{1}\\cdots s\_{n-k}\] of ℤ2\\mathbb{Z}\_{2} parity results from measuring each stabilizer. An error 𝖤\\mathsf{E} is initialized as a probability vector corresponding to each individual physical qubit; this vector is then contracted with the holographic tensor network, permitting us to calculate the syndrome 𝐬=𝖧𝖤\\mathbf{s}=\\mathsf{HE}, where 𝖧\\mathsf{H} is the parity-check matrix of the holographic code.

After finding the syndrome, we deduce the _pure error_ (or _destabilizer_) 𝖤pure\\mathsf{E}\_{\\text{pure}} by taking the _Moore-Penrose inverse_ (or pseudoinverse) 𝖧pseudo†\\mathsf{H}\_{\\text{pseudo}}^{\\dagger} of the parity-check matrix, resulting in the equation

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝖤pure=𝖧pseudo†​𝐬.\\mathsf{E}\_{\\text{pure}}=\\mathsf{H}\_{\\text{pseudo}}^{\\dagger}\\mathbf{s}~. |  | (3) |

Once the pure error is obtained, we proceed to calculate the probability that an error with the form of 𝖤pure\\mathsf{E}\_{\\text{pure}} has occurred on the nn physical qubits; this is done by contracting the tensor network with tensors that parameterizes the probability of errors on each physical qubit on the boundary. For independently distributed errors, even an exact contraction is efficient. From this procedure, we obtain the expression

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℙ​(𝖫,𝐬):=∑S∈𝖲Prob​\[𝖤pure\|S​L\],\\mathbb{P}(\\mathsf{L},\\mathbf{s}):=\\sum\_{S\\in\\mathsf{S}}\\text{Prob}\[\\mathsf{E}\_{\\text{pure}}\|SL\]~, |  | (4) |

where Prob​\[𝖤pure\|S​L\]\\text{Prob}\[\\mathsf{E}\_{\\text{pure}}\|SL\] signifies the probability of a pure error acting on the coset of stabilizer S∈𝖲S\\in\\mathsf{S} with respect to logical operator L∈𝖫L\\in\\mathsf{L}. In practice, the decoder must find LL such that ℙ​(𝖫,𝐬)\\mathbb{P}(\\mathsf{L},\\mathbf{s}) is maximized, i.e. arg​max⁡\[ℙ​(𝖫,𝐬)\]\\operatorname\*{arg\\,max}\\big\[\\mathbb{P}(\\mathsf{L},\\mathbf{s})\\big\]. As an additional condition, the summation over all logical cosets must be equivalent to unity; that is ∑L∈𝖫∑S∈𝖲ℙ​(𝖫,𝐬)=1\\sum\_{L\\in\\mathsf{L}}\\sum\_{S\\in\\mathsf{S}}\\mathbb{P}(\\mathsf{L},\\mathbf{s})=1. As before, we refer the reader to \[farrelly\_tn\_codes, parallel\_decoding\_tn\_codes, junyu\_msc\_thesis\] for further details on calculating the logical success rate.

## III Results

### III.1 Noise Model and Setup

The error model tested in this work consists of the code-capacity error model for Pauli noise. Such an error model takes on the form

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝖤​(ρ)=(1−p)​ρ+p​(rX​X​ρ​X+rY​Y​ρ​Y+rZ​Z​ρ​Z),\\mathsf{E}(\\rho)=(1-p)\\rho+p(r\_{X}X\\rho X+r\_{Y}Y\\rho Y+r\_{Z}Z\\rho Z)\ , |  | (5) |

with the relative error probabilities rX+rY+rZ=1r\_{X}+r\_{Y}+r\_{Z}=1, typically in the regime of rX=rYr\_{X}=r\_{Y} with a bias η=rZrX+rY≥12\\eta=\\frac{r\_{Z}}{r\_{X}+r\_{Y}}\\geq\\frac{1}{2} (in the case of ZZ-biased noise). When η=12\\eta=\\frac{1}{2}, one recovers the standard depolarizing noise channel. If we move η↦0\\eta\\mapsto 0, then we necessarily move towards _2-Pauli_ noise; that is, noise channels consisting only of two Pauli operators, such as XZ or XY noise.

The seed tensors and their associated logical operators and their stabilizers are shown in [Table1](https://arxiv.org/html/2408.06232v3#S3.T1 "In III.1 Noise Model and Setup ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"); we have shown all of the seed tensors’ stabilizers and logical operators studied in this work. Here we have used the notation X​XXX to denote X⊗XX\\otimes X for brevity. Additionally, the final entry for each stabilizer generator (with a bar above) denotes the action on the logical index.

|     |     |     |
| --- | --- | --- |
| Seed Tensor | Stabilizers | Logical Operators |
| HaPPY | X​Z​Z​X​I​I¯XZZXI\\bar{I}, I​X​Z​Z​X​I¯IXZZX\\bar{I}, X​I​X​Z​Z​I¯XIXZZ\\bar{I}, Z​X​I​X​Z​I¯ZXIXZ\\bar{I} | Z​Z​Z​Z​Z​Z¯,X​X​X​X​X​X¯ZZZZZ\\bar{Z},XXXXX\\bar{X} |
| Tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket | X​Z​I​Z​X​I​I​I¯,I​X​Z​I​Z​X​I​I¯,I​I​X​Z​I​Z​X​I¯,X​I​I​X​Z​I​Z​I¯,Z​X​I​I​X​Z​I​I¯,I​Z​X​I​I​X​Z​I¯,Z​I​Z​X​I​I​X​I¯XZIZXII\\bar{I},IXZIZXI\\bar{I},IIXZIZX\\bar{I},XIIXZIZ\\bar{I},ZXIIXZI\\bar{I},IZXIIXZ\\bar{I},ZIZXIIX\\bar{I} | Z​Z​Z​Z​Z​Z​Z​Z¯ZZZZZZZ\\bar{Z}, X​X​X​X​X​X​X​X¯XXXXXXX\\bar{X} |
| Steane | X​X​I​I​I​X​X​I¯XXIIIXX\\bar{I}, I​X​X​X​I​I​X​I¯IXXXIIX\\bar{I}, I​I​I​X​X​X​X​I¯IIIXXXX\\bar{I}, Z​Z​I​I​I​Z​Z​I¯ZZIIIZZ\\bar{I}, I​Z​Z​Z​I​I​Z​I¯IZZZIIZ\\bar{I}, I​I​I​Z​Z​Z​Z​I¯IIIZZZZ\\bar{I} | Z​Z​Z​Z​Z​Z​Z​Z¯ZZZZZZZ\\bar{Z}, X​X​X​X​X​X​X​X¯XXXXXXX\\bar{X} |
| ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket | Z​I​Z​I​I​I​I¯ZIZIII\\bar{I}, X​Z​Y​Y​X​I​I¯XZYYXI\\bar{I}, X​X​X​X​Z​I​I¯XXXXZI\\bar{I}, I​Z​Z​X​I​X​I¯IZZXIX\\bar{I}, X​Y​X​Y​I​Z​I¯XYXYIZ\\bar{I} | X​Z​X​Z​I​I​X¯XZXZII\\bar{X}, X​Y​Y​X​I​I​Z¯XYYXII\\bar{Z} |
| SCF | X​X​I​X​I​I¯XXIXI\\bar{I}, I​I​X​X​X​I¯IIXXX\\bar{I}, Z​I​Z​Z​I​I¯ZIZZI\\bar{I}, I​Z​I​Z​Z​I¯IZIZZ\\bar{I} | X​I​X​I​I​X¯XIXII\\bar{X}, I​I​Z​I​Z​Z¯IIZIZ\\bar{Z} |
| CD-Steane | X​Z​Z​I​I​I​X​I¯XZZIIIX\\bar{I}, X​I​Z​X​Z​I​I​I¯XIZXZII\\bar{I}, X​I​I​I​Z​Z​X​I¯XIIIZZX\\bar{I}, Z​X​X​I​I​I​Z​I¯ZXXIIIZ\\bar{I},Z​I​X​Z​X​I​I​I¯ZIXZXII\\bar{I}, Z​I​I​I​X​X​Z​I¯ZIIIXXZ\\bar{I} | X​Z​Z​X​Z​Z​X​X¯XZZXZZX\\bar{X}, Z​X​X​Z​X​X​Z​Z¯ZXXZXXZ\\bar{Z} |

Table 1: Seed tensors and their stabilizers, as well as logical operators for select holographic codes.

Threshold calculations were performed using the tensor-network decoder from \[farrelly\_tn\_codes, parallel\_decoding\_tn\_codes\]. These decoders and others will be made public in an upcoming software package for holographic quantum error correction codes \[fan2024lego\_hqec\]. However, for the purposes of understanding the current work, we focus on surveying biased-noise resilience for a swath of known holographic codes, and not on a systematic treatment of tensor-network decoding methodology \[bravyi2014efficient\_tn\_decoding\].

https://arxiv.org/html/2408.06232v3/x2.pngFigure 2: Threshold data points surveyed for the holographic codes tested in this work. All data points were ascertained using four threshold crossing points at each corresponding marker in the diagram. In blue, we highlight the pure Pauli biased points, and in red, we have accentuated the 2-Pauli bias points considered in this work. The depolarizing noise point is denoted in violet.

In our biased-noise threshold profiling, we tested 43 distinct Pauli biases and have displayed them on the ternary diagram shown in [Figure2](https://arxiv.org/html/2408.06232v3#S3.F2 "In III.1 Noise Model and Setup ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"). Each point of the triangular plot shown represents a pure Pauli error channel. Subsequently, points on the interior of the plot can be read by following the grid lines provided to the boundaries; for example, the point to the lower left of the central depolarizing noise marker can be interpreted as having relative biases r¯=(rX,rY,rZ)\\bar{r}=(r\_{X},~r\_{Y},~r\_{Z}) of (0.25,0.25,0.5)(0.25,~0.25,~0.5). At each bias point 10,000 Monte Carlo simulations were performed per threshold curve data point, per layer. We display commensurate threshold curve results for some select data points in [Figure4](https://arxiv.org/html/2408.06232v3#S3.F4 "In III.2 Zero-Rate Holographic Code Results ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding") for the zero-rate HaPPY code.

### III.2 Zero-Rate Holographic Code Results

https://arxiv.org/html/2408.06232v3/x3.pngFigure 3: Ternary plots for all holographic codes investigated in this study under biased noise, in the code-capacity setting. (a)-(d) depicts the zero-rate HaPPY, Steane, ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket, and SCF codes; thresholds are color-coded from dark blue (pt​h=10%p\_{th}=10\\%) to dark red (pt​h=50%p\_{th}=50\\%). Additionally, we tested the _tailored_⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket code from \[tailored\_713, tailored\_513\_xzzx\_codes\], which achieved an identical threshold profile to that of the HaPPY code.
https://arxiv.org/html/2408.06232v3/x4.pngFigure 4: Threshold curves for depolarizing, pure XX, YY, and ZZ noise, as studied using the tensor-network decoder, for the zero-rate HaPPY code at up to R=3R=3 layers of edge inflation.

The ternary plots for all four zero-rate holographic codes tested in this paper are depicted in [Figure3](https://arxiv.org/html/2408.06232v3#S3.F3 "In III.2 Zero-Rate Holographic Code Results ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"). From (a)-(d), we have displayed the: HaPPY; Steane; ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket; and SCF. At the center of each diagram, where depolarizing noise is represented, the zero-rate HaPPY code exhibits the lowest resilience (pt​h=17.9%p\_{th}=17.9\\%), whereas all other codes tested indicating thresholds in the region between pt​h=18%∼19%p\_{th}=18\\%\\sim 19\\%. As we move along each plot towards a pure 1-Pauli bias, we see starkly distinct behavior for every holographic code assessed: for example, the zero-rate HaPPY code (a) attains clear 50%50\\% thresholds in each of the pure 1-Pauli biases, while the Steane code’s resilience (b) appears to decrease. In the ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket and SCF codes, we observe asymmetrical biased-noise profiles with respect to pure Pauli noise behavior. For the ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code, we note that under pure 1-Pauli XX and YY noise channels, the threshold of the code increases, albeit more slowly than for the HaPPY code; notwithstanding this similarity, the ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code’s threshold dips by a small amount as we move towards the pure-ZZ region of the ternary plot. Interestingly, the SCF also evinces an asymmetrical biased-noise threshold spectrum. However, the SCF manifests high tolerance to pure YY errors, but to pure XX and ZZ errors decreases, as in the Steane code.

As a more detailed example, we plotted in [Figure4](https://arxiv.org/html/2408.06232v3#S3.F4 "In III.2 Zero-Rate Holographic Code Results ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding") the individual threshold curves obtained for the zero-rate HaPPY code for depolarizing noise, as well as for biased pure XX, pure YY, and pure ZZ noise. Around the fixed points in subfigures (b)-(d), the recovery rate promptly increases, which is due to several reasons: Firstly, the pure 1-Pauli noise capacity can be shown to be 50%50\\%. Secondly, as the tensor-network decoder is a maximum-likelihood decoder, after the p=0.50p=0.50 mark, the decoder selects the most-probable error and returns a pure error (destabilizer) vector which is used to correct. Therefore, unlike a minimum weight decoder, the tensor network decoder is still able to provide the right correction with high probability even when p>0.50p>0.50. More details can be found in \[harris\_iod, junyu\_msc\_thesis\].

If we look beyond the pure 1-Pauli portion of the ternary plots, we note more subtle behavior of these codes: for example, it can be seen that modest threshold increases emerge for the Steane and ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket codes as we move towards pure _2-Pauli_ noise, i.e., X​YXY, Y​ZYZ, and X​ZXZ noise. These changes can be seen more clearly by examining the threshold behavior of the codes via the tuning of a bias parameter η\\eta. In previous work, this aim was accomplished by comparing various zero-rate codes against the _hashing bound_, a useful lower bound for quantifying code-capacity channel performance \[xzzx\_surface\_code\]. However, in contrast to the present work, all previous works have examined the pure 1-Pauli noise limit associated with the hashing bound, and have not delved into combinations of two types of Pauli errors at once, a condition known to occur in the square-lattice GKP code under a symmetric Gaussian random displacement noise channel \[bosonic1, bosonic2, bosonic3, bosonic4\], as well as for error channels resulting from performing _Pauli twirling_ on the amplitude damping noise channel \[amp\_damping\_twirl\]. As such, we tune the η\\eta parameter within the range 0≤η≤+∞0\\leq\\eta\\leq+\\infty, extending previous work past the regime indicated by η≥0.5\\eta\\geq 0.5\[xzzx\_surface\_code, clifford\_deformed\_surface, tailored\_513\_xzzx\_codes\].

The hashing bound is formally defined as

|     |     |     |     |
| --- | --- | --- | --- |
|  | R=1−H​(p¯),R=1-H(\\bar{p})~, |  | (6) |

where RR represents an achievable rate k/nk/n for a random stabilizer code and H​(p¯)H(\\bar{p}) represents the _Shannon entropy_\[bennett1998quantum\]

|     |     |     |     |
| --- | --- | --- | --- |
|  | H​(p¯)=−∑i∈{I,X,Y,Z}pi​log⁡(pi).H(\\bar{p})=-\\sum\_{i\\in\\{I,X,Y,Z\\}}p\_{i}\\log{p\_{i}}~. |  | (7) |

Here, p¯=p​r¯\\bar{p}=p\\,\\bar{r}, rX+rY+rZ=1r\_{X}+r\_{Y}+r\_{Z}=1 as stated before, and pp represents the overall physical error probability. For a given noise model, there exists a physical error probability pp, at some given relative bias vector r¯\\bar{r}, for which the achievable rate RR goes to zero. This achievable rate via random coding is known as the _zero-rate hashing bound_.

https://arxiv.org/html/2408.06232v3/x5.pngFigure 5: Hashing bound plots for all of the codes tested in this work; we denote the hashing bound values in black solid line, while holographic codes are shown in varying colors and markers, together with calculated uncertainties. For all of the plots, biases ranged from η={0,+∞}\\eta=\\{0,+\\infty\\}. We list particular points of interest in [Table2](https://arxiv.org/html/2408.06232v3#S3.T2 "In III.2 Zero-Rate Holographic Code Results ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding").

[Figure5](https://arxiv.org/html/2408.06232v3#S3.F5 "In III.2 Zero-Rate Holographic Code Results ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding") depicts the comparison of the zero-rate hashing bound for 0≤η≤+∞0\\leq\\eta\\leq+\\infty with all four of the surveyed zero-rate holographic codes. In our plots, we calculate physical recovery rates for the following noise biases:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  | η∈(\\displaystyle\\eta\\;\\in\\;( | 0,1/1000,33/10000,99/10000,33/1000,1/10,1/3,1/2,\\displaystyle 0,\\nicefrac{{1}}{{1000}},\\nicefrac{{33}}{{10000}},\\nicefrac{{99}}{{10000}},\\nicefrac{{33}}{{1000}},\\nicefrac{{1}}{{10}},\\nicefrac{{1}}{{3}},\\nicefrac{{1}}{{2}}, |  | (8) |
|  |  | 1,3,10,30,100,300,1000,+∞).\\displaystyle 1,3,0,0,00,00,000,+\\infty)\ . |  |

In these results, the biased-noise properties of these codes manifest themselves across the full landscape of possible pure and 2-Pauli biases, i.e. pure XX, YY, and ZZ noise, in addition to pure X​YXY, Y​ZYZ, and X​ZXZ noise. In (a)-(c), we illustrate the bias tuning for pure XX, YY, and ZZ biases; consequently, as we tune the parameter η\\eta in the direction towards zero, we effectively remove XX, YY, and ZZ noise from the simulations, in effect achieving, as η→0\\eta\\to 0, pure Y​ZYZ noise from (a), pure X​ZXZ noise from (b), and pure X​YXY noise from (c).

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Noise bias (rX,rY,rZ)(r\_{X},r\_{Y},r\_{Z}) | HaPPY (%\\%) | Steane (%\\%) | SCF (%\\%) | ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket (%\\%) | Hashing (%\\%) | TQEC (%\\%) | Graph Codes (%\\%) |
| Depolarizing (1/3,1/3,1/3)(1/3,1/3,1/3) | 17.9±0.8117.9\\pm 0.81 | 18.98±0.3618.98\\pm 0.36 | 18.83±0.1318.83\\pm 0.13 | 18.46±0.3618.46\\pm 0.36 | 18.92918.929 | 19.14 | 19.059719.0597 |
| Pure X (1,0,0)(1,0,0) | 49.92±0.09649.92\\pm 0.096 | 10.79±0.1810.79\\pm 0.18 | 11.42±0.5211.42\\pm 0.52 | 33.56±1.0833.56\\pm 1.08 | 50.0050.00 | 50.00 | 50.0050.00 |
| Pure Y (0,1,0)(0,1,0) | 49.91±0.1149.91\\pm 0.11 | 10.8±0.1910.8\\pm 0.19 | 44.66±2.8244.66\\pm 2.82 | 33.56±1.0833.56\\pm 1.08 | 50.0050.00 | 50.0050.00 | 50.0050.00 |
| Pure Z (0,0,1)(0,0,1) | 49.91±0.1149.91\\pm 0.11 | 10.8±0.1910.8\\pm 0.19 | 11.42±0.5211.42\\pm 0.52 | 22.99±1.3922.99\\pm 1.39 | 50.0050.00 | 50.0050.00 | 50.0050.00 |
| Pure XZ (1/2,0,1/2)(1/2,0,1/2) | 21.45±0.6821.45\\pm 0.68 | 22.1±0.1622.1\\pm 0.16 | 24.027±1.0824.027\\pm 1.08 | 22.08±0.0422.08\\pm 0.04 | 22.70922.709 | ≈\\approxHashing | 22.68422.684 |
| Pure XY (1/2,1/2,0)(1/2,1/2,0) | 21.45±0.6921.45\\pm 0.69 | 22.1±0.1722.1\\pm 0.17 | 21.77±0.5121.77\\pm 0.51 | 22.58±0.1722.58\\pm 0.17 | 22.70922.709 | ≈\\approxHashing | 22.68422.684 |
| Pure YZ (0,1/2,1/2)(0,1/2,1/2) | 21.45±0.6821.45\\pm 0.68 | 22.1±0.1722.1\\pm 0.17 | 21.77±0.5121.77\\pm 0.51 | 22.08±0.0422.08\\pm 0.04 | 22.70922.709 | ≈\\approxHashing | 22.68422.684 |

Table 2: Recovery threshold data points pt​hp\_{th} for select pure and 2-Pauli biases. The entry in blue surpasses the hashing bound; entries in green attain it up to statistical uncertainty, while entries in gold come within 2%2\\% of achieving the bound.The “HaPPY” column refers to results obtained from both the original HaPPY code of \[happy\_paper\], as well as those from concatenating the tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket\[tailored\_713\]. In the last two columns, we compare to state-of-the-art results for topological codes (TQEC) as well as for graph codes: Depolarizing-noise thresholds for hexagonal color codes are taken from \[bombin\_strong\] and pure Pauli noise in surface codes from \[tuckett\_biased\_surface, xzzx\_surface\_code\], where thresholds around the Hashing bound were observed near the two-Pauli noise regime (the exact zero-bias regimes were not considered); graph code results are for the 5-in-5 code from \[leditzky\_pauli\_hashing\].

As is evidenced in each of the plots, the zero-rate HaPPY and tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket codes clearly achieve the hashing bound for all pure 1-Pauli biases, as well as for finite biases in which η>10\\eta>10. Additionally, in the limits for which η→0\\eta\\to 0, the HaPPY and tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket code thresholds closely trace out the hashing bound as pure 2-Pauli noise is approached. The behavior of the HaPPY code emulates in large part the behavior seen of the _generalized toric code_ family \[tailored\_513\_xzzx\_codes\]; we discuss this in more detail in [SectionIV](https://arxiv.org/html/2408.06232v3#S4 "IV Discussion ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding").

The Steane code portrays a distinct trend: in the pure 1-Pauli noise limit, the code performs significantly worse than all other codes tested. Nonetheless, the zero-rate Steane code eclipses the hashing bound for depolarizing noise (η=0.5\\eta=0.5), while also approaching the bound for finite biases as we approach the pure 2-Pauli limit (η=0\\eta=0). It was shown in previous work \[tuckett\_biased\_surface\] that the color code exhibits similar behavior in the pure 1-Pauli bias regime; as such, it is logical to infer that the holographic Steane code manifests similar behavior in these limits. Due to the fact that both codes are built from self-dual CSS codes \[lidar\_qec\], in the 1-Pauli limit, only one set of stabilizers gives information about the error, while the other stabilizers do not yield additional information for decoding. As such, the problem reduces to a classical linear code with a check matrix defined by only half of the symplectic check matrix in the quantum code. Notwithstanding, it is known that many code concatenation schemes based on graph states can slightly exceed the hashing bound; our results, up to the uncertainty margin given, show that the holographic Steane can at least match most of the codes discovered in \[leditzky\_pauli\_hashing\].

https://arxiv.org/html/2408.06232v3/x6.pngFigure 6: Threshold curves for the Clifford-deformed Steane code that we mention in [SectionIV](https://arxiv.org/html/2408.06232v3#S4 "IV Discussion ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"). Here, we have applied Hadamard gates to physical qubits 2,3,5,2,3,5, and 66. In (a) we document a slight threshold increase to 19.0±0.33%19.0\\pm 0.33\\%. (b) and (d) show the thresholds under pure X and Z noise, respectively, under which an increase to approximately 50%50\\% can be observed. Finally, (c) displays the results for pure Y noise, with a slight decrease to 10.58±0.12%10.58\\pm 0.12\\% apparent.

In \[3d\_surface\_hashing, clifford\_deformed\_surface\], it was shown that randomized _Clifford deformations_, when applied to the surface code, can improve threshold performance with respect to a code-capacity noise channel. In this way, a surface code may be tailored to achieve the 1-Pauli hashing bound; one wonders whether such randomized approaches could be leveraged in holographic codes as well. Indeed, we may regard the additional Hadamard gates in the Evenbly code \[evenbly\_codes2, steinberg\_evenbly\_codes1\] as an instance of Clifford deformation, in order to uphold the strict isometry properties present, while utilizing less highly-entangled quantum states.

As a preliminary step in this direction, we have performed a random Clifford deformation of the holographic Steane code using Hadamard gates, with the goal of improving the 1-Pauli threshold for the code. The seed tensors used in this modified holographic code are Clifford-equivalent to that of the original Steane code; the only difference lies in the application of Hadamard gates to physical qubits 2,3,52,3,5, and 66. The resulting stabilizer generators and logical operators for this Clifford-deformed Steane code are given in [Table1](https://arxiv.org/html/2408.06232v3#S3.T1 "In III.1 Noise Model and Setup ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding").

As is shown above, the stabilizers and logical operators do not follow the typical convention as expected for mixing Pauli operators in a cyclic manner, nor as in _generalized toric code_ constructions \[tailored\_513\_xzzx\_codes, tailored\_713, xzzx\_surface\_code, clifford\_deformed\_surface\]. The thresholds, reported in [Figure6](https://arxiv.org/html/2408.06232v3#S3.F6 "In III.2 Zero-Rate Holographic Code Results ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"), are for: (a) depolarizing noise (19.0±0.33%19.0\\pm 0.33\\%); (b) pure X noise (∼50%\\sim 50\\%); (c) pure Y noise (10.58±0.12%10.58\\pm 0.12\\%); and (d) pure Z noise (∼50%\\sim 50\\%). We observe that even our naive Clifford deformations, when combined with the holographic concatenation method, can greatly improve the threshold performance for targeting noise models of interest. Indeed, our results show that the Clifford-deformed holographic Steane code achieves the hashing bound for pure X and Z noise, and supersedes the bound for depolarizing noise. Such modifications will be investigated and are the subject of active research.

The SCF displays very interesting behavior at several points in [Figure5](https://arxiv.org/html/2408.06232v3#S3.F5 "In III.2 Zero-Rate Holographic Code Results ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding"). For biased XX and ZZ noise, the SCF performs similarly to the Steane code as η→+∞\\eta\\to+\\infty; this is due to the CSS properties of the seed tensor for both codes, as fewer parity checks are used for distinguishing errors in the limit of pure 1-Pauli noise. For biased YY noise, however, the SCF exhibits excellent threshold performance; although the SCF does not attain the hashing bound in the pure YY noise limit, many points of finite bias reach the bound. Additionally, as we tune the parameter η\\eta back towards zero, the pure X​ZXZ limit shows that the SCF surpasses the hashing bound at finite bias (η≤0.1\\eta\\leq 0.1). To the best of our knowledge, no other code construction thus far has surpassed the hashing bound for 2-Pauli noise \[leditzky\_pauli\_hashing, lower\_bounds\_capacity\_birgitta\].

Lastly, the ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code also exhibits breakaway threshold behavior, albeit for pure X​YXY noise. However, it can be observed in [Figure5](https://arxiv.org/html/2408.06232v3#S3.F5 "In III.2 Zero-Rate Holographic Code Results ‣ III Results ‣ Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding") that various points within the finitely-biased range η∈\[0,0.5\]\\eta\\in\[0,0.5\] come either within 2%2\\% of the hashing bound, or slightly exceeds it.

## IV Discussion

In this work we have shown strong evidence of extremely high threshold behavior for zero-rate holographic codes in the presence of 1-Pauli and 2-Pauli noise channels, for pure and finitely-biased noise regimes. In doing so, we have tested the: HaPPY and tailored ⟦7,1,3⟧\\llbracket 7,1,3\\rrbracket codes; Steane code; ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code; SCF code; and a Clifford-deformed Steane code. All codes have been shown to admit thresholds for some Pauli noise bias which either attain or surpass the hashing bound, and two of these codes, the SCF and the ⟦6,1,3⟧\\llbracket 6,1,3\\rrbracket code, surpass known the current state of the art for 2-Pauli noise \[leditzky\_pauli\_hashing, bhalerao2025improving\]. Our work demonstrates that holographic codes exhibit remarkable code-capacity properties under biased noise channels and can even overtake current state-of-the-art results \[leditzky\_pauli\_hashing\]. It moreover indicates that they constitute a novel and competitive class of stabilizer codes that is robust against biased noise, beyond the conventional options of topological codes \[xzzx\_surface\_code, basudha\_xyz2, domain\_wall\_color\_jens, tuckett\_biased\_surface, 3d\_surface\_hashing, clifford\_deformed\_surface\], naïve constructions of concatenated codes \[exact\_performance\], or other advanced techniques \[leditzky\_pauli\_hashing\]. Our results heavily imply that further modification via Clifford deformations is possible, and additionally that holographic codes can in fact be tailored to Pauli noise channels of interest.

Although our work constitutes the first such study of biased noise and holographic quantum codes, there are still many open directions for future research. Firstly, In related work \[evenbly\_codes2\], an integer-optimization decoder was utilized for the zero-rate _Evenbly code_ in order to pinpoint depolarizing and pure 1-Pauli noise thresholds of 19.1%19.1\\% and 50%50\\%, respectively overcoming and achieving the hashing bound. It would be interesting to see if a tensor-network decoder would allow for a more complete biased-noise threshold exploration of Evenbly codes and their many derivatives \[steinberg\_evenbly\_codes1, evenblyHTN, steinberg\_conformal\_HTN\]. However, in order to realize such an aim, the current tensor-network decoder utilized in our study would need to incorporate the extra Hadamard gates on edges, in order to extract the correct destabilizers from a syndrome. We leave such pursuits for subsequent work.

Additionally, it is known from \[evenbly\_codes2, steinberg\_evenbly\_codes1\] that Evenbly codes exhibit gauge-dependent threshold behavior, owing to the specific isometric constraints used in the structure of the code. In principle, nothing restricts us from utilizing such _gauge-fixing_ techniques in conjunction with maximum-rate constructions of the holographic codes studied here. However, the unique seed-tensor isometry properties of each holographic code may be utilized in order to give rise to similar gauge-dependent threshold “phases”; one example of this can be seen in the maximum-rate HaPPY code under gauge-fixing, which can exhibit very high threshold behavior \[alex\_logical\_recovery\] on a {5,5}\\{5,5\\} hyperbolic tiling. A systematic exploration of this subtopic would help to clarify the behavior of holographic codes under gauge-fixing constraints.

Thirdly, regarding the topic of finite-rate holographic code constructions, it is currently unknown whether there exist logical-qubit implantation schemes which maximize a code-capacity threshold for a given error model in a holographic code. It was shown in \[parallel\_decoding\_tn\_codes\] that several naive logical-qubit implantation schemes can approach the hashing bound; furthermore, it has been conjectured in \[evenbly\_codes2\] that certain finite-rate conceptions of Evenbly codes may in fact achieve the code-capacity threshold for quantum erasure noise, as well as the finite-rate hashing bound for Pauli noise. Investigating these possibilities will be at the center of future research efforts.

Recently, generalizations of Abelian stabilizer codes have been investigated as alternatives for low-overhead quantum error correction, as such codes naturally allow for non-Clifford logical gates \[xp\_stabilizer, webster2022xp, turaev\_viro\]. The quantum LEGO formalism itself is not restricted to only stabilizer circuits, and may be readily utilized for simulating aspects of either _non-Abelian stabilizer_ or _non-stabilizer_ codes. In this case, an enumerator-based method that combines tensor network and Monte Carlo sampling can be used to estimate logical error probabilities and thresholds of the code \[cao2024quantum\]. Alternatively, it is possible to calculate the _coherent information_ instead \[approx\_CFT\_codes, coherent\_information\]. However, new techniques are likely needed to calculate the coherent information for such generalized holographic codes, since the number of physical qubits at the boundary grows exponentially with a commensurate number of layers \[holographic\_codes\_topical\_review, conformal\_quasi\_holo\].

Comparing all of our results with those of _concatenated codes_, we note that the codes tested here fare better than typical tree-style concatenation \[exact\_performance, chamberland2017complementarygauge\], particularly for the depolarizing noise channel. Nevertheless, it was shown in \[leditzky\_pauli\_hashing\] that different types of repetition code concatenations can achieve threshold values comparable to ours for the depolarizing noise limit. Additionally, it was shown that various different concatenation schemes achieve or slightly surpass the hashing bound, depending on the details of the two repetition codes involved in the concatenation. Given this, one may then ask as to why our zero-rate holographic code constructions behave as they do. Considering the structural differences between holographic codes and more straightforward code-concatenation schemes, we would expect that in the 2-Pauli limit a conferrable advantage must be present by concatenation along the edges of a hyperbolic tessellation. Forthcoming work will investigate this advantage on more general footing.

As a final observation from high-energy physics, recent work \[deconfinement\] has shown that the bulk geometric transition in AdS/CFT implies a threshold for holographic codes in the continuum limit. Taking this finding in tandem with our results, it is natural to ask whether the _discretized_ isometric map typical of holographic codes provides a general method for achieving above-hashing-bound behavior, and additionally, whether or not AdS/CFT in the continuum limit implies the existence of a _fault-tolerance_ threshold for holographic codes.

### IV.1 Quantum Coding Theory

Here we put our results into perspective for quantum channel capacity and coding theory. Currently, understanding and mitigating the impact of quantum noise is crucial for quantum computation and communication. The most common way to characterize quantum noise is through quantum channels, which provide rigorous descriptions for how a quantum state is transformed or transmitted in the presence of errors \[wilde\_qit\]; as such, the maximum number of qubits that can be theoretically transmitted reliably in a noisy environment is the _quantum channel capacity_ (QCC) \[bennett1998quantum, qccapacity\_very\_noisy, schumacher1996quantum, schumacher1996sending, privateclassical\_qcapacity, lloyd\_capacity\_noisy\]. Determining the precise value of the QCC is therefore known to be incredibly challenging \[Bennett\_1997\], and in particular, the QCC is not accurately known even for a channel as ubiquitous as the depolarizing channel. A large part of the difficulty lies in the _superadditivity of coherent information_, which hinders a direct efficient evaluation of the quantum capacity when the channel acts independently and identically over many qubits. As a result, finding lower and upper bounds of the quantum capacity constitute important progress in quantum Shannon theory \[wilde\_qit, bennett1998quantum\].

In this vein, our results stand alongside recent efforts to characterize new classes of quantum codes that come arbitrarily close to the QCC \[leditzky\_pauli\_hashing, xzzx\_surface\_code\]. As the leading method for generating practical QEC codes achieving the QCC relies on random stabilizer codes, our work demonstrates via the holographic code construction that generalizations of code concatenation can achieve the theoretical lower bound for the QCC (i.e., the hashing limit). Such results are of paramount interest, since, as stated above, random quantum stabilizer codes do not generally achieve the optimal transmission rate for their analogous quantum counterparts such as the depolarizing channel or other Pauli channels, unlike their classical counterparts (which are typically capacity-achieving for symmetric channels).

### IV.2 Holographic Codes in Practice

We close with a short discussion on the practical implications of our findings. In this work, we have investigated the threshold of holographic codes with respect to _code-capacity_ noise channels. Although it has not been confirmed whether or not holographic codes admit a fault-tolerance threshold \[deconfinement\], it seems unreasonable to suspect otherwise, given the fact that the threshold data we have presented here is comparable to many state-of-the-art code families. A first step could be to test _phenomenological_ noise models, i.e., those that incorporate measurement noise into the syndrome-extraction process. This goal could in principle be achieved by mapping the tensor network to a _detector picture_, as was recently performed in \[renes\_2d\], thereby facilitating large-scale circuit-level noise simulations.

In the interim, one can consider techniques by which full fault-tolerant syndrome extraction and universal logic can be performed. \[yamasaki1, yamasaki2, goto\_many\_hypercube\] proved that generalized concatenated code schemes based on the quantum Hamming code can exhibit constant space overhead and quasi-polylogarithmic time overhead. These schemes, all based on code concatenation, involve the use of hard-decision layerwise decoding protocols \[knill2005quantum\]. As it has been proven that holographic quantum codes are specific instances of generalized concatenated codes for the hyperbolic plane \[heterogeneous\_holo\_qrm\], we would surmise that the aforementioned techniques can also be adapted to our setting. This idea is the subject of ongoing research.

Moreover, many alternatives have been suggested as well to the layerwise decoding scheme mentioned above. One method may involve _floquetifying_ holographic codes \[hastings2021dynamically\]; this procedure would solve two problems at once, in that high-weight stabilizers and logical operators could be controlled to a reasonable weight, and fault-tolerance could be guaranteed with an appropriate measurement schedule. In addition to these ideas, fault-tolerant logic has also been shown to be gauge-dependent \[evenbly\_codes2\] and universal in some cases for holographic codes \[heterogeneous\_holo\_qrm\]. Recent work has also made progress on lowering the computational complexity of decoding itself using tensor-network schemes \[gray2021hyperkourtis, hyperoptimized\_approximate\]. These techniques, often based on the analysis of critical or approximate contraction paths, could allow for even faster decoding for error correction and logical operations than is currently employed by tensor-network decoding schemes \[parallel\_decoding\_tn\_codes, farrelly\_tn\_codes\].

One may also ask what specific applications may be well-suited to the usage of a holographic code. An application of holographic codes may be found in _magic-state distillation_\[magic1, magic2\]. Indeed, for the case of the HaPPY and holographic Steane codes, the transversal logical S​H¯\\overline{SH} and H¯\\bar{H} gates allow for current state-of-the-art methods to be leveraged, as was pointed out in \[magic3\]. For practical quantum error correction, it is known that the square-lattice GKP code admits an induced X​ZXZ 2-Pauli noise channel under a symmetric Gaussian random displacement noise model \[bosonic1, bosonic2, bosonic3, bosonic4\], and also that Pauli-twirling the amplitude damping channel results in biased 2-Pauli noise \[amp\_damping\_twirl\]. Such applications could be combined with our work in the future.

Finally, although noise biases can lead to remarkable threshold improvements, it is well known that such gains can be erased in the experimental setting, principally due to complications with gate operations which can unbias the dominant noise channel \[puri2020bias\]. As holographic codes approach experimental realization, such considerations will also be necessary.

### IV.3 Acknowledgements

We thank Aritra Sarkar, David Elkouss, and Jens Eisert for discussions related to concatenated codes and quantum channel capacity, and Sivaprasad Omanakuttan for mentioning issues related to bias preservation, principally investigated in \[puri2020bias\]. We also thank Mackenzie Shaw and Kathleen Chang for mentioning at the conference FTQC ’24 in Benasque several realistic examples of 2-Pauli noise arising in practical quantum computing. MS and SF acknowledge financial support from the Intel corporation. AJ is supported by the Einstein Research Unit “Perspectives of a quantum digital transformation”.

### IV.4 Author Contributions

JF developed and implemented the tensor-network decoder during his master thesis, under the supervision of MS and SF. MS, CC, and AJ wrote the manuscript. AJ, CC, and SF provided project guidance.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="holographic-codes-error-correction-zoo.md">
<details>
<summary>Holographic codes | Error Correction Zoo</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://errorcorrectionzoo.org/list/holographic>

# Holographic codes | Error Correction Zoo

| Code | Description |
| --- | --- |
| A member of the family of \\(\[\[7^m,1,3^m\]\]\\) CSS codes, each of which is a recursive level-\\(m\\) concatenation of the Steane code. This family is one of the first to admit a [concatenated threshold](https://errorcorrectionzoo.org/c/qubits_into_qubits#defterm-Computational_20Xthreshold)\[ [1](https://errorcorrectionzoo.org/list/holographic#citation-1)– [5](https://errorcorrectionzoo.org/list/holographic#citation-5)\]. |
| Approximate code whose codewords lie in the low-energy subspace of a conformal field theory, e.g., the quantum Ising model at its critical point \[ [6](https://errorcorrectionzoo.org/list/holographic#citation-6), [7](https://errorcorrectionzoo.org/list/holographic#citation-7)\]. Its encoding is argued to perform source coding (i.e., compression) as well as channel coding (i.e., error correction) [\[6\]](https://errorcorrectionzoo.org/list/holographic#citation-6). |
| Holographic tensor-network code constructed out of a network of encoding isometries of the Steane code. Depending on how the isometry tensors are contracted, there is a zero-rate and a finite-rate code family. |
| Block quantum code whose features serve to model aspects of the AdS/CFT holographic duality and, more generally, quantum gravity. |
| Quantum Lego code whose encoding isometry forms a holographic tensor network, i.e., a tensor network associated with a tiling of hyperbolic space. Physical qubits are associated with uncontracted tensor legs at the boundary of the tessellation, while logical qubits are associated with uncontracted legs in the bulk. The number of layers emanating from the central point of the tiling is the radius of the code. |
| Holographic tensor-network code constructed out of a hyperinvariant tensor network [\[8\]](https://errorcorrectionzoo.org/list/holographic#citation-8), i.e., a MERA-like network admitting a hyperbolic geometry. The network is defined using two layers A and B, with constituent tensors satisfying isometry conditions (a.k.a. multitensor constraints). |
| An approximate quantum error-correcting code that protects the encoded interior of a black hole from computationally bounded exterior observers. Under the assumption that the Hawking radiation emitted by an old black hole is pseudorandom, there exists a subspace of the radiation system that encodes the black hole interior, entangled with the late outgoing Hawking quanta. The logical operators of this code, called ghost operators in [\[9\]](https://errorcorrectionzoo.org/list/holographic#citation-9), commute with efficient operations acting on the radiation, protecting the interior up to corrections exponentially small in the black hole’s entropy. The construction is state dependent: the encoding depends on the state that collapsed to form the black hole [\[9\]](https://errorcorrectionzoo.org/list/holographic#citation-9). |
| Multimode Fock-state bosonic approximate code derived from a matrix model, i.e., a bosonic theory with a large non-Abelian gauge group. The model’s degrees of freedom are matrix-valued bosons \\(a\\), each consisting of \\(N^2\\) harmonic oscillator modes and subject to an \\(SU(N)\\) gauge symmetry. |
| Holographic code constructed from six-leg five-qubit [perfect tensors](https://errorcorrectionzoo.org/c/ame#defterm-Absolutely_20Xmaximally_20Xentangled_20X_28XAME_29X_20Xstate) placed on hyperbolic pentagon and hexagon tilings. The code serves as a minimal model for several aspects of the AdS/CFT holographic duality [\[10\]](https://errorcorrectionzoo.org/list/holographic#citation-10) and potentially a dS/CFT duality [\[11\]](https://errorcorrectionzoo.org/list/holographic#citation-11). |
| Code whose codespace is spanned by \\(q\\) field-theoretic coherent states which are flowing under the renormalization group (RG) flow of massive free fields. The code approximately protects against displacements that represent local (i.e., short-distance, ultraviolet, or UV) operators. Intuitively, this is because RG cat codewords represent non-local (i.e., long-distance) degrees of freedom, which should only be excitable by acting on a macroscopically large number of short-distance degrees of freedom. |
| Approximate \\(n\\)-fermionic code whose codewords are low-energy states of the Sachdev-Ye-Kitaev (SYK) Hamiltonian \[ [12](https://errorcorrectionzoo.org/list/holographic#citation-12), [13](https://errorcorrectionzoo.org/list/holographic#citation-13)\] or other low-rank SYK models \[ [14](https://errorcorrectionzoo.org/list/holographic#citation-14), [15](https://errorcorrectionzoo.org/list/holographic#citation-15)\]. |
| Holographic tensor-network code constructed out of a network of encoding isometries of the \\(\[\[6,1,3\]\]\\) six-qubit stabilizer code. The structure of the isometry is similar to that of the heptagon holographic code since both isometries are rank-six tensors, but the isometry in this case is neither a [perfect tensor](https://errorcorrectionzoo.org/c/ame#defterm-Absolutely_20Xmaximally_20Xentangled_20X_28XAME_29X_20Xstate) nor a [planar-perfect tensor](https://errorcorrectionzoo.org/c/block_perfect). |
| A holographic tensor-network code constructed out of alternating isometries of the five-qubit and \\(\[\[4,1,1,2\]\]\\) Bacon-Shor codes. |
| Holographic tensor-network code constructed out of a network of encoding isometries of the \\(\[\[5,1,2\]\]\\) rotated surface code. The structure of the isometry is similar to that of the HaPPY code since both isometries are rank-six tensors. In the case of the SCF holographic code, the isometry is only a [planar-perfect tensor](https://errorcorrectionzoo.org/c/block_perfect) (as opposed to a [perfect tensor](https://errorcorrectionzoo.org/c/ame#defterm-Absolutely_20Xmaximally_20Xentangled_20X_28XAME_29X_20Xstate)). |
| A \\(\[\[3,1,2\]\]\_3\\) prime-qudit CSS code that is the smallest qutrit stabilizer code to detect a single-qutrit error. It has stabilizer generators \\(ZZZ\\) and \\(XXX\\). The code defines a quantum secret-sharing scheme and serves as a minimal model for the AdS/CFT holographic duality. It is also the smallest non-trivial instance of a quantum maximum distance separable code (QMDS), saturating the quantum Singleton bound. |
| A rotated surface code on one rung of a ladder, with one qubit on the rung, and four qubits surrounding it. This is the smallest code that implements a fault-tolerant logical \\(S\\) gate using a diagonal depth-one Clifford circuit [\[16\]](https://errorcorrectionzoo.org/list/holographic#citation-16). |
| Five-qubit cyclic stabilizer code that is the smallest qubit stabilizer code to correct a single-qubit error. |
| A degenerate, non-trivial \\(\[\[6,1,3\]\]\\) stabilizer code. It is one of two six-qubit distance-three codes that are unique up to equivalence [\[17\]](https://errorcorrectionzoo.org/list/holographic#citation-17), with the other code being decomposable and an extension of the five-qubit code [\[18\]](https://errorcorrectionzoo.org/list/holographic#citation-18) [\[19; ID 87\]](https://errorcorrectionzoo.org/list/holographic#citation-19). The code admits fault-tolerant syndrome extraction using only one ancilla per stabilizer generator measurement. |
| A \\(\[\[7,1,3\]\]\\) self-dual CSS code that is the smallest qubit CSS code to correct a single-qubit error [\[18\]](https://errorcorrectionzoo.org/list/holographic#citation-18). The code is constructed using the classical binary \\(\[7,4,3\]\\) Hamming code for protecting against both \\(X\\) and \\(Z\\) errors. |

## References

\[1\]E. Knill, R. Laflamme, and W. H. Zurek, “Resilient quantum computation: error models and thresholds”, Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences 454, 365 (1998) [arXiv:quant-ph/9702058](https://arxiv.org/abs/quant-ph/9702058) [DOI](https://doi.org/10.1098%2Frspa.1998.0166)\[2\]A. M. Steane, “Efficient fault-tolerant quantum computing”, Nature 399, 124 (1999) [arXiv:quant-ph/9809054](https://arxiv.org/abs/quant-ph/9809054) [DOI](https://doi.org/10.1038%2F20127)\[3\]A. M. Steane, “Overhead and noise threshold of fault-tolerant quantum error correction”, Physical Review A 68, (2003) [arXiv:quant-ph/0207119](https://arxiv.org/abs/quant-ph/0207119) [DOI](https://doi.org/10.1103%2Fphysreva.68.042322)\[4\]K. M. Svore, B. M. Terhal, and D. P. DiVincenzo, “Local fault-tolerant quantum computation”, Physical Review A 72, (2005) [arXiv:quant-ph/0410047](https://arxiv.org/abs/quant-ph/0410047) [DOI](https://doi.org/10.1103%2Fphysreva.72.022317)\[5\]K. M. Svore, D. P. DiVincenzo, and B. M. Terhal, “Noise Threshold for a Fault-Tolerant Two-Dimensional Lattice Architecture”, (2006) [arXiv:quant-ph/0604090](https://arxiv.org/abs/quant-ph/0604090)\[6\]F. Pastawski, J. Eisert, and H. Wilming, “Towards Holography via Quantum Source-Channel Codes”, Physical Review Letters 119, (2017) [arXiv:1611.07528](https://arxiv.org/abs/1611.07528) [DOI](https://doi.org/10.1103%2Fphysrevlett.119.020501)\[7\]S. Sang, T. H. Hsieh, and Y. Zou, “Approximate quantum error correcting codes from conformal field theory”, (2024) [arXiv:2406.09555](https://arxiv.org/abs/2406.09555)\[8\]G. Evenbly, “Hyperinvariant Tensor Networks and Holography”, Physical Review Letters 119, (2017) [arXiv:1704.04229](https://arxiv.org/abs/1704.04229) [DOI](https://doi.org/10.1103%2Fphysrevlett.119.141602)\[9\]I. Kim, E. Tang, and J. Preskill, “The ghost in the radiation: robust encodings of the black hole interior”, Journal of High Energy Physics 2020, (2020) [arXiv:2003.05451](https://arxiv.org/abs/2003.05451) [DOI](https://doi.org/10.1007%2Fjhep06(2020)031)\[10\]T. J. Osborne and D. E. Stiegemann, “Dynamics for holographic codes”, Journal of High Energy Physics 2020, (2020) [arXiv:1706.08823](https://arxiv.org/abs/1706.08823) [DOI](https://doi.org/10.1007%2Fjhep04(2020)154)\[11\]J. Cotler and A. Strominger, “The Universe as a Quantum Encoder”, (2022) [arXiv:2201.11658](https://arxiv.org/abs/2201.11658)\[12\]S. Sachdev and J. Ye, “Gapless spin-fluid ground state in a random quantum Heisenberg magnet”, Physical Review Letters 70, 3339 (1993) [arXiv:cond-mat/9212030](https://arxiv.org/abs/cond-mat/9212030) [DOI](https://doi.org/10.1103%2Fphysrevlett.70.3339)\[13\]A. Yu. Kitaev, “A simple model of quantum holography (part 2)”, Entanglement in Strongly-Correlated Quantum Matter (2015): 38\[14\]J. Kim, X. Cao, and E. Altman, “Low-rank Sachdev-Ye-Kitaev models”, Physical Review B 101, (2020) [arXiv:1910.10173](https://arxiv.org/abs/1910.10173) [DOI](https://doi.org/10.1103%2Fphysrevb.101.125112)\[15\]J. Kim, E. Altman, and X. Cao, “Dirac fast scramblers”, Physical Review B 103, (2021) [arXiv:2010.10545](https://arxiv.org/abs/2010.10545) [DOI](https://doi.org/10.1103%2Fphysrevb.103.l081113)\[16\]V. V. Albert, private communication, 2026\[17\]A. R. Calderbank, E. M. Rains, P. W. Shor, and N. J. A. Sloane, “Quantum Error Correction via Codes over GF(4)”, (1997) [arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)\[18\]B. Shaw, M. M. Wilde, O. Oreshkov, I. Kremsky, and D. A. Lidar, “Encoding one logical qubit into six physical qubits”, Physical Review A 78, (2008) [arXiv:0803.1495](https://arxiv.org/abs/0803.1495) [DOI](https://doi.org/10.1103%2Fphysreva.78.012337)\[19\]Qiskit Community, “Qiskit QEC framework”, [URL](https://github.com/qiskit-community/qiskit-qec)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="holographic-codes-from-hyperinvariant-tensor-networks-nature.md">
<details>
<summary>Holographic codes from hyperinvariant tensor networks | Nature Communications</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.nature.com/articles/s41467-023-42743-z>

# Holographic codes from hyperinvariant tensor networks | Nature Communications

Holographic codes from hyperinvariant tensor networks

## Abstract

Holographic quantum-error correcting codes are models of bulk/boundary dualities such as the anti-de Sitter/conformal field theory (AdS/CFT) correspondence, where a higher-dimensional bulk geometry is associated with the code’s logical degrees of freedom. Previous discrete holographic codes based on tensor networks have reproduced the general code properties expected from continuum AdS/CFT, such as complementary recovery. However, the boundary states of such tensor networks typically do not exhibit the expected correlation functions of CFT boundary states. In this work, we show that a new class of exact holographic codes, extending the previously proposed hyperinvariant tensor networks into quantum codes, produce the correct boundary correlation functions. This approach yields a dictionary between logical states in the bulk and the critical renormalization group flow of boundary states. Furthermore, these codes exhibit a state-dependent breakdown of complementary recovery as expected from AdS/CFT under small quantum gravity corrections.

## Introduction

The field of quantum error correction, while relevant for many practical applications in the context of quantum computation, also has deep connections to high-energy theory and quantum gravity. This is exemplified by the anti-de Sitter/conformal field theory (AdS/CFT) correspondence, a conjectured duality relating _d_ + 1-dimensional bulk quantum gravity on an asymptotically AdS space-time background to a _d_-dimensional CFT on its boundary[1](https://www.nature.com/articles/s41467-023-42743-z#ref-CR1 "Maldacena, J. M. The Large N limit of superconformal field theories and supergravity. Adv. Theor. Math. Phys. 2, 231 (1998)."), [2](https://www.nature.com/articles/s41467-023-42743-z#ref-CR2 "Witten, E. Anti-de Sitter space and holography. Adv. Theor. Math. Phys. 2, 253 (1998)."). This duality implies a dictionary between operators and fields between these two theories, and the details of this dictionary exhibit the defining features of a quantum error-correcting code[3](https://www.nature.com/articles/s41467-023-42743-z#ref-CR3 "Almheiri, A., Dong, X. & Harlow, D. Bulk locality and quantum error correction in AdS/CFT. JHEP 04, 163 (2015)."). Concretely, AdS/CFT relies on a parameter _N_ that characterizes both theories: While it counts the number of degrees of freedom of the boundary CFT, in the bulk the value of _N_ determines the effective gravitational strength in terms of the gravitational constant _G_ ~ 1/ _N_ 2 (in units where _ℏ_ = _c_ = 1) and thus the quantum-ness of the bulk: In the _N_ → _∞_ limit, the bulk theory is merely semi-classical gravity, while finite values of _N_ imply quantum gravity corrections. Although non-perturbative quantum gravity is poorly understood, the most popular setting of AdS/CFT is in this _N_ → _∞_ limit, potentially including perturbative corrections. It is this limit in which the code structure of AdS/CFT becomes most apparent: Counter-intuitively, the number of degrees of freedom of a bulk field on a semi-classical AdS background, when restricted onto a chosen time-slice at time _t_ and made finite via discretization and a radial cutoff, is smaller than that of the boundary CFT state. This is because considering only bulk states on a fixed semi-classical geometry imposes a restriction on the boundary Hilbert space, leaving out CFT states that are dual to a non-geometrical bulk or contain strong back-reaction (such as black hole states). As a result, the AdS/CFT dictionary becomes an (approximately) isometric code between bulk and boundary: The logical space of states associated with a semi-classical AdS geometry are encoded in a code subspace of the boundary CFT states[3](https://www.nature.com/articles/s41467-023-42743-z#ref-CR3 "Almheiri, A., Dong, X. & Harlow, D. Bulk locality and quantum error correction in AdS/CFT. JHEP 04, 163 (2015)."). This encoding has peculiar geometric features: As shown in Fig. [1](https://www.nature.com/articles/s41467-023-42743-z#Fig1) a, a region _A_ of the boundary CFT can be associated with an _entanglement wedge a_, bulk information in which can be fully represented on _A_. Conversely, any local bulk information around a point _x_ can be represented on any boundary region whose entanglement wedge contains it[4](https://www.nature.com/articles/s41467-023-42743-z#ref-CR4 "Dong, X., Harlow, D. & Wall, A. C. Reconstruction of bulk operators within the entanglement wedge in gauge-gravity duality. Phys. Rev. Lett. 117, 021601 (2016)."), [5](https://www.nature.com/articles/s41467-023-42743-z#ref-CR5 "Bao, N. & Kim, I. H. Precursor problem and holographic mutual information. Preprint at arXiv                    https://doi.org/10.48550/arXiv.1601.07616                                     (2016)."). For a bipartition \\({{{{{{{\\mathcal{H}}}}}}}}={{{{{{{{\\mathcal{H}}}}}}}}}\_{A}\\otimes {{{{{{{{\\mathcal{H}}}}}}}}}\_{{A}^{c}}\\) of the boundary Hilbert space (which is finite-dimensional due to the bulk discretization and cutoff), any such local bulk information can be represented on _A_ or _A_ _c_, but not both, a feature known as _complementary recovery_. In the bulk, _a_ and _a_ _c_ are separated by the Ryu–Takayanagi (RT) surface _γ_ _A_, a geodesic (extremal surface in higher dimensions) whose area determines the dominant _O_( _N_ 2) part of boundary entanglement entropy \\({S}\_{A}\\equiv S\[{\\rho }\_{A}\]=-{{{{{{{{\\rm{tr}}}}}}}}}\_{A}({\\rho }\_{A}\\log {\\rho }\_{A})\\) at large _N_ [6](https://www.nature.com/articles/s41467-023-42743-z#ref-CR6 "Ryu, S. & Takayanagi, T. Holographic derivation of entanglement entropy from AdS/CFT. Phys. Rev. Lett. 96, 181602 (2006)."), where \\({\\rho }\_{A}={{{{{{{{\\rm{tr}}}}}}}}}\_{{A}^{c}}(\\rho )\\) is the reduced density matrix of subregion _A_. Explicitly including _O_( _N_ 0) corrections, it is given by[7](https://www.nature.com/articles/s41467-023-42743-z#ref-CR7 "Faulkner, T., Lewkowycz, A. & Maldacena, J. Quantum corrections to holographic entanglement entropy. JHEP 11, 074 (2013)."), [8](https://www.nature.com/articles/s41467-023-42743-z#ref-CR8 "Lewkowycz, A. & Maldacena, J. Generalized gravitational entropy. JHEP 08, 090 (2013)."), [9](https://www.nature.com/articles/s41467-023-42743-z#ref-CR9 "Barrella, T., Dong, X., Hartnoll, S. A. & Martin, V. L. Holographic entanglement beyond classical gravity. JHEP 09, 109 (2013).")

$${S}\_{A}=\\frac{{{{{{{\\mathrm{area}}}}}}}\\,({\\gamma }\_{A})}{4G}+{S}\_{a}+O(G),$$

(1)

where _S_ _a_ is the bulk entropy between _a_ and _a_ _c_. As we consider quantum effects in the bulk, area( _γ_ _A_) should formally become an expectation value of an area operator. It has been conjectured that ( [1](https://www.nature.com/articles/s41467-023-42743-z#Equ1)) becomes exact in all orders of _G_ if one replaces _γ_ _A_ by a _quantum extremal surface_, extremizing the entire (quantum) entropy rather than the classical area[10](https://www.nature.com/articles/s41467-023-42743-z#ref-CR10 "Engelhardt, N. & Wall, A. C. Quantum extremal surfaces: holographic entanglement entropy beyond the classical regime. JHEP 01, 073 (2015)."). The general form of ( [1](https://www.nature.com/articles/s41467-023-42743-z#Equ1)) is a direct consequence of the holographic code properties[11](https://www.nature.com/articles/s41467-023-42743-z#ref-CR11 "Harlow, D. The Ryu-Takayanagi formula from quantum error correction. Commun. Math. Phys. 354, 865 (2017).").

**Fig. 1: Complementary recovery in holography.**

https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-023-42743-z/MediaObjects/41467_2023_42743_Fig1_HTML.png

[Full size image](https://www.nature.com/articles/s41467-023-42743-z/figures/1)

**a** In continuum AdS/CFT on slices at constant time _t_, a bipartition of the boundary CFT into two regions _A_ and _A_ _c_ is equivalent to a bipartition of the bulk into two entanglement wedges _a_ and _a_ _c_, separated by a Ryu–Takayanagi surface _γ_ _A_. Any bulk (field) operator _ϕ_( _x_) can be fully reconstructed on either _A_ or _A_ _c_, but not both. **b** In the holographic tensor network code introduced here, a boundary bipartition leads to bulk wedges that are separated by a large residual region (white); an operator _ϕ_ in this region cannot generally be reconstructed on either _A_ and _A_ _c_.

Both complementary recovery and a form of ( [1](https://www.nature.com/articles/s41467-023-42743-z#Equ1)) can be readily reproduced in discrete toy models of holography, most notable the family of perfect holographic codes, also known as HaPPY codes after their creators[12](https://www.nature.com/articles/s41467-023-42743-z#ref-CR12 "Pastawski, F., Yoshida, B., Harlow, D. & Preskill, J. Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence. JHEP 06, 149 (2015)."). These codes are based on tensor networks of so-called perfect tensors arranged on a regular hyperbolic lattice, producing a code between logical qubits within the bulk of the tensor network and physical qubits on its boundary. In this discretization, the Ryu–Takayanagi surface _γ_ _A_ becomes a cut through the tensor network. The bulk area term _S_ _a_ in ( [1](https://www.nature.com/articles/s41467-023-42743-z#Equ1)) becomes nonzero once the logical state in the bulk contains entanglement between _a_ and _a_ _c_. HaPPY codes can be constructed on various hyperbolic tilings and for higher local dimensions (i.e., with qudits instead of qubits). While this model reproduces the quantum error correction properties of AdS/CFT up to bulk discretization artifacts, the boundary code space does not contain states that can be readily associated with physical CFT states. While the entanglement entropy scaling agrees with results for critical states[12](https://www.nature.com/articles/s41467-023-42743-z#ref-CR12 "Pastawski, F., Yoshida, B., Harlow, D. & Preskill, J. Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence. JHEP 06, 149 (2015)."), [13](https://www.nature.com/articles/s41467-023-42743-z#ref-CR13 "Jahn, A., Gluza, M., Pastawski, F. & Eisert, J. Holography and criticality in matchgate tensor networks. Sci. Adv. 5, eaaw0092 (2019)."), the expected smooth polynomial decay of _n_-point correlation functions with distance is precluded by the code properties of the model; for example, simple spin-spin correlation functions such as \\(\\langle {X}\_{j}{X}\_{k}\\rangle\\) of Pauli _X_ operators between sites _j_, _k_ always vanish in the {4, 5} pentagon code, the standard example of a HaPPY code, as such operators are equivalent to correctable errors whose measurement cannot reveal any logical code information. Such correlation functions, while unphysical for finite _N_ CFTs, in fact accurately reflect the _N_ → _∞_ limit of AdS/CFT (and more generally of _fixed area states_ [14](https://www.nature.com/articles/s41467-023-42743-z#ref-CR14 "Akers, C. & Rath, P. Holographic Renyi entropy from quantum error correction. JHEP 05, 052 (2019)."), [15](https://www.nature.com/articles/s41467-023-42743-z#ref-CR15 "Dong, X., Harlow, D. & Marolf, D. Flat entanglement spectra in fixed-area states of quantum gravity. JHEP 10, 240 (2019).")), where all but the first term in ( [1](https://www.nature.com/articles/s41467-023-42743-z#Equ1)) dominate. For the mutual information _I_( _A_: _B_) = _S_ _A_ + _S_ _B_ − _S_ _A_ ∪ _B_ of two subregions _A_ and _B_, this limit suggests that for distances between _A_ and _B_ much larger than their sizes, two-point correlations exactly vanish by virtue of the bound

$$I(A:B)\\ge \\frac{{\\left(\\langle {{{{{{{{\\mathcal{O}}}}}}}}}\_{A}{{{{{{{{\\mathcal{O}}}}}}}}}\_{B}\\rangle -\\langle {{{{{{{{\\mathcal{O}}}}}}}}}\_{A}\\rangle \\langle {{{{{{{{\\mathcal{O}}}}}}}}}\_{B}\\rangle \\right)}^{2}}{2\| \| {{{{{{{{\\mathcal{O}}}}}}}}}\_{A}\| {\| }^{2}\| \| {{{{{{{{\\mathcal{O}}}}}}}}}\_{B}\| {\| }^{2}},$$

(2)

where \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{A,B}\\) are arbitrary Hermitian operators acting on _A_ and _B_, respectively. In continuum AdS/CFT, physical correlation functions are restored by the subdominant bulk entropy term _S_ _a_ into ( [1](https://www.nature.com/articles/s41467-023-42743-z#Equ1)). In the HaPPY code picture, a nonzero bulk term requires logical bulk states with long-distance entanglement, resembling the entanglement structure of bulk quantum fields. However, due the discretization of the bulk space, such entanglement is not resolved on sizes below the curvature radius (the size of a single tile), while in continuum AdS/CFT this sub-cutoff entanglement would become part of the area term[16](https://www.nature.com/articles/s41467-023-42743-z#ref-CR16 "Gesteau, E. Large N von Neumann algebras and the renormalization of Newton’s constant. Preprint at arXiv                    https://doi.org/10.48550/arXiv.2302.01938                                     (2023)."). As a result of this discretization, the code’s resilience against small errors makes logical bulk states inaccessible to small boundary operators, causing their correlation functions to vanish.

Building holographic codes with physical boundary correlations thus seems to require breaking the encoding map \\(V:{{{{{{{{\\mathcal{H}}}}}}}}}\_{{{{{{{{\\rm{bulk}}}}}}}}}\\to {{{{{{{{\\mathcal{H}}}}}}}}}\_{{{{{{{{\\rm{bdy}}}}}}}}}\\) from an exact isometry (with \\({V}^{{{{\\dagger}}} }V={\\mathbb{1}}\\)) to an approximate one. Indeed, this has been argued to hold for codes describing continuum AdS/CFT as a consequence of the Reeh–Schlieder theorem for boundary quantum fields[17](https://www.nature.com/articles/s41467-023-42743-z#ref-CR17 "Kelly, W. R. Bulk locality and entanglement swapping in AdS/CFT. JHEP 03, 153 (2017)."), [18](https://www.nature.com/articles/s41467-023-42743-z#ref-CR18 "Faulkner, T. The holographic map as a conditional expectation. Preprint at arXiv                    https://doi.org/10.48550/arXiv.2008.04810                                     (2020)."). Tensor network models of holographic codes with approximate encoding have previously been constructed[19](https://www.nature.com/articles/s41467-023-42743-z#ref-CR19 "Hayden, P. et al. Holographic duality from random tensor networks. JHEP 11, 009 (2016)."), [20](https://www.nature.com/articles/s41467-023-42743-z#ref-CR20 "Cao, C. & Lackey, B. Approximate Bacon-Shor code and holography. JHEP 05, 127 (2021).") and indeed allow for less constrained correlation functions that can decay polynomially. However, as they break exact bulk reconstruction, their features, e.g., state dependence of entanglement wedges, are difficult to analyze analytically. In addition, approximate encoding isometries cannot be directly implemented in terms of unitary gates in a quantum device. Rather than choosing an approximate encoding map, is it possible to construct holographic codes with physical correlation decay and approximate complementary recovery using an exact map? In Ref. [21](https://www.nature.com/articles/s41467-023-42743-z#ref-CR21 "Cao, C., Pollack, J. & Wang, Y. Hyperinvariant multiscale entanglement renormalization ansatz: approximate holographic error correction codes with power-law correlations. Phys. Rev. D 105, 026018 (2022).") it was argued that any holographic code with local bulk reconstruction (i.e., tensor-by-tensor from boundary to bulk) can only achieve this by breaking the tiling symmetries and placing different tensors on different sites of the tiling.

In this work, we construct an exact tensor network code that preserves the tiling symmetries and still has the desired properties listed above. This requires only a mild relaxation of the local reconstruction property, compatible with expectations for a holographic model with weak gravitational back-reaction, that leads to a soft breaking of complementary recovery for any bipartition (shown in Fig. [1](https://www.nature.com/articles/s41467-023-42743-z#Fig1)). The result is a tractable model of holography under quantum corrections, naturally producing physical correlation functions while relating holographic bulk states to the renormalization group (RG) flow of critical states on the boundary.

## Results

### Perfect holographic codes

We briefly review holographic codes based on perfect tensors on hyperbolic tilings. A regular { _p_, _q_} tiling of _p_-gons, _q_ of which meet at each vertex, is hyperbolic if _p_ _q_ > 2( _p_ + _q_). In our notation, which follows Refs. [22](https://www.nature.com/articles/s41467-023-42743-z#ref-CR22 "Evenbly, G. Hyperinvariant tensor networks and holography. Phys. Rev. Lett. 119, 141602 (2017)."), [23](https://www.nature.com/articles/s41467-023-42743-z#ref-CR23 "Steinberg, M. & Prior, J. Conformal properties of hyperinvariant tensor networks. Sci. Rep.                    https://doi.org/10.1038/s41598-021-04375-5                                     (2022).") and is related to that of Ref. [12](https://www.nature.com/articles/s41467-023-42743-z#ref-CR12 "Pastawski, F., Yoshida, B., Harlow, D. & Preskill, J. Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence. JHEP 06, 149 (2015).") by a _p_ ↔ _q_ duality transformation, the vertices are associated with tensors that each have _q_ planar legs, with a loop of contractions between _p_ tensors around each tile. To form a bulk/boundary code, each tensor \\({T}\_{j,{i}\_{1},{i}\_{2},\\ldots,{i}\_{q}}\\) has a bulk logical index _j_ representing the logical qudit of (bond) dimension _d_, and _q_ planar physical indices, each of dimension _χ_, usually chosen as _χ_ = _d_. The tensor thus serves as an encoding isometry _V_ _T_ mapping a logical qudit state vector \\(\\left\|\\psi \\right\\rangle\\) to its physical encoding on _q_ sites,

$${V}\_{T}\\Big \| \\psi \\Big\\rangle=\\mathop{\\sum }\\limits\_{j=1}^{d}\\mathop{\\sum }\\limits\_{{i}\_{1},\\ldots,{i}\_{q}=1}^{\\chi }{T}\_{j,{i}\_{1},\\ldots,{i}\_{q}}\\Big \\langle j \\Big\| \\psi \\Big \\rangle \\Big \| {i}\_{1},\\ldots,{i}\_{q}\\Big \\rangle$$

(3)

For simplicity, we assume that the tensors follow the same symmetries as the (infinite) tiling, i.e., the same tensor is placed on each vertex and they are rotationally invariant under permutations of the physical indices, \\({T}\_{j,{i}\_{1},{i}\_{2},\\ldots,{i}\_{q}}={T}\_{j,{i}\_{q},{i}\_{1},\\ldots,{i}\_{q-1}}\\). For the construction of holographic toy models proposed in Ref. [12](https://www.nature.com/articles/s41467-023-42743-z#ref-CR12 "Pastawski, F., Yoshida, B., Harlow, D. & Preskill, J. Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence. JHEP 06, 149 (2015)."), one further assumes that the tensor _T_ is _perfect_, defined as forming an isometry for any bipartition of its indices. More generally, a tensor _T_ is defined to be _k_-isometric (or equivalently, _k_-uniform[24](https://www.nature.com/articles/s41467-023-42743-z#ref-CR24 "Enriquez, M., Wintrowicz, I. & Życzkowski, K. Maximally entangled multipartite states: a brief survey. J. Phys. Conf. Ser. 698, 012003 (2016).")) if for any index bipartition into a set _S_ with ∣ _S_ ∣ = _k_ indices and its complement _S_ _c_,

$$\\mathop{\\sum}\\limits\_{{S}^{c}}{T}\_{S,{S}^{c}}{T}\_{{S}^{{\\prime} },{S}^{c}}^{\\star }\\propto {\\delta }\_{S,{S}^{{\\prime} }},$$

(4)

where the sum runs over all indices in _S_ _c_, and \\({T}\_{S,{S}^{c}}\\) is the tensor under the index bipartition. Under this definition, a tensor \\({T}\_{j,{i}\_{1},{i}\_{2},\\ldots,{i}\_{q}}\\) is perfect if it is _k_-isometric for any \\(k\\le \\lfloor \\frac{q+1}{2}\\rfloor\\). A quantum state represented by such a tensor thus appears maximally mixed to any observer with access to only _k_ sites or fewer. For perfect tensors, these states are given by absolutely maximally entangled (AME) states[24](https://www.nature.com/articles/s41467-023-42743-z#ref-CR24 "Enriquez, M., Wintrowicz, I. & Życzkowski, K. Maximally entangled multipartite states: a brief survey. J. Phys. Conf. Ser. 698, 012003 (2016)."), [25](https://www.nature.com/articles/s41467-023-42743-z#ref-CR25 "Goyeneche, D., Alsina, D., Latorre, J. I., Riera, A. & Życzkowski K. Absolutely maximally entangled states, combinatorial designs, and multiunitary matrices. Phys. Rev.                    https://doi.org/10.1103/physreva.92.032316                                     (2015)."), [26](https://www.nature.com/articles/s41467-023-42743-z#ref-CR26 "Raissi, Z. Modifying method of constructing quantum codes from highly entangled states. IEEE Access 8, 222439–222448 (2020)."), [27](https://www.nature.com/articles/s41467-023-42743-z#ref-CR27 "Raissi, Z., Teixido, A., Gogolin, C. & Acin A. Constructions of k-uniform and absolutely maximally entangled states beyond maximum distance codes. Phys. Rev. Res.                    https://doi.org/10.1103/physrevresearch.2.033411                                     (2020)."), [28](https://www.nature.com/articles/s41467-023-42743-z#ref-CR28 "Raissi, Z., Gogolin, C., Riera, A. & Acin, A. Optimal quantum error correcting codes from absolutely maximally entangled states. J. Phys. A 51, 075301 (2018)."), [29](https://www.nature.com/articles/s41467-023-42743-z#ref-CR29 "Mazurek, P., Farkas, M., Grudka, A., Horodecki, M. & Studziński, M. Quantum error-correction codes and absolutely maximally entangled states. Phys. Rev. A 101, 042305 (2020).").

Given this definition, a HaPPY code is then defined as a tensor network of perfect tensors over a hyperbolic tiling, such that contraction over the physical indices between adjacent tiles/tensors results in an isometry from the bulk degrees of freedom to the physical degrees of freedom on the tiling boundary. As a regular tiling of the hyperbolic disk contains infinitely many tiles, this boundary can either be defined asymptotically or by some finite cutoff after a certain number of layers of tiles. The isometry condition for the bulk-to-boundary map _V_ follows immediately for most { _p_, _q_} tilings, as the evaluation of _V_† _V_ can be decomposed into partial contractions between each perfect tensor _T_ and its complex conjugate _T_ ⋆, resulting in expressions of the form ( [4](https://www.nature.com/articles/s41467-023-42743-z#Equ4)). Graphically, this tile-by-tile reduction can be expressed by a greedy algorithm that iteratively pushes the tiling boundary into the bulk whenever this reduces the number of indices, corresponding to an application of the isometric map induced by any individual perfect tensor _T_ (see Fig. [2](https://www.nature.com/articles/s41467-023-42743-z#Fig2)). An example where the greedy algorithm fails is the {7, 3} tiling, where no local pushing (greedy step) reduces the number of indices. Indeed, a simple dimensional counting argument shows that a {7, 3} tensor network of perfect tensors does not form an isometry and hence does not define a code. Fortunately, a non-trivial greedy algorithm can be applied to any perfect tensor network on a { _p_, _q_} regular tiling with _q_ > 3, such as the {4, 5} hyperbolic pentagon code introduced in Ref. [12](https://www.nature.com/articles/s41467-023-42743-z#ref-CR12 "Pastawski, F., Yoshida, B., Harlow, D. & Preskill, J. Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence. JHEP 06, 149 (2015)."). HaPPY codes reproduce the AdS/CFT property of complementary recovery (Fig. [1](https://www.nature.com/articles/s41467-023-42743-z#Fig1)) in that the greedy algorithm applied to a boundary region _A_ and its complement _A_ _c_ will terminate at the same cut through the tiling – the discretized Ryu-Takayanagi surface _γ_ _A_ – for almost all choices of _A_. The union of the bulk regions _a_ and _a_ _c_ that are recoverable from _A_ and _A_ _c_, respectively, then fills the entire bulk. As described above, exact complementary recovery is expected from AdS/CFT at _N_ → _∞_, but creates problems for discrete holographic codes where code states are supposed to be related to CFTs and hence exhibit smoothly decaying correlation functions. A related problem arises when considering HaPPY codes from an RG perspective: In a tensor network representation of critical systems[30](https://www.nature.com/articles/s41467-023-42743-z#ref-CR30 "Vidal, G. Class of quantum many-body states that can be efficiently simulated. Phys. Rev. Lett. 101, 110501 (2008)."), [31](https://www.nature.com/articles/s41467-023-42743-z#ref-CR31 "Pfeifer, R. N. C., Evenbly, G. & Vidal, G. Entanglement renormalization, scale invariance, and quantum criticality. Phys. Rev. 79, 040301 (2009)."), the lattice version of a primary operator is an eigen-operator of the _scaling superoperator_, a map constructed from a single radial layer of tensor networks and its conjugate. However, the error-correcting properties of HaPPY codes are too strong to allow for non-trivial single-site operators to be preserved even under a single layer of the tensor network, as Fig. [3](https://www.nature.com/articles/s41467-023-42743-z#Fig3) a shows. As a consequence, HaPPY codes cannot be related to any particular critical lattice theory with a spectrum of primary fields, a desirable feature of a discrete model of AdS/CFT.

**Fig. 2: Bulk reconstruction in HaPPY codes.**

https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-023-42743-z/MediaObjects/41467_2023_42743_Fig2_HTML.png

[Full size image](https://www.nature.com/articles/s41467-023-42743-z/figures/2)

**a** A tensor network on a regular hyperbolic {4, 5} tiling, defining a map _V_ from logical bulk legs (red) to physical boundary legs (black). **b** Conditions of the form ( [4](https://www.nature.com/articles/s41467-023-42743-z#Equ4)) for perfect pentagon tensors, the choice of which makes _V_ isometric and produces a HaPPY code. Dark-shaded tensors are conjugated. **c** The perfect tensor conditions define steps in a greedy algorithm for iteratively reconstructing the bulk from a boundary region _A_ (bulk legs not drawn). **d** The greedy algorithm terminates at a minimal cut _γ_ _A_, a discrete Ryu–Takayanagi surface. Within the wedge _a_ bounded by _A_ ∪ _γ_ _A_, logical operators can be isometrically mapped to _A_.

**Fig. 3: Coarse-graining renormalization group step of a one-site operator.**

https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-023-42743-z/MediaObjects/41467_2023_42743_Fig3_HTML.png

[Full size image](https://www.nature.com/articles/s41467-023-42743-z/figures/3)

**a** In the {4, 5} HaPPY code, any single-site operator \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau }\\) on layer _τ_ of the tiling is a correctable error, and mapped to the identity on layer _τ_ + 1\. **b** In the {5, 4} HTN code, \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau }\\) is generally mapped to a local \\({{{{{{{\\mathcal{S}}}}}}}}({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau })={{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau+1}\\ne {\\mathbb{1}}\\), hence allowing for non-trivial single-site lattice primary operator with \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau+1}\\propto {{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau }\\). Tensors shaded in dark are conjugated, and red dots represent logical degrees of freedom, with legs suppressed.

### Hyperinvariant tensor networks

For the case of tensor networks without logical degrees of freedom, i.e., representations of holographic states rather than codes, the problem of non-trivial primary operators was resolved in Ref. [22](https://www.nature.com/articles/s41467-023-42743-z#ref-CR22 "Evenbly, G. Hyperinvariant tensor networks and holography. Phys. Rev. Lett. 119, 141602 (2017).") with the introduction of hyperinvariant tensor networks (HTN). This class of tensor networks has the same geometry as HaPPY codes, i.e., are constructed on a regular { _p_, _q_} hyperbolic tiling, with a _q_-leg vertex tensor _A_ placed on each vertex. In addition, for each edge a 2-leg edge tensor _B_ is contracted between two vertex tensors. For the choice of perfect _A_ and a splittable _B_ = _U_ _U_ T with unitary _U_ (in particular, \\(B=U={\\mathbb{1}}\\)), this construction just corresponds to a HaPPY code with the logical bulk projected onto a product state. However, HTNs allow for more general choices of _A_ and _B_ where layers of the tiling are both isometric and form super-operators with non-trivial spectra[22](https://www.nature.com/articles/s41467-023-42743-z#ref-CR22 "Evenbly, G. Hyperinvariant tensor networks and holography. Phys. Rev. Lett. 119, 141602 (2017)."), [23](https://www.nature.com/articles/s41467-023-42743-z#ref-CR23 "Steinberg, M. & Prior, J. Conformal properties of hyperinvariant tensor networks. Sci. Rep.                    https://doi.org/10.1038/s41598-021-04375-5                                     (2022)."), resulting in a tensor network similar to the MERA[30](https://www.nature.com/articles/s41467-023-42743-z#ref-CR30 "Vidal, G. Class of quantum many-body states that can be efficiently simulated. Phys. Rev. Lett. 101, 110501 (2008).") but with the geometry of HaPPY model. As we will now show, these conditions are general enough to also include holographic codes, i.e., HTNs whose vertex tensors have additional bulk legs and form an isometry from bulk to boundary. The main HTN model introduced in Ref. [22](https://www.nature.com/articles/s41467-023-42743-z#ref-CR22 "Evenbly, G. Hyperinvariant tensor networks and holography. Phys. Rev. Lett. 119, 141602 (2017)."), based on a {7, 3} tiling with 3-leg vertex tensors, can be immediately excluded from such an extension: Just as in the case of HaPPY codes, adding a bulk leg to every vertex of a {7, 3} tiling leads to more degrees of freedom in the bulk than on the boundary, ruling out a bulk-to-boundary isometry. Here we assume for simplicity that the local Hilbert spaces of each bulk and boundary leg has the same dimension _χ_. Upon closer inspection, one also finds that the HTN isometry conditions that would define a corresponding greedy algorithm cannot be fulfilled if the {7, 3} vertex tensors are associated with bulk qudits. However, the second HTN model from Ref. [22](https://www.nature.com/articles/s41467-023-42743-z#ref-CR22 "Evenbly, G. Hyperinvariant tensor networks and holography. Phys. Rev. Lett. 119, 141602 (2017)."), based on a {5, 4} tiling, is a viable candidate for an HTN code: Here the two isometry conditions (known as _multitensor constraints_ in[22](https://www.nature.com/articles/s41467-023-42743-z#ref-CR22 "Evenbly, G. Hyperinvariant tensor networks and holography. Phys. Rev. Lett. 119, 141602 (2017).")), the first for a single vertex tensor and the second for two neighboring ones, can be extended into reconstruction steps for bulk qudits, which we show in Fig. [4](https://www.nature.com/articles/s41467-023-42743-z#Fig4). The 4-leg tensor _A_ is promoted to a 5-leg tensor \\({A}^{{\\prime} }\\), while the _B_ tensor remains a fixed unitary matrix that does not depend on the bulk state. Note that the isometry conditions differ from the perfect tensor conditions of HaPPY codes (see Fig. [2](https://www.nature.com/articles/s41467-023-42743-z#Fig2)): Firstly, they do not require the \\({A}^{{\\prime} }\\) tensor to be perfect but only 1-isometric for all bipartitions and 2-isometric for those where the smaller side of the bipartition contains the logical leg. Secondly, bulk reconstruction is possible for { _p_, _q_} codes with even _q_, unlike HaPPY codes where a single logical site must be reconstructable from \\(\\lfloor \\frac{q}{2}\\rfloor\\) physical indices. Thirdly, they include the isometric constraints where combinations of neighboring tensors act as larger isometries recovering more than one logical site, in contrast to the HaPPY code’s greedy algorithm acting only on one tensor at a time.

**Fig. 4: Construction of a hyperinvariant tensor network (HTN) code.**

https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-023-42743-z/MediaObjects/41467_2023_42743_Fig4_HTML.png

[Full size image](https://www.nature.com/articles/s41467-023-42743-z/figures/4)

**a** The original HTN construction from Ref. [22](https://www.nature.com/articles/s41467-023-42743-z#ref-CR22 "Evenbly, G. Hyperinvariant tensor networks and holography. Phys. Rev. Lett. 119, 141602 (2017)."), [23](https://www.nature.com/articles/s41467-023-42743-z#ref-CR23 "Steinberg, M. & Prior, J. Conformal properties of hyperinvariant tensor networks. Sci. Rep.                    https://doi.org/10.1038/s41598-021-04375-5                                     (2022).") for a {5, 4} hyperbolic tiling; vertices and edges are associated with _A_ and _B_ tensors, respectively. **b** The isometry constraints for one- and two-vertex combinations of _A_ and _B_. With these constraints, each radial layer of tensors acts isometrically, in the manner of an RG transformation. **c** Implanting an additional leg on each _A_ tensor yields a bulk Hilbert space, with the tensor network acting as a bulk-boundary map. **d** The updated isometry constraints (with logical legs in red) turn the RG step into a bulk reconstruction step. Despite the _A_ tensors not being necessarily perfect as in the HaPPY code (Fig. [2](https://www.nature.com/articles/s41467-023-42743-z#Fig2)), the tensor network acts as an exact bulk-to-boundary isometry.

### HaPPY and hyperinvariant codes

Before giving an explicit solution to the HTN code conditions, we first explore the consequences of such conditions for bulk reconstruction. As noted above, tensors \\({A}^{{\\prime} }\\) that fulfill the isometric constraints of Fig. [4](https://www.nature.com/articles/s41467-023-42743-z#Fig4) d for a specific _B_ tensor can also be perfect. In that case, given a { _p_, _q_} tiling with odd _q_, bulk reconstruction would proceed as in the HaPPY code, where the union _a_ ∪ _a_ _c_ of the greedy wedges of _A_ and _A_ _c_ fills the entire bulk. However, we specifically wish to construct HTN codes with non-perfect tensors, whose super-operators have non-trivial spectra. In that case, we find that the bulk region that can be reconstructed for all states in the code space is strictly smaller than the HaPPY wedge. As we further find that the size of the reconstructable region is generally dependent on the bulk state, we will refer to it as the _reconstruction wedge_ in analogy to work on state-dependent bulk reconstruction in continuum AdS/CFT[32](https://www.nature.com/articles/s41467-023-42743-z#ref-CR32 "Hayden, P. & Penington, G. Learning the alpha-bits of black holes. JHEP 12, 007 (2019)."), [33](https://www.nature.com/articles/s41467-023-42743-z#ref-CR33 "Akers, C., Leichenauer, S. & Levine, A. Large breakdowns of entanglement wedge reconstruction. Phys. Rev. D 100, 126006 (2019)."). That the HTN reconstruction wedge can be significantly smaller than the HaPPY wedge is a direct consequence of utilizing non-perfect tensors. Specifically, the HTN isometry conditions in Fig. [4](https://www.nature.com/articles/s41467-023-42743-z#Fig4) d and their generalizations to other { _p_, _q_} tilings induce a greedy algorithm that is unable to produce connected bulk wedges from disconnected boundary regions. This is because these conditions, unlike in the HaPPY code, act as isometries only on neighboring legs. This property is similar to that of block-perfect tensors (which represent planar maximally-entangled (PME) states[34](https://www.nature.com/articles/s41467-023-42743-z#ref-CR34 "Doroudiani M. & Karimipour, V. Planar maximally entangled states. Phys. Rev. A                    https://doi.org/10.1103/physreva.102.012427                                     (2020).")) that have been previously considered in the context of holography[35](https://www.nature.com/articles/s41467-023-42743-z#ref-CR35 "Harris, R. J., McMahon, N. A., Brennen, G. K. & Stace, T. M. Calderbank-Shor-Steane holographic quantum error-correcting codes. Phys. Rev. A 98, 052301 (2018)."). A particular feature of HTN codes that follows from non-perfectness is that (guaranteed) complementary recovery is broken even between a connected boundary region _A_ and its complement _A_ _c_. An example of this is shown in Fig. [1](https://www.nature.com/articles/s41467-023-42743-z#Fig1) b: Even though _A_ and _A_ _c_ fill the entire boundary, their respective reconstruction wedges _a_ and _a_ _c_ exclude a strip of bulk sites that stretches all the way between the endpoints ∂ _A_. While in HaPPY codes such residual bulk regions can take up _O_(1) bulk sites, for HTN codes their number scales with the radial cutoff and is divergent for the infinite tiling. That this property is a consequence of non-perfect tensors can be seen in the example of a single tensor, as shown in Fig. [5](https://www.nature.com/articles/s41467-023-42743-z#Fig5) a, b: While perfect tensors allow logical reconstruction on either _A_ or _A_ _c_ (whichever is larger), for the HTN case with a merely 1-isometric vertex tensor, some bipartitions rule out exact reconstruction both on _A_ and _A_ _c_. For the entire tiling, this property then ensures a strip-shaped residual region around the minimal cut _γ_ _A_ in the tiling, as tensors that are half connected to _a_ and _a_ _c_ cannot be reached from either side by the greedy algorithm. This behavior was previously observed in the original HTN model without bulk legs[36](https://www.nature.com/articles/s41467-023-42743-z#ref-CR36 "Ling, Y., Liu, Y., Xian, Z.-Y. & Xiao, Y. Quantum error correction and entanglement spectrum in tensor networks. Phys. Rev. D 99, 026008 (2019).").

**Fig. 5: Bulk reconstruction in HTN codes.**

https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-023-42743-z/MediaObjects/41467_2023_42743_Fig5_HTML.png

[Full size image](https://www.nature.com/articles/s41467-023-42743-z/figures/5)

**a** For perfect tensors, any index bipartition into regions _A_ and _A_ _c_ leads to a reconstruction of the logical index (red dot) on either _A_ or _A_ _c_. **b** For the non-perfect tensors used in the HTN code, bipartitions exist for which neither _A_ nor _A_ _c_ are sufficient for reconstruction. **c** For a patch of the {5, 4} ququart HTN code with \\({A}^{{\\prime} }\\) and _B_ tensors given by (9) and ( [12](https://www.nature.com/articles/s41467-023-42743-z#Equ15)), we can show state-dependent reconstruction explicitly: For the given boundary regions _A_ and _A_ _c_, the central bulk ququart cannot be state-independently reconstructed on either. But given local projections of the neighboring bulk ququart on eigenstates of the logical ququart Paulis \\(\\bar{X}\\) and \\(\\bar{Z}\\), it can be fully reconstructed on either _A_ or _A_ _c_. While the RT surface _γ_ _A_ bounding the reconstructible region changes, its length ∣ _γ_ _A_∣ remains constant.

The breakdown of exact complementary recovery changes the form of the entanglement entropy _S_ _A_ of a boundary region _A_. In the HaPPY code, complementary recovery is realized via an isometry \\({V}\_{a}:{{{{{{{{\\mathcal{H}}}}}}}}}\_{a}\\otimes {{{{{{{{\\mathcal{H}}}}}}}}}\_{{\\gamma }\_{A}}\\to {{{{{{{{\\mathcal{H}}}}}}}}}\_{A}\\) from the logical qudits in the entanglement wedge _a_ and the physical qudits on the legs cut by the RT surface _γ_ _A_ to the boundary region _A_. This isometry can be constructed by simply contracting the tensors in _a_. Evaluating the von Neumann entropy _S_\[ _ρ_ _A_\] of the reduced density matrix \\({\\rho }\_{A}={{{{{{{{\\rm{tr}}}}}}}}}\_{{A}^{c}}\\rho\\) then yields the sum of two terms: The entropy of the reduced logical bulk state \\({\\tilde{\\rho }}\_{a}={{{{{{{{\\rm{tr}}}}}}}}}\_{{a}^{c}}\\tilde{\\rho }\\) and the entanglement along _γ_ _A_, which is composed of maximally entangled pairs due to the perfect tensor condition. This leads to the expression

$${S}\_{A}=\| {\\gamma }\_{A}\| \\log \\chi+{S}\_{a},$$

(5)

where ∣ _γ_ _A_∣ is the number of edges of the minimal cut _γ_ _A_, _χ_ the bond dimension, and \\({S}\_{a}=S\[{\\tilde{\\rho }}\_{a}\]\\) the bulk entropy. This expression clearly resembles the continuum AdS/CFT formula ( [1](https://www.nature.com/articles/s41467-023-42743-z#Equ1)) without _O_( _G_) corrections, i.e., in the semi-classical limit.

For HTN codes, exact complementary recovery is broken and ( [5](https://www.nature.com/articles/s41467-023-42743-z#Equ5)) no longer holds. Instead, _S_ _A_ now depends non-trivially on three contributions: The bulk entropy of the reconstruction wedge _a_ _r_, the non-maximal entanglement along the bulk cut \\({\\gamma }\_{A}^{{\\prime} }\\) (with \\(\\partial {a}\_{r}=A\\cup {\\gamma }\_{A}^{{\\prime} }\\)), and the entanglement mediated between \\({\\gamma }\_{A}^{{\\prime} }\\) and \\({\\gamma }\_{{A}^{c}}^{{\\prime} }\\) through the bulk residual region _r_, all of which are state-dependent. However, for a bulk state with negligible entanglement between _r_ and \\({r}^{c}={a}\_{r}\\cup {a}\_{r}^{c}\\) we expect an approximate form

$${S}\_{A}\\simeq {S}\_{{\\gamma }\_{A}^{{\\prime} }}\[{V}\_{r}^{{{{\\dagger}}} }{\\tilde{\\rho }}\_{r}{V}\_{r}\]+{S}\_{{a}\_{r}}.$$

(6)

Here the first term is the entanglement mediated from \\({\\gamma }\_{A}^{{\\prime} }\\) to \\({\\gamma }\_{{A}^{c}}^{{\\prime} }\\) through the residual region _r_, which is state-dependent on \\({\\tilde{\\rho }}\_{r}={{{{{{{{\\rm{tr}}}}}}}}}\_{a}{{{{{{{{\\rm{tr}}}}}}}}}\_{{a}^{c}}\\tilde{\\rho }\\), with _V_ _r_ being the isometry from logical qudits in _r_ to \\({\\gamma }\_{A}^{{\\prime} }\\cup {\\gamma }\_{{A}^{c}}^{{\\prime} }\\). As this term scales with the length of the minimal surface _γ_ _A_ and is bounded by \\(\| {\\gamma }\_{A}\| \\log \\chi\\), we identify it as the state-dependent area term in AdS/CFT under quantum corrections[7](https://www.nature.com/articles/s41467-023-42743-z#ref-CR7 "Faulkner, T., Lewkowycz, A. & Maldacena, J. Quantum corrections to holographic entanglement entropy. JHEP 11, 074 (2013)."), [10](https://www.nature.com/articles/s41467-023-42743-z#ref-CR10 "Engelhardt, N. & Wall, A. C. Quantum extremal surfaces: holographic entanglement entropy beyond the classical regime. JHEP 01, 073 (2015)."), with an example of such state dependence given below.

Without complementary recovery, non-trivial RG transformations become possible. As we show in Fig. [3](https://www.nature.com/articles/s41467-023-42743-z#Fig3) b, a local operator \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau }\\) on level _τ_ of the HTN tiling is coarse-grained into a local operator \\({{{{{{{\\mathcal{S}}}}}}}}({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau })={{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau+1}\\) on level _τ_ + 1, where \\({{{{{{{\\mathcal{S}}}}}}}}\\) is the scaling superoperator formed from one radial layer of the tiling and its conjugate. Unlike HaPPY codes, \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau+1}\\) is generally not the identity, and one can find lattice primary operators \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\alpha }\\) for which

$${{{{{{{\\mathcal{S}}}}}}}}({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\alpha })={s}^{{{{\\Delta }}}\_{\\alpha }}{{{{{{{{\\mathcal{O}}}}}}}}}\_{\\alpha },$$

(7)

where _s_ is the scaling factor of the tiling and Δ_α_ the scaling dimension of \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\alpha }\\)[22](https://www.nature.com/articles/s41467-023-42743-z#ref-CR22 "Evenbly, G. Hyperinvariant tensor networks and holography. Phys. Rev. Lett. 119, 141602 (2017)."). The property of finding non-trivial lattice primary operators is directly related to the code properties: Applying the scaling superoperator is equivalent to pushing an operator \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau }\\) through a radial layer of tensors, i.e., replacing it with another operator \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau+1}\\) that acts on different physical sites while acting identically on the codespace of the logical qudits in that layer. For any state vector \\(\\left\|\\bar{\\psi }\\right\\rangle\\) in the codespace, we thus require

$${{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau }\\left\|\\bar{\\psi }\\right\\rangle={{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau+1}\\left\|\\bar{\\psi }\\right\\rangle \\leftrightarrow \\langle \\bar{\\psi }\| {{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau+1}^{-1}{{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau }\| \\bar{\\psi }\\rangle=1.$$

(8)

For a HaPPY code built from perfect tensors, the only operators \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau }\\) and \\({{{{{{{{\\mathcal{O}}}}}}}}}\_{\\tau+1}\\) (each with support on a different single site) that fulfill this condition are the identity, as all two-site errors are correctable. This forces all two-point functions between non-trivial single-site operators to vanish. For HTN codes, where the vertex tensors are 1-isometric along planar legs, only single-site errors are correctable, and hence two-point functions are generally nonzero and non-trivial primaries exist.

The behavior of _n_-point correlation functions in HTN codes is closely related to the correctability of _n_-point errors for _n_ > 2, as well. Consider the single-site erasures for the {5, 4} HTN code shown in Fig. [6](https://www.nature.com/articles/s41467-023-42743-z#Fig6): Erasure of two single boundary sites prevents guaranteed reconstruction of a strip of logical sites on a geodesic between the two erasures, similar to the bipartition case of Fig. [1](https://www.nature.com/articles/s41467-023-42743-z#Fig1) b. This implies that two-point correlation functions are heavily distance-dependent and that long-range correlators can probe logical information deep in the bulk. For the three erasures in Fig. [6](https://www.nature.com/articles/s41467-023-42743-z#Fig6) b, the residual bulk region becomes even wider, consisting of the bulk volume enclosed by the discrete geodesics \\({\\gamma }\_{{A}\_{k}}\\) of the three disconnected boundary regions _A_ _k_. This drastically changes the code properties of HTN codes when compared to HaPPY codes: In HaPPY codes, bulk qudits remain resilient even against high-weight boundary errors as long as those are sufficiently sparse, a property know as _uberholography_ [37](https://www.nature.com/articles/s41467-023-42743-z#ref-CR37 "Pastawski, F. & Preskill, J. Code properties from holographic geometries. Physical Review X 7, 021022 (2017)."). On the contrary, HTN codes offer no such protection of logical information deep in the bulk against sparse errors with small support on the boundary. This comes with the caveat of state dependence: Boundary reconstruction beyond the reconstruction wedge may be possible for a semi-classical subspace of the logical Hilbert space whose protection against boundary errors matches that of the HaPPY code.

**Fig. 6: Effect of site erasures on bulk reconstruction.**

https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-023-42743-z/MediaObjects/41467_2023_42743_Fig6_HTML.png

[Full size image](https://www.nature.com/articles/s41467-023-42743-z/figures/6)

**a** In an HTN code, erasure of two boundary sites (black crosses) bisects the remaining boundary into two disjoint parts _A_ 1 and _A_ 2, with the reconstruction wedge of _A_ 1 ∪ _A_ 2 (shaded blue) being disjoint as well, separated by a strip-like region. **b** For three single-site erasures, the reconstruction wedge of _A_ 1 ∪ _A_ 2 ∪ _A_ 3 leaves out a larger region in the center of the bulk. Thus even small boundary operations can have an effect on information deep in the bulk for part of the codespace.

Earlier work on state dependence in tensor network codes considered modifications of the HaPPY code by inclusion of a black hole, i.e., a random tensor of high bond dimension (close to a perfect tensor at high bond dimension) whose logical leg, representing the black hole microstates, exhibits a variable dimension: For certain boundary regions this setting allows for approximate reconstruction of bulk operators when the reconstruction involves pushing them through the black hole tensor, which is possible if the mixed state of the black hole has small entropy (i.e., small logical dimension in the random tensor model). It has been argued that such state-dependent, approximate recovery is an essential feature of continuum AdS/CFT[32](https://www.nature.com/articles/s41467-023-42743-z#ref-CR32 "Hayden, P. & Penington, G. Learning the alpha-bits of black holes. JHEP 12, 007 (2019)."). Beyond mixed bulk states involving black holes, one further expects to find state dependence for pure bulk states even close to the vacuum state, i.e., with only little backreaction to the AdS geometry[33](https://www.nature.com/articles/s41467-023-42743-z#ref-CR33 "Akers, C., Leichenauer, S. & Levine, A. Large breakdowns of entanglement wedge reconstruction. Phys. Rev. D 100, 126006 (2019)."). State dependence and approximate recovery are thus unavoidable features of holographic codes, even if one restricts the bulk code space to low-energy perturbations around the vacuum. For a boundary bipartition into regions _A_ and _A_ _c_, this state dependence should appear as a splitting of the logical code space into _α_- _blocks_ each corresponding to a different Ryu–Takayanagi surface _γ_ _A_ separating the entanglement wedges _a_ and _a_ _c_, representing different bulk geometries in superposition[14](https://www.nature.com/articles/s41467-023-42743-z#ref-CR14 "Akers, C. & Rath, P. Holographic Renyi entropy from quantum error correction. JHEP 05, 052 (2019)."), [15](https://www.nature.com/articles/s41467-023-42743-z#ref-CR15 "Dong, X., Harlow, D. & Marolf, D. Flat entanglement spectra in fixed-area states of quantum gravity. JHEP 10, 240 (2019)."). It is this aspect in which HTN codes generalize HaPPY codes, as they exhibit some state dependence for pure states. An example is shown in Fig. [5](https://www.nature.com/articles/s41467-023-42743-z#Fig5) c for the {5, 4} tiling, using the explicit code that we introduce in the next section: Here, The central logical qudit can be reconstructed from a boundary region _A_ comprising half of the boundary only for a subspace of the full logical bulk in which two logical qudits next to the center are projected onto eigenstates of the logical Pauli operators \\(\\bar{X}\\) or \\(\\bar{Z}\\) (here denoted as \\(\\left\|\\bar{X}\\right\\rangle\\) and \\(\\left\|\\bar{Z}\\right\\rangle\\), with an index for the specific eigenstate suppressed). For a different projection, the central logical qudit can be reconstructed on _A_ _c_ instead. We can thus interpret the logical subspaces given by these projections as different _α_-blocks. While this allows for state-dependent bulk reconstruction with different _γ_ _A_ in each subspace, we see in our example that the length ∣ _γ_ _A_∣, i.e., the number of physical indices that _γ_ _A_ cuts across, remains constant. This is no coincidence: As shown recently, all stabilizer codes have trivial area operators[38](https://www.nature.com/articles/s41467-023-42743-z#ref-CR38 "Cao, C. Stabilizer codes have trivial area operators. Preprint at arXiv                    https://doi.org/10.48550/arXiv.2306.14996                                     (2023)."). This means that the area term of the entanglement entropy, when written in an algebraic decomposition along _α_-blocks, is a block-independent scalar depending only on the choice of _A_. Hence, HTN codes exhibit the maximum amount of state dependence that stabilizer codes allow.

Given such state dependence, we can identify tensor network analogs of fixed-area states with flat entanglement spectra for any boundary bipartition into connected regions _A_ and _A_ _c_, thus acting like states in a HaPPY code. In our explicit HTN code example, this state corresponds to a projection onto local \\(\\left\|\\bar{X}\\right\\rangle\\) eigenstates (for _d_-dimensional qudits, these are _d_ states spanning the logical Hilbert space). These _d_ _N_ states \\({\\left\|\\bar{X}\\right\\rangle }^{\\otimes N}\\) thus form the fixed-area basis of the bulk Hilbert space. Each fixed-area state has trivial superoperator spectra as in Fig. [3](https://www.nature.com/articles/s41467-023-42743-z#Fig3) b, behaving like classical AdS vacua without any bulk modes. Conversely, superpositions of these states can be interpreted as excited bulk modes with back-reaction, leading to non-trivial boundary correlation functions. Therefore, to describe the boundary ground state of a critical theory we start with a bulk product state \\({\\left\|\\right.{\\bar{\\psi }}\_{{{{{{\\rm{gnd}}}}}}}\\rangle }^{\\otimes N}\\) that is not a fixed-area state, and extract the operator spectrum of the boundary theory from the resulting superoperators. Low-energy excitations within this theory are then given by bulk states that locally deviate from \\({\|{\\bar{\\psi }}\_{{{{{\\rm{gnd}}}}}}\\rangle }\\).

### An explicit code construction

We now give an example of an HTN code that fulfills the HTN constraints for the {5, 4} geometry as visualized in Fig. [4](https://www.nature.com/articles/s41467-023-42743-z#Fig4) d. This example uses qudits with local dimension _d_ = 4 (ququarts), where each encoding tensor \\({A}^{{\\prime} }\\) represents an error-detection code spanned by the logical states[26](https://www.nature.com/articles/s41467-023-42743-z#ref-CR26 "Raissi, Z. Modifying method of constructing quantum codes from highly entangled states. IEEE Access 8, 222439–222448 (2020).")

$$\\left\|\\bar{0}\\right\\rangle=\\frac{1}{2}\\left(\\left\|0000\\right\\rangle+\\left\|1111\\right\\rangle+\\left\|2222\\right\\rangle+\\left\|3333\\right\\rangle \\right),$$

(9a)

$$\\left\|\\bar{1}\\right\\rangle=\\frac{1}{2}\\left(\\left\|0123\\right\\rangle+\\left\|1230\\right\\rangle+\\left\|2301\\right\\rangle+\\left\|3012\\right\\rangle \\right),$$

(9b)

$$\\left\|\\bar{2}\\right\\rangle=\\frac{1}{2}\\left(\\left\|0202\\right\\rangle+\\left\|1313\\right\\rangle+\\left\|2020\\right\\rangle+\\left\|3131\\right\\rangle \\right),$$

(9c)

$$\\left\|\\bar{3}\\right\\rangle=\\frac{1}{2}\\left(\\left\|0321\\right\\rangle+\\left\|1032\\right\\rangle+\\left\|2103\\right\\rangle+\\left\|3210\\right\\rangle \\right),$$

(9d)

which is stabilized by the ququart Pauli generators _X_ _X_ _X_ _X_, _I_ _Z_ _Z_ 2 _Z_, and _Z_ _Z_ 2 _Z_ _I_. The logical operators of this code can be represented as \\(\\bar{X}=IX{X}^{2}{X}^{3}\\) and \\(\\bar{Z}=II{Z}^{3}Z\\) or any cyclic permutations of the tensor products, as the code is completely invariant under a rotation of the physical qubits. Equivalently, the tensor \\({A}^{{\\prime} }\\) is invariant under cyclic permutation of the planar indices,

$${A}\_{j,{i}\_{1},{i}\_{2},{i}\_{3},{i}\_{4}}^{{\\prime} }={A}\_{j,{i}\_{4},{i}\_{1},{i}\_{2},{i}\_{3}}^{{\\prime} },$$

(10)

where _j_ is the logical index and _i_ _k_ are the planar ones. The projection onto any logical state results in a 4-ququart state that is 1-isometric on the planar legs, which implies that no logical information can be extracted from any single physical ququart. Thus (9) defines a ⟦4, 1, 2⟧4 code that can detect a single-site error. We now check the isometry condition for \\({w}^{{\\prime} }\\) and \\({u}^{{\\prime} }\\) in Fig. [4](https://www.nature.com/articles/s41467-023-42743-z#Fig4)(d). The \\({w}^{{\\prime} }\\) condition only depends on the \\({A}^{{\\prime} }\\) tensor as long as _B_ is unitary, and given ( [10](https://www.nature.com/articles/s41467-023-42743-z#Equ13)), it suffices to evaluate the condition from the logical index _j_ and the first planar index _i_ 1 to the remaining planar ones. Expressing \\({{w}^{{\\prime} }}^{{{{\\dagger}}} }{w}^{{\\prime} }\\) in index notation, we find

$$\\mathop{\\sum }\\limits\_{{i}\_{2},{i}\_{3},{i}\_{4}=0}^{3}{T}\_{j,{i}\_{1},{i}\_{2},{i}\_{3},{i}\_{4}}{T}\_{{j}^{{\\prime} },{i}\_{1}^{{\\prime} },{i}\_{2},{i}\_{3},{i}\_{4}}^{\\star }\\propto {\\delta }\_{j,{j}^{{\\prime} }}{\\delta }\_{{i}\_{1},{i}\_{1}^{{\\prime} }}.$$

(11)

In order to also fulfill the isometry (or rather unitary) condition for \\({u}^{{\\prime} }\\), we choose the _B_ tensor to be the ququart Hadamard matrix,

$$B=\\frac{1}{2}{H}\_{4}=\\frac{1}{2}\\left(\\begin{array}{cccc}1&1&1&1\\\ 1&-1&1&-1\\\ 1&1&1&-1\\\ 1&-1&-1&1\\end{array}\\right),$$

(12)

which is both symmetric and unitary. We find that this choice of \\({A}^{{\\prime} }\\) and _B_ leads to \\({u}^{{\\prime} }\\) being unitary, but omit the full expression for the sake of clarity. Another valid solution for _B_ that uses the same \\({A}^{{\\prime} }\\) is given by the 4-dimensional quantum Fourier transform. As the tensor \\({A}^{{\\prime} }\\) is generally non-perfect along its planar indices, it follows that the respective superoperators exhibit non-trivial spectra. However, any projection onto an eigenstate of \\(\\bar{X}\\), such as

$$\\left\|{\\bar{X}}\_{1}\\right\\rangle=\\frac{1}{2}\\left(\\left\|\\bar{0}\\right\\rangle+\\left\|\\bar{1}\\right\\rangle+\\left\|\\bar{2}\\right\\rangle+\\left\|\\bar{3}\\right\\rangle \\right),$$

(13)

will produce a tensor that is block-perfect on its remaining four planar legs. This is one possible choice for the state \\(\\left\|\\bar{X}\\right\\rangle\\) discussed above in the context of state-dependent bulk reconstruction, where \\(\\left\|\\bar{Z}\\right\\rangle\\) can be chosen as any of the four basis states \\(\\left\|{\\bar{Z}}\_{k}\\right\\rangle \\equiv \\left\|\\bar{k}\\right\\rangle\\). The proof of the specific reconstruction shown in Fig. [5](https://www.nature.com/articles/s41467-023-42743-z#Fig5) c for this code is described in the Methods section [4](https://www.nature.com/articles/s41467-023-42743-z#Sec8) using operator pushing techniques.

The 4-qudit HTN code also produces non-trivial superoperator spectra for certain bulk (product) states. The 1-site superoperator \\({{{{{{{\\mathcal{S}}}}}}}}\\) shown in Fig. [3b](https://www.nature.com/articles/s41467-023-42743-z#Fig3), for example, has four Hermitian eigenoperators for the bulk state \\(\\alpha \\left\|\\bar{0}\\right\\rangle+\\sqrt{1-{\\alpha }^{2}}\\left\|\\bar{2}\\right\\rangle\\) with 0 ≤ _α_ ≤ 1, two of which have positive eigenvalue: The identity \\({\\mathbb{1}}\\) with eigenvalue 1, and the operator

$${{{{{{{\\mathcal{O}}}}}}}}=\\frac{1}{\\sqrt{1+{\\lambda }^{2}}}\\left(\\begin{array}{cccc}1&0&\\lambda &0\\\ 0&1&0&\\lambda \\\ \\lambda &0&-1&0\\\ 0&\\lambda &0&-1\\end{array}\\right)$$

(14)

with eigenvalue \\(\\lambda=\\sqrt{2\\alpha \\sqrt{1-{\\alpha }^{2}}}\\). As 0 ≤ _λ_ ≤ 1, the norm of this operator generally decays under coarse-graining \\({{{{{{{\\mathcal{O}}}}}}}}\\to {{{{{{{\\mathcal{S}}}}}}}}({{{{{{{\\mathcal{O}}}}}}}})\\), as expected from an RG transformation of a primary operator. Using the scale factor \\(s=2+\\sqrt{3}\\) for the {5, 4} tiling, we can thus associate the operator \\({{{{{{{\\mathcal{O}}}}}}}}\\) with a scaling dimension \\({{\\Delta }}=-{\\log }\_{s}\\lambda\\)[22](https://www.nature.com/articles/s41467-023-42743-z#ref-CR22 "Evenbly, G. Hyperinvariant tensor networks and holography. Phys. Rev. Lett. 119, 141602 (2017).").

A similar analysis can be performed for any choice of tensors that form an HTN code. A systematic search for critical lattice models that can be described by HTN codes, as well as the precise relationship between code properties and critical spectra, will be an interesting subject for future work. We already note here that such models will break boundary translation invariance as a consequence of the tiling symmetries. Most instances will therefore not have a well-defined CFT continuum limit but will fall into the more general class of _quasiperiodic CFTs_ [39](https://www.com/articles/s41467-023-42743-z#ref-CR39 "Jahn, A., Zimborás, Z. & Eisert, J. Tensor network models of AdS/qCFT. Quantum 6, 643 (2022).").

## Discussion

A number of previous models have been proposed as approximate holographic codes in the past, the earliest being random tensor networks at finite bond dimension[19](https://www.nature.com/articles/s41467-023-42743-z#ref-CR19 "Hayden, P. et al. Holographic duality from random tensor networks. JHEP 11, 009 (2016)."), [40](https://www.nature.com/articles/s41467-023-42743-z#ref-CR40 "Qi, X.-L. & Yang, Z. Space-time random tensor networks and holographic duality. Preprint at arXiv                    https://doi.org/10.48550/arXiv.1801.05289                                     (2018)."). The resulting codes are approximate in their encoding isometry, making it difficult to study their properties analytically. Subsequent tensor network codes with exact encoding isometries but approximate complementary recovery have also been proposed, using tensors that alternate between perfect and non-perfect ones[20](https://www.nature.com/articles/s41467-023-42743-z#ref-CR20 "Cao, C. & Lackey, B. Approximate Bacon-Shor code and holography. JHEP 05, 127 (2021)."), [21](https://www.nature.com/articles/s41467-023-42743-z#ref-CR21 "Cao, C., Pollack, J. & Wang, Y. Hyperinvariant multiscale entanglement renormalization ansatz: approximate holographic error correction codes with power-law correlations. Phys. Rev. D 105, 026018 (2022)."). Such models have less symmetry than HaPPY codes and break complementary recovery only for some bipartitions, whereas it is softly broken in HTN codes for any bipartition. Similarly, two-point correlation functions in HTN codes are generically nonzero, whereas they must vanish e.g., in the hybrid holographic code of Ref. [20](https://www.nature.com/articles/s41467-023-42743-z#ref-CR20 "Cao, C. & Lackey, B. Approximate Bacon-Shor code and holography. JHEP 05, 127 (2021).") for small operators acting on one of the perfect tensors. HTN codes thus have more symmetrical features and retain the structure of stabilizer codes while only introducing small violations of locality during bulk reconstruction that are consistent with the expectation of small quantum gravity effects. Following this logic, a holographic code representing AdS/CFT with strong quantum gravity contributions can be built by requiring more intricate isometric constraints, representing the breakdown of a semi-classical geometry on which the bulk information is located.

As HTN codes break exact complementary recovery, it will be interesting to explore whether restrictions on HaPPY codes regarding fault-tolerant logical operations using boundary transversal gates[41](https://www.nature.com/articles/s41467-023-42743-z#ref-CR41 "Cree, S., Dolev, K., Calvera, V. & Williamson, D. J. Faulttolerant logical gates in holographic stabilizer codes are severely restricted. PRX Quantum 2, 030337 (2021).") still apply in this new setting. A holographic code relating local boundary to local bulk time evolution, potentially realizable by an HTN code, would also have a number of useful features regarding non-local quantum computation[42](https://www.nature.com/articles/s41467-023-42743-z#ref-CR42 "May, A. Complexity and entanglement in non-local computation and holography. Quantum 6, 864 (2022)."), [43](https://www.nature.com/articles/s41467-023-42743-z#ref-CR43 "Dolev K. & Cree S. Holography as a resource for non-local quantum computation. Preprint at arXiv                    https://doi.org/10.48550/arXiv.2210.13500                                     (2022)."). Another interesting question is whether HTN codes also support non-stabilizer subsystem codes such as those constructed in Ref. [20](https://www.com/articles/s41467-023-42743-z#ref-CR20 "Cao, C. & Lackey, B. Approximate Bacon-Shor code and holography. JHEP 05, 127 (2021)."), and how this affects state dependence.

While HTN and HaPPY codes share the same tensor network geometry, we saw that their resilience against erasure errors is somewhat different, with HTN codes suppressing the effect of boundary operations on logical qudits deep in the bulk approximately through an RG process, rather than guaranteeing uberholographic recoverability. In ongoing work, we show that more general classes of HTN codes built from 2-isometric states beyond the {5, 4} tiling can be constructed[44](https://www.nature.com/articles/s41467-023-42743-z#ref-CR44 "Steinberg, M., Harris, R., Jahn, A., Elkouss, D. & Feld S. Quantum error correction with hyperinvariant codes. (in preparation, 2023)."). There we also analyze their quantum error-correction properties and discuss applications for practical quantum computing.

## Methods

The hyperinvariant code construction is purely analytical and can be checked by explicit calculation on paper or using computer algebra systems. We now verify our central claim of state-dependent recovery of logical bulk qudits (shown in Fig. [5](https://www.nature.com/articles/s41467-023-42743-z#Fig5) c) using a graphical proof based on operator pushing for the ququart HTN code defined by the ⟦4, 1, 2⟧4 code (9) and the _B_ tensor ( [12](https://www.nature.com/articles/s41467-023-42743-z#Equ15)). For this purpose, we show that the logical algebra generated by the logical ququart Pauli operators \\(\\bar{X}\\) and \\(\\bar{Z}\\) can be reconstructed state-dependently on either the region _A_ or its complement _A_ _c_, given projections of the neighboring two ququarts on eigenstates of \\(\\bar{X}\\) or \\(\\bar{Z}\\). Specifically, one starts with a representation of \\(\\bar{X}\\) or \\(\\bar{Z}\\) in terms of physical Pauli operators on the internal (contracted) indices of the tensor, and then applies operator pushing: By applying stabilizers, we can remove Pauli operators on one physical index at the cost of adding new ones elsewhere, all while leaving the tensor invariant. For \\({A}^{{\\prime} }\\) tensors, whose logical leg is projected onto an eigenstate \\(\\left\|\\bar{X}\\right\\rangle\\) or \\(\\left\|\\bar{Z}\\right\\rangle\\) of a ququart Pauli operator, applying the respective logical operator (or any power thereof) is also an invariant operation. We can also move Pauli operators past _B_ tensors by using the identities _X_ _H_ 4 = _H_ 4 _Z_ T and _Z_ _H_ = _H_ _X_ T, which exchange ququart _X_ and _Z_ (note the transpose, as the direction in which the operator acts is reversed).

The part of the tensor network in Fig. [5](https://www.nature.com/articles/s41467-023-42743-z#Fig5) c that is relevant for our proof consists of a block of three \\({A}^{{\\prime} }\\) tensors and the two _B_ tensors between them that would form the bulk residual region given no restriction on the bulk Hilbert space. The actual operator pushing steps of this proof are shown in Fig. [7](https://www.nature.com/articles/s41467-023-42743-z#Fig7) for the setup in which the left \\({A}^{{\\prime} }\\) tensor is projected onto \\(\\left\|\\bar{X}\\right\\rangle\\), and the right one onto \\(\\left\|\\bar{Z}\\right\\rangle\\). We find that both \\(\\bar{X}\\) and \\(\\bar{Z}\\) acting on the central ququart can be represented as Pauli operators acting purely on the subregion _A_. By symmetry, swapping the two projections results in the opposite scenario, where representation only on _A_ _c_ is possible, corresponding to the two settings in Fig. [5](https://www.nature.com/articles/s41467-023-42743-z#Fig5) c. We also confirmed these results numerically, finding in the first scenario that the mutual information between the logical index and _A_ is \\(\\log 4\\), while it vanishes with regards to _A_ _c_, and vice versa in the second scenario. This proves genuinely state-dependent reconstruction: For different logical subspaces, the central logical ququart lies in different entanglement wedges.

**Fig. 7: Graphical proof of the state-dependent reconstruction of the central ququart in Fig. 5c.**

https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-023-42743-z/MediaObjects/41467_2023_42743_Fig7_HTML.png

[Full size image](https://www.nature.com/articles/s41467-023-42743-z/figures/7)

**a** The ququart Pauli operator _X_ is represented by the logical operator \\(\\bar{X}=X{X}^{2}{X}^{3}I\\). After pushing the Pauli operators acting on internal indices through the _B_ tensors (green dots), which exchanges _X_ ↔ _Z_, we apply the stabilizer \\({(Z{Z}^{2}ZI)}^{3}={Z}^{3}{Z}^{2}{Z}^{3}I\\) on the left side and \\({\\bar{Z}}^{3}={({Z}^{3}ZII)}^{3}=Z{Z}^{3}II\\) on the right, resulting in a physical operator represented only on boundary region _A_. **b** Similarly, we can push \\(\\bar{Z}={Z}^{3}ZII\\) to the left, apply \\({\\bar{X}}^{3}={(X{X}^{2}{X}^{3}I)}^{3}={X}^{3}{X}^{2}XI\\), and again arrive at a physical operator on _A_.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="how-space-and-time-could-be-a-quantum-error-correcting-code-.md">
<details>
<summary>How Space and Time Could Be a Quantum Error-Correcting Code</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103>

# How Space and Time Could Be a Quantum Error-Correcting Code

_By_ [Natalie Wolchover](https://www.quantamagazine.org/authors/natalie/)

_January 3, 2019_

The same codes needed to thwart errors in quantum computers may also give the fabric of space-time its intrinsic robustness.

https://www.quantamagazine.org/wp-content/uploads/2019/01/QuantumError_2880x1220-Lede.jpg

In toy “holographic” universes (if not the real universe), the fabric of space and time emerges from a network of quantum particles. Physicists have discovered that this works according to a principle called quantum error correction.

[DVDP](https://davidope.com/) for Quanta Magazine

## Introduction

In 1994, a mathematician at AT&T Research named [Peter Shor](http://www-math.mit.edu/~shor/) brought instant fame to “quantum computers” when he [discovered](https://arxiv.org/pdf/quant-ph/9508027.pdf) that these hypothetical devices could quickly factor large numbers — and thus break much of modern cryptography. But a fundamental problem stood in the way of actually building quantum computers: the innate frailty of their physical components.

Unlike binary bits of information in ordinary computers, “qubits” consist of quantum particles that have some probability of being in each of two states, designated \|0⟩ and \|1⟩, at the same time. When qubits interact, their possible states become interdependent, each one’s chances of \|0⟩ and \|1⟩ hinging on those of the other. The contingent possibilities proliferate as the qubits become more and more “entangled” with each operation. Sustaining and manipulating this exponentially growing number of simultaneous possibilities are what makes quantum computers so theoretically powerful.

But qubits are maddeningly error-prone. The feeblest magnetic field or stray microwave pulse causes them to undergo “bit-flips” that switch their chances of being \|0 **⟩** and \|1⟩ relative to the other qubits, or “phase-flips” that invert the mathematical relationship between their two states. For quantum computers to work, scientists must find schemes for protecting information even when individual qubits get corrupted. What’s more, these schemes must detect and correct errors without directly measuring the qubits, since measurements collapse qubits’ coexisting possibilities into definite realities: plain old 0s or 1s that can’t sustain quantum computations.

In 1995, Shor followed his factoring algorithm with another stunner: [proof](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.52.R2493) that “quantum error-correcting codes” exist. The computer scientists [Dorit Aharonov](http://www.cs.huji.ac.il/~doria/) and [Michael Ben-Or](https://www.cs.huji.ac.il/~benor/) (and other researchers working independently) [proved](https://arxiv.org/abs/quant-ph/9611025) a year later that these codes could theoretically push error rates close to zero. “This was the central discovery in the ’90s that convinced people that scalable quantum computing should be possible at all,” said [Scott Aaronson](https://www.scottaaronson.com/), a leading quantum computer scientist at the University of Texas — “that it is merely a staggering problem of engineering.”

https://www.quantamagazine.org/wp-content/uploads/2019/01/PeterShor_1500.jpg

https://www.quantamagazine.org/wp-content/uploads/2019/01/Dorit-Aharonov_1500.jpg

https://www.quantamagazine.org/wp-content/uploads/2019/01/MichaelBenOr_1500.jpg

From top: Peter Shor, Dorit Aharonov and Michael Ben-Or laid the foundation for quantum error correction and fault-tolerant quantum computing more than 20 years ago.

From left: Peter Shor, Dorit Aharonov and Michael Ben-Or laid the foundation for quantum error correction and fault-tolerant quantum computing more than 20 years ago.

Courtesy of Peter Shor; Courtesy of Dorit Aharonov; The Hebrew University of Jerusalem (Ben-Or)

Now, even as small quantum computers are materializing in labs around the world, useful ones that will outclass ordinary computers [remain years or decades away](https://www.quantamagazine.org/the-era-of-quantum-computing-is-here-outlook-cloudy-20180124/). Far more efficient quantum error-correcting codes are needed to cope with the daunting error rates of real qubits. The effort to design better codes is “one of the major thrusts of the field,” Aaronson said, along with improving the hardware.

But in the dogged pursuit of these codes over the past quarter-century, a funny thing happened in 2014, when physicists found evidence of a deep connection between quantum error correction and the nature of space, time and gravity. In Albert Einstein’s general theory of relativity, gravity is defined as the fabric of space and time — or “space-time” — bending around massive objects. (A ball tossed into the air travels along a straight line through space-time, which itself bends back toward Earth.) But powerful as Einstein’s theory is, physicists believe gravity must have a deeper, quantum origin from which the semblance of a space-time fabric somehow emerges.

That year — 2014 — three young quantum gravity researchers came to an astonishing realization. They were working in physicists’ theoretical playground of choice: a [toy universe called “anti-de Sitter space”](https://www.quantamagazine.org/albert-einstein-holograms-and-quantum-gravity-20181114/) that works like a hologram. The bendy fabric of space-time in the interior of the universe is a projection that emerges from entangled quantum particles living on its outer boundary. [Ahmed Almheiri](https://www.ias.edu/scholars/ahmed-almheiri), [Xi Dong](http://www.physics.ucsb.edu/people/xi-dong) and [Daniel Harlow](http://web.mit.edu/physics/people/faculty/harlow_daniel.html) did calculations suggesting that this holographic “emergence” of space-time works just like a quantum error-correcting code. They [conjectured](https://arxiv.org/abs/1411.7041) in the _Journal of High Energy Physics_ that space-time itself is a code — in anti-de Sitter (AdS) universes, at least. The paper has triggered a wave of activity in the quantum gravity community, and new quantum error-correcting codes have been discovered that capture more properties of space-time.

[John Preskill](http://www.theory.caltech.edu/people/preskill/), a theoretical physicist at the California Institute of Technology, says quantum error correction explains how space-time achieves its “intrinsic robustness,” despite being [woven out of fragile quantum stuff](https://www.quantamagazine.org/tensor-networks-and-entanglement-20150428/). “We’re not walking on eggshells to make sure we don’t make the geometry fall apart,” Preskill said. “I think this connection with quantum error correction is the deepest explanation we have for why that’s the case.”

The language of quantum error correction is also starting to enable researchers to probe the mysteries of black holes: spherical regions in which space-time curves so steeply inward toward the center that not even light can escape. “Everything traces back to black holes,” said Almheiri, who is now at the Institute for Advanced Study in Princeton, New Jersey. These paradox-ridden places are where gravity reaches its zenith and Einstein’s general relativity theory fails. “There are some indications that if you understand which code space-time implements,” he said, “it might help us in understanding the black hole interior.”

As a bonus, researchers hope holographic space-time might also point the way to scalable quantum computing, fulfilling the long-ago vision of Shor and others. “Space-time is a lot smarter than us,” Almheiri said. “The kind of quantum error-correcting code which is implemented in these constructions is a very efficient code.”

https://www.quantamagazine.org/wp-content/uploads/2019/01/Ahmed-Almheiri_1500.jpg

https://www.quantamagazine.org/wp-content/uploads/2019/01/Xi_Dong_1500.jpg

https://www.quantamagazine.org/wp-content/uploads/2019/01/Daniel-Harlow_1500.jpg

From top: Ahmed Almheiri, Xi Dong and Daniel Harlow originated a powerful new idea that the fabric of space-time is a quantum error-correcting code.

From left: Ahmed Almheiri, Xi Dong and Daniel Harlow originated a powerful new idea that the fabric of space-time is a quantum error-correcting code.

Maryam Meshar (Almheiri); Courtesy of Xi Dong; Justin Knight (Harlow)

So, how do quantum error-correcting codes work? The trick to protecting information in jittery qubits is to store it not in individual qubits, but in patterns of entanglement among many.

As a simple example, consider the three-qubit code: It uses three “physical” qubits to protect a single “logical” qubit of information against bit-flips. (The code isn’t really useful for quantum error correction because it can’t protect against phase-flips, but it’s nonetheless instructive.) The \|0⟩ state of the logical qubit corresponds to all three physical qubits being in their \|0⟩ states, and the \|1⟩ state corresponds to all three being \|1⟩’s. The system is in a “superposition” of these states, designated \|000⟩ + \|111⟩. But say one of the qubits bit-flips. How do we detect and correct the error without directly measuring any of the qubits?

The qubits can be fed through two gates in a quantum circuit. One gate checks the “parity” of the first and second physical qubit — whether they’re the same or different — and the other gate checks the parity of the first and third. When there’s no error (meaning the qubits are in the state \|000⟩ + \|111⟩), the parity-measuring gates determine that both the first and second and the first and third qubits are always the same. However, if the first qubit accidentally bit-flips, producing the state \|100⟩ + \|011⟩, the gates detect a difference in both of the pairs. For a bit-flip of the second qubit, yielding \|010⟩ + \|101⟩, the parity-measuring gates detect that the first and second qubits are different and first and third are the same, and if the third qubit flips, the gates indicate: same, different. These unique outcomes reveal which corrective surgery, if any, needs to be performed — an operation that flips back the first, second or third physical qubit without collapsing the logical qubit. “Quantum error correction, to me, it’s like magic,” Almheiri said.

https://www.quantamagazine.org/wp-content/uploads/2019/01/Qubit-Errors_560.jpg

Lucy Reading-Ikkanda/Quanta Magazine

The best error-correcting codes can typically recover all of the encoded information from slightly more than half of your physical qubits, even if the rest are corrupted. This fact is what hinted to Almheiri, Dong and Harlow in 2014 that quantum error correction might be related to the way anti-de Sitter space-time arises from quantum entanglement.

It’s important to note that AdS space is different from the space-time geometry of our “de Sitter” universe. Our universe is infused with positive vacuum energy that causes it to expand without bound, while anti-de Sitter space has negative vacuum energy, which gives it the hyperbolic geometry of one of M.C. Escher’s _Circle Limit_ designs. Escher’s tessellated creatures become smaller and smaller moving outward from the circle’s center, eventually vanishing at the perimeter; similarly, the spatial dimension radiating away from the center of AdS space gradually shrinks and eventually disappears, establishing the universe’s outer boundary. AdS space gained popularity among quantum gravity theorists in 1997 after the renowned physicist [Juan Maldacena discovered](https://www.quantamagazine.org/juan-maldacena-pondering-quantum-gravity-by-the-pond-20170623/) that the bendy space-time fabric in its interior is “holographically dual” to a quantum theory of particles living on the lower-dimensional, gravity-free boundary.

https://www.quantamagazine.org/wp-content/uploads/2019/01/Escher_1000.jpg

The hyperbolic geometry in M.C. Escher’s 1959 woodcut, Circle Limit III, is also a feature of anti-de Sitter space.

https://en.wikipedia.org/wiki/Circle_Limit_III#/media/File:Escher_Circle_Limit_III.jpg

In exploring how the duality works, as hundreds of physicists have in the past two decades, Almheiri and colleagues noticed that any point in the interior of AdS space could be constructed from slightly more than half of the boundary — just as in an optimal quantum error-correcting code.

In their paper conjecturing that holographic space-time and quantum error correction are one and the same, they described how even a simple code could be understood as a 2D hologram. It consists of three “qutrits” — particles that exist in any of three states — sitting at equidistant points around a circle. The entangled trio of qutrits encode one logical qutrit, corresponding to a single space-time point in the circle’s center. The code protects the point against the erasure of any of the three qutrits.

Of course, one point is not much of a universe. In 2015, Harlow, Preskill, Fernando Pastawski and Beni Yoshida [found another holographic code](https://arxiv.org/abs/1503.06237), nicknamed the HaPPY code, that captures more properties of AdS space. The code tiles space in five-sided building blocks — “little Tinkertoys,” said [Patrick Hayden](https://web.stanford.edu/~phayden/) of Stanford University, a leader in the research area. Each Tinkertoy represents a single space-time point. “These tiles would be playing the role of the fish in an Escher tiling,” Hayden said.

In the HaPPY code and other holographic error-correcting schemes that have been discovered, everything inside a region of the interior space-time called the “entanglement wedge” can be reconstructed from qubits on an adjacent region of the boundary. Overlapping regions on the boundary will have overlapping entanglement wedges, Hayden said, just as a logical qubit in a quantum computer is reproducible from many different subsets of physical qubits. “That’s where the error-correcting property comes in.”

“Quantum error correction gives us a more general way of thinking about geometry in this code language,” said Preskill, the Caltech physicist. The same language, he said, “ought to be applicable, in my opinion, to more general situations” — in particular, to a de Sitter universe like ours. But de Sitter space, lacking a spatial boundary, has so far proven much harder to understand as a hologram.

For now, researchers like Almheiri, Harlow and Hayden are sticking with AdS space, which shares many key properties with a de Sitter world but is simpler to study. Both space-time geometries abide by Einstein’s theory; they simply curve in different directions. Perhaps most importantly, both kinds of universes contain black holes. “The most fundamental property of gravity is that there are black holes,” said Harlow, who is now an assistant professor of physics at the Massachusetts Institute of Technology. “That’s what makes gravity different from all the other forces. That’s why quantum gravity is hard.”

The language of quantum error correction has provided a new way of describing black holes. The presence of a black hole is defined by **_“_** the breakdown of correctability,” Hayden said: “When there are so many errors that you can no longer keep track of what’s going on in the bulk \[space-time\] anymore, you get a black hole. It’s like a sink for your ignorance.”

Ignorance invariably abounds when it comes to black hole interiors. Stephen Hawking’s 1974 epiphany that black holes radiate heat, and thus eventually evaporate away, triggered the infamous [“black hole information paradox,”](https://www.quantamagazine.org/stephen-hawkings-black-hole-paradox-keeps-physicists-puzzled-20180314/) which asks what happens to all the information that black holes swallow. Physicists need a quantum theory of gravity to understand how things that fall in black holes also get out. The issue may relate to cosmology and the birth of the universe, since expansion out of a Big Bang singularity is much like gravitational collapse into a black hole in reverse.

https://www.quantamagazine.org/wp-content/uploads/2018/11/Cover_02.jpg

By clicking to watch this video, you agree to our [privacy policy.](https://www.quantamagazine.org/privacy-policy)

**Video**: How does gravity work in the quantum regime? A holographic duality from string theory offers a powerful tool for unraveling the mystery.

Directed by Emily Driscoll and animated by Jonathan Trueblood for Quanta Magazine

AdS space simplifies the information question. Since the boundary of an AdS universe is holographically dual to everything in it — black holes and all — the information that falls into a black hole is guaranteed never to be lost; it’s always holographically encoded on the universe’s boundary. Calculations suggest that to reconstruct information about a black hole’s interior from qubits on the boundary, you need access to entangled qubits throughout roughly three-quarters of the boundary. “Slightly more than half is not sufficient anymore,” Almheiri said. He added that the need for three-quarters seems to say something important about quantum gravity, but why that fraction comes up “is still an open question.”

In Almheiri’s first claim to fame in 2012, the tall, thin Emirati physicist and three collaborators [deepened](https://arxiv.org/abs/1207.3123) the information paradox. Their reasoning suggested that information might be prevented from ever falling into a black hole in the first place, by a “firewall” at the black hole’s event horizon.

Like most physicists, Almheiri doesn’t really believe black hole firewalls exist, but finding the way around them has proved difficult. Now, he thinks quantum error correction is what stops firewalls from forming, by protecting information even as it crosses black hole horizons. In [his latest, solo work](https://arxiv.org/abs/1810.02055), which appeared in October, he reported that quantum error correction is “essential for maintaining the smoothness of space-time at the horizon” of a two-mouthed black hole, called a wormhole. He speculates that quantum error correction, as well as preventing firewalls, is also how qubits escape a black hole after falling in, through strands of entanglement between the inside and outside that are themselves like miniature wormholes. This would resolve Hawking’s paradox.

This year, the Department of Defense is [funding research into holographic space-time](https://grantbulletin.research.uiowa.edu/fy-2019-defense-multidisciplinary-research-program-university-research-initiative-muri-white-paper), at least partly in case advances there might spin off more efficient error-correcting codes for quantum computers.

On the physics side, it remains to be seen whether de Sitter universes like ours can be described holographically, in terms of qubits and codes. “The whole connection is known for a world that is manifestly not our world,” Aaronson said. In [a paper](https://link.springer.com/article/10.1007%2FJHEP07%282018%29050) last summer, Dong, who is now at the University of California, Santa Barbara, and his co-authors [Eva Silverstein](https://sitp.stanford.edu/people/eva-silverstein) and Gonzalo Torroba took a step in the de Sitter direction, with an attempt at a primitive holographic description. Researchers are still studying that particular proposal, but Preskill thinks the language of quantum error correction will ultimately carry over to actual space-time.

“It’s really entanglement which is holding the space together,” he said. “If you want to weave space-time together out of little pieces, you have to entangle them in the right way. And the right way is to build a quantum error-correcting code.”

_This article was reprinted on_ [_Wired.com_](https://www.wired.com/story/space-and-time-could-be-a-quantum-error-correcting-code/) _._

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="pastawski-yoshida-harlow-preskill-happy-code-error-correctio.md">
<details>
<summary>Pastawski-Yoshida-Harlow-Preskill (HaPPY) code[[1]](https://errorcorrectionzoo.org/c/happy#citation-1)</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://errorcorrectionzoo.org/c/happy>

# Pastawski-Yoshida-Harlow-Preskill (HaPPY) code[[1]](https://errorcorrectionzoo.org/c/happy#citation-1)

Alternative Names: Perfect holographic code.

## Description

Holographic code constructed from six-leg five-qubit [perfect tensors](https://errorcorrectionzoo.org/c/ame#defterm-Absolutely_20Xmaximally_20Xentangled_20X_28XAME_29X_20Xstate) placed on hyperbolic pentagon and hexagon tilings. The code serves as a minimal model for several aspects of the AdS/CFT holographic duality [\[2\]](https://errorcorrectionzoo.org/c/happy#citation-2) and potentially a dS/CFT duality [\[3\]](https://errorcorrectionzoo.org/c/happy#citation-3).

It has been generalized to higher dimensions [\[4\]](https://errorcorrectionzoo.org/c/happy#citation-4) and to include gauge-like degrees of freedom on the links of the tensor network \[ [5](https://errorcorrectionzoo.org/c/happy#citation-5), [6](https://errorcorrectionzoo.org/c/happy#citation-6)\]. In the lifted version, the bulk symmetry of the HaPPY code can be interpreted as arising from restricting a bulk gauge-like theory to a fixed-flux sector [\[6\]](https://errorcorrectionzoo.org/c/happy#citation-6). All boundary global symmetries must be dual to bulk gauge symmetries, and vice versa [\[7\]](https://errorcorrectionzoo.org/c/happy#citation-7).

The construction below is described for qubits, but the underlying five-leg perfect tensor also has modular-qudit and oscillator extensions, and a rotor version can be stacked into an approximately error-correcting \\(U(1)\\)-covariant holographic code [\[8\]](https://errorcorrectionzoo.org/c/happy#citation-8). Encoding is accomplished using a tensor network of five-qubit encoding isometries, which are six-legged [perfect tensors](https://errorcorrectionzoo.org/c/ame#defterm-Absolutely_20Xmaximally_20Xentangled_20X_28XAME_29X_20Xstate) (with five legs corresponding to the physical qubits and one for the encoded logical qubit).

To construct the encoding, one first uniformly tiles the hyperbolic AdS/CFT disc using pentagons and hexagons. Then, one places a 6-legged five-qubit encoding tensor at each hexagon and pentagon, contracting legs between neighboring shapes and leaving one leg uncontracted at each pentagon. This construction forms an encoding isometry from the uncontracted legs in the bulk to the uncontracted legs at the boundary.

The single-qubit HaPPY code has a central pentagon encoding one bulk operator and hexagons tiling all other layers. The pentagon-hexagon HaPPY code has alternating layers of pentagons and hexagons in the tiling. The pentagon HaPPY code (a.k.a. the hyperbolic pentagon code, or HyPeC) consists of a purely pentagonal tiling.

## Protection

Protects against erasure errors and Pauli errors on the boundary qubits.

## Rate

The pentagon HaPPY code has an asymptotic rate \\(\\frac{1}{\\sqrt{5}} \\approx 0.447\\). The pentagon-hexagon HaPPY code has a rate of \\(0.299\\) if the last layer is a pentagon layer and a rate of \\(0.088\\) if the last layer is a hexagon layer.

## Encoding

Heisenberg-picture encoding is done through tensor pushing. Each bulk operator (logical) is pushed to an operator supported on a portion of the boundary region (physical). Pushing all the bulk operators through results in reconstruction of the boundary.ZX calculus based encoder for the pentagon HaPPY code [\[9\]](https://errorcorrectionzoo.org/c/happy#citation-9).

## Transversal and Permutation-Based Gates

Any transversal gate of the five-qubit code is a transversal gate of the HaPPY code since the HaPPY code is constructed from five-qubit encoding tensors, which are covariant under such gates.For locality-preserving physical gates on the boundary, the set of transversally implementable logical operations in the bulk is strictly contained in the [Clifford group](https://errorcorrectionzoo.org/c/clifford_group#defterm-Clifford_20Xgroup)[\[10\]](https://errorcorrectionzoo.org/c/happy#citation-10).

## Decoding

Hierarchical recovery model [\[1\]](https://errorcorrectionzoo.org/c/happy#citation-1).The greedy algorithm reconstructs bulk operators by iteratively absorbing tensors for which at least half of the legs are already included; the resulting greedy geodesic gives an explicit boundary reconstruction region [\[1\]](https://errorcorrectionzoo.org/c/happy#citation-1).

## Code Capacity Threshold

\\(26\\%\\) for boundary erasure errors on the pentagon-hexagon HaPPY code under the greedy decoder [\[1\]](https://errorcorrectionzoo.org/c/happy#citation-1).Lower bound of \\(1/12 \\approx 8.3\\%\\) for boundary erasure errors on the single-qubit HaPPY code under hierarchical recovery [\[1\]](https://errorcorrectionzoo.org/c/happy#citation-1). Numerical evidence indicates the threshold may be closer to \\(50\\%\\).There is no threshold for the pentagon HaPPY code as a constant number of errors (four) can make bulk recovery impossible [\[1\]](https://errorcorrectionzoo.org/c/happy#citation-1).\\(16.3\\%\\) for boundary Pauli errors on the single-qubit HaPPY code with 3 layers using integer optimization decoder [\[11\]](https://errorcorrectionzoo.org/c/happy#citation-11).\\(50\\%\\) against biased Pauli noise for single-qubit HaPPY code under tensor-network decoder [\[12\]](https://errorcorrectionzoo.org/c/happy#citation-12).

## Threshold

A single-qubit HaPPY code has a [measurement threshold](https://errorcorrectionzoo.org/c/qubits_into_qubits#defterm-Measurement_20Xthreshold) of one [\[13\]](https://errorcorrectionzoo.org/c/happy#citation-13).

## Notes

Reference [\[3\]](https://errorcorrectionzoo.org/c/happy#citation-3) discusses the HaPPY code for an AdS\_3 space and its relation to a dS\_2 braneworld with a conformal boundary.

## Cousins

- [Majorana stabilizer code](https://errorcorrectionzoo.org/c/majorana_stab)— The pentagon HaPPY code Hamiltonian can be expressed in terms of mutually commuting weight-two (two-body) Majorana operators [\[14\]](https://errorcorrectionzoo.org/c/happy#citation-14).
- [Perfect-tensor code](https://errorcorrectionzoo.org/c/ame)— The encoding of a HaPPY code is a holographic tensor network consisting of pentagon and hexagon [perfect tensors](https://errorcorrectionzoo.org/c/ame#defterm-Absolutely_20Xmaximally_20Xentangled_20X_28XAME_29X_20Xstate).

## Primary Hierarchy

[Quantum Domain](https://errorcorrectionzoo.org/domain/quantum_domain)

[Qubit Kingdom](https://errorcorrectionzoo.org/kingdom/qubits_into_qubits)

[Qubit code](https://errorcorrectionzoo.org/c/qubits_into_qubits) [QECC](https://errorcorrectionzoo.org/c/qecc "Qubit code ← Modular-qudit code ← Block quantum code ← Quantum error-correcting code (QECC)") [Quantum](https://errorcorrectionzoo.org/c/quantum_into_quantum "Qubit code ← OA qubit code ← Operator-algebra QECC (OAQECC) ← Quantum code")

[Union stabilizer (USt) code](https://errorcorrectionzoo.org/c/non_stabilizer) [QECC](https://errorcorrectionzoo.org/c/qecc "Union stabilizer (USt) code ← Modular-qudit USt code ← Modular-qudit code ← Block quantum code ← Quantum error-correcting code (QECC)") [Quantum](https://errorcorrectionzoo.org/c/quantum_into_quantum "Union stabilizer (USt) code ← Modular-qudit USt code ← Modular-qudit code ← Block quantum code ← Quantum error-correcting code (QECC) ← Operator-algebra QECC (OAQECC) ← Quantum code")

[Qubit stabilizer code](https://errorcorrectionzoo.org/c/qubit_stabilizer) [Stabilizer](https://errorcorrectionzoo.org/c/stabilizer "Qubit stabilizer code ← Modular-qudit stabilizer code ← Stabilizer code") [Hamiltonian-based](https://errorcorrectionzoo.org/c/hamiltonian "Qubit stabilizer code ← Modular-qudit stabilizer code ← Stabilizer code ← Commuting-projector Hamiltonian code ← Hamiltonian-based code") [Qubit](https://errorcorrectionzoo.org/c/qubits_into_qubits "Qubit stabilizer code ← XP stabilizer code ← Clifford-hierarchy stabilizer code ← Qubit code") [QECC](https://errorcorrectionzoo.org/c/qecc "Qubit stabilizer code ← Modular-qudit stabilizer code ← Tensor-network code ← Block quantum code ← Quantum error-correcting code (QECC)") [Quantum](https://errorcorrectionzoo.org/c/quantum_into_quantum "Qubit stabilizer code ← Operator-algebra (OA) qubit stabilizer code ← OA qubit code ← Operator-algebra QECC (OAQECC) ← Quantum code")

Parents

[Qubit stabilizer code](https://errorcorrectionzoo.org/c/qubit_stabilizer)

The HaPPY code is a stabilizer code because it is defined by a contracted network of stabilizer tensors; see [\[1; Thm. 6\]](https://errorcorrectionzoo.org/c/happy#citation-1).

[Holographic tensor-network code](https://errorcorrectionzoo.org/c/holographic_tensor) [HQECC](https://errorcorrectionzoo.org/c/holographic "Holographic tensor-network code ← Holographic code") [QECC](https://errorcorrectionzoo.org/c/qecc "Holographic tensor-network code ← Holographic code ← Quantum error-correcting code (QECC)") [Quantum](https://errorcorrectionzoo.org/c/quantum_into_quantum "Holographic tensor-network code ← Holographic code ← Quantum error-correcting code (QECC) ← Operator-algebra QECC (OAQECC) ← Quantum code")

The encoding of a HaPPY code is a holographic tensor network consisting of pentagon and hexagon [perfect tensors](https://errorcorrectionzoo.org/c/ame#defterm-Absolutely_20Xmaximally_20Xentangled_20X_28XAME_29X_20Xstate).

Pastawski-Yoshida-Harlow-Preskill (HaPPY) code

Children

[\\(\[\[5,1,3\]\]\\) Five-qubit perfect code](https://errorcorrectionzoo.org/c/stab_5_1_3)

The five-qubit code is the smallest (i.e., radius-one) single-qubit HaPPY code. The five-qubit encoding isometry tiles various holographic codes because its corresponding encoding isometry tensor is a [perfect tensor](https://errorcorrectionzoo.org/c/ame#defterm-Absolutely_20Xmaximally_20Xentangled_20X_28XAME_29X_20Xstate)[\[1\]](https://errorcorrectionzoo.org/c/happy#citation-1).

## References

\[1\]F. Pastawski, B. Yoshida, D. Harlow, and J. Preskill, “Holographic quantum error-correcting codes: toy models for the bulk/boundary correspondence”, Journal of High Energy Physics 2015, (2015) [arXiv:1503.06237](https://arxiv.org/abs/1503.06237) [DOI](https://doi.org/10.1007%2Fjhep06(2015)149)\[2\]T. J. Osborne and D. E. Stiegemann, “Dynamics for holographic codes”, Journal of High Energy Physics 2020, (2020) [arXiv:1706.08823](https://arxiv.org/abs/1706.08823) [DOI](https://doi.org/10.1007%2Fjhep04(2020)154)\[3\]J. Cotler and A. Strominger, “The Universe as a Quantum Encoder”, (2022) [arXiv:2201.11658](https://arxiv.org/abs/2201.11658)\[4\]M. Taylor and C. Woodward, “Holography, cellulations and error correcting codes”, (2023) [arXiv:2112.12468](https://arxiv.org/abs/2112.12468)\[5\]W. Donnelly, D. Marolf, B. Michel, and J. Wien, “Living on the edge: a toy model for holographic reconstruction of algebras with centers”, Journal of High Energy Physics 2017, (2017) [arXiv:1611.05841](https://arxiv.org/abs/1611.05841) [DOI](https://doi.org/10.1007%2Fjhep04(2017)093)\[6\]K. Dolev, V. Calvera, S. S. Cree, and D. J. Williamson, “Gauging the bulk: generalized gauging maps and holographic codes”, Journal of High Energy Physics 2022, (2022) [arXiv:2108.11402](https://arxiv.org/abs/2108.11402) [DOI](https://doi.org/10.1007%2Fjhep05(2022)158)\[7\]D. Harlow and H. Ooguri, “Symmetries in quantum field theory and quantum gravity”, (2019) [arXiv:1810.05338](https://arxiv.org/abs/1810.05338)\[8\]P. Faist, S. Nezami, V. V. Albert, G. Salton, F. Pastawski, P. Hayden, and J. Preskill, “Continuous Symmetries and Approximate Quantum Error Correction”, Physical Review X 10, (2020) [arXiv:1902.07714](https://arxiv.org/abs/1902.07714) [DOI](https://doi.org/10.1103%2Fphysrevx.10.041018)\[9\]Z. Wu, S. Cheng, and B. Zeng, “A ZX-Calculus Approach for the Construction of Graph Codes”, (2024) [arXiv:2304.08363](https://arxiv.org/abs/2304.08363)\[10\]S. Cree, K. Dolev, V. Calvera, and D. J. Williamson, “Fault-Tolerant Logical Gates in Holographic Stabilizer Codes Are Severely Restricted”, PRX Quantum 2, (2021) [arXiv:2103.13404](https://arxiv.org/abs/2103.13404) [DOI](https://doi.org/10.1103%2Fprxquantum.2.030337)\[11\]R. J. Harris, E. Coupe, N. A. McMahon, G. K. Brennen, and T. M. Stace, “Decoding holographic codes with an integer optimization decoder”, Physical Review A 102, (2020) [arXiv:2008.10206](https://arxiv.org/abs/2008.10206) [DOI](https://doi.org/10.1103%2Fphysreva.102.062417)\[12\]J. Fan, M. Steinberg, A. Jahn, C. Cao, and S. Feld, “Biased-Noise Thresholds of Zero-Rate Holographic Codes with Tensor-Network Decoding”, (2025) [arXiv:2408.06232](https://arxiv.org/abs/2408.06232)\[13\]S. Antonini, G. Bentsen, C. Cao, J. Harper, S.-K. Jian, and B. Swingle, “Holographic measurement and bulk teleportation”, Journal of High Energy Physics 2022, (2022) [arXiv:2209.12903](https://arxiv.org/abs/2209.12903) [DOI](https://doi.org/10.1007%2Fjhep12(2022)124)\[14\]A. Jahn, M. Gluza, F. Pastawski, and J. Eisert, “Majorana dimers and holographic quantum error-correcting codes”, Physical Review Research 1, (2019) [arXiv:1905.03268](https://arxiv.org/abs/1905.03268) [DOI](https://doi.org/10.1103%2Fphysrevresearch.1.033079)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="Introduction and the Shor 9-qubit code.md">
<details>
<summary>Introduction and the Shor 9-qubit code</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://people.eecs.berkeley.edu/~jswright/quantumcodingtheory24/scribe%20notes/lecture01.pdf>

Quantum Coding Theory (UC Berkeley CS294, Spring 2024)

Lecture 1: Introduction and the Shor 9-qubit code January 24, 2024

Lecturer: John Wright Scribe: John Wright

# 1 Introduction

## 1.1 The problem of noise in quantum computing

In 1994, Peter Shor discovered his quantum algorithm for factoring. As we all know, it was met with immediate acclaim and generated a significant increase in the level of interest in quantum computing. What is less remembered is that it was also met with a significant degree of skepticism, based on the belief that although it was a nice mathematical theorem, it would never be useful in practice. Why? The answer is noise.

<span id="page-0-0"></span>An ideal quantum computation can be represented as a circuit, as in [Figure 1.](#page-0-0)

![](_page_0_Figure_8.jpeg)

Figure 1: A quantum circuit.

In this circuit, the wires represent qubits, and the squares represent quantum operations, or gates, which are applied to them. Although this ideal circuit may work perfectly in theory, in practice a number of things can go wrong. For example, the hardware might be imperfect, and occasionally a gate might fail and do something completely different than what it was supposed to do. Another possibility is that a stray particle from the environment might interact with one of the wires, producing an error on that qubit. All of these are examples of noise, and they all have the potential to ruin the computation, resulting in an output which is useless.

One possible way to address this is to design hardware which is so precise that even lengthy computations can be expected to experience no errors. Roughly, if the ideal quantum circuit consists of T quantum gates, then we might hope that our quantum computer experiences an error on each gate with probability at most p ≤ O(1/T). In practice, though, things are much worse. For example, in 1995, one year after Shor's algorithm, an experimental quantum computer achieved an error probability of 20% per gate [?] (which means it could

be expected to run for around 5 gates before introducing an error). Even now, 30 years later, the very best quantum computers still only achieve error rates in the range of roughly 0.5-1%, much worse than what we would need to carry out a typical quantum computation.

This raised the serious possibility that noise might preclude quantum computers from ever working, and researchers of this time took this possibility very seriously. For example, several papers considered physically-relevant models of noise and how they interacted with Shor's factoring algorithm, and they discovered that it does indeed render the computation useless [?, ?]. One of the most prominent voices stressing the importance of studying noise in quantum computers was Rolf Landauer. Among other things, he was well-known for suggesting that any paper on quantum computation should come with the following disclaimer [?]:

"This proposal, like all proposals for quantum computation, relies on speculative technology, does not in its current form take into account all possible sources of noise, unreliability and manufacturing error, and probably will not work."

## 1.2 Enter quantum error correcting codes

One year later, in 1995, Shor [?] discovered that one could use tools from error correction to protect quantum states from the effect of noise. The result was his 9-qubit code, which we will see later in this lecture. In the 9-qubit code, one encodes a single qubit, which might be error-prone, into a blob of 9 qubits, as in the picture below.

![](_page_1_Picture_5.jpeg)

This encoding has the property that if exactly one qubit in the blob undergoes an error, the error can be detected and corrected. This gave a proof-of-concept that quantum noise could be overcome with error correction, even if the 9-qubit code only protects one qubit. Also in 1995 (and published in 1996), Andrew Steane independently discovered a different error correcting code known as the 7-qubit Steane code, which we will see later in this semester.

One year later, Shor showed how to error-correct not just a single qubit, but an entire quantum computation. In [?], he gave a method to compile a general T-gate ideal quantum computation into a quantum circuit with poly(T) gates which is resilient to noise. In particular, the compiled circuit will successfully simulate the original, ideal circuit so long as the error rate p on each gate is at most O(1/polylog(T)). (Here, poly(T) refers to a function which is O(T k ) for some k; similarly, polylog(T) refers to a function which is O(log(T) k ) for some k.) Thus, the compiled circuit is not much larger than the original circuit, and it can tolerate much higher rates of noise than the rate of p = O(1/T) which would be required if there were no error correction. However, this scheme still requires the noise rate to decrease as the size of the computation grows, which is not a reasonable assumption in practice.

The final breakthrough came later in 1996/7, independently by Kitaev [?], Aharanov and Ben-Or [?], and Knill, Laflamme, and Zurek [?], who improved on Shor's result and proved what is now known as the fault-tolerance/threshold theorem. They showed how to take an ideal T-gate quantum computation and compile it into a new circuit of T · polylog(T) gates—a minimal bloweup—with can correct against even constant levels of noise. This demonstrated once and for all that quantum computers could indeed overcome the problem of noise, and showed that developing scalable quantum computers is merely an astronomically difficult engineering task rather than an impossible engineering task. The error rate p below which error correction kicks in is known as the threshold, and its value depends on both the compilation scheme and the error model. Early estimates of p were quite low (in the ballpark of p = 10<sup>−</sup><sup>6</sup> ; see [?] for a discussion), but more recent estimates of placed it in the range of 0.5-1%, tantalizingly close to the error rates that are currently achievable in practice.

## 1.3 Outline of the course

A large part of this course will be devoted to explaining these developments from the mid-1990's in order to prove the fault tolerance theorem. However, we will also cover more recent developments in quantum error correction. Very roughly, the course will be structured as follows.

- 1. Basics of quantum error correction. This will include defining quantum error correcting codes as well as giving examples of basic quantum error correcting codes, such as Shor's 9-qubit code and Steane's 7-qubit code.
- 2. "Good" quantum codes. The last few years have seen the surprising development of new quantum error correcting codes with extremely good parameters, which are known as "good" quantum LDPC codes. We will cover the development of these codes, starting from the toric code.
- 3. The fault tolerance and threshold theorem.
- 4. Applications of quantum error correction to other areas. The main application I have in mind is to the quantum PCP and NLTS conjectures.

Feel free to suggest other topics if you are interested in them! We have a diverse audience and I'd like to know what topics other people find interesting.

## 2 Going from classical to quantum codes

## 2.1 The 3-bit repetition code

To build up to our first quantum error correcting code, we will develop some intuition by studying the most basic of all classical error correcting codes, which is known as the repetition code. In the classical world, our data consists of bits b ∈ {0, 1}, and the noise we would like

to protect against is *bit flip noise*, which sends 0 to 1 and 1 to 0. To do so, we will encode our bit b by adding extra bits containing redundancy; these extra redundant bits will allow us to recover b even if one of the bits is corrupted.

**Definition 2.1** (Repetition code). The repetition code encodes a single bit  $b \in \{0, 1\}$  into three bits by duplicating the bit three times, as follows.

$$0 \longrightarrow 000$$
$$1 \longrightarrow 111$$

The two strings on the right are known as *codewords*. 000 is the codeword representing the bit 0 and is therefore referred to as "logical 0", and similarly, 111 is referred to as "logical 1". We will sometimes use the following two pieces of notation for these codewords:

$$000 = \overline{0} = 0_L,$$
  
$$111 = \overline{1} = 1_L,$$

though I will probably switch between these notations throughout the course as I have not yet decided whether I prefer  $\overline{0}$  or  $0_L$ .

Suppose that one of our codewords experiences a single bit flip, such as:

$$000 \xrightarrow{\text{noise}} 010.$$

Then we can correct this bit flip by looking at the majority of the three bits. Since only one of our bits has been flipped, this will give us the correct value for the three bits:

$$000 \xrightarrow{\text{noise}} 010 \xrightarrow{\text{majority}} 000.$$

On the other hand, this scheme will fail if the codeword experiences two bit flip errors:

$$000 \xrightarrow{\text{noise}}^{\text{lots of}} 011 \xrightarrow{\text{majority}} 111 \neq 000.$$

Hence, the 3-bit repetition code allows us to correct one bit flip error, although it fails to correct two or more bit flip errors.

One final thing: note that 3 bit flips are required to move from  $0_L$  to  $1_L$ . (In other words,  $0_L$  and  $1_L$  have Hamming distance 3.) This means that the repetition code has distance 3. The distance of a code is an important parameter that we will discuss more in future lectures. But for now, it is useful to know that the bigger the distance of a code is, the more errors that one can correct at any given time.

## 2.2 What makes quantum error correction hard

We would like to use our intuition from the 3-bit repetition code to design a quantum error correcting code. Intuitively, this code should encode a qubit  $|\psi\rangle = a \cdot |0\rangle + b \cdot |1\rangle$  so that it is resilient to quantum noise. However, there are three generally agreed upon issues that make designing quantum codes much more difficult than designing classical codes.

1. (No cloning theorem) Analogously to the repetition code, we might want to encode |ψ⟩ by duplicating the state multiple times in order to add redundancy. However, the no cloning theorem states that the map

$$|\psi\rangle \rightarrow |\psi\rangle |\psi\rangle |\psi\rangle$$

is not possible. So how can we add redundancy?

2. (Quantum noise) Classically, there is only one source of noise: bit flips. Quantumly, however, there are many more types of noise. For example, there are phase flips, which act as follows:

$$a \cdot |0\rangle + b \cdot |1\rangle \xrightarrow{\text{noise}} a \cdot |0\rangle - b \cdot |1\rangle$$
.

These have no classical analogue. Indeed, there are an uncountably infinite number of different types of quantum noise, since there is a continuum of different quantum operations. Designing one code that protects against all of them seems impossible!

3. (Collapse of the wavefunction) If an error does occur on our encoded state, the natural thing to do is to perform a measurement on the state in order to diagnose the error. However, quantum measurements can collapse the state, which might destroy the information we were trying to protect.

These three issues mean that even the mere existence of quantum error correcting codes is unclear, and they mean that designing quantum codes can be a very subtle task. Note that according to Dave Bacon [?], these three issues did not present too much difficulty to the earlier pioneers of quantum error correction, but they are still obstacles that any quantum error correcting code must overcome.

## 2.3 A simplified noise model

For the rest of this lecture, we will sidestep issue (2) above by considering a simplified noise model in which only bit flip and phase flip noise can occur.

Definition 2.2 (Bit flip noise). Consider the unitary matrix

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$

This acts on the standard basis as follows:

$$X \cdot |0\rangle = |1\rangle$$
, and  $X \cdot |1\rangle = |0\rangle$ .

As a result, this is known as a bit flip error. In the Hadamard basis, it acts as follows:

$$\begin{aligned} |+\rangle &= |0\rangle + |1\rangle \mapsto |1\rangle + |0\rangle = |+\rangle \,, \\ |-\rangle &= |0\rangle - |1\rangle \mapsto |1\rangle - |0\rangle = - |-\rangle \,. \end{aligned}$$

Definition 2.3 (Phase flip noise). Consider the unitary matrix

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

This acts on the standard basis as follows:

$$Z \cdot |0\rangle = |0\rangle$$
, and  $Z \cdot |1\rangle = -|1\rangle$ .

As a result, this is known as a phase flip or a sign flip error. In the Hadamard basis, it acts as follows:

$$\begin{aligned} |+\rangle &= |0\rangle + |1\rangle \mapsto |0\rangle - |1\rangle = |-\rangle \,, \\ |-\rangle &= |0\rangle - |1\rangle \mapsto |0\rangle + |1\rangle = |+\rangle \,. \end{aligned}$$

Note that phase flip noise acts exactly as bit flip noise, only in the Hadamard basis, as it exchanges the roles of |+⟩ and |−⟩. In fact, we have the following relationship between these two matrices.

$$Z = HXH$$
 and  $X = HZH$ .

Once we allow qubits to undergo bit flips and phase flips, we should also allow them to undergo both types of noise at the same time. This results in a third type of noise which, as far as I know, doesn't have a nice name like "bit flip" or "phase flip".

Definition 2.4 (Bit and phase flip noise). Consider the unitary matrix

$$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = i \cdot XZ.$$

This first applies a phase flip and then applies a bit flip (and then multiplies by a random factor of i for some reason). As a result, this acts on the standard basis as follows:

$$Y \cdot |0\rangle = i \cdot |1\rangle$$
, and  $Y \cdot |1\rangle = -i \cdot |0\rangle$ .

Why include the factor of i? As a matter of fact, it's not necessary at all. Indeed, in John Preskill's quantum error correction notes [?], he simply defines the Y matrix as

$$Y = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$

and omits the i. Daniel Gottesman, in his excellent lectures on quantum error correction [?], states that the definition with the i gives you extra headaches in some parts of quantum coding theory, but that the definition without the i gives you extra headaches in other parts of quantum coding theory. We'll presumably see this as we go along in the semester. Of course, one reason to include the factor of i is that the matrices X, Y, Z are the famous Pauli matrices, which recur throughout quantum computation.

Remark 2.5 (Completeness of Pauli noise). As it turns out, these Pauli errors are *complete* for quantum noise, in the sense that if you design a quantum code that can correct for Pauli errors, then your quantum code corrects for all other types of errors for free. We will see this statement justified in an upcoming lecture. For now, we will just assert it is true. But this makes it a lot easier to design quantum codes using classical intuition, as it means that quantum error correction is exactly the same as classical error correction, except you have to worry about one more basis (i.e. the Hadamard basis).

## 3 The 3-qubit bit flip (/repetition) code

In order to build up to Shor's 9-qubit code, we will first construct a 3-qubit code which corrects against a single bit flip error but not against any phase flip errors. In designing this code, we will address issues (1) and (3) from above, by avoiding the no-cloning theorem and the collapse of the wavefunction.

#### 3.1 Definition of the code

**Definition 3.1** (The 3-qubit bit flip code). To define the 3-qubit bit flip code, we will first define it on the standard basis, and then we will extend it to general states via linearity. Given a basis state  $|b\rangle$ , for  $b \in \{0,1\}$ , we encode it by duplicating the bit three times, as follows.

$$|0\rangle \longrightarrow |0\rangle \otimes |0\rangle \otimes |0\rangle$$

$$|1\rangle \longrightarrow |1\rangle \otimes |1\rangle \otimes |1\rangle$$

We will often drop the tensor products and write  $|000\rangle$  as shorthand for  $|0\rangle \otimes |0\rangle \otimes |0\rangle$ . The state  $|000\rangle$  is known as the "logical 0 state" and can be written as either  $|\overline{0}\rangle$  or  $|0\rangle_L$ ; similarly,  $|111\rangle$  is known as the "logical 1 state" and can be written as either  $|\overline{1}\rangle$  or  $|1\rangle_L$ . A general state is encoded as follows.

$$|\psi\rangle = a \cdot |0\rangle + b \cdot |1\rangle \longrightarrow a \cdot |000\rangle + b \cdot |111\rangle$$
.

The state on the right is the *logical qubit* and can be written as  $|\psi\rangle_L$  or  $|\overline{\psi}\rangle$ ; it is the representation of the original qubit in our error correcting code. On the other hand, the three qubits which are used to encode the state are known as *physical qubits*.

We note that this code circumvents the no cloning theorem by not actually cloning the qubit state  $|\psi\rangle$ . In other words,

$$a\cdot |000\rangle + b\cdot |111\rangle \neq (a\cdot |0\rangle + b\cdot |1\rangle) \otimes (a\cdot |0\rangle + b\cdot |1\rangle) \otimes (a\cdot |0\rangle + b\cdot |1\rangle).$$

What it *does* do is it uses entanglement to copy only the standard basis information across the three qubits, which is not disallowed by the no cloning theorem.

<span id="page-7-0"></span>The encoding map for the 3-qubit bit flip code can be carried out by the quantum circuit in [Figure 2.](#page-7-0)

![](_page_7_Figure_1.jpeg)

Figure 2: The encoding circuit for the 3-qubit code.

<span id="page-7-1"></span>The quantum gate which is used twice in that circuit is the CNOT gate, which acts in [Figure 3](#page-7-1) for all a, b ∈ {0, 1}.

$$|a\rangle \xrightarrow{\qquad} |a\rangle$$

$$|b\rangle \xrightarrow{\qquad} |a+b \pmod{2}\rangle$$

Figure 3: The CNOT gate.

## 3.2 Bit flip error

Now let us investigate how this code behaves under bit flip errors. Suppose that a bit flip has occurred on the second qubit. This gives us the state

$$I \otimes X \otimes I \cdot |\psi\rangle_L = a \cdot |010\rangle + b \cdot |101\rangle.$$

The state on the right-hand side is the corrupted state and we will write it as <sup>|</sup>ψe⟩<sup>L</sup> . To detect that an error has occurred, a natural thing to do would be to measure the three qubits in the standard basis. This would give us the string 010 with probability |a| <sup>2</sup> and the string 101 with probability |b| 2 . In either case, we can observe that the three bits are not the same, and so an error must have occurred. However, in doing so, we have collapsed the superposition, meaning that we cannot recover |ψ⟩. So although we have detected the error, we cannot correct it.

The issue is that we measured too much: not only did we learn that there was a bit flip, we also simulated a standard basis measurement on |ψ⟩. So we should instead try to measure whether there was a bit flip and only whether there was a bit flip. To do this, we will measure (i) the parity of the first and second qubits and (ii) the parity of the second and third qubits. These parities are 1 and 1, respectively, in both branches of the superposition, and so measuring them will not collapse the state. In other words, we perform the circuit given [Figure 4.](#page-8-0)

<span id="page-8-0"></span>![](_page_8_Picture_0.jpeg)

Figure 4: Circuit for bit flip detection.

This circuit acts on the state |ψ⟩<sup>L</sup> as follows.

$$\begin{split} |\psi\rangle_L \otimes |00\rangle \\ &= (a \cdot |010\rangle + b \cdot |101\rangle) \otimes |00\rangle \\ &= a \cdot |010\rangle \otimes |00\rangle + b \cdot |101\rangle \otimes |00\rangle \\ &\to a \cdot |010\rangle \otimes |11\rangle + b \cdot |101\rangle \otimes |11\rangle \\ &= a \cdot |010\rangle \otimes |00\rangle + b \cdot |101\rangle \otimes |11\rangle \\ &= |\psi\rangle_L \otimes |11\rangle \,. \end{split}$$

The circuit concludes by measuring the second register, which results in the measurement outcome 11. This measurement outcome is known as the syndrome, and it gives the information necessary to diagnose where an error has occurred. In this case, the syndrome specifies that the qubits 1 and 2 disagree, as well as qubits 2 and 3, which indicates that a bit flip error has been applied to the second qubit. In general, the four possible syndromes specify the following errors.

| Syndrome | Error                 |
|----------|-----------------------|
| 00       | no error              |
| 01       | bit flip on 3rd qubit |
| 10       | bit flip on 1st qubit |
| 11       | bit flip on 2nd qubit |

It will be convenient to associate the syndrome bits with the error message that they specify. So in the future, we may write |00⟩ = |no error⟩, |01⟩ = |X on 3rd⟩, and so forth.

In this case, since the syndrome specifies that a bit flip has been applied to the second qubit it, we can correct this by applying a second bit flip to that qubit. Then, as

$$I \otimes X \otimes I \cdot |\widetilde{\psi}\rangle_L = |\psi\rangle_L,$$

we have recovered our original state and corrected the error. As a result, this code can correct one bit flip error. (Note that like the classical 3-bit repetition code, it cannot correct two bit flip errors.)

#### 3.3 Phase flip error

Suppose, on the other hand, that a phase flip error occurs on one of the qubits—the first qubit, for example. Writing ZII as shorthand for  $Z \otimes I \otimes I$ , this gives the state

$$ZII \cdot |\psi\rangle_L = ZII \cdot (a \cdot |000\rangle + b \cdot |111\rangle)$$
$$= a \cdot |000\rangle - b \cdot |111\rangle.$$

Can we detect this error? Unfortunately, the answer is no:  $a \cdot |000\rangle - b \cdot |111\rangle$  is the encoding of the state  $a \cdot |0\rangle - b \cdot |1\rangle$ , and so this appears to be a legitimate encoding of a state. As a result, although this code can detect a bit flip error, it cannot detect a phase flip error.

#### 3.4 Encoded operations

Suppose we wanted to apply a unitary operation to  $|\psi\rangle$ , but we only have access to the encoded state  $|\psi\rangle_L$ . One thing we could do is unencode  $|\psi\rangle_L$  to produce  $|\psi\rangle$ , apply the unitary, and then reencode the resulting state. However, this defeats the purpose of encoding the state to begin with, as unencoding it makes it vulnerable to errors again. Instead, we would like to apply the unitary by acting directly on the encoded state  $|\psi\rangle_L$ .

Suppose  $|\psi\rangle = a \cdot |0\rangle + b \cdot |1\rangle$  and  $|\psi\rangle_L = a \cdot |000\rangle + b \cdot |111\rangle$ . If we wanted to apply a bit flip to  $|\psi\rangle$ , this would correspond to applying the unitary XXX to  $|\psi\rangle_L$ , as

$$XXX \cdot |\psi\rangle_L = a \cdot |111\rangle + b \cdot |000\rangle$$

which is the encoding of  $X \cdot |\psi\rangle$ . In this case, XXX is referred to as a "logical X" and can be written as  $X_L$  or  $\overline{X}$ .

Similarly, suppose we wanted to apply a phase flip to  $|\psi\rangle$ . Then the corresponding operation on  $|\psi\rangle_L$  would be any of ZII, IIZ, or ZZZ. Any of these could be our choice for the "logical Z" operation  $Z_L = \overline{Z}$ . Note that our logical X operation just applies X to each physical qubit, and this last logical Z operation just applies Z to each physical qubit. These are known as  $transversal\ gates$  because they apply the desired unitary to each qubit in the encoding. They are important for fault tolerance, and we will see them in more detail later in the class.

#### 3.5 Conclusion

We have seen the 3-qubit bit flip code, which protects against a single bit flip error (but not against two or more bit flip errors or a phase flip error). This code was actually first discovered by Asher Peres in 1985 [?] in a work studying how to simulate classical computations on quantum computers and make them robust to noise. (See the interview by Shor [?] where he discusses the relationship of this work to his own.) Next class, we will see another code for correcting phase flip errors, and then we will see how to combine the two to create the 9-qubit code.

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

_No guideline code sources found._

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

_No guideline YouTube video transcripts found._

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

_No additional guideline sources scraped._

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="Albert Einstein, Holograms and Quantum Gravity.md">
<details>
<summary>Albert Einstein, Holograms and Quantum Gravity</summary>

Phase: [EXPLOITATION]

# Albert Einstein, Holograms and Quantum Gravity

[00:00] (A cartoon man with a pointer stands in front of a blackboard filled with complex physics equations and diagrams, two other cartoon people watch him) Physicists have long sought a theory that unifies quantum mechanics with Einstein's theory of gravity, to understand the laws of physics at the largest and the smallest scales.

(The screen fades to black, then shows a cartoon Saturn-like planet and a diagram of an atom with electrons orbiting a nucleus) Could the link come from a holographic principle within string theory called the AdS-CFT correspondence?

(Text appears: "Ads-CFT correspondence", with "correspondence" appearing below the acronym)

(The screen turns white with a logo of connected dots appearing, then morphing into a purple and blue blob, which then tessellates into a pattern. White text on a purple background appears: "In Theory")

[00:30] (A person in a dark movie theater with 3D glasses eats popcorn, watching a 3D shark on the screen which looks scary. The shark on screen looks distorted and colored pink and blue with the glasses off, and the text "2D" appears on screen. With the glasses on, the shark appears blue and 3D with the text "3D" on screen)

Imagine watching a 3D shark film with your 3D glasses on. That was scary. Take off your glasses and the screen looks very different. All the information is encoded on the 2D screen, yet we experience it differently in a higher dimension. Some researchers think quantum gravity may work much the same way.

(The screen turns blue, showing the formula for gravitational force: "Fg = G m1m2/r²")
_The video explains how a 3D experience is encoded in 2D information, likening it to a possible model for quantum gravity._

[00:46] (A cartoon of two spheres connected by a rod rotates, representing a torsion balance experiment. Then, a cartoon of the solar system with the sun and planets orbiting) Gravity is a force that explains how objects interact with each other on a large scale. Like how planets revolve around the sun. (A cartoon shark leaps out of the water, then splashes back down) And why leaping sharks fall back into the water. As Einstein described it, (A cartoon Albert Einstein appears on screen, text "Albert Einstein" above him) gravity results from a curvature in the geometry of space-time.

(A cartoon Earth sits in a distorted grid, showing space-time curvature, text "Gravity results from a curvature in the geometry of space-time." appears below)
But on a quantum level, (Two pink fuzzy spheres are shown, then tiny blue dots move between them) forces are produced by an exchange of particles. (Text "Electric force" appears) And since gravity is far weaker than any other force, (A large blue cartoon shark sits on a fluffy white cloud, with small green dots and a red question mark under its tail) we haven't been able to detect a gravity particle – a graviton – that fits into our understanding of quantum mechanics.

[01:16] (The screen shows an empty, dark movie theater with a white screen. A black, grid-like cone emerges from the screen, with a cartoon Earth at its wider end, representing space-time curvature and gravity. The background of the screen fills with glowing yellow dots, symbolizing quantum theory) Enter the Ads-CFT correspondence, a mathematical mapping similar to a hologram that shows how a region of space-time with gravity emerges out of a purely quantum theory.

(Text "Ads" appears on a blue background, then changes to "Anti-de Sitter space")
The AdS in Ads-CFT stands for Anti-de Sitter space.

[01:31] (A grid-like, bowl-shaped structure appears, representing Anti-de Sitter space, filled with stars. Text "Conformal field theory (a special particle theory)" points to yellow particles at the boundary of the bowl) It's the space-time region that pops up like a hologram from the conformal field theory, or CFT, that describes the particles at the gravity-free boundary of the AdS universe.

(Labels appear: "Anti-de Sitter space (with gravity)" pointing to the inside of the bowl, and "Conformal field theory (a special particle theory)" pointing to the boundary particles) No information is lost in the hologram.

(The bowl-shaped structure closes into a sphere, then flattens into a 2D circle with a hyperbolic tessellation inside) AdS space is negatively curved. It includes gravity and has one more dimension than CFT.

[02:01] (The 3D grid-like sphere appears again, with its upper half transparent, showing the lower half containing stars and particles. Labels appear: "AdS" pointing to the inner space, and "CFT" pointing to the grid boundary) You can think of the Ads-CFT universe as a sphere. The 3D Ads space-time sits inside the sphere, bounded by the 2D gravity-free CFT. The negative curvature of Ads space gives it a boundary, which is needed to make the holographic principle work.

(The sphere rotates, then focuses on a yellow line within the grid) The lower dimensional boundary allows for the correspondence to be a duality, two different ways of looking at a system.

[02:16] (The screen splits into two halves: left shows the 3D shark with 3D glasses on, right shows the pink and blue 2D shark with glasses off) Like seeing the shark with and without 3D glasses.

(The blue background with the bowl-shaped Anti-de Sitter space returns, but the outer surface of the bowl is now a swirling, colorful nebula) The Ads-CFT correspondence is a strong-weak duality.

[02:32] (Yellow particles move around the grid boundary of the bowl, then gather at the bottom. A black hole appears in the Ads side, circled, and a caption "Black hole" appears. Another caption "Quantum soup" points to the lower region of the CFT side) The individual particles on the weakly coupled Ads side correspond to bound states on the strongly coupled CFT side. This means that strongly coupled materials on the CFT side that are too complex to study can be converted into questions about individual particles moving on the Ads side. Or, at a black hole on the Ads side, and what you get on the CFT side is a soup of particles or plasma that physicists can learn about by studying the black holes. And because no information is lost in the holographic principle, gravity on the Ads side maps to the quantum interactions on the CFT side, giving researchers a way to describe gravity on the quantum level.

[03:02] (A flat, distorted grid representing our universe is shown next to the hyperbolic tessellation representing Ads-CFT, text "Our universe (slight positive curvature, no boundary)" on the left, and "Ads-CFT correspondence (negative curvature produces boundary)" on the right. A black hole appears in the center of the grid representing our universe, and another black hole appears in the center of the hyperbolic tessellation) Even though our universe has a different geometry than the Ads-CFT picture, and no boundary, understanding quantum gravity in Ads-CFT could reveal deep insights about black holes and the laws of physics at all scales.

[03:22] (The 3D shark is shown on the movie screen again) So next time you're watching a 3D movie, remember how holographic principles are being used to unlock the secrets of our universe.

(The screen fades to black with stars appearing, then fades to white with credits)
_The AdS-CFT correspondence, a strong-weak duality, allows physicists to study complex quantum systems by mapping them to simpler gravitational problems in Anti-de Sitter space, potentially offering insights into black holes and the fundamental laws of physics._

[03:34] (Credits roll)
Director: Emily V. Driscoll
Producer: Michelle Yun
Animation: Black Powder Design
Writers: Emily V. Driscoll, Natalie Wolchover
Music: Audio Network
Title Animation and Sound: Rosanna Wan
Title Music: Kyle Landstra
Thanks: Jared Kaplan, Tom Hartman, Srinel Jalagani

(Quanta Magazine logo appears with website and social media handles)

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="Black Holes _ Complementarity or Firewalls.md">
<details>
<summary><span id="page-13-0"></span>Black Holes: Complementarity or Firewalls?</summary>

### Black Holes: Complementarity or Firewalls?

Ahmed Almheiri,[1](#page-0-0)\* Donald Marolf,[2](#page-0-1)\* † Joseph Polchinski,[3](#page-0-2)† and James Sully[4](#page-0-3)\*

> \*Department of Physics University of California Santa Barbara, CA 93106

†Kavli Institute for Theoretical Physics University of California Santa Barbara, CA 93106-4030

#### Abstract

We argue that the following three statements cannot all be true: (i) Hawking radiation is in a pure state, (ii) the information carried by the radiation is emitted from the region near the horizon, with low energy effective field theory valid beyond some microscopic distance from the horizon, and (iii) the infalling observer encounters nothing unusual at the horizon. Perhaps the most conservative resolution is that the infalling observer burns up at the horizon. Alternatives would seem to require novel dynamics that nevertheless cause notable violations of semiclassical physics at macroscopic distances from the horizon.

<span id="page-0-0"></span><sup>1</sup>ahmed@physics.ucsb.edu

<span id="page-0-1"></span><sup>2</sup>marolf@physics.ucsb.edu

<span id="page-0-2"></span><sup>3</sup>joep@kitp.ucsb.edu

<span id="page-0-3"></span><sup>4</sup>sully@physics.ucsb.edu

### Contents

| 1 | Introduction                                 | 1  |
|---|----------------------------------------------|----|
| 2 | Complementarity is not enough                | 3  |
| 3 | Further discussion                           | 8  |
|   | 3.1<br>Extension to higher partial waves<br> | 8  |
|   | 3.2<br>Relaxing postulate 2?                 | 9  |
| 4 | Conclusions                                  | 13 |
| A | Approximate projection operators             | 15 |
| B | Effects of Gray-body factors                 | 15 |
| C | Black hole mining revisited                  | 17 |

### <span id="page-1-0"></span>1 Introduction

The black hole information paradox [\[1\]](#page-19-0) presents a sharp conflict between quantum theory and general relativity, and so is an important clue to their unification. Gauge/gravity duality has provided some insight, giving strong evidence that all information is carried away by the Hawking radiation. It is widely believed that an external observer sees this information emitted by complicated dynamics at or very near the horizon, while an observer falling through the horizon encounters nothing special there. These three properties — purity of the Hawking radiation, emission of the information from the horizon, and the absence of drama for the infalling observer — have in particular been incorporated into the axioms of black hole complementarity (BHC) [\[2,](#page-19-1) [3\]](#page-19-2).

Various thought experiments have been examined [\[4,](#page-20-0) [5\]](#page-20-1), and argued to show no inconsistency between the observations of the external and infalling observers[1](#page-1-1) . For example, when a bit is thrown into a black hole, then as long as there is a minimum time of order r<sup>s</sup> ln(rs/lP) before the bit thermalizes and can be reemitted with the Hawking radiation, no observer will see illegal quantum cloning. This time scale has an interesting resonance with ideas from quantum information theory and from Matrix theory [\[7,](#page-20-2) [8,](#page-20-3) [9,](#page-20-4) [10\]](#page-20-5), which suggest that it may actually be achieved.

<span id="page-1-1"></span><sup>1</sup>Limits on complementarity with parametrically many fields have been discussed in Ref. [\[6\]](#page-20-6).

There would be an inconsistency if one were to consider a large Hilbert space that describes both observers at once. Such a Hilbert space appears when quantum gravity is treated as an effective field theory, but it cannot be part of the correct theory of quantum gravity if BHC holds. This is consistent with the idea of holography, wherein quantum gravity is to be constructed in terms of degrees of freedom that are highly nonlocal from the bulk point of view. For guidance in such uncharted waters, as in the earlier revolutions of relativity and quantum theory, it is important to ask what observations are actually possible.

We will consider first a thought experiment that is a small variation on that of Ref. [\[4\]](#page-20-0), differing in that it uses the naturally produced Hawking pairs rather than introducing additional entangled ingoing bits. This leads us to a rather different conclusion, that the thermalization time does not protect us from an inconsistency of BHC. Rather, if the experience of the outside observer is as we have assumed, then the infalling observer must encounter high energy quanta at the horizon. Our first thought experiment requires these only in low partial waves. However, a second thought experiment, using a detector lowered through the potential barrier to the near-horizon region, allows us to probe higher partial waves and come to the same conclusion about these. Thus, the infalling observer either burns up at the horizon, or there must be some novel and likely nonlocal dynamics that extends a macroscopic distance from the horizon, as recently proposed in Refs. [\[11\]](#page-20-7). If the latter, we find that the dynamics would have to be of a rather complicated form.

This analysis was inspired in part by the bit models of Refs. [\[12,](#page-20-8) [13,](#page-20-9) [14,](#page-20-10) [11,](#page-20-7) [15,](#page-20-11) [16\]](#page-20-12), and in particular by the theorem that purity of the Hawking radiation implies that the horizon cannot be 'information-free' [\[12\]](#page-20-8) — that is, unitarity of Hawking evaporation requires O(1) corrections to low energy evolution at the horizon. We have tried to understand the consequences of this argument for complementarity, and to flesh out the bit model into a more complete picture of the dynamics. This leads us to a stronger result, namely that there are either order one corrections to the evolution of high energy modes near the horizon, or the corrections must extend to distances of order the Schwarzschild radius from the black hole.[2](#page-2-0)

We note that the three postulates that are in conflict — purity of the Hawking radiation, absence of infalling drama, and semiclassical behavior outside the horizon — are widely held even by those who do not explicitly label them as 'black hole complementarity.'

<span id="page-2-0"></span><sup>2</sup>After completion of this work we learned that Ref. [\[17\]](#page-20-13) had also argued that black hole evaporation would result in "a loss of trans-event horizon entanglement" and thus "fields far from the vacuum state in the vicinity of the event horizon," termed there an energetic curtain. The argument differs from ours in detail and is based on a model of black hole evaporation that differs from the usual Hawking process and does not satisfy postulate 2. This difference also allows Ref. [\[17\]](#page-20-13) to conclude that the energetic curtain can be delayed beyond the Page time, possibly even until the black hole evaporates to the Planck scale.

### <span id="page-3-0"></span>2 Complementarity is not enough

In considering a slight variant on the thought experiment of Susskind and Thorlacius [\[4\]](#page-20-0), we are unable to find an outcome that is consistent with the postulates of black hole complementarity as stated in Ref. [\[2\]](#page-19-1):

Postulate 1: The process of formation and evaporation of a black hole, as viewed by a distant observer, can be described entirely within the context of standard quantum theory. In particular, there exists a unitary S-matrix which describes the evolution from infalling matter to outgoing Hawking-like radiation.

Postulate 2: Outside the stretched horizon of a massive black hole, physics can be described to good approximation by a set of semi-classical field equations.

Postulate 3: To a distant observer, a black hole appears to be a quantum system with discrete energy levels. The dimension of the subspace of states describing a black hole of mass M is the exponential of the Bekenstein entropy S(M).

We take as implicit in postulate 2 that the semi-classical field equations are those of a low energy effective field theory with local Lorentz invariance.

These postulates do not refer to the experience of an infalling observer, but Ref. [\[2\]](#page-19-1) states a 'certainty,' which for uniformity we label as a further postulate:

Postulate 4: A freely falling observer experiences nothing out of the ordinary when crossing the horizon.

To be more specific, we will assume that postulate 4 means both that any low-energy dynamics this observer can probe near his worldline is well-described by familiar Lorentz-invariant effective field theory and also that the probability for an infalling observer to encounter a quantum with energy E 1/r<sup>s</sup> (measured in the infalling frame) is suppressed by an exponentially decreasing adiabatic factor as predicted by quantum field theory in curved spacetime. We will argue that postulates 1, 2, and 4 are not consistent with one another for a sufficiently old black hole.

Consider a black hole that forms from collapse of some pure state and subsequently decays. Dividing the Hawking radiation into an early part and a late part, postulate 1 implies that the state of the Hawking radiation is pure,

$$|\Psi\rangle = \sum_{i} |\psi_{i}\rangle_{E} \otimes |i\rangle_{L} \,.$$
 (2.1)

Here we have taken an arbitrary complete basis |ii<sup>L</sup> for the late radiation. Following the ideas of Refs. [\[18,](#page-21-0) [7\]](#page-20-2), we use postulates 1, 2, and 3 to make the division after the Page time when the black hole has emitted half of its initial Bekenstein-Hawking entropy; we will refer to this as an 'old' black hole. The number of states in the early subspace will then be much larger than that in the late subspace and, as a result, for typical states |Ψi the reduced density matrix describing the late-time radiation is close to the identity. We can therefore construct operators acting on the early radiation, whose action on |Ψi is equal to that of a projection operator onto any given subspace of the late radiation; this is shown explicitly in appendix [A.](#page-15-0)

To simplify the discussion, we treat gray-body factors by taking the transmission coefficients T to have unit magnitude for a few low partial waves and to vanish for higher partial waves. A more complete discussion of gray-body factors is included in appendix [B](#page-15-1) and shown to lead to the same basic conclusion that we reach below. Since the total radiated energy is finite, this allows us to think of the Hawking radiation as defining a finite-dimensional Hilbert space. The argument in appendix [A](#page-15-0) assumes that the state of the Hawking radiation is effectively random within this space, as is widely assumed. We will argue later that this is not necessary. We also assume, as in Ref. [\[7\]](#page-20-2), that the observer knows the initial state of the black hole and also the black hole S-matrix.

Now, consider an outgoing Hawking mode in the later part of the radiation. We take this mode to be a localized packet with width of order r<sup>s</sup> corresponding to a superposition of frequencies O(r −1 s ). Note that postulate 2 allows us to assign a unique observer-independent lowering operator b to this mode. We can project onto eigenspaces of the number operator b † b. In other words, an observer making measurements on the early radiation can know the number of photons that will be present in a given mode of the late radiation.

Following postulate 2, we can now relate this Hawking mode to one at earlier times, as long as we stay outside the stretched horizon. The earlier mode is blue-shifted, and so may have frequency ω<sup>∗</sup> much larger than O(r −1 s ) though still sub-Planckian.

Next consider an infalling observer and the associated set of infalling modes with lowering operators a. Recall that Hawking radiation arises precisely because

<span id="page-4-0"></span>
$$b = \int_0^\infty d\omega \left( B(\omega) a_\omega + C(\omega) a_\omega^{\dagger} \right) , \qquad (2.2)$$

so that the full state cannot be both an a-vacuum (a|Ψi = 0) and a b † b eigenstate. Here we have again used our simplified gray-body factors.

The application of postulates 1 and 2 has thus led to the conclusion that the infalling observer will encounter high-energy modes. Note that the infalling observer need not have actually made the measurement on the early radiation: to guarantee the presence of the high energy quanta it is enough that it is possible, just as shining light on a two-slit experiment destroys the fringes even if we do not observe the scattered light. Here we make the implicit assumption that the measurements of the infalling observer can be described in terms of an

![](_page_5_Figure_0.jpeg)

Figure 1: Eddington-Finkelstein coordinates, showing the infalling observer encountering the outgoing Hawking mode (shaded) at a time when its size is  $\omega_*^{-1} \ll r_s$ . If the observer's measurements are given by an eigenstate of  $a^{\dagger}a$ , postulate 1 is violated; if they are given by an eigenstate of  $b^{\dagger}b$ , postulate 4 is violated; if the result depends on when the observer falls in, postulate 2 is violated.

effective quantum field theory. Instead we could simply suppose that if he chooses to measure  $b^{\dagger}b$  he finds the expected eigenvalue, while if he measures the noncommuting operator  $a^{\dagger}a$  instead he finds the expected vanishing value. But this would be an extreme modification of the quantum mechanics of the observer, and does not seem plausible.

Fig. 1 gives a pictorial summary of our argument, using ingoing Eddington-Finkelstein coordinates. The support of the mode b is shaded. At large distance it is a well-defined Hawking photon, in a predicted eigenstate of  $b^{\dagger}b$  by postulate 1. The observer encounters it when its wavelength is much shorter: the field must be in the ground state  $a_{\omega}^{\dagger}a_{\omega}=0$ , by postulate 4, and so cannot be in an eigenstate of  $b^{\dagger}b$ . But by postulate 2, the evolution of the mode outside the horizon is essentially free, so this is a contradiction.

To restate our paradox in brief, the purity of the Hawking radiation implies that the late radiation is fully entangled with the early radiation, and the absence of drama for the infalling observer implies that it is fully entangled with the modes behind the horizon. This

is tantamount to cloning. For example [12], it violates strong subadditivity of the entropy,

$$S_{AB} + S_{BC} \ge S_B + S_{ABC}. \tag{2.3}$$

Let A be the early Hawking modes, B be our outgoing Hawking mode, and C be its interior partner mode. For an old black hole, the entropy is decreasing and so  $S_{AB} < S_A$ . The absence of infalling drama means that  $S_{BC} = 0$  and so  $S_{ABC} = S_A$ . Subadditivity then gives  $S_A \ge S_B + S_A$ , which fails substantially since the density matrix for system B by itself is thermal. This argument is exactly as in Ref. [12], where the additional observations we are making are that i) the reasoning holds even under the postulates of black hole complementarity and ii) the modes b and c have high energy as seen by an infalling observer.

Actually, assuming the Page argument [18], the inequality is violated even more strongly: for an old black hole the entropy decrease is maximal,  $S_{AB} = S_A - S_B$ , so that we get from subadditivity that  $S_A \geq 2S_B + S_A$ . Appendix A makes an equivalent assumption, the randomness of the Hawking state, in order to show that measurements of the early radiation predict the state of the late mode with high fidelity. We see from the subadditivity argument that this strong assumption is not needed; it is sufficient that the entropy of the black hole be decreasing. From another point of view, one need not be able to predict the state with perfect fidelity; rather, any information about the state of the b mode precludes the state being annihilated by a.

Note that the measurement of  $N_b$  takes place entirely outside the horizon, while the measurement of  $N_a$  (real excitations above the infalling vacuum) must involve a region that extends over both sides of the horizon. These are noncommuting measurements, but by measuring  $N_b$  the observer can infer something about what would have happened if  $N_a$  had been measured instead. For an analogy, consider a set of identically prepared spins. If each is measured along the x-axis and found to be  $+\frac{1}{2}$ , we can infer that a measurement along the z-axis would have had equal probability to return  $+\frac{1}{2}$  and  $-\frac{1}{2}$ . The multiple spins are needed to reduce statistical variance; similarly in our case the observer would need to measure several modes  $N_b$  to have confidence that he was actually entangled with the early radiation.

One might ask if there could be a possible loophole in the argument: A physical observer will have a nonzero mass, and so the mass and entropy of the black hole will increase after he falls in. However, we may choose to consider a particular Hawking wavepacket which is already separated from the streched horizon by a finite amount when it is encountered by the infalling observer. Thus by postulate 2 the further evolution of this mode is semiclassical and not affected by the subsequent merging of the observer with the black hole. In making this argument we are also assuming that the dynamics of the stretched horizon is causal.

Ref. [19], in response our argument, has claimed that it is not possible to measure the state of the early radiation in the basis that is required for our argument due to gravitational

effects. Essentially we are taking the early radiation as input to a quantum computation in the flat region distant from the black hole, which then returns the desired bit in an easily measured form. We do not see an argument that would forbid such computations. Note that in order to distinguish a pure state of Hawking radiation from a mixed state, it is also necessary to measure the state of the radiation in many bases; thus the claim of Ref. [\[19\]](#page-21-1) would mean that there is no information problem in the first place.

Ref. [\[20\]](#page-21-2) raises a related issue, that the quantum computation might take longer than the black hole lifetime to carry out. The most precise formulation of the information problem is in AdS spacetime, where the geometry itself serves to confine the Hawking quanta [\[21,](#page-21-3) [22\]](#page-21-4). We can use a similar strategy here: consider an N = 4 Yang-Mills theory on S 3 , dual to AdS gravity, in addition to a reference system consisting of a large collection of spins. Prepare the total system in a pure state, with the Yang-Mills theory fully entangled with the spins, such that its density matrix is thermal with a temperature above the Hawking-Page transition [\[21\]](#page-21-3). In effect we are using the spins in place of the early radiation. But since the spins do not live in the AdS space, there are clearly no constraints of time or gravitation that could prevent an observer from measuring Pˆ and then diving into the black hole and finding, via our argument, high energy quanta.[3](#page-7-0)

Thus far the asymptotically flat discussion applies to a black hole that is older than the Page time; we needed this in order to frame a sharp paradox using the entanglement with the Hawking radiation. However, we are discussing what should be intrinsic properties of the black hole, not dependent on its entanglement with some external system. After the black hole scrambling time [\[7,](#page-20-2) [8\]](#page-20-3), almost every small subsystem of the black hole is in an almost maximally mixed state. So if the degrees of freedom sampled by the infalling observer can be considered typical, then they are 'old' in an intrinsic sense. Our conclusions should then hold. If the black hole is a fast scrambler the scrambling time is r<sup>s</sup> ln(rs/lP), after which we have to expect either drama for the infalling observer or novel physics outside the black hole. Ref. [\[20\]](#page-21-2) has suggested that the existence of the high energy quanta might be a special observable which is governed by the Page time rather than the fast scrambling time. We view this as an open question pending development of a dynamical theory of these quanta and how they form.

<span id="page-7-0"></span><sup>3</sup> We have deliberately chosen the reference system not to have a geometric dual. In the case where it is a second copy of the gauge theory [\[22\]](#page-21-4), there are additional subtleties [\[23\]](#page-21-5).

### <span id="page-8-0"></span>3 Further discussion

#### <span id="page-8-1"></span>3.1 Extension to higher partial waves

It is well known that Hawking radiation from an asymptotically flat Schwarzschild black hole is dominated by low angular momentum modes; see e.g. [\[28\]](#page-21-6). This is a consequence of the fact that a black hole of Hawking temperaure T<sup>H</sup> and Schwarzschild radius r<sup>s</sup> has THr<sup>s</sup> ∼ 1, so that high angular momentum modes of energy T<sup>H</sup> are trapped behind a large barrier in the effective radial potential. One might therefore be tempted to believe that the issue discussed in section [2](#page-3-0) concerns only a small number of partial waves. Since a local observer is unlikely to encounter such quanta, one might then conclude that a (much-weakened) version of postulate 4 might still hold in which the suppression is replaced by a fixed (1/area) power law.[4](#page-8-2)

This would already be a striking result: these quanta must appear quite close to the horizon (see Fig. 1) and so violate the standard wisdom that the horizon is not a distinguished location. And they are not rare in the sense that their number is of the same order as the number of actual Hawking quanta. However, we will argue for an even stronger result, by considering a thought experiment in which the centrifugal barrier is penetrated.

As noted long ago by Unruh and Wald [\[29\]](#page-21-7), it is possible to 'mine' energy from the modes trapped behind the effective potential. The basic procedure is to lower some object below the potential barrier, let the object absorb the trapped modes, and then raise the object back above the barrier. Unruh and Wald thought of the object as a box that could be opened to collect ambient radiation and then closed to keep the radiation from escaping. One may also visualize the object as a particle detector, though the two are equivalent at the level discussed here.

We analyze a particular version of the mining process in appendix [C](#page-17-0) in order to address gravitational back-reaction and other concerns not considered in [\[29\]](#page-21-7); see also [\[30\]](#page-21-8) for similar conclusions. While these additional issues limit the rate at which our process can mine energy to below that predicted by [\[29\]](#page-21-7) (see footnote [10\)](#page-18-0), they do not change the basic result that energy can be extracted from the high angular momentum modes. In fact, we are unable to identify any fundamental constraint that would forbid the extraction of energy from any mode separated from the horizon by more than a Planck distance `p.

In the context of such a mining operation, the arguments of section [2](#page-3-0) can be applied to the higher partial waves as well. One need only consider the internal state of the mining equipment to be part of the late-time Hawking radiation. In particular, postulate 2 can be

<span id="page-8-2"></span><sup>4</sup> In addition, one would need to propose a mechanism through which these quanta would arise from the infalling perspective. This would appear to require that the infalling observer experience violations of local quantum field theory at this (power-law-suppressed) level.

used to evolve the mode b to be mined backward in time and to conclude for an old black hole that, even before the mining process takes place, the mode must be fully entangled with the early-time radiation. Postulate 4 is then violated for these modes as well, suggesting that the infalling observer encounters a Planck density of Planck scale radiation and burns up. One might say that the black hole is protected by a Planck-scale firewall.

The arguments that we have given for the firewall are largely built on those that have been used to support the fuzzball picture [\[12\]](#page-20-8), and one might wonder whether the fuzzball provides the actual dynamical picture of the firewall. It is not clear to what extent there is a well-defined fuzzball construction for macroscopic nonextremal black holes, but our conclusions seem to contradict the scenario advocated in [\[16\]](#page-20-12), which incorporates a form of complementarity such that an infalling observer sees nothing unusual on the horizon (though he may be constructed in some dual form on the branes). Since the branes are thought of as extending only a microscopic distance above the horizon, essentially a realization of the stretched horizon, postulate 2 holds and our argument would apply. Ref. [\[27\]](#page-21-9) has reiterated this complementarity conjecture, but does not address our arguments directly.

A sharp end to spacetime, similar to the firewall, arose in a related context in Ref. [\[31\]](#page-22-0) (though see [\[23\]](#page-21-5) for comments). Additional earlier suggestions that the geometry end at the horizon, or that the interior geometry is very different from Schwarzschild, include Ref. [\[24\]](#page-21-10), whose connection with general relativity is not clear, Ref. [\[25\]](#page-21-11), using sources that violate various energy conditions, and Ref. [\[26\]](#page-21-12), using a higher derivative action. Other works have reached similar conclusions from quite different starting points. These include Ref. [\[32\]](#page-22-1), which attempts to argue that the black hole S-matrix hypothesis requires strong interactions between ingoing and outgoing particles such that the former never cross the horizon, and ref. [\[33\]](#page-22-2), which starts from the assumption that acts far outside the black hole can causally affect spacelike separated observers in the interior.

Note that this firewall need not be visible to any observer that remains outside the horizon. All that we have argued is that the infalling observer does not experience a pure state. There remains considerable freedom in the possible reduced density matrices that could describe a few localized degrees of freedom outside the black hole, so that this matrix might still agree perfectly with that predicted by Hawking [\[34\]](#page-22-3). In this case any local signal that an external observer might hope to ascribe to the firewall at distance 1/ω<sup>∗</sup> cannot be disentangled from the Unruh radiation that results from probing this scale without falling into the black hole.

### <span id="page-9-0"></span>3.2 Relaxing postulate 2?

Postulate 2 plays a crucial role in any version of our argument, allowing us to use low energy effective gravity to associate a unique observer-independent operator b with the designated mode and to evolve it in time. The purity of Hawking radiation implies a breakdown of semiclassical physics, but the usual complementarity assumption as stated in this postulate is that the complicated dynamics that leads to re-emission of information takes place, from the point of view of the exterior observer, only on the stretched horizon a Planckian distance above the event horizon. A possible alternative to the firewall is thus that this postulate should be relaxed, giving some novel (and perhaps non-local) evolution that extends a finite distance from black hole as has recently been proposed in Ref. [11]. We agree with [11] that one would like to keep such novel physics to a minimum.

However, if we are to relax postulate 2 then the modified dynamics must not only be more nonlocal than expected, but also much larger in magnitude. It is generally believed that the return of information requires modification of the Hawking calculation only for observables involving O(S) quanta, or in effects of order  $e^{-S}$ , or [22] for small numbers of quanta over extremely long time-scales. However, preservation of postulates 1 and 4 requires that an  $N_a$  eigenstate evolve to an  $N_b$  eigenstate, which is an O(1) effect visible in the two-point function over time scales not much larger than the light-crossing time.

Note that our thought experiment is very similar to that in Ref. [4], except that instead of using bits thrown into the black hole, it uses the naturally produced Hawking bits. In the former case, an observer who has seen the exterior bit cannot see its interior clone, basically because it is too deep in the interior after a scrambling time of at least  $r_{\rm s} \ln(r_{\rm s}/l_{\rm P})$ . In the case we consider, the scrambling time does not seem to enter in the same way: the infalling observer encounters the high energy quantum right behind the horizon, at a distance  $\omega_*^{-1}$ .<sup>5</sup>

We should therefore ask how the scrambling time might affect the argument. Decay is not an equilibrium process, and after emission of a Hawking quantum there will be a delay before the black hole returns to its typical state, just as there is when it absorbs a quantum.<sup>6</sup> It is interesting that the conjectured fast-scrambling time  $r_{\rm s} \ln(r_{\rm s}/l_{\rm P})$  is the same magnitude as the time during which the Hawking mode moves out from the stretched horizon to a macroscopic distance  $O(2r_{\rm s})$ , and during which it redshifts from a near-Planckian energy to  $O(r_{\rm s}^{-1})$ . We therefore investigate what form of time evolution would be needed to restore postulate 4.

Consider an old black hole containing N bits in a basis state  $|j\rangle$ ; the full state of the system is given by a sum over j, entangled with the outgoing Hawking radiation. Immediately after emission of a Hawking mode (which we idealize as a single bit) from the stretched horizon, postulate 4 requires that the mode be entangled with the modes behind the horizon. We must therefore use a state of N+1 bits to describe the resulting hole, so that the evolution

<span id="page-10-0"></span><sup>&</sup>lt;sup>5</sup>It is worth noting that nowhere in our argument do we consider 'nice slices,' which extend deep into the black hole interior and which often enter into discussions of the breakdown of effective field theory in black holes. All observations are limited to the exterior and a small distance  $\omega_*^{-1}$  behind the horizon.

<span id="page-10-1"></span><sup>&</sup>lt;sup>6</sup>To be precise, it never reaches a fully typical state, as additional emissions occur in the meantime.

is

<span id="page-11-1"></span>
$$|j\rangle \to \sum_{k} |j, k; k\rangle$$
. (3.1)

We have taken a convenient basis in which k is the state of the Hawking bit and we have singled out the interior bit with which it is entangled. After the thermalization time, the hole has only N − 1 bits, and

<span id="page-11-0"></span>
$$\sum_{k} |j, k; k\rangle \to \sum_{l, m} |l; m\rangle \langle l; m|j\rangle. \tag{3.2}$$

The N bits of j are mapped into the N − 1 bits of l plus the outgoing bit m. The effect is that one bit of entanglement with the earlier radiation is transferred to to the outgoing bit k.

Eq. [\(3.2\)](#page-11-0) describes unitary evolution from an N bit space indexed by j to (N − 1) + 1 bit spaces indexed by l and k. The state on the left is embedded in a space of N + 2 bits, but the evolution has been specified only when two are in a definite state. For any other state of these two bits there is a high energy quantum near the horizon, which should be atypical in the black hole Hilbert space. Our description differs from the bit models of [\[12,](#page-20-8) [14,](#page-20-10) [11,](#page-20-7) [15,](#page-20-11) [16\]](#page-20-12) through the explicit description of these bits before thermalization occurs, i.e. the intermediate state in Eqs. [\(3.1,](#page-11-1) [3.2\)](#page-11-0). This will play a key role below. Note that the evolution [\(3.2\)](#page-11-0) cannot be thought of as simple thermalization of the black hole, because it evolves from a Hilbert space of N + 1 bits to one of N − 1 bits.[7](#page-11-2) Rather, it acts unitarily on the whole {black hole + outside Hawking mode} system.

In other words, we have again arrived at the above-mentioned possibility that novel and perhaps non-local dynamics extends a finite distance `new from the black hole. The size of `new will set the scale of radiation encountered by the infalling observer. If this novel physics is associated with thermalization, then `new ∼ r<sup>s</sup> as proposed in [\[11\]](#page-20-7) so that an infalling observer sees only radiation with ω<sup>∗</sup> ∼ r −1 s in rough agreement with the prediction of local field theory.

Perhaps this is the way things work though, if so, there seem to be significant further implications. Ref [\[11\]](#page-20-7) envisioned this new effect as acting only on a few partial waves of otherwise essentially free fields. The analogous statement here would be that it acts on the internal state of any mining equipment used to extract energy from the black hole, including

$$|j,k'\rangle \to \sum_{l} |l\rangle\langle l;k'|j\rangle$$
. (3.3)

This is nonunitary evolution from a space of N + 1 bits to one of N −1 bits: note that k 0 is in the ket on the left and the bra on the right. This is similar to the nonunitary evolution appearing in the black hole final state conjecture [\[35\]](#page-22-4).

<span id="page-11-2"></span><sup>7</sup>We could try to describe this as acting only on the black hole degrees of freedom by projecting with a Hawking mode hk 0 | to get

for example notes that the equipment might print on paper and then lock in a vault in order to record the results of the experiment.

Even this appears appears to be insufficient. Let us suppose that the equipment can manipulate the quantum data in the storage bit, say on receipt of a signal from far away, so as to perform an arbitrary unitary U transformation on the storage bit. Then the analogue of equation [\(3.1\)](#page-11-1) becomes

<span id="page-12-0"></span>
$$|j\rangle \to \sum_{k} |j, k; Uk\rangle$$
. (3.4)

We might take U to permute the storage bit basis states k, or we might take it to act as the phase (−1)<sup>k</sup> . For each |ji, allowing U to range over all unitary operations generates a basis for a Hilbert space of dimension 4. In this sense, the right hand side of [\(3.4\)](#page-12-0) spans a full N + 2 bit Hilbert space. There can thus be no U-independent analogue of equation [\(3.2\)](#page-11-0) involving only a remaining N − 1 bit black hole and 1 additional storage bit. Note that explicit dependence of the Hamiltonian on U would violate the usual rules of quantum mechanics.

Unless there is some physical constraint that restricts their initial state, including any other finite number of bits is not helpful. Without such a restriction, these bits can neither provide a useful record of transformation U, nor can they be used as an empty box into which to deposit the information about U in [\(3.4\)](#page-12-0). They simply add equally to the dimensions of the Hilbert spaces on the left- and right-hand sides of the supposed new version of [\(3.2\)](#page-11-0) with no effect on the 2 bit mismatch noted above.

Since one clear restriction is the existence of the storage bits themselves, an effect that destroys these bits as they are transported back to large r might suffice. A final alternative might be to couple to the infinite number of states associated with occupation numbers in outgoing radiative modes, though one would expect such a coupling to modify even the mean rate at which energy and/or information escape from the black hole. Seeing no more gentle alternatives, we therefore disagree with [\[11\]](#page-20-7) that this new physics can be 'innocuous' in all of the senses described there.

The alternative would appear to be that some yet unknown new physics (or some effect that we have neglected) simply prevents energy from being mined closer to the horizon than `new. This might be a new fixed scale or some geometric mean of `<sup>p</sup> and rs. There would then be no obvious reason to believe that infalling observers experience radiation above the scale 1/`new, though one would certainly expect them to see some violation of local quantum field theory. This scenario is realized in certain models of local quantum field theory that violate local lorentz invariance [\[36\]](#page-22-5). In these models, there are simply no outgoing modes within distance `new of the horizon. Some additional physics would of course be needed to transfer information to the Hawking-like modes at the scale `s, but since we have removed the possibility of mining the radiation at a lower scale, this effect can now be limited to the natural Hawking-like modes themselves.

Recently, Refs. [\[43,](#page-23-0) [44,](#page-23-1) [45,](#page-23-2) [46\]](#page-23-3) have suggested that an extended "strong" complementarity principle might survive. In particular, an asymptotic observer would see an eigenstate of Nb, and infalling observer an eigenstate of Na. This abandons the strong form of postulate 2, that we can use effective field theory freely outside the horizon, but has been argued to preserve a weaker postulate that no single observer can see a violation of effective field theory. We disagree. One can consider a continuous family of possible observers, falling in at different times. One who meets a mode near the stretched horizon sees an N<sup>a</sup> eigenstate, and one who meets it far from the black hole sees an N<sup>b</sup> eigenstate. Observers in between would see a continuum of interpolating states. But two close-spaced observers can communicate (or a single observer can carry an apparatus that measures time-dependence near his worldline), so this time-dependence is detectable and violates effective field theory: the weakened postulate appears to be no safer than the strong one.

More theoretically, note that Eq. [\(2.2\)](#page-4-0) is basic to the derivation of Hawking radiation, with the LHS evaluated by an asymptotic observer and the RHS constrained by the fact that an infalling observer sees near-vacuum (by the adiabatic principle). If one rejects this as meaningless because no observer can see both sides, then one has the burden of providing a new theory to derive the Hawking flux, in which this equation is replaced by something presumably more complicated. Still further concerns about this idea were raised in [\[47\]](#page-23-4).

# <span id="page-13-0"></span>4 Conclusions

Historically, the black hole information paradox presented three main alternatives, each problematic: information loss, purity of the Hawking radiation, and remnants. The discovery of gauge/gravity duality pointed to purity, and to a fundamentally nonlocal formulation of quantum gravity. Our work again seems to present some sharp and perhaps unpalatable alternatives: a firewall at the horizon, or novel and probably nonlocal dynamics extending a macroscopic distance outside the horizon. (We note that the firewall also has elements of nonlocality, in that its location, the horizon, is not determined by any local feature but by a global property.) The second alternative has the potential to connect with one of the notable features of BHC, the fast-scrambling time scale, but our attempt to determine possible forms of the dynamics leads us to conclude that it would nevertheless cause notable violations of semiclassical physics at macroscopic distances from the horizon.

The tensions noted in this work may lead the reader to wonder whether even the most basic coarse-grained properties of Hawking emission as derived in [\[34\]](#page-22-3) are to be trusted. But the thermodynamic picture of black holes now rests on many pillars that remain intact. Even at the microscopic level, at least in string theory, independent evidence for thermal emission from black holes comes from studies of low energy excitations of D-branes and from AdS/CFT. This leads one to suspect that some appropriately weakened version of postulates 2 and 4 might be retained in order to help explain the success of the Hawking calculation, though finding a consistent scenario remains a challenge.

Let us conclude by briefly commenting on more general causal horizons, which of course share many features in common with black holes. For example, the reader will note that we pass through Rindler horizons all the time and do not burn up or experience obvious new physics. We believe that this is due to an essential difference between Rindler and black hole horizons. Since Rindler horizons have infinite entropy, their quantum memory never fills. 'Young' Rindler horizons never evolve to become 'old.' From another point of view, the fact that Rindler horizons do not evaporate makes it impossible to apply the arguments of section [2.](#page-3-0)

One might also ask about cosmological horizons, such as those in de Sitter space. These are more like black holes in that they have finite entropy, though they still do not evaporate. The experimental evidence is also not clear cut. Our present universe is just now emerging into an era dominated by dark energy. As a result, any cosmological horizons through which we cross soon should be expected to be young. Even if they behave like fast-scrambling (r<sup>s</sup> ln rs) black holes it will be a time ∼ 60 times the age of our universe before they become old. On the other hand, the fact that early universe inflation must last more than 60 efoldings suggests that the associated cosmological horizons may have become old. We leave for future work the question of whether this would significantly affect its predictions for cosmology and whether this argues that, despite their finite entropy, cosmological horizons differ fundamentally from black holes.

## Acknowledgments

We thank Raphael Bousso, Adam Brown, Steve Giddings, David Gross, Daniel Harlow, Patrick Hayden, Samir Mathur, Yasunori Nomura, John Preskill, Mark Srednicki, Douglas Stanford, Lenny Susskind, Bill Unruh, Aron Wall, and all of the participants of the KITP Bits, Branes, and Black Holes program for useful discussions. AA, JS, and JP were supported in part by NSF grants PHY05-51164 and PHY07-57035, and by FQXi grant RFP3-1017. DM was supported in part by the National Science Foundation under Grant Nos PHY11- 25915 and PHY08-55415, by FQXi grant RFP3-1008, and by funds from the University of California. He also thanks the Kavli Institute for Theoretical Physics for their hospitality during much of this work.

### <span id="page-15-0"></span>A Approximate projection operators

Consider the projection operator onto state |ii<sup>L</sup> in some orthonormal basis for the late radiation, P <sup>i</sup> = |iiLhi|L. We consider the case that the Hawking state |Ψi is chosen with uniform measure, as in the microcanonical ensemble; in Appendix B we will discuss a slight generalization. Then the operator

$$\hat{P}^i = L|\psi_i\rangle_E\langle\psi_i|_E, \qquad (A.1)$$

which acts on the state of the early radiation, allows us to anticipate the measurement of P i if E L. Here E and L are the dimensions of the early and late Hilbert spaces (so 1 ≤ i, j, . . . ≤ L, while 1 ≤ a, b, . . . ≤ E for an E-basis to be introduced later). That is,

$$\hat{P}^i|\Psi\rangle \approx P^i|\Psi\rangle = |\psi_i\rangle_E \otimes |i\rangle_L. \tag{A.2}$$

If the |ψii<sup>E</sup> were orthogonal with equal norms, this would be an equality, and we show that it approaches this for typical states |Ψi when L E.

The relative error is

$$\mathcal{E} = \frac{\|(P^i - \hat{P}^i)|\Psi\rangle\|^2}{\|P^i|\Psi\rangle\|^2} = (1 - L\langle\psi_i|\psi_i\rangle_E)^2 + L^2 \sum_{j \neq i} |\langle\psi_i|\psi_j\rangle_E|^2$$
(A.3)

Expanding in an orthonormal basis |ψii<sup>E</sup> = P<sup>E</sup> <sup>a</sup>=1 cia|aiE, the average over |Ψi with the uniform measure gives

<span id="page-15-3"></span>
$$\overline{c_{ia}c_{jb}^*} = \frac{1}{LE}\delta_{ij}\delta_{ab}, \qquad \overline{c_{ia}c_{jb}^*c_{kc}c_{ld}^*} = \frac{1}{L^2E^2}(\delta_{ij}\delta_{kl}\delta_{ab}\delta_{cd} + \delta_{il}\delta_{jk}\delta_{ad}\delta_{bc})$$
(A.4)

(dropping terms of relative order 1/LE), and so

<span id="page-15-4"></span>
$$\overline{\langle \psi_i | \psi_j \rangle_E} = \frac{1}{L} \delta_{ij} , \qquad \overline{\langle \psi_i | \psi_j \rangle_E \langle \psi_k | \psi_l \rangle_E} = \frac{1}{L^2} \delta_{ij} \delta_{kl} + \frac{1}{L^2 E} \delta_{il} \delta_{jk} . \tag{A.5}$$

Then for E L 1,

<span id="page-15-2"></span>
$$\overline{\mathcal{E}} = \frac{L}{E} \,. \tag{A.6}$$

This decreases exponentially after the halfway point of the black hole's life. While the explicit calculations above refer to projections onto a one-dimensional space, [\(A.6\)](#page-15-2) also holds for more general projections given by sums of the Pˆ<sup>i</sup> above.

### <span id="page-15-1"></span>B Effects of Gray-body factors

In the linear approximation, each quantum field outside the black hole may be decomposed using spherical harmonics. Each mode then leads to an effective 1+1 scattering problem in an effective potential which depends on the mode's angular momentum j. The annihilation operators b, c, d corresponding to the outgoing mode outside the barrier (b), the incoming mode outside the barrier (c), and the outgoing mode inside the barrier (d) are then related by reflection and transmission coefficients R, T through  $b = T^*d + \frac{RT^*}{T}c$ , so that

$$N_b = |T|^2 N_d + RT^* d^{\dagger} c + R^* T c^{\dagger} d + |R|^2 N_c.$$
(B.1)

On the other hand, (2.2) now becomes

$$d = \int_0^\infty d\omega \left( B(\omega) a_\omega + C(\omega) a_\omega^{\dagger} \right) . \tag{B.2}$$

As usual in a scattering problem, the incoming modes on opposite sides of the barrier are completely independent. Thus  $c, c^{\dagger}$  commute with  $a_{\omega}, a_{\omega}^{\dagger}$ .

Although the gray-body coefficients complicate the relation between the outgoing Hawking modes b and the infalling modes a, it remains true that the number operators  $N_b, N_{a_{\omega}}$  fail to commute unless the transmission coefficient T is very small. In particular, even when acting on a state in the  $a, \tilde{a}$ , and c vacuum  $(c|\psi\rangle = a_{\omega}|\psi\rangle = \tilde{a}_{\omega}|\psi\rangle$  for all  $\omega$ ) we have

<span id="page-16-0"></span>
$$N_b|\psi\rangle = T(T^*d^{\dagger} + R^*c^{\dagger}) \int_0^{\infty} d\omega \, C(\omega) a_{\omega}^{\dagger}|\psi\rangle,$$
 (B.3)

which for an infalling observer contains of order  $|T|^2$  particles for small T.

Since T decreases exponentially for large j, the state (B.3) is indistinguishable from the infalling vacuum for large j. But for the first few partial waves it leads to a noticeable flux of particles for infalling observers.

Due to gray body factors, the state of the Hawking radiation also deviates from the microcanonical ensemble assumed in Appendix A. To model this effect we replace

$$\delta_{ij}/L \to p_j \delta_{ij} \,, \quad \delta_{ab}/E \to \tilde{p}_a \delta_{ab}$$
 (B.4)

in the expectation values (A.4), with the  $p_i$  and  $\tilde{p}_a$  each summing to unity. Then the expectation values (A.5) become

$$\overline{\langle \psi_i | \psi_j \rangle_E} = p_i \delta_{ij} , \qquad \overline{\langle \psi_i | \psi_j \rangle_E \langle \psi_k | \psi_l \rangle_E} = p_i p_k \delta_{ij} \delta_{kl} + p_i p_k (\sum_a \tilde{p}_a^2) \delta_{il} \delta_{jk} . \tag{B.5}$$

For the approximate projection operator we take

$$\hat{P}^i = |\psi_i\rangle_E \langle \psi_i|_E / p_i \,. \tag{B.6}$$

One then finds

$$\overline{\mathcal{E}} = \frac{\sum_{a} \tilde{p}_{a}^{2}}{p_{i}}.$$
(B.7)

The numerator is of order 1/E<sup>0</sup> where E 0 is the number of states of the early radiation that are populated with significant probability. The denominator is similarly of order 1/L<sup>0</sup> for states of the final radiation that are populated with significant probability, so the conclusion is the same as before for these states. Note that we have assumed that the late-time density matrix is diagonal in the late basis i in which we project. The semi-classical analysis [\[34\]](#page-22-3) suggests that this is the case, to good approximation, for the occupation number basis.

### <span id="page-17-0"></span>C Black hole mining revisited

We now study a specific process for mining energy from the high angular momentum modes of a (say, Schwarzschild) black hole's thermal atmosphere in order to examine constraints beyond those addressed in [\[29\]](#page-21-7). These modes lie close to the horizon. We therefore wish to lower a detector to within a proper distance L r<sup>s</sup> of the horizon, so that we probe modes of angular momentum rs/L 1. We take the detector to be of size ∼ L and (unexcited) mass mdet = <sup>−</sup><sup>1</sup>L −1 . Here is a small constant (e.g., 1/100 or 10<sup>−</sup><sup>6</sup> ) independent of r<sup>s</sup> and the Planck scale `p. The detector is attached to one end of a tension µ cosmic string.[8](#page-17-1) This attachment presumably makes use of an appropriate monopole that allows the string to end, which we think of as part of our detector. The other end of the cosmic string is attached to a static Dyson sphere of radius r<sup>0</sup> ∼ −1 r<sup>s</sup> which completely encloses the black hole.[9](#page-17-2) We work in d ≥ 4 spacetime dimensions.

The detector is to be lowered from r<sup>0</sup> to within a proper distance L `<sup>p</sup> of the horizon, where the locally measured temperature is Tloc ∼ 1/L. Since mdet Tloc, the detector can remain stable in this thermal bath. In particular, there is little danger of it colliding with an anti-detector in black hole's thermal atmosphere.

At higher altitudes the detector does not interact significantly with the black hole's thermal atmosphere due to its small physical size and the resulting small cross-section for absorption. But it will begin to do so at the target height L. The absorption of a Hawking photon increases the mass of the detector by the relatively small amount Tloc ∼ L <sup>−</sup><sup>1</sup> = mdet. The detector is to be left in place long enough to absorb a Hawking photon (which requires an asymptotically measured time of order rs) and then lifted back to r0. As discussed in [\[29\]](#page-21-7), the net amount of energy extracted from the black hole is of order TH. We must choose µ = mdet/L ∼ <sup>−</sup><sup>1</sup>L −2 so that it can support the weight of the detector at the height L. This

<span id="page-17-1"></span><sup>8</sup>The extraction of energy from black holes via cosmic strings was also studied by Lawrence and Martinec [\[37\]](#page-22-6) and by Frolov and Fursaev [\[38\]](#page-22-7). They considered strings that pierce the horizon, while we intentionally keep our apparatus outside. We avoid direct coupling to the black hole so as not to confuse our investigation of the high angular momentum modes in the thermal atmosphere of the black hole.

<span id="page-17-2"></span><sup>9</sup>We choose a Dyson sphere for simplicity. One could also use orbiting space stations. For small enough orbital velocities, the motion of the space station should not affect the detector during the time that it is active.

condition also ensures that the local temperature at L satisfies  $T_{\text{loc}}^2 \ll \mu$  so that closed loops of string are not a significant part of the thermal atmosphere at this depth. We note that the natural width  $\mu^{-1/2}$  of the cosmic string is much less than L.

It is natural to ask if gravitational back-reaction might prevent our experiment from taking place. There are potential issues at both large and small scales, but it is easy to check that both are avoided. Large-scale back-reaction is shown to be small by noting that the total (asymptotically-measured) energy of our apparatus is small compared to the mass  $M_{BH}$  of the black hole. Indeed, this energy satisfies

$$E_{\text{apparatus}} \lesssim \mu r_0 + m_{\text{det}} = \epsilon^{-1} L^{-1} (r_s/\epsilon L + 1) \sim \epsilon^{-2} r_s/L^2 \ll r_s/\ell_p^2.$$
 (C.1)

So since  $d \geq 4$  we have

$$E_{\text{apparatus}} \ll \frac{r_s}{\ell_p^2} \left(\frac{r_s}{\ell_p}\right)^{d-4} \sim M_{BH},$$
 (C.2)

and there is no further restriction on our experiment<sup>10</sup>.

At small scales, one might ask whether our waiting detector is close enough to the black hole to be engulfed by even a small tide raised on the horizon by the gravitational field of our apparatus. But since tidal effects are short-ranged ( $\sim 1/r^{d-1}$ ), such a tide will be due mostly to the detector and the very bottom part of the string (within  $\sim L$  of the horizon). It can therefore be addressed using the Rindler approximation to the black hole geometry. Dimensional analysis, the lack of any scales in Rindler space, and the fact that the detector mass can enter only through  $Gm_{\rm det}/T_H$  then imply that there can be no such effect for

<span id="page-18-1"></span>
$$L \gg \ell_p (m_{\text{det}}/T_{\text{loc}})^{1/(d-2)} \sim \ell_p \epsilon^{-1/(d-2)}.$$
 (C.3)

Our discussion above involved the use of a cosmic string. For more mundane strings, one would be forced to consider whether the string is in fact strong enough to support its own weight and that of the detector being raised. It turns out [30] that any sufficiently strong string acts much like a cosmic string. But this observation raises a final concern: As opposed to jump ropes and bicycle chains, the tension of a cosmic string is fixed once and for all. We can choose parameters so that our detector is in static equilibrium at height L (so that the upward pull from the string balances the gravitational attraction of the black hole), but this equilibrium is necessarily unstable.

<span id="page-18-0"></span><sup>&</sup>lt;sup>10</sup> However, back-reaction does prevent one from placing an arbitrary number of such strings near the black hole. This limits the number of mining processes that can run concurrently and thus the total rate at which energy can be extracted from the black hole. Since there are  $\sim (R/L)^{d-2}$  Hawking quanta at the scale L, one would like to use  $N_A \sim (R/L)^{d-2}$  copies of our apparatus. The constraint  $E_{\rm apparatus} \ll M_{BH}$  then requires  $L^d \gg r_s^2 \ell_p^{d-2}$  and allows us to mine energy only at rates  $E/t \ll M_{BH}/t_{\rm extract}$  for  $t_{\rm extract} = T_H^{-1} (r_s/\ell_p)^{2(1-2/d)}$  in agreement with [38]. Similar arguments will appear in [30]. Without this constraint, one would obtain the Unruh-Wald result  $t_{\rm extract} \sim T_H^{-1}$ .

Let us therefore suspend our detector on a pair of cosmic strings, instead of just one, so that the two strings meet at our detector with some non-zero angle. The upward force then depends on the angle between the two strings. As with a piano wire, the net force increases when the string is pulled downward. This effect can be used to stabilize the detector at its operating location, and the detector can be raised and lowered by moving top ends of the strings along the Dyson sphere.

Moving the detector adiabatically slowly makes the process reversible so that no excess energy is left behind in the black hole. In fact, one can perform the experiment well within the natural black hole evaporation time  $t_{evap} \sim r_s^{d-1}/\ell_p^{d-2}$  of a  $d \geq 4$  an asymptotically flat black hole without generating significant entropy. This can be seen by first noting that (C.3) implies, even if the detector were to fall through the horizon, that the formation of caustics is not relevant to the production of horizon entropy [39, 40]. One may then use the Raychaudhuri equation parametrized by Killing time instead of affine parameter as in derivation of the physical process first law [41] to write

$$\Delta A \sim r_s \int dt \, dA \, \sigma^2,$$
 (C.4)

where we have taken the right-hand side of the Raychaudhuri equation to be dominated by the shear contribution  $\sigma^2$  generated by gravitational tides from the moving detector. Compare with e.g. eqn. (2.7) of [40]. Since tidal effects decrease rapidly with distance, the integrals are dominated by the UV scale L and we have

$$\frac{\Delta A}{\ell_p^{d-2}} \sim r_s \frac{\ell_p^{d-2} m_{\text{det}}^2}{L^{d-3}} \left(\frac{r_s}{L} \frac{dL}{dt}\right)^2 \sim \frac{r_s^3}{\epsilon^2 L t^2} \left(\frac{\ell_p}{L}\right)^{d-2},\tag{C.5}$$

where  $\frac{dL}{dt}$  represents a typical value characterizing the motion of the detector at the scale L (which is related to a typical velocity  $v = \frac{r_s}{L} \frac{dL}{dt}$  seen by a typical freely-falling observer through the redshift factor  $r_s/L$ ). In the final step we have used  $m_{det} = \epsilon^{-1}L^{-1}$  and we approximated  $\frac{dL}{dt} \sim L/t$ , where t is the timescale of the experiment. Since  $L \gg \ell_p$ , the result will be small whenever  $t \gtrsim \sqrt{r_s^3/\ell_p}$ .

</details>

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

<details>
<summary>Bulk Locality and Quantum Error Correction in AdS/CFT</summary>

# Bulk Locality and Quantum Error Correction in AdS/CFT

### Ahmed Almheiri,<sup>a</sup> Xi Dong,<sup>a</sup> Daniel Harlow<sup>b</sup>

<sup>a</sup>Stanford Institute for Theoretical Physics, Department of Physics, Stanford University, Stanford, CA 94305, USA

Abstract: We point out a connection between the emergence of bulk locality in AdS/CFT and the theory of quantum error correction. Bulk notions such as Bogoliubov transformations, location in the radial direction, and the holographic entropy bound all have natural CFT interpretations in the language of quantum error correction. We also show that the question of whether bulk operator reconstruction works only in the causal wedge or all the way to the extremal surface is related to the question of whether or not the quantum error correcting code realized by AdS/CFT is also a "quantum secret sharing scheme", and suggest a tensor network calculation that may settle the issue. Interestingly, the version of quantum error correction which is best suited to our analysis is the somewhat nonstandard "operator algebra quantum error correction" of Beny, Kempf, and Kribs. Our proposal gives a precise formulation of the idea of "subregion-subregion" duality in AdS/CFT, and clarifies the limits of its validity.

<sup>b</sup>Princeton Center for Theoretical Science, Princeton University, Princeton NJ 08540 USA E-mail: [almheiri@stanford.edu](mailto:almheiri@stanford.edu), [xidong@stanford.edu](mailto:xidong@stanford.edu), [dharlow@princeton.edu](mailto:dharlow@princeton.edu)

### <span id="page-2-0"></span>1 Introduction

Almost twenty years after its initial formulation, the AdS/CFT correspondence remains our best-understood example of a precise theory of quantum gravity. It has shed light on many deep puzzles in quantum gravity, and has also been of practical use in studying the dynamics of strongly interacting quantum field theories. One aspect that remains mysterious, however, is the emergence of approximate bulk locality. Locality near the boundary is straightforward. In the "extrapolate" version of the AdS/CFT dictionary we have a simple relation [\[1,](#page-36-0) [2\]](#page-36-1)

<span id="page-2-3"></span>
$$\lim_{r \to \infty} r^{\Delta} \phi(r, x) = \mathcal{O}(x) \tag{1.1}$$

between limiting values of a bulk field φ and a conformal field theory operator O; this dictionary manifestly respects locality in the x directions since the CFT does. The radial direction, however, is more subtle. One way to see this is to observe that naively a local operator in the center of the bulk should commute with every local operator at the boundary on a fixed time slice containing that bulk operator. This is not consistent, however, with a standard property of quantum field theory; any operator that commutes with all local operators at a fixed time must be proportional to the identity.[1](#page-2-1) Bulk locality thus cannot be respected within the CFT at the level of the algebra of operators; we'd then like to know in what sense it is respected.[2](#page-2-2)

The basic idea of this paper is that bulk locality is a statement about certain subspaces of states in the CFT. That these subspaces can be large is a consequence of the large-N properties of the CFT, but the large degree of non-local entanglement in finite energy states of the CFT also plays an essential role. Our strategy will be to gradually back away from the r → ∞ limit in equation [\(1.1\)](#page-2-3) and study how the the CFT representations of bulk operators spread in spatial support as we do so. On the

<span id="page-2-1"></span><sup>1</sup> In lattice theories with scalars and fermions coupled to abelian gauge fields this property is essentially obvious in the Hamiltonian formulation. Showing it for non-abelian gauge fields on the lattice requires more work. In either case the idea is to show that the algebra generated by local operators on a time-slice acts irreducibly on the Hilbert space; the statement then follows from Schur's lemma. In the continuum this idea is called the "time-slice axiom" [\[3,](#page-36-2) [4\]](#page-36-3); for recent rigorous discussions, see, e.g., [\[5,](#page-36-4) [6\]](#page-37-0). There are actually topological theories where the time-slice axiom is false, for example in Chern-Simons theory quantized on a topologically nontrivial Riemann surface, but we don't expect this loophole to be relevant for CFTs with ordinary gravity duals.

<span id="page-2-2"></span><sup>2</sup>One subtlety in this argument is that to put the operator at a definite bulk point in a diffeomorphism-invariant way we need to include "gravitational dressing" that will allow the operator to not necessarily commute with local operators at the boundary at subleading order in 1/N. We will discuss this more in section [5,](#page-23-0) where we will see that this level of non-locality is not enough to avoid a contradiction between the bulk and boundary algebras.

bulk side the tool we will mostly use is the AdS-Rindler reconstruction of bulk fields introduced in [\[7\]](#page-37-1) and refined in [\[8\]](#page-37-2). We will observe that this construction has several paradoxical features, which we will illuminate by recasting it on the CFT side in the language of quantum error correcting codes [\[9,](#page-37-3) [10\]](#page-37-4). This language gives a new, more general perspective on the issue of bulk reconstruction, and we believe that it is the natural framework for understanding the idea of "subregion-subregion" duality [\[11–](#page-37-5)[14\]](#page-37-6). In particular, the radial direction in the bulk is realized in the CFT as a measure of how well CFT representations of bulk quantum information are protected from local erasures. The holographic principle also naturally arises in the guise of the general statement that there is an upper bound on how much quantum information a given code can protect from erasures.

One point that will appear in this analysis is that truncated subalgebras of bulk observables are of interest; these were also advocated in [\[15\]](#page-37-7) in the context of describing the black hole interior. Aspects of our proposal are inspired by their construction, but here we do not discuss black hole interiors and we are not violating quantum mechanics [\[16\]](#page-37-8). A connection between black holes and quantum error correction was also made in [\[17\]](#page-37-9), which is essentially an earlier version of the proposal of [\[15\]](#page-37-7), but again the context was different and our work here should be uncontroversial by comparison.

Before proceeding, let us establish a few conventions used throughout this paper. We will frequently discuss subspaces and tensor factors of the Hilbert space. When we say that an operator acts within a subspace we also mean that the same is true for its hermitian conjugate. If the Hilbert space is a tensor product H<sup>E</sup> ⊗ H<sup>E</sup> , for any operator O<sup>E</sup> that acts on E we may trivially form an operator I<sup>E</sup> ⊗O<sup>E</sup> that acts on the entire Hilbert space. We will often drop the identity operator I<sup>E</sup> and write it simply as O<sup>E</sup> . The reader should also keep in mind that the CFT regions A and A that we will talk about in section [4](#page-16-0) unfortunately correspond to E and E respectively in the language of section [3.](#page-8-0)

### <span id="page-3-0"></span>2 Bulk reconstruction and an AdS-Rindler puzzle

### <span id="page-3-1"></span>2.1 Global AdS reconstruction

We begin by briefly recalling the standard CFT construction of local bulk fields in AdS [\[1,](#page-36-0) [7,](#page-37-1) [18\]](#page-37-10). We will first work in global coordinates, where the metric asymptotically has the form

<span id="page-3-2"></span>
$$ds^{2} \sim -(r^{2}+1)dt^{2} + \frac{dr^{2}}{r^{2}+1} + r^{2}d\Omega_{d-1}^{2}.$$
 (2.1)

The CFT dual to this system lives on S <sup>d</sup>−<sup>1</sup> × R, with the R being the time direction. The Hilbert space of states is the set of field configurations on S d−1 . The idea is then to perturbatively construct operators in the CFT which obey the bulk equations of motion, with the boundary conditions set by the dictionary [\(1.1\)](#page-2-3). For simplicity we will assume that all bulk interactions are suppressed by inverse powers of a quantity N, which will also set the AdS radius in Planck units. At leading order in 1/N, this procedure results in a straightforward prescription for the CFT representation of a bulk field φ(x); we simply have

<span id="page-4-1"></span>
$$\phi(x) = \int_{\mathbb{S}^{d-1} \times \mathbb{R}} dY K(x; Y) \mathcal{O}(Y), \qquad (2.2)$$

where the integral is over the conformal boundary and K(x, Y ) is a so-called "smearing function". The smearing function obeys the bulk wave equation in its x index, and leads to [\(1.1\)](#page-2-3) as we take x to the boundary. It can be chosen to only have support when x and Y are spacelike separated, which we illustrate for AdS<sup>3</sup> in the left diagram of figure [1;](#page-5-1) the point x is represented by a boundary integral over the green region only. In the case of empty AdS, where we take [\(2.1\)](#page-3-2) to hold everywhere, explicit representations of the smearing function can be found in [\[7,](#page-37-1) [18\]](#page-37-10).[3](#page-4-0) 1/N corrections can be systematically included [\[18,](#page-37-10) [19\]](#page-37-11), although we won't really need to discuss them here. At higher orders in this perturbation theory we will need to confront the problem of defining local operators in a diffeomorphism invariant theory, but we postpone discussion of this until section [5.](#page-23-0)

It is not obvious from the definition that the operators [\(2.2\)](#page-4-1) have the expected commutators in the bulk; this has been checked perturbatively within low point correlation functions in [\[19\]](#page-37-11), but must eventually break down in states with enough excitations to avoid a contradiction with the argument in our introduction. We will argue below that, within the subspace of states that are "perturbatively close" to the vacuum, it breaks down only at the level of non-perturbatively small corrections.

Note that once we have a representation of the form [\(2.2\)](#page-4-1), we can use the CFT Hamiltonian to re-express all operators on the right hand side in terms of Heisenberg picture fields on a single Cauchy surface in the CFT, denoted as Σ in figure [1.](#page-5-1) This representation is quite nontrivial, in general it involves severely nonlocal and multitrace operators. It also has the property that if we take x to be near the boundary but not quite on it, the single-time CFT representation of φ(x) still involves operators

<span id="page-4-0"></span><sup>3</sup>One subtlety here is that for more general asymptotically AdS backgrounds, we are not aware of a rigorous argument for the existence of K, even in the distributional sense that we will see we need to allow in the following subsection. One obvious problem is that x could be behind a horizon, but even for geometries with no horizons the only precise argument for the existence of K (or more precisely the existence of the "spacelike Green's function" it is built from) requires spherical symmetry [\[18\]](#page-37-10). We are not aware of any obstruction to its existence, but it would nonetheless be very interesting to see a detailed analysis of this somewhat nonstandard problem in partial differential equations.

![](_page_5_Picture_0.jpeg)

Figure 1. AdS<sup>3</sup> reconstruction globally, and in an AdS-Rindler wedge.

<span id="page-5-1"></span>with support on all of Σ. We might hope to find a representation whose boundary support shrinks as the operator approaches the boundary, and indeed the AdS-Rindler representation does exactly this, as we will now explain.

### <span id="page-5-0"></span>2.2 AdS-Rindler reconstruction

Consider a subregion A of a CFT Cauchy surface Σ. The boundary domain of dependence of A, denoted D[A], is defined as the set of points on the boundary with the property that every inextendible causal curve, meaning a curve whose tangent vector is never spacelike and which is not part of a larger curve with this property, that passes through it must also intersect A. This is illustrated for the boundary of AdS<sup>3</sup> in the right diagram of figure [1,](#page-5-1) where A is the boundary interval lying between the two vertical hash marks and D[A] is shaded green. For any boundary region R, its bulk causal future/past J <sup>±</sup>[R] is defined as the set of bulk points which can be reached by bulk causal curves evolving from/to the region R. The causal wedge of a CFT subregion A [\[14\]](#page-37-6) (for earlier related definitions see [\[20\]](#page-37-12)) is defined as

$$W_C[A] \equiv \mathcal{J}^+[D[A]] \cap \mathcal{J}^-[D[A]]. \tag{2.3}$$

In the right diagram of figure [1,](#page-5-1) WC[A] roughly lies between the dashed lines and D[A]. The bulk codimension-two surface χ<sup>A</sup> in the figure is the "rim" of the wedge and is commonly referred to as the causal surface of A [\[14\]](#page-37-6); more precisely it is defined as the part of the intersection of the boundaries of J <sup>±</sup>[D[A]] that does not also intersect the

![](_page_6_Picture_0.jpeg)

Figure 2. Coordinates for the AdS-Rindler wedge for AdS3, shaded in blue. In this case we have −∞ < x < ∞.

<span id="page-6-0"></span>conformal boundary at infinity. χ<sup>A</sup> can also be described as the intersection of the past and future horizons of D[A].

A simple example of these definitions is where we take the geometry to be pure AdSd+1, Σ = S d−1 to be the t = 0 slice of the boundary, and A to be one hemisphere of Σ. In this case WC[A] becomes what is usually referred to as the AdS-Rindler wedge. A natural set of bulk coordinates on the AdS-Rindler wedge gives a metric with the form

$$ds^{2} = -(\rho^{2} - 1)d\tau^{2} + \frac{d\rho^{2}}{\rho^{2} - 1} + \rho^{2} \left( dx^{2} + \sinh^{2} x d\Omega_{d-2}^{2} \right), \tag{2.4}$$

where the coordinate ranges are ρ > 1, x ≥ 0, −∞ < τ < ∞ and the geometry in parentheses is just the d − 1 dimensional hyperbolic disc. The causal surface χ<sup>A</sup> is given by the limit ρ → 1 at fixed τ , and A itself is given by ρ → ∞ and τ = 0. We illustrate this for AdS<sup>3</sup> in figure [2.](#page-6-0) By acting on this example with bulk isometries (or equivalently boundary conformal transformations), we can arrive at the causal wedge for any round disc in Σ. The case of AdS<sup>3</sup> is especially simple; all connected boundary regions are intervals and thus can be produced in this way.

The point then is that the construction of CFT representations of bulk fields in the previous subsection can also be implemented purely within the causal wedge [\[7\]](#page-37-1).[4](#page-6-1) At leading order in 1/N, the claim is that for any φ(x) with x ∈ WC[A], we can again represent φ(x) via the expression [\(2.2\)](#page-4-1), but with the Y integral now taken only over D[A]. This is illustrated for AdS<sup>3</sup> in the right diagram in figure [1,](#page-5-1) where we have

<span id="page-6-1"></span><sup>4</sup>This has been worked out explicitly only at leading order in 1/N for the case of the AdS-Rindler wedge, the 1/N corrections should basically be treatable using the same methods as for the global construction and the existence for more general geometries has the same caveats as before.

<span id="page-7-1"></span>![](_page_7_Picture_0.jpeg)

Figure 3. Three examples of AdS3-Rindler reconstruction. Shown here is a top-down view of a bulk Cauchy slice whose boundary is Σ. On the left, the blue shaded region is the intersection of this Cauchy slice with the causal wedge for a CFT region A that is the complement of a small boundary interval around the boundary point Y . In the center we have the point x lying in the causal wedge of two different CFT regions, A and B. A borders the blue and green regions, while B borders the green and yellow regions. The black circle segments are χA, χB, and χA∩B. On the right we have split Σ into a union of three disjoint intervals, A, B, and C, and the circle segments are χA, χB, and χC.

allowed for a conformal transformation that changes the size of the boundary interval A. We review more details of this construction in appendix [A;](#page-31-0) the only major subtlety is that the smearing function K no longer exists as a function and must be understood as a distribution for integration against CFT expectation values [\[8\]](#page-37-2) (see also [\[21\]](#page-37-13) for some related discussion).

Thus we see that the AdS-Rindler construction of φ indeed has the property that if x is close to the boundary, only a small boundary region A localized near x is needed to be able to reconstruct φ in D(A). Moreover, by making use of the CFT evolution we can again rewrite the expression [\(2.2\)](#page-4-1) entirely in terms of nonlocal Heisenberg operators acting at t = 0, but now they will act only on A.

### <span id="page-7-0"></span>2.3 Overlapping wedges

The AdS-Rindler construction of bulk fields we have just described has the somewhat counter-intuitive property that the same bulk field operator φ(x) lies in multiple causal wedges, and thus can be represented as an operator on distinct regions A, B, . . . in Σ. One consequence of this is shown in the left diagram of figure [3;](#page-7-1) for any bulk field operator φ(x) and any CFT local operator O(Y ) such that x and Y are spacelike separated, we can choose a causal wedge WC[A] such that O(Y ) lies in the complement of A in Σ. By CFT locality O(Y ) then must exactly commute with our representation of φ(x) in that wedge. This is coming dangerously close to contradicting the theorem mentioned in the introduction, that is that no nontrivial operator in the CFT can commute with all local CFT operators on Σ.

To avoid this contradiction it must be the case that the representations of φ(x) in different wedges are not really all the same operator on the CFT Hilbert space. We can see this in another way by considering the setup of the center diagram in figure [3,](#page-7-1) where we have two overlapping wedges WC[A] and WC[B] that both contain the point x but x is not contained in WC[A ∩ B]. For a CFT operator defined with support only on A to really be equal to a CFT operator defined with support only on B, it must be that the operator really only has support on A∩B. But given that we have chosen x to lie outside of WC[A ∩ B], we do not expect the operator to have such a representation. In fact in this example the operator has a representation on the complement of A ∩ B, and we will see in section [\(3.5\)](#page-15-0) that when this is so a version of the no-cloning theorem of quantum mechanics forbids an accurate representation of the operator on A ∩ B.

We can see the non-equivalence of the operators even more clearly by considering a third example, shown in the right diagram in figure [3.](#page-7-1) Now a bulk field at the point x lies outside of the causal wedge for any one of the regions, but it can be reconstructed in A∪B, B ∪C, or A∪C. The mutual intersection of these regions is just three points, and if we consider another set of three regions slightly rotated from these we can come up with a set of six possible reconstructions whose mutual intersection is genuinely empty. There is simply no possible way that they can all be equal as operators. For future reference we will refer to the three operators as φAB(x), φBC(x), and φAC(x).

We thus need to decide how we are to reconcile these operator inequivalences with the fact that in the bulk theory it seems that the operators are equivalent. There will clearly be some CFT states where they act quite differently, and we would like to understand the physics of the subset of states where their action is equivalent. This problem can be nicely understood in the language of quantum error correction, to which we now turn.

### <span id="page-8-0"></span>3 Correcting quantum erasures

Say Alice wants to send Bob a quantum state of k qubits in the mail, but she is worried that some of the qubits might get lost on the way. Quantum error correction is a procedure that allows her to embed this state into n > k qubits in such a way that even if some qubits are lost, Bob can still recover it. In this section we review some basic facts about this, beginning with an example.[5](#page-8-1)

<span id="page-8-1"></span><sup>5</sup>Our presentation of quantum error correction is somewhat nonstandard, since we are interested only correcting for the erasure of a known set of qubits. This allows us to omit many of the usual

#### <span id="page-9-0"></span>3.1 A simple example of erasure correction

The simplest example of quantum error correction actually involves three-state "qutrits" instead of two-state qubits, and it uses three qutrits to send a single-qutrit message [25]. Say Alice wishes to send the state

$$|\psi\rangle = \sum_{i=0}^{2} a_i |i\rangle. \tag{3.1}$$

The idea is to instead send the state

<span id="page-9-1"></span>
$$|\widetilde{\psi}\rangle = \sum_{i=0}^{2} a_i |\widetilde{i}\rangle,$$
 (3.2)

where

$$|\widetilde{0}\rangle = \frac{1}{\sqrt{3}} (|000\rangle + |111\rangle + |222\rangle)$$

$$|\widetilde{1}\rangle = \frac{1}{\sqrt{3}} (|012\rangle + |120\rangle + |201\rangle)$$

$$|\widetilde{2}\rangle = \frac{1}{\sqrt{3}} (|021\rangle + |102\rangle + |210\rangle).$$
(3.3)

This protocol has two remarkable properties. First of all for any state  $|\widetilde{\psi}\rangle$ , the reduced density matrix on any one of the qutrits is maximally mixed. Thus no single qutrit can be used to acquire any information about the state. Secondly, from any two of the qutrits Bob can reconstruct the state. For example, say he has access to only the first two qutrits. He can make use of the fact that there exists a unitary transformation  $U_{12}$  acting only on the first two qutrits that implements

<span id="page-9-2"></span>
$$(U_{12} \otimes I_3) |\widetilde{i}\rangle = |i\rangle \otimes \frac{1}{\sqrt{3}} (|00\rangle + |11\rangle + |22\rangle). \tag{3.4}$$

Acting with this on the encoded message, we see that Bob can recover the state  $|\psi\rangle$ :

$$(U_{12} \otimes I_3) |\widetilde{\psi}\rangle = |\psi\rangle \otimes \frac{1}{\sqrt{3}} (|00\rangle + |11\rangle + |22\rangle). \tag{3.5}$$

Explicitly  $U_{12}$  is a permutation that acts as

$$\begin{array}{c|cccc} |00\rangle \rightarrow |00\rangle & |11\rangle \rightarrow |01\rangle & |22\rangle \rightarrow |02\rangle \\ |01\rangle \rightarrow |12\rangle & |12\rangle \rightarrow |10\rangle & |20\rangle \rightarrow |11\rangle & . \\ |02\rangle \rightarrow |21\rangle & |10\rangle \rightarrow |22\rangle & |21\rangle \rightarrow |20\rangle \end{array} \tag{3.6}$$

topics, such as quantum channels, ancilla, check operators, etc. Standard reviews of this more general formalism are [22, 23]; for a concise description of the basic ideas see section 4 of [24].

Clearly by the symmetry of [\(3.3\)](#page-9-1) a similar construction is also possible if Bob has access only to the second and third, or first and third qutrits. Thus Bob can correct for the loss of any one of the qutrits; in quantum information terminology one describes this as a quantum error correcting code that can protect against arbitrary single qutrit erasures. The subspace spanned by [\(3.3\)](#page-9-1) is called the code subspace; the entanglement of the states in the code subspace is essential for the functioning of the protocol.

In our discussion of reconstruction in the previous section we were interested in the action of operators rather than the recovery of states, and we can rephrase the error correction protocol in this language. Indeed, say that O is an operator that acts on the single qutrit Hilbert space as[6](#page-10-0)

$$O|i\rangle = \sum_{j} (O)_{ji}|j\rangle. \tag{3.7}$$

For any such <sup>O</sup> we can always find a (non-unique) three-qutrit operator <sup>O</sup><sup>e</sup> which implements the same transformation on the code subspace:

$$\widetilde{O}|\widetilde{i}\rangle = \sum_{j} (O)_{ji}|\widetilde{j}\rangle.$$
 (3.8)

In quantum computing language, operators like <sup>O</sup><sup>e</sup> that act directly on the code subspace in this manner are called logical operations, since they are the types of things that we want to implement when performing a fault-tolerant quantum computation.

For a general code subspace, <sup>O</sup><sup>e</sup> would need to have nontrivial support on all three qutrits. For the code subspace in question, however, is straightforward to see that the operator

$$O_{12} \equiv U_{12}^{\dagger} O U_{12},$$
 (3.9)

where O is taken to act on the first qutrit, acts as

$$O_{12}|\widetilde{i}\rangle = \sum_{j} (O)_{ji}|\widetilde{j}\rangle.$$
 (3.10)

<sup>O</sup><sup>12</sup> is thus an <sup>O</sup><sup>e</sup> that has support only on the first two qutrits. Since we can also analogously construct O<sup>23</sup> or O13, we have realized a situation where operators with nontrivial support on different qutrits have the same action on the code subspace. This should be reminiscent of our discussion of overlapping wedges in the previous section; we will make the connection more explicit soon but first we need to discuss some general properties of quantum erasure correction.

<span id="page-10-0"></span><sup>6</sup>Here we write (O)ij to indicate the matrix elements of the operator O on the code subspace, with the parentheses there to distinguish this from the operators O12, O23, etc to be defined momentarily.

Before moving on, however, we want to introduce a notational simplification. So far we have been careful to distinguish the single-qutrit operator O from its three-qutrit representations <sup>O</sup>e. We find it convenient, however, to from now on abuse notation by instead thinking of "O" as an abstract logical operation and using it both cases; which operator we mean should always be clear from the context. So for example we can write

$$O_{12}|\widetilde{i}\rangle = O|\widetilde{i}\rangle.$$
 (3.11)

### <span id="page-11-0"></span>3.2 General erasure correction

We now describe a natural generalization of the protocol of the previous subsection. For familiarity we will describe it using qubits, although none of the results rely on this. Say that we want to protect a k-qubit code subspace of an n-qubit system against the loss of some collection of E of l of the qubits. We define the code subspace H<sup>C</sup> as the span of the orthonormal states

<span id="page-11-1"></span>
$$|\tilde{i}\rangle = U_{enc}|i_1 \dots i_k 0_{k+1} \dots 0_n\rangle,$$
 (3.12)

where Uenc is called the encoding unitary transformation. There is a necessary and sufficient condition for the correctability of the erasure of E [\[26\]](#page-38-3). Say that we adjoin to our system a reference system R of k additional qubits. We then consider the state

$$|\phi\rangle = 2^{-k/2} \sum_{i} |i\rangle_R |\widetilde{i}\rangle_{\overline{E}E},$$
 (3.13)

where E denotes the set of n − l qubits that aren't erased. The code [\(3.12\)](#page-11-1) can correct for the erasure of E if and only if we have

<span id="page-11-3"></span>
$$\rho_{RE}[\phi] = \rho_R[\phi] \otimes \rho_E[\phi]. \tag{3.14}$$

Here ρR[φ], ρE[φ], etc are the reduced density matrices obtained from |φi by partial trace. This is equivalent to saying that the mutual information IRE = S<sup>R</sup> + S<sup>E</sup> − SRE vanishes, where S<sup>X</sup> is the Von Neumman entropy, S<sup>X</sup> ≡ −trρ<sup>X</sup> log ρX. Let us first see that this ensures we can correct the erasure. The Schmidt decomposition[7](#page-11-2) of

$$|\psi\rangle = \sum_{i} C_{i} |i\rangle_{A} |i\rangle_{B}. \tag{3.15}$$

For a derivation and some more details see for example [\[27\]](#page-38-4).

<span id="page-11-2"></span><sup>7</sup>The Schmidt decomposition of a pure state |ψi in a bipartite Hilbert space H<sup>A</sup> ⊗ H<sup>B</sup> is the observation that for any |ψi ∈ H<sup>A</sup> ⊗ H<sup>B</sup> there exists a set of orthonormal states |ii<sup>A</sup> in HA, a set of orthonormal states |ii<sup>B</sup> in HB, and a set of non-negative real numbers C<sup>i</sup> such that

|φi, together with [\(3.14\)](#page-11-3), ensures us that there exists a basis |ei for E and a set of orthonormal states |ψi,ei<sup>E</sup> in E such that

$$|\phi\rangle = 2^{-k/2} \sum_{i,e} C_e |i\rangle_R |e\rangle_E |\psi_{i,e}\rangle_{\overline{E}},$$
 (3.16)

where C<sup>e</sup> are some non-negative coefficients obeying P <sup>e</sup> C 2 <sup>e</sup> = 1. In other words there exists a unitary transformation U<sup>E</sup> acting only on E such that

$$U_{\overline{E}}|\phi\rangle = 2^{-k/2} \sum_{i} |i\rangle_{R}|i\rangle_{\overline{E}_{1}} \otimes |\chi\rangle_{\overline{E}_{2}E}, \tag{3.17}$$

where we have denoted the first k qubits of E as E<sup>1</sup> and the rest as E2. |χi is some state that is independent of i. This then implies that we must have

$$U_{\overline{E}}|\widetilde{i}\rangle_{\overline{E}E} = |i\rangle_{\overline{E}_1} \otimes |\chi\rangle_{\overline{E}_2E}, \tag{3.18}$$

which is the analogue of [\(3.4\)](#page-9-2) above and demonstrates that we can use U<sup>E</sup> to correct the erasure. If we do not have [\(3.14\)](#page-11-3), then there is nonzero correlation between R and E, so we can learn about the state of R by doing measurements on E. Since any successful protocol must not care about what happens to the qubits we lose, this prevents us from being able to correct the erasure. We can thus loosely rephrase [\(3.14\)](#page-11-3) as the statement that the erasure of E is correctable if and only if no information about i can be obtained from E. This is related to the no-cloning theorem; if we were able to get the same quantum information about the encoded state <sup>|</sup>ψe<sup>i</sup> from both <sup>E</sup> and <sup>E</sup> then we would have built a machine for cloning that information.

There is a useful reformulation of the condition [\(3.14\)](#page-11-3) as the statement that for any operator X<sup>E</sup> acting on E, we must have [\[28\]](#page-38-5)

<span id="page-12-1"></span>
$$\langle \widetilde{i}|X_E|\widetilde{j}\rangle = \delta_{ij}C(X).$$
 (3.19)

In other words we must have the projection of X<sup>E</sup> onto the code subspace be proportional to the identity. One immediate consequence of this is that in any state <sup>|</sup>ψe<sup>i</sup> in the code subspace, the correlation function of X<sup>E</sup> with any operator O that acts within the code subspace[8](#page-12-0) must vanish:

<span id="page-12-2"></span>
$$\langle \widetilde{\psi} | OX_E | \widetilde{\psi} \rangle - \langle \widetilde{\psi} | O | \widetilde{\psi} \rangle \langle \widetilde{\psi} | X_E | \widetilde{\psi} \rangle = 0.$$
 (3.20)

This is another manifestation of the idea that E has no access to the encoded information.

<span id="page-12-0"></span><sup>8</sup>Throughout this paper, when we say that an operator acts within a subspace we mean that the same is true for its hermitian conjugate as well.

As in the previous subsection, we can use  $U_{\overline{E}}$  to realize any operator O acting within the code subspace as an operator  $O_{\overline{E}}$  that acts just on  $\overline{E}$ . Indeed we have both

<span id="page-13-0"></span>
$$O_{\overline{E}}|\widetilde{\psi}\rangle = O|\widetilde{\psi}\rangle$$

$$O_{\overline{E}}^{\dagger}|\widetilde{\psi}\rangle = O^{\dagger}|\widetilde{\psi}\rangle. \tag{3.21}$$

In fact the converse of this statement also holds; if any operator on the code subspace can be realized as an operator on  $\overline{E}$  as in (3.21), then the code is able to correct for the loss of E. The proof is simple. Say that the code were not correctable; then as just discussed there must exist an operator  $X_E$  on E where (3.19) does not hold. By Schur's lemma, there must then exist an operator O on the code subspace that does not commute with  $X_E$  on  $\mathcal{H}_C$ , that is with  $\langle i|[O,X_E]|\tilde{j}\rangle \neq 0$  for some i and j. But this operator O can't be realized on  $\mathcal{H}_C$  by an operator  $O_{\overline{E}}$  that acts only on  $\overline{E}$ , since any such operator by definition would commute with  $X_E$ .

We now turn to the question of when we should expect (3.14) (or equivalently (3.19) or (3.21)) to hold. In situations where we would like our code to be able to correct against a wide variety of erasures, we expect that  $\rho_E[\phi]$  will have full rank. In that case, in order to be able to have the orthonormal set of states  $|\psi_{i,e}\rangle$  we need the dimensionality of  $\overline{E}$  to be at least as large as dimensionality of RE. In other words we need

<span id="page-13-2"></span>
$$n \ge 2l + k. \tag{3.22}$$

This condition is quite intuitive; wanting to send a larger message or correct larger erasures requires more qubits.

In fact for large systems (3.22) is typically not only necessary but sufficient. Say we take  $|\phi\rangle$  to be a random state of  $2^{k+n}$  qubits in the Haar measure. By Page's theorem [29]<sup>10</sup>, the density matrix of R will be exponentially close to maximally mixed provided that  $n-k \gg 1$ , so by the Schmidt decomposition this is equivalent to choosing a random k-qubit code subspace of n qubits. The condition (3.14) will hold if RE is maximally mixed, which again by Page's theorem should be true provided that  $n-2l-k \gg 1$ . Thus, not only is (3.22) necessary for a typical code to correct for the loss of a particular set E of l qubits, it is basically sufficient for the code to correct for the loss of any set of l qubits.

<span id="page-13-1"></span><sup>&</sup>lt;sup>9</sup>This excludes trivial cases like  $U_{enc} = 1$  with E chosen to be the last n - k qubits. This code is completely defeated by erasing any of the first k qubits, and if we knew that erasures would only affect the last n - k qubits why would we include those qubits at all?

<span id="page-13-3"></span><sup>&</sup>lt;sup>10</sup>Page's theorem is the statement that a random state of a bipartite Hilbert space  $\mathcal{H}_A \otimes \mathcal{H}_B$  will be maximally mixed on the smaller factor up to corrections that go like the ratio of dimension of the smaller factor to the dimension of the larger factor. For more details see e.g. [27].

### <span id="page-14-0"></span>3.3 Quantum secret sharing

The three-qutrit example of section [3.1](#page-9-0) has the interesting property that every collection of qutrits either can perfectly reconstruct the state |ψi or has no information about it at all. General error correcting codes do not have this property, since sometimes we can have erasures which can be "partially corrected", but it is interesting to think about the codes that do. Say that we have a Hilbert space that is a tensor product of p factors of not necessarily equal size, which in this context we will refer to as shares. A code subspace C of this Hilbert space is called a Quantum Secret Sharing Scheme if it has the property that every collection of shares either can distinguish perfectly different elements of C, meaning given access to it we can correct for the erasure of its complement, or it cannot distinguish different elements at all [\[25\]](#page-38-0). Collections which enable erasure correction are called authorized and collections which do not are called unauthorized. We will see a possible application of quantum secret sharing to AdS/CFT in section [4.3](#page-21-0) below.

### <span id="page-14-1"></span>3.4 Approximate erasure correction

So far we have discussed exact quantum error correction, but in AdS/CFT we only expect the emergence of the bulk to be approximate. It will thus be important for us to get a sense of how badly we might want to allow our three necessary and sufficient conditions for correctability to be violated. The simplest way to relax the condition [\(3.14\)](#page-11-3) is to require only [\[30\]](#page-38-7)

<span id="page-14-3"></span>
$$||\rho_{RE} - \rho_R \otimes \rho_E||_1 \ll 1. \tag{3.23}$$

Here ||M||<sup>1</sup> <sup>≡</sup> tr<sup>√</sup> M†M is the trace norm of M; two density matrices whose difference has trace norm are "operationally close" in the sense that the probability distributions they predict for arbitrary measurements differ by at most . This essentially says that typical states in the code subspace can be reconstructed to accuracy ; following [\[30\]](#page-38-7) we take this to be the definition of approximate error correction. We would like to relate this to our second condition for correctability, [\(3.19\)](#page-12-1), but we need a convenient way to quantify the violation of [\(3.19\)](#page-12-1). One good choice is to use correlation functions of the form

<span id="page-14-2"></span>
$$C_{\phi}(O, X_E) \equiv \langle \phi | O_R^T X_E | \phi \rangle - \langle \phi | O_R^T | \phi \rangle \langle \phi | X_E | \phi \rangle = \operatorname{tr}_{RE} \left[ O_R^T X_E \left( \rho_{RE} - \rho_R \otimes \rho_E \right) \right]. \tag{3.24}$$

Here O<sup>T</sup> <sup>R</sup> denotes taking the transpose of an operator O on the code subspace and acting with it on the reference system R; by construction acting on the state |φi this is equivalent to acting with O on EE. Cφ(O, XE) is essentially the average of the correlation function (3.20) over all  $|\widetilde{\psi}\rangle \in \mathcal{H}_{\mathcal{C}}$ ; they become equal in the limit of a large code subspace.<sup>11</sup> From the right hand side of (3.24) it is not difficult to show that [31]

<span id="page-15-2"></span>
$$||\rho_{RE} - \rho_R \otimes \rho_E||_1 \ge \left| \frac{C_\phi(O, X_E)}{\lambda_O \lambda_X} \right|,$$
 (3.25)

where  $\lambda_O$  and  $\lambda_X$  are the largest eigenvalues of their respective operators. Thus we see that, as one might expect from our discussion around (3.19), the presence of nonzero correlation between O and  $X_E$  puts a limit on how accurately we can correct for the erasure of E. This inequality will be very useful in our discussion of AdS/CFT, since after all computing correlation functions in the bulk theory is much easier than computing the trace norm directly.

#### <span id="page-15-0"></span>3.5 Operator algebra quantum error correction

In our discussion of AdS/CFT we will soon see that the presence of bulk correlation puts nontrivial restrictions on the correctability of errors via the inequality (3.25). There is, however, a generalized version of quantum error correction, called operator algebra quantum error correction, that is able to accommodate such correlation by requiring that our third necessary and sufficient condition (3.21) apply only to a *subalgebra* of operators on the code subspace [32, 33]. This requirement is greatly illuminated by the following theorem:

**Theorem.** Say that we have a code subspace  $\mathcal{H}_{\mathcal{C}} \subset \mathcal{H}_{E} \otimes \mathcal{H}_{\overline{E}}$  and an operator O that, together with its hermitian conjugate, acts within the code subspace. In other words we have

$$O|\widetilde{i}\rangle = \sum_{j} O_{ji}|\widetilde{j}\rangle,$$

$$O^{\dagger}|\widetilde{i}\rangle = \sum_{j} O_{ij}^{*}|\widetilde{j}\rangle.$$
(3.26)

Then there exists an operator  $O_{\overline{E}}$  acting just on  $\overline{E}$  that obeys

$$O_{\overline{E}}|\widetilde{\psi}\rangle = O|\widetilde{\psi}\rangle,$$

$$O_{\overline{E}}^{\dagger}|\widetilde{\psi}\rangle = O^{\dagger}|\widetilde{\psi}\rangle$$
(3.27)

for any  $|\widetilde{\psi}\rangle \in \mathcal{H}_{\mathcal{C}}$  if and only if O commutes with the projection of any operator  $X_E$  onto the code subspace, where  $X_E$  acts on E. In other words

<span id="page-15-3"></span>
$$\langle \tilde{i}|[O, X_E]|\tilde{j}\rangle = 0 \qquad \forall i, j.$$
 (3.28)

<span id="page-15-1"></span><sup>&</sup>lt;sup>11</sup>This average can be computed using the unitary integration technology described for example in appendix D of [27]; the corrections vanish like powers of  $2^{-k}$ , which will be exponentially small in N for our AdS-CFT construction.

We give a proof of this theorem in appendix [B.](#page-34-0) It is clear that the set of O's that satisfy the assumptions of the theorem form a unital \*-subalgebra A of the operators on the code subspace, meaning they include the identity and are closed under addition, multiplication, and hermitian conjugation. If we take A to be the entire algebra of operators on H<sup>C</sup> then we recover our condition [\(3.21\)](#page-13-0). Notice, however, that when A is a proper subalgebra we cannot use our previous argument to derive the condition [\(3.19\)](#page-12-1) from [\(3.21\)](#page-13-0), since the O that we constructed that doesn't have an O<sup>E</sup> will not be in A. This gives a loophole that simultaneously allows correlation between O and X<sup>E</sup> and the existence of O<sup>E</sup> .

For example in the two qubit system, consider a code subspace spanned by <sup>√</sup> 1 2 (|00i + |11i) and <sup>√</sup> 1 2 (|01i + |10i). The operator X that exchanges these two states can be realized just on the first qubit as the X<sup>1</sup> operator that flips it, even though in either state this operator is perfectly correlated with the X<sup>2</sup> operator that flips the second qubit. This is possible because the Z operator on the code subspace, for which the first state is a +1 eigenstate and the second state is a −1 eigenstate, cannot be realized as an operator just on the first qubit; this code corrects only the subalgebra generated by 1 and X.

This example has the perhaps surprising property that the encoded 1 and X operators can be realized on either of the two qubits, which seems in tension with our discussion of the no-cloning theorem above [\(3.19\)](#page-12-1). This is an artifact, however, of the fact that this subalgebra is abelian, and is thus in some sense classical. It is easy to prove that as long as the subalgebra is non-abelian, if it can be represented on E then it cannot be represented on E; the proof follows immediately by contradiction if we look at the commutator of two non-commuting elements of the algebra, but with one represented on E and one represented on E. We used this "algebraic no-cloning theorem" above in our discussion of figure [3.](#page-7-1)

### <span id="page-16-0"></span>4 AdS/CFT as quantum error correction

We now return to our discussion of bulk reconstruction. Consider again the right diagram in figure [3.](#page-7-1) We argued using the AdS-Rindler reconstruction that the operator in the center can be represented either as an operator φAB with support on A ∪ B, an operator φBC with support on B ∪ C, or an operator φAC with support on A ∪ C. By now it should be obvious that this is directly analogous to the situation with O12, O23, and O<sup>13</sup> in the three qutrit example, or more generally the existence of the operator O<sup>E</sup> . The main proposal of this paper is that this is more than an analogy, it is actually how AdS/CFT is reproducing the bulk! In other words we can think of local bulk operators as logical operations on an encoded subspace, which becomes better and better protected against localized boundary errors as we move the operators inwards in

![](_page_17_Picture_0.jpeg)

Figure 4. Correcting for erasures in AdS/CFT. Bulk quantum information at point in the center is protected in the CFT against the erasure of the boundary of any one of the green regions, but bulk information at the point near the boundary is completely lost by an erasure of the boundary of the red region.

<span id="page-17-2"></span>the radial direction.[12](#page-17-1) We illustrate this in figure [4.](#page-17-2) In the remainder of the paper we will spell out this idea in more detail, giving the bulk versions of most of the statements of the previous section.

### <span id="page-17-0"></span>4.1 Defining code subspaces

We begin by defining a set of candidate code subspaces for AdS/CFT. Our proposal is that we should pick some finite set of local bulk operators φi(x), realized in the CFT via the global representation of section [2.1.](#page-3-1) We then define a code subspace H<sup>C</sup> as the linear span of states of the form

<span id="page-17-3"></span>
$$|\Omega\rangle, \phi_i(x)|\Omega\rangle, \phi_i(x_1)\phi_j(x_2)|\Omega\rangle, \dots,$$
 (4.1)

where we take the range of i, the number of φi(x)'s we act with, and the number of points x where the operators can be located to be bounded by some fixed finite number. Here |Ωi is the ground state of the system; we could also do a similar construction around other sufficiently "semiclassical" states, but for rigor we will stick to |Ωi since, as mentioned in section [2.1,](#page-3-1) the existence of appropriate smearing functions has not been completely established in the general case. We postpone to section [5](#page-23-0) the question of how large H<sup>C</sup> can be. It is essential that our definition of the code subspace will be different for different choices of the operators φi(x); the set of erasures that are

<span id="page-17-1"></span><sup>12</sup>One detail here is that in defining the "center" of AdS we are implicitly choosing a conformal frame in the CFT; otherwise AdS is a homogeneous space and no point is special. This is also implicit in our notion of "small" and "large" erasures in the CFT.

correctable will depend on this choice, and we can learn about the way that the bulk theory is realized in the CFT by studying this dependence. For example, in figure 4 we see that moving the operators closer to the boundary makes our code subspace less protected against small erasures. The CFT is not just one error-correcting code, it is many at once!

We would like to think of the operators  $\phi_i(x)$  as logical operations on this code subspace, but this does not quite work since by construction acting repeatedly with  $\phi_i(x)$  will eventually take us out of  $\mathcal{H}_{\mathcal{C}}$ . To get a set of operators that really act within  $\mathcal{H}_{\mathcal{C}}$  we can include projection operators onto  $\mathcal{H}_{\mathcal{C}}$  on both sides of  $\phi_i$ ; these will be irrelevant except in studying high-point correlation functions, so we will not carry them around explicitly here.<sup>13</sup> Now consider a decomposition of the boundary Cauchy surface  $\Sigma$  into A and  $\overline{A}$ . If our code subspace  $\mathcal{H}_{\mathcal{C}}$  can protect against the erasure of  $\overline{A}$ , then by our condition (3.21) it must be that we can find a representation of any operator on  $\mathcal{H}_{\mathcal{C}}$  with support only in A. In fact, this is what the AdS-Rindler reconstruction we reviewed in section 2.2 provides us; any causal wedge  $\mathcal{W}_{\mathcal{C}}[A]$  which contains the locations of the  $\phi_i(x)$ 's used in defining  $\mathcal{H}_{\mathcal{C}}$  will allow a set of operators  $\phi_{A,i}(x)$  with support only on A and whose action on  $\mathcal{H}_{\mathcal{C}}$  is the same as that of  $\phi_i(x)$ . We now see that in the CFT this is a statement about being able to correct for the erasure of  $\overline{A}$ .

To avoid confusion, we stress that, just because we do not include some  $\phi(x)$  in defining the code subspace, we do not mean to imply that its AdS-Rindler reconstruction does not work on that subspace. We could easily consider a slightly larger subspace where we include it, and we could then interpret its AdS-Rindler reconstruction as arising from quantum error correction. The only fundamental limitation on the AdS-Rindler reconstruction comes from the backreaction considerations we discuss in section 5 below.

#### <span id="page-18-0"></span>4.2 Bulk correlation and smearing

It is illuminating to understand in more detail to what extent the AdS-Rindler reconstruction is consistent with our three equivalent conditions (3.14), (3.19), (3.21) for quantum erasure correction. We clearly do not expect them to hold exactly, but we might hope for them to hold in the approximate sense of (3.23). As we explained in section 3.4, a good diagnostic for approximate quantum erasure correction is that the

<span id="page-18-1"></span>has a normalized overlap with the vacuum of order  $\frac{\langle \Omega | \phi^m | \Omega \rangle}{\sqrt{\langle \Omega | \phi^{2m} | \Omega \rangle}} \sim 2^{-m}$ . The scaling with m follows from counting Wick contractions at leading order in 1/N. If we choose our code subspace such that the maximum power of each  $\phi$  grows like some power of N, then for states on which the projection onto  $\mathcal{H}_{\mathcal{C}}$  is nontrivial this overlap will be exponentially small in N. It then will be okay to conjugate the  $\phi$ 's by these projectors without ruining their low-point correlation functions.

![](_page_19_Picture_0.jpeg)

Figure 5. Potentially troublesome bulk correlation. Here φ(x) is an operator that acts within the code subspace HC, and which we thus expect can be represented as an operator on A. φ(y) we similarly expect to reconstructed on A, but there is nonvanishing correlation between them in the ground state |Ωi. Using inequality [\(3.25\)](#page-15-2), this correlation puts a lower bound on the accuracy with which we can view AdS/CFT as quantum error correction in the conventional sense of section [3.2.](#page-11-0)

<span id="page-19-1"></span>correlation functions between operators acting within the code subspace and operators acting on the set to be erased are small enough that the inequality [\(3.25\)](#page-15-2) does not preclude [\(3.23\)](#page-14-3) from holding.[14](#page-19-0)

In fact it is a basic property of bulk physics that there is correlation between fields in WC[A] and fields in WC[A], as we indicate in figure [5.](#page-19-1) In deciding whether or not this bulk correlation interferes with our interpretation of AdS-Rindler reconstruction as quantum error correction, we need to properly take into account the operator eigenvalues in the denominator of [\(3.25\)](#page-15-2). Formally these are infinite in a continuum quantum field theory, but every quantum field theorist knows that field operators are not really well-defined until they are integrated against smooth test functions with support over some region of nonzero measure, which we will take to have linear size s. For simplicity we will take the bulk fields to be massless scalars and take their separation to be small compared to the AdS radius, in which case we have

<span id="page-19-2"></span>
$$\frac{\langle \Omega | \phi(x) \phi(y) | \Omega \rangle}{\lambda_{\phi}^2} \sim \left( \frac{\epsilon_s}{d(x, y)} \right)^{d-1}. \tag{4.2}$$

Here d is the spacetime dimension of the boundary theory and d(x, y) is the geodesic distance between x and y. This formula also holds in other states we produce by acting on |Ωi with smeared operators near x, and thus on average in the code subspace HC.

<span id="page-19-0"></span><sup>14</sup>We thank Juan Maldacena for pointing out the relevance of [\(3.25\)](#page-15-2) in this situation.

We thus see that the right hand side of [\(3.25\)](#page-15-2) will be small in our case provided that the operators φi(x) used in constructing H<sup>C</sup> are smeared over a distance which is small compared to their distance to the causal surface χ<sup>A</sup> of the wedge WC[A] in which we are trying to reconstruct them.

This observation does much to justify our interpretation of AdS-Rindler reconstruction as quantum error correction, but it is somewhat unsatisfactory in the sense that the AdS-Rindler reconstruction still seems to work in the situation where we smear the operators over a distance that is comparable to their distance to the bifurcate Rindler horizon χA, even though the bulk correlation is then too large to be ignored. Indeed we interpret this as saying that the conventional quantum error correction of section [3.2](#page-11-0) does not fully capture the mechanism by which AdS/CFT realizes bulk locality. The operator algebra quantum error correction introduced in section [3.5,](#page-15-0) however, provides precisely the generalization we need to fix this. Consider for example an operator S which acts on φ(x)|Ωi as Sφ(x)|Ωi = |Ωi, and which annihilates any state orthogonal to φ(x)|Ωi. This is an operator that acts within the code subspace, but its commutator with an operator φ(y) in WC[A] obeys

$$\langle \Omega | [S, \phi(y)] | \Omega \rangle = \langle \Omega | \phi(x) \phi(y) | \Omega \rangle \neq 0. \tag{4.3}$$

Thus S clearly cannot have a representation as an operator just on A. Fortunately there is no reason to expect this operator to have an AdS-Rindler reconstruction, but the broader lesson is that we should really expect AdS-Rindler reconstruction to in general produce only a subalgebra of the operators on HC. We saw in section [3.5](#page-15-0) that the condition a subalgebra must obey for this to be possible is that the subalgebra must commute with the projection onto H<sup>C</sup> of any operator on A. In fact this is precisely the condition that we expect to be true for local operators in WC[A] (and their sums and products), which by bulk causality should commute with operators in WC[A].[15](#page-20-0) That this commutator vanishes with the projections onto H<sup>C</sup> of all CFT operators in A is not something we can prove directly, but AdS-Rindler reconstruction requires it.

A second reason to prefer operator algebra quantum error correction is that even when the right hand side of [\(4.2\)](#page-19-2) is small, it will at most be suppressed by some fixed power of 1/N. This is because we should not smear the operators over distances shorter than the Planck length. Since we in principle would like a version of AdS-Rindler reconstruction that works to all orders in 1/N, it would be unsatisfying if our error correction interpretation failed at some finite order because of bulk correlation.

<span id="page-20-0"></span><sup>15</sup>This statement is rendered somewhat more subtle by the need for gravitational dressing to localize operators in a gravitational theory; we will see in section [5](#page-23-0) that this commutator continues to vanish at higher orders in 1/N, as required by operator algebra quantum error correction.

![](_page_21_Picture_0.jpeg)

Figure 6. A reconstruction phase transition? As we increase the region A, the extremalarea codimension two surface of smallest area whose boundary is ∂A, shown as the solid lines, changes discontinuously. Does this mean that we can now reconstruct the point in the center as an operator on A?

<span id="page-21-1"></span>We can now state our final proposal: the AdS-Rindler reconstruction of local bulk operators in [\[7,](#page-37-1) [8\]](#page-37-2) is dual in the CFT to the operator algebra quantum error correction of [\[32,](#page-38-9) [33\]](#page-38-10). An erasure of a region A is correctable if the φi(x)'s used in defining the code subspace all lie within the causal wedge WC[A]. In cases where the operators we are interested in are well-localized away from the causal surface χ<sup>A</sup> of WC[A], the situation is well-approximated by conventional quantum error correction. Either way, the further the φi(x)'s are from the asymptotic boundary, the better they are protected from CFT erasures.

It is worth emphasizing that in the case where a bulk operator is of order an AdS radius distance from WC[A], our approximate equivalence between conventional and operator algebra quantum error correction requires sub-AdS scale bulk locality. This is a special property of those CFTs that have local holographic duals, which we have here reformulated in the language of quantum information theory.

### <span id="page-21-0"></span>4.3 Disconnected regions and quantum secret sharing

So far we have only discussed the erasure of connected regions of the boundary. More general erasures are also interesting. Consider for example the AdS<sup>3</sup> situation depicted in figure [6.](#page-21-1) Here we consider a region A which is the union of two disjoint intervals; in other words we have erased two disjoint intervals. Can we choose a code subspace where we can realize the bulk operator in the center as an operator acting on A or A? If the AdS-Rindler reconstruction is the last word on bulk reconstruction [\[11\]](#page-37-5), then the answer is clearly no; this point lies neither in WC[A] nor in WC[A]. This is possible within the context of quantum error correction, but only if both A and A can access partial information about the code subspace. For example, say that A had no information whatsoever about which state of the code subspace we are in. Then by definition [\(3.14\)](#page-11-3) would hold, so we could recover the information from A. We are not, however, able to determine whether or not such partial information is really present.

In fact there have been recent conjectures in the literature that this operator can still be reconstructed in A as long as A is bigger than A; more generally, the claim is that one can do reconstruction throughout the entanglement wedge, which is defined as the bulk domain of dependence of any bulk spacelike surface whose boundary is the union of A and the codimension two extremal-area surface of minimal area whose boundary is ∂A [\[12,](#page-37-15) [34–](#page-38-11)[36\]](#page-38-12).[16](#page-22-1) In the figure, the intersection of the entanglement wedge with a bulk Cauchy surface is shaded blue; the minimal area condition causes a discontinuous change as we increase the size of A. Is this conjecture compatible with our proposal? Indeed it is; we saw below equation [\(3.22\)](#page-13-2) that in a generic code subspace any A which is greater than half of the system can correct for the erasure of its complement A. [17](#page-22-2) The sharp jump in correctability as A surpasses A in size is consistent with our analysis around [\(3.22\)](#page-13-2), where from Page's theorem we expect that the density matrix of A together with the reference system will approach being maximally mixed exponentially fast once we cross the transition.

In section [3.3](#page-14-0) we saw that a division of the CFT into a union of shares with the property that any collection of the shares has either complete information or no information about the encoded state is called a quantum secret sharing scheme; we now see that in the situation of figure [6](#page-21-1) we will be able to reconstruct the operator in the center if and only if our boundary division into four regions gives a quantum secret sharing scheme.

### <span id="page-22-0"></span>4.4 MERA as an error correcting code?

One shortcoming of our work so far is that, although we have laid out a plausible CFT interpretation of AdS-Rindler reconstruction as quantum error correction, we have ultimately relied on the bulk in deriving this reconstruction. This boils down to

<span id="page-22-1"></span><sup>16</sup>One argument that this must be the case is as follows: the extension by [\[37\]](#page-38-13) of the Ryu-Takayanagi proposal [\[38\]](#page-38-14) to next to leading order in 1/N claims that bulk entanglement entropy in the entanglement wedge contributes to the Von Neumann entropy SA. So for example if we have a spin sitting in the entanglement wedge of A that is entangled with another spin in W<sup>C</sup> [A], then the spin in the entanglement wedge contributes log 2 to SA. It is hard to see how this could be the case if we could not project the spin onto a definite state by doing some measurement on A, but the operator we measure would then be a representation on A of a logical operator on the spin.

<span id="page-22-2"></span><sup>17</sup>More carefully it has to be greater than half by an amount that depends on the size of the code subspace, which we can think of as being parametrically smaller than the full Hilbert space. We explore this in more detail in the following section.

the assumption that there exist operators in the CFT that obey the bulk equations of motion and algebra on a subspace. We then use this assumption to perform the Bogoliubov transformation that relates the global and the Rindler reconstructions. This assumption is quite plausible, and essentially follows from the assumed large-N structure of the CFT [\[39\]](#page-38-15), but it would still be nice if we could explicitly demonstrate the structure of the quantum error correcting code in the CFT. In particular, in section [4.2](#page-18-0) we had to use bulk causality to argue that the necessary and sufficient condition [\(3.28\)](#page-15-3) for operator algebra quantum error correction held, and we were not able to check it explicitly for all possible CFT operators on A. Similarly we were unable to determine whether or not the central point could be reconstructed in the two-interval A of the previous subsection.

A promising starting point for addressing these issues is the MERA tensor network construction of a discrete version of AdS/CFT [\[40–](#page-39-0)[42\]](#page-39-1). It seems possible that in that fairly controlled setting one could rigorously confirm the quantum error correction structure we have motivated in this paper. Moreover, one could attempt to determine explicitly whether or not the example of the previous subsection allows reconstruction of the operator in the center; this could be done by using the global construction to make a code subspace, entangling this code subspace with a reference system R to prepare a state |φi, and then seeing whether there is mutual information between R and A. The state |φi would still be prepared by a tensor network, with tensors acting both on the CFT and/or the reference system. This calculation would go a long way towards settling the "causal wedge vs. entanglement wedge" debate of bulk reconstruction.[18](#page-23-1) We will not attempt this calculation here, but the typicality argument leading to [\(3.22\)](#page-13-2) favors the entanglement wedge; we will say more about this in section [5.3.](#page-29-0)

### <span id="page-23-0"></span>5 Backreaction and holography

We now turn to the question of how large we can make the code subspace HC. Each φi(x) that we act with raises the energy of the state, so doing so repeatedly will eventually lead to backreaction becoming important. When this happens it is clear that the approximation of perturbation theory around a fixed background geometry will break down. In this section we argue that this is related to a basic property of error correct-

<span id="page-23-1"></span><sup>18</sup>One challenge in doing this is that the region of discrepancy between the entanglement wedge and the causal wedge in that example has a size which is only of order the AdS radius, and it is not so clear how to represent sub-AdS scale physics using MERA. One strategy for getting around this is to consider the limit of A being a union of a large number of smaller disjoint intervals of equal size; this allows a parametrically large separation between the causal wedge and the entanglement wedge.

![](_page_24_Picture_0.jpeg)

Figure 7. Locating bulk points using spatial geodesics. By construction we can only define points that lie in the bulk domain of dependence of any bulk Cauchy surface with boundary Σ.

<span id="page-24-1"></span>ing codes: the larger the code subspace, the fewer correctable errors. For erasures we quantified this in equation [\(3.22\)](#page-13-2) above.

### <span id="page-24-0"></span>5.1 Defining local operators

Once we allow nontrivial backreaction, it is no longer possible to ignore the issue of how we define bulk local operators in a diffeomorphism-invariant way. Following [\[43,](#page-39-2) [44\]](#page-39-3), we do this by choosing a cutoff surface at large but finite radius, with induced metric S <sup>d</sup>−<sup>1</sup> × R, and then specifying bulk points by sending in spacelike geodesics from the t = 0 slice of this cutoff surface that start out orthogonal to the S <sup>d</sup>−<sup>1</sup> directions. We then take the limit as the cutoff surface approaches the boundary. Points are labeled by a location on S d−1 , a renormalized proper distance along the geodesic, and an angle in the radial/temporal plane. This is illustrated in figure [7.](#page-24-1) These geodesics can be thought of as the "gravitational dressing" of the bulk operator, analogous to the Wilson line one would use to connect a charged operator to the boundary to make it gauge-invariant in electrodynamics.

As in the electromagnetic case, the operators defined in this way will have nonlocal commutators due to their nontrivial Dirac brackets. The study of these commutators was initiated in [\[18\]](#page-37-10), and more recently elaborated in [\[44\]](#page-39-3).[19](#page-24-2) A full analysis has not yet been completed, however, and one point that has not yet been addressed is essential

<span id="page-24-2"></span><sup>19</sup>A subtlety here is that they send their geodesics from arbitrary boundary times, but take them to be orthogonal to the boundary in the temporal direction as well as the S <sup>d</sup>−<sup>1</sup> directions. These operators agree with ours at t = 0, which is where we will study them, but as a matter of principle we have not made their choice because we want to restrict to Schrodinger-picture operators acting on a

![](_page_25_Picture_0.jpeg)

Figure 8. Two dressed bulk local operators. If the operator on the right is to be reconstructed on the boundary of the green wedge, and the operator on the left to be reconstructed on the boundary of the blue wedge, then they must be commuting operators. By taking one of these operators to the boundary, we conclude that any dressed bulk local operator must commute with all boundary local operators except possibly those at the endpoint of its geodesic.

<span id="page-25-1"></span>for the consistency of the AdS/Rindler reconstruction at higher orders in 1/N: to all orders in 1/N perturbation theory around a fixed background, two dressed bulk operators with the property that all points on their dressing geodesics are mutually spacelike separated in that background must commute.[20](#page-25-0) The reason this must be the case is illustrated in figure [8.](#page-25-1)

We can use this observation to verify that bulk non-locality from the gravitational dressing of operators does not invalidate some of our previous claims. In the introduction we argued that, because in the bulk theory a local operator in the center of the space commutes with all local operators at the boundary, the bulk operator algebra is inconsistent with the CFT algebra. We can now give a version of this argument that includes the gravitational dressing; from figure [8,](#page-25-1) we see that we should modify the previous statement to "commutes with all local operators at the boundary except at one point". Were this to hold as an operator equation in the CFT, it would now not imply that the operator in the center must be trivial in the CFT, but it would imply that this operator can be nontrivial at t = 0 only at the point where the dressing

fixed time slice at the boundary. As explained in more detail in section 4.2 of [\[18\]](#page-37-10), this is the natural way to define the fixed-time Hilbert space in the bulk, since it makes it clear that expectation values are independent of possible sources on the boundary at later times.

<span id="page-25-0"></span><sup>20</sup>More carefully, we should hold the boundary endpoints of the geodesics fixed as we take N → ∞ for this statement to hold. One of us (DH) has checked this statement directly in bulk canonical gravity in the setup of [\[44\]](#page-39-3), by computing the Dirac brackets and seeing that they are local in the ˆx directions to any finite order in perturbation theory, but we postpone discussion of this to a future publication.

![](_page_26_Picture_0.jpeg)

Figure 9. An algebraic paradox: a bulk operator at φ(x) is dressed by a geodesic ending at X. The bulk algebra suggests this operator commutes with all local CFT operators on the Cauchy surface Σ except those at X, and is thus a local operator there. However, we can find a boundary point Y which is both spacelike separated from X and causally separated from x; the bulk would then require local operators there which don't commute with φ(x), while the CFT would require them all to commute.

<span id="page-26-1"></span>geodesic ends.[21](#page-26-0) This statement, however, is not consistent with bulk causality, as we illustrate in figure [9.](#page-26-1) So we thus indeed find that the bulk operator algebra cannot be realized in the CFT at the level of operator equations. As already explained, the resolution is that the bulk algebra holds in the CFT only acting on a code subspace of states.

Similarly we can now revisit our claim that bulk operators in WC[A] perturbatively commute with bulk operators in WC[A], which was a necessary condition for our interpretation of the AdS-Rindler construction as operator algebra quantum error correction. But this is exactly what the argument of figure [8](#page-25-1) accomplishes; as long as the gravitational dressing of an operator at x ∈ WC[A] also lies entirely in WC[A], meaning that the spatial geodesic connecting x to the boundary also lies in WC[A], then it will only have non-local commutators with operators that are also located in WC[A]; any operator whose localizing geodesic is entirely in one wedge will still perturbatively commute with any operator whose localizing geodesic is entirely in the complementary wedge.

<span id="page-26-0"></span><sup>21</sup>As before this statement is straightforwardly true for scalars, fermions, and/or abelian gauge fields on a lattice, and we expect it to hold also for non-abelian lattice gauge fields. In the continuum it follows from a combination of the time-slice axiom and "Haag duality", which says that if we split a time-slice into two regions the commutant of the set of local operators in the domain of dependence of one of the regions is the set of local operators in the domain of dependence of the other region. In the case of gauge theories one has to be careful since Haag duality does not quite hold, since there can be a nontrivial center of the algebra for a region, but the center is always localized near the boundary [\[45\]](#page-39-4) and shouldn't disrupt this argument.

In this subsection, to connect to the formalism of [\[44\]](#page-39-3) we studied only operators attached to geodesics that start out orthogonal to the boundary time direction at t = 0. It would be interesting to do the analogue of their analysis at arbitrary temporal-radial angle; this amounts to working with boundary conditions that approach the "open-FRW" slicing of AdS

$$ds^{2} = -dt^{2} + \sin^{2} t \left( d\chi^{2} + \sinh^{2} \chi d\Omega_{d-1}^{2} \right)$$
 (5.1)

as χ → ∞. As explained in [\[18\]](#page-37-10), this would be a natural bulk construction of Schrodinger picture gauge-invariant operators on the fixed-boundary-time Hilbert space.

### <span id="page-27-0"></span>5.2 Shrinking of the causal wedge

We now return to the question of how backreaction affects causal wedge reconstruction. Our basic proposal is that adding energy in the bulk causes the causal wedge of a fixed boundary region A to recede towards the boundary, giving it less access to bulk operators defined at fixed renormalized geodesic distance (for some related discussion see [\[14,](#page-37-6) [34,](#page-38-11) [35,](#page-38-16) [46,](#page-39-5) [47\]](#page-39-6)).

Consider for example the AdS-Schwarzschild geometry in d + 1 dimensions.

$$ds^{2} = -f(r)dt^{2} + \frac{dr^{2}}{f(r)} + r^{2}d\Omega_{d-1}^{2},$$
(5.2)

with

$$f(r) \equiv r^2 + 1 - \frac{\alpha}{r^{d-2}}.$$
 (5.3)

α is proportional to the ADM mass of this geometry. Now consider a boundary disc A of angular size θ; its causal wedge reaches a radius rθ(α) in the bulk defined implicitly by

$$\frac{\theta}{2} = \int_{r_{\theta}(\alpha)}^{\infty} \frac{dr'}{f(r')}.$$
 (5.4)

The proper distance of this radius to a cutoff surface at r = r<sup>c</sup> is

$$\int_{r_{\theta}(\alpha)}^{r_c} \frac{dr'}{\sqrt{f(r')}} = \int_{r_{\theta}(\alpha)}^{r_c} dr' \left(\frac{1}{\sqrt{f(r')}} - \frac{1}{r'}\right) + \log \frac{r_c}{r_{\theta}(\alpha)},\tag{5.5}$$

so we can subtract log r<sup>c</sup> to define a renormalized proper distance

$$d_{\theta}(\alpha) \equiv \int_{r_{\theta}(\alpha)}^{\infty} dr' \left( \frac{1}{\sqrt{f(r')}} - \frac{1}{r'} \right) - \log r_{\theta}(\alpha).$$
 (5.6)

We claim that dθ(α) is a decreasing function of α at fixed θ, which by differentiating under the integral sign is equivalent to the claim that

$$\int_{r}^{\infty} \frac{dr'}{r'^{d-2}} \frac{1}{f(r')^{3/2}} \left[ \sqrt{\frac{f(r)}{f(r')}} - \frac{1}{2} \right] > 0$$
 (5.7)

for all α > 0 and for all r > r+(α), where r+(α) is the positive root of f. This can be shown analytically in various limits, and is easily checked numerically in the general case. One can also study the asymptotically-AdS<sup>3</sup> BTZ black hole, where a similar result holds and all integrals can be done analytically. Thus we see that indeed the causal wedge has access to fewer and fewer bulk observables as we increase the mass of the matter in the center. This after all must be the case, since as we keep increasing the mass a point at fixed renormalized geodesic distance from the boundary will eventually go through the horizon.

It is interesting to think about how general this statement is; under what circumstances can the causal wedge move inwards in renormalized geodesic distance as we insert energy? One might guess that the null energy condition should generically prevent this, but to test that we need a more precise conjecture. One first guess is that in any geometry obeying the null energy condition the causal wedge of a fixed boundary region can see at most as far in renormalized geodesic distance as it can in the vacuum. In fact this conjecture is false, we have constructed explicit counterexamples. Indeed a weaker conjecture, where we replace the null energy condition by the dominant energy condition[22](#page-28-0), still has counterexamples. One counterexample is given by a small perturbation of AdS4, with the metric

$$ds^{2} = -f(r)dt^{2} + \frac{dr^{2}}{f(r)} + r^{2}d\Omega_{2}^{2}, \qquad (5.8)$$

where

$$f(r) = r^2 + 1 + \epsilon h(r), \qquad h(r) = -\frac{r^2}{\left(\sqrt{r^2 + 1} + 10\right)^3}.$$
 (5.9)

With a small positive , the causal wedges of certain fixed boundary regions can see farther in renormalized geodesic distance than they can in the vacuum. These boundary regions include spherical regions whose causal wedges probe deep into the bulk geometry.

Although these counterexamples prevent any straightforward "monoticity of causal wedge recession theorem", we expect that the Schwarzschild calculation we have just

<span id="page-28-0"></span><sup>22</sup>With the presence of a negative cosmological constant, we only impose the dominant energy condition on the "matter" part of stress tensor which does not include the cosmological constant. This was used in [\[48\]](#page-39-7) to prove the positive mass theorem in asymptotically anti-de Sitter space.

discussed captures the general tendency. It would be nice to prove a more general theorem verifying this, but we have not succeeded in finding one.

### <span id="page-29-0"></span>5.3 Counting states

The recession of the causal wedge has a nice quantum error correction interpretation; as we allow the code subspace to have more and more excited states, a bulk operator localized at some fixed geodesic distance will eventually no longer lie in the causal wedge of a fixed boundary region. In other words, the code will lose some of its ability to correct erasures; we will need access to more of the boundary to study the same bulk observables. In this subsection we study this a bit more quantitatively, making contact with the general condition [\(3.22\)](#page-13-2) for typical correctability.

To apply [\(3.22\)](#page-13-2) to AdS/CFT, we need to identify CFT analogues of the quantities n, l, and k. n is the total number of qubits used in doing the encoding, and should roughly correspond to the total number of CFT degrees of freedom relevant for reconstructing a particular bulk region of interest. This is somewhat nontrivial; the CFT has an infinite number of degrees of freedom in the UV which are needed to reconstruct bulk operators that are arbitrarily close to the boundary. To deal with this we take our code subspace to only involve states where we act on the vacuum with operators φi(x) that are all localized within a region R at the center of the AdS space that has proper size of order the AdS radius. We will also take them to be smeared over distances that are small compared to their separation from the boundary of R, so that we do not have to worry about the difference between conventional and operator algebra quantum error correction. The global reconstructions [\(2.2\)](#page-4-1) of these operators involve integrals over functions that vary smoothly on the scale of the radius of curvature of the boundary S d−1 , so we can integrate out all CFT degrees of freedom with shorter wavelength.[23](#page-29-1) For concreteness we will consider the case of the N = 4 super Yang-Mills theory in 3 + 1 boundary dimensions with gauge group SU(N), in which case we have

$$n \sim N^2. \tag{5.10}$$

Erasing a disc of angular size θ will then correspond to erasing

$$l = \frac{\theta - \sin \theta}{2\pi} n \tag{5.11}$$

qubits, where this function is just n times the ratio of the area of the disc to the area of the S 3 .

<span id="page-29-1"></span><sup>23</sup>It is not hard to generalize to the case where R is taken to be parametrically larger than the AdS radius, this essentially involves a repeat of the analysis of [\[49\]](#page-39-8).

Let us first consider the case where the code subspace is small, that is when k ∼ 1. From [\(3.22\)](#page-13-2) we then expect that we can correct for the erasure as long as n − 2l 1, or in other words θ < π. But this is exactly what we expect from the AdS-Rindler reconstruction; once θ < π, WC[A] will contain the center of the space. It is interesting to note that the derivation of [\(3.22\)](#page-13-2) applied to an erasure of an arbitrary collection of ` qubits, so this suggests that we should also be able to reconstruct operators in the center on a union of disconnected regions, provided that together they make up more than half of the boundary. With regards to our discussion of section [4.3,](#page-21-0) this gives support to the entanglement wedge over the causal wedge.

We can now start increasing k; nothing interesting will happen until we get k ∼ N<sup>2</sup> , after which the set of erasures we are able to correct will start decreasing. But this is exactly the condition for backreaction to become important in the center; with k ∼ N<sup>2</sup> the entropy of the code subspace is comparable to that of a black hole filling R and thus most states in the code subspace must actually be black holes. So both on the CFT side through equation [\(3.22\)](#page-13-2) and the bulk side via backreaction we arrive at the same conclusion for when correctability should break down. This is a manifestation of the holographic entropy bound of [\[50\]](#page-39-9).

### <span id="page-30-0"></span>6 Conclusion

In this paper we have provided what we consider to be a new understanding of how the holographic principle is realized in AdS/CFT. Bulk effective field theory operators emerge as a set of logical operations on various encoded subspaces, which are protected against local errors in the boundary CFT. The bulk algebra is realized only on these subspaces, and only if we do not try to describe too many operations at once. Asking for more causes the error correction procedure to fail, which in the bulk is manifested by the formation of a black hole.

To some extent we have only recast known facts about the AdS-Rindler reconstruction in a new language, but in our view that construction is quite opaque once the operators in the boundary domain of dependence of A are evolved back to the boundary Cauchy surface Σ at t = 0. Our description in terms of error correction is phrased entirely on this Cauchy surface, and gives what we feel to be a satisfying interpretation of how the AdS-Rindler reconstruction is realized in the CFT that cleanly resolves some of its paradoxical features.

It is of course interesting to ask if there are any implications of this work for the recent controversy on whether or not the interiors of black holes are describable in AdS/CFT; for now we leave this for future study.

Acknowledgments We'd like to thank Vijay Balasubramanian, Will Donnelly, Ethan Dyer, Patrick Hayden, Jennifer Lin, Juan Maldacena, Don Marolf, Eric Mintun, Ian Morrison, Joe Polchinski, Vladimir Rosenhaus, Steve Shenker, Douglas Stanford, Lenny Susskind, Herman Verlinde, Bob Wald, and Aron Wall for useful discussions. XD is supported by the National Science Foundation under grant PHY-0756174, and DH is supported by the Princeton Center for Theoretical Science. We are also grateful to the Aspen Center for Physics for providing a stimulating research environment during the "Emergent Spacetime in String Theory" workshop, where this work was initiated. The center is funded in part by the NSF grant no. PHYS-1066293.

### <span id="page-31-0"></span>A More details on AdS-Rindler reconstruction

In this appendix we review a bit more about the AdS-Rindler reconstruction. The AdS-Rindler wedge has metric

$$ds^{2} = -(\rho^{2} - 1)d\tau^{2} + \frac{d\rho^{2}}{\rho^{2} - 1} + \rho^{2}dH_{d-1}^{2},$$
(A.1)

where dH<sup>2</sup> d−1 is the standard metric on the d − 1 dimensional hyperbolic ball Hd−1. We will refer to coordinates on Hd−<sup>1</sup> collectively as α. A free real scalar field on this background can be expressed in the Heisenberg picture as

<span id="page-31-1"></span>
$$\phi(\rho, \tau, \alpha) = \int_0^\infty \frac{d\omega}{2\pi} \sum_{\lambda} \left( f_{\omega\lambda}(\rho, \tau, \alpha) a_{\omega\lambda} + f_{\omega\lambda}^*(\rho, \tau, \alpha) a_{\omega\lambda}^{\dagger} \right), \tag{A.2}$$

where fωλ(ρ, τ, α) is a solution of the Klein-Gordon equation of the form

$$f_{\omega\lambda}(\rho,\tau,\alpha) = e^{-i\omega\tau} Y_{\lambda}(\alpha) \psi_{\omega\lambda}(\rho).$$
 (A.3)

Here Yλ(α) is an eigenfunction of the Laplacian on Hd−<sup>1</sup> with eigenvalue −λ; the set of λ's is continuous (and positive) so "P λ " should really be understood as shorthand for an integral together with a sum over degeneracies. ψωλ is explicitly given by

$$\psi_{\omega,\lambda}(\rho) = \mathcal{N}_{\omega\lambda}\rho^{-\Delta} \left(1 - \frac{1}{\rho^2}\right)^{-\frac{i\omega}{2}} F\left(-\frac{(d-2)}{4} + \frac{\Delta}{2} - \frac{i\omega}{2} + \frac{1}{2}\sqrt{\frac{(d-2)^2}{4} - \lambda}, -\frac{(d-2)}{4} + \frac{\Delta}{2} - \frac{i\omega}{2} - \frac{1}{2}\sqrt{\frac{(d-2)^2}{4} - \lambda}, \Delta - \frac{d-2}{2}, \frac{1}{\rho^2}\right),$$
(A.4)

with

$$\mathcal{N}_{\omega\lambda} = \frac{1}{\sqrt{2|\omega|}} \frac{\Gamma\left(-\frac{(d-2)}{4} + \frac{\Delta}{2} + \frac{i\omega}{2r_s} + \frac{1}{2}\sqrt{\frac{(d-2)^2}{4} - \frac{\lambda}{r_s^2}}\right) \Gamma\left(-\frac{(d-2)}{4} + \frac{\Delta}{2} + \frac{i\omega}{2r_s} - \frac{1}{2}\sqrt{\frac{(d-2)^2}{4} - \frac{\lambda}{r_s^2}}\right)}{\Gamma\left(\Delta - \frac{d-2}{2}\right) \Gamma\left(\frac{i\omega}{r_s}\right)} \tag{A.5}$$

and

$$\Delta = \frac{d}{2} + \frac{1}{2}\sqrt{d^2 + 4m^2}.$$
 (A.6)

The normalization is chosen to ensure that a and a † have the usual algebra, and implies that for ρ large and negative, ψωλ is of order <sup>√</sup> ω . F is a hypergeometric function that goes to one as ρ → ∞. By comparing to the extrapolate dictionary [\(1.1\)](#page-2-3) we can read off that

$$\mathcal{O}_{\omega\lambda} = \int d\tau d\alpha e^{i\omega\tau} Y_{\lambda}^*(\alpha) \mathcal{O}(\tau, \alpha) = N_{\omega\lambda} a_{\omega\lambda}, \tag{A.7}$$

and substituting back into [\(A.2\)](#page-31-1) and formally exchanging the τα integral with the ωλ integral/sum we arrive at

$$\phi(\rho, \tau, \alpha) = \int d\tau' d\alpha' K(\rho, \tau, \alpha; \tau' \alpha') \mathcal{O}(\tau', \alpha'). \tag{A.8}$$

The "smearing function" K is given by

<span id="page-32-0"></span>
$$K(\rho, \tau, \alpha; \tau'\alpha') = \int_{-\infty}^{\infty} \frac{d\omega}{2\pi} \sum_{\lambda} \frac{1}{N_{\omega\lambda}} f_{\omega\lambda}(\rho, \tau, \alpha) e^{i\omega\tau'} Y_{\lambda}^{*}(\alpha') e^{i\omega\tau'}. \tag{A.9}$$

K can be understood as a kernel for constructing a bulk solution of the KG equation in the AdS-Rindler wedge given arbitrary boundary conditions at spatial infinity as a function of τ and α. It was immediately realized, however, that in fact this expression for K is not well-defined [\[7\]](#page-37-1) (see also [\[51,](#page-39-10) [52\]](#page-39-11)); the reason is that from Stirling's formula it is straightforward to see that at large λ we have

$$|N_{\omega\lambda}|^2 \sim e^{-\pi\sqrt{\lambda}}.\tag{A.10}$$

This is problematic for the convergence of the λ integral in [\(A.9\)](#page-32-0), and using the WKB approximation for Y and ψ at large λ it is not hard to see that indeed the integral does not converge for any choice of bulk and boundary points [\[8,](#page-37-2) [51,](#page-39-10) [52\]](#page-39-11).

In fact, the nonconvergence of K is necessary to avoid the following paradox; say that we have two overlapping Rindler wedges, WC[A] and WC[B], as in figure [10.](#page-33-0) If K existed then since the fωλ solutions are complete it would construct a unique solution of the KG equation in WC[A] with some particular boundary conditions in D[A]. We

![](_page_33_Picture_0.jpeg)

Figure 10. Overlapping Rindler wedges, shown in the boundary. D[A] is in blue, D[B] is in yellow, and their overlap is in green.

<span id="page-33-0"></span>can, however, imagine modifying the spatial boundary conditions at a point x that is in D[B] but not in D[A], such that x is nonetheless causally separated from a point in WC[A]. We then should be able to send a signal to WC[A] without modifying the boundary conditions in D[A], which contradicts the uniqueness of the solution.

In [\[7\]](#page-37-1) it was argued that one should analytically continue in the boundary spatial coordinates to avoid this divergence, but this is a rather unusual thing to do to a quantum field theory and would be rather problematic from the point of view of our analysis in this paper. The issue was recently illuminated considerably in [\[8\]](#page-37-2) (see also [\[21\]](#page-37-13)), where it was argued that as long as we are careful to think of K as a distribution for integration against CFT correlation functions we are allowed to use it without any analytic continuations. The key point of [\[8\]](#page-37-2) was that at least at leading order in 1/N, if we integrate K against appropriate bulk test functions then its singularity structure is such that we are always able to integrate it against CFT expectation values and get a reasonable answer. Intuitively, the reason that this is able to avoid the contradiction of the previous paragraph is that in the CFT O obeys a boundary equation of motion; we are not free to choose it independently at different boundary times. Turning on a source at x will necessarily propagate in the boundary into D[A]∪ D[B], so we will not be able to change the boundary data at x without also changing it in D[A].

The argument of [\[8\]](#page-37-2) does not immediately generalize to higher order corrections in 1/N, but we expect a more detailed analysis will show that it can be improved order by order in 1/N. [24](#page-33-1)

<span id="page-33-1"></span><sup>24</sup>Recently it was argued that AdS/CFT in the AdS-Rindler wedge cannot be understood as a statement about subregions in the global CFT [\[53\]](#page-39-12). It is true that there is a subtlety here in that the cutoffs in the bulk are different in the two cases, but AdS/CFT is really a statement about the continuum CFTs. The discrepancies discussed in [\[53\]](#page-39-12) were localized to "cutoff sized regions" in the CFT, which really means that they are not part of the continuum theory. That CFT expectation

### <span id="page-34-0"></span>B The basic theorem of operator algebra quantum error correction

In this appendix we prove the theorem of section [3.5.](#page-15-0) The proof is original, but the theorem is a special case of the results of [\[32,](#page-38-9) [33\]](#page-38-10).

Proof. Indeed say that we have a code subspace H<sup>C</sup> spanned by an orthonormal basis <sup>|</sup>eiiEE . Moreover say that O is an operator which acts as

$$O|\widetilde{i}\rangle = \sum_{j} O_{ji}|\widetilde{j}\rangle$$

$$O^{\dagger}|\widetilde{i}\rangle = \sum_{j} O_{ij}^{*}|\widetilde{j}\rangle.$$
(B.1)

Finally, say that for any operator X<sup>E</sup> acting on E we have

<span id="page-34-5"></span>
$$\langle \widetilde{i}|[O, X_E]|\widetilde{j}\rangle = 0 \qquad \forall i, j.$$
 (B.2)

We'd then like to show that there exists an operator O<sup>E</sup> acting only on E and obeying

<span id="page-34-3"></span>
$$O_{\overline{E}}|\widetilde{i}\rangle = O|\widetilde{i}\rangle$$

$$O_{\overline{E}}^{\dagger}|\widetilde{i}\rangle = O^{\dagger}|\widetilde{i}\rangle. \tag{B.3}$$

Let us first observe that in general in a bipartite system in a state

$$|\psi\rangle = \sum_{ab} C_{ba} |a\rangle_A |b\rangle_B,$$
 (B.4)

operators O<sup>A</sup> on A and O<sup>B</sup> on B will obey

$$O_B|\psi\rangle = O_A|\psi\rangle$$
 (B.5)

if and only if

<span id="page-34-2"></span>
$$O_B C = C O_A^T. (B.6)$$

Now in the setup of the theorem, let us consider the state[25](#page-34-1)

<span id="page-34-4"></span>
$$|\phi\rangle = \sum_{i} |i\rangle_{R}|\widetilde{i}\rangle_{E\overline{E}}.$$
 (B.7)

values have the right singularity structure to be integrated against K in [\(A.9\)](#page-32-0) is related to the fact that they are computed in states that remain finite energy as we take the continuum limit, and as explained in [\[8\]](#page-37-2) it is forgetting this that leads to trouble.

<span id="page-34-1"></span><sup>25</sup>For convenience we have dropped the overall normalization, it will cancel between the two sides of [\(B.6\)](#page-34-2).

The properties (B.3) will clearly hold if and only if they hold on  $|\phi\rangle$ , ie if

<span id="page-35-0"></span>
$$O_{\overline{E}}|\phi\rangle = O|\phi\rangle$$

$$O_{\overline{E}}^{\dagger}|\phi\rangle = O^{\dagger}|\phi\rangle, \tag{B.8}$$

so this is all we need to show ((B.3) follows from applying projections to R).

Our strategy then is to notice that we can decompose  $RE\overline{E}$  into a bipartite system in two different ways, either as the R system and the  $E\overline{E}$  system or as the E system and the E system. The first decomposition is manifest in (B.7), and since in this case E is just the identity we see that (B.6) holds and we have

$$O_R|\phi\rangle = O|\phi\rangle,$$
 (B.9)

where  $O_R \equiv O^T$  acts just on R. The point then is that we can interpret  $O_R$  as  $O_R \otimes I_E$ , and then see if we can mirror it back onto  $\overline{E}$  using (B.6). If so then we succeed in constructing  $O_{\overline{E}}$ .

To proceed, we can define

$$|\tilde{i}\rangle = \sum_{a.m} C_{am}^{i} |m\rangle_{E} |a\rangle_{\overline{E}},$$
 (B.10)

in which case we have

$$|\phi\rangle = \sum_{i,a,m} C_{am}^{i} |im\rangle_{RE} |a\rangle_{\overline{E}}.$$
 (B.11)

It will be very convenient in what follows to treat C as a rectangular matrix, with a being the first index and im being the second index. For example, we have the reduced density matrices

$$\rho_{\overline{E}} = CC^{\dagger} \equiv g$$

$$\rho_{RE} = C^T C^*. \tag{B.12}$$

Since g is a non-negative hermitian matrix with positive trace, it will be invertible on a subspace of  $\overline{E}$ . Moreover, any state orthogonal to this subspace will also be orthogonal to all of the  $|i\rangle$ 's, so we can just take  $\overline{E}$  to be given by this subspace; g is then invertible. This then means that C has a right inverse  $C^{\dagger}g^{-1}$ .

Now observe that the commutator condition (B.2) implies that

<span id="page-35-1"></span>
$$C^{\dagger}CO = OC^{\dagger}C, \tag{B.13}$$

or equivalently that

$$[O_R \otimes I_E, \rho_{RE}] = 0. \tag{B.14}$$

If C † g <sup>−</sup><sup>1</sup> were a left inverse of C, then [\(B.6\)](#page-34-2) would hold if we define

$$O_{\overline{E}} = COC^{\dagger}g^{-1}, \tag{B.15}$$

which would then give us the first equation in [\(B.8\)](#page-35-0) (remember that O<sup>R</sup> = O<sup>T</sup> ). In fact it is a right inverse, but we can use [\(B.13\)](#page-35-1) to show that [\(B.6\)](#page-34-2) holds nonetheless:[26](#page-36-5)

$$O_{\overline{E}}C = COC^{\dagger}g^{-1}C$$

$$= g^{-1}CC^{\dagger}COC^{\dagger}g^{-1}C$$

$$= g^{-1}COC^{\dagger}CC^{\dagger}g^{-1}C$$

$$= g^{-1}COC^{\dagger}C$$

$$= g^{-1}CC^{\dagger}CO$$

$$= CO.$$
(B.16)

Moreover

$$O_{\overline{E}}^{\dagger} = g^{-1}CO^{\dagger}C^{\dagger}$$

$$= g^{-1}CO^{\dagger}C^{\dagger}CC^{\dagger}g^{-1}$$

$$= CO^{\dagger}C^{\dagger}g^{-1}, \qquad (B.17)$$

where we've used [\(B.13\)](#page-35-1), so the second equation in [\(B.8\)](#page-35-0) is also satisfied. This concludes the proof.

</details>

<details>
<summary>Holographic Quantum Error Correction and the Projected Black Hole Interior</summary>

## Holographic Quantum Error Correction and the Projected Black Hole Interior

### Ahmed Almheiri

Institute for Advanced Study, Princeton, NJ 08540, USA

E-mail: [almheiri@ias.edu](mailto:almheiri@ias.edu)

Abstract: The quantum error correction interpretation of AdS/CFT establishes a sense of fluidity to the bulk/boundary dictionary. We show how this property can be utilized to construct a dictionary for operators behind horizons of pure black holes. We demonstrate this within the context of the SYK model with pure black hole microstates obtained via projecting out a single side of the thermofield double (and perturbed versions thereof). Assuming an erasure subsystem code for the duality between the eternal black hole and the thermofield double, this projection results in a rewiring of the dictionary so as to map the interior operators to the remaining boundary in a determinable way. We find this dictionary to be sensitive to the implemented projection in a manner reminiscent of previous state-dependent constructions of the black hole interior. We also comment on how the fluidity of the dictionary can be used to transfer information between two black holes connected by a wormhole, relating the ideas of entanglement wedge reconstruction and the Hayden-Preskill decoding criterion.

Dedicated to the memory of Joseph Polchinski

## Contents

| 1 | Introduction                                                |                                                                    | 1      |
|---|-------------------------------------------------------------|--------------------------------------------------------------------|--------|
| 2 |                                                             | Pure SYK Black Hole Microstates                                    |        |
|   | 2.1                                                         | KM Construction of Atypical Microstates                            | 5<br>5 |
|   | 2.2                                                         | More Typical Microstates                                           | 8      |
|   | 2.3                                                         | Bulk Particle Gravitational Dressing and Boundary Energy           | 10     |
| 3 | Reconstruction of the Interior via Quantum Error Correction |                                                                    | 13     |
|   | 3.1                                                         | A Puzzle                                                           | 13     |
|   | 3.2                                                         | Toy Model: Projected Random Tensor                                 | 14     |
|   | 3.3                                                         | Projected Quantum Subsystem Correcting Code                        | 21     |
|   | 3.4                                                         | Operator Algebra Quantum Error Correction from Projected Subsystem |        |
|   |                                                             | Codes                                                              | 25     |
|   | 3.5                                                         | Reconstruction as Teleportation or Active Quantum Error Correction | 28     |
| 4 | An Apologia for State Dependence                            |                                                                    | 30     |
|   | 4.1                                                         | Arguments Against State Dependence                                 | 31     |
|   | 4.2                                                         | Relation to State-Dependent Constructions of the Interior          | 32     |
|   | 4.3                                                         | Monogamy of Entanglement and ER=EPR                                | 35     |
|   | 4.4                                                         | Comments on Complexity                                             | 43     |
| 5 | Conclusion                                                  |                                                                    | 45     |
| A | Bulk Particle Gravitational Dressing                        |                                                                    | 47     |
| B | Initial Energy Increase due to an External Coupling         |                                                                    | 52     |

## <span id="page-1-0"></span>1 Introduction

The enigmatic nature of the black hole interior has received much attention in recent years due to the conflict between semi-classical expectations of a smooth horizon and the treatment of black holes as quantum systems with a finite density of states [\[1\]](#page-54-0). These confusions regarding the interior are fundamentally linked to the problem of information loss [\[2\]](#page-54-1), and it is generally believed that a solution of the former might inform us on the latter.

In the context of the AdS/CFT conjecture, where these paradoxes become sharpest, these issues manifest themselves in the difficulty of establishing a dictionary between interior operators and CFT observables [\[3\]](#page-54-2). A plethora of proposals have been put forward which try to ensure a smooth horizon for an infalling observer [\[4–](#page-54-3)[13\]](#page-55-0). A more or less common strategy of these proposals is to begin with some pure state black hole in AdS/CFT, along with the boundary dual of the bulk algebra of operators outside but near the horizon and then try and find a corresponding boundary algebra which mimics the semi-classical algebra of operators behind the black hole horizon. The goal is to find such an algebra with the condition that they ensure a smooth horizon in the considered pure state. However, primarily because these conditions are enforced without prior knowledge of the actual physics of the interior they tend to create ambiguities that run afoul of the standard rules of quantum mechanics [\[14,](#page-55-1) [15\]](#page-55-2).

The new framework for understanding the AdS/CFT dictionary as a Quantum Error Correcting (QEC) code [\[16\]](#page-55-3) has not yet been utilized to address these issues. This framework was proposed as a resolution of an apparent inconsistency between subregion-subregion duality (SSD) and the properties of operator algebras in quantum field theories. In particular, SSD seems to indicate the existence of non-trivial bulk operators which commute with all local operators in the CFT on a given time slice, in contradiction with Schur's lemma (or the "time-slice axiom" in continuum QFT [\[17,](#page-55-4) [18\]](#page-55-5)) that they must then be proportional to the identity. Viewed through the lens of QEC, this conflict is resolved by interpreting the SSD operator identities as subspace statements holding within some code subspace Hcode. For example, one can show that if a logical operator (one that acts within the code subspace) <sup>O</sup><sup>r</sup> satisfies

$$\mathcal{P}_{code} \left[ \widetilde{\mathcal{O}}, X_E \right] \mathcal{P}_{code} = \mathcal{P}_{code} \left[ \widetilde{\mathcal{O}}^{\dagger}, X_E \right] \mathcal{P}_{code} = 0$$
 (1.1)

for all operators X<sup>E</sup> supported on some subsystem E and where Pcode is the projector on the code subspace Hcode, then there exists an operator supported on the complement of <sup>E</sup>, denoted by <sup>E</sup>s, such that

$$\widetilde{\mathcal{O}}\mathcal{P}_{code} = \mathcal{O}_{\bar{E}}\mathcal{P}_{code}, \ \widetilde{\mathcal{O}}^{\dagger}\mathcal{P}_{code} = \mathcal{O}_{\bar{E}}^{\dagger}\mathcal{P}_{code}$$
 (1.2)

This describes a version of a QEC usually called Operator Algebra Quantum Error Correction (OAQEC) [\[19,](#page-55-6) [20\]](#page-55-7). This framework has also aided in understanding two other important aspects of the AdS/CFT duality. The first is the so-called entanglement wedge reconstruction proposal which states that the density matrix of a boundary subregion <sup>E</sup><sup>s</sup> is sufficient to reconstruct the entire entanglement wedge <sup>W</sup>E<sup>s</sup>, the bulk region composed of the union of all spacelike slices bounded by the Ryu-Takayanagi (RT) or Hubeny-Rangamani-Takayanagi (HRT) surface and the boundary subregion itself [\[21–](#page-55-8)[23\]](#page-55-9). The proven statement is that any bulk operator with support within WE<sup>s</sup> has a dual boundary operator supported purely on <sup>E</sup><sup>s</sup> [\[24,](#page-55-10) [25\]](#page-55-11). Furthermore as shown in [\[26\]](#page-55-12), this framework reproduces the RT [\[27\]](#page-56-0) (HRT [\[28\]](#page-56-1)) formula for computing the von Neumann entropy of the region <sup>E</sup>s, along with its associated quantum corrections (bulk EFT entanglement entropy) [\[29\]](#page-56-2),

$$S(\rho_{\bar{E}}) = \frac{A}{4G_N} + S(\rho_{W_{\bar{E}}}).$$
 (1.3)

Given the success of this framework it behooves us to apply it to the context of the black hole interior.

The setting in which we will implement these ideas to the black hole interior will be within the duality between AdS<sup>2</sup> gravity and (a subsector of) the SYK model. The SYK model is a system of N Majorana fermions randomly coupled via the q-local Hamiltonian [\[30,](#page-56-3) [31\]](#page-56-4),

$$H = (-1)^{q/2} \sum_{i_1...i_q}^{N} J_{i_1...i_q} \psi_{i_1}...\psi_{i_q}$$
(1.4)

for q ! N. This system has been found to reproduce many features of gravity in AdS<sup>2</sup> including the pattern of conformal symmetry breaking at low energies [\[32\]](#page-56-5), as well as saturating the bound on chaos typical of commutators in black hole backgrounds [\[33\]](#page-56-6). A particularly interesting and controlled setting in which the reconstruction of the black hole interior can be addressed is the Kourkoulo-Maldacena (KM) construction of pure black hole microstates in the SYK model [\[34\]](#page-56-7) [1](#page-3-0) (see also [\[36\]](#page-56-8) for further constructions). The KM construction is as follows. First one defines a set of states |Bsy which satisfy

$$\left(\psi^{2k-1} - is_k \psi^{2k}\right) |B_s\rangle = 0 \iff S_k |B_s\rangle = s_k |B_s\rangle \tag{1.5}$$

where S<sup>k</sup> " 2iψ<sup>2</sup>k´<sup>1</sup>ψ 2k is a spin operator with eigenvalues s<sup>k</sup> " ˘1. This set of states spans the entire Hilbert space of SYK of dimension 2<sup>N</sup>{<sup>2</sup> . One can then obtain black holes of effective temperature β by evolving these states in Euclidean time

$$|B_s^{\beta}\rangle = e^{-\frac{\beta}{2}H}|B_s\rangle \tag{1.6}$$

which produces an overcomplete basis of black hole microstates of temperature β. Within the low energy analysis, the geometry of these black holes looks like that of an

<span id="page-3-0"></span><sup>1</sup>See also [\[35\]](#page-56-9) for earlier consideration of microstates in an SYK-like model.

eternal black hole except that one boundary is excised by an end-of-the-world brane (EWB) which falls into the black hole. Moreover, these states can be prepared by projecting on the thermofield double (TFD) with the CPT invariant state |Bsy,

$${}_{L}\langle B_{s}|\beta\rangle_{LR} = |B_{s}^{\beta}\rangle_{R} \tag{1.7}$$

where

$$|\beta\rangle_{LR} = \frac{1}{\sqrt{Z_{\beta}}} \sum_{E} e^{-\frac{\beta}{2}H} |E\rangle_{L} |E\rangle_{R}$$
 (1.8)

Therefore the dual of acting with the projection operator is the insertion of the EWB which falls into the eternal black hole.

It is this latter construction that we will use to find the dictionary for the interior of the pure black hole microstates. The idea is to begin with the eternal black hole, with or without anti-time-ordered shockwaves in the interior, viewed as an erasure subsystem code of [\[26\]](#page-55-12) describing the dictionary between the left and right exteriors and their corresponding boundaries, and then to study how this dictionary is modified by the projection on the left boundary. We will study this first using a toy model involving random tensors and then prove some general theorems about when and which interior operators may be reconstructed after such projections. We will ultimately find that a necessary and sufficient condition for the reconstructability of an interior subalgebra is given by

$$\mathcal{P}_{code}[\widetilde{\mathcal{O}}, P_L^s] \mathcal{P}_{code} = \mathcal{P}_{code}[\widetilde{\mathcal{O}}^\dagger, P_L^s] \mathcal{P}_{code} = 0$$
 (1.9)

for an interior operator <sup>O</sup><sup>r</sup> and with left projection <sup>P</sup> s <sup>L</sup> " |BsyLxBs|, and which guarantees the existence of an operator on the right SYK O<sup>s</sup> <sup>R</sup> such that

$$_{L}\langle B_{s}|\widetilde{\mathcal{O}}|\beta\rangle_{LR} = O_{R}^{s} \ _{L}\langle B_{s}|\beta\rangle_{LR} = O_{R}^{s}|B_{s}^{\beta}\rangle_{R}$$
 (1.10)

where the superscript s is there to indicate that this operator depends on the particular projection, P s L . We will discuss the extent of this state-dependence and draw connections to the previous such proposals for the interior. We will discuss how the main reason that this construction avoids the pitfalls of the previous proposals is that the typicality of the state is not the determining factor to the question of the nature of the horizon.

Finally, we will discuss how the fluidity of the dictionary provides a bulk mechanism for transferring information between two boundary SYK systems dual to an eternal black hole by means of evaporating one system into the other. The information will be transferred in the sense that a message deposited into one boundary will end up in the entanglement wedge of the other, and whose state can then be read off using entanglement wedge reconstruction. We will see that the protocol is very similar to the situation of an evaporating black hole that has reached the Page time, where further infalling messages can be decoded from the Hawking radiation using the Hayden-Preskill protocol upon allowing the black hole to release a few more Hawking quanta [\[37\]](#page-56-10).

## <span id="page-5-0"></span>2 Pure SYK Black Hole Microstates

### <span id="page-5-1"></span>2.1 KM Construction of Atypical Microstates

We begin by reviewing the analysis of KM in constructing the states |Bsy dual to pure black hole microstates of effective inverse temperature β with an end-of-the-world brane (EWB) capping off the spacetime deep inside the interior [\[34\]](#page-56-7). This dual bulk description is deduced from the form of the fermion bilinear correlation functions studied in the low energy limit 1 ! βJ ! N and working to leading order in the 1{N expansion.

Consider the diagonal correlation functions xB<sup>β</sup> s |ψ i pt1qψ i pt2q|B<sup>β</sup> s y which can be written in terms of the TFD as

$$\langle \beta | \left[ |B_s \rangle_L \langle B_s | \otimes \psi^i(t_1) \psi^i(t_2) \right] | \beta \rangle$$
 (2.1)

where the fermions are operators belonging to the right SYK. Since the projections |BsyLxBs| for different s form a complete basis, the sum over s just reproduces the thermal expectation value

$$\sum_{s} \langle \beta | \left[ |B_s\rangle_L \langle B_s| \otimes \psi^i(t_1) \psi^i(t_2) \right] |\beta\rangle = \text{Tr} \left[ e^{-\beta H} \psi^i(t_1) \psi^i(t_2) \right]$$
 (2.2)

At large N, the SYK model has an emergent OpNq flavor symmetry, of which a particularly interesting subgroup is the flip group

<span id="page-5-2"></span>
$$\psi^k \to (-1)^{k-1} \psi^k \tag{2.3}$$

In thinking about the doubled system, we denote the flip group as the one which acts identically on both SYKs. This group implements spin flips and therefore relates the different eigenstates |Bsy of the spin operator S<sup>k</sup> " 2iψ<sup>2</sup>k´<sup>1</sup>ψ 2k . The TFD state is invariant under this subgroup. In particular, both the Hamiltonian and the maximally entangled state in the energy basis are individually invariant, which becomes manifest when written in the |Bsy basis:

$$\sum_{s} |B_{s}\rangle_{L}\langle B_{s}| \times \sum_{E} |E\rangle_{L}|E\rangle_{R} = \sum_{s} |B_{s}\rangle_{L}|B_{s}\rangle_{R}$$
(2.4)

![](_page_6_Picture_0.jpeg)

**Figure 1**. The diagram on the left is the standard eternal black hole spacetime dual to the thermofield double state. The projected state on the right is dual to a black hole in a pure state with an end-of-the-world (EWB) brane cutting off the spacetime in the interior. The EWB can be viewed as a UV insertion on the left boundary which then proceeds to fall into the black hole.

<span id="page-6-0"></span>Therefore, we find that the diagonal correlation functions

$$\langle \beta | \left[ |B_s\rangle_L \langle B_s| \otimes \psi^i(t_1)\psi^i(t_2) \right] |\beta\rangle$$
 (2.5)

are invariant under  $|B_s\rangle \rightarrow |B_{s'}\rangle$ , and hence

$$\langle \beta | \Big[ |B_s\rangle_L \langle B_s| \otimes \psi^i(t_1)\psi^i(t_2) \Big] |\beta\rangle = 2^{-N/2} \sum_s \langle \beta | \Big[ |B_s\rangle_L \langle B_s| \otimes \psi^i(t_1)\psi^i(t_2) \Big] |\beta\rangle \qquad (2.6)$$

$$= 2^{-N/2} \text{Tr} \left[ e^{-\beta H} \psi^i(t_1)\psi^i(t_2) \right] \qquad (2.7)$$

Therefore diagonal correlation functions are identical to thermal correlation functions at large N. In the low energy limit this attains the conformal form

$$\langle B_s^{\beta} | \psi^i(t_1) \psi^i(t_2) | B_s^{\beta} \rangle \sim \frac{1}{\left\lceil \frac{\beta J}{\pi} \sinh \frac{\pi(t_1 - t_2)}{\beta} \right\rceil^{2\Delta}}$$
 (2.8)

One deduces from this that the bulk geometry is just  $AdS_2$ . We will see next that the off-diagonal correlators reveal the presence of the EWB.

To compute the off-diagonal correlators, say  $\psi^1(t_1)\psi^2(t_2)$ , one first notes that while this product is not invariant under the spin group, the following operator is invariant

$$S_1 \otimes \psi^1(t_1)\psi^2(t_2)$$
 (2.9)

Moreover, recall that  $S_k|B_s\rangle = s_k|B_s\rangle$ . To compute the off-diagonal correlator, one considers

$$\langle \beta | \Big[ |B_s\rangle_L \langle B_s| \otimes \mathbb{I}_R \Big] \Big[ S_1 \otimes \psi^1(t_1) \psi^2(t_2) \Big] \Big[ |B_{\bar{s}}\rangle_L \langle B_{\bar{s}}| \otimes \mathbb{I}_R \Big] |\beta\rangle$$
 (2.10)

which simplifies to

$$s_1 \langle B_s | \psi^1(t_1) \psi^2(t_2) | B_s \rangle \delta_{s\bar{s}}$$
 (2.11)

From the flip group it is clear that the unsimplified correlation function is invariant under the replacement of  $B_s \to B_{s'}$ . Again, this invariance means we can sum over the spins s and  $\bar{s}$  removing the projectors all together to obtain

$$s_1 \langle B_s | \psi^1(t_1) \psi^2(t_2) | B_s \rangle = 2^{-N/2} 2i \langle \beta | \left[ \psi^1(0) \psi^2(0) \otimes \psi^1(t_1) \psi^2(t_2) \right] | \beta \rangle$$
 (2.12)

$$=2^{-N/2} 2i\langle\beta|\psi^1(0)\otimes\psi^1(t_1)|\beta\rangle\langle\beta|\psi^2(0)\otimes\psi^2(t_2)|\beta\rangle \qquad (2.13)$$

where the last line is the large N result. This is the product of two left-right diagonal fermion correlation functions, each of which at low energy can be deduced from the single sided correlator by taking a single  $t \to t + i\beta/2$ 

$$\langle \beta | \psi^1(0) \otimes \psi^1(t_1) | \beta \rangle \sim \frac{1}{\left[\frac{\beta J}{\pi} \cosh \frac{\pi t_1}{\beta}\right]^{2\Delta}}$$
 (2.14)

This indicates that the state  $|B_s^{\beta}\rangle$  contains the insertion of a high energy operator localized at the single point  $\tau = \beta/2$  on the Euclidean AdS<sub>2</sub> boundary. When continued into Lorentzian time this insertion starts off at t = 0 near the left SYK boundary and falls into the black hole. This is shown in figure 1.

Finally, we review the overcompleteness of this set of states [34]. These black hole microstates are in one to one correspondence with the states  $|B_s\rangle$ , which number at  $2^{N/2}$ , where N is the number of Majorana fermions in the SYK model. Using the techniques above, we have the (not normalized) overlap

$$\langle B_s^{\beta} | B_s^{\beta} \rangle \equiv \langle \beta | \left[ |B_s \rangle_L \langle B_s | \otimes \mathbb{I} \right] | \beta \rangle = 2^{-N/2} Z(\beta)$$
 (2.15)

Therefore, expanding these states in the energy basis we get

$$|B_s^{\beta}\rangle = \frac{1}{2^{-N/4}\sqrt{Z(\beta)}} \sum_{\alpha} e^{-\beta E_{\alpha}/2} c_{\alpha}^s |E_{\alpha}\rangle$$
 (2.16)

Note that the sum runs only over half of the energy eigenstates since  $(-1)^F = \prod_{k=1}^{N/2} S_k$  commutes with Hamiltonian; the energy eigenstates which appear in this expression are

those that live in the same spin parity sector as  $|B_s\rangle$ . As can be checked numerically [34], we can assume these coefficients to be random complex numbers which on average satisfy

<span id="page-8-2"></span>
$$c_{\alpha}^{s} c_{\alpha}^{s*} = 2^{-N/2+1} \delta_{ss'} \tag{2.17}$$

This is the expected behavior assuming the states  $|B_s\rangle$  are random states in the energy basis. We can compute the overlap of different black hole microstates by assuming the coefficients  $c_{\alpha}^{s}$  to be random unitary matrices<sup>2</sup>. With this assumption, we confirm 2.17 and also find that on average

$$\sqrt{\left|\langle B_s^{\beta} | B_{s'}^{\beta} \rangle\right|^2} = \frac{\sqrt{2Z(2\beta)}}{Z(\beta)} \sqrt{1 - \frac{2^{-N/2}Z^2(\beta)}{Z(2\beta)}}$$
(2.18)

which is exponentially small in N. This vanishes as  $\beta \to 0$  as required. This non-vanishing overlap is a sign of the 'over' in overcompleteness. The 'completeness' is shown in equation 2.2.

#### <span id="page-8-0"></span>2.2 More Typical Microstates

The fact that the off-diagonal correlators are not down by powers of 1/N is indicative of these microstates being special. We now describe how to prepare more typical microstates where, at the level of two point functions, all but the diagonal correlators are small. These will be black holes with long throats supported by a large number of out-of-time-order (OTO) shockwaves in the interior.

Let  $W_L$  represent a left sided unitary operator which creates a series of OTO shockwaves when acting on  $|\beta\rangle$ . In particular, the state

$$|W\beta\rangle_{LR} \equiv W_L|\beta\rangle_{LR} \tag{2.19}$$

is dual to the long wormhole supported by OTO shockwaves. Let's assume that the operators  $W_L$  are invariant under the diagonal spin group, which implies that  $|W\beta\rangle_{LR}$  is invariant as well. We want to check that the state

$$|B_s^W\rangle_R \equiv {}_L\langle B_s|W\beta\rangle \tag{2.20}$$

is dual to a single sided black hole with a long throat by computing the diagonal and offdiagonal correlation functions. Just as before, the diagonal correlators can be written as

$${}_{R}\langle B_{s}^{W}|\psi^{i}(t_{1})\psi^{i}(t_{2})|B_{s}^{W}\rangle_{R} = \langle W\beta|\Big[|B_{s}\rangle_{L}\langle B_{s}|\otimes\psi^{i}(t_{1})\psi^{i}(t_{2})\Big]|W\beta\rangle$$
(2.21)

<span id="page-8-1"></span><sup>&</sup>lt;sup>2</sup>We thank D. Stanford for discussions on this point.

![](_page_9_Picture_0.jpeg)

**Figure 2**. Long wormholes supported by out-of-time-ordered (OTO) shockwaves also project into pure states with long throats capped off by an EWB.

<span id="page-9-0"></span>and which are invariant under  $s \to s'$ . Note, since  $W_L$  is unitary, this invariance implies that this expression is equal to

$$\langle \beta | \left[ |B_s\rangle_L \langle B_s| \otimes \psi^i(t_1)\psi^i(t_2) \right] |\beta\rangle$$
 (2.22)

which is given by the thermal expectation value as shown before, and so

$$_R\langle B_s^W | \psi^i(t_1) \psi^i(t_2) | B_s^W \rangle_R \propto \text{Tr} \left[ e^{\beta H} \psi^i(t_1) \psi^i(t_2) \right]$$
 (2.23)

The analysis of the off-diagonal correlator is the same, we have

$$s_{1}\langle B_{s}^{W}|\psi^{1}(t_{1})\psi^{2}(t_{2})|B_{s}^{W}\rangle =$$

$$\langle W\beta|\Big[|B_{s}\rangle_{L}\langle B_{s}|\otimes \mathbb{I}_{R}\Big]\Big[S_{1}\otimes\psi^{1}(t_{1})\psi^{2}(t_{2})\Big]\Big[|B_{\bar{s}}\rangle_{L}\langle B_{\bar{s}}|\otimes \mathbb{I}_{R}\Big]|W\beta\rangle$$
(2.24)

and which is also invariant under the Flip group. Therefore, by the same arguments above is given by

$$= \langle W\beta | \left[ 2i\psi^{1}(0)\psi^{2}(0)\psi^{1}(t_{1})\psi^{2}(t_{2}) \right] | W\beta \rangle$$
(2.25)

$$= 2i\langle W\beta|\psi^{1}(0)\otimes\psi^{1}(t_{1})|W\beta\rangle\langle W\beta|\psi^{2}(0)\otimes\psi^{2}(t_{2})|W\beta\rangle$$
 (2.26)

where the second line is the large N result, and which can be made arbitrarily small as the number of shockwaves is increased. This is the same as what happens in higher dimensions where the left-right correlators die off exponentially in the spatial distance between the boundaries, which here grows arbitrarily with the number of shockwaves [38]. See figure 2. Therefore, we have arrived at pure state black holes in SYK that are more reminiscent of typical states in that all simple observables have thermalized, all the while having an understanding of the structure of the interior of the black hole.

This set of states is also overcomplete and with overlap equal to the atypical case,

$$\langle B_s^W | B_{s'}^W \rangle = \langle B_s^\beta | B_{s'}^\beta \rangle \tag{2.27}$$

It is interesting to compute the overlap between typical and atypical states for the same left projection operator. Using the techniques above we find

$$\langle B_s^{\beta} | B_{s'}^W \rangle = \langle \beta | W | \beta \rangle \tag{2.28}$$

and therefore for states that differ by a small number of shockwaves (assumed to be created in the same way) the overlap is suppressed by powers of 1/N. This can potentially be made exponentially small in N by considering a very large number (order N) of shockwaves.

#### <span id="page-10-0"></span>2.3Bulk Particle Gravitational Dressing and Boundary Energy

We study in this section the possible ways that a bulk particle maybe be gravitationally dressed in AdS<sub>2</sub>, and how this dressing affects the trajectory of the boundary and its energy. Our analysis will be completely within the Schwarzian theory coupled to massive bulk matter. We will leave the details to appendix A.

We will work mostly in embedding space and global AdS<sub>2</sub> coordinates which are related by

$$Y^{-1} = \frac{\cos t}{\sin \sigma} \tag{2.29}$$

$$Y^{0} = \frac{\sin t}{\sin \sigma}$$

$$Y^{1} = -\frac{\cos \sigma}{\sin \sigma}$$
(2.30)

$$Y^1 = -\frac{\cos \sigma}{\sin \sigma} \tag{2.31}$$

whose metrics are

$$ds^{2} = -(dY^{-1})^{2} - (dY^{0})^{2} + (dY^{1})^{2}, Y^{2} = -1$$
(2.32)

$$ds^2 = \frac{-dt^2 + d\sigma^2}{\sin^2 \sigma} \tag{2.33}$$

We begin with the case of a bulk particle in the eternal black hole solution represented by two boundary particles, one for each SYK system. These boundary particles behave as oppositely charged particles in an electric field whose trajectories satisfy [34, 39, 40]

$$Y \cdot Q_{L_{\hat{\sigma}}} = +q, \quad Y \cdot Q_{R_{\hat{\sigma}}} = -q \tag{2.34}$$

where  $Y^{\mu}$  is the trajectory in embedding space, and for some q. These conditions completely determine the trajectory in terms of the charges. Ignoring the presence of the bulk particle for the moment, we can pick a gauge where the boundary charges are

$$Q_{R_{a}}^{a} = (Q_{R_{a}}^{-1}, Q_{R_{a}}^{0}, Q_{R_{a}}^{1}) = (\sqrt{E}, 0, 0) = -Q_{L_{a}}^{a}$$
(2.35)

The left boundary charge is determined form the right by the gauge constraint condition  $Q_{R_{\partial}} + Q_{L_{\partial}} = 0$ . The energy measured on either boundary is given by the quadratic Casimir constructed from the charges, for e.g.

$$H_R = -Q_{R_{\hat{\sigma}}}^2 = E \tag{2.36}$$

A massive neutral bulk particle satisfies the condition

$$Y \cdot Q_{Bp} = 0 \tag{2.37}$$

which also completely determines the trajectory. We choose to parameterize this charge as

$$Q_{Bp}^{a} = m(\sinh \gamma \sin \theta, \sinh \gamma \cos \theta, -\cosh \gamma)$$
 (2.38)

where m is the mass of the particle,  $\gamma$  is the rapidity of the particle relative to global  $AdS_2$  coordinates (the world line approaches a null line as  $\gamma \to \infty$ ), and  $\pi - \theta$  is the value of global time t at which the particle passes through the center of  $AdS_2$ ,  $\sigma = \pi/2$ . A typical trajectory is shown in figure 3. In order to place this particle inside the eternal black hole spacetime, we must satisfy the new gauge constraint

$$Q_{L_{\partial}}^{a} + Q_{Bp}^{a} + Q_{R_{\partial}}^{a} = 0 (2.39)$$

We choose to do so by keeping fixed the trajectory of the bulk particle in global coordinates. This amounts to holding fixed  $Q_{Bp}$  and modifying the boundary particle charges. This modification is the result of gravitationally dressing the bulk particle to the boundaries, of which there is an infinite number of ways to do so. Two particularly interesting cases is where the bulk particle is either dressed entirely to the left or entirely to the right. Respectively, this would leave the charge of the right or left unchanged. This has an interesting effect on the energy measured on the boundaries. The energy of the two boundaries when dressing the particle entirely to the right is

$$H_L = E (2.40)$$

$$H_R = \left(\sqrt{E} - m\sinh\gamma\sin\theta\right)^2 + \left(m\sinh\gamma\cos\theta\right)^2 - \left(m\cosh\gamma\right)^2 \tag{2.41}$$

$$= E - 2m\sqrt{E}\sinh\gamma\sin\theta - m^2 \tag{2.42}$$

$$\approx E - 2m\sqrt{E}\sinh\gamma\sin\theta\tag{2.43}$$

![](_page_12_Figure_0.jpeg)

<span id="page-12-0"></span>Figure 3. Gravitationally dressing a bulk particle (green) to either boundary pushes the boundary trajectories away from the center of AdS2. The solid boundary lines correspond to dressing entirely to the right, and the dotted trajectories are for dressing entirely to the left. The same story holds for the case of the EWB on the right diagram.

where in the last line we took the mass of the particle to be much smaller than mass of the black hole. Since all the dressing is pointing towards the right boundary, we see that the left energy is insensitive to the presence of the bulk particle, as expected.

The dependence of the right measured energy on the trajectory of the bulk particle is interesting. Let's first consider the case where γ ‰ 0. In the gauge picked, the bulk particle will emerge from the past horizon and fall into the future horizon, and θ controls on which exterior the particle will emerge into. For 0 ă θ ă π the particle emerges into the left exterior and registers as negative energy on the right boundary, while for π ă θ ă 2π it emerges into the right exterior and registers as positive energy on the right boundary. For the case where θ " πn for n P Z the particle never emerges out of the black hole and it registers as negative energy m<sup>2</sup> when dressed to either boundary. This case is identical to the γ " 0 situation which describes a particle at rest going through the bifurcation point, and in fact the two are related by an SL2 transformation which preserves the boundary particle trajectories, namely Rindler time evolution.

The trajectories of the boundary particles are also modified by the dressing. As discussed in appendix [A,](#page-47-0) the modification is qualitatively the same for all θ, and the boundary trajectory is pushed farther towards the global AdS<sup>2</sup> boundary.

The situation with the end-of-the-world brane is nearly identical. The charge of the brane is that of a bulk particle with γ Ñ 8 and θ " π{2. Dressing the bulk particle to the boundary leads to the same conclusions as in the eternal black hole in terms of energy and modification of the trajectory. The new thing here is that we have the option of dressing the bulk particle to the brane. Such particles do not change the energy at the boundary, and can be thought of as operators in the single remaining SYK boundary that commute with the Hamiltonian (obviously not as an operator statement but within some subspace of states). Moreover, we find that the trajectory of the brane is not modified but its mass is always decreased independent of the location of the bulk particle[3](#page-13-2) .

## <span id="page-13-0"></span>3 Reconstruction of the Interior via Quantum Error Correction

## <span id="page-13-1"></span>3.1 A Puzzle

In the previous section we reviewed how to construct pure black hole microstates with apparently smooth horizons by projecting out one side of the TFD. We discuss in this subsection an issue this raises from the perspective of bulk reconstruction. In particular, we know from subregion-subregion duality (SSD) that one may write the TFD interpreted as an erasure subsystem code [\[26\]](#page-55-12) as

$$|\beta\rangle_{LR} = U_L U_R |\psi\rangle_{ab} |\chi\rangle_{\bar{a}\bar{b}} \tag{3.1}$$

where H<sup>a</sup> b Ha¯ is a subspace of H<sup>L</sup> and H<sup>b</sup> b H¯<sup>b</sup> is a subspace of HR. The state |ψyab represents the state of the quantum fields on the fixed eternal black hole background, and the code subspace is spanned by all states obtained by acting on the factor. The empty TFD, or the Hartle-Hawking vacuum, is an element of the code subspace. All LR states in this subspace maintain the same state of ¯a ¯b, which represents the fixed background geometry. The unitaries are the so-called encoding unitaries which control how the bulk state is embedded in the boundary product Hilbert space.

This code reproduces the RT formula along with the FLM correction [\[26\]](#page-55-12). Indeed, the von Neuman entropy of, say, the right boundary is

$$S(\rho_R^{\beta}) = S(\rho_{\bar{a}}^{\chi}) + S(\rho_a^{\psi}) \tag{3.2}$$

where the subscripts denote the state from which the reduced density matrix is computed. The first term is fixed for all states in this code subspace and can be thought of as the area term A{4G<sup>N</sup> . The second is the FLM bulk entanglement entropy piece.

<span id="page-13-2"></span><sup>3</sup> Dressing the bulk particles to the brane requires the theory to contain branes of different masses, which is an assumption we make about the UV theory of the bulk. We thank J. Maldacena for pointing this out.

![](_page_14_Picture_0.jpeg)

Figure 4. The naive expectation (left figure) is that a complete projection on the left boundary would distangle the quantum fields across the horizon forming a firewall. This is inconsistent with the motivated picture from the SYK analysis (right) that this projection generates a pure black hole with an interior and a smooth horizon.

<span id="page-14-1"></span>Now we can state the puzzle: if we project out the left system in the TFD we will necessarily disentangle L and R and thus naively also disentangle the two subsystems a and b from each other,

$$|\beta\rangle_{LR} = U_L U_R |\psi\rangle_{ab} |\chi\rangle_{\bar{a}\bar{b}} \to |P\rangle_L \langle P|\beta\rangle_{LR} \stackrel{?}{=} |P\rangle_{a\bar{a}} |P\beta\rangle_{b\bar{b}}$$
(3.3)

Therefore, it would seem that the bulk state will necessarily factorize into an unentangled state of the quantum fields across the horizon! This is a recipe for a firewall. This is inconsistent with the constructions of the previous section where the smoothness of the horizon was maintained after the action of the projection. See figure [4.](#page-14-1)

The rest of this paper is about the resolution of this puzzle and its related consequences. We will see that the flaw in the last argument is the assumed rigidity of the AdS/CFT dictionary relating the bulk and boundary Hilbert spaces. We will show how the QEC interpretation of the duality produces a fluid dictionary which maintains the entanglement across the horizon. Moreover, this construction produces an explicit reconstruction map for the operators behind black hole horizon. It will be clear that this dictionary will be 'state-dependent' providing a concrete realization of the recent ideas of reconstructing the interiors of black holes [\[4–](#page-54-3)[9,](#page-55-13) [11–](#page-55-14)[13\]](#page-55-0).

## <span id="page-14-0"></span>3.2 Toy Model: Projected Random Tensor

We begin by considering a toy model for the AdS/CFT correspondence constructed out of a network of random tensors [\[41,](#page-56-14) [42\]](#page-56-15). A random tensor is a quantum circuit which prepares a set of qubits in a random state in, say, the computational basis. Let's define such a tensor that prepares a state in the product Hilbert space H<sup>L</sup> b H<sup>a</sup> b H<sup>H</sup><sup>L</sup> , with

![](_page_15_Picture_0.jpeg)

Figure 5. A single tensor can be viewed as the encoding of the state of a pure black hole's horizon degrees of freedom H<sup>L</sup> and a set of external modes a into the boundary degrees of freedom L.

|HL| " |Ha| ˆ |H<sup>H</sup><sup>L</sup> |, and also that |Ha| ! |H<sup>H</sup><sup>L</sup> |. The prepared state is

$$|T\rangle = U_{Rand}|00...0\rangle_{LaH_L} = \sum_{ik} |\psi_{ik}\rangle_L |i\rangle_a |k\rangle_{H_L}$$
 (3.4)

where the sum runs over an entire basis of HabH<sup>H</sup><sup>L</sup> . The random unitary URand, guarantees that <sup>L</sup>xψik|ψ<sup>i</sup> 1k <sup>1</sup>y<sup>L</sup> " δii<sup>1</sup>δkk<sup>1</sup>, implying both that there is no mutual information between a and H<sup>L</sup> and that both are maximally entangled with L. The subspace of L spanned by t|ψikyLu is the code subspace of the HL.

This tensor can be thought of as a simplified version of a holographic dictionary for a pure black hole in AdS with boundary L, a set of low energy exterior modes a, and horizon degrees of freedom HL. The dictionary is implemented in the following way: Given a bulk state |φyaH<sup>L</sup> we can obtain its boundary dual by projecting its complex conjugate on the tensor state as follows

$$|\Psi_{\phi}\rangle_{L} = {}_{aH_{L}}\langle\phi^{*}|T\rangle. \tag{3.5}$$

The complex conjugation is just a convenience in order to guarantee that <sup>ř</sup> ik αik|iya|ky<sup>H</sup><sup>L</sup> maps to <sup>ř</sup> ik αik|ψikyL.

From this we can deduce an operator dictionary. An operator OaH<sup>L</sup> on aH<sup>L</sup> would be 'dual' to an operator O<sup>L</sup> on L if OaH<sup>L</sup> |φyaH<sup>L</sup> maps to OL|Ψφy<sup>L</sup> for all |φyaH<sup>L</sup> . Take for instance a bulk operator supported only on a, and an operator on L which satisfies this duality criterion

$$\mathcal{O}_a \otimes \mathbb{I}_{H_L} = \sum_{ij} \mathcal{O}_{ij} |i\rangle_a \langle j| \otimes \mathbb{I}_{H_L} \to \mathcal{O}_L = \sum_{ijk} \mathcal{O}_{ij} |\psi_{ik}\rangle_L \langle \psi_{jk}|$$
(3.6)

![](_page_16_Picture_0.jpeg)

**Figure 6**. The combined tensor produces a subsystem code describing the encoding of the two exterior sets of modes, a and b, into their corresponding boundaries, L and R.

We can get a toy model for the eternal black hole by sowing two such codes via summing over the horizon indices H. We denote the new tensor by  $|TT\rangle$ 

$$|TT\rangle = \sum_{ijk} |\psi_{ik}\rangle_L |\psi_{jk}\rangle_R |i\rangle_a |j\rangle_b$$
 (3.7)

It's not hard to see that this code satisfies subregion-subregion duality, namely

$$\mathcal{O}_a \otimes \mathbb{I}_b \to \mathcal{O}_L \otimes \mathbb{I}_R, \ \mathbb{I}_a \otimes \mathcal{O}_b \to \mathbb{I}_L \otimes \mathcal{O}_R$$
 (3.8)

using a similar map to the single tensor case, and furthermore satisfies the quantum corrected RT formula. Take for instance a state  $|\phi\rangle_{ab}$  which maps to the state  $|\Psi_{\phi}\rangle_{LR}$ . The von Neumann entropy of R in this state is

$$S(\rho_R^{\Psi_\phi}) = |\mathcal{H}_H| + S(\rho_b^\phi) \tag{3.9}$$

where  $|\mathcal{H}_H|$  comes from summing the index k and can be regarded as reproducing the area term of RT, and  $\rho_b^{\phi} = \text{Tr}_a |\phi\rangle\!\langle\phi|$ ,  $\rho_R^{\Psi_{\phi}} = \text{Tr}_L |\Psi_{\phi}\rangle\!\langle\Psi_{\phi}|$ . The second term is the FLM quantum correction to the RT formula.

Now we study how the correction properties of this code get modified by the action of a projection operator on the L system. In particular, we want to see if a state  $|\phi\rangle_{ab}$  is preserved under the action of a projector on L. We check this through the following series of steps:

1. Project the state  $|\phi^*\rangle_{ab}$  on the TFD tensor network to obtain the boundary dual of  $|\phi\rangle_{ab}$ 

$$|\phi\rangle_{ab} \to |\Psi_{\phi}\rangle_{LR} = {}_{ab}\langle\phi^*|TT\rangle$$
 (3.10)

![](_page_17_Picture_0.jpeg)

Figure 7. The projected tensor now describes a mapping of both a and b into the right boundary R. The map from b into R is the same as in the unprojected case and does not depend on P, while the map from a into R depends on it sensitively.

2. Act on the left boundary with the projection operator |PyLxP| to obtain a new product state of the two boundaries

$$|P\rangle_L\langle P|\Psi_{\phi}\rangle_{LR}$$
 (3.11)

3. Run this new product state through the old tensor network to generate its dual bulk state. The question of interest is: what are the conditions on P such that we regain the original bulk state |φyab

$$_{LR}\langle\Psi_{\phi}|P\rangle_{L}\langle P|TT\rangle \stackrel{?}{=} |\phi\rangle_{ab}$$
 (3.12)

Note that a more convenient interpretation of the left hand side of this equality is the projection of a new state of the right boundary <sup>L</sup>xP|ΨφyLR on the new projected tensor network <sup>L</sup>xP|T Ty. This new projected tensor network represents the new dictionary post projection.

For this to be true for all bulk states, it is necessary and sufficient to apply it to a basis

$$\sum_{k} {}_{R} \langle \psi_{jk} | {}_{L} \langle \psi_{ik} | P \rangle_{L} \langle P | TT \rangle \stackrel{?}{=} | i \rangle_{a} | j \rangle_{b}$$
(3.13)

The left hand side simplifies to

$$\sum_{i'} \left( \sum_{k} {}_{L} \langle \psi_{ik} | P \rangle_{L} \langle P | \psi_{i'k} \rangle_{L} \right) |i'\rangle_{a} |j\rangle_{b}$$
(3.14)

Therefore, to preserve the bulk state we require that

<span id="page-18-1"></span>
$$\sum_{k} {}_{L} \langle \psi_{ik} | P \rangle_{L} \langle P | \psi_{i'k} \rangle_{L} = \delta_{ii'}$$
(3.15)

This condition is a standard QEC condition on the set of correctable errors, namely that they act as the identity within the code subspace. From the bulk, this says that the insertion of the end-of-the-world brane does not alter the state of the bulk quantum fields. This is not exactly correct, and we'll consider the more realistic situation in section 3.4.

This condition can be satisfied by choosing P such that the projection of  $|P\rangle_L$  onto the code subspace is a random state in the basis  $|\psi_{ik}\rangle$ ; equivalently that  $\langle P|\psi_{i'k}\rangle$  are random complex numbers. This satisfies the necessary equality to an accuracy of  $\sqrt{|a|/|H_L|}$ . Note that we can easily pick a projection which does not preserve the bulk state, for example  $|P\rangle = \sum_k \alpha_k |\psi_{1k}\rangle$ , for any  $\alpha_k$ . This will necessarily break the entanglement between the bulk modes creating a firewall.

We can also determine the operator map from the bulk legs a and b into R after the projection. The goal is to find for every logical operator  $\mathcal{O}_{LR}$ , dual to some bulk operator  $\mathcal{O}_{ab}$  in the original unprojected tensor code, an operator supported purely on R such that

<span id="page-18-0"></span>
$${}_{L}\langle P|\mathcal{O}_{LR}|\Psi_{\phi}\rangle_{LR} = \mathcal{O}_{R} {}_{L}\langle P|\Psi_{\phi}\rangle_{LR}$$
(3.16)

for all  $|\phi\rangle_{ab}$  where  $|\Psi_{\phi}\rangle_{LR} = {}_{ab}\langle\phi^*|TT\rangle$ . The dictionary for operators on the right exterior is the same as that of the original unprojected tensor giving the map

$$\mathbb{I}_a \otimes \mathcal{O}_b \equiv \mathbb{I}_a \otimes \sum_{jj'} \mathcal{O}_{jj'} |j\rangle_b \langle j'| \to \mathcal{O}_R^b = \sum_{jj'k} \mathcal{O}_{jj'} |\psi_{jk}\rangle_R \langle \psi_{j'k}|$$
(3.17)

As for operators originally on the left exterior, which become interior operators after the projection, we have

$$\mathcal{O}_{a} \otimes \mathbb{I}_{b} \equiv \sum_{ii'} \mathcal{O}_{ii'} |i\rangle_{a} \langle i'| \otimes \mathbb{I}_{b}$$

$$\to \mathcal{O}_{R}^{a}(P) = \sum_{ii'jkk'} \mathcal{O}_{ii'L} \langle P|\psi_{ik}\rangle_{L} |\psi_{jk}\rangle_{R} \langle \psi_{jk'}|_{L} \langle \psi_{i'k'}|P\rangle_{L}$$
(3.18)

Which can be checked to satisfy 3.16 assuming 3.15. And therefore we have generated a new dictionary for the interior operators  $\mathcal{O}_R^a(P)$  which looks very different from that of the exterior operators  $\mathcal{O}_R^b$ . A key difference is in the dependence of the interior operators on the projection operator P, and therefore on the microstate of the black

![](_page_19_Picture_0.jpeg)

Figure 8. This long tensor network can be viewed as either a regular eternal black hole with more external modes in the code subspace, or as a long wormhole where some of bulk legs correspond to modes in the interior. The top left picture represents the standard dictionary for a wormhole where the RT surface in the center. As you go from P<sup>1</sup> to P<sup>3</sup> the projection is more fine tuned to place the brane, shown in dotted green, at different locations in the bulk.

<span id="page-19-0"></span>hole around which our code subspace lives. This dictionary therefore is state-dependent [\[4–](#page-54-3)[9,](#page-55-13) [11](#page-55-14)[–13\]](#page-55-0).

This result shows how the puzzle of the previous subsection is resolved in this model, and that indeed the bulk state and the entanglement across the horizon is maintained. The invalid assumption we made previously was to take the dictionary between the bulk and boundary to be rigid, namely that defined by the state |T Ty. However, what we learn now is that the projected tensor defines a new dictionary generated by acting with the projection operator <sup>L</sup>xP|T Ty. In particular, while prior to the projection the bulk factors a and b were reconstructable in L and R respectively, the post projection tensor network <sup>L</sup>xP|T Ty maps both to the right boundary R. This fluidity of the dictionary is a new observation bound to be critical for general bulk reconstruction.

This toy model makes it seem that the entire left exterior is either projected on or remapped to the right, without anything in between. However, this is due to the simplicity of the model having only a single bulk index on each exterior. We could consider instead combining a number of random tensors that satisfy the subregion subregion duality structure of the thermofield double. Take for instance the case with four bulk legs shown in figure [8](#page-19-0) utilizing four random tensors of different dimensionality. Note that this tensor network can also be thought of as that of a long wormhole where some of the bulk indices correspond to modes in the interior. The tensor state for this network is

$$|T^4\rangle = \sum_{i_1 i_2 j_1 j_2 k} |\psi_{i_1 i_2 k}\rangle_L |\psi_{j_1 j_2 k}\rangle_R |i_1\rangle_{a_1} |i_2\rangle_{a_2} |j_1\rangle_{b_1} |j_2\rangle_{b_2}$$
(3.19)

where the sums run over an entire basis of  $\mathcal{H}_{a_1} \otimes \mathcal{H}_{a_2} \otimes \mathcal{H}_{b_1} \otimes \mathcal{H}_{b_2}$ , and the states appearing in the factors L and R satisfy  $\langle \psi_{i_1 i_2 k} | \psi_{i'_1 i'_2 k'} \rangle = \delta_{i_1 i'_1} \delta_{i_2 i'_2} \delta_{kk'}$ . For a completely generic projection operator we would reproduce

$$\sum_{k} {}_{L} \langle \psi_{i_1 i_2 k} | P \rangle_{L} \langle P | \psi_{i'_1 i'_2 k} \rangle_{L} = \delta_{i_1 i'_1} \delta_{i_2 i'_2}$$

$$(3.20)$$

However, we could choose a less random projector so that  $_L\langle\psi_{i_1i_2k}|P\rangle_L$  are random coefficients without correlations when varying  $i_2$  and k, but with correlations in the  $i_1$  index. This can be chosen to produce, for example, the condition

$$\sum_{k} {}_{L} \langle \psi_{i_1 i_2 k} | P \rangle_{L} \langle P | \psi_{i'_1 i'_2 k} \rangle_{L} = \delta_{i_1 1} \delta_{i'_1 1} \delta_{i_2 i'_2}$$

$$(3.21)$$

Therefore, the bulk state would transform after the projection as follows

$$|\psi\rangle_{a_1a_2b_1b_2} \to |1\rangle_{a_1}|\widetilde{\psi}\rangle_{a_2b_1b_2}$$
 (3.22)

where the latter factor is mapped to the right boundary, as in the top right picture of figure 8. The bulk dual of the projection in this case would be a brane which partitions the bulk between the  $a_1$  and  $a_2$  subsystems<sup>4</sup>.

We've assumed in this section that the size of the bulk Hilbert space a corresponding to the projected black hole interior was smaller than that of the horizon legs  $H_L$ . This was necessary to ensure the QEC property of establishing a dictionary between the interior and the boundary, and to guarantee that orthogonal bulk states map to orthogonal boundary states. To see how this would fail otherwise, consider again the projected tensor network represented by the state

$${}_{L}\langle P|TT\rangle = \sum_{ijk} {}_{L}\langle P|\psi_{ik}\rangle_{L}|\psi_{jk}\rangle_{R}|i\rangle_{a}|j\rangle_{b}$$
(3.23)

Consider two (naively) orthogonal bulk states  $|i\rangle_a|j\rangle_a$  and  $|i'\rangle_a|j'\rangle_a$  and compute their overlap after mapping them to the boundary. These states map onto the boundary as

$$|i\rangle_a|j\rangle_a \to \sum_k {}_L\langle P|\psi_{ik}\rangle_L|\psi_{jk}\rangle_R$$
 (3.24)

$$|i'\rangle_a|j'\rangle_a \to \sum_k {}_L\langle P|\psi_{i'k}\rangle_L|\psi_{j'k}\rangle_R$$
 (3.25)

The overlap of these states on the boundary is given by

$$\sum_{kk'} {}_{L} \langle \psi_{ik'} | P \rangle_{LL} \langle P | \psi_{ik} \rangle_{LR} \langle \psi_{j'k'} | \psi_{jk} \rangle_{R} = \delta_{j'j} \sum_{k} {}_{L} \langle \psi_{ik'} | P \rangle_{LL} \langle P | \psi_{ik} \rangle_{L}$$
(3.26)

<span id="page-20-0"></span><sup>&</sup>lt;sup>4</sup>One can also find a projection which projects on the state of  $a_2$  but where  $a_1$  is still remapped to the R boundary. It is not obvious what the bulk spacetime would look like for this situation.

The delta function  $\delta_{j'j}$  represents the orthogonality of the exterior bulk states irrespective of the size of the horizon. For the case of  $|a| \ll |H_L|$ , the second factor should equal  $\delta_{ii'}$  giving the QEC property 3.15. Now, if  $|a| > |H_L|$ , this property can never be satisfied (a Hilbert space cannot contain a number of mutually orthogonal states greater than its dimension), and therefore the states  $|i\rangle_a$  and  $|i'\rangle_a$  are not orthogonal from the boundary perspective. The reason why the size of the horizon is relevant is that it acts as bottleneck that the information of a needs to go through on its way to the right boundary R. It would be interesting to study what this means for bulk operators, and whether it implies a departure from their naively expected algebra. In the rest of the paper we will assume that the dimension of the bulk legs is never larger than the dimension of the horizon as to avoid these problems.

## <span id="page-21-0"></span>3.3 Projected Quantum Subsystem Correcting Code

Next we consider the erasure subsystem code of [26] and prove a theorem about how its recovery properties are modified by the projection operator. We will continue with the notation above adapted to the eternal black hole setup.

This code is summarized as follows: Within the two boundary Hilbert space,  $\mathcal{H} = \mathcal{H}_L \otimes \mathcal{H}_R$  (assumed to have finite dimension), one can assume the existence of a factorizeable code subspace  $\mathcal{H}_{code} = \mathcal{H}_a \otimes \mathcal{H}_b$ , whereby a and b correspond to the left and right exteriors respectively. Defining  $|\tilde{i}\rangle$  and  $|\tilde{j}\rangle$  as orthonormal basis states for  $\mathcal{H}_a$  and  $\mathcal{H}_b$ , the following statements, among others, are equiavalent [26]

1. For |a| < |L| and |b| < |R|, the left and right Hilbert spaces can be decomposed as  $\mathcal{H}_L = (\mathcal{H}_{L_a} \otimes \mathcal{H}_{\bar{L}_a}) \oplus \mathcal{H}_{\tilde{L}}$  and  $\mathcal{H}_R = (\mathcal{H}_{R_b} \otimes \mathcal{H}_{\bar{R}_b}) \oplus \mathcal{H}_{\tilde{R}}$ , with  $|L_a| = |a|$  and  $|R_b| = |b|$  and where  $|\tilde{L}| < |a|$  and  $|\tilde{R}| < |b|$ . There exists encoding unitary operators  $U_L$  and  $U_R$  on L and R, respectively, such that

$$|\tilde{ij}\rangle_{LR} = U_L U_R |i\rangle_{L_a} |j\rangle_{R_b} |\chi\rangle_{\bar{L}_a\bar{R}_b}$$
 (3.27)

for some state  $|\chi\rangle$  on  $\mathcal{H}_{\bar{L}_a}\otimes\mathcal{H}_{\bar{R}_b}$ .

2. For all logical operators  $\widetilde{\mathcal{O}}_a$  and  $\widetilde{\mathcal{O}}_b$  acting within the code subspace  $\mathcal{H}_{code}$ , there exist operators  $\mathcal{O}_L$  and  $\mathcal{O}_R$  such that

$$\mathcal{O}_L |\widetilde{\psi}\rangle = \widetilde{\mathcal{O}}_a |\widetilde{\psi}\rangle, \ \mathcal{O}_L^{\dagger} |\widetilde{\psi}\rangle = \widetilde{\mathcal{O}}_a^{\dagger} |\widetilde{\psi}\rangle$$
 (3.28)

$$\mathcal{O}_R |\widetilde{\psi}\rangle = \widetilde{\mathcal{O}}_b |\widetilde{\psi}\rangle, \ \mathcal{O}_R^{\dagger} |\widetilde{\psi}\rangle = \widetilde{\mathcal{O}}_b^{\dagger} |\widetilde{\psi}\rangle$$
 (3.29)

for any state  $|\widetilde{\psi}\rangle \in \mathcal{H}_{code}$ .

#### 3. The reference state

$$|\phi\rangle = \frac{1}{\sqrt{|a||b|}} \sum_{ij} |i\rangle_{T_a} |j\rangle_{T_b} |\widetilde{ij}\rangle \tag{3.30}$$

where  $T_a$  and  $T_b$  are auxiliary subsystems of dimensions |a| and |b| respectively. The density matrices constructed from this state satisfy

$$\rho_{T_a T_b R}(\phi) = \rho_{T_a}(\phi) \otimes \rho_{T_b R}(\phi) \tag{3.31}$$

$$\rho_{T_a T_b L}(\phi) = \rho_{T_b}(\phi) \otimes \rho_{T_a L}(\phi) \tag{3.32}$$

We refer the reader to [26] for a full proof of the equivalence of these statements. The second point above is the QEC interpretation of subregion subregion duality, and it follows straightforwardly from the first condition. Since  $|a| = |L_a|$ , there is an isomorphism between operators acting on  $\mathcal{H}_a$  and  $\mathcal{H}_{L_a}$ ,

$$\widetilde{\mathcal{O}}_a|\widetilde{i}\rangle = \sum_k \mathcal{O}_{ki}|\widetilde{k}\rangle \sim \mathcal{O}_{L_a}|i\rangle_{L_a} = \sum_k \mathcal{O}_{ki}|k\rangle_{L_a}$$
 (3.33)

Therefore, an operator on L with the same action can be defined as

$$\mathcal{O}_L = U_L \mathcal{O}_{L_a} U_L^{\dagger} \tag{3.34}$$

The same conclusion holds for the right side.

Next, we will study how this code is modified by the action of a projector on the L subsystem. We will see, just as in the random tensor toy model, we can place conditions on the projection operators such that the entire original code subspace continues to be correctable. Consider the following theorem:

<span id="page-22-0"></span>**theorem 3.3.1.** Consider a subsystem code for the encoding of a code subspace  $\mathcal{H}_{code} = \mathcal{H}_a \otimes \mathcal{H}_b$  in a larger physical Hilbert space  $\mathcal{H}_L \otimes \mathcal{H}_R$  with the properties described above. Consider also a complete projection  $P_L \equiv |P\rangle_L \langle P|$  on the subsystem L. The following statements are equivalent:

(i) For  $|a| < |\overline{R}_b|$ , we consider the decomposition of  $\mathcal{H}_{\bar{R}_b} = \left(\mathcal{H}_{\bar{R}_b^1} \otimes \mathcal{H}_{\bar{R}_b^2}\right) \oplus \mathcal{H}_{\bar{R}_b^3}$  with  $|\bar{R}_b^1| = |a|$  and  $|\bar{R}_b^3| < |a|$ . The projected code states can be written as

$$\frac{L\langle P|\tilde{ij}\rangle_{LR}}{\sqrt{N^{P}}} = U_{R}\left(W_{\bar{R}_{b}}^{P} \otimes \mathbb{I}_{R_{b}}\right)|i\rangle_{\bar{R}_{b}^{1}}|j\rangle_{R_{b}}|\widetilde{\chi}\rangle_{\bar{R}_{b}^{2}}$$
(3.35)

where  $U_R$  is the same unitary of the original subsystem code, and  $W_{\bar{R}_b}^P$  is a unitary which depends on the projection, and for some state  $|\widetilde{\chi}\rangle_{\bar{R}_b^2}$  and normalization  $N^P$ .

(ii) For any logical operator  $\widetilde{\mathcal{O}}$  of the unprojected code, there exists an operator  $\mathcal{O}_R$  such that

$$_{L}\langle P|\widetilde{\mathcal{O}}|\widetilde{\psi}\rangle_{LR} = \mathcal{O}_{R} \ _{L}\langle P|\widetilde{\psi}\rangle_{LR}$$
 (3.36)

$$_{L}\langle P|\widetilde{\mathcal{O}}^{\dagger}|\widetilde{\psi}\rangle_{LR} = \mathcal{O}_{R}^{\dagger} \ _{L}\langle P|\widetilde{\psi}\rangle_{LR}$$
 (3.37)

for any state  $|\widetilde{\psi}\rangle$  of the original code subspace.

(iii) The projection onto the code subspace of  $P_L$  acts identically on the code subspace

$$\mathcal{P}_{code} \ P_L \ \mathcal{P}_{code} = N^P \ \mathcal{P}_{code} \tag{3.38}$$

where  $\mathcal{P}_{code}$  is the projector on the original  $\mathcal{H}_{code}$ , for some positive real number  $N^{P}$ .

(iv) The projected reference state

$$_{L}\langle P|\phi\rangle = \frac{1}{\sqrt{|a||b|}} \sum_{ij} |ij\rangle_{T_{a}T_{b}} _{L}\langle P|\widetilde{ij}\rangle_{LR}$$
 (3.39)

when normalized, satisfies  $I(T_a, T_b) = 0$  and  $S_{ent}(\rho_{T_aT_b}) = \ln |\mathcal{H}_{code}|$ .

Proof.

•  $(i) \implies (ii)$ :

For any logical operator  $\widetilde{\mathcal{O}}$  we can define an operator

$$\mathcal{O}_{R} = U_{R} \left( W_{\bar{R}_{b}}^{P} \otimes \mathbb{I}_{R_{b}} \right) \mathcal{O}_{\bar{R}_{b}^{1} R_{b}} \left( \left( W_{\bar{R}_{b}}^{P} \right)^{\dagger} \otimes \mathbb{I}_{R_{b}} \right) U_{R}^{\dagger}$$
(3.40)

where  $\mathcal{O}_{\bar{R}_b^1 R_b}$  has support only on  $\bar{R}_b^1 R_b$  and has the same matrix elements as  $\widetilde{\mathcal{O}}$ . This immediately implies the second property.

• (ii) => (iii):

For all logical operators  $\widetilde{\mathcal{O}}$  we have

$$\widetilde{\mathcal{O}}\mathcal{P}_{code}|P\rangle_{L}\langle P|\mathcal{P}_{code} = \mathcal{P}_{code}\widetilde{\mathcal{O}}|P\rangle_{L}\langle P|\mathcal{P}_{code}$$
(3.41)

$$= \mathcal{P}_{code}|P\rangle_L \mathcal{O}_{R\ L}\langle P|\mathcal{P}_{code}$$
 (3.42)

$$= \mathcal{P}_{code}|P\rangle_L\langle P|\tilde{\mathcal{O}}\mathcal{P}_{code} \tag{3.43}$$

$$= \mathcal{P}_{code}|P\rangle_L\langle P|\ \mathcal{P}_{code}\widetilde{\mathcal{O}}$$
 (3.44)

We used the property (ii) twice. Therefore  $\left[\widetilde{\mathcal{O}}, \mathcal{P}_{code} P_L \mathcal{P}_{code}\right] = 0$  for all operators acting with the code subspace. Schur's lemma then guarantees

$$\mathcal{P}_{code} P_L \mathcal{P}_{code} \propto \mathcal{P}_{code}$$
 (3.45)

The left hand side being a positive operator determines the proportionality constant to be a positive really number we can call  $N^P$ .

•  $(iii) \implies (iv)$ :

By direct computation we have

$$\rho_{T_a T_b} = \frac{1}{|a||b|} \sum_{ii'jj'} |ij\rangle_{T_a T_b} \langle i'j'| \frac{LR\langle i'j'|P\rangle_L \langle P|ij\rangle_{LR}}{N^P}$$
(3.46)

$$= \frac{1}{|a||b|} \sum_{ii'jj'} |ij\rangle_{T_a T_b} \langle i'j'|\delta_{ii'}\delta_{jj'}$$
(3.47)

$$= \frac{1}{|a||b|} \sum_{ij} |ij\rangle_{T_a T_b} \langle ij| \tag{3.48}$$

$$= \rho_{T_a} \otimes \rho_{T_b} \tag{3.49}$$

where in the first step we used  $\mathcal{P}_{code}$   $P_L$   $\mathcal{P}_{code} = N^P$   $\mathcal{P}_{code}$ . This factorized density matrix ensures that the mutual information between  $T_a$  and  $T_b$  vanishes. Moreover, the total density matrix is maximally mixed with dimension  $|\mathcal{H}_{code}|$ , and therefore

$$S_{ent}(\rho_{T_aT_b}) = \ln |\mathcal{H}_{code}| \tag{3.50}$$

 $\bullet \ \ (iv) \implies \ (i):$ 

Inherited from the original unprojected code we have that

$${}_{L}\langle P|\widetilde{ij}\rangle_{LR} = U_{R}|j\rangle_{R_{b}} {}_{L}\langle P|U_{L}|i\rangle_{L_{a}}|\chi\rangle_{\bar{L}_{a}\bar{R}_{b}}$$
(3.51)

and therefore we need to show

$${}_{L}\langle P|U_{L}|i\rangle_{L_{a}}|\chi\rangle_{\bar{L}_{a}\bar{R}_{b}} = \sqrt{N^{P}}W_{\bar{R}_{b}}^{P}|i\rangle_{\bar{R}_{b}^{1}}|\widetilde{\chi}\rangle_{\bar{R}_{b}^{2}}$$
(3.52)

For some unitary  $W_{\bar{R}_b}^P$  on  $\bar{R}_b$  and numerical factor  $\sqrt{N^P}$ . This can only be true if  $|L_a| = |a| < |\bar{R}_b|$ . Dividing  $|\bar{R}_b|$  by |a| we get  $|\bar{R}_b^2|$  with remainder  $|\bar{R}_b^3| < |a|$ . Therefore we can consider the Hilbert space factorization  $\mathcal{H}_{\bar{R}_b} = \left(\mathcal{H}_{\bar{R}_b^1} \otimes \mathcal{H}_{\bar{R}_b^2}\right) \oplus \mathcal{H}_{\bar{R}_b^3}$ , with  $|\bar{R}_b^1| = |a|$ .

The state  $_L\langle P|\phi\rangle$  is a purification of the maximally mixed density matrix of the  $T_aT_b$  subsystem, which after normalization must be of the form

$$\frac{L\langle P|\phi\rangle}{\sqrt{N_{\phi}^{P}}} = \sum_{ij} |ij\rangle_{T_a T_b} V_R |ij\rangle_R \tag{3.53}$$

$$= \sum_{ij} |ij\rangle_{T_a T_b} V_R |j\rangle_{R_b} |i\rangle_{\bar{R}_b^1} |\widetilde{\chi}\rangle_{\bar{R}_b^2}$$
 (3.54)

For some  $V_R$  to be determined based on the Hilbert space factorization of R. Requiring this to be equal to the projected reference state we must have

$$U_R|j\rangle_{R_b} {}_L\langle P|U_L|i\rangle_{L_a}|\chi\rangle_{\bar{L}_a\bar{R}_b} = \sqrt{N_\phi^P}V_R|j\rangle_{R_b}|i\rangle_{\bar{R}_b^1}|\widetilde{\chi}\rangle_{\bar{R}_b^2}$$
(3.55)

for all j, which forces  $V_R$  to satisfy

$$U_R^{\dagger} V_R = W_{\bar{R}_b}^P \otimes \mathbb{I}_{R_b} \tag{3.56}$$

for some  $W_{\bar{R}_b}^P$ . It also follows that we should identify the constants  $N_{\phi}^P = N^P$ .

# <span id="page-25-0"></span>3.4 Operator Algebra Quantum Error Correction from Projected Subsystem Codes

The projected subsystem code of the previous section is not quite realized by the KM construction of projecting out one side of the SYK thermofield double. The issue is that the projections considered in KM act nontrivially within the code subspace. Indeed, correlation functions of simple operators receive a modification, for example the off-diagonal fermion correlation functions with and without the projection are:

$$\langle \beta | \mathbb{I}_L \otimes \psi_R^1(t_1) \psi_R^2(t_2) | \beta \rangle \sim \mathcal{O}(1/N^q)$$
 (3.57)

$$\langle \beta | P_L \otimes \psi_R^1(t_1) \psi_R^2(t_2) | \beta \rangle \sim G_\beta(t_1, i\beta/2) G_\beta(t_2, i\beta/2)$$
 (3.58)

Therefore, the projection on the code subspace of  $P_L$  does not act identically within the code subspace

$$\mathcal{P}_{code} P_L \mathcal{P}_{code} \not\subset \mathcal{P}_{code}$$
 (3.59)

This immediately precludes the complete recovery of the state of the code subspace prior to the projection. However, as we will see, it still allows us to recover a subalgebra of logical operators, namely all operators which satisfy

$$\left[\mathcal{P}_{code} \ P_L \ \mathcal{P}_{code}, \widetilde{\mathcal{O}}\right] = 0 \tag{3.60}$$

This kind of QEC has appeared before in [19, 20] and is called Operator Algebra Quantum Error Correction (OAQEC), and was utilized in [16, 25, 26].

This condition is motivated from the bulk picture of the brane on the t=0 slice being localized near the boundary and would therefore commute with spacelike separated operators on that same slice. It would then apply to any bulk operator, inside or outside the horizon, that is dressed to the remaining boundary. The situation is not so clear for the left dressed operators, as those naively do not commute with the projection operator. We conjecture that, in some sense, the part of the operator that extends past the location of the brane into the bulk does commute with the projection, but we fully acknowledge the difficulty of squaring this with bulk diffeomorphism invariance.

Moving on, we will prove the following theorem:

<span id="page-26-0"></span>**theorem 3.4.1.** Consider a subsystem code for the encoding of a code subspace  $\mathcal{H}_{code} = \mathcal{H}_a \otimes \mathcal{H}_b$  in a larger physical Hilbert space  $\mathcal{H}_L \otimes \mathcal{H}_R$  with the properties described above. Consider also a complete projection  $P_L \equiv |P\rangle_L \langle P|$  on the subsystem L. For any logical operator  $\widetilde{\mathcal{O}}$  the following statements are equivalent:

(i) There exists an operator  $O_R$ , and its Hermitian conjugate  $O_R^{\dagger}$ , with support on R such that

$$_{L}\langle P|\tilde{\mathcal{O}}|\tilde{\psi}\rangle_{LR} = O_{R} _{L}\langle P|\tilde{\psi}\rangle_{LR}$$
 (3.61)

$$_{L}\langle P|\tilde{\mathcal{O}}^{\dagger}|\tilde{\psi}\rangle_{LR} = O_{R}^{\dagger} _{L}\langle P|\tilde{\psi}\rangle_{LR}$$
 (3.62)

for all states  $|\widetilde{\psi}\rangle_{LR} \in \mathcal{H}_{code}$ .

(ii) The logical operator  $\widetilde{\mathcal{O}}$  commutes with the projection on the code subspace of the projection operator  $P_L$ 

$$\left[ \mathcal{P}_{code} \ P_L \ \mathcal{P}_{code}, \widetilde{\mathcal{O}} \right] = 0 \tag{3.63}$$

Proof.

- $(i) \implies (ii)$ :
  This is identical to the proof of the  $(ii) \implies (iii)$  implication of theorem 3.3.1.
- $\bullet$  (ii)  $\Longrightarrow$  (i): On the original subsystem code reference state

$$|\phi\rangle = \frac{1}{\sqrt{|a||b|}} \sum_{ij} |ij\rangle_{T_a T_b} |\tilde{i}\tilde{j}\rangle_{LR}$$
 (3.64)

we have

$$\widetilde{\mathcal{O}}|\phi\rangle = \mathcal{O}_{T_a T_b}^T |\phi\rangle \tag{3.65}$$

where  $\mathcal{O}^T$  is the transpose of  $\widetilde{\mathcal{O}}$  but with support on  $T_aT_b$ . Similarly for the Hermitian conjugate  $\widetilde{\mathcal{O}}^{\dagger}$  and  $\left(\mathcal{O}_{T_aT_b}^{\dagger}\right)^T$ . Notice that the projection of  $P_L$  on the code subspace

$$\mathcal{P}_{code} \ P_L \ \mathcal{P}_{code} = \sum_{ii'jj'} \left( \langle \widetilde{ij} | P \rangle_L \langle \ P | \widetilde{i'j'} \rangle \right) |\widetilde{ij} \rangle \langle \widetilde{i'j'} |$$
 (3.66)

has the same matrix elements as the transpose of the reference  $T_aT_b$  density matrix of the normalized state

$$\frac{{}_{L}\langle P|\phi\rangle}{\sqrt{N_{\phi}^{P}}} = \frac{1}{\sqrt{N_{\phi}^{P}|a||b|}} \sum_{ij} |ij\rangle_{T_{a}T_{b}} {}_{L}\langle P|\widetilde{ij}\rangle_{LR}$$
(3.67)

given by

$$\rho_{T_a T_b} = \frac{1}{|a||b|} \sum_{ii'jj'} \left( \frac{\langle \widetilde{i'j'}|P\rangle_L \langle P|\widetilde{ij}\rangle}{N_\phi^P} \right) |ij\rangle_{T_a T_b} \langle i'j'|$$
(3.68)

This shows the equivalence of

$$\left[\mathcal{P}_{code} \ P_L \ \mathcal{P}_{code}, \widetilde{\mathcal{O}}\right] = 0 \Longleftrightarrow \left[\rho_{T_a T_b}, \mathcal{O}_{T_a T_b}^T\right] = 0 \tag{3.69}$$

and similarly for  $\widetilde{\mathcal{O}}^{\dagger}$  and  $\left(\mathcal{O}_{T_aT_b}^{\dagger}\right)^T$  since the density matrices and projectors are Hermitian.

The next step is to show that this implies the existence of  $O_R$  such that

$$\mathcal{O}_{T_a T_b}^T L \langle P | \phi \rangle = O_R L \langle P | \phi \rangle \tag{3.70}$$

$$\left(\mathcal{O}_{T_a T_b}^{\dagger}\right)^T {}_L \langle P|\phi\rangle = O_R^{\dagger} {}_L \langle P|\phi\rangle \tag{3.71}$$

This has already been proven in [16], but we reiterate it here for completeness. We show this by constructing such an  $O_R$  and  $O_R^{\dagger}$ , and show that they are indeed Hermitian conjugates. For the sake of notational simplicity, we redefine  $|I\rangle \equiv |ij\rangle$ . Moreover, we work in a different basis for the R subsystem such that

$${}_{L}\langle P|\phi\rangle^{N} \equiv \frac{{}_{L}\langle P|\phi\rangle}{\sqrt{N_{\phi}^{P}}} = \sum_{IK} \alpha_{KI}|I\rangle_{T_{a}T_{b}}|K\rangle_{R}$$
(3.72)

where αKI can be thought of as a |Hcode| ˆ |HR| rectangular matrix. The density matrix of the reference subsystem is given by ρ<sup>T</sup>aT<sup>b</sup> " αα: . The commutativity of O<sup>T</sup> TaT<sup>b</sup> with this density matrix ensures that it preserves the subspace of support of ρ<sup>T</sup>aT<sup>b</sup> on Hcode. Within this subspace α has a right inverse α ´<sup>1</sup> " α :ρ ´1 TaT<sup>b</sup> . This allows us to construct O<sup>R</sup> as follows:

$$\mathcal{O}_{T_a T_b}^T L \langle P | \phi \rangle^N = \sum_{IJK} (\mathcal{O}^T)_{JI} \alpha_{KI} | J \rangle_{T_a T_b} | K \rangle_R$$
(3.73)

$$= \sum_{JK} \alpha_{MJ} |J\rangle_{T_a T_b} \sum_{ILM} \alpha_{ML}^{-1} \left(\mathcal{O}^T\right)_{LI} \alpha_{KI} |K\rangle_R$$
 (3.74)

$$= \sum_{JK} \alpha_{MJ} |J\rangle_{T_a T_b} \left(\alpha^{-1} \mathcal{O}^T \alpha\right)^T |M\rangle_R \tag{3.75}$$

$$= \left(\alpha^T \mathcal{O}(\alpha^{-1})^T\right)_R \ _L \langle P|\phi\rangle^N \tag{3.76}$$

and similarly for the Hermitian conjugate ´ O : TaT<sup>b</sup> ¯T . Therefore we have

$$O_R = \alpha^T \mathcal{O}(\alpha^{-1})^T \tag{3.77}$$

$$O_R^{\dagger} = \alpha^T \mathcal{O}^{\dagger} (\alpha^{-1})^T \tag{3.78}$$

All we have left to show is that the right hand sides of these expressions truly are Hermitian conjugates of one another. This is easy to see as follows. Starting with the formula for O : R and taking the conjugate we get

$$(O_R^{\dagger})^{\dagger} = \left(\alpha^T \mathcal{O}^{\dagger} (\alpha^{-1})^T\right)^{\dagger} \tag{3.79}$$

$$= (\alpha^{-1})^* \mathcal{O}\alpha^* \tag{3.80}$$

$$= (\alpha^{-1})^* \mathcal{O}\alpha^* \alpha^T (\alpha^{-1})^T \tag{3.81}$$

$$= (\alpha^{-1})^* \alpha^* \alpha^T \mathcal{O}(\alpha^{-1})^T \tag{3.82}$$

$$= \alpha^T \mathcal{O}(\alpha^{-1})^T \tag{3.83}$$

$$=O_R \tag{3.84}$$

where we used rO, α˚α T s " rO, ρ<sup>T</sup> TaT<sup>b</sup> s " 0 in going between the third and fourth steps.

### <span id="page-28-0"></span>3.5 Reconstruction as Teleportation or Active Quantum Error Correction

The QEC codes used to describe subregion-subregion duality in [\[16,](#page-55-3) [25,](#page-55-11) [26\]](#page-55-12) belong to the broad class of Erasure codes. These codes are passive QEC codes in that they do not involve an error diagnostic step after which a suitable recovery operation is implemented. It is assumed in these codes that one has prior knowledge of which subsystem is going to be corrupted and only then can the information about the code subspace (or a subalgebra) be recovered from its complement. This is naturally suited for the question of subregion-subregion duality in AdS/CFT.

The codes studied in this paper involve a recovery procedure which depends crucially on the details of the projection, PL, and must involve an active diagnostic step in order to determine which P<sup>L</sup> was acted with on the L subsystem[5](#page-29-0) . There are two equivalent ways of phrasing the recovery procedure: Either as quantum teleportation where knowledge of a measurement result on the entangled LR system in some basis P k L informs the correct teleportation protocol, or as an active QEC involving a diagnostic step on the already projected L subsystem to determine which P k <sup>L</sup> was acted with. This latter interpretation requires that we know before hand the basis of these 'errors' or projectors. To connect our codes to these interpretations, let's first focus on the case discussed in [3.3](#page-21-0) where the code subspace is completely recovered after the projection. Consider a message |ψy<sup>m</sup> P H<sup>m</sup> which we choose to encode into the code subspace as

$$|\psi\rangle_m|0\rangle_{LR} \to |0\rangle_m|\widetilde{\psi}\rangle_{LR}$$
 (3.85)

We keep general how much of the state |ψy can be decoded from L or R. Since our protocols allow for the information initially in L to be decoded from R, the teleportation should be thought as sending part of the message initially encoded in L to R. Then, we can append to our physical system an ancilla subsystem e which keeps track of the left measurement:

$$|\widetilde{\psi}\rangle_{LR}|0\rangle_e \to \sum_k P_L^k|\widetilde{\psi}\rangle_{LR}|k\rangle_e$$
 (3.86)

By measuring e we can determine which projection operator was acted on the physical system and then, assuming the P k L 's satisfy the conditions of the previous subsections, we can proceed to decode the information of the code subspace.

We can make this look like active quantum error correction by throwing out the information about the ancilla subsystem e. Considering a more general state ρr P Hcode Ă H<sup>L</sup> b HR, the evolution of the system is obtained by tracing out e to get

$$\widetilde{\rho} \to \mathcal{P} \circ \widetilde{\rho} \equiv \sum_{k} P_L^k \ \widetilde{\rho} \ P_L^k$$
 (3.87)

<span id="page-29-0"></span><sup>5</sup>We are grateful for discussions on this point with D. Poulin who demanded a more interesting example of QEC in AdS/CFT beyond passive erasure codes, and hope to have demonstrated such an example in this work.

This evolution is implemented by a quantum channel or a POVM with elements, or 'Kraus' operators,  $P_L^k$ . Assuming that each individual projection can be corrected in the sense of 3.3, we can write

$$\mathcal{P} \circ \widetilde{\rho} = \sum_{k} P_{L}^{k} \otimes \left[ U_{R} W_{\bar{R}_{b}}^{P_{k}} \left( \rho_{\bar{R}_{b}^{1} R_{b}} \otimes \chi_{\bar{R}_{b}^{2}} \right) W_{\bar{R}_{b}}^{P_{k} \dagger} U_{R}^{\dagger} \right]$$
(3.88)

Since the different projection operators are orthogonal, we can define a recovery channel with elements

$$R_m = P_L^m \otimes W_{\bar{R}_b}^{P_m \dagger} U_R^{\dagger} \tag{3.89}$$

where the projector on the L tensor factor is used to diagnose the error, and the other decodes the message. This clearly decodes the information successfully to give

$$\mathcal{R} \circ \mathcal{P} \circ \widetilde{\rho} = \rho_{\bar{R}_b^1 R_b} \otimes \chi_{\bar{R}_b^2} \tag{3.90}$$

where  $\rho_{\bar{R}_b^1 R_b}$  has the same matrix elements as  $\tilde{\rho}$ .

A similar diagnostic procedure can be implemented for the case presented 3.4 when only a subalgebra acting on the code subspace is preserved. The channel  $\mathcal{O}$  acting within the code subspace is preserved or recovered if we can find a corresponding channel  $\mathcal{O}^{\mathcal{R}}$  such that

$$\mathcal{P} \circ \mathcal{O} \circ \widetilde{\rho} = \mathcal{O}^{\mathcal{R}} \circ \mathcal{P} \circ \widetilde{\rho} \tag{3.91}$$

It's not hard to see that  $\mathcal{O}^{\mathcal{R}}$  composed of

$$\mathcal{O}_m^{\mathcal{R}} = P_L^m \otimes O_R^{P_m} \tag{3.92}$$

would ensure this, where the operator  $O_R^{P_m}$  is that constructed in the proof of theorem 3.4.1.

## <span id="page-30-0"></span>4 An Apologia for State Dependence

We discuss in this section the relation of this framework to previous proposals for the black hole interior [4–9], and address the objections of these proposals raised in [3, 14, 15, 43, 44] in light of this work. We also comment on the relation of our construction to ER=EPR [10] and provide a possible mechanism for transferring information between two black holes connected via a wormhole.

#### <span id="page-31-0"></span>4.1 Arguments Against State Dependence

We review some of the issues raised against state dependence in [3, 14, 15, 43, 44] and discuss how they are averted in our construction. Some of these points were already presented in [5], for example. All issues here will pertain to large pure black holes in AdS that have come into equilibrium with their Hawking radiation.

## $\widetilde{b}^\dagger$ and the Finite Density of States of the CFT / Typicality

As discussed in [3, 44], there is a conflict between the algerba of the boundary dressed interior creation and annihilation operators,  $\tilde{b}_w$  and  $\tilde{b}_w^{\dagger}$ , and the finite density of states of the dual CFT. The conflict is between the following two statements

$$[H, \widetilde{b}_w^{\dagger}] = -w\widetilde{b}_w^{\dagger} \text{ and } \left(\frac{1}{1 + \widetilde{b}_w^{\dagger}\widetilde{b}_w}\widetilde{b}_w\right)\widetilde{b}_w^{\dagger} = 1$$
 (4.1)

The first relation is the statement that  $\tilde{b}_w^{\dagger}$  lowers the energy of the CFT and is therefore a many-to-one map from the subspace of states of energy  $E_0$  to that of energy  $E_0 - w$ . This reduces the number of states by a factor of  $e^{-\beta w}$ , which is  $\mathcal{O}(1)$  for  $w \sim 1/\beta$ . This necessitates that  $\tilde{b}_w^{\dagger}$  cannot be an invertible map! However, the second statement shows precisely how the standard low energy QFT algebra ensures the existence of an inverse map.

As discussed in [5], this paradox is easily avoided by taking the interior operators to be state dependent. For example, the operator  $\tilde{b}_w^{\{s\}\dagger}$  associated to the microstate  $|B_s^{\beta}\rangle$  will not have the interpretation of a simple mode behind the horizon when acted on another microstate  $|B_s'^{\beta}\rangle$  where  $s \neq s'$ , and will most probably raise the energy of the boundary.

It is interesting to note that conflict does not arise for the the brane dressed versions of  $\tilde{b}_w^{\{s\}\dagger}$ , since those do not modify the energy of the boundary to leading order in N. Nevertheless, those operators as well are state dependent.

The argument from typicality is also averted by state dependence. In short, the typicality argument involves computing the microcanonical average at some large energy  $E_0$  of the Kruskal number operator  $N_A = a_w^{\dagger} a_w$  at the horizon in the basis of Schwarzschild mode number eigenbasis

$$\langle N_a \rangle_{E_0} = \sum_{n_b} \langle n_b | N_a | n_b \rangle \tag{4.2}$$

The microcanonical average is basis independent allowing us to choose this particular basis. Now, from the Bogoliubov transformation relating  $a_w$  and  $b_w$  it is clear that the expectation value of  $N_a$  is non-zero in any eigenstate of  $N_b$ , and therefore

$$\langle n_b | N_a | n_b \rangle \sim \mathcal{O}(1)$$
 (4.3)

The fact that N<sup>a</sup> is a positive operator ensures there are no cancellations. This result implies that typical states of the microcanonical ensemble have firewalls.

This argument breaks down for state dependent constructions because the operator N<sup>a</sup> is composed of interior operators and therefore is not a linear operator in the Hilbert space that one can simply take the average of. While the previous state dependent constructions want to ensure a smooth horizon for typical states [\[4–](#page-54-3)[6\]](#page-54-5), we take the perspective that there is no general statement that one can make about arbitrary typical states. We do show how an over-complete basis of typical looking states (where all exterior observables have thermalized) do not have singular horizons.

### The Frozen Vacuum and Violations of the Born Rule

Another objection to state dependent constructions is the inability of those constructions to find anything else other than the vacuum at the horizon [\[43\]](#page-57-0). This criticism does not apply to our construction since the nature of the horizon follows from that of the eternal wormhole prior to the projection, as in section [2.](#page-9-0)

Also, the requirement that all typical states have smooth horizons has been shown to lead to violations of the Born rule [\[14,](#page-55-1) [15\]](#page-55-2). In particular, it is shown how to construct two states, one without a firewall and one with, which are almost parallel in the Hilbert space. This again does not apply in our case since it is not a statement about typical states in general. Consider for example a smooth horizon state, say |B<sup>β</sup> s y, and a unitary U<sup>s</sup> which inserts a shockwave just behind the horizon that is dressed to the brane and therefore commutes with the Hamiltonian. We want to interpret the state Us|B<sup>β</sup> s y as a black hole with a firewall. Using the techniques of SYK and assuming that the U<sup>s</sup> is invariant under the diagonal spin group discussed in section [2,](#page-9-0) this overlap reduces to the one point function of a unitary V which inserts a shockwave in the TFD:

$$\langle B_s^{\beta} | U_s | B_s^{\beta} \rangle = \langle \beta | V | \beta \rangle \tag{4.4}$$

This is a one point function in the TFD state and is small if not zero.

## <span id="page-32-0"></span>4.2 Relation to State-Dependent Constructions of the Interior

We first give a quick review of state-dependent constructions of the interior following the formalism of [\[4–](#page-54-3)[6\]](#page-54-5) for definiteness. We will also comment on [\[7–](#page-54-6)[9\]](#page-55-13) which features aspects of QEC.

This proposal is concerned with reconstructing the interiors of large black holes in AdS that have come into equilibrium with their own Hawking radiation. The idea is to begin with a typical state |Ψ0y drawn from some microcanoncal ensemble at some high energy above the Hawking-Page transition [\[45\]](#page-57-2) of width that doesn't scale with 1{G<sup>N</sup> . Then one considers the algebra of simple operators O<sup>w</sup> P A, written here in fourier modes, dual to a set of low energy operators acting on the exterior of the black hole. A is not a closed algebra since it does not include operators composed of products of 1{G<sup>N</sup> simple operators or larger. This is then used to define a 'code subspace' spanned by elements Hcode " spantA|Ψ0yu. Such typical states |Ψ0y are also called 'equilibrium' states in that correlation functions of operators in A are given by their thermal expectation values, as expected from ETH [\[46–](#page-57-3)[48\]](#page-57-4). It is then argued that one expects the representation of A to be reducible in Hcode allowing for the existence of a nontrivial commutant A<sup>1</sup> of A. Using the theory of Tomita-Takesaki (see [\[49\]](#page-57-5) for a review), the interior operators <sup>O</sup>r<sup>w</sup> are identified as some subalgebra of <sup>A</sup><sup>1</sup> which satisfies the following conditions

$$\widetilde{\mathcal{O}}_w |\Psi_0\rangle = e^{-\frac{\beta H}{2}} \mathcal{O}_w^{\dagger} e^{\frac{\beta H}{2}} |\Psi_0\rangle \tag{4.5}$$

$$\widetilde{\mathcal{O}}_w \mathcal{O}_{w_1} ... \mathcal{O}_{w_n} |\Psi_0\rangle = \mathcal{O}_{w_1} ... \mathcal{O}_{w_n} \widetilde{\mathcal{O}}_w |\Psi_0\rangle$$
(4.6)

$$[H, \widetilde{\mathcal{O}}_w] \mathcal{O}_{w_1} ... \mathcal{O}_{w_n} |\Psi_0\rangle = w \widetilde{\mathcal{O}}_w \mathcal{O}_{w_1} ... \mathcal{O}_{w_n} |\Psi_0\rangle$$
(4.7)

(4.8)

The operators <sup>O</sup>r<sup>w</sup> are 'mirrored' versions of the exterior operators <sup>O</sup><sup>w</sup> defined by these conditions. This construction is motivated by the analogy to the TFD double state, which due to the entanglement between the left and the right sides we have

$$\mathcal{O}_L|\beta\rangle = e^{-\frac{\beta H}{2}}\mathcal{O}_R^{\dagger}e^{\frac{\beta H}{2}}|\beta\rangle$$
 (4.9)

for any O<sup>L</sup> and a corresponding OR. From these definitions one finds that correlation functions involving small numbers of operators from A Y A<sup>1</sup> are given by those in the thermal state, a signal taken to say that the region near the horizon is identical to that in eternal black hole. We therefore see that the construction produces an algebra of interior looking operators whenever observables composed of the simple exterior algebra have all thermalized.

The idea of the interior operators being related to the left operators is in the same spirit as the proposal of this paper. Indeed, the interior operators constructed via QEC satisfy a similar set of constraints as the mirror conditions above

$$_{L}\langle P|\mathcal{O}_{L}|\beta\rangle_{LR} = \widetilde{\mathcal{O}}_{R} \ _{L}\langle P|\beta\rangle_{LR}$$
 (4.10)

$$_{L}\langle P|\mathcal{O}_{L}\mathcal{O}_{R}^{1}...\mathcal{O}_{R}^{n}|\beta\rangle_{LR} = \mathcal{O}_{R}^{1}...\mathcal{O}_{R}^{n}\widetilde{\mathcal{O}}_{R} \ _{L}\langle P|\beta\rangle_{LR}$$
 (4.11)

where <sup>O</sup>r<sup>R</sup> " <sup>α</sup> <sup>T</sup>O pα ´1 q T as explained in the previous section. We also have that

$$0 = {}_{L}\langle P|[O_{L}, O_{R}]\mathcal{O}_{R}^{1}...\mathcal{O}_{R}^{n}|\beta\rangle_{LR} = \left[\widetilde{\mathcal{O}}_{R}, O_{R}\right]\mathcal{O}_{R}^{1}...\mathcal{O}_{R}^{n} {}_{L}\langle P|\beta\rangle_{LR}$$
(4.12)

which is just the statement that operators which commute in the unprojected code subspace continue to commute after the projection (assuming both satisfy the recoverability condition of section [3.4\)](#page-25-0). The commutator with the Hamiltonian condition also follows, but it depends on whether the interior operator is dressed to the brane or boundary, where it will respectively either commute or not.

There are crucial differences though. An obvious one is that the mirroring procedure does not preserve the Hermiticity property of the operators; Hermitian conjugate pairs do not mirror into Hermitian conjugate pairs. In our discussion, this was guaranteed by QEC and proven in section [3.4.](#page-25-0) It's not clear how much of a problem this is (if at all), but one might worry that since positive operators do not mirror to positive operators in the interior, observables such as the number operator might produce unphysical results in the interior.

The mirroring procedure is reliant on considering an equilibrium state for which all low energy external observables have thermalized. This was not necessary for our construction; we found that we can determine the dictionary both for atypical states of section [1](#page-6-0) by projecting on the TFD and for typical states obtained by acting with a series of OTO shockwaves prior to the projection.

Another issue with the mirror construction is that the nature of the interior is determined by the construction rather than by the considered equilibrium state. This was discussed in the previous subsection with regards to the frozen vacuum objection. In our construction the nature of the horizon is predetermined, in part, by the state of the two sided wormhole prior to the projection. We could for instance consider a state which contains a shockwave which skims the horizon from the left hand side and then act with the left projection, just like those in figure [2.](#page-9-0) In these long wormholes, the right external operators are not sensitive to any of the left shockwaves and, as argued above, will look completely thermalized making such a state indistinguishable from an equilibrium state. Therefore one can carry out the mirroring procedure in this case. However, the actual boundary dual of interior operators will be sensitive to this shockwave while the mirror construction would entirely miss it.

Finally we comment on the use of QEC in [\[7–](#page-54-6)[9\]](#page-55-13) and how it connects to the proposal of this paper. They consider a young black hole not yet maximally (or thermally) entangled with its Hawking radiation and track its state as it emits a single quantum of radiation:

$$|\Psi\rangle_B|0\rangle_R \to \sum_i E_i|\Psi\rangle_B|i\rangle_R$$
 (4.13)

where the state of B belongs to a direct sum of Hilbert spaces of black holes of different masses, and R is the external radiation Hilbert space initialized in the vacuum state |0yR. This evolution is a unitary transformation acting on the BR system, and therefore the operators <sup>E</sup><sup>i</sup> must satisfy <sup>ř</sup> i E : <sup>i</sup> E<sup>i</sup> " 1. Upon tracing out R, this evolution looks like the action of an error channel

$$\mathcal{E}(|\Psi\rangle_B\langle\Psi|) = \sum_i E_i |\Psi\rangle_B\langle\Psi|E_i^{\dagger}$$
(4.14)

Just as in the mirror construction, the goal here is to be able to find the subsystem of B that the radiation state is entangled with and identify it with interior partner Hawking mode. The key result of their work is that if one assumes that this error channel is correctable, i.e. the existence of recovery channel such that

$$\mathcal{R} \circ \mathcal{E} (|\Psi\rangle_B \langle \Psi|) \propto |\Psi\rangle_B \langle \Psi| \tag{4.15}$$

then one can algorithmically find a subsystem of B which behaves in the appropriate way to mimic the interior Hawking partner. As in standard QEC, this recovery procedure can be implemented on a subspace of states of HB, i.e. a code subspace. The recoverability condition becomes xm|E : <sup>i</sup> E<sup>j</sup> |ny 9 δmn for any states |my and |ny in the code subspace. However, this proposal again suffers from the same ambiguity issues raised above.

It should therefore be clear that the usage of QEC in this paper and in [\[7–](#page-54-6)[9\]](#page-55-13) is different, though both involve the standard quantum information framework of QEC. The origin of QEC in this paper is the interpretation of the AdS/CFT dictionary as a QEC code. Take for example the discussion of section [3.2.](#page-14-0) The representation of the dictionary as a set of tensors, along with the encoding and decoding procedure of going from the bulk legs to the boundary and back, has been proposed as a toy model for the AdS/CFT dictionary by, for example, [\[41,](#page-56-14) [42\]](#page-56-15). The goal of the present work was to study how this dictionary is rewired by the application of the projection operator on a subsystem of the boundary.

Nevertheless, it is our view that the proposal of this paper should be viewed as a realization of the general ideas of state-dependent constructions but with more rules so as to stave off some of their inherent ambiguities.

## <span id="page-35-0"></span>4.3 Monogamy of Entanglement and ER=EPR

Next, we engineer situations to satisfy the preconditions of the monogamy of entanglement argument for firewalls [\[1,](#page-54-0) [50,](#page-57-6) [51\]](#page-57-7) and see how it affects the nature of the horizon. We will do this by either explicitly considering an entangled state of a set of black hole microstates and some external system or by picking a certain microstate and allowing it to evaporate.

Consider first the set of 2<sup>N</sup>{<sup>2</sup> black hole microstates |B<sup>β</sup> s yR, labeled by s, of an SYK system R all of which have smooth horizons. This is an overcomplete basis of black hole microstates of effective inverse temperature β. As discussed in section [3,](#page-13-0) the dictionary between the bulk and boundary is understood for both the exterior modes, b, and interior modes a, where the dictionary of the latter is state dependent.

Next, we want to consider entangling R with an external system E, which could be another SYK system, in a state |ΨyRE such that the reduced density matrix of R is thermal. This is supposed to mimic an evaporating black hole that has reached the Page time [\[52,](#page-57-8) [53\]](#page-57-9) and is thermally entangled with its Hawking radiation. Up to a product unitary U<sup>R</sup> b U<sup>E</sup> on the two systems, a general such state is

$$|\Psi\rangle_{RE} = \sum_{s} |B_s^{\beta}\rangle_R |Q_s\rangle_E \tag{4.16}$$

where <sup>E</sup>xQs|Q<sup>s</sup> <sup>1</sup>y<sup>E</sup> " δss<sup>1</sup>. We can check that the reduced density matrix of R is thermal by explicit computation

$$\rho_R = \sum_s |B_s^{\beta} \rangle \langle B_s^{\beta}| \tag{4.17}$$

$$= e^{-\frac{\beta}{2}H} \sum_{s} |B_s\rangle \langle B_s|e^{-\frac{\beta}{2}H}$$
(4.18)

$$=e^{-\beta H} \tag{4.19}$$

as required. The von Neumann entropy of ρ<sup>R</sup> expressed in bulk quantities is

$$S(\rho_R) = \frac{A}{4G_N} + S_{bulk}(\rho_b) \tag{4.20}$$

where ρ<sup>b</sup> is the density matrix of the bulk quantum fields b. Before we justify this result, we point out that it would satisfy the preconditions of the firewall argument, namely that both the black hole horizon and the external modes b are entangled with the external system E. By monogamy of entanglement, this would preclude b from being entangled with the interior modes a.

Saying that we now have a firewall is too quick. The reason being that we can take the external system to be another SYK and write its states as

$$|Q_s\rangle_E = V_E|B_s\rangle_E \tag{4.21}$$

for some unitary VE, since the states that appear on both sides of this equation are an orthogonal set. Therefore the entangled state between R and E is simply

$$|\Psi\rangle_{RE} = V_E \sum_s |B_s^{\beta}\rangle_R |B_s\rangle_E \tag{4.22}$$

$$=V_E|\beta\rangle_{RE} \tag{4.23}$$

which is just a unitary transformation acting on one boundary of the standard TFD. We see that we have the reverse of the puzzle described in 3.1; the modes a were initially encoded on R but have somehow transferred to E. The dictionary has been rewired by the entanglement so that a is now reconstructable in E. Modulo the unitary  $V_E$ , the bulk system b continues to be purified by a, and their entanglement contributes to the von Neumann entropy of  $\rho_R$  in the form of the FLM piece  $S_{bulk}(\rho_b)$ . Whether there is a firewall or not is determined by the unitary  $V_E$ . This demonstrates how the fluidity of the dictionary in response to the entanglement realizes the ideas of ER = EPR [10]. We got this by basically going through the SYK projected microstate construction but backwards.

This fluidity can be used to transfer information from R to E by means of entanglement. The basic idea is that prior to entangling R with E, we first encode some information in the interior of the pure black hole microstates of R in the modes a via a state dependent unitary

$$|B_s^{\beta}\rangle_R \to U_s^R |B_s^{\beta}\rangle_R$$
 (4.24)

This unitary produces the same density matrix for the bulk fields a for all s. Note that this is not a single unitary acted on all the different  $|B_s^{\beta}\rangle_R$  but a different one for each state. Entangling these states with the external SYK, but with  $V_E = \mathbb{I}_E$ , it's not hard to see that we will get

$$|\Psi\rangle_{RE} = U^E |\beta\rangle_{RE} \tag{4.25}$$

where  $U^E$  is a truly unitary operator and acts within the code subspace of the eternal black hole on the bulk subsystem a. We see that the shift in the dictionary allows us to decode the new state of a from the system E only.

Now, it is a reasonable objection to say that we have not really transferred information from R to E, since the encoded information in R was not encoded by a single state independent unitary. Nevertheless, we will now provide a more convincing demonstration of the connection between the transfer of information and the fluidity of the dictionary. We will do this in a series of steps below, but will leave the complete quantitative analysis for future work.

#### Throwing Information into the Black Hole

Consider starting with the TFD state of two SYK systems L and R. We can inject some information via a unitary on R at some early time, which proceeds to fall into the black hole.

$$U_R(t_I)|\beta\rangle_{LR} \tag{4.26}$$

This unitary increases the energy of the right system slightly and takes it out of thermal equilibrium, without changing its von Neumann entropy. After the state thermalizes, it will reach a state where its coarse grained thermal entropy is larger than its von Neumann entropy. We call this difference δS.

## Evaporation (1/2): Tracking the Trajectory of the Boundary Particle

Consider then coupling the R SYK to an external auxilliary system X assumed to be at a lower temperature than 1{β so that energy flows from R into X. There are two effects to turning on this coupling which occur in the following sequence. The first is an initial increase of energy of both systems R and X, and then a transfer of energy from R into X.

The initial increase of the energy is explained in appendix [B,](#page-52-0) and has to do with the fact that, at early times, the leading order effect on the energy comes from the second order contribution in the coupling. Following this initial spike, the energy starts to leak from system R into system X. A good way to model the energy transfer out of the R SYK system is by setting absorbing boundary conditions on the bulk stress tensor along the right boundary [\[54\]](#page-57-10). In the Schwarzian limit of SYK, the change of energy and the flux of energy at infinity of a massless bulk scalar field theory are related via via

$$\frac{dM}{du} = t^2 T_{tz} \tag{4.27}$$

where t, z are bulk Poincare coordinates and u is the boundary time. The energy of R is determined by the boundary trajectory tpuq as

$$M = -\frac{\phi_r}{8\pi G_N} \{t, u\} \tag{4.28}$$

where φ<sup>r</sup> is the 'renormalized' value of the dilaton, or the coefficient of the growing factor in the bulk dilaton profile as the boundary is approached.

As discussed in [\[54\]](#page-57-10), the bulk stress energy due to the Hawking radiation is generated from the conformal anomaly. The relation between the Poincare stress tensor and that due to the black hole is

$$T_{y^{\pm}y^{\pm}} = (\partial_{y^{\pm}}x^{\pm})^{2}T_{x^{\pm}x^{\pm}} + \frac{c}{12}\{x^{\pm}, y^{\pm}\}$$
 (4.29)

where x ˘ " t˘z. The conformal transformation is x ˘ " x ˘py ˘q where py ` `y ´q{2 " u is the boundary proper time. c is the central charge of the bulk quantum field theory. The absorbing boundary conditions, in the two coordinate systems, are

$$T_{y^+y^+} = \frac{c}{12} \{x^+, y^+\}, \quad T_{y^-y^-} = 0$$
 (4.30)

$$T_{x^+x^+} = 0, \quad T_{x^-x^-} = -(\partial_{y^-}x^-)^{-2}\frac{c}{12}\{x^-, y^-\}$$
 (4.31)

And therefore, the energy flux on the boundary is

$$T_{tz} = \frac{c}{48} (t')^{-2} \{t, u\}$$
(4.32)

This is a negative energy flux falling into the bulk. The energy then satisfies

$$\frac{d}{du}\{t, u\} = -\frac{\pi cG_N}{6\phi_r}\{t, u\}$$
(4.33)

This can be solved [54] for t(u) to show that the boundary particle receives a (continuous) series of kicks away from the center of the bulk.

The final precise trajectory of the boundary particle resulting from these two effects depends sensitively on the details of the coupling to the external system. Nevertheless, it is plausible to anticipate that the total effect is to push the boundary particle outwards towards the global AdS<sub>2</sub> boundary such that it hits the boundary at an earlier time than the unperturbed situation. We know for sure that it cannot extend beyond this point as that would allow the left SYK to transmit signals to the right. This would be ensured by the bulk ANEC. It would be interesting to understand the principle on the boundary dual to this<sup>6</sup>.

#### Evaporation (2/2): Tracking the Energy and Entanglement Entropy of R

The energy as a function of u solves to an exponentially decreasing function of time

$$M(u) = M(u_0)e^{-k(u-u_0)} (4.34)$$

where  $k = \frac{\pi cG_N}{6\phi_r}$  and  $u_0$  is the time the absorbing boundary conditions are turned on. Taking k to be small, we can assume the evaporation to be quasi-adiabatic and continue to use the thermodynamic relations between energy, entropy, and temperature. From the energy temperature relation

$$M = 2\pi^2 \frac{\phi_r}{8\pi G_N} T^2 \tag{4.35}$$

<span id="page-39-0"></span><sup>&</sup>lt;sup>6</sup>I thank D. Stanford for discussions on this point.

![](_page_40_Figure_0.jpeg)

<span id="page-40-0"></span>Figure 9. Behavior of various entropies as a function of boundary time u. The blue curve represents the thermal evolution of the thermal entropy of R computed from the total mass of the black hole, and represents the maximum possible entanglement entropy of R. The red curve is the evolution of the entanglement entropy as R leaks energy into X, assuming maximal such transfer.

the temperature as function of time is found to be

$$T(u) = T(u_0)e^{-\frac{k}{2}(u-u_0)}$$
(4.36)

The thermal entropy as a function of time is

$$S_{th}(u) = S_0 + 4\pi^2 \frac{\phi_r}{8\pi G_N} T(u)$$
(4.37)

$$= S_0 + (S_{th}(u_0) - S_0)e^{-\frac{k}{2}(u - u_0)}$$
(4.38)

This thermal entropy is a decreasing function of time and can be thought of as the maximum value of entanglement entropy given the energy Mpuq.

The insertion of the message at early times increases the energy, and therefore the von Neumann entropy of R differs from its thermal entropy by δS,

$$S_{ent}(u_0) = S_{th}(u_0) - \delta S$$
 (4.39)

As the black hole evaporates, we can model the increase of the entanglement entropy by the decrease of the thermal entropy, which follows from the usual state of Hawking radiation. Again, assuming quasi-adiabatic evaporation we can write

$$\Delta S_{ent}(u) = -\Delta S_{th} = -\int_{u_0}^{u} \frac{dE(u)}{T(u)} = \left(S_{th}(u_0) - S_0\right) \left(1 - e^{-\frac{k}{2}(u - u_0)}\right)$$
(4.40)

where now we have

$$S_{ent}(u) = S_{ent}(u_0) + \Delta S_{ent}(u) \tag{4.41}$$

$$= S_{th}(u_0) - \delta S + \left(S_{th}(u_0) - S_0\right) \left(1 - e^{-\frac{k}{2}(u - u_0)}\right)$$
(4.42)

Just as in the standard Hawking evaporation in any dimension, the analogous relation obtained from the usual Hawking process is only trustworthy until around the Page time. This is the time when the thermal entropy of the system is equal to its entanglement entropy,

$$S_{th}(u_{Page}) = S_{ent}(u_{Page}) \tag{4.43}$$

This time is

$$u_{Page} = u_0 - \frac{2}{k} \ln \left[ 1 - \frac{\delta S}{2(S_{th}(u_0) - S_0)} \right]$$
 (4.44)

$$\approx u_0 + \frac{12}{c} \frac{\delta S}{T(u_0)} \tag{4.45}$$

Which is a short time for  $\delta S \sim \mathcal{O}(1)$ . Starting at this time, the thermal entropy of the black hole will be equal to its entanglement entropy. This will be given by the area of the new horizon of the smaller black hole, which therefore becomes the RT surface for the entire system R. We expect this to follow since the density matrix of R approaches the thermal state. See figure 9.

#### Deposit the Extracted Energy of R from X into L

After transferring energy from system R to X, the state of LR is no longer pure. We gain extra information about the nature of this state by evolving both systems using the original time independent Hamiltonians to the far future and far past. We expect that the right boundary particle will, again, hit the global boundary prematurely. This will result in a new horizon for R that must be its new RT surface since  $\rho_R$  is (almost) thermal. This is shown in the third diagram of figure 10. The bulk dual of the LR system will then contain two RT surfaces, one for each boundary. These are the surfaces (points)  $A_L$  and  $\widetilde{A}_R$ , which do not coincide.

Consider now depositing the energy extracted from R into L by means of a unitary acting on LX. We imagine that this process can be done in a quasi-adiabatic way on L so as to not modify the bulk picture drastically. This process will not alter the density matrix of R, and therefore  $\widetilde{A}_R$  will continue to be its RT surface. After this process is complete, the state of LR will be pure and the RT surfaces of the two boundaries will coincide on  $\widetilde{A}_R$ .

<span id="page-42-0"></span>![](_page_42_Picture_0.jpeg)

Figure 10. The left most diagram (I) represents dropping a message (green) into the TFD of LR. The second (II) represents the extraction of energy from R, represented here by the some initial positive energy (red) followed by negative energy (blue) and some final positive energy due to switching off the interaction (red). In the third diagram (III), the right system is evolved using a time independent Hamiltonian. Here the space time has two RT surfaces (points),  $A_L$  and  $\tilde{A}_R$  for the L and R respectively. In the last diagram (IV) the RT surfaces coincide again but at the new location of  $\tilde{A}_R$ . The initial message is in the entanglement wedge of the L (but outside its causal wedge).

Something interesting has just happened. The message sent into R at early times is now contained within the entanglement wedge of L, and thereby reconstructable from L. We see that the fluidity of the dictionary under entanglement transfer has been rewired the dictionary precisely such that information initially in R is now contained in L. We note the parallel here between this information transfer and the Hayden-Preskill criterion for the decoding a message from the Hawking radiation [37]. Here we view R as the black hole and L as the Hawking radiation, and the TFD as the system at the Page time. Then, after throwing in a new message, we have to wait for some extra time for qubits to transfer from R to L until R becomes maximally entangled with L, at which point the message can be decoded from L.

A similar observation can be made for an evaporating pure large black hole in  $AdS_2$ , although there is a subtlety due to its ground state entropy. As reviewed earlier, for this black hole to reach the Page time it must build up its entanglement entropy until it coincides with its thermal entropy  $S_{th}(T) = S_0 + CT$ , where C is some constant. However, since the rate of evaporation is controlled by the temperature,  $\dot{M} \sim T^2$ , it is clear that the black hole can only evaporate away a  $CT_{\text{initial}}$  amount of entropy, and therefore will never become thermally entangled with the auxiliary system<sup>7</sup>. Naively,

<span id="page-42-1"></span><sup>&</sup>lt;sup>7</sup>Since the ground state degeneracy is actually lifted by the SYK interactions, the black hole will actually evolve to the Page time provided we wait long enough. However, the Schwrazian description is expected not to be valid for such long times.

![](_page_43_Picture_0.jpeg)

Figure 11. The projected tensor network can be viewed as a circuit which prepares the state of the right boundary R assuming some inputs from the bulk a and b and starting from a very simple state P on the left (a product state of spins). The top figure corresponds to projecting on the thermofield double which gives a relatively short tensor network and therefore prepares a low complexity state on R. The bottom figure shows a long tensor network which prepares a complex state for large n (the number of tensors).

<span id="page-43-1"></span>one might have thought possible to consider large temperatures such that CTinitial ą 2S0, though this is not the case since then Sth would exceed the total number of states of the SYK system; for large q, S<sup>0</sup> " N ln 2 ´ Nπ<sup>2</sup> {4q <sup>2</sup> ` ... [\[31,](#page-56-4) [55\]](#page-57-11) and the total number of states in the SYK model is 2<sup>N</sup>{<sup>2</sup> .

This subtlety can be avoided by adding another process which continuously adds pure matter into the evaporating black hole so as to keep its temperature constant. The entanglement via the Hawking process will continue to increase and the combined effect of the added matter and the evaporation will push the boundary particle outwards towards the global AdS<sup>2</sup> boundary. Just as in the wormhole example, a message thrown in at early times will escape the new RT surface generated by the build up of entanglement. In order to retrieve the information, one can imagine depositing the extracted energy into another SYK system, L, and, up to a unitary on this system alone, the dual spacetime can be made to look like a wormhole with the message located in the entanglement wedge of L.

### <span id="page-43-0"></span>4.4 Comments on Complexity

We comment here on the connections with the idea of holographic computational complexity [\[56–](#page-57-12)[59\]](#page-57-13). It is interesting to note the difference of complexity between the typical and atypical black hole microstates considered in section [2](#page-5-0) and how that depends on the details of the projector. The projection operator |BsyxBs| projects the left SYK

![](_page_44_Picture_0.jpeg)

Figure 12. Projecting on the left SYK with a complicated but fine tuned projector <sup>P</sup><sup>r</sup> projects a chosen set of bulk internal indices into a simple state P. To estimate the complexity of the right SYK R we only need to count the number of tensors between it and the simple projector, which in the presented case is n ´ k ` 1 tensors.

onto a simple product state of spins - a state of low complexity. The resulting state of the right SYK is the Euclidean time evolution of this product state by an amount β{2

$$|B_s^{\beta}\rangle = e^{-\frac{\beta}{2}H}|B_s\rangle \tag{4.46}$$

Assuming that β " Op1q, we will take this evolved state to be roughly of the same complexity as the product state, that is both are simple[8](#page-44-0) . Moreover, the simplicity of this state can be deduced from the relatively short projected tensor network, which can be viewed as that which prepares the state of R starting with a simple state of P.

Projecting a long wormhole supported by left OTO shockwaves waves does not produce such a simple state. As shown in figure [11,](#page-43-1) projecting on a long wormhole constructed by n OTO shockwaves results in a tensor network composed of roughly n tensors. Each tensor is generated by sandwiching the insertion of a local operator, the shockwave, by Hamiltonian evolution of a scrambling time. Taking into account the partial cancellation between the forward and backward time evolution, we can estimate the complexity of each tensor as N, the number of spins in SYK, and therefore the total complexity of these states is roughly n ˆ N[9](#page-44-1) [\[56–](#page-57-12)[59\]](#page-57-13).

Counterintuitively, it turns out that projecting on the left SYK with a more complicated state of the spins can result in a simpler state of R. The caveat is that this more complicated projector needs to be fine tuned with respect to the bulk tensors. A

<span id="page-44-0"></span><sup>8</sup>Euclidean evolution generically takes all states to the vacuum, assuming we evolve for long enough, and therefore tends to a complexity decreasing transformation.

<span id="page-44-1"></span><sup>9</sup> In a previous draft we forgot to take into account the partial cancellation between the forward and backward time evolution and concluded the complexity of each tensor to be ln N. We thank Ying Zhao for pointing this out to us.

demonstration of this is to start with a long tensor network where we can fine tune the projector to any given number of bulk tensors and shorten the network to any length that we desire, up to the horizon[10](#page-45-1). The key is to find the left projector which projects the bulk internal legs between a given pair of tensors into a simple state. In the situation where the black hole is lengthened by a series of OTO shockwaves, this can be easily achieved by picking a projector which undoes these shockwaves. It would be interesting to understand this in the more general setup where the lengthening procedure is not so simple.

## <span id="page-45-0"></span>5 Conclusion

The goal of this paper was to understand the dictionary for operators inside the horizon of pure black hole microstates. We considered such microstates in the SYK model which are prepared by starting with the thermofield double, dual to the eternal black hole, and completely projecting out one of the boundaries [\[34\]](#page-56-7). The dual of this projection is to insert an end-of-the-world brane near the projected boundary which falls into the black hole. This prepares an overcomplete set of black holes all of which are firewall-free.

We argued that this preparation process would naively create a firewall at the bifurcation surface. The point was that the entanglement of the bulk fields across the horizon contributes to the entanglement entropy between the two boundaries [\[29\]](#page-56-2), and one might worry that breaking the latter would necessarily break the former. This would naively follow from subregion-subregion duality which says that the density matrix of the bulk fields on the left/right can be recovered from the density matrix of the left/right boundary.

Nevertheless, we showed that the quantum error correction interpretation of the duality avoids this conclusion by giving the AdS/CFT dictionary an interesting kind of fluidity. We showed how the (say left) projection causes a rewiring of the dictionary so as to map bulk operators originally dual to the left boundary to the right. This establishes a dictionary for operators behind the black hole horizon.

This dictionary was found to have the interesting feature that it depends on the projection operator used. This is reminiscient of previous state-dependent proposals of reconstructing the black hole interior [\[4](#page-54-3)[–9,](#page-55-13) [11–](#page-55-14)[13\]](#page-55-0). We comment that a key difference between this work and these proposals is that our construction first considers a bulk state where the nature of the horizon is known and then finds the dictionary, while the previous proposals begin with a boundary equilibrium state and then constructs a

<span id="page-45-1"></span><sup>10</sup>The reason we can't go past the horizon in these tensor network models is that the horizon acts as a bottleneck and thus only the bulk legs to its left (internal legs included) map isometrically to the left boundary. Similarly, all bulk legs on the right of the horizon map to the right boundary.

![](_page_46_Picture_0.jpeg)

Figure 13. The state of an evaporating black hole is dual to a longer and longer wormhole, with ever changing RT surface. The blue dot is the new RT surface for the now smaller black hole.

<span id="page-46-0"></span>subalgebra on the boundary for which the black hole horizon looks smooth. We show that one can construct an explicit example of a black hole that looks to be completely thermalized (an equilibrium state) from the exterior but which has a 'firewall' just behind the horizon which these state-dependent constructions would entirely miss.

We also preformed a preliminary analysis of how to utilize the fluidity of the dictionary to transfer information between two black holes connected by a wormhole. By starting with two SYKs in the TFD state, we showed that extracting energy from one boundary and dumping it in the other causes the RT surface to shift to a new surface of smaller area that is spacelike related to the original RT surface and positioned between it and the boundary. That there should be a new RT surface of smaller area follows because the temperature of the evaporating black hole is decreasing and so must its entanglement entropy, and therefore the original RT surface would suggest a larger entropy than is allowed by thermodynamics. We showed how this implies that a message sent in at early times from the evaporating side ends up within the entanglement wedge of the growing side and thereby becomes reconstructable from the other boundary. This occurs once the evaporating side has reached the Page time, when its entanglement entropy equals its thermal entropy.

We also argued for the analogous effect for the case of starting with a pure large black hole in AdS and allowing it to evaporate. We can engineer the situation so that the black hole reaches the Page time and becomes thermally mixed with some external system. Once again, a message sent in at early times will be located outside the newly generated RT surface, and therefore will not be reconstructable on the original system. The principle in play in both of these examples is that a black hole allowed to evaporate via a generic non-fine-tuned process will have its event horizon coincide with its RT surface by the Page time. This presents a new picture of the evolution of the spacetime as a black hole evaporates shown in figure [13.](#page-46-0)

We also commented on how the choice of the left projector determines the complex-

ity of the resulting state on the right. By focusing on the tensor network representation of LR system and projecting on L, we argued that the resulting tensor network can be viewed as the quantum circuit which prepares the state of R and from which the complexity of the state can be estimated.

## Acknowledgments

I would like to thank Juan Maldacena for the many illuminating discussions which led to this work, and Douglas Stanford for being a constant resource along the way. I would also like to thank William Donnelly, Patrick Hayden, Nima Lashkari, Raghu Mahajan, Geoffrey Penington, David Poulin, Xiao-liang Qi, Herman Verlinde, and Ying Zhao for discussions. I are grateful to the KITP Program Quantum Physics of Information (Sep 18 - Dec 15, 2017), where some part of the work was performed. This research was supported in part by the National Science Foundation under Grant No. NSF PHY17-48958.

## <span id="page-47-0"></span>A Bulk Particle Gravitational Dressing

Let's begin by listing a set of coordinates for AdS2:

$$Y^{-1} = \frac{\cos t}{\sin \sigma} = \cosh r \tag{A.1}$$

$$Y^{0} = \frac{\sin t}{\sin \sigma} = \sinh r \sinh \tau \tag{A.2}$$

$$Y^{1} = -\frac{\cos \sigma}{\sin \sigma} = \sinh r \cosh \tau \tag{A.3}$$

Which are the embedding, global, and Rindler coordinates respectively. The metrics are the following

$$ds^{2} = -(dY^{-1})^{2} - (dY^{0})^{2} + (dY^{1})^{2}, Y^{2} = -1$$
(A.4)

$$ds^2 = \frac{-dt^2 + d\sigma^2}{\sin^2 \sigma} \tag{A.5}$$

$$ds^2 = dr^2 - \sinh^2 r \ d\tau^2 \tag{A.6}$$

The trajectory of a massive particle is completely determined by the condition

$$Y \cdot Q = 0 \tag{A.7}$$

For a particle that sits in the center of the bulk the charge is given by

$$Q_{center}^a = (0, 0, -m) \tag{A.8}$$

Via an SL2 transformation we can push this particle to any massive geodesic. The most general form for the charge of such a particle is

$$Q^{a} = m(\sinh \gamma \sin \theta, \sinh \gamma \cos \theta, -\cosh \gamma)$$
(A.9)

where γ can be thought of as a rapidity determining the velocity of the particle when it passes the center of the bulk, and θ controls the shift of the trajectory in bulk global time. The trajectory of the particle in embedding coordinates is

$$Y^{-1} = \cos\theta \cos T + \sin\theta \cosh\gamma \sin T \tag{A.10}$$

$$Y^{0} = -\sin\theta\cos T + \cos\theta\cosh\gamma\sin T \tag{A.11}$$

$$Y^{1} = -\sinh\gamma\sin T\tag{A.12}$$

where T is some time parameter along the trajectory.

The brane of [\[34\]](#page-56-7) reaches the boundary at bulk time t " τ " 0. In embedding coordinates this is

$$Y^{-1} \to \infty \tag{A.13}$$

$$Y^0 = 0 \tag{A.14}$$

$$Y^1 \to -\infty \tag{A.15}$$

We then deduce the values of θ and γ to be

$$\gamma \to \infty$$
 (A.16)

$$\theta = \frac{\pi}{2} \tag{A.17}$$

and embedding time parameter

$$T = \frac{\pi}{2} \tag{A.18}$$

This is the embedding proper time at which the particle is a maximum |Y 1 |.

Next we turn to the bulk particle. For a particle to fall into the black hole from the left exterior we have

$$0 < \gamma < \infty \tag{A.19}$$

$$0 < \theta < \pi \tag{A.20}$$

The first condition ensures that the particle is neither at rest nor falling in at the speed of light. The second ensures the particle falls in from the left exterior by guaranteeing that the largest radial position of the particle (the point where  $T = \frac{\pi}{2}$ ) occurs within  $-\frac{\pi}{2} < t < \frac{\pi}{2}$ , where t is the bulk global time. At this point t and  $\theta$  are related via

$$t = \frac{\pi}{2} - \theta \tag{A.21}$$

Now we consider the boundary particle. It's trajectory is fixed by the condition

$$Y \cdot Q = -q \tag{A.22}$$

for some q. It turns out that Q is proportional to the location of the bifurcation point in embedding coordinates. We have been working in the gauge where the bulk t=0 slice corresponds to the  $Y^0=0$  slice in embedding coordinates. Therefore, we can ensure the bifurcation point also rests on this slice by picking the charge to be

$$Q_{R_{\hat{\sigma}}}^a = (\sqrt{E}, 0, 0) \tag{A.23}$$

where  $R_{\partial}$  is the label for the right boundary particle. Assuming for now that we have the thermofield double, we would require another boundary particle for the left side whose charge must be

$$Q_{L_2}^a = (-\sqrt{E}, 0, 0) \tag{A.24}$$

by the requirement  $Q_{L_{\partial}}^{a} + Q_{R_{\partial}}^{a} = 0$ . The energy as measured on the right boundary is simply the square of the charges

$$H = -Q_{R_{\partial}}^2 = E \tag{A.25}$$

before considering the brane, we can study how the charges and trajectories of the TFD get modified by the presence of a bulk particle. The bulk particle charge is

$$Q_{Bp}^{a} = m(\sinh \gamma \sin \theta, \sinh \gamma \cos \theta, -\cosh \gamma)$$
 (A.26)

And we need to satisfy

$$Q_{L_{\partial}}^{a} + Q_{R_{\partial}}^{a} + Q_{Bp}^{a} = 0 (A.27)$$

There are obviously an infinite number of ways to do this, and they correspond to how the bulk particle is dressed to either boundary. Two interesting cases is when the particle is either entirely dressed to the right:

$$Q_{R_{\partial}}^{a} = (\sqrt{E} - m \sinh \gamma \sin \theta, -m \sinh \gamma \cos \theta, m \cosh \gamma)$$
 (A.28)

$$Q_{L_{\hat{\sigma}}}^{a} = (-\sqrt{E}, 0, 0) \tag{A.29}$$

or entirely to the left

$$Q_{R_{\hat{\sigma}}}^{a} = (\sqrt{E}, 0, 0) \tag{A.30}$$

$$Q_{L_{\hat{\sigma}}}^{a} = (-\sqrt{E} - m\sinh\gamma\sin\theta, -m\sinh\gamma\cos\theta, m\cosh\gamma)$$
 (A.31)

The final thing to show in the context of the TFD is how the bulk matter affects the boundary particle trajectory. I will show that independent of  $\theta$ , which exterior the bulk particle emerges into, the boundary particle is pushed towards the global boundary and hits it sooner compared to the no bulk particle case. In the case with no bulk particle, the boundary particle trajectory is bounded between the global bulk times

$$-\frac{\pi}{2} \leqslant t \leqslant \frac{\pi}{2} \tag{A.32}$$

The goal is to show that the modified trajectory is bounded by as

$$-\frac{\pi}{2} < t_{-} \le t \le t_{+} < \frac{\pi}{2} \tag{A.33}$$

where the  $t_{-}$  and  $t_{+}$  are the new boundary times which the boundary particle approaches. To see this, we have to note that the boundary particle trajectory requires that  $Y \cdot Q$  be a constant. The idea is that by taking the boundary limit while keeping this quantity fixed we should find that the global time approaches a certain value. Recall that we can reexpress the embedding coordinates in terms of global coordinates as

$$Y^{-1} = \frac{\cos t}{\sin \sigma} \tag{A.34}$$

$$Y^{0} = \frac{\sin t}{\sin \sigma}$$

$$Y^{1} = -\frac{\cos \sigma}{\sin \sigma}$$
(A.35)

$$Y^{1} = -\frac{\cos \sigma}{\sin \sigma} \tag{A.36}$$

All of which diverge at the same rate as  $\sigma \to \pi$ . Therefore we find the condition that

$$-Q^{-1}\cos t - Q^0\sin t + Q^1 = 0 (A.37)$$

where

$$Q^{a} = (\sqrt{E} - m \sinh \gamma \sin \theta, -m \sinh \gamma \cos \theta, m \cosh \gamma)$$
(A.38)

In the case with no bulk particle we have  $Q^a = (\sqrt{E}, 0, 0)$  and therefore  $t = \pm \frac{\pi}{2}$  satisfies the constraint. The general solution of the constraint is

$$\cos t_{\pm} = \frac{Q^{-1}Q^{1} \pm |Q^{0}|\sqrt{H}}{(Q^{-1})^{2} + (Q^{1})^{2}}$$
(A.39)

![](_page_51_Picture_0.jpeg)

Figure 14. The covering space of the EWB geometry with a bulk particle. The covering space needs to be considered to ensure the vanishing of the gauge constraint.

Where H " ´Q<sup>2</sup> . Let's evaluate this for m cosh γ ! E. To first order in m cosh γ{ ? E we find

$$\cos t_{\pm} = \frac{m}{\sqrt{E}} \left[ \cosh \gamma \pm \sinh \gamma \cos \theta \right] > 0 \tag{A.40}$$

and therefore |t˘| ă <sup>π</sup> 2 .

Finally we consider the case of the brane. To analyze this we need to consider the covering space before the Z<sup>2</sup> has been taken [\[34\]](#page-56-7). In this space we would have the brane, which we can place at rest in the center, and two boundary particles. The extra bulk particle also needs to be duplicated. The brane and bulk particle charges are

$$Q_{brane}^{a} = (0, 0, -\mu) \tag{A.41}$$

$$Q_{BP_L}^a = m(\sinh \gamma \sin \theta, \sinh \gamma \cos \theta, -\cosh \gamma)$$
 (A.42)

$$Q_{BP_R}^a = m(-\sinh\gamma\sin\theta, -\sinh\gamma\cos\theta, -\cosh\gamma)$$
 (A.43)

were the two bulk particle charges are related by θ Ñ θ ` π. Notice that the sum of the bulk particle charges is

$$Q_{BP_L}^a + Q_{BP_R}^a = (0, 0, -2m\cosh\gamma)$$
 (A.44)

and again, now we have the choice to either dress the bulk particles to the brane or the boundary particles. The analysis of the latter case is identical to what we did previously with the TFD. Dressing them to the brane simply changes the mass of the brane to

$$-\mu \to -\mu + 2m\cosh\gamma \tag{A.45}$$

Note that the boundary particle trajectories are unchanged since the total charge of the bulk particles plus the brane is equal to that of the previous case with only a brane by itself (with a different mass). Also, the trajectory of the brane is unaltered since it is insensitive to multiplying the charge by an overall factor. Note that brane mass is always decreased independent of θ.

## <span id="page-52-0"></span>B Initial Energy Increase due to an External Coupling

We prove in this appendix that at early times that coupling to another system will generically raise the energy of an initially static system. We imagine coupling a SYK system R to an external system X.

Let X be at arbitrary system in its vacuum, and let's consider modifying the total Hamiltonian with a general coupling

$$H_T = H_0 + \delta H(t) \tag{B.1}$$

where

$$H_0 \equiv H_{SYK}^R + H^X \tag{B.2}$$

$$\delta H(t) \equiv \lambda A_R(t) B_X(t)$$
 (B.3)

Let's assume that R is in the thermal state. Working in the interaction picture, the evolved state is

$$|\Psi(t)\rangle_{LRX} = e^{-iH_0t} \mathcal{T} e^{-i\int_{t_0}^t dt' \delta H(t')} |\beta\rangle_{LR} |0\rangle_X$$
 (B.4)

We want to compute change in energy of system R immediately after turning on the interaction, which we do so by working to leading order in δt " t ´ t0. We can then Taylor expand the interaction exponent

$$|\Psi(t)\rangle_{LRX} = e^{-iH_0t}e^{-i\delta t\delta H(t_0) - i\delta t^2\partial_{t_0}\delta H(t_0) + \dots}|\beta\rangle_{LR}|0\rangle_X$$
(B.5)

Now we'll compute the instantaneous energy change for either system. The general computation is

$$\delta E_K = {}_{LRX} \langle \Psi(t) | H^K | \Psi(t) \rangle_{LRX} - {}_{X} \langle 0 | {}_{LR} \langle \beta | H^K | \beta \rangle_{LR} | 0 \rangle_{X}$$
 (B.6)

where  $K = \{R, X\}$ . The first order in  $\delta t$  comes from

$$\delta E_R^{(1)} = -i\delta t \ _X \langle 0|_{LR} \langle \beta| \ [H_{SYK}^R, \delta H(t_0)] \ |\beta\rangle_{LR} |0\rangle_X \tag{B.7}$$

$$= -\lambda \delta t \left\langle \dot{A}(t) \right\rangle \left\langle B(t) \right\rangle \tag{B.8}$$

$$\delta E_X^{(1)} = -i\delta t \ _X \langle 0|_{LR} \langle \beta| \ [H_\phi^X, \delta H(t_0)] \ |\beta\rangle_{LR} |0\rangle_X \tag{B.9}$$

$$= -\lambda \delta t \left\langle A(t) \right\rangle \left\langle \dot{B}(t) \right\rangle \tag{B.10}$$

where  $\langle A(t) \rangle = \langle \beta | A(t) | \beta \rangle$  and  $\langle 0 | B(t) | 0 \rangle$ . Note that both states of X and R are time translation invariant, and therefore the time derivatives of one point functions must vanish. The same conclusion holds assuming that R is not precisely the thermal state but has thermalized. We conclude that to first order  $\delta E = 0$ , or at least to very good approximation. Not that it would have been problematic if this wasn't true since we have the freedom to tune the sign of  $\lambda$  so as to reduce the energy of the scalar field theory below that of the vacuum.

We turn next to the second order contribution in  $\delta t$ . Expanding, we find

$$\delta E_R^{(2)} = \frac{\lambda^2}{2} i \langle [\dot{A}(t_0), A(t_0)] \rangle \langle B^2(t_0) \rangle$$
(B.11)

$$\delta E_X^{(2)} = \frac{\lambda^2}{2} i \langle A^2(t_0) \rangle \langle [\dot{B}(t_0), B(t_0)] \rangle$$
 (B.12)

Note that we do not have a choice in the overall sign of these contributions to the total energy. We first give a qualitative argument for why these contributions have to be positive, and then prove it rigorously. For either system, these expressions are what one would obtain when turning on a single system Hamiltonian deformation. For example for the R system we would have

$$\delta H(t) = \tilde{\lambda} A(t) \tag{B.13}$$

where  $\tilde{\lambda} = \lambda \sqrt{\langle B^2(t_0) \rangle}$ . Since this amounts to acting with a unitary on either system we can make definite statements about how the energy will change. Since system X begins in the ground state, this must increase the energy. The same conclusion would hold for R in the thermal state, since this state minimizes the expectation value of the Hamiltonian while keeping fixed the entanglement entropy.

The more careful argument is the following. The commutator can be written as

$$i\langle [\dot{A}(t_0), A(t_0)] \rangle = i \operatorname{Tr} \left[ e^{-\beta H} \left( \dot{A}(t_0 - i\tau) A(t_0) - A(t_0) \dot{A}(t_0 + i\tau) \right) \right] \Big|_{\tau \to 0}$$
 (B.14)

$$= -\partial_{\tau} \text{Tr} \left[ e^{-\beta H} \left( A(t_0 - i\tau) A(t_0) + A(t_0) A(t_0 + i\tau) \right) \right] \Big|_{\tau \to 0}$$
 (B.15)

$$= -2\partial_{\tau} \operatorname{Tr} \left[ e^{-(\beta - \tau)H} A(t_0) e^{-\tau H} A(t_0) \right] \Big|_{\tau \to 0}$$
(B.16)

We want to show that

$$\partial_{\tau} \operatorname{Tr} \left[ e^{-(\beta - \tau)H} A(t_0) e^{-\tau H} A(t_0) \right] \Big|_{\tau \to 0} < 0$$
(B.17)

This is not hard to prove. Consider working out the trace in the energy basis. This gives

$$-\sum_{nm} |A_{nm}|^2 e^{-\beta E_n - \tau(E_m - E_n)} (E_m - E_n)$$
(B.18)

which after noting that  $|A_{nm}|$  is symmetric in n and m can be re-expressed as

$$-2\sum_{n>m} |A_{nm}|^2 e^{\beta(E_n + E_m)/2} (E_m - E_n) \sinh\left[\left(\frac{\beta}{2} - \tau\right) (E_m - E_n)\right]$$
 (B.19)

which is indeed negative for  $\tau = 0$ . This shows that

$$i\langle [\dot{A}(t_0), A(t_0)] \rangle > 0 \tag{B.20}$$

in the thermal state. The same conclusion would hold for a state that has thermalized and for a simple operator A.

</details>

<details>
<summary><span id="page-0-0"></span>Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence</summary>

# <span id="page-0-0"></span>Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence

### Fernando Pastawski,\*<sup>a</sup> Beni Yoshida\*<sup>a</sup> Daniel Harlow,<sup>b</sup> John Preskill,<sup>a</sup>

E-mail: [fernando.pastawski@gmail.com](mailto:fernando.pastawski@gmail.com), [rouge@caltech.edu](mailto:rouge@caltech.edu), [dharlow@princeton.edu](mailto:dharlow@princeton.edu), [preskill@caltech.edu](mailto:preskill@caltech.edu)

Abstract: We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel construction of quantum error-correcting codes with a tensor network structure. Our building block is a special type of tensor with maximal entanglement along any bipartition, which gives rise to an isometry from the bulk Hilbert space to the boundary Hilbert space. The entire tensor network is an encoder for a quantum error-correcting code, where the bulk and boundary degrees of freedom may be identified as logical and physical degrees of freedom respectively. These models capture key features of entanglement in the AdS/CFT correspondence; in particular, the Ryu-Takayanagi formula and the negativity of tripartite information are obeyed exactly in many cases. That bulk logical operators can be represented on multiple boundary regions mimics the Rindler-wedge reconstruction of boundary operators from bulk operators, realizing explicitly the quantum error-correcting features of AdS/CFT recently proposed in [\[1\]](#page-60-0).

a Institute for Quantum Information & Matter and Walter Burke Institute for Theoretical Physics, California Institute of Technology, Pasadena, California 91125, USA

<sup>b</sup>Princeton Center for Theoretical Science, Princeton University, Princeton NJ 08540 USA \*These authors contributed equally to this work.

# Contents

| 1 | Introduction                                                  | 1  |
|---|---------------------------------------------------------------|----|
| 2 | Isometries and perfect tensors                                | 3  |
| 3 | Construction of holographic quantum states and codes          | 6  |
| 4 | Entanglement structure of holographic states                  | 9  |
|   | 4.1<br>Ryu-Takayanagi formula                                 | 9  |
|   | 4.2<br>Bipartite entanglement of disconnected regions         | 11 |
|   | 4.3<br>A map of multipartite entanglement                     | 14 |
|   | 4.4<br>Negative tripartite information                        | 19 |
| 5 | Quantum error correction in holographic codes                 | 21 |
|   | 5.1<br>AdS-Rindler reconstruction as error correction         | 21 |
|   | 5.2<br>The physical interpretation of holographic codes       | 23 |
|   | 5.3<br>Bulk reconstruction from tensor pushing                | 23 |
|   | 5.4<br>Connected reconstruction and the causal wedge          | 25 |
|   | 5.5<br>Disconnected reconstruction and the entanglement wedge | 26 |
|   | 5.6<br>Erasure threshold                                      | 30 |
|   | 5.7<br>Holographic stabilizer codes                           | 34 |
|   | 5.8<br>Are local gauge constraints enough?                    | 37 |
| 6 | Black holes and holography                                    | 38 |
| 7 | Open problems and outlook                                     | 39 |
| A | Perfect tensor examples                                       | 41 |
|   | A.1<br>5-qubit code and 6-qubit state                         | 41 |
|   | A.2<br>3 -qutrit code and 4-qutrit state                      | 43 |
|   | A.3<br>Large<br>n                                             | 44 |
| B | Proof of RT for negatively curved planar graphs               | 45 |
| C | Counting tensors in the pentagon code                         | 48 |
|   | C.1<br>Counting tensors                                       | 48 |
|   | C.2<br>Connected reconstruction                               | 49 |

| D |     | Estimating greedy erasure thresholds           | 51 |
|---|-----|------------------------------------------------|----|
|   | D.1 | Analytic bounds                                | 52 |
|   | D.2 | Numerical evaluation                           | 56 |
| E |     | Reconstructing beyond the greedy algorithm     | 56 |
|   | E.1 | Reconstruction from symmetry guarantees        | 56 |
|   | E.2 | Approximate reconstruction for typical tensors | 59 |
|   |     |                                                |    |

### <span id="page-2-0"></span>1 Introduction

The AdS/CFT correspondence, an exact duality between quantum gravity on a (d+1) dimensional asymptotically-AdS space and a d-dimensional CFT defined on its boundary, has significantly advanced our understanding of quantum gravity, as well as provided a powerful framework for studying strongly-coupled quantum field theories. One aspect of this duality is a remarkable relationship between geometry and entanglement. This notion first appeared in the proposal [\[2\]](#page-61-0) that two entangled CFT's have a bulk dual connecting them through a wormhole, and was later quantified by Ryu and Takayanagi via their proposal that entanglement entropy in the CFT is computed by the area of a certain minimal surface in the bulk geometry [\[3,](#page-61-1) [4\]](#page-61-2). This latter proposal, known as the Ryu-Takayanagi (RT) formula, has led to much further work on sharpening the connection between geometry and entanglement [\[5–](#page-61-3)[12\]](#page-61-4)

In the condensed matter physics community, improved understanding of quantum entanglement has led to significant progress in the numerical simulation of emergent phenomena in strongly-interacting systems. A key ingredient of such algorithms is the use of tensor networks to efficiently represent quantum many-body states [\[13–](#page-61-5) [15\]](#page-61-6). Vidal combined this idea with entanglement renormalization to formulate the Multiscale Entanglement Renormalization Ansatz (MERA) [\[16,](#page-61-7) [17\]](#page-61-8), a family of tensor networks that efficiently approximate wave functions with long-range entanglement of the type exhibited by ground states of local scale-invariant Hamiltonians [\[18–](#page-61-9)[20\]](#page-62-0). The key idea is to represent entanglement at different length scales using tensors in a hierarchical array.

In the AdS/CFT correspondence, the emergent radial direction can be regarded as a renormalization scale [\[21\]](#page-62-1), and spatial slices have a hyperbolic geometry resembling the exponentially growing tensor networks of MERA. This similarity between AdS/CFT and MERA was pointed out by Swingle, who argued that some physics of the AdS/CFT correspondence can be modeled by a MERA-like tensor network where quantum entanglement in the boundary theory is regarded as a building block for the emergent bulk geometry [\[22,](#page-62-2) [23\]](#page-62-3).

Recently it has been argued in [\[1\]](#page-60-0) that the emergence of bulk locality in AdS/CFT can be usefully characterized in the language of quantum error-correcting codes. Certain paradoxical features of the correspondence arise naturally by interpreting bulk local operators as logical operators on certain subspaces of states in the CFT, whose entanglement structure protects these operators from boundary erasures. Moreover, inspired by [\[22,](#page-62-2) [23\]](#page-62-3), it was suggested that there should be tensor network models that concretely implement these ideas.

In this paper, we propose such a family of exactly solvable toy models of the bulk/boundary correspondence based on a novel tensor-network construction of quantum error-correcting codes. Other authors have recently used holographic ideas [\[24,](#page-62-4) [25\]](#page-62-5) and related tensor network constructions [\[26,](#page-62-6) [27\]](#page-62-7) to build quantum codes with interesting properties or toy models of the bulk/boundary correspondence [\[28\]](#page-62-8), but our approach differs from previous work by combining the following properties, all of which are desirable for a model of AdS/CFT:

- Exactly solvable: Many of the properties of our models can be shown explicitly. In particular, an exact prescription for mapping bulk operators to boundary operators can be obtained, and we can give examples where the Ryu-Takayanagi formula holds exactly for all connected boundary regions.
- QECC: Our models are quantum error-correcting codes, where the bulk/boundary legs of the tensor network correspond to input/outputs of an encoding quantum circuit. In this sense they realize explicitly the proposal of [\[1\]](#page-60-0).
- Bulk uniformity: The tensor network is supported on a uniform tiling of a hyperbolic space, known as a hyperbolic tessellation. If the tiling is extended to an infinite system, the tensor network has no inherent directionality and all the locations in the bulk can be treated on an equal footing (see Fig. [4b\)](#page-8-0).

The rest of this paper is organized as follows: In section [2,](#page-4-0) we introduce a class of tensors called perfect tensors, which are associated with pure quantum states of many spins such that the entanglement is maximal across any partition of the spins into two sets of equal size. In section [3,](#page-7-0) we construct holographic states and codes by building networks of perfect tensors. These codes have properties reminiscent of the AdS/CFT correspondence, elucidated in the rest of the paper, where the code's logical/physical degrees of freedom are interpreted as the bulk/boundary degrees of freedom of a CFT with a gravitational dual.

In section [4,](#page-10-0) we study the entanglement structure of holographic states, showing that the Ryu-Takayanagi formula is exactly satisfied for any connected boundary region, developing a graphical representation of multipartite entanglement, and confirming the negativity of tripartite information [\[9\]](#page-61-10). In section [5,](#page-22-0) we investigate the dictionary relating bulk and boundary observables, define a lattice version of the causal wedge, and explain how bulk local operators in the causal wedge can be reconstructed on the boundary; we also define a lattice version of the entanglement wedge, and offer evidence supporting the entanglement wedge hypothesis proposed in [\[40–](#page-63-0)[42\]](#page-63-1), see also [\[67\]](#page-64-0). We briefly discuss how to describe black holes using holographic codes in section [6.](#page-39-0) Section [7](#page-40-0) contains our conclusions, and many details appear in the appendices.

### <span id="page-4-0"></span>2 Isometries and perfect tensors

In this section we review some tools which will be used in our constructions of holographic states and codes. We begin with a standard definition:

Definition 1. Say H<sup>A</sup> and H<sup>B</sup> are two Hilbert spaces, not necessarily of the same dimensionality. An isometry from H<sup>A</sup> to H<sup>B</sup> is a linear map T : H<sup>A</sup> 7→ H<sup>B</sup> with the property that it preserves the inner product.

If H<sup>A</sup> and H<sup>B</sup> have finite dimensionality, as we will assume throughout this paper, then it immediately follows that such a T can exist only if their dimensionalities dim(A) and dim(B) obey dim(A) ≤ dim(B). In the special case where dim(A) = dim(B), T is just a unitary transformation. Clearly the composition of two isometries is also an isometry.

If T : H<sup>A</sup> 7→ H<sup>B</sup> is an isometry, then T †<sup>T</sup> is the identity on <sup>H</sup><sup>A</sup> and T T† is a projector mapping H<sup>B</sup> to the range of T. We may represent the map T as a two-index tensor acting as

$$T: |a\rangle \mapsto \sum_{b} |b\rangle T_{ba},$$
 (2.1)

where {|ai} denotes a complete orthonormal basis for H<sup>A</sup> and {|bi} for HB. Then T is an isometry if and only if

<span id="page-4-1"></span>
$$\sum_{b} T_{a'b}^{\dagger} T_{ba} = \delta_{a'a}. \tag{2.2}$$

We represent this graphically in figure [1,](#page-5-0) following the convention that operators are ordered from left to right, so that in the figure T † is applied after T. We will call a tensor obeying [\(2.2\)](#page-4-1) an isometric tensor.

<span id="page-5-0"></span>![](_page_5_Picture_0.jpeg)

Figure 1. Diagrammatic tensor notation, here showing that T is an isometry.

Isometric tensors have the property that any operator O acting on its "incoming" leg, can be replaced by an equal norm operator O<sup>0</sup> acting on its "outgoing" leg, because

$$TO = TOT^{\dagger}T = (TOT^{\dagger})T \equiv O'T;$$
 (2.3)

we illustrate this property in figure [2.](#page-5-1) This operation is essential for what follows,

<span id="page-5-1"></span>![](_page_5_Picture_5.jpeg)

Figure 2. Operator pushing through an isometric tensor.

and we will often describe it as "pushing an operator through a tensor". It is also easy to check a useful converse of operator pushing: If the two-index tensor T has the property that any unitary transformation U contracted with its incoming index can be replaced by a corresponding unitary transformation U 0 contracted with its outgoing index (i.e., T U = U <sup>0</sup>T), then T obeys [\(2.2\)](#page-4-1) up to a scalar factor, and therefore must be proportional to an isometric tensor.

$$\begin{array}{c|c}
a_1 & T & b & T^{\dagger} \\
\hline
 & a_1' & = & \frac{a_1}{\times \dim(A_2)}
\end{array}$$

<span id="page-5-2"></span>Figure 3. If H<sup>A</sup> = HA<sup>2</sup> ⊗ HA<sup>1</sup> , then we can move one of the factors to the output while preserving the isometric structure.

Another important property of isometric tensors is that if the input Hilbert space factorizes, we may reinterpret an input factor as an output factor while preserving [\(2.2\)](#page-4-1), up to an overall rescaling. That is, if T : H<sup>A</sup><sup>2</sup> ⊗ H<sup>A</sup><sup>1</sup> 7→ H<sup>B</sup> is an isometric map, acting on a basis according to

$$T: |a_2 a_1\rangle \mapsto \sum_b |b\rangle T_{ba_2 a_1},\tag{2.4}$$

then  $\tilde{T}: \mathcal{H}_{A_1} \mapsto \mathcal{H}_B \otimes \mathcal{H}_{A_2}$  acting as

$$\tilde{T}:|a_1\rangle\mapsto\sum_{ba_2}|ba_2\rangle T_{ba_2a_1}$$
 (2.5)

obeys  $\tilde{T}^{\dagger}\tilde{T} = \dim(A_2)I_{A_1}$ . We illustrate this property in figure 3.

In this paper we will be interested in a special class of isometric tensors, which we will call perfect tensors. To formulate the concept of a perfect tensor, first note that we may divide the m indices of a tensor  $T_{a_1a_2...a_m}$  into a set A and a complementary set  $A^c$ . We use |A| to denote the cardinality of the set A; hence  $|A| + |A^c| = m$ . Then T may be regarded as a linear map from the span of the indices in A to the span of the indices in  $A^c$ . We will usually assume that each index ranges over v values, and we will use A to denote both the set of |A| indices and the corresponding vector space with dimension  $v^{|A|}$ ; thus we say T maps A to  $A^c$ .

**Definition 2.** A 2n-index tensor  $T_{a_1a_2...a_{2n}}$  is a **perfect tensor** if, for any bipartition of its indices into a set A and complementary set  $A^c$  with  $|A| \leq |A^c|$ , T is proportional to an isometric tensor from A to  $A^c$ .

It is not obvious that nontrivial perfect tensors exist, but they do! Note that for T to be perfect it suffices for T to be a unitary transformation when  $|A| = |A^c| = n$ ; in that case the property illustrated in figure 3 ensures that T is proportional to an isometric tensor for |A| < n. In Appendix A we describe perfect tensors explicitly for the case n = 3, v = 2 and for the case n = 2, v = 3; other cases with larger n and v are also discussed there. To keep our discussion concrete, we will focus especially on the six-index tensor for qubits  $(v = 2)^1$ , but much of what we say applies to arbitrary 2n-index perfect tensors.

Perfect tensors are related to other notable ideas in quantum information theory. In general, a tensor T with m indices, each ranging over v values, describes a pure quantum state  $|\psi\rangle$  of m v-dimensional spins, where, up to a normalization factor,

$$|\psi\rangle = \sum_{a_1, a_2, \dots, a_m} T_{a_1 a_2 \dots a_m} |a_1 a_2 \dots a_m\rangle. \tag{2.6}$$

<sup>&</sup>lt;sup>1</sup>This can be obtained from the encoding map of the 5-qubit code.

A perfect tensor describes a pure state of 2n spins with a special property — any set of n spins is maximally entangled with the complementary set of n spins. Such states have been called absolutely maximally entangled (AME) states [\[29,](#page-62-9) [30\]](#page-62-10). Conversely any AME state defines a perfect tensor. Regarded as a linear map from one spin to 2n − 1 spins, a perfect tensor is the isometric encoding map of a quantum error-correcting code which encodes a single logical spin in a block of 2n−1 physical spins, where the logical spin is protected against the erasure of any n−1 physical spins. Because n is more than half of all the physical spins, this is the best possible protection against erasure errors compatible with the no-cloning principle. In coding terminology this code has distance n and is denoted [[m, k, d]]<sup>v</sup> = [[2n − 1, 1, n]]v, where m is the number of physical spins in the code block, k is the number of protected logical spins, and d is the code distance. This code is also the basis for a quantum-secret-sharing scheme called a ((n, 2n − 1)) threshold scheme [\[31\]](#page-62-11); code states have the property that a party holding any n − 1 spins has no information about the logical spin, while a party holding any n spins has complete information about the logical spin (because erasure of the remaining n − 1 spins is correctable).

### <span id="page-7-0"></span>3 Construction of holographic quantum states and codes

We have seen how tensors can be interpreted as quantum states or quantum codes. In this section we construct tensor networks in which the fundamental building blocks are perfect tensors. Our tensor networks describe states which we call holographic states, and codes which we call holographic codes.

We shall focus on examples based on tilings of two-dimensional hyperbolic space, which are specific realizations of uniform hyperbolic tilings known as hyperbolic tessellations. These tilings have desirable symmetries for constructing a toy model of the AdS/CFT correspondence. In particular they are discretely scale-invariant, and there exist graph isomorphisms that bring any point in the graph to the center while preserving the local structure of the tiling.[2](#page-0-0) The machinery we develop may also be straightforwardly applied to non-uniform and higher-dimensional graphs.

Let's first consider a uniform tiling of a two-dimensional hyperbolic space by hexagons, with four hexagons adjacent at each vertex, as depicted in Fig [4a.](#page-8-1) A perfect tensor with six legs is placed at each hexagon, and legs of perfect tensors are contracted with neighboring tensors at shared edges of the hexagons. We associate physical spins with the uncontracted open tensor legs on the boundary of the hyperbolic tiling; the

<sup>2</sup>Such transformations can be directly visualized using Kaleidotile software [\[32\]](#page-62-12), which is freely available and has been of great aid in developing geometric intuition and producing figures of uniform hyperbolic tilings in this paper.

<span id="page-8-1"></span>![](_page_8_Figure_0.jpeg)

<span id="page-8-0"></span>Figure 4. White dots represent physical legs on the boundary. Red dots represent logical input legs associated to each perfect tensor.

tensor network corresponds to a pure state of these boundary spins, which we call a holographic state. Note that perfect tensors are not necessarily symmetric under all the possible permutations of tensor legs, and thus we specify some particular ordering of tensor legs in the construction.

We may similarly attach a state interpretation to more general networks constructed by contracting perfect tensors:

Definition 3. Consider a tensor network composed of perfect tensors which cover some geometric manifold with boundary, where all the interior tensor legs are contracted. A holographic state is a state interpretation of such a tensor network, where physical degrees of freedom are associated with all uncontracted legs at the boundary of the manifold.

We now provide an example of a holographic quantum code. As in a holographic state, we consider a uniform tiling of the hyperbolic disc, this time by pentagons, with four pentagons adjacent at each vertex. A perfect tensor with six legs is placed at each pentagon, so that each tensor has one additional uncontracted open leg. This additional tensor leg is interpreted as a bulk index or logical input for the tensor network (see Fig. [4b\)](#page-8-0). The entire system can be viewed as a big tensor with logical legs in the bulk and physical legs on the boundary. We then have the following theorem:

Theorem 1. The pentagon-tiling tensor network is an isometric tensor from the bulk to the boundary. We call it the holographic pentagon code.

We can prove this theorem by noting that if we order the tensors into layers labeled by increasing graph distance from the center, each tensor has at most two legs contracted with the tensors at the previous layer (this property is a consequence of the "negative curvature" of the graph). Therefore, even if we regard the pentagon's bulk logical index as an input leg, the total number of input legs is at most three, and we may therefore regard each tensor as an isometry from input legs to output legs. Applying the perfect tensors layer by layer, and recalling that the product of isometries is an isometry, we obtain an isometry mapping all the logical indices in the bulk to the physical indices on the boundary.

We can view this isometry as the encoding transformation of a quantum errorcorrecting code, which we call a holographic code. The number of logical v-dimensional spins is the number Nbulk of pentagons in the tiling, and the number of physical vdimensional spins in the code block is the number Nboundary of uncontracted boundary indices in the tensor network. We show in Appendix [C](#page-49-0) that the rate of the code, meaning the ratio of the number of logical spins to the number of physical spins, approaches

<span id="page-9-0"></span>
$$\frac{N_{\rm bulk}}{N_{\rm boundary}} \to \frac{1}{\sqrt{5}} \approx .447$$
 (3.1)

in the limit of a large number of layers.

This pentagon code was constructed by successively adding layers of tensors starting from the center and stopping after repeating this procedure a certain number of times (two layers in figure [4b\)](#page-8-0). Alternatively, we may fill the bulk using a non-uniform cutoff, so that the graph distance between the "center" and the boundary varies from one portion of the boundary to another (as occurs in figure [4a\)](#page-8-1). By exerting this freedom, we may change the corresponding value [3.1](#page-9-0) for the rate of the code and even slightly increase it. By varying the choice of perfect tensor and the shape of the cutoff, a large family of holographic codes can be constructed:

Definition 4. Consider a tensor network composed of perfect tensors which cover some geometric manifold with boundaries. The tensor network is called a holographic code if it gives rise to an isometric map from uncontracted bulk legs to uncontracted boundary legs.

Tensor networks with open legs in the bulk were first proposed by Vidal [\[17\]](#page-61-8). More recently, Qi [\[28\]](#page-62-8) constructed a tensor-tree model with an exact unitary mapping between the bulk and the boundary. The most important difference between their models and ours is that their states are not protected against erasure of physical spins because the code rate is asymptotically unity. In addition our models are more symmetric; since perfect tensors can be interpreted as isometries along any direction, our models have no preferred direction in the bulk and all bulk sites are treated equally. In particular, the pentagon code has the nice feature that, because the 6-leg perfect tensor we construct in appendix [A](#page-42-0) is symmetric under cyclic permutations of five of the legs, which we take to be the contracted legs, the symmetry of the network is just the full symmetry of the graph.

# <span id="page-10-0"></span>4 Entanglement structure of holographic states

In this section we explore to what extent holographic states reproduce key properties of the AdS/CFT correspondence, such as the Ryu-Takayanagi formula for entropy of a boundary region [\[3\]](#page-61-1) and the negativity of tripartite information [\[9\]](#page-61-10).

### <span id="page-10-1"></span>4.1 Ryu-Takayanagi formula

The Ryu-Takayanagi (RT) formula says that for a CFT whose gravitational dual is wellapproximated by Einstein gravity at low energies, in any static state with a geometric bulk description the entropy S<sup>A</sup> of a boundary subregion A at fixed time obeys

$$S_A = \frac{\text{Area}(\gamma_A)}{4G}; \tag{4.1}$$

here G is Newton's constant and γ<sup>A</sup> is the minimal-area codimension-two bulk surface whose boundary matches the boundary ∂A of A. In our examples the bulk theory is 2 + 1 dimensional, so γ<sup>A</sup> will be a spacelike bulk geodesic whose "area" is just defined as its length.

In our discrete setting, we will define γ<sup>A</sup> as a certain cut through the tensor network which partitions it into two disjoint sets of perfect tensors. Associated with a cut c is a decomposition of the tensor network as a contraction of two tensors P and Q, where the contracted legs lie along the cut; the number of contracted legs is called the length of c, denoted |c|. If A is a set of boundary legs and A<sup>c</sup> is the complementary set of boundary legs, then we say that the boundary of the cut c matches the boundary of A if the uncontracted legs of P are the legs of A, and the uncontracted legs of Q are the legs of A<sup>c</sup> . The minimal bulk geodesic bounded by A, γA, is then defined as the cut c of shortest length whose boundary matches the boundary of A. We use P to denote, not just the tensor associated with one side of the cut, but also the set of bulk lattice sites corresponding to the perfect tensors which are contracted to construct P; likewise for Q. We note that P or Q might have more than one connected component, and so might γ<sup>A</sup> when regarded as a path in the dual graph.

A standard argument for tensor network representations of quantum states shows that  $|\gamma_A|$  provides an *upper bound* on  $S_A$ . If P and Q are the tensors associated with a cut c whose boundary matches the boundary of A, then the holographic state  $|\psi\rangle$  may be expressed (up to normalization) as

<span id="page-11-2"></span>
$$|\psi\rangle = \sum_{a,b,i} |ab\rangle P_{ai} Q_{bi} \equiv \sum_{i} |P_i\rangle_A \otimes |Q_i\rangle_{A^c}.$$
 (4.2)

Here a and b run over complete bases for A and  $A^c$  respectively, and i runs over all possible values of the indices contracted along c; the vectors  $\{|P_i\rangle\}$  in  $\mathcal{H}_A$  and the vectors  $\{|Q_i\rangle\}$  in  $\mathcal{H}_{A^c}$  are not necessarily orthogonal or normalized. (See figure 5.) Tracing out  $A^c$  we obtain (up to normalization) the density operator on A:

![](_page_11_Picture_3.jpeg)

**Figure 5**. A cut through a holographic tensor network by a curve c bounded by  $\partial A$ . Boundary indices a and b are uncontracted in A and its complement  $A^c$  respectively; tensors P and Q are contracted by summing over the index i which is cut by c.

<span id="page-11-0"></span>
$$\rho_A = \sum_{i,i'} \langle Q_{i'} | Q_i \rangle | P_i \rangle \langle P_{i'} |. \tag{4.3}$$

Evidently the rank of  $\rho_A$  is at most the number of terms in the sum over i, namely  $v^{|c|}$ . The density operator of a given rank with maximal Von Neumann entropy is proportional to the identity on its support, and has entropy equal to log of the rank. We obtain the best bound by choosing the cut  $c = \gamma_A$  with the shortest length:

<span id="page-11-1"></span>
$$S_A \le |\gamma_A| \cdot \log v. \tag{4.4}$$

In most of what follows, we will define entropy by taking logs with base v, and so

suppress the log v factor.

If the tensors P and Q are actually isometries from i to a and b respectively, then {|Pii} and {|Qii} are sets of orthonormal vectors; in that case [\(4.4\)](#page-11-1) is saturated and a discrete analogue of the RT formula holds exactly. Under what conditions will P and Q be isometries? We can prove the following theorem:

<span id="page-12-1"></span>Theorem 2. Suppose that we have a holographic state associated to a simply-connected planar tensor network of perfect tensors, whose graph has "non-positive curvature".[3](#page-0-0) Then for any connected region A on the boundary, we have S<sup>A</sup> = |γA|; in other words, the lattice RT formula holds.

The strategy of the proof is to show that P and Q can in fact be interpreted as unitary transformations, from the cut together with some subregion of A or A<sup>c</sup> to the rest of A or A<sup>c</sup> respectively. We can then use the identity depicted in figure [3](#page-5-2) to reinterpret these transformations as isometries from the cut to A and from the cut to A<sup>c</sup> respectively; the RT formula follows. The key to the argument, explained in appendix [B,](#page-46-0) is using a strengthened version of the max-flow min-cut theorem (which is standard in graph theory [\[33\]](#page-62-13)) to establish that the tensor network representations of P and Q can be interpreted as unitary quantum circuits.

### <span id="page-12-0"></span>4.2 Bipartite entanglement of disconnected regions

Unfortunately the proof of Theorem [2](#page-12-1) does not directly generalize to a disconnected region A, nor even to connected regions for states, such as our holographic code states, where not all perfect tensor indices are contracted in the bulk. We do not consider this to be a serious problem for our models. However, we still find it worthwhile to introduce some machinery that allows us to quantify this presumption somewhat.

The first technique we will introduce is an algorithmic procedure for constructing, given a boundary region A, a bulk curve γ ? <sup>A</sup> bounded by ∂A such that the corresponding tensor P is guaranteed to be an isometry. For a holographic state the isometry P maps γ ? <sup>A</sup> to A, and for a holographic code P maps γ ? <sup>A</sup> and all incoming bulk indices of P to A. Furthermore, γ ? <sup>A</sup> is a local minimum of the length, in the sense that no single tensor can be added to or removed from P which reduces the length of the cut.

The algorithm makes essential use of the properties of perfect tensors and is quite simple. We consider a sequence of cuts {cα} each bounded by ∂A, and a corresponding sequence of isometries {Pα}, such that each cut in the sequence is obtained from the previous one by a local move on the bulk lattice. The sequence begins with the trivial

<sup>3</sup>The scalar curvature of a graph is somewhat tricky to define in general; the condition we really need here is that the distance functional from one point on the dual network to another does not have interior local maxima.

cut, A itself; in each step we identify one perfect tensor which has at least half of its legs contracted with P<sup>α</sup> and construct Pα+1 by adding this perfect tensor to Pα. Thus Pα+1 is obtained by composing P<sup>α</sup> with an isometry defined by a perfect tensor, and therefore Pα+1 is an isometry if P<sup>α</sup> is. The procedure halts when the cut reaches γ ? <sup>A</sup> and no further local moves are possible. Though many different sequences of local moves are allowed, γ ? <sup>A</sup> is well defined; tensors eligible for inclusion in Pα+1 remain so as other tensors are included, so the output of the algorithm does not depend on the order of inclusion. Following standard computer science terminology, we call this procedure the greedy algorithm and call γ ? <sup>A</sup> the greedy geodesic. A step of the greedy algorithm is illustrated in figure [6.](#page-13-0)

![](_page_13_Picture_1.jpeg)

Figure 6. A step in the greedy algorithm. The upper node has at least three legs contracted with the region P, which we have shaded red, so we include it into P.

<span id="page-13-0"></span>![](_page_13_Picture_3.jpeg)

Figure 7. Three examples where the greedy algorithm fails to find the matching minimal geodesics from complementary regions. The first example involves disconnected regions in the holographic state. The second example involves a positive curvature obstruction at the center of the tiling which blocks the greedy geodesic from reaching the global minimal surface. The third example involves a connected region for the holographic code. In both the first and the third figure the greedy algorithm finds minimal geodesics from both sides but they do not match. In both cases, it is possible for the entropy to be slightly smaller than the length of the geodesic. This depends on tensors which were not absorbed by either of the greedy geodesics which we call the bipartite residual regions.

<span id="page-13-1"></span>When the assumptions of Theorem [2](#page-12-1) are satisfied, the argument in appendix [B](#page-46-0) ensures that the greedy algorithm will find a true minimal geodesic γA. If there is more than one minimal geodesic, as is sometimes the case, then the greedy algorithm might continue past a minimal geodesic and proceed through minimal geodesics of equal length. In that case, the tensors in between the successive geodesics define a unitary transformation from one cut to the other. If A has more than one connected component, if there is positive curvature, or if there are uncontracted bulk indices as for a holographic code, the greedy algorithm does not necessarily succeed in finding matching minimal geodesics, as we illustrate in figure 7.

In cases where the greedy algorithm fails to find a minimal geodesic, we can still use it to prove an interesting *lower* bound on the entropy  $S_A$ . Suppose that  $\gamma_A^*$  and  $\gamma_{A^c}^*$  are two greedy geodesics, produced by applying the greedy algorithm to A and its complement  $A^c$  respectively, where P and Q are the corresponding tensors. Furthermore, suppose that  $\gamma_A^* \cap \gamma_{A^c}^*$  is non-empty, in the sense that some links are cut by both geodesics. We can represent that state as<sup>4</sup>

$$|\psi\rangle = \sum_{a,b,i,j,k} |ab\rangle P_{a,ij} Q_{b,ik} S_{jk} \equiv \sum_{i,j,k} S_{jk} |P_{ij}\rangle_A \otimes |Q_{ik}\rangle_{A^c}.$$
 (4.5)

Here *i* denotes the index shared between  $\gamma_A^*$  and  $\gamma_{A^c}^*$ , *j* is the index unique to  $\gamma_A^*$ , *k* is the index unique to  $\gamma_{A^c}^*$ , and *S* denotes the tensor that sits "in between"  $\gamma_A^*$  and  $\gamma_{A^c}^*$ . We call the set of lattice sites in *S* the *bipartite residual region* (where the modifier "bipartite" draws a distinction with the *multipartite residual region* to be discussed in section 4.3.) Because *P* and *Q* are isometries, both  $\{|P_{ij}\rangle\}$  and  $\{|Q_{ik}\rangle\}$  are sets of orthonormal vectors. Therefore, the marginal density operator for *A* is

$$\rho_A = \sum_{i,j,j',k} S_{jk} S_{j'k}^* |P_{ij}\rangle\langle P_{ij'}|. \tag{4.6}$$

This density operator has support on the subspace of A spanned by  $\{|P_{ij}\rangle\}$ , which has dimension  $v^{|\gamma_A^{\star}|}$ , and this subspace has a decomposition into subsystems  $A_1 \otimes A_2$  such that the basis element  $|P_{ij}\rangle$  may be expressed as  $|i\rangle_{A_1} \otimes |j\rangle_{A_2}$ , where  $\{|i\rangle\}$  and  $\{|j\rangle\}$  are orthonormal bases for  $A_1$  and  $A_2$  respectively. We may then write

$$\rho_A = \left(\sum_i |i\rangle\langle i|_{A_1}\right) \otimes \left(\sum_{j,j',k} S_{jk} S_{j'k}^* |j\rangle\langle j'|_{A_2}\right),\tag{4.7}$$

<sup>&</sup>lt;sup>4</sup>For holographic codes with dangling bulk legs, we assume for now that a product state is fed into all bulk legs. If the input bulk state were entangled instead, there would be additional contributions to the boundary entanglement which we are not including. This same proviso also applies to the discussion in the following subsection.

and from the additivity of the entropy, using  $\dim(A_1) = v^{|A_1|} = v^{|\gamma_A^* \cap \gamma_{A^c}^*|}$ , we obtain the following theorem.

<span id="page-15-1"></span>**Theorem 3.** For a holographic state or code, if A is a (not necessarily connected) boundary region and  $A^c$  is its complement, then the entropy of A satisfies

<span id="page-15-2"></span>
$$S_A \ge |\gamma_A^{\star} \cap \gamma_{A^c}^{\star}|,\tag{4.8}$$

where  $\gamma_A^{\star}$  is the greedy geodesic obtained by applying the greedy algorithm to A and  $\gamma_{A^c}^{\star}$  is the greedy geodesic obtained by applying the greedy algorithm to  $A^c$ .

We see from Theorem 3 that violations of the Ryu-Takayanagi formula are closely related to the size of the bipartite residual region. In particular, if there is no bipartite residual region then  $S_A = |\gamma_A^*|$ ; the upper bound (4.4) and the lower bound (4.8) together imply that  $\gamma_A^*$  is in fact a minimal geodesic, and RT holds. We will argue in section 4.3 that the bipartite residual region has size O(1) when the regions A and  $A^c$  on the boundary have O(1) connected components. In this sense, the corrections to the RT formula are typically small.

#### <span id="page-15-0"></span>4.3 A map of multipartite entanglement

So far we have emphasized the bipartite entanglement between a boundary region A and its complement  $A^c$  in a holographic state or code. But we may also divide the boundary into three or more regions and investigate the structure of the entanglement among these regions. The entanglement structure can be elucidated via an entanglement "distillation" procedure which we will now describe.

To explain this procedure we begin by revisiting the case of bipartite entanglement. We have seen that if the conditions of Theorem 2 are satisfied, then a holographic state can be expressed in the form (4.2), where a subsystem of A of dimension  $v^{|\gamma_A^*|}$  is maximally entangled with a corresponding subsystem of  $A^c$ . This entanglement shared between two systems is generally diluted, since each party may contain many more than  $S_A$  spins. The entanglement would be more useful in a more concentrated form.

The procedure for transforming dilute entanglement into concentrated entanglement, called entanglement distillation, is particularly simple for a bipartite pure state like  $|\psi\rangle$  in (4.2). We choose  $|\gamma_A^*|$  specified spins in A (the subsystem  $A_1$  of A) and we choose  $|\gamma_A^*|$  spins in  $A^c$  (the subsystem  $A_1^c$  of  $A^c$ ). Then we apply a unitary transformation  $U_A$  acting on A that transforms the basis states  $\{|P_i\rangle_A\}$  to the standard basis states of  $A_1$ , and a unitary transformation  $U_{A^c}$  acting on  $A^c$  that transforms the basis states  $\{|Q_i\rangle_{A^c}\}$  to the standard basis states of  $A_1^c$ , thus obtaining the state

$$|\psi'\rangle = (|\Phi\rangle^{\otimes|\gamma_A^*|})_{A_1A_1^c} \otimes |\tilde{\chi}\rangle_{A_2} \otimes |\tilde{\phi}\rangle_{A_2^c}, \tag{4.9}$$

in which the entanglement of A with  $A^c$  now resides entirely in the system  $A_1A_1^c$ . Here  $A_2$  denotes the complement of  $A_1$  in A,  $A_2^c$  denotes the complement of  $A_1^c$  in  $A^c$ , and

$$|\Phi\rangle = \frac{1}{\sqrt{v}} \sum_{\alpha=1}^{v} |\alpha\rangle \otimes |\alpha\rangle$$
 (4.10)

is a maximally entangled EPR pair of two spins.

There is a method for constructing the unitary transformations  $U_A$  and  $U_{A^c}$  explicitly, which has a pleasing geometrical interpretation. The method uses the greedy algorithm for constructing  $\gamma_A^{\star}$ , but where now each local move, in which the cut through the tensor network advances into the bulk by moving past one additional tensor, is accompanied by a local unitary transformation that decouples spins from the network. This local unitary transformation is depicted in figure 8, where entanglement distillation is performed on a pair of contracted six-leg tensors.

<span id="page-16-0"></span>![](_page_16_Picture_4.jpeg)

Figure 8. The correspondence between local moves and distillation of EPR pairs. (a) Distillation of two EPR pairs. (b) The corresponding local moves. Before the first move, the tensor on the left has four legs crossed by the cut. Because the tensor is perfect, its remaining two legs are maximally entangled with a subsystem of these four. The first local unitary transformation acts on the four spins below the cut, transforming the basis to decouple the second and third spin, while the first and fourth spins remain contracted across the cut; in the corresponding local move, the cut advances upward past the tensor on the left. After the first move, the tensor on the right has five legs crossed by the cut. The second unitary transformation changes the basis of these five spins, decoupling the first four, while the fifth remains contracted across the cut; now the corresponding local move advances the cut upward past the tensor on the right. The product of the two local unitaries has distilled two EPR pairs which cross the cut, while decoupling six spins below the cut.

Since each local move of the greedy algorithm moves the cut past a tensor which

initially has at least three legs crossed by the cut, the legs above the cut are always maximally entangled with the legs below, and the corresponding local unitary transformation exists. For purposes of visualization, we may imagine that the spins which remain contracted across the cut advance further into the bulk in each step, remaining adjacent to the cut, while the spins which decouple are left behind. When the greedy algorithm applied to A terminates, then, all the decoupled spins of A are distributed throughout the bulk region in between the greedy geodesic and the boundary, while  $|\gamma_A^*|$  spins of A, lined up along the greedy geodesic, are contracted with tensors on the other side of the greedy geodesic. If we also apply the greedy algorithm to  $A^c$ , then under the conditions of Theorem 2, the algorithm terminates at the same greedy geodesic. Acting together, then, the unitary transformations associated with the two greedy algorithms have decoupled all the boundary spins, except for  $|\gamma_A^*|$  EPR pairs, one for each of the legs crossed by the greedy geodesic, thus executing the entanglement distillation protocol.

Run backwards, the sequence of local unitary transformations associated with the greedy algorithm constitutes a holographic quantum circuit, which prepares the boundary state. The input to this circuit is  $|\gamma_A^*|$  EPR pairs, plus a suitable number of additional spins in a product state, distributed throughout the bulk. The circuit builds the state step by step, gradually incorporating the bulk spins as the cut advances outward from the greedy geodesic toward the boundary. The input state, envisioned as a set of EPR pairs lined up along  $\gamma_A^*$ , provides a map of entanglement, a picture characterizing the structure of the entanglement between A and  $A^c$ . (See figure 9.) The initial EPR pairs along the greedy geodesic which are deep inside the bulk encode long-range entanglement between A and  $A^c$ , while the EPR pairs closer to the boundary encode shorter-range entanglement.

![](_page_17_Picture_2.jpeg)

**Figure 9.** A geometric map of bipartite entanglement. White dots represent physical spins distilled by applying local unitary transformations to A and  $A^c$ .

<span id="page-17-0"></span>We can likewise use the greedy algorithm to create a map of multipartite entangle-

ment, whether or not the conditions of Theorem 2 are satisfied. Suppose, for example, that we divide the boundary into four regions A, B, C, D, each of which is connected, as in figure 10. We may apply the greedy algorithm separately to each of the four regions, obtaining greedy geodesics  $\gamma_A^{\star}$ ,  $\gamma_B^{\star}$ ,  $\gamma_C^{\star}$ ,  $\gamma_D^{\star}$ . The bulk region in between A and its greedy geodesic  $\gamma_A^{\star}$  is called the causal wedge of A, denoted C[A]. (The significance of the causal wedge in holographic codes will be discussed at length in section 5.) As figure 10 indicates, the union  $C[A] \cup C[B] \cup C[C] \cup C[D]$  of the four causal wedges need not cover the entire bulk lattice — there may be a multipartite residual region in the bulk, which the greedy algorithm fails to reach when applied to the boundary regions one at a time. As we explain below, the size of the multipartite residual region is expected to be O(1), independent of the total system size.

![](_page_18_Picture_1.jpeg)

Figure 10. The "map of entanglement" and multipartite residual regions in a holographic state. For  $|A||C| \gg |B||D|$  it is possible for the residual region to pinch off so much that EPR pairs can be directly distilled between A and C. In other words, due to the discretization of the lattice, the causal wedges C[A] and C[C] may be adjacent in the bulk. In this case the residual region may be composed of two disconnected components,  $R_B$  and  $R_C$  which can contribute tripartite correlations. A similar analysis holds for  $|A||C| \ll |B||D|$ . For  $|A||C| \approx |B||D|$ , a single connected residual region R contiguous to the four causal wedges is expected and may contribute four-party correlations.

<span id="page-18-0"></span>Multipartite residual regions in the bulk can indicate multipartite entanglement among the four regions on the boundary. As discussed above for the case of bipartite entanglement, suppose we decouple spins in each of A, B, C, D by performing suitable local unitary transformations associated with each step of the greedy algorithm. Where the greedy geodesics of adjacent regions meet, EPR pairs are distilled, in keeping with

our observation in section [4.2](#page-12-0) that the bipartite entanglement of two boundary regions is no less than the length of the greedy geodesic shared by the two regions. The tensors trapped inside a multipartite residual region however, do not necessarily have a decomposition into EPR pairs. Instead it describes a state with multipartite entanglement, which cannot be expressed as a product of states with only bipartite entanglement.

Just as for a partition of the boundary into connected regions A and A<sup>c</sup> , we can reverse the order in which tensors are incorporated by the greedy algorithm to obtain a holographic quantum circuit of isometries which prepares the boundary state. When we partition the boundary into four connected regions, however, the input to the circuit includes more than just EPR pairs distributed along shared greedy geodesics and decoupled spins in the bulk; additional multipartite states associated with each connected component of the bulk multipartite residual region are also part of the input. The circuit factorizes into a product U<sup>A</sup> ⊗ U<sup>B</sup> ⊗ U<sup>C</sup> ⊗ UD, with each of the four unitary transformations acting within its own causal wedge to build the corresponding connected component of the boundary. Again, the greedy geodesics encode a "map" of the entanglement among A, B, C, D, now including a description of multipartite entanglement among all the regions as well as bipartite entanglement among pairs of regions. Two such maps are shown in figure [10;](#page-18-0) in these cases a single six-leg tensor is trapped in each connected component of the bulk multipartite residual region, though in general a more complex tensor network could be trapped inside as indicated in figure [7.](#page-13-1)

We may also argue that if the bulk has constant negative curvature, then for any partition of the boundary into O(1) connected components, the multipartite residual region is always O(1) in size. This statement is true for the Riemannian geometry of the hyperbolic plane, but is merely heuristic because it disregards subtleties arising from the discrete lattice structure of the bulk. For a two-dimensional Riemannian manifold, the Gauss-Bonnet theorem applied to the residual region R states that

<span id="page-19-0"></span>
$$\int_{R} K dA + \int_{\partial R} k_g ds = 2\pi \chi(R). \tag{4.11}$$

here K is the Gaussian curvature, k<sup>g</sup> is the geodesic curvature, and χ(R) is the Euler characteristic of the residual region, which is χ = 1 when R has the topology of a disk. If R is the interior of an m-gon whose sides are geodesics, [\(4.11\)](#page-19-0) says that the integral of K over R is the deviation of the sum of interior angles of the m-gon from the corresponding sum for an m-gon in flat space; the latter sum is (m − 2)π because the m-gon can be covered by m − 2 triangles. For the AdS space, the interior angles approach zero as the space becomes large compared to its curvature radius; therefore assuming uniform negative curvature K = −1/α<sup>2</sup> (where α is the AdS radius), we conclude that the volume of the residual region is

$$V(R) = \pi(m-2)\alpha^2. \tag{4.12}$$

In our tensor networks α is of order the length of a link; therefore V (R) is O(1) in lattice units if m is O(1), which establishes our claim.

Likewise, the bipartite residual region arising from a partition of the boundary into two regions A and A<sup>c</sup> , discussed in section [4.2,](#page-12-0) has size O(1) if A and A<sup>c</sup> both have O(1) connected components. Indeed, the bipartite residual region is contained in the multipartite residual region found by applying the greedy algorithm separately to each connected component of A and of A<sup>c</sup> .

### <span id="page-20-0"></span>4.4 Negative tripartite information

A useful characterization of multipartite entanglement is the tripartite information, defined as

$$I_3(A, B, C) \equiv S_A + S_B + S_C - S_{AB} - S_{AC} - S_{BC} + S_{ABC}. \tag{4.13}$$

For a general (mixed) tripartite quantum state, I<sup>3</sup> can take any real value. It is zero, though, for any tripartite pure state of ABC, since in that case SABC = 0 and e.g. regions A and BC, being complementary, have the same entropy and therefore make cancelling contributions to I3. Nor is there a contribution to I<sup>3</sup> from EPR pairs shared between a pair of the three regions (because e.g. a pair shared by AB yields positive contributions to S<sup>A</sup> and S<sup>B</sup> which are cancelled by negative contributions from −SAC and −SBC) or from entanglement shared between one of the three regions and a fourth disjoint region. Thus, for a holographic state and for any partition of the boundary into four regions A, B, C, D, nonzero contributions to I3(A, B, C) can arise only from the distilled multipartite states trapped in residual regions.

In the holographic setting, it has been shown that I<sup>3</sup> ≤ 0 follows from the RT formula [\[9\]](#page-61-10). For holographic states and codes, the non-positivity of I<sup>3</sup> is not ensured in general, because of the potential (small) violations of the RT formula. In some special cases, though, RT holds exactly, and the non-positivity of I<sup>3</sup> then follows. For example, suppose that we partition the boundary into four connected regions A, B, C, D, and that each connected component of the multipartite residual region traps just one perfect tensor. In that case there is no bipartite residual region, so Theorem [3](#page-15-1) implies that RT is exact and therefore I<sup>3</sup> ≤ 0. To see that there is no bipartite residual region in this case, consider the bipartite partition of the boundary into the two disconnected regions AC and BD, and consider an isolated 2n-index perfect tensor surrounded by three or all four of the greedy geodesics  $\gamma_A^{\star}$ ,  $\gamma_B^{\star}$ ,  $\gamma_C^{\star}$ ,  $\gamma_D^{\star}$ . This tensor must have at least n legs crossing either  $\gamma_A^{\star} \cup \gamma_C^{\star}$  or  $\gamma_B^{\star} \cup \gamma_D^{\star}$ . Therefore, when we apply the greedy algorithm to the boundary regions AC and BD, one cut or the other will advance past this isolated tensor, excluding it from the bipartite residual region.

Under suitable conditions we can actually prove a stronger result — that  $I_3$  is strictly negative. Let us say that a connected component of the multipartite residual region is three sided if surrounded by three of the four greedy geodesics, and four sided if surrounded by all four greedy geodesics. Three-sided components make no contribution to  $I_3$ ; if the three surrounding greedy geodesics are those of X, Y, Z, the symmetry of  $I_3$  implies  $I_3(A, B, C) = I_3(X, Y, Z)$ , which vanishes for any pure state of XYZ. But an isolated 2n-index perfect tensor which crosses all four greedy geodesics makes a negative contribution to  $I_3$ :

<span id="page-21-0"></span>**Theorem 4.** Suppose the 2n indices of a perfect tensor state are partitioned into four disjoint nonempty sets A, B, C, D such that 0 < |A|, |B|, |C|, |D| < n. Then the tripartite information  $I_3$  is strictly negative:  $I_3(A, B, C) < 0$ .

*Proof.* First we notice that for a four-part *pure* state ABCD, the tripartite information I(A, B, C) is actually completely symmetric under permutations of the four subsystems, which we can see by using the property that complementary regions have the same entropy in a pure state:

$$I_{3}(A, B, C) = S_{A} + S_{B} + S_{C} - S_{AB} - S_{BC} - S_{AC} + S_{ABC}$$

$$= S_{A} + S_{B} + S_{C} + S_{D} - \frac{1}{2}(S_{AB} + S_{CD} + S_{BC} + S_{AD} + S_{AC} + S_{BD}).$$

$$(4.14)$$

$$= (4.15)$$

We may therefore assume without loss of generality that  $|A| \leq |B| \leq |C| \leq |D|$  which implies  $|AB| \leq |CD|$  and  $|AC| \leq |BD|$ . Now we use the defining property of 2n-index perfect tensors, that a set of n or fewer indices is maximally entangled with its complement, which implies  $S_X = \min(|X|, 2n - |X|)$ , with entropy expressed in units of  $\log v$ . Therefore  $S_A = |A|, S_B = |B|, S_C = |C|, S_D = |D|$ , and furthermore  $S_{AB} = |AB|$  and  $S_{AC} = |AC|$ . Now we distinguish two cases. If  $|AD| \leq |BC|$ , then  $S_{BC} = S_{AD} = |AD|$  and we have

$$I_3(A, B, C) = |A| + |B| + |C| + |D| - |AB| - |AC| - |AD| = -2|A| < 0.$$
 (4.16)

If on the other hand  $|BC| \leq |AD|$ , then  $S_{AD} = S_{BC} = |BC|$  and we have

$$I_3(A, B, C) = |A| + |B| + |C| + |D| - |AB| - |AC| - |BC| = 2|D| - 2n < 0, \quad (4.17)$$

where to obtain the second equality we use |AB| + |AC| + |BC| = 2(|A| + |B| + |C|) = 2(2n - |D|). This completes the proof.

For a holographic state with boundary partitioned into sets A, B, C, D, the conditions of Theorem 4 are satisfied by an isolated perfect tensor trapped inside a four-sided component of the multipartite residual region; fewer than n of the tensor's legs cross any greedy geodesic, because otherwise the greedy algorithm would have moved the cut forward past this perfect tensor, which therefore would not be in the multipartite residual region. Furthermore, since entropy is additive for a product state,  $I_3$  is also strictly negative for any product of perfect tensor states shared by A, B, C, D, provided that at least one factor has support on all four sets. Since only the four-sided regions contribute to  $I_3$ , we conclude that  $I_3$  is strictly negative if the multipartite residual region contains at least one four-sided connected component, and if each four-sided connected component contains only one perfect tensor.

### <span id="page-22-0"></span>5 Quantum error correction in holographic codes

In this section we study the error correction properties of our holographic codes in more detail. The idea that a CFT with a gravity dual must have error correcting properties was recently proposed in [1], and in this section we will see that our holographic codes illustrate many aspects of the proposal of [1] quite explicitly.

#### <span id="page-22-1"></span>5.1 AdS-Rindler reconstruction as error correction

We begin by briefly recalling the main point emphasized in [1], which is that in AdS/CFT a bulk local observable can be realized by many different operators in the CFT. In fact, if x is any point in the bulk, and Y is any point on the boundary, the AdS/CFT dictionary can be chosen so that it maps the bulk local field  $\phi(x)$  to a CFT operator  $\mathcal{O}[\phi(x)]$  which has no support in an open set containing Y, and therefore commutes with any local field of the CFT supported near Y. Since Y is an arbitrary boundary point, if the CFT operator corresponding to  $\phi(x)$  were actually unique, we would conclude that  $\mathcal{O}$  commutes with all local fields in the CFT, and therefore is a multiple of the identity because the local field algebra is irreducible. This paradox is evaded once we recognize that the correspondence is not unique. If Y, Z are two distinct boundary points, the CFT operator corresponding to  $\phi(x)$  can be chosen to be either  $\mathcal{O}$ , which commutes with CFT local fields supported near Y, or  $\mathcal{O}'$ , which commutes with CFT local fields supported near Y, or  $\mathcal{O}'$ , which commutes with CFT local fields supported near Y, or  $\mathcal{O}'$ , which commutes with CFT local fields supported near Y, or  $\mathcal{O}'$ , which commutes with CFT local fields supported near Y, or  $\mathcal{O}'$ , which commutes with CFT local fields supported near Y, or  $\mathcal{O}'$ , which commutes with CFT local fields supported near Y, or  $\mathcal{O}'$ , which commutes with CFT local fields supported near Y, or  $\mathcal{O}'$ , which commutes with CFT local fields interchangeably for describing bulk physics.

![](_page_23_Picture_0.jpeg)

Figure 11. Bulk field reconstruction in the causal wedge. On the left is a spacetime diagram, showing the full spacetime extent of the causal wedge  $\mathcal{C}[A]$  associated with a boundary subregion A that lies within a boundary time slice  $\Sigma$ . The point x lies within  $\mathcal{C}[A]$  and thus any operator at x can be reconstructed on A. On the right is a bulk time slice containing x and  $\Sigma$ , which has a geometry similar to that of our tensor networks. The point x can simultaneously lie in distinct causal wedges, so  $\phi(x)$  has multiple representations in the CFT.

<span id="page-23-0"></span>This novel feature of AdS/CFT, that a bulk local observable can be represented by boundary CFT operators in multiple ways, is illustrated in figure 11. The idea is that any fixed-time CFT subregion A defines a subregion in the bulk, the causal wedge  $\mathcal{C}[A]$ . For any point  $x \in \mathcal{C}[A]$ , bulk quantum field theory ensures that any bulk local operator  $\phi(x)$  can be represented in the CFT as some nonlocal operator on A. This representation is called the AdS-Rindler reconstruction of the operator [34, 35]. Because a given bulk point x can lie within distinct causal wedges associated with different boundary regions, the bulk operator  $\phi(x)$  can have distinct representations in the CFT with different spatial support.

In [1] the non-uniqueness of the CFT operator corresponding to the bulk operator  $\phi(x)$  was interpreted as indicating that  $\phi(x)$  is a logical operator preserving a code subspace of the Hilbert space of the CFT. This code subspace is protected against "errors" in which parts of the boundary are "erased." If the boundary operator corresponding to  $\phi(x)$  acts on a subsystem of the CFT which is protected against erasure of the boundary region  $A^c$ , then this operator can be represented in the CFT as an operator supported on A, the complement of the erased region. Thus we may interpret the AdS-Rindler reconstruction of  $\phi(x)$  on boundary region A as correcting for the erasure of  $A^c$ ; choosing the erased portion of the boundary in different ways leads

to different reconstructions of φ(x). Moreover, operators near the center of the bulk are "well protected" in the sense that a large region needs to be erased to prevent their reconstruction, while operators near the boundary can be erased more easily by removing a smaller part of the boundary [\[1\]](#page-60-0).

We may think of this code subspace as the low-energy sector of the CFT corresponding to a relatively smooth dual classical geometry. All CFT operators are physical, and thus have some bulk interpretation, but the "logical" operators are special ones which map low-energy states to other low-energy states. The same logical action can be realized by distinct CFT operators, as these distinct operators act on high-energy CFT states (those outside the code subspace) differently even though they act on low-energy states in the same way.

### <span id="page-24-0"></span>5.2 The physical interpretation of holographic codes

The error-correcting properties of the AdS/CFT correspondence were motivated in [\[1\]](#page-60-0) by bulk calculations, together with plausibility arguments regarding the CFT. Our central observation in this paper is that analogous statements are provably true in holographic codes.

We emphasize that in holographic codes the uncontracted bulk legs hanging from each tensor should not be thought of as tensor factors in addition to the boundary legs. Rather the entire physical Hilbert space is spanned by states of the boundary legs only. The bulk legs just provide a way of conveniently describing states in a certain code subspace of this boundary Hilbert space, obtained by feeding states of the bulk legs through the isometry defined by the entire tensor network; this code subspace can be regarded as a simplified model of the low-energy states in a CFT.

Likewise, operators acting on the dangling bulk indices correspond to nonlocal operators in the boundary theory whose algebra and action on the code subspace resembles what we would expect for the CFT description of how bulk local operators act on low-energy CFT states. When we speak of a "bulk local operator" we really mean the nonlocal boundary operator obtained by pushing an operator acting on a dangling bulk index out to the boundary using the isometry defined by the network.

### <span id="page-24-1"></span>5.3 Bulk reconstruction from tensor pushing

We now explain how holographic codes realize the AdS-Rindler reconstruction of figure [11.](#page-23-0) The basic idea is that, instead of using the full isometry of the entire network to push a local bulk operator to the boundary, we can instead successively push it through individual perfect tensors in a manner of our choosing by using the operation of figure [2.](#page-5-1) We illustrate the reconstruction for two different bulk points of the pentagon code in figure [12.](#page-25-0) Here we use the defining property of perfect tensors — that the tensor provides a unitary transformation which maps any three legs of the tensor to the complementary set of three legs, and therefore also an isometry mapping any set of three or fewer "incoming" legs to any disjoint set of three "outgoing" legs. In figure [12,](#page-25-0) each bulk vertex with arrows showing incoming and outgoing directions indicates such an isometry, and the complete set of blue legs is a product of such isometries, and hence also an isometry. The blue operator on the boundary is obtained by conjugating the blue bulk operator by the blue isometry, and the same applies to the green bulk and boundary operators. In the construction of the isometry, we regard the dangling bulk index on each tensor as an incoming index, and therefore require that no more than two contracted indices are incoming for each blue (or green) tensor. The same blue isometry, then, can be used to push not just the central blue bulk index to the boundary, but also any of the other incoming bulk indices (which are not shown in the figure) on blue tensors.

![](_page_25_Picture_1.jpeg)

Figure 12. Boundary reconstruction of bulk operators. The blue operator on the central bulk leg is pushed to an operator supported on a fairly large boundary region, while the green bulk operator further from the center is pushed to an operator supported on a smaller boundary region. Bulk legs for the other tensors are not shown.

<span id="page-25-0"></span>The boundary operation corresponding to a given bulk local operator manifestly has the non-uniqueness we described in our discussion of the AdS-Rindler reconstruction. For example, we could move one of the three blue arrows directed outward from the central blue vertex to a different edge, thus reconstructing the central bulk operator on a different boundary region, or we could have sent the green arrows in the opposite direction and reconstructed the green bulk operator on a considerably larger boundary region on the opposite side. No matter which reconstruction we use, the boundary operator is obtained from the isometric embedding of the bulk indices into the code subspace of the boundary Hilbert space, and therefore each reconstructed operator corresponding to a given bulk operator acts on the code subspace in the same way.

In the theory of quantum error-correcting codes, we say that an error is an erasure (or equivalently a located error ) if the set of spins damaged by the error is known, so this information can be used in recovering from the error. Holographic codes also provide protection against errors which act at unknown locations on the boundary, but for the purpose of developing the analogy with the AdS/CFT correspondence we will focus on protecting against erasure. A logical system can be protected against erasure of a set of spins in the code block if the full algebra of logical operations has a realization supported on the complementary set of unerased spins. In AdS/CFT we might only require reconstruction of a subalgebra of the full logical algebra; for example, the pentagon code provides better protection for the degrees of freedom deep within the bulk than for those closer to the boundary. The framework in which a quantum code protects only a subalgebra of the code's full logical algebra has been called operator algebra quantum error correction [\[36](#page-62-16)[–39\]](#page-63-2).

### <span id="page-26-0"></span>5.4 Connected reconstruction and the causal wedge

Given a subregion A of the boundary, which bulk local operators can be reconstructed on A? This is not an easy question to answer in general, but at least we can give a simple description of a large logical subsystem reconstructable on A, namely those logical operators acting on bulk sites which are reachable using the greedy algorithm explained in section [4.](#page-10-0)

Recall that the greedy algorithm associates with any boundary region A a greedy geodesic γ ? <sup>A</sup> whose boundary matches the boundary of A, such that A and γ ? <sup>A</sup> enclose a tensor P<sup>A</sup> which defines an isometry mapping free bulk legs in P<sup>A</sup> together with the legs cut by γ ? <sup>A</sup> to A. Using this isometry applied to any operator acting on a bulk leg in PA(tensored with the identity acting on all the rest of the isometry's input indices), we may push that logical operator through the isometry to obtain its reconstruction on A. Let's call the position of a perfect tensor in the network a bulk point and say that the greedy algorithm reaches a bulk point if it moves the cut past that tensor, hence using it in the construction of P<sup>A</sup>

This operator reconstruction procedure can be applied to any boundary region A. In the special case where A is connected, it provides a precise analog of the AdS-Rindler reconstruction in holographic codes, which we can formalize with a definition and theorem:

**Definition 5.** Suppose that A is a **connected** boundary region. The **causal wedge** of A, denoted C[A], is the set of bulk points reached by applying the greedy algorithm to A.

<span id="page-27-1"></span>We then have:

**Theorem 5.** Suppose A is a connected boundary region. Then any bulk local operator in the causal wedge C[A] can be reconstructed as a boundary operator supported on A.

We could have formulated a geometric notion of the causal wedge, defining it as the set of bulk points enclosed between A and the actual minimal geodesic  $\gamma_A$ , rather than the greedy geodesic. This geometrical definition is closer in spirit to how the term "causal wedge" has been used in the context of AdS/CFT. But we prefer this greedy notion of causal wedge instead, so that Theorem 5 is correct as stated.

As figure 12 illustrates, bulk operators near the boundary can be reconstructed on smaller connected regions than bulk operators near the center, just as for the AdS-Rindler reconstruction in AdS/CFT. It is natural to wonder how large the connected region A should be for the operator at the center of the bulk to be reconstructable on A. This question is studied for the pentagon code in appendix C by investigating whether the greedy algorithm applied to A reaches the central tensor in the network. We find that a connected region of  $N_A$  boundary spins necessarily allows reconstruction of all operators acting on the center provided that A covers a sufficiently large fraction of the boundary, namely

<span id="page-27-2"></span>
$$f_A \equiv \frac{N_A}{N_{\text{boundary}}} > \frac{5 + \sqrt{5}}{10} \equiv f_c \approx .724.$$
 (5.1)

The analogous result for the AdS-Rindler reconstruction is  $f_c = 1/2$ , but the discreteness of our lattice introduces some additional overhead. It turns out, though, that because the tensor network is not invariant under translations of the boundary, whether the connected region A allows reconstruction of the center depends not just on the size of A but also on its location. In appendix C we show that, while the condition (5.1) is needed to guarantee reconstruction of the central operator on an arbitrary connected region, there are some connected regions with  $f_A = \frac{N_A}{N_{boundary}} = \frac{3+\sqrt{5}}{10} \approx .524$  that suffice for the reconstruction.

#### <span id="page-27-0"></span>5.5 Disconnected reconstruction and the entanglement wedge

Now let's consider what bulk operators can be constructed on boundary regions with more than one connected component. First we extend the definition of the causal wedge to disconnected regions: Definition 6. Suppose that A is a boundary region, which is a union of connected components A1, A2, . . .. The causal wedge of A, denoted C[A], is defined as the union of the causal wedges of the components of <sup>A</sup>, <sup>C</sup>[A] = <sup>S</sup> i C[A<sup>i</sup> ].

Since we have already established that any bulk operator in C[A<sup>i</sup> ] is reconstructable on A<sup>i</sup> if A<sup>i</sup> is connected, it follows immediately from this definition that even for disconnected regions any bulk operator in C[A] is reconstructable on A.

The causal wedge contains bulk operators which can be reconstructed when we apply the greedy algorithm to the connected components of A one at a time. But the greedy algorithm might advance further into the bulk, beyond the causal wedge, when applied to A instead. Specifically, there could be a 2n-index tensor just beyond the causal wedge of A with n or more legs crossing the union of greedy geodesics γ ? Ai ∪γ ? Aj , even though fewer than n legs cross γ ? Ai or γ ? Aj individually. Then applying the greedy algorithm to A<sup>i</sup> ∪A<sup>j</sup> moves the cut past this tensor. This step may then render further tensors eligible for inclusion, and in fact we will see that sometimes the greedy algorithm can move far beyond the causal wedge C[A]

![](_page_28_Picture_3.jpeg)

Figure 13. Disconnected reconstruction of a central operator beyond the causal wedge. Each of two separate connected boundary regions is too small for reconstruction of the central operator, yet the reconstruction is possible on the union of the two regions. In this example the greedy algorithm reaches the central tensor when applied to both connected components at once, but not when applied to either component by itself.

<span id="page-28-0"></span>A concrete first example illustrating reconstruction of a bulk operator outside the causal wedge is shown in figure [13.](#page-28-0) In this example, A is the union of two connected components A<sup>1</sup> and A2, and the full operator algebra of the central tensor can be pushed to either A<sup>c</sup> 1 or A<sup>c</sup> 2 . This implies that no nontrivial operator acting on the central tensor can be pushed to either A<sup>1</sup> or A2. For every nontrivial operator φ in the algebra there is another operator φ <sup>0</sup> which does not commute with φ. If φ 0 can be pushed to A<sup>c</sup> 1 , then surely φ cannot be pushed to A1, because operators supported on complementary regions must commute. The same argument applies to A2. Yet the greedy algorithm applied to A reaches the central tensor, showing that its full operator algebra can be pushed to the union of A<sup>1</sup> and A2.

That operators beyond the causal wedge of A can be reconstructed on A has deep potential implications for AdS/CFT. Perturbative gravity techniques like the AdS-Rindler reconstruction can be used to construct bulk operators in the causal wedge but not beyond. Yet there has been speculation in the literature that reconstruction should be possible in a larger region, the entanglement wedge [\[40\]](#page-63-0), see also [\[41,](#page-63-3) [42,](#page-63-1) [67\]](#page-64-0). In AdS/CFT, the entanglement wedge E[A] is defined by first finding the minimal area surface γ<sup>A</sup> used in the RT formula, and then drawing a codimension one (i.e., twodimensional for AdS3) spatial slice in the bulk whose only boundaries are γ<sup>A</sup> and A. The bulk domain of dependence of this slice is then defined as the entanglement wedge E[A]. The entanglement wedge contains the causal wedge, but can be much larger in some cases. Figure [14](#page-30-0) illustrates a simple example highlighting the distinction between the causal and entanglement wedges.[5](#page-0-0)

We would like to investigate whether bulk operators in the entanglement wedge are reconstructable for holographic codes, but how should the entanglement wedge be defined? A definition of E[A] close to that used in AdS/CFT is:

Definition 7. Suppose A is a (not necessarily connected) boundary region. The geometric entanglement wedge of A is the set of bulk points in the bulk region bounded by A and γA, where γ<sup>A</sup> is the minimal bulk geodesic whose boundary matches the boundary of A. If there is more than one minimal bulk geodesic, γ<sup>A</sup> is chosen to make the geometric entanglement wedge as large as possible.

The main motivation for the conjecture that operators in the entanglement wedge are reconstructable in AdS/CFT comes from the validity of the RT formula for disconnected regions. (Additional evidence was given in [\[1\]](#page-60-0) based on a typicality argument.) But we have already seen above that the RT formula does not hold exactly in holographic codes, so we should not necessarily expect the entanglement wedge conjecture

<sup>5</sup> In excited states where the geometry deviates from pure AdS, there are differences between the entanglement wedge and the causal wedge even for connected boundary regions. We will not try to capture this in our toy models, since without a theory of dynamics we cannot capture the full spacetime definitions of these regions. Our discussion is limited to the case where we stick with states near the vacuum, in which case A needs to be disconnected for its causal wedge and entanglement wedge to differ.

![](_page_30_Picture_0.jpeg)

Figure 14. The intersection of the entanglement wedge  $\mathcal{E}[A]$  with a bulk time-slice, in the case where A has two connected components. Minimal geodesics in the bulk are solid lines. When A is smaller than  $A^c$ , we have the situation on the left and the causal wedge agrees with the entanglement wedge. When A is bigger, however, the minimal geodesics switch and the entanglement wedge becomes larger. In particular the point in the center lies in the  $\mathcal{E}[A]$  but not  $\mathcal{C}[A]$ .

<span id="page-30-0"></span>to hold in detail for the geometric entanglement wedge. Instead, as in defining the causal wedge, we prefer a definition that makes the reconstructability manifest:

**Definition 8.** Suppose A is a (not necessarily connected) boundary region. The **greedy entanglement wedge** of A, denoted  $\mathcal{E}[A]$ , is the set of bulk points reached by applying the greedy algorithm to all connected components of A simultaneously.

With this definition, bulk local operators in  $\mathcal{E}[A]$  are automatically reconstructable in A, using the isometry defined by  $P_A$  to push these operators to the boundary. The greedy algorithm also ensures that the interior boundary of  $\mathcal{E}[A]$  is the greedy geodesic  $\gamma_A^*$ , though not necessarily the minimal geodesic  $\gamma_A$ .

A drawback of this definition is that  $\mathcal{E}[A]$  includes only the bulk local operators which can be reconstructed on A using the greedy algorithm; it might miss additional bulk operators which can be reconstructed by other methods. In fact we can find examples of codes such that some bulk local operators lying outside  $\mathcal{E}[A]$  can be reconstructed on A, as discussed in appendix E. These codes typically have special properties, such as symmetries, which make the reconstruction possible. If we know nothing more about the perfect tensors used to construct the code, aside from their perfection, we have no general reason to expect that bulk operators far outside the greedy entanglement wedge will be reconstructable. That said, we confess that we lack a complete understanding of when reconstruction is possible, and hope that further progress on this issue can be achieved in future work.

### <span id="page-31-0"></span>5.6 Erasure threshold

If the entanglement wedge conjecture is true for AdS/CFT, if holographic codes faithfully model the entanglement structure of boundary theories with classical gravitational duals, and if the greedy entanglement wedge is a reasonable stand-in for the entanglement wedge, then we should be able to find holographic codes and boundary regions such that the greedy entanglement wedge reaches far outside the causal wedge. In this section we provide examples which confirm this expectation. One way to formalize this is to choose A to be a randomly chosen set of boundary spins, whose size is a specified fraction of the total boundary. The geometry of the hyperbolic plane suggests that, if A is large enough, the causal wedge C[A] will stick close to the boundary, yet the entanglement wedge E[A] reaches the center of the bulk with high probability; we illustrate this in figure [15.](#page-31-1) We will see that not all holographic codes have this property, but we are able to provide concrete examples that do.

![](_page_31_Figure_2.jpeg)

<span id="page-31-1"></span>Figure 15. (a) When a boundary region A is partitioned into many connected components it may have a very shallow causal wedge C[A] if each connected component is small. (b) In contrast, if A comprises a sufficiently large fraction of the boundary, its entanglement wedge E[A] will extend deep into the bulk.

Another, perhaps better, way to formulate this case is to imagine a probabilistic noise model which acts independently (without any noise correlations) on each of the physical boundary spins, where each spin is either erased with probability p or left untouched with probability 1 − p. If p is small, the set A of unerased boundary spins breaks into many connected islands, where a typical island contains O(1/p) spins and has a causal wedge which reaches into the bulk by only a constant distance. We can show, though, that if the holographic code is properly chosen and the erasure probability p is less than a threshold value pc, then E[A] contains the central bulk spin with a success probability deviating from one by an amount which becomes doubly exponentially small as the radius of the bulk increases.

Which codes have an erasure threshold? One necessary requirement is that the code must have a distance that increases with the system size. For the purpose of reconstructing the central tensor in the bulk, this means that there should not be any logical operator supported on a constant number of boundary spins which acts nontrivially on the central bulk index. That's because erasure of any constant number of spins occurs with a nonzero constant probability, and recovery from the erasure error is not possible if a nontrivial logical operator has support on the erased qubits.

The pentagon code fails to fulfill this necessary condition. To illustrate the problem, it is helpful to consider first a simpler code, the "triangle code" constructed by contracting four-index perfect tensors, where each leg is a 3-level spin, a qutrit. Each triangle in the bulk has a dangling bulk index, and the code is constructed as a tensor network forming a tree, the Bethe lattice; each triangle is contracted with one triangle closer to the center and two triangles further from the center, as shown on the left side of figure [16a.](#page-32-0) (Qi's model [\[28\]](#page-62-8) is based on a tensor network with a similar structure.) One way to describe the greedy algorithm is to say that it propagates erasures from the boundary toward the center of the bulk — the inward directed leg of a triangle is erased if either of its outward directed legs is erased, and the central triangle can be reconstructed only if at least two of that triangle's legs are unerased.

<span id="page-32-0"></span>![](_page_32_Figure_3.jpeg)

Figure 16. Dangerous small erasures for the triangle (a) and pentagon codes (b). In the triangle code erasing two boundary spins, boxed in blue, can prevent reconstruction of the central tensor. In the pentagon code erasing four spins can prevent the reconstruction.

<span id="page-32-1"></span>It is easy, then, to prevent the greedy algorithm from reaching the center — only

two spins need to be erased. A single erasure on the boundary propagates all the way up to the center of the network, erasing one of the central triangle's legs. A single erasure on a different branch of the tree propagates up to another of the central triangle's legs, blocking the reconstruction of the central tensor on the remaining unerased spins.

The greedy algorithm fails for a good reason. As described in appendix [A.2,](#page-44-0) The logical algebra for the three-qutrit code represented by a single triangle is generated by logical operators of the form <sup>X</sup>¯ <sup>=</sup> <sup>X</sup> <sup>⊗</sup>X<sup>−</sup><sup>1</sup>⊗I, where <sup>X</sup> is a generalized Pauli operator; in fact the code is symmetric under permutation of the three qutrits, so we can choose X and X<sup>−</sup><sup>1</sup> to act on any two of the three qutrits without changing the operator's action on the code space. Now choose a path through the Bethe lattice which begins on one leaf, travels to the center, exits the center on a different branch, and finally reaches another leaf on that branch. Apply the operator X¯ to each of the logical bulk indices visited by this path. Then for each leg along the path the X from the triangle on one side cancels the X<sup>−</sup><sup>1</sup> coming from the triangle on the other side, except for one uncanceled X on one leaf and one X<sup>−</sup><sup>1</sup> on the other. We conclude that the code admits a logical operator acting nontrivially on the central triangle which has support on only two boundary spins. That is why the central bulk spin can be damaged by erasing only two boundary spins.

For the pentagon code the situation is only slightly better. If we pick just four spins at the positions shown on the right side of figure [16b,](#page-32-1) then the greedy algorithm applied to the complement of these four spins never absorbs any of the tensors adjacent to the dashed line. This failure is just a property of the graph defining the holographic code, but once again we can understand the failure by noting that there is a logical operator acting on the central pentagon supported on these four boundary spins, so erasing these four spins prevents central bulk operators from being reconstructed on their complement. Now we may consider a product of bulk logical operators acting on the pentagons just above and just below the dashed line. We use the logical operator of the five-qubit code <sup>X</sup>¯ <sup>=</sup> <sup>−</sup><sup>Z</sup> <sup>⊗</sup> <sup>X</sup> <sup>⊗</sup> <sup>Z</sup> <sup>⊗</sup> <sup>I</sup> <sup>⊗</sup> <sup>I</sup> described in appendix [A.1,](#page-42-1) where <sup>X</sup> and Z are Pauli operators (which square to one), and the operator's action is unchanged by cyclic permutations of the five qubits. Now X's applied from either side of the cut cancel on the legs crossed by the cut, and Z's applied from either side cancel for the legs just above and below the cut, leaving only four uncanceled Z's acting on the boundary qubits.

Of course, uncorrectable damage deep inside the bulk caused by erasing just a few boundary spins is not at all what we expect in AdS/CFT, where according to the entanglement wedge conjecture we should always be able to reconstruct the center of the bulk from a sufficiently large fraction of the boundary, whatever its shape or location. To obtain a better model for AdS/CFT we should modify the holographic code, thinning out the algebra of bulk logical operators, and hence reducing the rate of the code.

A code that works better can be obtained by a simple modification of the pentagon code — the modified tensor network is constructed by starting with a pentagon at the center and adding alternating layers of hexagons (with no dangling bulk indices) and pentagons (each with one bulk index) as the network grows radially outward. The associated network is depicted in figure 17. This change suffices to remove all the constant-weight logical operators acting nontrivally on the center and in fact we can prove that this pentagon/hexagon code has an erasure threshold. Numerical studies show that erasure can be corrected by the greedy algorithm with high success probability for  $p \leq p_c^{\rm greedy} \approx 0.26$ ; the erasure threshold  $p_c$  achieved by the optimal recovery method might be higher than  $p_c^{\rm greedy}$  if the tensors have further special properties aside from just being perfect.

<span id="page-34-1"></span>![](_page_34_Figure_2.jpeg)

<span id="page-34-2"></span><span id="page-34-0"></span>Figure 17. Tensor networks for holographic pentagon/hexagon codes with erasure thresholds, where neighboring polygons share contracted indices. In the network shown on the left, pentagons and hexagons alternate on the lattice; each pentagon carries one dangling bulk index, and hexagons carry no bulk degrees of freedom. The logical qubit residing on the central pentagon is well protected against erasure if the erasure probability on the boundary is below the threshold value  $p_c$ . In the network on the right, there is just a single bulk qubit located at the center; the rest of the network is similar to the holographic state constructed from hexagons only.

Since our main interest is in the reconstruction of the center of the bulk, in appendix D we study a code for which the only logical index resides at the center, also shown in figure 17. This code is almost the same as the holographic state obtained by contracting six-leg perfect tensors (hexagons), except that the tensor network contains one pentagon

at the center; we therefore call it the single-qubit hexagon code. We prove the existence of an erasure threshold for this code, and also derive an analytic lower bound on the threshold erasure rate p<sup>c</sup> ≥ 1/12. Numerical evidence indicates that the threshold is actually quite close to p<sup>c</sup> = 1/2.

The lower bound on the threshold is derived using a simplified and less powerful version of the greedy algorithm, the hierarchical recovery method, which begins at the boundary and proceeds inward toward the center of the bulk. A tensor at level j + 1 of this hierarchy is connected to at least four tensors at level j, and the level-(j + 1) tensor is erased if two or more of its level-j neighbors are erased. The proof proceeds by recursively deriving an upper bound on the erasure probability p<sup>j</sup> at level j, finding

$$p_j \le p_c \left(\frac{p}{p_c}\right)^{\lambda^j},\tag{5.2}$$

where p<sup>c</sup> = 1/12 and λ = 1+<sup>√</sup> 5 2 . Thus the erasure probability for the central tensor drops doubly exponentially with the radius of the bulk if p < pc, which means that the central tensor can be reconstructed on the set of unerased boundary qubits with very high probability.

A tricky aspect of the proof is that, because a single level-j tensor couples to two level-(j + 1) tensors, there are noise correlations which propagate from level to level. Fortunately, the hyperbolic geometry controls the spread of correlations, making the analysis manageable. In fact, correlations beyond nearest neighbors never arise. This is one advantage of using the hierarchical recovery method rather than the greedy algorithm. A similar proof strategy may also be applied to other holographic codes.

### <span id="page-35-0"></span>5.7 Holographic stabilizer codes

Stabilizer codes have been extensively studied in quantum coding theory, and are often used in applications to fault-tolerant quantum computing [\[43\]](#page-63-4). Here we describe how to construct a family of holographic codes which are also stabilizer codes. We introduce the stabilizer formalism to pave the way for section [5.8,](#page-38-0) where we study some geometrical properties of holographic stabilizer codes.

Stabilizer codes can be defined for higher-dimensional spins as well, but here we will assume the spins are qubits for simplicity. A Pauli operator acting on n qubits is a tensor product of Pauli matrices, that is, one of the 4<sup>n</sup> operators contained in the set

$$\{I, X, Y, Z\}^{\otimes n} \tag{5.3}$$

where I is the 2 × 2 identity matrix and X, Y, Z are the 2 × 2 Pauli matrices (often

denoted σx, σy, σz). We use [[n, k]] to denote a quantum code with k logical qubits embedded in a block of n physical qubits. We say that an [[n, k]] code is a stabilizer code (also called an additive quantum code), if the code space can be completely characterized as the simultaneous eigenspace of n − k commuting Pauli operators. These commuting Pauli operators are called the code's stabilizer generators because they generate an abelian group called the code's stabilizer group. The special case of a k = 0 stabilizer code is called a stabilizer state. We say that an n-index tensor is a stabilizer tensor if the corresponding n-qubit state is a stabilizer state.

For example, the six-index perfect tensor is a perfect stabilizer tensor, and holographic codes defined by tiling a hyperbolic geometry with pentagons are stabilizer codes. More generally, we may formulate the following theorem:

<span id="page-36-0"></span>Theorem 6. Consider a holographic code defined by a contracted network of perfect stabilizer tensors, and suppose that the greedy algorithm starting at the boundary reaches the entire network. Then the code is a stabilizer code.

To understand why Theorem [6](#page-36-0) is true we need to see how to construct the code's stabilizer generators. To be concrete, consider holographic codes constructed from tilings by hexagons and pentagons. The six-index perfect tensor defines a [[6,0]] stabilizer code, whose stabilizers are enumerated in appendix [A.1.](#page-42-1) As we have already noted, it also defines isometries from any set of 1, 2, or 3 indices to the complementary set of indices; these isometries may be regarded as the encoding maps for [[5, 1]], [[4, 2]], and [[3, 3]] stabilizer codes respectively.

To be specific, consider the [[5, 1]] code, and let M denote its isometric encoding map taking a one-qubit input to the corresponding encoded state in the code block of five qubits. We can characterize M by specifying how it acts on Pauli operators, which (together with the identity) span the space of operators acting on a single qubit. Since the Pauli group is generated by X and Z it suffices to specify

$$M: X \mapsto \bar{X}, \quad M: Z \mapsto \bar{Z},$$
 (5.4)

where X¯ and Z¯ are the code's logical Pauli operators, given explicitly in appendix [A.](#page-42-0) Similarly, the action on Pauli operators defines isometric encoders for the [[4, 2]] and [[3, 3]] stabilizer codes, except that for e.g. the [[4, 2]] code we specify the action on the four independent Pauli operators X1, X2, Z1, Z2, where the subscript 1, 2 labels the code's two logical qubits. For stabilizer codes the encoding isometry is always a Clifford isometry, meaning its action by conjugation maps k-qubit Pauli operators to n-qubit Pauli operators.

We already explained in section [3](#page-7-0) that when the condition of Theorem [6](#page-36-0) is satisfied then the encoding isometry for the holographic code can be obtained by composing the isometries associated with each perfect tensor in the network. A given tensor may have 0, 1, 2, or 3 incoming legs, including the dangling bulk leg (if the tensor is a pentagon) and all the incoming contracted legs, which are output legs from previously applied isometries. To prove Theorem [6](#page-36-0) then, it is enough to know that composing the encoding isometries of two stabilizer codes yields the encoding isometry of a stabilizer code.

To see how this works, it is helpful to think about the simple special case of a concatenated quantum code, for which the tensor network is a tree. Consider in particular a code with just one logical qubit — the central pentagon has one incoming logical leg and five outgoing legs, while every other tensor is a hexagon with one incoming leg and five outgoing legs. If the [[5, 1]] code is concatenated just once, the tensor network has five hexagons and describes a [[25, 1]] stabilizer code. To obtain this code's isometric map, we first apply the encoding isometry M of the [[5, 1]] to the logical qubit, and then apply M again to each one of the five outgoing qubits. If S denotes the stabilizer group of the [[5, 1]] code, then the stabilizer of the [[25, 1]] code will include S acting on each one of the five subblocks corresponding to the five hexagons in the tensor network. But it also includes elements which act collectively on four of the five hexagons. For example, as described in appendix [A.1,](#page-42-1) one of the stabilizer generators for the [[5, 1]] code is the Pauli operator X ⊗ Z ⊗ Z ⊗ X ⊗ I. The isometries associated with the five hexagons map this operator to <sup>X</sup>¯ <sup>⊗</sup> <sup>Z</sup>¯ <sup>⊗</sup> <sup>Z</sup>¯ <sup>⊗</sup> <sup>X</sup>¯ <sup>⊗</sup> <sup>I</sup>, where now X, ¯ <sup>Z</sup>¯ are the logical Pauli operators acting on the five outgoing qubits emanating from a single hexagon.

The same idea applies to more general compositions of code isometries. Suppose that S1, M<sup>1</sup> are the stabilizer group and encoding isometry for an [[n1, k1]] stabilizer code and that S2, M<sup>2</sup> are the stabilizer group and encoding isometry for an [[n2, k2]] stabilizer code. We may apply M<sup>2</sup> to m of the n<sup>1</sup> output qubits from M<sup>1</sup> along with k<sup>2</sup> − m additional input qubits (where m ≤ n<sup>1</sup> and m ≤ k2), thus obtaining an [[n<sup>1</sup> − m + n2, k<sup>1</sup> + k<sup>2</sup> − m]] code. In fact this code is a stabilizer code, whose stabilizer group is generated by S<sup>2</sup> and M2(S1); here we use a streamlined notation, in which it is understood that operators and maps are extended by identity operators where necessary, and we note that the elements of M2(S1) are Pauli operators because M<sup>2</sup> is a Clifford isometry. Thus we have proven Theorem [6.](#page-36-0) It is also worthwhile to note that the stabilizer group and encoding isometry for the holographic code can be efficiently computed by composing the isometries arising from the perfect tensors in the network.

### <span id="page-38-0"></span>5.8 Are local gauge constraints enough?

It has recently been argued that in AdS/CFT gauge constraints in the boundary CFT may pick out a small enough subspace of states to explain the error correcting properties of AdS/CFT [\[44\]](#page-63-5). The idea is that any gauge-invariant state already possess some nonlocal entanglement via the imposition of the gauge constraints, and that this might be enough to resolve the various paradoxes of [\[1\]](#page-60-0).[6](#page-0-0)

We can try to test this idea for the holographic stabilizer codes discussed in section [5.7.](#page-35-0) Since gauge constraints are spatially local, the argument of Ref. [\[44\]](#page-63-5) suggests that the code's stabilizer group should be locally generated, in the sense that it has a complete set of generators, each with support on a constant number of neighboring boundary qubits. In fact, though, holographic stabilizer codes do not have this property in cases where the greedy entanglement wedge reaches outside the causal wedge. This property poses no problem for the proposal of [\[1\]](#page-60-0) however, as those authors argued that energetic constraints should also be included in defining the code subspace.

Consider for example the disconnected boundary region A = A<sup>1</sup> ∪ A<sup>2</sup> in the pentagon code, depicted in figure [13.](#page-28-0) We have already seen that the full logical algebra of the central pentagon can be reconstructed on the disconnected region A1∪A2, but that no nontrivial logical operator acting on the central pentagon is supported on either one of the connected components A1, A2. In a stabilizer code, a logical Pauli operator supported on A<sup>1</sup> ∪ A<sup>2</sup> is a tensor product O = O<sup>A</sup><sup>1</sup> ⊗ O<sup>A</sup><sup>2</sup> of Pauli operators supported on A<sup>1</sup> and A<sup>2</sup> separately. In order to preserve the code space, this logical Pauli operator must commute with all of the code's stabilizer generators. But if the two components A<sup>1</sup> and A<sup>2</sup> are distantly separated and the stabilizer generators are geometrically local, then no stabilizer generator has nontrivial support on both A<sup>1</sup> and A2. Any stabilizer generator with no support on A<sup>2</sup> trivially commutes with O<sup>A</sup><sup>2</sup> , and if it commutes with O then it must commute with O<sup>A</sup><sup>1</sup> as well. Likewise, a stabilizer generator with no support on A<sup>1</sup> must commute with O<sup>A</sup><sup>2</sup> if it commutes with O. Therefore O<sup>A</sup><sup>1</sup> and O<sup>A</sup><sup>2</sup> are logical operators, and at least one is nontrivial if their product is, contradicting the hypothesis that no nontrivial logical operator is supported on either connected component of A. The conclusion is that the stabilizer generators cannot be geometrically local.

The above argument applies even to higher-dimensional holographic stabilizer codes. In the case were the boundary is one dimensional, we may simply appeal to a known

<sup>6</sup>The word "gauge" is sometimes used in quantum information theory in a way that is non-standard from the point of view of quantum field theorists. In quantum field theory, states that are not gaugeinvariant have no physical interpretation, and are not really part of the Hilbert space of the theory; they appear only as a mathematical convenience. This is what the authors of [\[44\]](#page-63-5) meant by gauge constraints, and it is what we mean here.

result in quantum coding theory, that a stabilizer code in one dimension with geometrically local generators has constant distance [\[45,](#page-63-6) [46\]](#page-63-7). Therefore, a one-dimensional code with a local stabilizer cannot have a positive erasure threshold.

### <span id="page-39-0"></span>6 Black holes and holography

In holographic codes, bulk operators are reconstructed only on a subspace of the boundary Hilbert space. This may seem troubling, since the holographic correspondence is supposed to assign a bulk interpretation to all possible states on the boundary. A resolution of this confusion was proposed in [\[1\]](#page-60-0) — a particular bulk operator might not always be reconstructable because it lies deep inside a black hole for most boundary states.[7](#page-0-0) In fact we can see this directly in our models if we incorporate black holes in a manner that we now describe.

To illustrate the idea, consider the pentagon code, but with the central tensor removed. The central tensor's one free bulk index has been replaced by five bulk indices, those which had previously been contracted with legs of the missing pentagon; the tensor network now provides an isometry mapping these five indices, together with the bulk legs on the remaining pentagons, to the boundary. Thus the code subspace of the boundary Hilbert space is larger than for the pure pentagon code. We interpret this enlarged code space as describing configurations of the bulk with a black hole in the center, whose microstate is determined by the input to the new bulk legs. The entropy of the black hole is the logarithm of the dimension of the Hilbert space of black hole microstates, or

$$S_{BH} = \log_2(2^5 - 2) \approx 4.9,$$
 (6.1)

since only four of the bulk spins are new and we shouldn't count states that were part of the original pentagon code subspace. We depict this construction in figure [18a](#page-40-1).

We can construct larger black holes by removing more central layers of the network; it is clear that their entropy scales with their horizon area, as predicted by Bekenstein and Hawking [\[49,](#page-63-8) [50\]](#page-63-9). As the black hole grows, the number of bulk legs outside the black hole decreases, so we can reconstruct fewer and fewer bulk local operators. Eventually the black hole eats up the entire network, and our isometry becomes trivial (and unitary). Thus our model really does assign a bulk interpretations to all boundary states, as demanded by AdS/CFT — most boundary states correspond to large black holes in the bulk.

<sup>7</sup>We are currently agnostic about the reconstruction of bulk operators just inside the horizon, which must be needed in some form to describe the experience of an infalling observer. This is a topic of much recent controversy [\[47,](#page-63-10) [48\]](#page-63-11), but we will not take sides here.

![](_page_40_Picture_0.jpeg)

Figure 18. A black hole in a holographic code, and the corresponding wormhole geometry.

<span id="page-40-1"></span>It is amusing to note that we can also describe configurations corresponding to the two-sided wormhole of [\[2\]](#page-61-0); we just prepare two networks with central black holes of equal size, and maximally entangle the bulk legs at their horizons, as shown in figure [18b](#page-40-1). It would be interesting to make contact with recent speculations about how the length of the wormhole relates to the complexity of the tensor network describing the state [\[51–](#page-63-12)[53\]](#page-63-13), although for that purpose we would probably need to incorporate dynamics into our model.

# <span id="page-40-0"></span>7 Open problems and outlook

A remarkable convergence of quantum information science and quantum gravity has accelerated recently, propelled in particular by a vision of quantum entanglement as the foundation of emergent geometry. We expect this interface area to continue to grow in importance, as practitioners in both communities struggle to develop a common language and toolset. This paper was spurred by the connection between AdS/CFT and quantum error correction proposed in [\[1\]](#page-60-0). We have strived to make this connection more concrete and accessible by formulating toy models which capture the key ideas, and we hope our account will equip a broader community of scientists to contribute to further progress. Indeed, much remains to be done.

First of all, the entanglement structure of holographic codes is not yet completely understood. We would like a more precise characterization of the violations of the Ryu-Takayanagi formula which can occur, and of the relationship between bulk residual regions and the multipartite entanglement of the boundary state. How is the greedy entanglement wedge different from the geometric entanglement wedge, and to what extent does the greedy entanglement wedge reach beyond the causal wedge?

We have not yet discussed the correlation functions of boundary observables in holographic codes because we do not have much to say. In a stabilizer state |ψi, where P and Q are Pauli operators, the expectation value hψ|P Q|ψi is either zero (if P Q anticommutes with an element of the stabilizer) or a phase (if P Q commutes with the stabilizer); the same conclusion applies to a stabilizer code unless P Q is a nontrivial logical operator preserving the code subspace. In contrast, two-point correlations in a CFT decay algebraically with distance; how might we recover this behavior in holographic codes? Perhaps algebraic decay is recovered for non-stabilizer holographic states, by defining suitable coarse-grained observables, or by injecting an encoded state such that bulk correlation functions decay exponentially as in Ref. [\[28\]](#page-62-8). Or we might replace perfect tensors by tensors which are nearly perfect.

The behavior of two-point correlators highlights one way our toy models differ from full-blown AdS/CFT, but there are other ways as well; for one, there is no obvious analog of diffeomorphism invariance in a lattice model. What features in our lattice model correspond to the 1/N corrections in the continuum theory? In AdS/CFT the AdS radius is large compared to the Planck scale when the bulk theory is weakly coupled, yet in the pentagon model for example the curvature scale is comparable to the lattice cutoff. To approximate flatter bulk geometries we should study more general tessellations, including higher dimensional ones. A particularly serious drawback of our toy models so far is that we have not introduced any bulk or boundary dynamics. Can holographic codes illuminate dynamical processes like the formation and evaporation of a black hole?

Finally, we have emphasized that holographic states and codes provide a concrete realization of some aspects of AdS/CFT, but they may also be interesting for other reasons, for example as models of topological matter. Furthermore, holographic codes generalize the concatenated quantum codes that have been extensively used in discussions of fault-tolerant quantum computing [\[43\]](#page-63-4), and might likewise be applied for the purpose of protecting quantum computers against noise. For this application it would be valuable to develop the theory of holographic codes in a variety of directions, such as studying tradeoffs between rate and distance, formulating efficient schemes for correcting more general errors than erasure errors, and finding ways to realize a universal set of logical operations acting on the code space.

### Acknowledgment

We thank Ning Bao, Oliver Buerschaper, Glen Evenbly, Daniel Gottesman, Aram Harrow, Isaac Kim, Seth Lloyd, Nima Lashkari, Hirosi Ooguri, Grant Salton, Kristan Temme, Guifre Vidal and Xiaoliang Qi for useful comments and discussions. We also have enjoyed discussions with Ahmed Almheiri, Xi Dong, and Brian Swingle, and with Matthew Headrick, about their independent and upcoming related work. FP, BY, and JP acknowledge funding provided by the Institute for Quantum Information and Matter, a NSF Physics Frontiers Center with support of the Gordon and Betty Moore Foundation (Grants No. PHY-0803371 and PHY-1125565). BY is supported by the David and Ellen Lee Postdoctoral fellowship. DH is supported by the Princeton Center for Theoretical Science.

### <span id="page-42-0"></span>A Perfect tensor examples

In this section we will present the 5-qubit code, the 3-qutrit code and discuss possibilities of constructing perfect tensors with a larger number of legs. The 5-qubit code is a qubit stabilizer code of the form introduced in section [5.7](#page-35-0) whereas the 3-qutrit code can be described through a natural generalization of the stabilizer formalism to higher spin dimensions.

### <span id="page-42-1"></span>A.1 5-qubit code and 6-qubit state

The five-qubit code is a [[5, 1, 3]]<sup>2</sup> perfect code with distance 3 encoding one logical qubit in five physical qubits. It is a stabilizer code with a stabilizer subgroup given by S = hS1, S2, S3, S4i, where

$$S_{1} = X \otimes Z \otimes Z \otimes X \otimes I$$

$$S_{2} = I \otimes X \otimes Z \otimes Z \otimes X$$

$$S_{3} = X \otimes I \otimes X \otimes Z \otimes Z$$

$$S_{4} = Z \otimes X \otimes I \otimes X \otimes Z.$$
(A.1)

<span id="page-42-2"></span>Note that S1S2S3S<sup>4</sup> = Z ⊗ Z ⊗ X ⊗ I ⊗ X and hence the group is manifestly invariant under cyclic permutations. As is the case in the stabilizer formalism, codes are characterized by an abelian stabilizer subgroup ([S<sup>i</sup> , S<sup>j</sup> ] = 0) and codespace is the joint +1 eigenspace for this group, code states satisfy

$$S_j|\psi\rangle = |\psi\rangle \qquad j = 1, \dots 4.$$
 (A.2)

In this case, there are two orthogonal codeword states.

Logical operators are unitary operators which preserve the codeword space, but may act non-trivially on it. They are given by

<span id="page-43-0"></span>
$$\overline{X} = X \otimes X \otimes X \otimes X \otimes X \qquad \overline{Z} = Z \otimes Z \otimes Z \otimes Z \otimes Z.$$
 (A.3)

One may see that both X and Z commute with all the stabilizer generators, so they indeed preserves the codeword space. Yet, they anti-commute with each other, so they characterize one logical qubit, and X and Z behave as logical Pauli-X and -Z operators for a logical qubit. Namely, one can denote two codeword states by <sup>|</sup>˜0<sup>i</sup> and <sup>|</sup>˜1<sup>i</sup> such that <sup>Z</sup>|˜0<sup>i</sup> <sup>=</sup> <sup>|</sup>˜0i, <sup>Z</sup>|˜1<sup>i</sup> <sup>=</sup> −|˜1i, <sup>X</sup>|˜0<sup>i</sup> <sup>=</sup> <sup>|</sup>˜1i, <sup>X</sup>|˜1<sup>i</sup> <sup>=</sup> <sup>|</sup>˜0i. Applications of stabilizer generators to logical operators do not change the action on the codeword space, so representations of logical operators are not unique. Then one can introduce the following equivalence relations among logical operators

$$\overline{Z} \sim \overline{Z}U \qquad \overline{X} \sim \overline{X}U \qquad \text{where} \quad U \in \mathcal{S}$$
 (A.4)

as equivalent logical operators act in the same way on the codeword space. In particular, one can conclude that on the codespace, <sup>X</sup>¯ ∼ −<sup>Z</sup> <sup>⊗</sup> <sup>X</sup> <sup>⊗</sup> <sup>Z</sup> <sup>⊗</sup> <sup>I</sup> <sup>⊗</sup> <sup>I</sup> or any cyclic permutation thereof by multiplying eq. [A.3](#page-43-0) by stabilizer generators in eq. [A.1.](#page-42-2) In the five-qubit code, one can show that logical operators must act non-trivially on at least three physical qubits (weight 3) and the reduced density matrices on any two physical qubits is always maximally mixed.

One can convert the five-qubit code into a six-qubit perfect state. Imagine that we add one extra qubit to the five-qubit code such that the new qubit is entangled with a logical state of the five-qubit code. To be specific, we consider a six-qubit state whose stabilized by S <sup>0</sup> <sup>=</sup> <sup>h</sup><sup>S</sup> 0 1 , S<sup>0</sup> 2 , S<sup>0</sup> 3 , S<sup>0</sup> 4 , S<sup>0</sup> 5 , S<sup>0</sup> 6 i, with generators are given by

$$S'_{1} = X \otimes Z \otimes Z \otimes X \otimes I \otimes I$$

$$S'_{2} = I \otimes X \otimes Z \otimes Z \otimes X \otimes I$$

$$S'_{3} = X \otimes I \otimes X \otimes Z \otimes Z \otimes I$$

$$S'_{4} = Z \otimes X \otimes I \otimes X \otimes Z \otimes I$$

$$S'_{5} = X \otimes X \otimes X \otimes X \otimes X \otimes X \otimes X = \overline{X} \otimes X$$

$$S'_{6} = Z \otimes Z \otimes Z \otimes Z \otimes Z \otimes Z \otimes Z = \overline{Z} \otimes Z.$$

$$(A.5)$$

Here we have "recycled" stabilizer generators S1, . . . , S<sup>4</sup> from the five-qubit code:

$$S'_j = S_j \otimes I$$
 for  $j = 1, \dots, 4$ . (A.6)

We then constructed new stabilizer generators  $S'_5$  and  $S'_6$  from logical operators of the five-qubit code as follows:

$$S_5' = \overline{X} \otimes X \qquad S_6' = \overline{Z} \otimes Z$$
 (A.7)

where  $\overline{X}$  and  $\overline{Z}$  act on five qubits. One may easily check that stabilizer generators commute with each other. The wavefunction is specified by

$$S'_{j}|\psi\rangle = |\psi\rangle \qquad j = 1, \dots, 6,$$
 (A.8)

and the six-qubit state is given by  $|\psi\rangle = |\tilde{0}\rangle \otimes |0\rangle + |\tilde{1}\rangle \otimes |1\rangle$ . From the construction, one can see that  $\rho_A \propto I_A$  if  $|A| \leq 3$ . It turns out that this conversion is generic. That is, one can always convert a perfect code with 2n-1 spins into a perfect state with 2n spins.

### <span id="page-44-0"></span>A.2 3 -qutrit code and 4-qutrit state

One of the simplest examples of perfect tensors is given by the three qutrit code. This stabilizer code allows encoding one logical qutrit onto three physical qutrits in a way that it may be recovered even after erasure of any single physical qutrit. The reason for providing this additional example at this point is that we believe that this family of perfect tensors may naturally be suited to generalizations leading to a continuum type limit.

The code states for this code can be given as follows.

$$\sqrt{3}|\tilde{0}\rangle = |000\rangle + |111\rangle + |222\rangle$$
$$\sqrt{3}|\tilde{1}\rangle = |012\rangle + |120\rangle + |201\rangle$$
$$\sqrt{3}|\tilde{2}\rangle = |021\rangle + |102\rangle + |210\rangle.$$

Correspondingly, the perfect state can be given explicitly as

$$\begin{split} 3|[[4,0,3]]_3\rangle =& |0000\rangle + |1110\rangle + |2220\rangle \\ +& |0121\rangle + |1201\rangle + |2011\rangle \\ +& |0212\rangle + |1022\rangle + |2102\rangle. \end{split}$$

The  $[4,0,3]_3$  state is determined by the following stabilizer group

$$S = \langle ZZZI, ZZ^{-1}IZ, XXXI, XX^{-1}IX \rangle, \tag{A.9}$$

where we have omitted the three tensor product operator ⊗ between the qutrit Pauli operators

$$I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \quad X = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \quad Z = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \omega & 0 \\ 0 & 0 & \omega^2 \end{pmatrix} \quad \omega = e^{2i\pi/3}. \tag{A.10}$$

From this presentation of the stabilizer group, it becomes clear that this perfect state corresponds to a self dual CSS code. [8](#page-0-0) This separation of X and Z type operators, and treating them on similar footing may potentially allow generalization to continuum variable where position and momentum conjugate variables play a similar role.

Like any other maximally entangled stabilizer state, given a bipartition, the [[4, 0, 3]]<sup>3</sup> perfect state may be interpreted as a unitary gate belonging to the generalized Clifford group. A second reason for presenting this code is that we can provide a simple and explicit presentation of the corresponding Clifford circuit. In the case of the [[4, 0, 3]]3, the corresponding Clifford is composed to two controlled adder gates which are run in opposite directions one after the other.

$$U_{[[4,0,3]]_3} = |x_1, x_2\rangle \to |2x_1 + x_2, x_1 + x_2\rangle =$$
(A.11)

### <span id="page-45-0"></span>A.3 Large n

In order to obtain perfect tensors for large n, one needs to increase v as well, with the first known construction [\[54\]](#page-63-14) having v ∝ O(n). A construction with v ∝ O( √ n) was later proposed [\[55\]](#page-64-1).

While perfect tensors are essential in guaranteeing the isometric properties used in the analysis of holographic codes, they do require a large degree of fine tuning for their construction. An interesting observation is that according to canonical typicality, most pure states are almost maximally entangled along any balanced bi-partition [\[56,](#page-64-2) [57\]](#page-64-3). Hence Haar random states may in some sense provide a good approximation to perfect states. This is not meant in the sense of trace distance. The observation is that random states will except for a measure zero subset have full rank along any bipartition. This allows operators to be pushed from lower dimensional side to higher dimensional side in a way similar to figure [2.](#page-5-1) The only difference being that in this case normalization is not preserved (if it was there to begin with). Furthermore, the average bipartite entanglement of random states is very close to maximal. For this reason, we might expect that they typically do not change normalization too drastically.

<sup>8</sup>For CSS codes, the stabilizer group can be decomposed into X part and Z part. Self-dual means that the stabilizer subgroups for the X and the Z part have exactly the same form.

### <span id="page-46-0"></span>B Proof of RT for negatively curved planar graphs

As we have presented in eq. [4.4,](#page-11-1) there is an upper bound on the amount of entanglement a tensor network state can have based on the minimal cut γ<sup>A</sup> dividing the network into two tensors P and Q. In this section, we will explain how to guarantee that this upper bound is saturated for connected regions in a certain class of holographic states. Namely, we shall focus on holographic states associated to planar graphs with nonpositive curvature.

We argued that proving the RT formula amounts to showing that the tensors P and Q can be interpreted as unitary transformations, from the minimal geodesic cut γ<sup>A</sup> together with some subregion of A or A<sup>c</sup> to the rest of A or A<sup>c</sup> respectively. We will show that this is indeed the case by giving unitary circuit interpretations to the tensor networks for each of them.

Indeed, the following are necessary and sufficient conditions for a circuit interpretation of a network of perfect tensors:

- Covering: Each edge (contracted or uncontracted index) is assigned a directionality.
- Flow: Each tensor has an equal number of incoming and outgoing indices.
- Acyclic: The resulting directionality has no closed cycles (no loops).

The covering condition is necessary to interpret the direction in which each tensor in the network processes information by having well defined inputs and outputs. The flow condition is necessary for the interpretation of every tensor to be that of a unitary gate. The acyclic condition is non-local and guarantees that the order of application of the operations in the network is consistent, where an inconsistency may be thought of as the presence of closed time-like curves in the circuit picture. These conditions are enough to show that the interpretation is that of a unitary quantum circuit.

One additional condition is required in order to prove the saturation of the RT entanglement entropy, for a simply connected boundary region A.

• Equal time interpretation: The minimal cut γ<sup>A</sup> is crossed in the same direction by the directed interpretation of each link that it cuts.

This condition allows viewing the geodesic as an "equal time" curve in the unitary circuit interpretation of the tensor network.

Let us first describe the construction for the circuit interpretation. The steps may be readily visualized in figure [19a.](#page-48-0)

In a planar graph we can associate a minimal cut γ<sup>A</sup> to a path through the dual graph, and since we are taking A to be connected, this path will also be connected. We may associate two nodes in the dual lattice at the end points of a simply connected boundary region A, which will also be the endpoints of γ<sup>A</sup> in the dual lattice. We will take one of these nodes to be the starting node and label it 0. We may then label all other nodes in the dual lattice according to the distance (number of steps/cuts) from the starting node. Since γ<sup>A</sup> is a minimal geodesic, this labeling monotonically increases along the nodes it traverses.

We may now assign an orientation to edges (contracted indices) in the tensor network. The orientation is chosen such that, from the two adjacent nodes of the dual lattice, the node with higher label is always found to the right. This orientation may be interpreted as the direction of "flow of information" through the circuit.

We now argue that this orientation gives a unitary circuit interpretation for P (and thus for Q by exchanging A and A<sup>c</sup> ). We emphasize that the argument rests on the following assumptions about the graph:

- Planar embedding: The tensor network may be laid out in a planar fashion with the boundary of the network corresponding to a simple boundary on the embedding.
- Perfect tensors: Tensors in the network have an even number of legs and are unitary along any balanced distribution of the legs.
- Curvature: The network is expected to represent an AdS bulk and thus is expected to have the discrete analogue of negative curvature. We have not tried to define this idea in general, but the aspect of it we need here is that the distance function between two nodes of the network has no local maxima away from the boundary.

We have already used the planar embedding assumption implicitly by constructing the dual lattice and referring to right and left. It is however less obvious that we have also made a restricted use of the perfect tensor assumption. Namely, we have used the fact that each tensor has an even number of legs. Because of this, the dual lattice is bipartite. In other words, nodes may be labeled with two "colors" which we shall conveniently call 'even' and 'odd' such that two nodes of the same color are never adjacent. In particular, the parity of the distance labeling coincides with the "color". Hence, two neighboring nodes can not have the same value label making the directionality of the tensor index between them always be well defined (i.e. satisfies covering condition).

To ensure the flow condition, it suffices to count the number of incoming indices minus the number of outgoing indices and verify that this value is zero. Due to the triangle inequality, and the bipartite nature, labels for neighboring nodes can only differ by one. Hence, the difference between the number of outgoing and incoming indices for any tensor in the network is given by P<sup>2</sup><sup>n</sup> <sup>j</sup>=1 (fj+1 − f<sup>j</sup> ) = 0, where f<sup>j</sup> are the labels associated to the 2n nodes immediately surrounding the tensor taken in cyclic order.

The acyclic condition is a bit more subtle since it is a non-local property. We will prove that the presence of a cycle in this context implies the existence of an interior local maximum for the labeling. Let us assume that our construction produces some cycle C in the tensor network. Depending on the orientation of C (clockwise or counterclockwise), the the node label values immediately to the interior of the loop will be larger or smaller than those immediately to the exteriors. In the counterclockwise case, we may chose a node in the interior of C with lowest possible label. The label for this node is smaller than those of all its neighbors, including those in the exterior of C,

<span id="page-48-0"></span>![](_page_48_Figure_2.jpeg)

Figure 19. Here we illustrate how to construct a unitary circuit interpretation of a holographic state which witnesses the RT entanglement for a simply connected boundary region. (a) The following steps for the construction are illustrated: i) Label the node located at one end of the boundary as 0. ii) Label all other nodes according to the distance from this node. iii) Direct all tensor indices such that the larger label lies to the right. (b) In the example, the circuit interpretation for the network has depth 12. For this reason we provide a full sequential presentation of the circuit interpretation along one side of the geodesic, condensing the remaining 7 gates into UA<sup>c</sup> . Note that there are outputs that are produced directly by UA, without going through UA<sup>c</sup> as well as inputs that are fed directly to UA<sup>c</sup> without going through UA.

<span id="page-49-2"></span>![](_page_49_Picture_0.jpeg)

**Figure 20**. The first few levels of the unwrapped pentagon code. The dangling logical legs are not shown, and the "hollow" lines and dots are identified with the solid ones on the other side. The tensors in the top row have all remaining non-logical legs extended outwards and treated as physical qubits.

which contradicts the assumption that it is defined based on a graph distance function. In the clockwise case, we may choose a node in the interior of C with the largest possible label. In this case the label for this node is larger than that of all its neighbors, including those outside of C. In other words, we have found an interior maximum for the distance function. This is in contradiction with our stand-in assumption associated to negatively curved surface homeomorphic to the disc, which leads us to the conclusion that our construction produces no loops.

Finally, it is straightforward to show that the geodesic  $\gamma_A$  can be provided an *equal* time interpretation in the circuit. Firstly, it completely splits the circuits in two parts. Secondly, the direction associated to all contracted indices crossed by  $\gamma_A$  is uniform since the nodes it transverses are by definition labeled in strict ascending order.

### <span id="page-49-0"></span>C Counting tensors in the pentagon code

#### <span id="page-49-1"></span>C.1 Counting tensors

In this appendix we compute some basic properties of the pentagon code that we quoted in the text. In these computations it is useful to "unwrap" the code, as in figure 20. The central tensor is placed at the bottom, which we will refer to as the zeroth layer, the first five tensors as the first layer, and so on, with the layer number n being equivalent to the graph distance to the central tensor.

At each layer, it is clear that there are two kinds of tensors: those with one leg connected to the previous layer and those with two. We will denote the numbers of these at layer n as  $f_n$  and  $g_n$ , so for example  $f_1 = 5$  and  $g_1 = 0$ . Moreover if we group these together as a two component vector, we have the recursive equation

$$\begin{pmatrix} f_{n+1} \\ g_{n+1} \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} f_n \\ g_n \end{pmatrix}. \tag{C.1}$$

Applying this equation repeatedly we can compute the number of tensors of either type at any n via

$$\begin{pmatrix} f_n \\ g_n \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}^{n-1} \begin{pmatrix} 5 \\ 0 \end{pmatrix}. \tag{C.2}$$

This is easily computed by diagonalizing the matrix M ≡ 2 1 1 1 , at large n we have

$$f_{n} = \frac{5 - \sqrt{5}}{2} \left( \frac{3 + \sqrt{5}}{2} \right)^{n} \left[ 1 + O\left( \left( \frac{3 - \sqrt{5}}{3 + \sqrt{5}} \right)^{n} \right) \right]$$

$$g_{n} = \frac{3\sqrt{5} - 5}{2} \left( \frac{3 + \sqrt{5}}{2} \right)^{n} \left[ 1 + O\left( \left( \frac{3 - \sqrt{5}}{3 + \sqrt{5}} \right)^{n} \right) \right]. \tag{C.3}$$

If we truncate at layer n, the total number of boundary qubits is

$$N_{boundary} = 4f(n) + 3f(n) \tag{C.4}$$

and the total number of bulk tensors is

$$N_{bulk} = 1 + \sum_{k=1}^{n} (f_k + g_k). \tag{C.5}$$

Asymptotically we have

<span id="page-50-1"></span>
$$\frac{N_{bulk}}{N_{boundary}} \to \frac{1}{\sqrt{5}} \approx .447,$$
 (C.6)

which reproduces equation [\(3.1\)](#page-9-0).

### <span id="page-50-0"></span>C.2 Connected reconstruction

We'll now compute the size of connected boundary region that we need to reconstruct operators on the logical leg of the central (n = 0) tensor. This is complicated by the fact that our network is not translationally invariant; whether or not we can reconstruct the center depends not only on the size of the boundary region we have access to but also where it is. The "best case" situation is illustrated in figure [21.](#page-51-0)

We can compute the number of physical qubits in the best-case region by growing the tree it bounds: we start with f<sup>1</sup> = 3 and g<sup>1</sup> = 0, and then proceed as before by applying M repeatedly, being careful to remove two tensors at the ends at each layer.

![](_page_51_Picture_0.jpeg)

**Figure 21**. The best-case reconstruction of the center; we need to use only three "branches" of the tree, and in the outer branches we can choose to push "inwards" every time.

<span id="page-51-1"></span><span id="page-51-0"></span>![](_page_51_Picture_2.jpeg)

**Figure 22**. The worst-case reconstruction of the center; we are just barely not able to use the second branch, so we need to use the third, fourth, and fifth.

This tree thus obeys the modified recursion relation

$$\begin{pmatrix} f_{n+1} \\ g_{n+1} \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} f_n \\ g_n \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \tag{C.7}$$

which has solution

$$\begin{pmatrix} f_n \\ g_n \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}^{n-1} \begin{pmatrix} 3 \\ 0 \end{pmatrix} - \sum_{k=0}^{n-2} \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}^k \begin{pmatrix} 0 \\ 1 \end{pmatrix}. \tag{C.8}$$

After cutting off the tree at level n the number of physical qubits in the best-case region will be  $N_{best} = 4f_n + 3g_n - 3$ , and by diagonalizing M we see that asymptotically

$$\frac{N_{best}}{N_{boundary}} \to \frac{3 + \sqrt{5}}{10} \approx .524. \tag{C.9}$$

We can also study the "worst case" location of the region, which is shown in figure 22. To compute its size in the large n limit we only need to replace the initial condition  $f_1 = 3, g_1 = 0$  by  $f_1 = 4, g_1 = 0$ , and we find

$$\frac{N_{worst}}{N_{boundary}} \to \frac{5 + \sqrt{5}}{10} \approx .724, \tag{C.10}$$

which reproduces (5.1).

We can connect this worst-case result to the "bad" sets of points from figure 16b that prevent a general threshold for this code: these points are shown in figure 23.

![](_page_52_Figure_0.jpeg)

<span id="page-52-1"></span>**Figure 23**. Locations of the "bad" points from figure 16b. If the worst-case region were just a little smaller on the right it wouldn't contain any of them so, it wouldn't be able to reconstruct the center.

Similar calculations are possible in the pentagon-hexagon code we introduced to restore the threshold, we find

$$\frac{N_{bulk}}{N_{boundary}} \rightarrow \begin{cases} \frac{3\sqrt{6}-4}{38} \approx .088 & n \text{ odd} \\ \frac{3\sqrt{6}+4}{38} \approx .299 & n \text{ even} \end{cases}, \tag{C.11}$$

with the two cases being whether the last layer is taken to be pentagons (n even) or hexagons (n odd). The rate is thus relatively small compared to (C.6), which suggests that this code should be better protected against erasures, as indeed we find. The rate when n is odd is smaller since it throws in an extra level of hexagons without any new logical legs. We can also compute the sizes of the best and worst case connected reconstructions of the center, we find

$$\frac{N_{best}}{N_{tot}} \to \frac{6 + \sqrt{6}}{20} \approx .422$$

$$\frac{N_{worst}}{N_{tot}} \to \frac{10 + \sqrt{6}}{20} \approx .622.$$
(C.12)

These are smaller than the pentagon results, as expected since the code is denser, and are closer to the AdS/CFT value of 1/2.

# <span id="page-52-0"></span>D Estimating greedy erasure thresholds

Noise models which are independent and identically distributed (i.i.d.) are usually analytically tractable while providing reasonable predictive capability based on the few parameters defining the individual noise model. In the case of erasure noise, this is particularly simple since the only parameter is  $\epsilon$ , the erasure probability per qubit. In addition to randomized bench-marking it is sometimes instructive to provide analytic bounds on how small the error/erasure probability needs to be in order to guarantee a recovery probability for the encoded data which approaches unit. This can give us information about the scaling of the logical error probability with other parameters of

the code. A complementary approach consists of providing precise numerical estimates of the threshold value p<sup>c</sup> based on numerical simulations.

### <span id="page-53-0"></span>D.1 Analytic bounds

In this section, we derive such an analytic upper bound on the probability of logical error. The goal of the section is to provide an example of how such a bound is derived illustrating a proof technique and obtaining a functional form for the logical error probability. We do not strive to derive a tight bound or address a particularly relevant holographic code scenario. In fact, the recovery procedure we model is strictly weaker than the one provided by the greedy algorithm which is itself weaker than an optimal erasure recovery algorithm. The model we analyze is essentially identical to the holographic hexagon state except that instead of starting from a single [[6, 0, 4]] tensor at the center, we start with a single [[5, 1, 3]] and build up n layers of [[6, 0, 4]] tensors from there. We shall call this the single qubit hexagon code and its analysis is essentially identical to that of a holographic hexagon state.

For this code we obtain the following conclusion.

Theorem 7. Consider a single qubit hexagon code with n layers and an i.i.d. erasure probability for physical qubit given by ≤ ? . Then it is possible to recover the central logical qubit with probability p greater than

$$p \ge 1 - \epsilon^* \left(\frac{\epsilon}{\epsilon^*}\right)^{\lambda^n}. \tag{D.1}$$

Here, 
$$\epsilon^* = 1/12$$
 and  $\lambda = \frac{1+\sqrt{5}}{2}$ .

This is the same functional form associated to concatenated error correcting codes. Namely, the loss probability for the logical data decays doubly exponentially with the "depth" n of the code or exponentially with the number of physical spins. We would expect to get a result of the same form for any such code with an erasure threshold. The only expected difference being the value of the threshold ? and the scaling dimension λ. We will now prove the theorem as an illustration to obtaining these values. Since we will use a simplified hierarchical recovery procedure, the proof technique will be essentially equivalent to that of concatenated codes. An interesting open problem is to provide an analytic threshold analysis fully respecting the greedy algorithm which corresponds to the problem of bootstrap percolation [\[58\]](#page-64-4). We have numerically analyzed this problem or the qubit hexagon code and found ? ≈ 0.48(2) whereas independent analytic arguments particular to this model predict an erasure threshold of ? = 1/2 for an optimal recovery protocol.

Proof. We will consider a hierarchical recovery model which is even simpler and can not perform better than the greedy algorithm. Namely, we may provide a coupling [\[59\]](#page-64-5) between the probability distributions over recovered tensors such that the set of recovered tensors by the greedy algorithm always includes the set of tensors recovered by the hierarchical recovery. The reason for this is that the hierarchical algorithm can be interpreted as n iterations of the greedy algorithm where tensors a distance j from the boundary may be incorporated only during iteration j. The difference with the greedy algorithm, is that once the greedy algorithm recovers a tensor at distance j + 1 from the boundary, it allows itself to reinspect its neighboring tensors at distance j and incorporate those. This may in general lead to highly non-trivial sequences for incorporating tensors in the bulk. The sequential nature of the hierarchical recovery model allows establishing a clear dependence between the tensors.

In the hierarchical recovery model, each level consists of a ring of tensors, which are only connected with the next level and the previous. In order to adequately model the errors at each level, we will need to inductively provide bounds for different error configurations. Assuming we are dealing with the hexagon lattice with four hexagons adjacent per vertex, it will be sufficient to deal with two types of bounds, one for single errors (single missing tensor) and the second for pairs of neighboring missing tensors. We will call these bounds s and d for single and double and we will use a subindex j to label the layer to which these bounds apply.

Initially, we have s<sup>0</sup> = and d<sup>0</sup> = <sup>2</sup> which corresponds to assuming an i.i.d. erasure model with each physical index being erased with probability . The core of the proof is simply to recursively bound sj+1 and dj+1 in terms of s<sup>j</sup> and d<sup>j</sup> .

A non-trivial observation, is that we do not need to consider erasure correlations beyond nearest neighbors. Due to the hierarchical structure which is contracting, correlated erasures beyond nearest neighbors of a chain can not exist (see figure [24\)](#page-55-0). This is an artifact of having chosen a privileged "re-normalization" direction and is an effect analogous to having all scaling operators be three body in MERA. In fact, long range correlations between tensors do arise in the recovery model dictated by the greedy algorithm. Here e indicates where a reconstruction index is missing or erased whereas ? indicates that the index could be missing or available.

Considering all error configuration at layer j which could lead to errors at layer j + 1, we may bound

<span id="page-54-1"></span><span id="page-54-0"></span>
$$s_{j+1} \le 3d_j + 3s_j^2 \tag{D.2}$$

$$d_{j+1} \le 3s_j(3d_n + 3s_j^2). \tag{D.3}$$

Here, we have aimed for simplicity instead of tightness of the bound. Let us give a

![](_page_55_Picture_0.jpeg)

Figure 24. We illustrate how correlated erasures can not grow beyond nearest neighbor in the hierarchical recovery model.

<span id="page-55-0"></span>brief explanation for the RHS of equations D.2 and D.3.

Since each hexagon has at least 4 legs connected to lower layers, two of its neighboring tensors (within four legs) need to be missing such that tensor fails to be recovered from the lower layer. For this to happen, there must either be two neighboring indices missing from the lower chain or two non-neighboring indices missing. There are three ways for this to happen illustrated by the following minimal error strings

$$\{ee \star \star, \star ee \star, \star \star ee,$$
 (D.4)

$$e \star e \star, e \star \star e, \star e \star e$$
 (D.5)

These scenarios cover all possible situations leading to the failure of hierarchical reconstruction (some of the, more unlikely ones such as *eeee* are being covered multiple times).

Similarly, we may account for all possible scenarios that lead to a double erasure ee at level j+1 Two consecutive tensors at chain j+1 always share exactly one descendant which may provide a source of correlated errors. Furthermore, at least one of the two tensors at layer j+1 will have a total of five descendants. As an overestimate of  $d_j$  we may disregard the value of the joint descendant. Regardless, we know that there should be two erasures in the remaining four descendants of the tensor with five descendants and at least one erasure among the outermost three descendants of the other tensor (see figure 25).

Assuming  $s_j \geq d_j \geq s_j^2$  which must hold for such a model, we may extract the dominant (smallest) exponent for  $\epsilon$  associated to the  $s_j$  and  $d_j$  bounds given by the recursion relation

$$\begin{pmatrix} \deg(s_{n+1}, \epsilon) \\ \deg(d_{n+1}, \epsilon) \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} \deg(s_n, \epsilon) \\ \deg(d_n, \epsilon) \end{pmatrix}$$
(D.6)

Here, by deg(p(x), x) denotes the lowest degree exponent of x present in the polynomial

<span id="page-56-0"></span>![](_page_56_Picture_0.jpeg)

**Figure 25**. We illustrate the prerequisite for two erasures to be propagated one layer higher. The most fragile case corresponds to one of the sites having only four descendants since at least one of them needs to have five. Irrespective of the availability of a shared descendant there is a minimum number of erasures that need to occur in order to propagate two contiguous erasures.

p(x). The recursion matrix has the eigenvalues  $\phi_{\pm} = \frac{1 \pm \sqrt{5}}{2}$  and the  $\phi_{+}$  eigenvector being  $(1, \phi_{+})$ . This means that the  $\epsilon$  exponent for  $s_n$  increases exponentially as  $\phi_{+}^n$ .

We may now calculate the fix-point solution of inequalities D.2 and D.3, taking them as equations and find  $(s^*, d^*) = (1/12, 1/48)$ . Assume that  $s_0 \leq rs^*$  for some  $r \leq 1$  and consequently,  $d_0 = s_0^2 \leq r^{\phi_+} d^*$ . We may prove inductively that  $s_j \leq r^{\phi_+^j} s^*$  and  $d_j \leq r^{\phi_+^{j+1}} d^*$ . In order to do so, one need only verify

$$s_{j+1} \le 3d^*r^{\phi^{j+1}} + 3s^*r^{2\phi^j} \le r^{\phi^{j+1}}s^*$$
 (D.7)

$$d_{j+1} \le 3(s^* r^{\phi^j}) 3(d^* r^{\phi^{j+1}} + 3s^* r^{2\phi^j}) \le r^{\phi_+^{j+2}} d^*.$$
 (D.8)

Where we may divide by an appropriate power of r such as  $r^{\phi_+^{j+1}}$  and obtain

$$3d^{\star} + 3s^{\star}r^{\phi^{n-2}} \le s^{\star} \tag{D.9}$$

$$3(s^*)3(d^* + 3s^*r^{\frac{3-\sqrt{5}}{2}\phi^n}) \le d^*.$$
(D.10)

This allows us to reach the conclusion of the theorem with  $\epsilon^* = s^*$  and  $\lambda = \phi^+$ .

A bounding procedure similar to this one may also be applied to the code involving alternating layers of pentagons and hexagons as for many other holographic codes with certain regularity structure. We have only restricted to consider the hexagon lattice to exemplify the kind of reasoning involved. In the case of the holographic pentagon code, there is no way to make such an argument work and there is a good reason for this. Namely there are constant weight 4 logical operators affecting the central qubit in the holographic pentagon code. The way this becomes manifest when attempting a similar proof approach is by obtaining a scaling dimension  $\lambda=1$ .

### <span id="page-57-0"></span>D.2 Numerical evaluation

We may numerically evaluate the probability for the greedy algorithm to absorb the central tensor given a boundary region constructed by erasing a random set of physical indices according to an i.i.d. distribution. This gives us a conservative estimate of how well protected the central qubit is from i.i.d. erasure since an optimal recovery method can only do better. We perform such estimates for different values of the lattice radius in order to identify the value p<sup>c</sup> associated to a correctability phase transition. For the regular pentagon lattice tensor network we find that there is no indication of the central qubit being well protected.

Given that the pentagon code does not have a threshold, we introduce the pentagon/hexagon code as a similar example that does have an erasure threshold in this context. It is the regular lattice composed of pentagons and hexagons, with two pentagons and two hexagons adjacent at each vertex. Such a lattice might employ [[6, 0, 4]]<sup>2</sup> and [[5, 1, 3]]<sup>2</sup> tensors. Intuitively, we expect that by diluting the number of logical legs, we may obtain better protection for the encoded logical qubits. Indeed, for such a lattice, we find that there is a threshold value p ∗ such that if the i.i.d. probability of boundary erasure is smaller than p ∗ , then the central logical qubit may be reconstructed with a probability which approaches one as the cutoff radius of the lattice is increased. Such a statement can be proven using techniques very similar to the threshold proof of section [D.1.](#page-53-0) We have numerically tested the performance of the greedy recovery algorithm for recovering the central qubit in three possible lattices (see figure [26\)](#page-58-0) supporting our claim that a lower density of logical legs leads to a higher tolerable erasure threshold.

# <span id="page-57-1"></span>E Reconstructing beyond the greedy algorithm

The greedy algorithm provides an explicit prescription for representing bulk logical operators on a specified region of the boundary. A key virtue is that the region obtained does not depend in any way on the specific perfect tensors used to construct the network. In this sense, it is analogous to the AdS/Rindler reconstruction, which is explicit and applicable to a large family of models satisfying a holographic correspondence.

### <span id="page-57-2"></span>E.1 Reconstruction from symmetry guarantees

The greedy entanglement wedge falls short of the expectations for a geometric entanglement wedge in certain ways. For instance, in the scenario where the minimal surface separating A from A<sup>c</sup> is well defined, we expect E[A] ∪ E[A<sup>c</sup> ] to contain the full lattice.

![](_page_58_Figure_0.jpeg)

<span id="page-58-0"></span>(a) Holographic pentagon code

(b) Pentagon/hexagon code

(c) Single qubit hexagon code

Figure 26. Here we present Monte Carlo simulation for the probability of the central tensor being incorporated by the greedy algorithm applied to a holographic code. The greedy algorithm is applied to a region A constructed by randomly taking each boundary physical index to belong to A with probability p. We plot the central tensor containment probability in the greedy wedge according to the lattice radius (i.e. the distance from the central tensor at which the a priory infinite network is truncated). (a) We consider the holographic pentagon code of figure 4b. Numerical results remains consistent with the existence of five possible weight 4 representations of the string-like logical operators acting on the central qubit. (b) We focus on the pentagon/hexagon code of figure 17a which has an erasure threshold in terms of the recoverability. We observe some oscillatory behavior due to the fact that tensor 'layers' added alternate between pentagons and hexagons. (c) We present numerical data for the greedy algorithm applied to the 1 qubit hexagon code of figure 17b which corresponds to a tensor network identical to the holographic hexagon state except for having a single pentagon at its center.

Our first example of reconstruction beyond the greedy wedge involves a family of holographic stabilizer codes with a single logical qudit. In this case, perfect reconstruction on either A or its complement  $A^c$  can be guaranteed by exploiting a symmetry.

Particularly, the three qutrit stabilizer code of section A.2 is of CSS [60] type, a property which we can show is inherited by any derived holographic code by following the arguments of section 5.7. Furthermore, the qutrit Hadamard operator H is a symmetry of the qutrit code meaning that applying H to all tensor indices preserves the tensor. The Hadamard operator is symmetric, unitary but generally not Hermitian  $^{9}$ . and is specified by its action on the generators X and Z

$$HXH^{\dagger} = Z^{\dagger} \qquad HZH^{\dagger} = X.$$
 (E.1)

The local symmetry of the tensors gives rise to a global symmetry on the full

<sup>&</sup>lt;sup>9</sup>For general qudits, the Hadamard gate is given by  $H = \frac{1}{\sqrt{d}} \sum_{i,j} \omega^{ij} |i\rangle\langle j|$ , where  $\omega = e^{2\pi i/d}$ .

<span id="page-59-1"></span><span id="page-59-0"></span>![](_page_59_Picture_0.jpeg)

Figure 27. In (a) we represent a bipartite network composed of tensors with a symmetry H and H<sup>∗</sup> . We alternate applying H (solid squares) and H<sup>∗</sup> (hollow squares) to all legs of tensors in the bipartite tensor network. In (b) we represent the same tensor network where a portion A of the boundary was marked with hollow dots and its complement A<sup>c</sup> was marked with full dots. The regions A and A<sup>c</sup> have been chosen such that the greedy algorithm does not progress on either. The greedy algorithm will recover the full network when initiated from the full boundary showing that the network indeed corresponds to a holographic code.

tensor network[10](#page-0-0). To see this, we multiply each tensor leg either by H or its inverse H† = H<sup>∗</sup> . Since each individual tensor is invariant under such an action, the full tensor network should be invariant. Furthermore, if we assume that the tensor network graph is bipartite we may alternate multiplication by H and H† such that these may locally cancel on all contracted indices, as depicted in figure [27a.](#page-59-0) We are then left with a symmetry acting exclusively on the free bulk and boundary legs of the tensor network. This symmetry guarantees a form of duality between X-type logical operator and Z-type logical operators where dual operators have exactly the same support.

Theorem 1 in of Ref. [\[64\]](#page-64-7) precisely relates the number of independent logical operators supported on complementary subsets of qudits. Their result applies to general subsystem codes and includes a sharper claim for CSS codes [\[65\]](#page-64-8). In particular, for any subset A of qudits, one may define `(A) to be the number of independent Pauli logical operators supported exclusively on A.

Lemma 1. Given a stabilizer code with k logical qubits, `(A)+`(A<sup>c</sup> ) = 2k. Furthermore if the code is of CSS type, we have ` Z (A) + ` <sup>X</sup>(A<sup>c</sup> ) = k = ` Z (A<sup>c</sup> ) + ` <sup>X</sup>(A), where `X and ` <sup>Z</sup> denote the number of X-type and Z-type generators respectively.

<sup>10</sup>Here we limit ourselves to provide the simplest example which conveys the general spirit of deriving global symmetries from local tensor symmetries [\[61\]](#page-64-9). The state of the art for this line of reasoning in tensor networks can be found in [\[62,](#page-64-10) [63\]](#page-64-11).

This is called the cleaning lemma for stabilizer codes and applies to prime dimension qudits[11](#page-0-0) .

Assume that we are dealing with a CSS code with a single logical qudit, k = 1 and a Hadamard type symmetry which guarantees ` <sup>X</sup>(A) = ` Z (A). From this we may exclude the case `(A) = `(A<sup>c</sup> ) = 1 and conclude that the full logical algebra may be reconstructed either on A or on A<sup>c</sup> . This conclusion is analogous to E[A] ∪ E[A<sup>c</sup> covering the full bulk, which is expected from the usual geometric entanglement wedge. In contrast, the greedy algorithm does not provide such a guarantee for the greedy entanglement wedge. Figure [27b](#page-59-1) illustrates a partition of the boundary of a tensor network into two regions such that the greedy algorithm does not make progress in either region. The same tensor network may be associated to a CSS type stabilizer code with self-duality properties where all the previously exposed arguments apply.

The same cleaning lemma may be used to guarantee that when |A<sup>c</sup> | = 4 qubits are deleted, at least 2k − 8 independent logical Pauli operators can be reconstructed on A, where k is the number of logical qubits in the code[12](#page-0-0). In the context of the example of figure [16b,](#page-32-1) even though the greedy entanglement wedge of A lacks a large number of tensors, the number of missing generators to reconstructed the full algebra is small.

### <span id="page-60-1"></span>E.2 Approximate reconstruction for typical tensors

Consider a connected residual region R obtained after removing the greedy entanglement wedge associated to boundary region A and the one associated to its complement Ac . A "typical" residual region will be composed of randomly chosen perfect tensors without any specific symmetry imposed. In this case, we may average the entanglement entropy associated to boundaries γ ? <sup>A</sup> and γ ? <sup>A</sup><sup>c</sup> . We expect that for |γ ? <sup>A</sup>| ≥ |γ ? <sup>A</sup><sup>c</sup> | + n<sup>R</sup> the map from the bulk logical indices and the smaller boundary onto the larger one will generically be full rank. Furthermore, we conjecture that for random perfect tensors, the average value of S<sup>A</sup> will approach |γ ? <sup>A</sup><sup>c</sup> | + n<sup>R</sup> exponentially with |γ ? <sup>A</sup>| − |γ ? <sup>A</sup><sup>c</sup> | − nR. We expect an argument analogous to that of Ref. [\[66\]](#page-64-12) to allow us to reach such a conclusion. In turn this would imply that the logical operators in the residual region can be reconstructed on γ ? <sup>A</sup> (and in turn on A) to a good approximation.

</details>

</golden_source>