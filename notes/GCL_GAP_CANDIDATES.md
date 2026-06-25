# GCL Gap Candidates

本文件只整理 research gaps，不生成完整方法。

## G1: Semantic False Positives in Node-Level GCL

- Gap ID: G1
- Gap name: positive pairs can be semantically inconsistent
- Existing shortcoming: GRACE/GCA-style augmentations assume two corrupted views of a node preserve semantics, but edge/feature drops can destroy label-relevant context or preserve spurious structure.
- Evidence: GRACE/GCA rely on stochastic/adaptive augmentations; G-Censor argues task-oriented views matter; CM-GCL uses node-text modality to form contrastive pairs.
- Mechanism vs tuning: failure is about whether the positive relation is valid, not the drop rate alone.
- Closest work: GCA, RGCL, G-Censor, CM-GCL.
- Technical opening: evaluate positive-pair semantic consistency using feature/text/graph agreement diagnostics.
- Minimum falsification experiment: measure downstream accuracy vs estimated positive-pair consistency across homophily bins under fixed evaluator.
- Negative-result value: shows augmentation semantics are not a major bottleneck under strict protocol.
- Suitable for node-classification main paper: YES
- Risk: HIGH
- Stage 2: YES

## G2: False Negatives Under Homophily and Heterophily Shift

- Gap ID: G2
- Gap name: negative sampling validity changes across graph regimes
- Existing shortcoming: ProGCL handles false negatives probabilistically, but regime-specific failure under homophily/heterophily remains under-characterized.
- Evidence: ProGCL; HLCL; homophily-aware heterogeneous GCL.
- Mechanism vs tuning: a negative pair can be semantically invalid depending on class/structure regime.
- Closest work: ProGCL, HLCL, SPGCL.
- Technical opening: split false-negative analysis by structural homophily, feature similarity and text semantics.
- Minimum falsification experiment: compare hard-negative scores with label agreement on validation-only diagnostics.
- Negative-result value: proves false negatives are not the decisive failure mode under target protocol.
- Suitable: YES
- Risk: HIGH
- Stage 2: YES

## G3: Masked Graph Modeling vs Contrastive Learning Under Identical Evaluator

- Gap ID: G3
- Gap name: unclear when MGM beats GCL for node classification
- Existing shortcoming: GraphMAE/GraphMAE2/MaskGAE report strong results, but protocols often differ from GCL frozen-evaluator setups.
- Evidence: GraphMAE, GraphMAE2, MaskGAE.
- Mechanism vs tuning: predictive/reconstructive objectives optimize different semantics than instance discrimination.
- Closest work: GraphMAE2.
- Technical opening: protocol-aligned objective comparison and diagnostic of raw reconstruction vs latent prediction.
- Minimum falsification experiment: same split/evaluator/backbone comparing GRACE/GCA/BGRL/GraphMAE variants.
- Negative-result value: clarifies whether masked modeling is only protocol advantage.
- Suitable: YES
- Risk: MEDIUM
- Stage 2: YES

## G4: Negative-Free Collapse Is Under-Audited on Graphs

- Gap ID: G4
- Gap name: graph-specific collapse diagnostics are weak
- Existing shortcoming: BGRL/CCA-SSG/GBT avoid negatives, but collapse prevention is often inferred from accuracy.
- Evidence: BGRL, CCA-SSG, Graph Barlow Twins, VICReg/BYOL transfer.
- Mechanism vs tuning: collapse and oversmoothing are representation-level failures distinct from hyperparameters.
- Closest work: BGRL, CCA-SSG.
- Technical opening: variance/covariance/eigenspectrum diagnostics across graph regimes.
- Minimum falsification experiment: compare representation rank/variance and accuracy under fixed splits.
- Negative-result value: shows negative-free methods are stable enough; focus elsewhere.
- Suitable: YES
- Risk: MEDIUM
- Stage 2: YES

## G5: Heterophily-Aware GCL Lacks Clear Boundary Conditions

- Gap ID: G5
- Gap name: spectral/filter solutions may not generalize across heterophily types
- Existing shortcoming: HLCL uses graph filters, but heterophily can arise from labels, features, directedness, or roles.
- Evidence: HLCL; supervised heterophily GNN literature; Directed GCL OpenReview hit.
- Mechanism vs tuning: filter choice encodes an assumption about signal frequency.
- Closest work: HLCL.
- Technical opening: categorize heterophily failure types before designing methods.
- Minimum falsification experiment: fixed split evaluation over multiple heterophily benchmark families.
- Negative-result value: identifies which heterophily subtype matters for GCL.
- Suitable: YES
- Risk: MEDIUM
- Stage 2: YES

## G6: LLM Semantic Priors Need Leakage-Safe Protocols

- Gap ID: G6
- Gap name: text semantics can help GCL but may leak supervision or benchmark knowledge
- Existing shortcoming: LangGSL/TAG work uses LLM features/pseudo-labels, but benchmark contamination and split consistency are hard to audit.
- Evidence: LangGSL and recent TAG/LLM graph learning.
- Mechanism vs tuning: semantic prior changes information source, not just model capacity.
- Closest work: LangGSL, CM-GCL.
- Technical opening: define allowed semantic signals and leakage-safe pseudo-label audits.
- Minimum falsification experiment: compare frozen text embeddings, LLM pseudo-labels and graph-only SSL under same split.
- Negative-result value: determines whether LLM signal is necessary or misleading.
- Suitable: UNCLEAR
- Risk: HIGH
- Stage 2: UNCLEAR

## G7: Worst-Group Robustness Is Missing from GCL Reporting

- Gap ID: G7
- Gap name: mean accuracy hides regime failures
- Existing shortcoming: GCL papers mostly report mean over datasets/seeds, not worst homophily/noise/label-scarcity group.
- Evidence: benchmark protocol matrix shows reporting inconsistency; OOD/DG literature suggests mean can hide failures.
- Mechanism vs tuning: representation can be good on average but fail on minority regimes.
- Closest work: robust GNN / heterophily-aware GCL.
- Technical opening: report worst-group over structure/noise regimes.
- Minimum falsification experiment: bin nodes/datasets by homophily/noise and compute worst-bin accuracy.
- Negative-result value: if no hidden failure, standard mean reporting may be sufficient.
- Suitable: YES
- Risk: MEDIUM
- Stage 2: YES

## G8: Cross-Domain Generalization Is Under-Specified

- Gap ID: G8
- Gap name: graph SSL transfer claims lack protocol alignment
- Existing shortcoming: transfer/cross-domain graph work exists, but node-classification GCL often stays transductive.
- Evidence: GCC/G5, I-JEPA/IRM transfer primitives.
- Mechanism vs tuning: domain shift changes invariances and spurious correlations.
- Closest work: GCC, G5, cross-domain GNN.
- Technical opening: define source/target graph environments and invariant diagnostics.
- Minimum falsification experiment: train/pretrain on one graph family, evaluate frozen on another with fixed evaluator.
- Negative-result value: tells whether cross-domain claims are too ambitious for main paper.
- Suitable: UNCLEAR
- Risk: HIGH
- Stage 2: UNCLEAR
