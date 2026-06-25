# Stage 2A Raw Ideas

Date: 2026-06-25

Scope: gap-driven idea generation only. No code, no pilots, no experiments, no repo cloning, no Stage 2B refine.

## Source Gaps

Primary: G1 semantic false positives, G2 false negatives under homophily/heterophily, G3 MGM vs GCL under identical evaluator, G5 heterophily boundary conditions.

Companion: G4 negative-free collapse diagnostics, G7 worst-group reporting.

Deferred unless unusually strong: G6 LLM semantic priors, G8 cross-domain generalization.

## Idea GCL-I01: Semantic-Preserving Positive Validity Tests

- Idea ID: GCL-I01
- Title: 语义保持阳性对的可证伪构造
- Primary gap: G1
- Core problem: GCL assumes two augmented views of the same node remain semantically consistent, but edge/feature perturbations can destroy label-relevant context.
- Why current methods fail: GRACE/GCA tune augmentation; AFGRL/SPGCL discover positives; G-Censor proposes task-oriented views. None gives a protocol-aligned positive semantic-validity audit under this project's frozen evaluator.
- Closest works: GRACE, GCA, AFGRL, G-Censor, SPGCL, CM-GCL.
- What closest works already solve: random/adaptive augmentations, augmentation-free positive discovery, task-oriented counterfactual views, multimodal positives.
- What remains open: auditable positive validity before alignment.
- Core hypothesis: positives that pass structural consistency, latent-context predictability and feature stability tests will yield more stable frozen node representations.
- Method sketch: generate multiple perturbation views; predict masked ego-context latent targets; accept positives only if structure/context/feature tests pass; store failed views as diagnostics; train fixed InfoNCE or no-negative objective on accepted positives.
- Relation to SSL theory: modifies InfoNCE alignment by adding a masked-latent validity condition; reports uniformity cost.
- Mechanism: positive + masked latent validation.
- Not a simple trick: changes positive relation definition, not a scalar weight/gate.
- Minimum novelty condition: distinct from GCA centrality, AFGRL kNN/cluster positives and G-Censor counterfactual views.
- Minimum falsification experiment: compare positive validity score vs downstream accuracy for GRACE/GCA/AFGRL under fixed splits/evaluator.
- Kill condition: validity score does not correlate with validation/test accuracy and performance does not beat GCA/AFGRL.
- Support condition: validity score predicts downstream accuracy and improves mean±std on multiple datasets.
- Expected datasets/splits: Cora/CiteSeer/PubMed, Wiki-CS, Amazon, Coauthor; 10/10/80 JSON splits where applicable; official Wiki-CS separately.
- Expected evaluator: frozen encoder + L2 logistic regression; test@best validation epoch.
- Risk: HIGH
- Difficulty: MEDIUM
- Contribution type: method + diagnostic.

## Idea GCL-I02: Regime-Conditioned Negative Validity Boundary

- Idea ID: GCL-I02
- Title: 同配/异配条件下的负样本语义边界学习
- Primary gap: G2
- Core problem: hard negatives can be useful in homophilic regimes but harmful false negatives in heterophilic or role-based regimes.
- Why current methods fail: ProGCL estimates false-negative probabilities but does not characterize graph-regime boundaries; HLCL focuses on filters; SPGCL focuses positives.
- Closest works: ProGCL, HLCL, SPGCL, negative metric learning for graphs, counterfactual hard negatives.
- What closest works already solve: hard-negative risk, heterophily filters, positive sampling, some counterfactual negative construction.
- What remains open: predicting when hard negatives help or hurt.
- Core hypothesis: local homophily proxy, feature similarity and structural role similarity jointly predict negative validity.
- Method sketch: compute relation signatures for node pairs; partition pairs into confident negative/ambiguous/likely false negative; use confident negatives in InfoNCE; route ambiguous pairs to prototype-level separation; audit with validation-only label agreement.
- Relation to SSL theory: controls InfoNCE uniformity so semantically related nodes are not forced apart.
- Mechanism: negative + prototype fallback.
- Not a simple trick: produces a relation taxonomy and training semantics, not generic loss reweighting.
- Minimum novelty condition: explains ProGCL success/failure across homophily bins rather than replacing it with another weight.
- Minimum falsification experiment: validation-label-only audit of harmful-negative predictions vs true label agreement.
- Kill condition: harmful-negative prediction is random or removing ambiguous negatives worsens performance.
- Support condition: reduces false-negative rate and explains/improves ProGCL failures.
- Expected datasets/splits: Cora/CiteSeer/PubMed, Amazon/Coauthor, Actor/Chameleon/Squirrel/Penn94/Twitch/Genius; JSON or fixed splits.
- Expected evaluator: frozen encoder + logistic regression plus negative validity audit.
- Risk: HIGH
- Difficulty: MEDIUM-HIGH
- Contribution type: method.

## Idea GCL-I03: Protocol-Aligned MGM-vs-GCL Regime Selector

- Idea ID: GCL-I03
- Title: GCL 与 MGM 的同协议判别器
- Primary gap: G3
- Core problem: GraphMAE/GraphMAE2/MaskGAE and GCL results are hard to compare because split/evaluator/backbone/training budgets differ.
- Why current methods fail: papers mix protocols and conflate objective advantage with evaluator advantage.
- Closest works: GraphMAE, GraphMAE2, MaskGAE, GRACE, GCA, BGRL.
- What closest works already solve: masked reconstruction, latent prediction, edge/path masking, InfoNCE, bootstrap SSL.
- What remains open: a predictive boundary for when masked modeling beats contrastive learning.
- Core hypothesis: feature-label predictability, edge homophily and context reconstruction difficulty predict whether MGM or GCL is better.
- Method sketch: implement comparable InfoNCE/bootstrap/masked-feature/masked-latent objectives; lock backbone/splits/seeds/evaluator/budget; compute graph-regime metrics; learn a protocol-level objective selector; report failure cases.
- Relation to SSL theory: compares InfoNCE, bootstrap and masked modeling with alignment/uniformity and reconstruction metrics.
- Mechanism: benchmark-mechanism hybrid; masked + contrastive comparison.
- Not a simple trick: no objective gate in a final method; contribution is a protocol-aligned regime boundary.
- Minimum novelty condition: beyond rerunning GraphMAE; must predict objective ranking from graph properties.
- Minimum falsification experiment: rerun GRACE/GCA/BGRL/GraphMAE-style variants under identical evaluator and test if metrics predict objective ranking.
- Kill condition: objective ranking is unrelated to regime metrics.
- Support condition: metrics predict objective winner on most datasets/seeds and expose protocol bias.
- Expected datasets/splits: Cora/CiteSeer/PubMed, Wiki-CS, Amazon, Coauthor, ogbn-Arxiv; JSON or official splits.
- Expected evaluator: frozen encoder + identical logistic/linear probe.
- Risk: MEDIUM
- Difficulty: MEDIUM
- Contribution type: benchmark + diagnostic + possible method selector.

## Idea GCL-I04: Heterophily-Type Signed Relation Contrast

- Idea ID: GCL-I04
- Title: 异配类型感知的 signed relation contrast
- Primary gap: G5
- Core problem: heterophily is not one phenomenon; label, feature, role and directed heterophily imply different SSL relations.
- Why current methods fail: HLCL high/low-pass filters can mix role equivalence with class similarity; SPGCL positive sampling does not define relation ontology.
- Closest works: HLCL, SPGCL, directed GCL, supervised heterophily GNNs.
- What closest works already solve: heterophily filters, positive sampling, performance on several heterophily benchmarks.
- What remains open: which relation should be aligned, separated or predicted under each heterophily type.
- Core hypothesis: signed multi-relation contrast better matches heterophily subtypes than binary positive/negative or universal filters.
- Method sketch: estimate relation type from ego graph; align homophilic-same relations; prototype-align role-equivalent nodes; predict context for complementary heterophilic relations; send uncertain relations to masked diagnostics; report by subtype.
- Relation to SSL theory: extends InfoNCE's binary relation into signed multi-relation objectives with masked context prediction.
- Mechanism: positive + negative + masked + prototype.
- Not a simple trick: changes the contrastive relation ontology.
- Minimum novelty condition: explains failures not captured by HLCL-style filters.
- Minimum falsification experiment: compare signed relation contrast to HLCL-style filters on heterophily subtypes.
- Kill condition: relation type cannot be estimated or never beats HLCL/SPGCL.
- Support condition: clear improvement on at least one heterophily subtype and honest explanation of non-improving subtypes.
- Expected datasets/splits: Actor, Chameleon, Squirrel, Penn94, Twitch, Genius plus homophily sanity checks.
- Expected evaluator: frozen encoder + logistic regression; subtype/worst-group reporting.
- Risk: HIGH
- Difficulty: HIGH
- Contribution type: method.

## Idea GCL-I05: Bad Positive Views as Masked Counter-Evidence

- Idea ID: GCL-I05
- Title: Positive failure prediction as training signal
- Primary gap: G1 + G3
- Core problem: failed augmentations are usually discarded or avoided, but failures can reveal label-relevant context.
- Why current methods fail: GCA avoids important perturbations; GraphMAE reconstructs random masks; neither learns from positive-pair failure.
- Closest works: GCA, G-Censor, GraphMAE2, MaskGAE.
- What closest works already solve: adaptive augmentation, counterfactual views, masked latent prediction.
- What remains open: using failed positive views as supervised-by-structure counter-evidence.
- Core hypothesis: predicting which perturbations break positive validity teaches the encoder what context should not be invariant.
- Method sketch: generate perturbations and view consistency; route low-consistency views to masked counter-evidence instead of alignment; predict failed ego-context latent; align high-consistency views; analyze failure-prediction vs downstream accuracy.
- Relation to SSL theory: pre-audits InfoNCE alignment and uses masked modeling for failed positives.
- Mechanism: positive + masked.
- Not a simple trick: failed views become a distinct learning task, not a gated-out loss item.
- Minimum novelty condition: distinct from GCA avoidance and GraphMAE random masking.
- Minimum falsification experiment: compare random masking, GCA adaptive augmentation and failure-driven masking.
- Kill condition: failure-driven masking is no more predictive than random masking and does not help downstream.
- Support condition: failure prediction identifies label-relevant perturbations and improves robustness.
- Expected datasets/splits: citation, Amazon/Coauthor and noisy-structure variants; 10/10/80 JSON splits.
- Expected evaluator: frozen encoder + logistic regression plus positive failure diagnostic.
- Risk: MEDIUM-HIGH
- Difficulty: MEDIUM
- Contribution type: hybrid GCL-MGM method.

## Idea GCL-I06: Worst-Regime Relation Repair

- Idea ID: GCL-I06
- Title: Worst-regime contrastive learning
- Primary gap: G7 companion to G1/G2/G5
- Core problem: mean accuracy hides low-degree, boundary, noisy or minority homophily-regime failures.
- Why current methods fail: most GCL papers report dataset-level mean±std, not worst-bin behavior.
- Closest works: GroupDRO, robust GNNs, HLCL, ProGCL.
- What remains open: whether relation repair improves worst-bin performance beyond simple reweighting.
- Core hypothesis: validation-only structural bins expose hidden relation failures; repairing relations in worst bins improves robustness.
- Method sketch: define degree/homophily/noise/boundary bins without test labels; estimate bin-wise alignment/uniformity; repair relations in worst bins; report mean and worst-bin; test tradeoff.
- Mechanism: positive + negative diagnostics.
- Not a simple trick: relation repair and reporting protocol, not only GroupDRO-style loss weighting.
- Minimum novelty condition: mean-worst ranking reversal and repair better than reweighting.
- Falsification: bin GRACE/GCA/BGRL/ProGCL and compare worst-bin vs mean.
- Risk: MEDIUM
- Difficulty: MEDIUM
- Contribution type: companion diagnostic/method.

## Idea GCL-I07: Balanced Semantic Prototypes

- Idea ID: GCL-I07
- Title: Balanced semantic prototypes for graph contrast
- Primary gap: G1 + G2
- Core problem: prototype/cluster GCL can learn degree/community popularity instead of class semantics.
- Closest works: AFGRL, SPGCL, prototypical/cluster GCL, SwAV/DeepCluster transfers.
- Hypothesis: balancing prototypes by feature diversity, degree distribution and homophily diversity reduces false positives/negatives.
- Method sketch: online balanced prototypes; swapped assignments; align within confident prototypes; use masked prediction for uncertain nodes; audit purity with validation labels only.
- Mechanism: prototype + positive + masked.
- Not a simple trick: prototype assignment mechanism, not scalar weighting.
- Falsification: compare ordinary, degree-balanced and degree+feature+homophily-balanced prototypes.
- Risk: MEDIUM-HIGH
- Difficulty: MEDIUM
- Contribution type: prototype method.

## Idea GCL-I08: Leakage-Safe Text Semantic Auditor

- Idea ID: GCL-I08
- Title: Leakage-safe text semantics as contrastive auditor, not pseudo-label teacher
- Primary gap: G6
- Core problem: LLM/TAG signals may help pair validity but risk benchmark leakage.
- Closest works: LangGSL, CM-GCL, TAPE-like TAG methods, LLM graph annotator work.
- Hypothesis: frozen text embeddings can audit pair validity without producing pseudo-labels.
- Method sketch: define leakage policy; use frozen text embeddings for pair agreement only; compare graph-only, text-auditor and pseudo-label variants; report contamination risks.
- Mechanism: semantic positive/negative auditor.
- Not a simple trick: contribution is leakage-safe audit protocol.
- Falsification: if only pseudo-labels help, the safe auditor is insufficient.
- Risk: HIGH
- Difficulty: HIGH
- Contribution type: protocol/method, deferred.

## Idea GCL-I09: Three-Way Graph SSL Collapse Diagnostics

- Idea ID: GCL-I09
- Title: Collapse is not one thing
- Primary gap: G4 companion to G3/G5
- Core problem: no-negative graph SSL can fail by rank collapse, oversmoothing or class mixing.
- Closest works: BGRL, CCA-SSG, Graph Barlow Twins, VICReg.
- Hypothesis: graph-specific smoothing/class-mixing failures predict node-classification drops beyond variance/covariance metrics.
- Method sketch: define rank/variance, neighbor smoothing and class-mixing diagnostics; trace BGRL/CCA-SSG/GBT/AFGRL; apply diagnosis-specific repair; report whether diagnostics precede failure.
- Mechanism: no-negative + diagnostic repair.
- Not a simple trick: collapse taxonomy and matched repair.
- Falsification: ordinary variance/covariance explains all failures.
- Risk: MEDIUM
- Difficulty: MEDIUM
- Contribution type: diagnostic-to-method.

## Idea GCL-I10: Local Environment Invariance

- Idea ID: GCL-I10
- Title: Local environment invariance for node-level GCL
- Primary gap: G5 + G8
- Core problem: transductive GCL invariances may not hold across local graph environments.
- Closest works: GCC/G5, IRM, RGCL, BGRL large-scale.
- Hypothesis: relations stable across degree/homophily/noise/ego-density environments generalize better.
- Method sketch: construct local environments inside one graph; estimate relation consistency across environments; train on stable relations; evaluate held-out environments; keep cross-graph only secondary.
- Mechanism: relation invariance.
- Not a simple trick: held-out environment falsification.
- Falsification: local environment invariance does not predict held-out performance.
- Risk: HIGH
- Difficulty: HIGH
- Contribution type: setting-opening method, deferred.

## Initial Ranking From Idea Generation

1. GCL-I03
2. GCL-I02
3. GCL-I01
4. GCL-I04
5. GCL-I05
6. GCL-I09
7. GCL-I07
8. GCL-I06
9. GCL-I08
10. GCL-I10
