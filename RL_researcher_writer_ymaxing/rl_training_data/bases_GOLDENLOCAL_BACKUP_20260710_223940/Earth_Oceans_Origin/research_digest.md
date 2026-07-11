<digest_meta>
  <article_title>Earth_Oceans_Origin</article_title>
  <total_sources>8</total_sources>
  <total_artefacts>3</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>38</n_orphan_anchors>
  <n_content_sections>4</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
| A01 | Hydrogen Isotopic Composition of Hydrous Minerals in Asteroid Ryugu | table | sample,pearson,coeff,times,water | 10 | \| Sample                 \| Туре          |
| A02 | Hydrogen Isotopic Composition of Hydrous Minerals in Asteroid Ryugu | table | times,references | 12 | \| Name        \| Type               \| $D/ |
| A03 | Noble Gases and Stable Isotopes Track the Origin and Early | table | radiogenic,isotopes,mixing,ratios,recommended | 18 | \| Non-radiogenic isotopes (mixing ratios |
</artefact_registry>

<sources>
<s slug="A nearly terrestrial DH" type="exploitation">
The source reanalyzes >4000 Rosetta water isotope measurements from comet 67P/C-G to show that dust in the coma markedly elevates local D/H ratios via preferential HDO adsorption onto grain surfaces. The bulk nucleus D/H measured beyond dust influence is nearly terrestrial, aligning 67P/C-G with other Jupiter-family comets (JFCs) and supporting possible JFC contributions to Earth’s oceans. Key concepts include D/H as a PSN formation tracer (enriched ices from prestellar cores equilibrate variably with H2 at different heliocentric distances), the dust cycle of sublimation/redeposition (phases 1–3 tied to perihelion and seasonal hemispheres), and extended sources from ice-coated grains.

Concrete techniques and tools include ROSINA DFMS (Nier-Johnson geometry, m/Δm >3000, double-Gaussian peak fitting with fixed a2=0.1a1 and c2=3c1 relations), Bayesian nested sampling via the dynesty Python package (1000 live points, uniform/Gaussian priors on p0/D/z, log-likelihood via χ2) for separating overlapping HDO and H2^17O signals in mass 19, and pixel/gain-step corrections applied to level-3 data. Additional instruments referenced are ROSINA COPS, MIRO, and remote observations of Hale-Bopp jets.

Specific claims and data: 4339 valid D/H and 16O/17O plus 9177 16O/18O measurements; final bulk values D/H=(2.59±0.36)×10^{-4} (1.2–1.6×VSMOW), 16O/17O=2214±340, 16O/18O=392±73, and H2^18O/H2^17O=5.65±1.36 (matches MIRO); ratios stable >120 km post-perihelion; pre-perihelion northern latitudes show up to 10× enrichment correlated with hypervolatiles (CO, CH4, HCN); D/H decreases with distance and increasing outgassing rate. Comparisons reproduce prior values except near perihelion.

The source includes a 23-line Python tool-loop example for Bayesian fitting of DFMS spectra and multiple supplementary tables/figures on priors, covariances, and binned statistics. Coverage gaps include incomplete modeling of grain-size distributions (micrometers to cm-scale chunks), lack of direct constraints on ISM versus PSN grain origins, and reliance on post-perihelion data for the bulk value.
</s>
<s slug="Earth’s water may have been inherited from material" type="exploitation">
Earth’s water may have been inherited from material similar to enstatite chondrite meteorites reports measurements of hydrogen abundance and isotopic composition in 13 enstatite chondrite (EC) meteorites spanning petrologic types EH3 to EH6 plus the aubrite Norton County. The central claim is that EC-like material supplies at least three times the mass of Earth’s oceans (1.4 × 10²¹ kg H₂O) while matching mantle δD (–220 to –20 ‰) and δ¹⁵N values, removing the requirement for late addition of outer-Solar-System carbonaceous chondrites (CCs) as the sole water source.

Hydrogen was quantified on bulk powders by EA-IRMS and at the micrometer scale in chondrule mesostasis by SIMS at CRPG Nancy. Bulk EC water-equivalent contents range from 0.08 to 0.54 wt % H₂O (EH3 average 0.44 ± 0.04 wt %); the least-metamorphosed Sahara 97096 (EH3.1-3.4) interior yields 0.5 ± 0.1 wt % H₂O and δD = –103.6 ± 0.7 ‰. Mesostasis in Sahara 97096 contains 2700–12 300 ppm H₂O (average 7560 ± 1546 ppm) with homogeneous δD = –147 ± 16 ‰. Comparative SIMS data on CV chondrites Vigarano and Kaba give lower values (210–330 ppm). IOM contributes an additional ~380 ppm H₂O. Three mixing models (100 % EC; 68 % EC + 32 % CC; 71 % EC + 24 % OC + 5 % CC) each show EC-derived water exceeding the mantle inventory of 1–10 ocean masses.

Isotopic plots (δD vs. 1/H, δD vs. δ¹⁵N) demonstrate that EC bulk and mesostasis values lie within primitive-mantle ranges and are distinct from terrestrial alteration signatures. Only ECs simultaneously satisfy both H and N mantle compositions; solar H and CC contributions are considered but ruled out on H/Ne and noble-gas grounds. Surficial reservoirs require an additional ~4 % (H) to ~15 % (N) CI-like component delivered after mantle–surface homogenization.

Limitations include possible underestimation of pyroxene-hosted H (up to 5300 ppm measured in Norton County), unidentified carriers (sulfur-rich carbon-bearing porous amorphous silica), and the assumption that measured H abundances survived accretion without volatile loss. The study does not address timing of EC versus CI delivery or dynamical pathways that would emplace EC-like bodies at 1 AU.
</s>
<s slug="Hydrogen Isotopic Composition of Hydrous Minerals in Asteroid Ryugu" type="exploitation">
The main topic is the hydrogen isotopic composition of hydrous minerals (primarily serpentine and saponite) in Cb-type asteroid Ryugu samples returned by JAXA Hayabusa2, used to constrain the D/H ratio of water on its parent body and evaluate CI-like contributions to Earth's surficial reservoirs. Key concepts include aqueous alteration on the parent asteroid, interstellar ice inheritance followed by partial re-equilibration with nebular H2, and mass-balance estimates separating hydrous-mineral hydrogen from organic matter.

Analyses employed secondary ion mass spectrometry (SIMS) on the CAMECA IMS-1280HR2 instrument at CRPG with a 10 kV Cs+ primary beam rastered over 12 × 12 µm² areas, collecting H−, D−, 13C−, and 29Si− signals; calibration used reference materials (Kipawa amphibole, montmorillonite, serpentine, hydrogen-bearing glasses, terrestrial kerogen, and D-rich IOM) to correct instrumental mass fractionation (slope 2.2 ± 0.2). Least-squares linear regression of D−/H− versus C−/H− yielded zero-intercept (D/H)0 values, converted to δD relative to SMOW (D/H_SMOW = 155.76 × 10−6). Samples comprised Ryugu particles A0040, A0094 (site A), and C0002 (site C), plus Orgueil (CI) and Mighei (CM) for direct comparison; BSE/EDS mapping avoided anhydrous silicates, cracks, and holes.

Specific claims include D/H_Ryugu = [165 ± 19] × 10−6 (δD_Ryugu = +59 ± 121 ‰, 2σ), statistically indistinguishable from Orgueil and Alais hydrous minerals (δD_CI ≈ +98 ± 99 ‰) but higher than Mighei (δD_Mighei = −388 ± 134 ‰). Bulk Ryugu δD = +252 ± 13 ‰ exceeds most CI values; IOM δD values are lower (+306 to +440 ‰). CI-like material is estimated to supply ∼3 % of Earth's surficial hydrogen, accounting for ∼30 % of ocean water mass. Water is concluded to derive from D-enriched interstellar ice that partially exchanged with nebular H2 before accretion.

The source includes a 10-line table of hydrous mineral D/H ratios estimated from SIMS measurements (topic: sample, Pearson coeff, times, water) and a 12-line table of reference values and averages of the SIMS measurements (topic: times, references). Limitations include large 2σ uncertainties (±121 ‰) on δD_Ryugu that prevent resolution of modest parent-body exchange effects, restriction to three Ryugu particles from two sites, and exclusion of NH3 or other minor H-bearing phases only by correlation strength rather than direct measurement.
</s>
<s slug="Noble Gases and Stable Isotopes Track the Origin and Early" type="exploitation">
Noble gases (He, Ne, Ar, Kr, Xe) and stable isotopes (H, C, N, O, S) serve as tracers of volatile origins, planetary differentiation, outgassing, and atmospheric escape on terrestrial planets. The source reviews existing Venus atmospheric datasets, contrasts them with Earth/Mars/solar/chondritic/cometary reservoirs, and identifies open questions on accretion sources and loss processes relevant to early Earth ocean formation via shared volatile delivery and escape histories.

Key concepts include primordial vs. radiogenic noble-gas isotopes, mass-dependent fractionation during hydrodynamic escape, and mass-independent anomalies (e.g., 17O, 33S/36S). Direct nebular accretion vs. indirect meteoritic/cometary delivery is distinguished by isotope fingerprints; 20Ne/22Ne, 36Ar/38Ar, and Kr/Xe ratios discriminate solar-wind-irradiated, chondritic (phase Q), or cometary end-members. Radiogenic 40Ar/36Ar and 129Xe/132Xe constrain timing and extent of mantle outgassing.

Concrete data include: Venus 20Ne/22Ne ≈12 (solar-like), 40Ar/36Ar = 1.11±0.02 (low outgassing), D/H yielding δDVSMOW = 120 000‰, 12C/13C = 89.3±1.6; upper limits only for 3He/4He (<3×10−4), 21Ne/22Ne (<0.067), 132Xe (1–10 ppb), and δ15N (0±200‰). Two Kr abundance estimates (25 vs. 600 ppb) bracket chondritic vs. solar-like patterns. The source includes an 18-line table of mixing ratios, isotope values, and recommended precisions (Chassefière et al. 2012) plus three-isotope plots (Ne, Ar, Kr, Xe) and abundance-normalized figures comparing Venus–Earth–Mars–CI chondrites.

Claims supporting origin sections: Venus Ne/Ar and Xe depletion patterns resemble Earth/Mars “missing xenon”; low 40Ar implies ~25 % radiogenic-Ar outgassing vs. Earth’s ~50 %; similar Xe fractionation (3–4 ‰ u−1) on all three planets suggests common H–Xe coupled escape; C/N ratios near-chondritic on Venus and Earth.

Gaps: no Kr/Xe isotopes, no 17O/18O or S isotopes, imprecise 3He/4He and Xe abundance; photochemistry (SO2 photolysis) may alter O/S signatures; K/U ratio for bulk Venus remains debated. DAVINCI in-situ mass spectrometry and potential sample-return (free-return ballistic trajectory with DSMC-modeled high-velocity sampling) are identified as required future techniques.
</s>
<s slug="The Winchcombe meteorite, a unique and pristine" type="exploitation">
The Winchcombe meteorite (CM2.0–2.4) is a near-pristine carbonaceous chondrite fall whose pre-atmospheric orbit, short CRE age, hydrated mineralogy, and hydrogen isotopic composition link volatile-rich C-type asteroids to delivery of Earth’s water and prebiotic organics. Its fireball was recorded 21:54:16 UT 28 Feb 2021 by UKFAll networks (UKMON CMOS/CCD, UKFN DSLR, SCAMP/FRIPON all-sky, NEMETODE, GMN, AllSky7). The 13 ± 3 kg meteoroid entered at 13.5 km s⁻¹ with T_J = 3.121 ± 0.006, placing its source near the 3:1 Jovian resonance (a ≈ 2.5 AU); median near-Earth residence ~0.08 Ma; ²¹Ne and ²⁶Al CRE ages ~0.3 Ma and 0.27 ± 0.08 Ma. Recovered mass 531.5 g within 7 days (main 319.5 g stone collected ~12 h post-fall).

Petrography (ZEISS EVO 15LS SEM-EDS, FEI Helios/Quanta FIB-TEM, PANalytical/Enraf-Nonius PSD-XRD) shows >80 vol% Mg-rich serpentine-group phyllosilicates, tochilinite-cronstedtite intergrowths, calcite/dolomite, magnetite framboids, and rare anhydrous silicates; macroporosity 0.6–4.2% (Zeiss Xradia Versa 520 XCT). Bulk density ~2090 kg m⁻³ implies pre-atmospheric diameter 0.3 ± 0.1 m. Low-temperature (<150 °C) aqueous alteration reached near-completion on the parent body. Noble-gas data indicate near-surface regolith origin.

TGA (TA SDT Q600) gave 10.5 ± 1.1 wt% water after correction for adsorbed terrestrial H₂O; hydrogen stepwise pyrolysis (SUERC) yielded bulk δD = −142 ± 4‰ (SMOW), matching the terrestrial hydrosphere range. Stepped combustion (Open University Finesse) returned 2.0 ± 0.1 wt% C (δ¹³C = −1.7 ± 1.1‰) and 433.8 ± 20.3 ppm N (δ¹⁵N = 16.7 ± 0.9‰). LC-MS (Dionex RSLC + Orbitrap QExactive) and GC-MS (Agilent 7890A/5975C, CP-Chirasil columns) detected lipids, fatty acids, and racemic protein amino acids (α-aminoisobutyric acid 467 ± 17 ng g⁻¹, isovaline 391 ± 17 ng g⁻¹). Nanoglobules confirmed by TEM.

Spectral properties (VOSEG BRDF, Bruker VERTEX 70v FTIR) match hydrated C-type asteroids (albedo 4.09 ± 0.18%). Oxygen and titanium isotopes align with other CM falls. Limitations: only three ~50 mg aliquots for modal mineralogy and noble gases; amino-acid analyses limited to <1 month post-fall samples; no direct dynamical modeling of ejection or long-term thermal history beyond orbital integration.
</s>
<s slug="The source of hydrogen in earth’s building blocks" type="exploitation">
The source investigates the origin and abundance of hydrogen in enstatite chondrites (ECs) as Earth's building blocks, using micrometre-scale S-XANES spectroscopy on the EH3 chondrite LAR 12252 at beamline I18, Diamond Light Source. It addresses contradictions between nominally anhydrous mineralogy (implying negligible H) and bulk measurements showing 0.08–0.54 wt% H₂O, potentially supplying up to ~14 times Earth's ocean mass, with ~70% of Earth's volatiles possibly from inner solar system material.

Key concepts include H-S bonding (identified at ~2473.2 eV peak), pyrrhotite (Fe₁₋ₓS, 0 < x < 0.125) linked to H enrichment via peak shifts from 2471.8 eV (troilite) to lower energies, fine matrix (average 9.8 ± 3.1 times higher H-S amplitude than mesostasis), and formation via low-T sulfidation (reaction 1: 7FeS + ½S₂(g) → Fe₇S₈) followed by high-T sacrificial catalysis with nebular H₂ producing H₂S trapped in SiO₂-rich glass (reaction 2). S-XANES maps (470×480 μm², 5 μm spot, 0.2 eV steps from 2465–2495 eV) and spot spectra distinguish native H-S from terrestrial S⁶⁺ weathering (filtered by S⁶⁺:FeS amplitude ratio <0.5).

Techniques comprise multi-Gaussian peak fitting in IGOR Pro (2465–2478 eV range for FeS/H-S, 2580–2590 eV for S⁶⁺), normalisation of H-S amplitudes to 15 chondrule mesostasis spots, and mass-fraction calculations using densities (3730/3240 kg m⁻³), 21.5 vol% clastic matrix, and ~50 vol% fine matrix from paired EH3 meteorites SAH 97072/97096, yielding ~4.8 wt% fine matrix contributing ~5× more H than mesostasis (~13% of bulk H).

Data points include fine matrix H-S enrichment up to ~40× mesostasis averages, pyrrhotite-H-S amplitude correlation (ratios 0–1), absence of S⁶⁺ in metal/enstatite, and support for ECs explaining Earth's full water budget without stochastic late veneer. Includes figures mapping H-S amplitudes and schematic of nebular pyrrhotite-glass assembly.

Limitations include 5 μm spot size preventing direct submicron pyrrhotite observation, reliance on non-LAR 12252 parameters for matrix proportions, variable mesostasis H introducing largest error, and exclusion of metamorphosed ECs/aubrites.
</s>
<s slug="rosetta-fuels-debate-on-origin-of-earth-s-oceans" type="exploitation">
Rosetta fuels debate on origin of Earth’s oceans reports ESA’s Rosetta mission measurements of water vapour at Comet 67P/Churyumov–Gerasimenko, showing a deuterium-to-hydrogen (D/H) ratio more than three times higher than Earth’s oceans. The main topic is the delivery mechanism for Earth’s water after the planet formed hot 4.6 billion years ago, with key concepts including the D/H ratio as a tracer of formation distance and time in the protoplanetary disc, Jupiter-family comets versus Oort-cloud comets, and the relative roles of comets versus asteroids.

ROSINA (Rosetta Orbiter Spectrometer for Ion and Neutral Analysis) performed the measurements using its double focusing mass spectrometer (DFMS) on HD16O/H216O, collecting over 50 spectra between 8 August and 5 September 2014. The comet, a Jupiter-family body with a 6.5-year period orbiting between Earth/Mars and Jupiter, was reached on 6 August 2014. Prior benchmarks cited include the sole match to Earth’s D/H ratio from Comet 103P/Hartley 2 (Herschel, 2011) among 11 measured comets, plus matching ratios from Asteroid Belt meteorites despite their lower water content.

The source states that the elevated D/H value rules out the idea that Jupiter-family comets contain solely Earth ocean-like water and adds weight to asteroid-delivery models, while suggesting Jupiter-family comets may have formed over a wider range of distances than previously modelled. It references the peer-reviewed paper “67P/Churyumov-Gerasimenko, a Jupiter Family Comet with a high D/H ratio” (Altwegg et al., Science, 10 December 2014).

Notable limitations include the reliance on in-situ data from only the first month after arrival, before perihelion evolution; the absence of later ROSINA or Philae results; and the still-open quantitative partitioning between cometary and asteroidal contributions. The text notes that ongoing Rosetta escort observations through 2015 were expected to provide additional constraints on cometary evolution and Solar System water delivery.
</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-introduction | 1 | 8 | 0 |
| S2::section-2-a-showdown-between-comets-and-asteroids | 2 | 7 | 0 |
| S3::section-3-hydrogen-meet-magma | 3 | 6 | 0 |
| S4::section-4-drowning-in-a-sea-of-possibilities | 2 | 6 | 0 |
tavily_saturation=1.0
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-introduction" self_contained="no" sources="rosetta-fuels-debate-on-origin-of-earth-s-oceans,Earth’s water may have been inherited from material,A nearly terrestrial DH" artefacts="">
  <intent>Introduce the uncertainty of Earth's ocean origins despite extensive exploration, contrasting historical cometary preference with later shifts toward asteroids and endogenous production.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="rosetta-fuels-debate-on-origin-of-earth-s-oceans"/>
    <item name="theoretical_foundations" present="yes" evidence="Earth’s water may have been inherited from material"/>
    <item name="technical_nuances" present="yes" evidence="A nearly terrestrial DH"/>
    <item name="latest_advancements" present="yes" evidence="A nearly terrestrial DH"/>
    <item name="limitations_failure_modes" present="yes" evidence="rosetta-fuels-debate-on-origin-of-earth-s-oceans"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Earth’s water may have been inherited from material"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="rosetta-fuels-debate-on-origin-of-earth-s-oceans"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="rosetta-fuels-debate-on-origin-of-earth-s-oceans"/>
    <item name="enabling_technologies" present="yes" evidence="A nearly terrestrial DH"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="5">
    <orphan route="unreachable" anchor="Open the article with the NASA Europa Clipper mission (scheduled to investigate the subsurface ocean of Jupiter's icy mo" bullet="motivation">Pure narrative hook absent from any source.</orphan>
    <orphan route="unreachable" anchor="Immediately pivot to the counter-intuitive reality that, despite decades of solar-system exploration, spacecraft flybys," bullet="motivation">Pure narrative hook absent from any source.</orphan>
    <orphan route="unreachable" anchor="Trace the historical arc for the reader: the early preference for comets as the dominant water source. Explain why it wa" bullet="historical_context">Pure narrative hook absent from any source.</orphan>
    <orphan route="unreachable" anchor="Transition to Section 2: Summarize how the historical cometary model first dominated, then faced falsification through i" bullet="theoretical_foundations">Pure narrative hook absent from any source.</orphan>
    <orphan route="unreachable" anchor="Section length: 365 words" bullet="motivation">Pure formatting directive absent from any source.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-a-showdown-between-comets-and-asteroids" self_contained="no" sources="The Winchcombe meteorite, a unique and pristine,Hydrogen Isotopic Composition of Hydrous Minerals in Asteroid Ryugu,Noble Gases and Stable Isotopes Track the Origin and Early" artefacts="A01,A02,A03">
  <intent>Detail quantitative isotopic and dynamical evidence comparing cometary versus asteroidal exogenous water delivery using mission and meteorite data.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="rosetta-fuels-debate-on-origin-of-earth-s-oceans"/>
    <item name="theoretical_foundations" present="yes" evidence="Hydrogen Isotopic Composition of Hydrous Minerals in Asteroid Ryugu"/>
    <item name="technical_nuances" present="yes" evidence="The Winchcombe meteorite, a unique and pristine"/>
    <item name="latest_advancements" present="yes" evidence="A nearly terrestrial DH"/>
    <item name="limitations_failure_modes" present="yes" evidence="Noble Gases and Stable Isotopes Track the Origin and Early"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Hydrogen Isotopic Composition of Hydrous Minerals in Asteroid Ryugu"/>
    <item name="artefact_available" present="yes" evidence="A01"/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="Noble Gases and Stable Isotopes Track the Origin and Early"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="rosetta-fuels-debate-on-origin-of-earth-s-oceans"/>
    <item name="enabling_technologies" present="yes" evidence="The Winchcombe meteorite, a unique and pristine"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="13">
    <orphan route="unreachable" anchor="Transition from Section 1: briefly repeat the central problem - Earth formed about 4.54 billion years ago. Much about it" bullet="motivation">Pure narrative transition absent from any source.</orphan>
    <orphan route="unreachable" anchor="Position comets as the early frontrunner by detailing their formation in the cold Kuiper Belt and Oort cloud where water" bullet="theoretical_foundations">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Present the D/H ratio as the decisive diagnostic tracer: report the Giotto spacecraft's 1986 in-situ measurement of Hall" bullet="technical_nuances">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Insert an image with the URL <https://www.quantamagazine.org/wp-content/uploads/2026/06/Giotto_launch_preparations-cr.ES" bullet="motivation">Pure formatting directive absent from any source.</orphan>
    <orphan route="unreachable" anchor="Insert an image with the URL <https://www.quantamagazine.org/wp-content/uploads/2026/06/Giotto_images_of_Comet_Halley-cr" bullet="motivation">Pure formatting directive absent from any source.</orphan>
    <orphan route="unreachable" anchor="Counter with the asteroid case: highlight the high impact frequency of outer-belt asteroids during the late heavy bombar" bullet="case_studies_metrics">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Insert an image with the URL <https://www.quantamagazine.org/wp-content/uploads/2024/11/TheComet_crChristianStangl-Lede-" bullet="motivation">Pure formatting directive absent from any source.</orphan>
    <orphan route="unreachable" anchor="Expose the persistent shortcomings of the asteroid-only model for the reader: noble-gas abundance patterns (especially x" bullet="limitations_failure_modes">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Pivot the narrative to the radical alternative: because both cometary and asteroidal models encounter quantitative contr" bullet="theoretical_foundations">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Insert an image with the URL <https://www.quantamagazine.org/wp-content/uploads/2026/06/arrival-bennu-full-rotation-cr.N" bullet="motivation">Pure formatting directive absent from any source.</orphan>
    <orphan route="unreachable" anchor="Draw on the golden-source ESA Rosetta article to illustrate how mission data can simultaneously close one door (comets)" bullet="motivation">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Transition to Section 3: Recapitulate that the exogenous-delivery debate leaves unresolved tensions in both isotopic and" bullet="limitations_failure_modes">Pure narrative transition absent from any source.</orphan>
    <orphan route="unreachable" anchor="Section length: 935 words" bullet="motivation">Pure formatting directive absent from any source.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-hydrogen-meet-magma" self_contained="no" sources="The source of hydrogen in earth’s building blocks,rosetta-fuels-debate-on-origin-of-earth-s-oceans,Earth’s water may have been inherited from material" artefacts="">
  <intent>Present the endogenous water-production mechanism via hydrogen-magma ocean reactions supported by enstatite chondrite reanalysis and laboratory experiments.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="Earth’s water may have been inherited from material"/>
    <item name="theoretical_foundations" present="yes" evidence="The source of hydrogen in earth’s building blocks"/>
    <item name="technical_nuances" present="yes" evidence="The source of hydrogen in earth’s building blocks"/>
    <item name="latest_advancements" present="yes" evidence="The source of hydrogen in earth’s building blocks"/>
    <item name="limitations_failure_modes" present="yes" evidence="The source of hydrogen in earth’s building blocks"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Earth’s water may have been inherited from material"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="The source of hydrogen in earth’s building blocks"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="Earth’s water may have been inherited from material"/>
    <item name="enabling_technologies" present="yes" evidence="The source of hydrogen in earth’s building blocks"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="9">
    <orphan route="unreachable" anchor="Briefly introduce the topic: When astronomers simulate the ways exoplanets, with a diversity of atmospheres, took shape," bullet="motivation">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Begin with the reevaluation of metoerites called enstatite chondrites: new laboratory measurements reveal previously ove" bullet="theoretical_foundations">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Draw inference from exoplanet formation simulations: statistical demographics of sub-Neptunes and super-Earths imply tha" bullet="theoretical_foundations">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Detail the core mechanism: under extreme pressures and temperatures at the base of a magma ocean, dissolved hydrogen rea" bullet="technical_nuances">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Present the laboratory breakthroughs: describe diamond-anvil cell experiments combined with laser heating that successfu" bullet="latest_advancements">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Explicitly reference the applicability debate, including the quotes by various scientists, for Earth-mass planets rather" bullet="limitations_failure_modes">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Conclude the section by spelling out the broad habitability implication: if rocky planets can be "born water-rich" throu" bullet="motivation">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Cite the golden-source Nature papers on magma-ocean water formation and high-pressure hydrogen-magma experiments to grou" bullet="technical_nuances">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Transition to Section 4: Acknowledge that the endogenous mechanism does not necessarily exclude all exogenous contributi" bullet="limitations_failure_modes">Pure narrative transition absent from any source.</orphan>
    <orphan route="unreachable" anchor="Section length: 900 words" bullet="motivation">Pure formatting directive absent from any source.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-drowning-in-a-sea-of-possibilities" self_contained="no" sources="A nearly terrestrial DH,rosetta-fuels-debate-on-origin-of-earth-s-oceans,Noble Gases and Stable Isotopes Track the Origin and Early" artefacts="">
  <intent>Synthesize mixed-source model while enumerating post-delivery processing factors that obscure original isotopic signatures and drawing parallels to origin-of-life research.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="A nearly terrestrial DH"/>
    <item name="theoretical_foundations" present="yes" evidence="A nearly terrestrial DH"/>
    <item name="technical_nuances" present="yes" evidence="A nearly terrestrial DH"/>
    <item name="latest_advancements" present="yes" evidence="A nearly terrestrial DH"/>
    <item name="limitations_failure_modes" present="yes" evidence="Noble Gases and Stable Isotopes Track the Origin and Early"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="rosetta-fuels-debate-on-origin-of-earth-s-oceans"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="Noble Gases and Stable Isotopes Track the Origin and Early"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="rosetta-fuels-debate-on-origin-of-earth-s-oceans"/>
    <item name="enabling_technologies" present="yes" evidence="A nearly terrestrial DH"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="6">
    <orphan route="unreachable" anchor="Reintroduce a limited cometary resurgence by presenting the Herschel Space Observatory measurement of Hartley 2 that yie" bullet="latest_advancements">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Insert an image with the URL <https://www.quantamagazine.org/wp-content/uploads/2026/06/Comet-Hartley-2-cr-NASA-JPL-Calt" bullet="motivation">Pure formatting directive absent from any source.</orphan>
    <orphan route="unreachable" anchor="Synthesize a mixed-source model for the reader: Earth's oceans most plausibly result from a combination of (i) cometary" bullet="theoretical_foundations">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Enumerate the complicating factors that continue to obscure original signatures: post-delivery geological processing (ma" bullet="limitations_failure_modes">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Draw the parallel to the origin-of-life question: just as deeper knowledge of prebiotic chemistry has replaced a single" bullet="cross_domain_analogies">Pure narrative absent from any source.</orphan>
    <orphan route="unreachable" anchor="Section length: 350 words" bullet="motivation">Pure formatting directive absent from any source.</orphan>
  </orphan_anchors>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction" need_depth="2" need_breadth="3" target_words="365" mandatory_bullets="4" must_cover_depth="2" must_stay_brief="1"/>
  <section id="S2::section-2-a-showdown-between-comets-and-asteroids" need_depth="1" need_breadth="3" target_words="935" mandatory_bullets="12" must_cover_depth="6" must_stay_brief="2"/>
  <section id="S3::section-3-hydrogen-meet-magma" need_depth="2" need_breadth="3" target_words="900" mandatory_bullets="9" must_cover_depth="5" must_stay_brief="2"/>
  <section id="S4::section-4-drowning-in-a-sea-of-possibilities" need_depth="2" need_breadth="3" target_words="350" mandatory_bullets="4" must_cover_depth="2" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S3::section-3-hydrogen-meet-magma, S4::section-4-drowning-in-a-sea-of-possibilities</weakest_sections>
    <strongest_sections>S2::section-2-a-showdown-between-comets-and-asteroids, S1::section-1-introduction</strongest_sections>
    <dominant_gap_type>breadth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>