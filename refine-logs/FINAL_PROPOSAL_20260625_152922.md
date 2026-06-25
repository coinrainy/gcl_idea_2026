# Final Proposal

Date: 2026-06-25
Stage: Stage 2B refine

## Title

Protocol-Aligned Graph SSL Regime Diagnostic for Node Classification

## Active Idea

`GCL-I03` is the active idea.

`GCL-I02` is retained only as an auxiliary negative-validity audit and fallback.

## One-Sentence Thesis

Under identical node-classification protocol, label-free graph-regime metrics can predict when masked graph modeling, negative-based graph contrastive learning or bootstrap graph SSL is the appropriate objective family.

## Problem Anchor

The graph SSL literature often compares objective families through incompatible experimental protocols. Masked graph modeling papers, contrastive learning papers and bootstrap methods may use different splits, backbones, evaluators, budgets and reporting rules. These mismatches make it unclear whether an objective family is genuinely better for a graph regime or merely advantaged by protocol.

## Proposed Method Concept

Build a diagnostic workflow rather than a new loss:

1. Fix split, seed, backbone, evaluator and budget.
2. Run representative objective families under the same protocol.
3. Compute label-free graph-regime metrics before labels enter the pipeline.
4. Predict objective-family suitability from those metrics.
5. Use validation-only label audits to interpret failures, including a negative-validity audit from `GCL-I02`.

## Dominant Contribution

The dominant contribution is the protocol-aligned label-free regime diagnostic. It aims to answer when each SSL objective family should be trusted, not to claim that one family universally wins.

## Supporting Contribution

The supporting contribution is an audit-only negative-validity analysis adapted from `GCL-I02`. It checks whether contrastive failures correspond to ambiguous or likely false-negative pairs, while avoiding a new hard-negative reweighting claim.

## Explicitly Rejected Complexity

- No new MGM+GCL hybrid objective.
- No learned negative metric module in Stage 3 pilot.
- No LLM or pseudo-label signal.
- No test-label-aided selector.
- No multi-module architecture whose parts cannot be falsified separately.

## Claims To Test

Claim C1: Under matched protocol, objective-family ranking differs by graph regime and is not reliably inferred from published tables.

Claim C2: Label-free graph-regime metrics predict objective-family ranking better than chance in pilot settings.

Claim C3: Label-audit metrics explain failure modes but are not required as selector inputs.

Claim C4: Negative-validity audit explains some contrastive failures without turning the method into ProGCL-style reweighting.

## Closest-Work Boundary

GraphMAE, GraphMAE2, MaskGAE, AUG-MAE, CORE and GCMAE block any claim that a masked objective or masked-contrastive hybrid is the novelty.

ProGCL, GRAPE, Negative Metric Learning for Graphs, BalanceGCL, counterfactual hard negatives, SPGCL, HLCL and HomoGCL block generic hard-negative claims.

The safe novelty claim is protocol-aligned label-free objective-boundary prediction for node classification.

## Stage 3 Pilot Commitment

The next step is a pilot only. It should run a small representative set of datasets and objective families with fixed protocol and pre-registered kill conditions. Pilot results cannot support formal claims.

## Verdict

GO to Stage 3 pilot.
