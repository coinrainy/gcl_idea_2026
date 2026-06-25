# GCL-I02: Regime-Conditioned Negative Validity Boundary

- Stage: Stage 2B
- Status: AUXILIARY_AUDIT_FALLBACK
- Primary gap: G2
- Closest works: ProGCL, Negative Metric Learning for Graphs, counterfactual hard negatives, SPGCL, HLCL
- Reviewer verdict: KEEP

## Summary

Predict when hard negatives are harmful using local homophily proxy, feature similarity and structural role similarity. Confident negatives remain in InfoNCE; ambiguous relations use safer separation/audit.

## Why It Remains Open

The intended contribution is not reweighting. It is a regime boundary explaining where ProGCL-style hard-negative mining helps or fails.

## Falsification

On two homophilic and two heterophilic datasets, use validation labels only for audit and test whether predicted false-negative/ambiguous pairs match label agreement. Kill if predictions are random or merely duplicate ProGCL weights.

## Stage 2B Update

Decision: not selected as dominant idea.

Role: auxiliary negative-validity audit and fallback. It may explain why contrastive objectives lose under the active `GCL-I03` protocol-aligned pilot, but it must not become a training signal, selector input, or ProGCL-style reweighting method in Stage 3 pilot.

Escalate to main route only if `GCL-I03` fails but label-free negative-validity metrics consistently explain objective ranking and remain clearly separated from ProGCL, GRAPE, Negative Metric Learning for Graphs and BalanceGCL.
