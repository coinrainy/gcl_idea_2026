# GCL-I06: Worst-Regime Relation Repair

- Stage: Stage 2A
- Status: REVISE
- Primary gap: G7
- Closest works: GroupDRO, robust GNNs, HLCL, ProGCL
- Reviewer verdict: REVISE

## Summary

Use degree/homophily/noise/boundary bins to expose hidden GCL failures and repair relations in worst regimes.

## Why Not Final

Likely to become GroupDRO/reweighting if framed as a method. Best used as reporting/diagnostic companion for GCL-I02 or GCL-I04.

## Falsification

Check whether GRACE/GCA/BGRL/ProGCL mean ranking differs from worst-bin ranking. Kill as standalone if mean and worst-bin always agree.
