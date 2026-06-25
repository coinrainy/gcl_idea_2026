# Raw Result Schema Explanation

Date: 2026-06-25

## Purpose

`schemas/raw_result_schema.json` defines the minimum record for every future pilot run.

## Rules

- 所有 pilot run 的 `stage` 必须是 `pilot`。
- Failed runs 也必须记录，`status` 为 `fail`，并填写 `failure_reason`。
- Summary table 必须从 raw JSON 自动生成。
- 不得手工复制 best number。
- Pilot result 不支持 SOTA、formal claim、robust claim 或论文主表结论。

## Field Notes

- `run_command`, `config_path`, `config_hash`, `split_file`, `result_file_path`, `log_path` and `commit_hash` are required for traceability.
- `evaluation_setting` must be `transductive` or `inductive`; Stage 3.1 default should be explicit transductive node classification only if all methods get the same graph visibility.
- `graph_visibility` must describe whether all methods can see the same graph structure/features during unsupervised pretraining and metric extraction.
- `valid_at_best` records validation metric at the selected validation epoch.
- `test_at_best` may be logged for later auditing, but must not drive model selection, selector design, survival decision, hyperparameter choice, or checkpoint choice.
- `final_valid` and `final_test` record the last epoch metrics for debugging.
- `evaluator_type` should be `frozen_encoder_linear_evaluator` unless a future approved protocol says otherwise.
- `evaluator_seed`, `early_stopping_metric`, `patience` and `max_epochs` must be recorded to satisfy evaluator traceability.
- `backbone`, `hidden_dim`, `projection_dim`, `pretrain_epochs` and `budget_policy` must be recorded so GRACE/BGRL/GraphMAE budget differences are auditable.
- `training_time_sec` and `peak_memory_mb` are required for budget comparability; may be `null` only for failed runs before training starts.

## Future Path Convention

```text
results/raw/pilot/{dataset}/{method}/{run_id}.json
```

Stage 3.0 does not create raw result files.
