# GCL-I02: Regime-Conditioned Negative Validity Boundary

- Stage: Stage 2A
- Status: KEEP
- Primary gap: G2
- Closest works: ProGCL, Negative Metric Learning for Graphs, counterfactual hard negatives, SPGCL, HLCL
- Reviewer verdict: KEEP

## Summary

Predict when hard negatives are harmful using local homophily proxy, feature similarity and structural role similarity. Confident negatives remain in InfoNCE; ambiguous relations use safer separation/audit.

## Why It Remains Open

The intended contribution is not reweighting. It is a regime boundary explaining where ProGCL-style hard-negative mining helps or fails.

## Falsification

On two homophilic and two heterophilic datasets, use validation labels only for audit and test whether predicted false-negative/ambiguous pairs match label agreement. Kill if predictions are random or merely duplicate ProGCL weights.
