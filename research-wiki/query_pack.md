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

## Stage 3.1.5 Loader / Split Smoke Status

Environment dependencies are available (`torch`, `torch_geometric`, `dgl`, `numpy`, `sklearn` all importable), but the target dataset caches are absent:

- Cora: `download_required_not_approved`
- Wiki-CS: `download_required_not_approved`
- Actor: `download_required_not_approved`

Metadata files were written under `dataset_metadata/stage3_1_5/` and validated against `schemas/dataset_metadata_schema.json`. No split JSON files were written because downloads are not approved and local caches are missing.

Auditor verdict: `BLOCKED`. Post-audit fixes applied: split schema now requires `class_distribution_test=null`; placeholder Cora split generation was disabled until labels can be safely read from an approved local cache; command provenance was added to the Stage 3.1.5 report.

Stage 3.1.5 verdict: `BLOCKED`. This is a data-access/cache blocker, not an experimental result. No training, evaluator, GPU, baseline clone, pilot run or accuracy exists. Stage 3.2 planning and pilot execution remain disallowed until data access is explicitly resolved and a rerun passes independent review.

## Stage 3.1.6 Controlled Dataset Access Status

User explicitly authorized `DATA_ACCESS_MODE=controlled_download` for Cora, Wiki-CS and Actor only, through PyG official dataset loaders. No hand-written URL downloader, baseline clone, dependency install, training, evaluator, GPU command, pilot run, accuracy, loss or performance table was used.

Dataset status:

- Cora: blocked by PyG Planetoid official source timeout, `FSTimeoutError`; metadata written at `dataset_metadata/stage3_1_6/Cora.json`; no Cora split JSON.
- Wiki-CS: available; metadata at `dataset_metadata/stage3_1_6/Wiki-CS.json`; official splits written and validated at `splits/Wiki-CS/split_seed_0.json`, `splits/Wiki-CS/split_seed_1.json`, `splits/Wiki-CS/split_seed_2.json`.
- Actor: available; metadata at `dataset_metadata/stage3_1_6/Actor.json`; fixed heterophily splits written and validated at `splits/Actor/split_seed_0.json`, `splits/Actor/split_seed_1.json`, `splits/Actor/split_seed_2.json`.

Split status:

- Wiki-CS split type: `official_wikics`.
- Actor split type: `heterophily_fixed`.
- All written split files have `class_distribution_test=null`.

Stage 3.1.6 executor verdict: `GO` because at least two datasets completed metadata + validated split JSON. Fresh `gcl_experiment_auditor` verdict: `WARN`.

This only allows Stage 3.2 planning / implementation approval. Stage 3.2 pilot run remains disallowed until a separate approval. Do not mix Cora custom, Wiki-CS official and Actor fixed split results in one directly comparable main table.

### Stage 3.1.6 Cora Fix

Cora data access was repaired after the initial `FSTimeoutError`. The code still uses PyG `Planetoid`; if the default `github.com/.../raw/...` endpoint times out, it temporarily switches `Planetoid.url` to the same official `kimiyoung/planetoid` raw GitHub endpoint and lets the PyG loader download/process the dataset.

Current Cora status:

- Metadata: `dataset_metadata/stage3_1_6/Cora.json`
- Split files: `splits/Cora/split_seed_0.json`, `splits/Cora/split_seed_1.json`, `splits/Cora/split_seed_2.json`
- Split type: `custom_stratified_random_1_1_8`
- Split counts: train 271 / validation 271 / test 2166
- `class_distribution_test=null`

Current Stage 3.1.6 data status: Cora, Wiki-CS and Actor all have metadata + validated split JSON. No training, evaluator, GPU use, baseline clone, accuracy/loss/performance table, completed experiment or pilot run has occurred.

### Stage 3.1.6R Reconciliation

Stage 3.1.6R reconciled the mismatch between the final Stage 3.1.6 artifacts and the older auditor report. Metadata recheck PASS, split recheck PASS, and boundary check PASS.

Fresh `gcl_experiment_auditor` verdict: `WARN`, with no reconciliation blocking issue. Previous Cora auditor inconsistency is resolved: `splits/Cora/split_seed_0.json`, `splits/Cora/split_seed_1.json`, and `splits/Cora/split_seed_2.json` exist and validate with `split_type=custom_stratified_random_1_1_8` and `class_distribution_test=null`.

Stage 3.2 planning / implementation approval is allowed. Stage 3.2 pilot run remains forbidden until a separate approval and run manifest. No completed experiment, accuracy, loss, performance table, GPU output, evaluator run, training run, or baseline clone exists from Stage 3.1.6R.

Protocol warning remains active: Cora custom, Wiki-CS official, and Actor fixed splits must not be mixed into one directly comparable main table.

### Stage 3.2P Pilot Planning

Stage 3.2P completed planning / implementation approval only. It generated scope, data/split readiness, pilot scope, method implementation, evaluator, budget parity, metric freeze, result logging, run manifest draft, and execution-gate documents under `refine-logs/`.

Data/split readiness: PASS for Cora, Wiki-CS, and Actor metadata plus seeds 0/1/2 split JSON. Split protocols remain different: Cora custom stratified random 1:1:8, Wiki-CS official, Actor heterophily fixed. Future results may compare methods within each dataset only and must not put these protocols into one directly comparable main table.

Pilot plan scope: GRACE, BGRL, GraphMAE over Cora/Wiki-CS/Actor seeds 0/1/2, 27 future pilot runs. This is pilot-only and cannot support SOTA, robustness, formal, paper main-table, or survival claims.

Fresh `gcl_experiment_auditor` verdict: `WARN`, no Stage 3.2P planning blocking issue. Stage 3.2E implementation / execution preparation is allowed with WARN if explicitly requested later. Direct pilot run remains blocked because methods are placeholders, the evaluator is synthetic-only, the manifest is draft-only with `execution_allowed=false`, and a later execution gate must pass.

No completed experiment, training run, evaluator run, GPU use, baseline clone, accuracy, loss, performance table, result file, or pilot run exists from Stage 3.2P. Stage 3.2E must not start automatically.
