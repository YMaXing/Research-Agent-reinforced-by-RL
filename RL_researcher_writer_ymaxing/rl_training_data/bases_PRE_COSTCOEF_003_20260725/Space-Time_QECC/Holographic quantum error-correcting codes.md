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

