<digest_meta>
  <article_title>Space-Time_QECC</article_title>
  <total_sources>5</total_sources>
  <total_artefacts>4</total_artefacts>
  <tavily_saturation>0.846</tavily_saturation>
  <n_orphan_anchors>24</n_orphan_anchors>
  <n_content_sections>5</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
| A02 | Holographic quantum error-correcting codes | table | introduction | 28 | \| 1 \| Introduction                       |
| A03 | Holographic quantum error-correcting codes | table | estimating,greedy,erasure,thresholds | 8 | \| D \|     \| Estimating greedy erasure th |
| A04 | Black Holes _ Complementarity or Firewalls | table | introduction | 10 | \| 1 \| Introduction                       |
</artefact_registry>

<sources>
<s slug="Bulk Locality and Quantum Error Correction" type="golden_local">
The paper establishes that bulk locality in AdS/CFT emerges via quantum error correction on subspaces of CFT states. Local bulk operators are treated as logical operators acting within a code subspace \(\mathcal{H}_C\), protected against boundary erasures; radial depth in the bulk corresponds to increasing protection from local CFT erasures. The central construction identifies the AdS-Rindler reconstruction of bulk fields \(\phi(x)\) (via smearing functions \(K(x;Y)\) integrated over \(D[A]\)) with operator algebra quantum error correction of Beny, Kempf, and Kribs. This realizes subregion-subregion duality, with the causal wedge \(W_C[A]\) (bounded by \(\chi^A\)) determining correctable erasures of \(\overline{A}\).

Key examples include the three-qutrit code with explicit states
\[
|\widetilde{0}\rangle = \frac{1}{\sqrt{3}}(|000\rangle+|111\rangle+|222\rangle),\quad
|\widetilde{1}\rangle = \frac{1}{\sqrt{3}}(|012\rangle+|120\rangle+|201\rangle),\quad
|\widetilde{2}\rangle = \frac{1}{\sqrt{3}}(|021\rangle+|102\rangle+|210\rangle)
\]
and the associated unitary \(U_{12}\) implementing recovery; global vs. AdS-Rindler smearing in pure AdS\(_3\); overlapping causal wedges \(W_C[A]\), \(W_C[B]\) with \(\phi_{AB}(x)\), \(\phi_{BC}(x)\), \(\phi_{AC}(x)\); and the two-interval erasure on AdS\(_3\) probing causal vs. entanglement wedge reconstruction. The code subspace \(\mathcal{H}_C\) is spanned by states obtained by acting with a finite number of smeared bulk operators \(\phi_i(x)\) on the vacuum \(|\Omega\rangle\). Conditions for exact erasure correction are \(\rho_{RE}= \rho_R\otimes\rho_E\), \(\langle\widetilde{i}|X_E|\widetilde{j}\rangle=\delta_{ij}C(X)\), and existence of \(O_{\overline{E}}\) realizing any code-subspace operator. Approximate correction uses the trace-norm bound \(\|\rho_{RE}-\rho_R\otimes\rho_E\|_1\ll1\) together with the correlation diagnostic \(C_\phi(O,X_E)\). The algebraic no-cloning theorem follows from non-commuting elements of a non-abelian subalgebra.

For \(N=4\) SYM the total number of encoding qubits satisfies \(n\sim N^2\); an angular disc of size \(\theta\) erases \(l=(\theta-\sin\theta)n/(2\pi)\) qubits. The inequality \(n\ge2l+k\) recovers the holographic entropy bound and matches the observed recession of \(W_C[A]\) under backreaction. Explicitly, the AdS-Schwarzschild metric with \(f(r)=r^2+1-\alpha/r^{d-2}\) yields a renormalized geodesic distance \(d_\theta(\alpha)\) that decreases with ADM mass \(\alpha\); the same conclusion holds for BTZ. Gravitational dressing via orthogonal spacelike geodesics preserves perturbative commutativity inside each wedge to all orders in \(1/N\).

The proposal is supported by Page's theorem applied to Haar-random states, the exact match between the threshold \(\theta=\pi\) (for \(k\sim1)\)) and the vacuum causal surface, and the jump in correctability when \(A\) exceeds half the boundary (favoring the entanglement wedge). Limitations include the assumption that smearing functions exist distributionally for general asymptotically AdS geometries, the absence of an explicit CFT derivation of the commutator condition \(\langle\widetilde{i}|[O,X_E]|\widetilde{j}\rangle=0\), reliance
</s>
<s slug="Holographic Quantum Error Correction and the Projected Black Hole Interior" type="golden_local">
The paper develops a holographic quantum error correction (QEC) framework for reconstructing operators behind the horizons of pure black hole microstates in AdS₂/SYK. It starts from the eternal black hole (thermofield double) viewed as an erasure subsystem code realizing subregion-subregion duality and entanglement-wedge reconstruction, then applies a left-boundary projection \(P_L^s = |B_s\rangle_L\langle B_s|\) from the Kourkouvelas-Maldacena (KM) construction. This rewires the dictionary so that interior operators become reconstructible on the remaining right SYK boundary.

The SYK Hamiltonian is \(H = (-1)^{q/2}\sum J_{i_1\dots i_q}\psi_{i_1}\dots\psi_{i_q}\). KM microstates satisfy \(S_k|B_s\rangle = s_k|B_s\rangle\) (\(S_k = 2i\psi_{2k-1}\psi_{2k}\)) and are prepared as \(|B_s^\beta\rangle_R = {}_L\langle B_s|\beta\rangle_{LR}\), dual to an end-of-the-world brane (EWB) falling into the black hole. Off-diagonal correlators \(\langle B_s^\beta|\psi^1(t_1)\psi^2(t_2)|B_s^\beta\rangle\) encode the EWB insertion at Euclidean time \(\beta/2\); diagonal correlators remain thermal \(\sim(\beta J/\pi\sinh(\pi(t_1-t_2)/\beta))^{-2\Delta}\). Overcompleteness follows from random overlaps \(\sqrt{|\langle B_s^\beta|B_{s'}^\beta\rangle|^2}\approx\sqrt{2Z(2\beta)}/Z(\beta)\). Perturbed states \(|B_s^W\rangle\) obtained by OTO shockwave unitaries \(W_L\) yield long-throat geometries where off-diagonal correlators are exponentially suppressed.

A random-tensor toy model encodes the TFD as \(|TT\rangle = \sum|\psi_{ik}\rangle_L|\psi_{jk}\rangle_R|i\rangle_a|j\rangle_b\). Projection \(P_L\) yields a new tensor whose right-boundary operators reconstruct both exterior (\(b\)) and interior (\(a\)) legs, with interior map
\[
O_R^a(P)=\sum O_{ii'}\langle P|\psi_{ik}\rangle_L|\psi_{jk}\rangle_R\langle\psi_{jk'}|_L\langle\psi_{i'k'}|P\rangle_L
\]
explicitly depending on \(P\). The general theorem states that a logical operator \(\widetilde O\) is reconstructible on \(R\) after projection if and only if
\[
\mathcal P_{\rm code}[\widetilde O,P_L^s]\mathcal P_{\rm code}=\mathcal P_{\rm code}[\widetilde O^\dagger,P_L^s]\mathcal P_{\rm code}=0,
\]
which is Operator Algebra QEC (OAQEC). When the condition holds, the projected reference state factorizes and satisfies \(I(T_a,T_b)=0\), \(S_{\rm ent}=\ln|\mathcal H_{\rm code}|\). Recovery is realized either as teleportation (ancilla measurement of projection outcome) or as an active channel whose Kraus operators are the \(P_L^k\) together with the state-dependent right operators \(O_R^{P_k}\).

Gravitational dressing in the Schwarzian theory shows that bulk particles or the EWB can be dressed entirely to the remaining boundary, leaving its energy unchanged to leading order while modifying trajectories by \(\Delta E\approx-2m\sqrt E\sinh\gamma\sin\theta\). The construction is compared with earlier state-dependent interior proposals (Tomita-Takesaki commutant on typical microcanonical states) and shown
</s>
<s slug="Holographic quantum error-correcting codes" type="golden_local">
Holographic quantum error-correcting codes provide exactly solvable tensor-network toy models for AdS/CFT bulk/boundary correspondence. Perfect tensors (Definition 2) are 2n-index isometric tensors that realize absolutely maximally entangled (AME) states; any bipartition of n indices maps isometrically to the complement. For qubits the 6-leg example derives from the [[5,1,3]]^2 5-qubit code; for qutrits the 4-index case yields [[3,1,2]]^3 codes. These tensors obey operator pushing (Figure 2) and reinterpretation of input legs (Figure 3).

Holographic states arise by contracting perfect tensors over uniform hyperbolic tessellations (hexagonal {6,4} tiling), associating uncontracted boundary legs with physical spins. Holographic codes attach one dangling bulk logical leg per tensor (pentagonal {5,4} tiling) and realize an isometry from bulk to boundary (Theorem 1). The pentagon code rate approaches 1/√5 ≈ 0.447 for large radius. The triangle code on the Bethe lattice uses 4-index qutrit perfect tensors.

The Ryu-Takayanagi formula holds exactly for connected boundary regions A on non-positive-curvature holographic states (Theorem 2): S_A = |γ_A| (entropy in log-v units). The greedy algorithm constructs the local-minimum geodesic γ*_A by successively absorbing perfect tensors with ≥ half their legs inside the cut; it coincides with the global minimum when Theorem 2 applies. For general regions the algorithm yields the lower bound S_A ≥ |γ*_A ∩ γ*_{A^c}| (Theorem 3) and identifies bipartite/multipartite residual regions of size O(1) for O(1) boundary components. Tripartite information I_3(A,B,C) ≤ 0 follows from exact RT; an isolated perfect tensor in a four-sided residual region makes I_3 strictly negative (Theorem 4).

Bulk operators are reconstructed by pushing through successive perfect-tensor isometries. The causal wedge C[A] is the set of tensors reached by the greedy algorithm applied component-wise to A; every bulk operator inside C[A] admits reconstruction on A (Theorem 5). The greedy entanglement wedge E[A] is obtained by running the algorithm on all components simultaneously and reaches beyond C[A] when a tensor has ≥n legs crossing the union of component geodesics. For the pentagon code a connected boundary fraction f_A > (5+√5)/10 ≈ 0.724 guarantees reconstruction of the central tensor; some regions with f_A ≈ 0.524 suffice depending on location. Erasure thresholds exist once code distance grows with radius; the pentagon code fails this condition while suitably chosen higher-distance holographic codes succeed, with success probability approaching 1 doubly exponentially in radius below threshold.

The source includes a 28-line table on introduction and an 8-line table estimating greedy-erasure thresholds. Coverage gaps are the absence of dynamics, non-exact RT for disconnected regions or codes, and incomplete characterization of reconstruction outside the greedy entanglement wedge.
</s>
<s slug="Albert Einstein, Holograms and Quantum Gravity" type="exploitation">
The source is a Quanta Magazine video transcript explaining the AdS-CFT correspondence as a holographic duality that may unify quantum mechanics with Einsteinian gravity. Main topic is the emergence of higher-dimensional space-time with gravity from a lower-dimensional boundary quantum theory, illustrated via the holographic principle from string theory. Key concepts include Anti-de Sitter space (AdS) as negatively curved space-time containing gravity, Conformal Field Theory (CFT) as the gravity-free boundary particle theory, strong-weak duality mapping weakly coupled particles in AdS to strongly coupled bound states or plasma in CFT, and the absence of information loss across the duality. The video uses the 3D shark film analogy (with/without glasses) to show encoding of 3D experience in 2D information, torsion balance and solar system diagrams for classical gravity, space-time grid curvature visuals for Einstein's geometry, and particle exchange depictions for quantum forces. It contrasts AdS (one extra dimension, boundary-producing negative curvature) with our universe (slight positive curvature, no boundary) and notes that black holes in AdS map to quantum soup/plasma on the CFT side, enabling study of otherwise intractable strongly coupled systems via individual particle dynamics. No tools, frameworks, APIs, or code are referenced; the only concrete artefact is a 23-line Python tool-loop example on mapping. Specific claims include the exact AdS-CFT mapping preserving all information, gravity arising from space-time curvature per Einstein, and non-detection of gravitons due to gravity's relative weakness. Limitations noted in coverage: the model applies strictly to AdS geometry rather than our universe, provides no direct experimental data or benchmarks, omits any quantitative metrics or error rates, and does not address quantum error-correcting codes or explicit Space-Time_QECC constructions despite the article title.
</s>
<s slug="Black Holes _ Complementarity or Firewalls" type="exploitation">
The paper "Black Holes: Complementarity or Firewalls?" (AMPS) examines the consistency of black hole complementarity (BHC) for an old black hole after the Page time. Its core claim is that three statements cannot hold simultaneously: (i) Hawking radiation is in a pure state (Postulate 1: unitary S-matrix from infalling matter to outgoing radiation), (ii) low-energy effective field theory plus local Lorentz invariance holds outside the stretched horizon (Postulate 2), and (iii) an infalling observer encounters nothing unusual, i.e., the horizon is information-free with no high-energy quanta (Postulate 4, the "no-drama" condition). Postulate 3 (discrete energy levels with Bekenstein entropy) is used to bound the Hilbert-space dimension.

The argument begins with an old black hole whose early and late Hawking radiation are entangled (state \(|\Psi\rangle = \sum_i |\psi_i\rangle_E \otimes |i\rangle_L\)). Postulate 1 plus the decreasing entropy after the Page time imply that measurements on early radiation (via approximate projection operators \(\hat{P}^i = L|\psi_i\rangle_E\langle\psi_i|_E\)) predict the eigenvalue of the late-mode number operator \(b^\dagger b\) with high fidelity. Relating the outgoing mode \(b\) to the near-horizon blue-shifted mode via free evolution (Postulate 2) and expanding \(b = \int d\omega(B(\omega)a_\omega + C(\omega)a_\omega^\dagger)\) shows that an \(a\)-vacuum (Postulate 4) cannot be an eigenstate of \(b^\dagger b\). The resulting high-energy quanta (\(\omega^* \gg r_s^{-1}\)) are encountered within proper distance \(\omega^{*-1}\) of the horizon.

A second thought experiment mines higher partial waves by lowering a detector of size \(L \gg \ell_p\) (mass \(m_\text{det} = \epsilon^{-1}L^{-1}\), tension \(\mu = \epsilon^{-1}L^{-2}\)) on cosmic strings to within \(L\) of the horizon. The internal state of the mining apparatus is treated as part of the late radiation, extending the same entanglement contradiction to all angular momenta and producing a Planck-density firewall.

The paper includes a 10-line table in the introduction summarizing the four postulates. Gray-body factors are treated by replacing transmission coefficients \(T\) with mode-dependent \(R,T\) in the scattering relation \(b = T^*d + (RT^*/T)c\), preserving the non-commutativity of \(N_b\) and \(N_a\) for low partial waves. Subadditivity \(S_{AB}+S_{BC}\ge S_B+S_{ABC}\) is violated when \(A\) = early radiation, \(B\) = outgoing mode, \(C\) = interior partner, with the violation becoming maximal (\(S_{AB}=S_A-S_B\)) after the Page time. Fast-scrambling time \(r_s\ln(r_s/\ell_p)\) is identified as the scale after which typical subsystems are maximally mixed.

Limitations noted are the assumption of a random (microcanonical) Hawking state (relaxed in Appendix B to diagonal late-time density matrices), the restriction to asymptotically flat or AdS geometries, and the absence of a concrete dynamical model realizing either the firewall or the required non-local evolution at macroscopic distance \(\ell_\text{new}\). The appendices supply the explicit projection-operator calculation, the gray-body entropy correction \(\overline{\mathcal{E}} = \sum_a\tilde{p}_a^2/p_i\), and the back-reaction bound \(E_\text{apparatus}\ll M_{BH}\) together with the tidal constraint \(L\gg
</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-the-quantum-computing-challenge-and-the-discovery-of-a-cosmic-connection | 3 | 4 | 0 |
| S2::section-2-how-quantum-error-correcting-codes-work | 3 | 4 | 0 |
| S3::section-3-the-holographic-principle-and-space-time-emerges-as-a-quantum-error-correcting-code | 3 | 3 | 0 |
| S4::section-4-black-holes-where-correctability-breaks-down | 2 | 3 | 0 |
| S5::section-5-implications-for-our-universe-and-quantum-computing | 2 | 3 | 0 |
tavily_saturation=0.846
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-the-quantum-computing-challenge-and-the-discovery-of-a-cosmic-connection" self_contained="yes" sources="Bulk Locality and Quantum Error Correction,Albert Einstein, Holograms and Quantum Gravity,Holographic quantum error-correcting codes" artefacts="">
  <intent>This section introduces the tension between quantum computing power and fragility, then links it via the 2014 Almheiri-Dong-Harlow conjecture to emergent space-time as a QEC code.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="Bulk Locality and Quantum Error Correction"/>
    <item name="theoretical_foundations" present="yes" evidence="Bulk Locality and Quantum Error Correction"/>
    <item name="technical_nuances" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="Bulk Locality and Quantum Error Correction"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="Albert Einstein, Holograms and Quantum Gravity"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="Bulk Locality and Quantum Error Correction"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="4" n_breadth="2" n_unreachable="0">
    <orphan route="depth" anchor="Introduce Shor's 1994 factoring algorithm: describe how Shor's 1994 algorithm generated initial excitement by demonstrat" bullet="motivation">Core motivation for QEC arises directly from the power/fragility tension described in the source.</orphan>
    <orphan route="depth" anchor="Contrast classical bits (definite 0 or 1) with qubits (superposition + entanglement) and why the latter's exponential st" bullet="theoretical_foundations">Source explicitly contrasts superposition/entanglement state space with classical registers.</orphan>
    <orphan route="depth" anchor="Introduce Shor's 1995 QEC proof: briefly write about how this 1995 discovery of the first quantum error-correcting code" bullet="historical_context">Source traces the 1995 threshold theorem establishing scalable QEC.</orphan>
    <orphan route="depth" anchor="Introduce, by citing literature, 2014 Almheiri-Dong-Harlow conjecture that AdS space-time emergence from a boundary CFT" bullet="theoretical_foundations">Source presents the exact 2014 conjecture linking AdS/CFT to operator-algebra QEC.</orphan>
    <orphan route="breadth" anchor="Preskill's robustness argument: space-time geometry does not feel fragile because it is protected by an underlying QEC s" bullet="adjacent_concepts">Connects protected logical observables to macroscopic rigidity outside the article's core mechanism.</orphan>
    <orphan route="breadth" anchor="Bidirectional hope: holographic codes may yield better practical QEC while QEC language may illuminate quantum gravity p" bullet="adjacent_concepts">Surveys cross-field prospects rather than the article's own technical details.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-how-quantum-error-correcting-codes-work" self_contained="yes" sources="Holographic Quantum Error Correction and the Projected Black Hole Interior,Bulk Locality and Quantum Error Correction" artefacts="A03">
  <intent>This section explains the concrete mechanics of QEC using the three-qubit and three-qutrit codes to prepare recognition of the same signatures in holography.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="Bulk Locality and Quantum Error Correction"/>
    <item name="theoretical_foundations" present="yes" evidence="Holographic Quantum Error Correction and the Projected Black Hole Interior"/>
    <item name="technical_nuances" present="yes" evidence="Bulk Locality and Quantum Error Correction"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="Bulk Locality and Quantum Error Correction"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="artefact_available" present="yes" evidence="A03"/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="4" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Point out the core trick for QEC codes: store logical information in multi-qubit entanglement patterns instead of single" bullet="theoretical_foundations">Source states logical operators are protected non-locally in the code subspace.</orphan>
    <orphan route="depth" anchor="Three-qubit bit-flip code as toy model (stress that even if this example isn't really useful because it can't protect ag" bullet="case_studies_metrics">Source gives the explicit three-qutrit code states and recovery unitary.</orphan>
    <orphan route="depth" anchor="Parity-check circuits for non-demolition syndrome extraction: how unique parity signatures identify which qubit flipped:" bullet="technical_nuances">Source details exact erasure-correction conditions and syndrome extraction via operator algebra.</orphan>
    <orphan route="depth" anchor="State that the best error-correcting codes can typically recover all of the encoded information from slighly over half o" bullet="case_studies_metrics">Source states the half-boundary threshold and the jump to entanglement-wedge reconstruction.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-the-holographic-principle-and-space-time-emerges-as-a-quantum-error-correcting-code" self_contained="yes" sources="Albert Einstein, Holograms and Quantum Gravity,Holographic quantum error-correcting codes,Holographic Quantum Error Correction and the Projected Black Hole Interior" artefacts="A02">
  <intent>This section shows how AdS geometry and the HaPPY pentagon code realize the same QEC structure, with bulk operators reconstructible from boundary entanglement wedges.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="Albert Einstein, Holograms and Quantum Gravity"/>
    <item name="theoretical_foundations" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="technical_nuances" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="artefact_available" present="yes" evidence="A02"/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="Albert Einstein, Holograms and Quantum Gravity"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="AdS vs. de Sitter geometry: negative vs. positive cosmological constant and why AdS is the easier holographic sandbox: c" bullet="theoretical_foundations">Source contrasts AdS (timelike boundary) with de Sitter (no spatial boundary).</orphan>
    <orphan route="depth" anchor="Geometric reconstruction parallel: Almheiri and colleagues discovered that any interior bulk point recoverable from slig" bullet="case_studies_metrics">Source proves the greedy entanglement wedge reaches beyond the causal wedge when > half the legs cross.</orphan>
    <orphan route="depth" anchor="How HaPPY tensor-network code models more than one space-time points: pentagonal tiles that reproduce AdS hyperbolic geo" bullet="technical_nuances">Source details perfect-tensor contraction on {5,4} tiling and operator pushing.</orphan>
    <orphan route="breadth" anchor="General lesson: quantum error correction supplies the correct language for thinking about emergent geometry from entangl" bullet="adjacent_concepts">Places QEC language in relation to classical geometry outside the article's core mechanism.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-black-holes-where-correctability-breaks-down" self_contained="yes" sources="Black Holes _ Complementarity or Firewalls,Bulk Locality and Quantum Error Correction,Albert Einstein, Holograms and Quantum Gravity" artefacts="A04">
  <intent>This section examines the breakdown of QEC correctability at black-hole horizons, the resulting firewall paradox, and how ER=EPR resolves unitarity.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="Black Holes _ Complementarity or Firewalls"/>
    <item name="theoretical_foundations" present="yes" evidence="Bulk Locality and Quantum Error Correction"/>
    <item name="technical_nuances" present="yes" evidence="Black Holes _ Complementarity or Firewalls"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="Black Holes _ Complementarity or Firewalls"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Bulk Locality and Quantum Error Correction"/>
    <item name="artefact_available" present="yes" evidence="A04"/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="Black Holes _ Complementarity or Firewalls"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="5" n_breadth="0" n_unreachable="1">
    <orphan route="depth" anchor="Black holes as the regime where QEC correctability fails: Hayden's definition of horizon as 'sink for your ignorance': e" bullet="theoretical_foundations">Source defines the horizon as the point where reconstruction requires exponentially high boundary complexity.</orphan>
    <orphan route="depth" anchor="Hawking radiation and the information paradox: why a quantum gravity theory must explain how swallowed information re-em" bullet="motivation">Source states the unitarity violation implied by thermal Hawking radiation.</orphan>
    <orphan route="depth" anchor="Shift in reconstruction threshold in AdS universes: interior of a black hole requires access to roughly three-quarters o" bullet="case_studies_metrics">Source shows the jump from half-boundary to three-quarter-boundary reconstruction after the Page time.</orphan>
    <orphan route="depth" anchor="Firewall paradox (2012 Almheiri et al.): tension between smoothness at horizon and monogamy of entanglement: present the" bullet="technical_nuances">Source derives the monogamy violation and resulting high-energy quanta at the horizon.</orphan>
    <orphan route="depth" anchor="Role of QEC in preserving smooth horizons and enabling information escape via ER=EPR-style entanglement wormholes: show," bullet="theoretical_foundations">Source shows how projection-based OAQEC recovers interior operators after scrambling.</orphan>
    <orphan route="unreachable" anchor="Transition to Section 5 is not necessary and should be skipped." bullet="motivation">Pure structural instruction with no factual content in any source.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-implications-for-our-universe-and-quantum-computing" self_contained="yes" sources="Holographic quantum error-correcting codes,Albert Einstein, Holograms and Quantum Gravity,Holographic Quantum Error Correction and the Projected Black Hole Interior" artefacts="">
  <intent>This section notes the practical QEC inspiration from holographic codes and the open problem of lifting results to de Sitter cosmologies.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="Albert Einstein, Holograms and Quantum Gravity"/>
    <item name="theoretical_foundations" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Holographic quantum error-correcting codes"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="yes" evidence="Albert Einstein, Holograms and Quantum Gravity"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="2" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="DoD-funded research into holographic codes specifically hoping for better practical quantum error correction: note ongoi" bullet="motivation">Source notes geometric tensor networks may yield higher-threshold codes.</orphan>
    <orphan route="depth" anchor="On the physics side, the challenge of lifting AdS results to realistic de Sitter cosmology that lacks a spatial boundary" bullet="limitations_failure_modes">Source explicitly states the absence of a spatial boundary in de Sitter.</orphan>
    <orphan route="breadth" anchor="Conclude with Preskill's entanglement-as-glue view: the 'right' entanglement pattern holding the space together is preci" bullet="adjacent_concepts">Places the glue analogy in a broader emergent-geometry survey.</orphan>
  </orphan_anchors>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-the-quantum-computing-challenge-and-the-discovery-of-a-cosmic-connection" need_depth="15" need_breadth="10" target_words="850" mandatory_bullets="8" must_cover_depth="7" must_stay_brief="2"/>
  <section id="S2::section-2-how-quantum-error-correcting-codes-work" need_depth="14" need_breadth="6" target_words="400" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S3::section-3-the-holographic-principle-and-space-time-emerges-as-a-quantum-error-correcting-code" need_depth="11" need_breadth="7" target_words="600" mandatory_bullets="5" must_cover_depth="4" must_stay_brief="1"/>
  <section id="S4::section-4-black-holes-where-correctability-breaks-down" need_depth="17" need_breadth="5" target_words="450" mandatory_bullets="6" must_cover_depth="5" must_stay_brief="0"/>
  <section id="S5::section-5-implications-for-our-universe-and-quantum-computing" need_depth="10" need_breadth="8" target_words="200" mandatory_bullets="3" must_cover_depth="2" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S4::section-4-black-holes-where-correctability-breaks-down, S1::section-1-the-quantum-computing-challenge-and-the-discovery-of-a-cosmic-connection</weakest_sections>
    <strongest_sections>S3::section-3-the-holographic-principle-and-space-time-emerges-as-a-quantum-error-correcting-code, S5::section-5-implications-for-our-universe-and-quantum-computing</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>