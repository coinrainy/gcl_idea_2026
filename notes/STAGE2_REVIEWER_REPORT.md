# Stage 2A Reviewer Report

Reviewer: fresh `gcl_scientific_reviewer`

Input files only:

- `RESEARCH_BRIEF.md`
- `BENCHMARK_PROTOCOL.md`
- `research-wiki/query_pack.md`
- `notes/CLOSEST_WORK_DELTA_TABLE.md`
- `notes/STAGE2_FILTERED_IDEAS.md`
- `notes/stage2_novelty/`

Executor summary was not provided to the reviewer.

## Overall Evidence Status

Current materials contain idea proposals and novelty-check notes only. There are no smoke, pilot, development or formal experiments. Therefore no performance, robustness or SOTA claim is supported.

Common alternative explanations to control later: protocol differences, added objective/capacity/search budget, validation-label leakage, text/semantic leakage.

## Reviewer Recommendation

Main candidates:

1. `GCL-I03`
2. `GCL-I02`

Backup:

1. `GCL-I04`

Other ideas should be revised as diagnostics or killed/deferred.

## Per-Idea Verdicts

| Idea | Verdict | Priority | Strongest closest work | Summary |
| --- | --- | --- | --- | --- |
| GCL-I03 | KEEP | 1 | GraphMAE, GraphMAE2, MaskGAE, CORE, GCMAE, Revisiting Graph Autoencoders | Best candidate, but should be framed as diagnostic/benchmark objective-boundary work, not a strong new method. |
| GCL-I02 | KEEP | 2 | ProGCL, Negative Metric Learning for Graphs, counterfactual hard negatives, SPGCL, HLCL | Main method candidate if reframed as "when hard negatives are harmful" regime boundary, not reweighting. |
| GCL-I04 | REVISE | 3 | HLCL, GCL-OT, DSSL, HGRL, GraphACL, SPGCL | Backup; first prove heterophily subtype diagnostic before full method. |
| GCL-I01 | REVISE | 4 | GCA, AFGRL, G-Censor, SPGCL, CM-GCL | Real problem but risks becoming positive gate + masked auxiliary loss. |
| GCL-I09 | REVISE | 5 | BGRL, CCA-SSG, Graph Barlow Twins, AFGRL, VICReg | Useful diagnostic, likely companion to I03. |
| GCL-I06 | REVISE | 6 | GroupDRO, robust GNNs, HLCL, ProGCL | Useful worst-bin reporting companion; not main method. |
| GCL-I08 | REVISE | 7 | LangGSL, CM-GCL, TAPE/TAG LLM methods | Leakage audit may dominate; not main Stage 2 route. |
| GCL-I05 | KILL | 8 | GCA, G-Censor, GraphMAE2, MaskGAE, CORE/GCMAE | Too much like module fusion. Keep only as I01 ablation if needed. |
| GCL-I07 | KILL | 9 | AFGRL, SPGCL, prototypical/cluster GCL | Prototype/cluster route too crowded and likely incremental. |
| GCL-I10 | KILL | 10 | GCC/G5, IRM, RGCL, BGRL large-scale | Scope too broad and cross-domain-heavy. |

## Required Additional Novelty Checks

- `GCL-I03`: 2024-2026 graph SSL benchmark/protocol papers, automated graph SSL objective selection, GCL vs untrained/GAE baseline papers.
- `GCL-I02`: Negative Metric Learning for Graphs, GRAPE/affinity-uncertainty hard negative, BalanceGCL, HomoGCL, homophily-aware heterogeneous GCL.
- `GCL-I04`: GCL-OT, DSSL, HGRL, GraphACL, MUSE/LOHA, relation-aware heterophily learning.

## Lowest-Cost Next Experiments

These are designs only; no experiment was run in Stage 2A.

- `GCL-I03`: same backbone/split/seed/evaluator/budget for GRACE/GCA/BGRL/GraphMAE-style variants; test whether feature-label predictability, edge homophily and reconstruction difficulty predict objective winner. Kill if they do not.
- `GCL-I02`: on two homophilic and two heterophilic datasets, use validation labels only for audit; test whether predicted false-negative/ambiguous pairs match true label agreement and compare ProGCL vs relation-boundary variant. Kill if predictions are random or just reweighting.
- `GCL-I04`: diagnostic only first; on heterophily datasets prove at least one subtype is not explained by HLCL filters. Kill if subtype diagnostic cannot separate failure modes.

## Final Reviewer Verdict

Continue to Stage 2B refine only if the next stage focuses on `GCL-I03` and/or `GCL-I02`, with `GCL-I04` as backup. Do not enter experiments before refine.
