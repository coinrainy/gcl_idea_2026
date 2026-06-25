# GCL-I03: Protocol-Aligned MGM-vs-GCL Regime Selector

- Stage: Stage 2A
- Status: KEEP
- Primary gap: G3
- Closest works: GraphMAE, GraphMAE2, MaskGAE, CORE, GCMAE, GRACE, GCA, BGRL
- Reviewer verdict: KEEP

## Summary

Compare contrastive, bootstrap and masked graph SSL objectives under identical split, seed, backbone, evaluator and budget. Test whether graph-regime metrics predict the objective winner.

## Why It Remains Open

Published tables are not directly comparable. The contribution is a protocol-aligned objective boundary, not a new SOTA objective.

## Falsification

Rerun GRACE/GCA/BGRL/GraphMAE-style variants under the same evaluator and check whether feature-label predictability, edge homophily and reconstruction difficulty predict objective ranking. Kill if they do not.
