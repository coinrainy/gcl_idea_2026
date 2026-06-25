# DeepXiv Targeted Search

Date: 2026-06-25

Raw files: `notes/stage1_6_deepxiv/search_*.txt`.

## Query Results

| Query | Top relevant hits | Stage 2 action |
| --- | --- | --- |
| graph contrastive learning node classification | CDLG (`2306.11344`), supervised GCL for few-shot node classification (`2203.15936`), Coarse-to-Fine CL (`2212.06423`), HCL (`2210.12020`), MVGRL (`2006.05582`) | Add as secondary risk items if Stage 2 targets node-specific contrast objectives. |
| graph contrastive learning false negatives | Negative Metric Learning for Graphs (`2505.10307`), counterfactual hard negatives (`2207.00148`), graph ranking CL (`2310.14525`) | Extend G2 risk list; do not claim generic hard-negative novelty. |
| graph contrastive learning positive samples | node similarity positives (`2208.06743`), counterfactual hard negatives (`2207.00148`), implicit mechanisms (`2311.02687`), pair-wise augmentation (`2402.10468`), SPGCL-related positive sampling (`2206.11959`) | Keep G1/G2 high risk; SPGCL remains the strongest recent blocker. |
| negative-free graph contrastive learning | robust GCL (`2102.13085`), LocalGCL (`2212.04604`), HCL (`2210.12020`) | Keep G4 as diagnostic companion rather than main novelty by default. |
| masked graph modeling node classification | MaskGAE (`2205.10053`), MGAE (`2201.02534`), GraphMAE-adjacent prompting/pretraining (`2407.15431`) | Keep G3; compare MGM vs GCL only after protocol alignment. |
| graph contrastive learning heterophily | HLCL (`2303.06344`), robust GCL/GROC (`2102.13085`), heterophilic hypergraph CL (`2511.18783`), homophily-aware heterogeneous GCL (`2501.08538`), GCL-OT (`2511.16778`) | Keep G5/G2 high risk; add GCL-OT and hypergraph items as Stage 2 checks if heterophily is selected. |
| graph contrastive learning augmentation | GMA/GMCL (`2401.03638`), ArieL (`2202.06491`), GraphCL (`2010.13902`), GPA (`2209.06560`), iGCL (`2211.03710`) | Block simple augmentation novelty; use as secondary readings for G1. |
| graph contrastive learning prototype clustering | GCC clustering (`2104.01429`), SCAGC (`2110.08264`), prototypical GCL (`2106.09645`), center-oriented prototype clustering (`2508.15231`) | Prototype direction needs separate novelty audit; not enough for final idea. |
| LLM graph self-supervised learning node classification | label-free graph learning with LLM annotators (`2605.27913`), N2N alignment (`2302.04626`), CDLG (`2306.11344`) | G6 stays promising but leakage-risky; no direct GCL protocol claim. |
| graph contrastive learning robustness structural noise | GROC (`2102.13085`), adversarial robustness of GCL (`2311.17853`), FedRGL (`2411.18905`) | Keep G7 as robustness reporting companion; no mean-accuracy-only robustness claim. |

## High-Risk Paper Reads

| Paper | DeepXiv status | Protocol evidence recovered | Still `UNCLEAR` |
| --- | --- | --- | --- |
| GRACE (`2006.04131`) | brief/head/Experiments available | node-level augmentation GCL, transductive evaluation context | exact saved split files, seed list, test@best |
| GCA (`2010.14945`) | brief/head/Experiments/Implementation Details available | Wiki-CS public split; Amazon/Coauthor random 10/10/80; frozen logistic evaluation; 20 runs | exact seed list and test@best |
| ProGCL (`2110.02027`) | brief/head/Experiments available | false-negative-aware hard negative mining confirmed | exact split/seed/test@best details |
| AFGRL (`2112.02472`) | brief/head/Experiments available | augmentation-free positives; logistic evaluator; reports test when validation is best | exact seed list |
| CCA-SSG (`2106.12484`) | brief/head/Experiments/Implementation Details available | public citation splits; 10/10/80 for Amazon/Coauthor in appendix; frozen logistic evaluator | split ambiguity across main/appendix, test@best |
| Graph Barlow Twins (`2106.02466`) | brief/head/Experiments/Ablation/Appendix available | no-negative/decorrelation risk confirmed | exact evaluator/splits/seeds still not enough for A-class |
| GraphMAE (`2205.10803`) | brief/head/Experiments/Appendix available | masked feature reconstruction; public/OGB split evidence | test@best and exact evaluator alignment |
| GraphMAE2 (`2304.04779`) | brief/head/Experiments/Appendix available | OGB-style large-scale evaluation, linear probing/fine-tuning variants | Stage-2 GCL comparability requires rerun |
| MaskGAE (`2205.10053`) | brief/head/Experiments/Appendix available | Photo/Computer node classification uses 1:1:8; frozen linear classifier stated | exact seeds and test@best |
| HLCL (`2303.06344`) | brief/head/Experiments available | heterophily graph-filter risk confirmed | acceptance status, exact split/evaluator/seeds |
| LangGSL (`2410.12096`) | brief/head/Experiments available | LLM/GSLM semantic-prior and robustness risk confirmed | leakage protocol, exact split/evaluator/seeds |
| SPGCL (`2606.10284`) | brief/head/Experiments/Appendix available | homophily/heterophily node classification, frozen linear classifier, ten repeats, ablation table | exact saved splits, seed identities, test@best |

## Direct Comparability

No DeepXiv-read paper is marked directly comparable under `BENCHMARK_PROTOCOL.md`.

Reason: even when split type and evaluator are described, the project still lacks exact saved split JSON, identical seed list, and confirmed `test@best validation epoch` behavior for the published tables.
