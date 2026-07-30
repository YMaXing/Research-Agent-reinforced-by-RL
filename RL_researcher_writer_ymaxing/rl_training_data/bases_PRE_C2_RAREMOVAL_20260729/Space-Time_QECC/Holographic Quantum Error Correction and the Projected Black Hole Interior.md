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
