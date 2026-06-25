# GCL-I09: Three-Way Graph SSL Collapse Diagnostics

- Stage: Stage 2A
- Status: REVISE
- Primary gap: G4
- Closest works: BGRL, CCA-SSG, Graph Barlow Twins, AFGRL, VICReg
- Reviewer verdict: REVISE

## Summary

Distinguish rank collapse, neighbor oversmoothing and class mixing in no-negative graph SSL.

## Why Not Main

Useful diagnostic, likely companion to GCL-I03. Needs proof that diagnostics predict failure before accuracy drops.

## Falsification

Track rank, variance, neighbor smoothing and class-mixing diagnostics for BGRL/CCA-SSG/GBT/AFGRL. Kill standalone if ordinary variance/covariance explains all failures.
