# Gap Map

Stable gap IDs for Stage 1. These are research gaps, not final methods.

## G1: Semantic False Positives in Node-Level GCL

- Status: unresolved
- Evidence: GRACE/GCA assume semantic-preserving augmentations; G-Censor and CM-GCL show task/modality-aware positives matter.
- Mechanism: positive-pair validity, not just augmentation rate.
- Closest works: GCA, RGCL, G-Censor, CM-GCL.
- Stage 2 recommendation: YES

## G2: False Negatives Under Homophily and Heterophily Shift

- Status: unresolved
- Evidence: ProGCL, HLCL, homophily-aware heterogeneous GCL, SPGCL.
- Mechanism: negative-pair semantic validity changes by graph regime.
- Closest works: ProGCL, HLCL, SPGCL.
- Stage 2 recommendation: YES

## G3: Masked Graph Modeling vs Contrastive Learning Under Identical Evaluator

- Status: unresolved
- Evidence: GraphMAE, GraphMAE2, MaskGAE.
- Mechanism: predictive/reconstructive SSL optimizes different signals from instance discrimination.
- Closest works: GraphMAE2, MaskGAE.
- Stage 2 recommendation: YES

## G4: Negative-Free Collapse Is Under-Audited on Graphs

- Status: unresolved
- Evidence: BGRL, CCA-SSG, Graph Barlow Twins, AFGRL.
- Mechanism: collapse/oversmoothing is representation-level, not just accuracy.
- Closest works: BGRL, CCA-SSG.
- Stage 2 recommendation: YES

## G5: Heterophily-Aware GCL Lacks Clear Boundary Conditions

- Status: unresolved
- Evidence: HLCL and supervised heterophily GNN literature.
- Mechanism: filter/view assumptions differ across heterophily subtypes.
- Closest works: HLCL, directed GCL.
- Stage 2 recommendation: YES

## G6: LLM Semantic Priors Need Leakage-Safe Protocols

- Status: unresolved
- Evidence: LangGSL, CM-GCL and TAG/LLM graph learning.
- Mechanism: semantic prior changes information source; leakage and contamination must be audited.
- Closest works: LangGSL, CM-GCL.
- Stage 2 recommendation: UNCLEAR

## G7: Worst-Group Robustness Is Missing from GCL Reporting

- Status: unresolved
- Evidence: protocol matrix shows mean-only reporting and unclear split/evaluator details.
- Mechanism: average accuracy can hide homophily/noise/low-label failure regimes.
- Closest works: robust GNN and heterophily-aware GCL.
- Stage 2 recommendation: YES

## G8: Cross-Domain Generalization Is Under-Specified

- Status: unresolved
- Evidence: GCC/G5 style transfer and OOD SSL literature.
- Mechanism: domain shift changes graph invariances and spurious correlations.
- Closest works: GCC, G5, IRM-style DG.
- Stage 2 recommendation: UNCLEAR
