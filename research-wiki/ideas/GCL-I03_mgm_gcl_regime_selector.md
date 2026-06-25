# GCL-I03: Protocol-Aligned MGM-vs-GCL Regime Selector

- Stage: Stage 2B
- Status: ACTIVE_SELECTED
- Primary gap: G3
- Closest works: GraphMAE, GraphMAE2, MaskGAE, CORE, GCMAE, GRACE, GCA, BGRL
- Reviewer verdict: KEEP

## Summary

Compare contrastive, bootstrap and masked graph SSL objectives under identical split, seed, backbone, evaluator and budget. Test whether graph-regime metrics predict the objective winner.

## Why It Remains Open

Published tables are not directly comparable. The contribution is a protocol-aligned objective boundary, not a new SOTA objective.

## Falsification

Rerun GRACE/GCA/BGRL/GraphMAE-style variants under the same evaluator and check whether label-free graph-regime metrics such as feature-neighborhood smoothness, reconstruction difficulty, augmentation stability and structural role statistics predict objective ranking. Label-derived metrics such as feature-label predictability and label homophily are audit-only. Kill if label-free metrics do not predict ranking.

## Stage 2B Update

Decision: SELECT as active idea for Stage 3 pilot.

Refined contribution: protocol-aligned label-free graph SSL regime diagnostic. Label-free metrics may predict objective-family suitability; label-derived metrics are audit-only and must not train or select.

`GCL-I02` is retained only as an auxiliary negative-validity audit for contrastive failures. This is not a full merge and not a new hard-negative reweighting method.
