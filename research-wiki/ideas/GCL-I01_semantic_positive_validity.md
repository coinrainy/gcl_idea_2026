# GCL-I01: Semantic-Preserving Positive Validity Tests

- Stage: Stage 2A
- Status: REVISE
- Primary gap: G1
- Closest works: GCA, AFGRL, G-Censor, SPGCL, CM-GCL
- Reviewer verdict: REVISE

## Summary

Accept positive graph views only when structural consistency, feature stability and masked-latent context predictability agree. Failed views become diagnostics, not positives.

## Why Not Final

Reviewer warns it may look like positive gate plus masked auxiliary loss unless validity score independently predicts failure beyond GCA/AFGRL/G-Censor/SPGCL.

## Falsification

Fixed GRACE/GCA/AFGRL under same split/evaluator; compute positive-validity score vs validation/test@best correlation. Kill if correlation is weak.
