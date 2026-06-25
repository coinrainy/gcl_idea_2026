# Research Wiki Query Pack

## Project Direction

GCL for node classification. Seek a mechanism-level contribution around positive/negative construction, augmentation semantics, negative-free SSL, masked graph modeling, homophily/heterophily, structural noise, semantic consistency, LLM/TAG priors, and strict evaluation integrity.

## Top Papers

- GRACE (`paper:zhu2020_deep_graph_contrastive`): classic node-level GCL with stochastic graph/feature augmentation.
- GCA (`paper:zhu2020_graph_contrastive_learning`): adaptive topology/feature augmentation; high risk for any augmentation claim.
- ProGCL (`paper:xia2021_progcl_rethinking_hard`): closest false-negative / hard-negative work.
- BGRL (`paper:thakoor2021_largescale_representation_learning`): negative-free bootstrap GCL.
- CCA-SSG and Graph Barlow Twins: no-negative/decorrelation baselines.
- GraphMAE / GraphMAE2 / MaskGAE: masked graph modeling competitors; compare only under identical evaluator.
- HLCL / CM-GCL / G-Censor: OpenReview high-risk closest works for heterophily, multimodal/imbalanced positives, task-oriented views.
- LangGSL: LLM/TAG semantic prior risk; must audit leakage.
- Khan-GCL and SPGCL: recent arXiv preprints on hard negatives / positive samples; treat as parallel work, not established SOTA.

## Top Gaps

- G1 semantic false positives in node-level GCL.
- G2 false negatives change under homophily/heterophily regimes.
- G3 masked graph modeling vs GCL under identical frozen evaluator is unresolved.
- G4 graph-specific collapse diagnostics for negative-free SSL are weak.
- G5 heterophily-aware GCL lacks boundary-condition analysis.
- G6 LLM semantic priors need leakage-safe protocol.
- G7 worst-group robustness is missing from GCL reporting.
- G8 cross-domain generalization claims are under-specified.

## Closest-Work Risks

- Positive/negative construction: ProGCL, SPGCL, CM-GCL, G-Censor.
- Augmentation semantics: GCA, RGCL, G-Censor.
- Negative-free: BGRL, CCA-SSG, Graph Barlow Twins, AFGRL.
- Masked/predictive: GraphMAE2, MaskGAE.
- Heterophily: HLCL.
- LLM/TAG: LangGSL, CM-GCL.

## Method Transfer Primitives

Keep only mechanisms directly relevant to GCL node classification:

- false-negative probability estimation;
- alignment-uniformity diagnostics by graph regime;
- latent prediction instead of raw reconstruction;
- teacher-student pseudo-targets with confidence audits;
- balanced prototype assignments;
- variance/covariance collapse prevention;
- robust sample selection for noisy positives/edges;
- invariant/worst-group reporting across graph regimes;
- leakage-safe LLM/text semantic signals.

## Failed / Non-Goal Directions

Do not generate simple gate, reweighting, adapter, residual, temperature-only or backbone-swap ideas. Do not mechanically copy visual SSL augmentations. Do not claim SOTA from published tables with unclear split/evaluator/seeds. Do not use LLM pseudo-labels without leakage and contamination audits.

## Open Unknowns

- Exact split/evaluator/seeds/test@best for several core papers remain UNCLEAR.
- Semantic Scholar, DeepXiv and Exa were unavailable in this environment; coverage is arXiv + Web/OpenReview heavy.
- Which OpenReview ICLR 2024-2026 / ICML / NeurIPS submissions are accepted vs rejected is not fully resolved for all hits.
- Stage 2 should start from gaps, not final methods.
