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

## Stage 2A Idea Status

Raw ideas are recorded in `notes/STAGE2_RAW_IDEAS.md` and `research-wiki/ideas/`.

Filtered ideas and novelty checks:

- Main candidate 1: `GCL-I03` protocol-aligned MGM-vs-GCL regime selector. Reviewer verdict `KEEP`; frame as diagnostic/benchmark objective-boundary work.
- Main candidate 2: `GCL-I02` regime-conditioned negative validity boundary. Reviewer verdict `KEEP`; frame as "when hard negatives are harmful", not reweighting.
- Backup: `GCL-I04` heterophily-type signed relation contrast. Reviewer verdict `REVISE`; first prove subtype diagnostic beyond HLCL/GCL-OT.
- Revise/companion: `GCL-I01`, `GCL-I06`, `GCL-I08`, `GCL-I09`.
- Killed: `GCL-I05`, `GCL-I07`, `GCL-I10`; do not regenerate without a new closest-work delta.

Required Stage 2B checks before experiments:

- For `GCL-I03`: graph SSL benchmark/protocol papers, automated graph SSL objective selection, GCL vs untrained/GAE baselines.
- For `GCL-I02`: Negative Metric Learning for Graphs, GRAPE/affinity-uncertainty hard negative, BalanceGCL, HomoGCL, homophily-aware heterogeneous GCL.
- For `GCL-I04`: GCL-OT, DSSL, HGRL, GraphACL, relation-aware heterophily learning.

No idea is accepted as a final method.

## Stage 3.0 Readiness Status

Active idea remains `GCL-I03`; `GCL-I02` remains auxiliary audit / fallback only. Stage 3.0 narrows future readiness to:

- datasets: Cora, Wiki-CS, Actor, with PubMed/Coauthor-CS/Chameleon as fallbacks;
- methods: GRACE, BGRL, GraphMAE as the minimal objective-family set;
- schemas: split JSON, raw result JSON, metric JSON;
- manifest: draft only, not executable;
- engineering direction: prefer unified minimal framework with shared split reader, frozen linear evaluator, logger and metric interface.

No experiment, smoke test, data download, baseline clone or training implementation has been performed in Stage 3.0.

Stage 3.1 remains blocked until auditor review passes or required fixes are applied.

Stage 3.0 auditor result:

- Auditor verdict: `WARN`.
- Stage 3.0 verdict: `GO` limited to Stage 3.1 minimal implementation / smoke-test scaffold.
- Stage 3.2 pilot remains blocked.
- Post-audit fixes applied: raw result traceability fields, metric label-free/audit artifact separation, shared split test-distribution policy, transductive graph visibility declaration.
- Still no experiment, smoke test, dataset download, baseline clone, training implementation or result evidence.

## Stage 3.1 Synthetic Scaffold Status

Stage 3.1 implemented scaffold-only code:

- schema validator;
- synthetic split fixture and split integrity checker;
- raw result logger;
- metric artifact writer with `freeze_hash`;
- selector-safe label-free metric loader;
- frozen evaluator dry-run on synthetic embeddings;
- GRACE/BGRL/GraphMAE method placeholders;
- scaffold-only configs;
- synthetic smoke runner.

Synthetic smoke status: passed via `python scripts/run_stage3_1_synthetic_smoke.py`.

Auditor verdict: `WARN`; no Stage 3.1 blocking issue. Stage 3.1.5 real loader / split generation smoke may be requested next, but only under a separate user request and without training/pilot/GPU/baseline cloning.

No real dataset was accessed. No model was trained. No GPU was used. No baseline repository was cloned. No pilot run or performance claim exists. Stage 3.2 remains blocked.
