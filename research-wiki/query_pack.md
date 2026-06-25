# Research Wiki Query Pack

## Project Direction

GCL for node classification with strict evaluation integrity. Stage 2 may use this pack for gap-driven ideation, but must not start from a final method.

## Source Reliability

arXiv/PDF recovery succeeded for high-risk closest works. Semantic Scholar is still rate-limited except BGRL metadata. DeepXiv has been fixed after Stage 1.5 (`deepxiv-sdk==0.3.1`, adapter search/brief verified). Exa unavailable because `EXA_API_KEY` is empty. OpenReview partly recovered; HLCL and G-Censor acceptance status remain `UNCLEAR`.

## Top Closest Works

- GRACE: random edge/feature augmentation + node-level InfoNCE; random 10/10/80 for citation networks; frozen logistic evaluator; 20 runs.
- GCA: adaptive topology/feature augmentation; Wiki-CS public splits, others 10/10/80; frozen logistic evaluator; 20 runs.
- ProGCL: probability-aware hard negatives; follows GCA/BGRL-style splits; 20 random splits/initializations for reproduced baselines.
- BGRL: negative-free bootstrap; WikiCS canonical, Amazon/Coauthor 10/10/80, OGB official, PPI predefined; frozen linear eval.
- CCA-SSG / Graph Barlow Twins / AFGRL: no-negative/decorrelation/augmentation-free positive discovery.
- GraphMAE / GraphMAE2 / MaskGAE: masked graph modeling; strong but evaluator/protocol differs from GCL.
- HLCL: heterophily-aware graph filters; acceptance/protocol details still `UNCLEAR`.
- CM-GCL: NeurIPS 2022, multimodal imbalanced node classification; 70/10/20, fine-tuning, not frozen evaluator.
- G-Censor: task-oriented counterfactual views; OpenReview status and protocol still `UNCLEAR`.
- LangGSL: LLM/TAG semantic prior, robust graph structure learning; split/evaluator/leakage protocol `UNCLEAR`.
- SPGCL/Khan-GCL: recent arXiv positive/hard-negative preprints; treat as parallel risk, not established SOTA.

## Direct Comparability

No published result is directly comparable under `BENCHMARK_PROTOCOL.md`. Even papers using 10/10/80 lack our exact saved split JSON, seed list, and confirmed `test@best validation epoch`.

## Stage 2 Gap Priorities

Prioritize:

- G1 semantic false positives;
- G2 false negatives under homophily/heterophily;
- G3 MGM vs GCL under identical evaluator;
- G5 heterophily boundary conditions.

Use as companion diagnostics:

- G4 collapse/oversmoothing diagnostics;
- G7 worst-group reporting.

Treat carefully or defer:

- G6 LLM semantic priors because leakage risk is high;
- G8 cross-domain generalization because scope may expand too far.

## Novelty Boundaries

- Do not claim better augmentation unless separated from GCA/AFGRL/G-Censor.
- Do not claim false-negative handling unless separated from ProGCL/SPGCL/HLCL.
- Do not claim negative-free novelty unless separated from BGRL/CCA-SSG/GBT/AFGRL.
- Do not claim masked SSL novelty unless separated from GraphMAE2/MaskGAE.
- Do not use LLM/TAG signal without leakage-safe protocol.

## Non-Goal Banlist

No simple gate, reweighting, adapter, residual, temperature schedule, backbone swap, or mechanical vision-SSL transplant. No SOTA claim from published tables with unclear protocol. No final method in Stage 1.5.

## Open Unknowns

- Exact accepted/rejected status for HLCL and G-Censor.
- Exact evaluator/seeds/early stopping for Graph Barlow Twins, HLCL, G-Censor, LangGSL, SPGCL.
- Whether Stage 2 wants a main gap around positives/negatives, MGM comparison, or heterophily boundary conditions.

## Stage 1.6 DeepXiv Addendum

DeepXiv is now usable for targeted arXiv retrieval. Raw Stage 1.6 results are stored in `notes/stage1_6_deepxiv/`, with readable reports in `notes/DEEPXIV_STAGE1_COMPLETION_REPORT.md` and `notes/DEEPXIV_TARGETED_SEARCH.md`.

Additional risk items from targeted search:

- GMA/GMCL (`2401.03638`), ArieL (`2202.06491`), GPA (`2209.06560`) and iGCL (`2211.03710`) strengthen the ban on simple augmentation novelty.
- Negative Metric Learning for Graphs (`2505.10307`), counterfactual hard negatives (`2207.00148`) and graph ranking CL (`2310.14525`) extend G2 false-negative risk.
- GCL-OT (`2511.16778`) and heterophilic hypergraph CL (`2511.18783`) should be checked if Stage 2 selects heterophily.
- Label-free graph learning with LLM annotators (`2605.27913`) strengthens G6 leakage risk.

No Stage 1.6 DeepXiv result is directly comparable under `BENCHMARK_PROTOCOL.md`. Exact saved split JSON, identical seed list and confirmed `test@best validation epoch` remain required.
