# Gap Map

Stable gap IDs. These are research gaps and novelty boundaries, not final methods.

## G1: Semantic False Positives in Node-Level GCL

- Status: unresolved
- Closest works: GCA, AFGRL, CM-GCL, G-Censor.
- Already solved: adaptive augmentations, augmentation-free positives, multimodal positives, task-oriented views.
- Not solved: systematic positive semantic-validity audit under identical frozen node evaluator.
- Blocked claim: simple feature/structure positive heuristic as novelty.
- Minimum novelty condition: show a measurable semantic-positive failure not covered by GCA/AFGRL/G-Censor.
- Must-run falsification: correlate positive consistency diagnostics with downstream accuracy under fixed split/evaluator.
- Stage 2 recommendation: YES
- Risk: HIGH

## G2: False Negatives Under Homophily and Heterophily Shift

- Status: unresolved
- Closest works: ProGCL, HLCL, SPGCL, homophily-aware heterogeneous GCL.
- Already solved: probability-aware hard negatives, graph-filter heterophily views, positive sampling.
- Not solved: unified regime-conditioned false-negative/false-positive boundary.
- Blocked claim: generic hard-negative reweighting solves GCL negatives.
- Minimum novelty condition: predict when negative mining is harmful/helpful across graph regimes.
- Must-run falsification: validation-only false-negative estimates vs label agreement by homophily bin.
- Stage 2 recommendation: YES
- Risk: HIGH

## G3: Masked Graph Modeling vs Contrastive Learning Under Identical Evaluator

- Status: unresolved
- Closest works: GraphMAE, GraphMAE2, MaskGAE.
- Already solved: masked feature/edge modeling and latent prediction.
- Not solved: apples-to-apples GCL vs MGM comparison under same split/evaluator/backbone.
- Blocked claim: masked reconstruction alone as new contribution.
- Minimum novelty condition: isolate objective-level difference after protocol alignment.
- Must-run falsification: rerun GRACE/GCA/BGRL/GraphMAE variants under same split/seed/evaluator.
- Stage 2 recommendation: YES
- Risk: MEDIUM-HIGH

## G4: Negative-Free Collapse Is Under-Audited on Graphs

- Status: unresolved
- Closest works: BGRL, CCA-SSG, Graph Barlow Twins, AFGRL.
- Already solved: no-negative bootstrap/decorrelation/positive discovery.
- Not solved: graph-specific collapse/oversmoothing diagnostics beyond accuracy.
- Blocked claim: negative-free GCL as novelty.
- Minimum novelty condition: define diagnostics that predict graph SSL failures.
- Must-run falsification: compare rank/variance/eigenspectrum vs accuracy across graph regimes.
- Stage 2 recommendation: YES
- Risk: MEDIUM

## G5: Heterophily-Aware GCL Lacks Clear Boundary Conditions

- Status: unresolved
- Closest works: HLCL, directed GCL, supervised heterophily GNNs.
- Already solved: graph-filter and directed-structure view generation.
- Not solved: boundaries across heterophily subtypes.
- Blocked claim: high-/low-pass filter addition for heterophily.
- Minimum novelty condition: taxonomy plus evidence of failure not explained by HLCL.
- Must-run falsification: evaluate same SSL objectives across heterophily benchmarks with fixed splits.
- Stage 2 recommendation: YES
- Risk: HIGH

## G6: LLM Semantic Priors Need Leakage-Safe Protocols

- Status: unresolved
- Closest works: LangGSL, CM-GCL, TAG/LLM graph learning.
- Already solved: text/LLM features, pseudo-labels, node-text contrast.
- Not solved: leakage-safe, split-consistent GCL evaluation.
- Blocked claim: LLM pseudo-labels improve GCL.
- Minimum novelty condition: explicit leakage model and ablation against frozen text embeddings.
- Must-run falsification: graph-only vs text-embedding vs LLM pseudo-label under no-test-label/no-contamination rules.
- Stage 2 recommendation: UNCLEAR
- Risk: HIGH

## G7: Worst-Group Robustness Is Missing from GCL Reporting

- Status: unresolved
- Closest works: HLCL, robust GNNs, GroupDRO-style reporting.
- Already solved: some heterophily/noise improvements.
- Not solved: worst-group reporting for GCL claims.
- Blocked claim: mean accuracy proves robustness.
- Minimum novelty condition: define groups without test leakage and report worst-bin effects.
- Must-run falsification: bin by homophily/noise/degree/label scarcity and report worst-bin accuracy.
- Stage 2 recommendation: YES as diagnostic companion
- Risk: MEDIUM

## G8: Cross-Domain Generalization Is Under-Specified

- Status: unresolved
- Closest works: BGRL large-scale, GCC/G5, IRM-style DG.
- Already solved: some graph pretraining and transfer settings.
- Not solved: protocol-aligned domain generalization for node classification.
- Blocked claim: broad cross-dataset generalization from same-domain tables.
- Minimum novelty condition: specify source/target domains and invariant assumptions.
- Must-run falsification: pretrain on one graph family, freeze/evaluate on another with controlled evaluator.
- Stage 2 recommendation: DEFER unless Stage 2 targets cross-domain.
- Risk: HIGH

## Stage 1.6 DeepXiv Gap Update

DeepXiv targeted retrieval did not overturn the Stage 1.5 gap map. It sharpened the following boundaries:

- G1 remains open but high risk because GMA/GMCL, GPA, iGCL, AFGRL and G-Censor-like task-oriented views already cover many positive/augmentation heuristics.
- G2 remains open and high risk because ProGCL/SPGCL plus newer negative-metric/counterfactual-hard-negative works cover generic negative refinement.
- G3 remains open because GraphMAE/GraphMAE2/MaskGAE report strong masked objectives, but DeepXiv still does not establish exact protocol equivalence with this project.
- G5 remains high risk because HLCL, GCL-OT and related heterophily papers already address filter/transport/heterophily variants.
- G6 remains `UNCLEAR` for main Stage 2 direction because LangGSL and label-free LLM graph learning raise leakage and contamination issues.

No new final method or idea was generated in Stage 1.6.

## Stage 2A Idea Status

Stage 2A generated 10 raw ideas and did not select a final method.

- G1: `GCL-I01` is `REVISE`; `GCL-I05` is `KILL`.
- G2: `GCL-I02` is `KEEP` and is a main candidate.
- G3: `GCL-I03` is `KEEP` and is the highest-priority main candidate.
- G4: `GCL-I09` is `REVISE`; use as companion diagnostic for `GCL-I03`.
- G5: `GCL-I04` is `REVISE` and backup candidate; `GCL-I10` is `KILL` due scope.
- G6: `GCL-I08` is `REVISE / DEFER`, not a main recommendation.
- G7: `GCL-I06` is `REVISE`, companion diagnostic only.

Stage 2A reviewer recommends `GCL-I03` and `GCL-I02` as main candidates, with `GCL-I04` as backup. No experiment has been run.
