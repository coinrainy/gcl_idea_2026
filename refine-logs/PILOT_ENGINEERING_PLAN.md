# Pilot Engineering Plan

Date: 2026-06-25
Stage: Stage 3.0

## 1. Stage 3.1 Minimal Implementation Goal

Stage 3.1 should implement only the scaffolding needed for a future smoke test:

- dataset loader adapters for selected datasets;
- split JSON reader/writer validation;
- shared encoder interface;
- frozen linear evaluator interface;
- raw result logger;
- metric extraction interface stubs or minimal label-free metrics;
- config skeletons for GRACE, BGRL and GraphMAE.

Stage 3.1 should not run pilot experiments.

## 2. Unified Framework vs Wrapper

Prefer a single unified framework for Stage 3.1. Use PyG-style data objects if feasible because Cora, Wiki-CS and Actor are commonly available through PyG loaders. The unified framework should own:

- split reading;
- encoder construction;
- evaluator;
- logging;
- metric saving.

Wrappers around official implementations are fallback only. If wrappers are used, they must export embeddings to the shared frozen evaluator and write raw results through the shared schema.

## 3. Priority Methods

Implementation order:

1. GRACE minimal objective.
2. BGRL minimal objective.
3. GraphMAE minimal masked-feature objective or wrapper with disabled official evaluator.

Do not implement ProGCL in Stage 3.1 unless a later readiness fix requires an audit stub.

## 4. Priority Datasets

Support in order:

1. Cora.
2. Wiki-CS.
3. Actor.

Fallbacks:

- PubMed for Cora;
- Coauthor-CS for Wiki-CS;
- Chameleon for Actor.

## 5. Split Generation And Reading Flow

Stage 3.1 may implement split generation code but should not run large experiments.

Required flow:

1. choose split protocol per dataset;
2. generate or load official split;
3. save JSON following `schemas/split_schema.json`;
4. validate disjoint train/val/test indices;
5. every method receives only `split_file` path, never generates its own split.

## 6. Label-Free Metric Flow

Required flow:

1. compute label-free metrics before label-audit and before validation outcome;
2. save `results/metrics/pilot/{dataset}/split_seed_{seed}_label_free.json`;
3. mark `artifact_type: label_free_regime_metrics`, `selector_visible: true` and `metric_freeze_status: frozen_before_validation_outcome`;
4. compute a `freeze_hash`;
5. save any label-audit metrics to `results/metrics/pilot/{dataset}/split_seed_{seed}_label_audit.json` with `selector_visible: false`;
6. prevent metric files from being overwritten after validation ranking is known.

## 7. Unified Evaluator

All SSL methods must output frozen node embeddings. The evaluator should:

- train a linear classifier on train indices;
- select epoch by validation accuracy;
- report `valid_at_best`, `test_at_best`, `final_valid`, `final_test`;
- never use test accuracy for early stopping;
- write results through `schemas/raw_result_schema.json`.
- record evaluator seed, early-stopping metric, patience, max epochs, split file, config hash, run command and result file path.

## 8. Result Logging Flow

Every run, including failure, writes one raw JSON file:

```text
results/raw/pilot/{dataset}/{method}/{run_id}.json
```

The logger must capture method, objective family, evaluation setting, graph visibility, split path/type, split seed, model seed, config path/hash, run command, commit hash, status, failure reason, evaluator type/seed, early-stopping details, backbone/budget fields, result file path, time, memory and log path.

## 9. Summary Script Plan

Stage 3.1 may create a summary script skeleton, but Stage 3.0 does not. Future summary scripts must:

- read raw JSON only;
- include failed runs in diagnostics;
- never manually copy best numbers;
- keep pilot summaries separate from formal summaries.

## 10. Smoke Test Plan

Smoke tests are Stage 3.1 only. Planned smoke tests:

- schema validation on a tiny synthetic split object;
- one loader import check without downloading extra data unless explicitly approved;
- evaluator dry path on synthetic embeddings;
- logger writes failure record correctly;
- no real dataset training.

No smoke test is run in Stage 3.0.

## 11. Things Stage 3.1 Does Not Do

- no pilot run;
- no GPU experiment;
- no formal experiment;
- no paper table;
- no SOTA claim;
- no ProGCL method implementation by default;
- no hidden split generation inside methods;
- no GraphMAE official evaluator if it cannot be unified.

## 12. Blocking Issues Before True Pilot Run

True Stage 3.2 pilot run is blocked until:

- split JSON files exist and validate for all selected datasets/seeds;
- GRACE/BGRL/GraphMAE share a frozen evaluator;
- pretraining budgets are comparable and documented;
- raw result logger is implemented and tested;
- metric freeze mechanism exists;
- failed-run logging works;
- transductive/inductive setting and graph visibility are explicit and equal across methods;
- shared split files expose no test-label distribution to selector/training code;
- auditor approves Stage 3.1 output for Stage 3.2 pilot.

## Special Engineering Checks

If GRACE / BGRL / GraphMAE official implementations differ too much, use unified minimal implementations first. If GraphMAE evaluator differs from GCL evaluator, discard the official evaluator and use frozen linear evaluation on exported embeddings. If dataset split protocols differ, do not put them into one comparable ranking table without explicit `split_type`. If method budget differs, define comparable budget by matched encoder, hidden dimension, pretrain epochs or wall-clock cap and report any unavoidable mismatch.
