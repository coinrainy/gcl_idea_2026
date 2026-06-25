# Stage 3.2P Pilot Scope

Date: 2026-06-26
Stage: Stage 3.2P Pilot Planning / Implementation Approval

## Pilot Status

The future Stage 3.2 pilot remains `pilot`, not `formal`.

This document only defines planned future scope. It does not execute any run.

## Dataset Scope

| Dataset | Split type | Seeds | Split files |
| --- | --- | --- | --- |
| Cora | `custom_stratified_random_1_1_8` | 0, 1, 2 | `splits/Cora/split_seed_{0,1,2}.json` |
| Wiki-CS | `official_wikics` | 0, 1, 2 | `splits/Wiki-CS/split_seed_{0,1,2}.json` |
| Actor | `heterophily_fixed` | 0, 1, 2 | `splits/Actor/split_seed_{0,1,2}.json` |

## Method Scope

| Method | Objective family |
| --- | --- |
| GRACE | `negative_based_contrastive` |
| BGRL | `bootstrap_negative_free` |
| GraphMAE | `masked_graph_modeling` |

## Planned Future Run Count

3 datasets x 3 methods x 3 seeds = 27 pilot runs.

## Reporting Limits

- Every future run must be labeled `pilot`.
- Seeds are limited to `[0, 1, 2]`.
- Each dataset must use its existing split files.
- Comparisons are only within each dataset across GRACE / BGRL / GraphMAE.
- No cross-dataset direct mean ranking.
- No SOTA claim.
- No robustness claim.
- No paper main table.
- No formal conclusion.
- No survival decision unless a later Stage 3.2E execution finishes and then passes an independent result-to-claim / auditor review.

## Current Permission

Planning only. No training, evaluator run, pilot execution, GPU use, baseline clone, result file, or performance table is allowed in Stage 3.2P.
