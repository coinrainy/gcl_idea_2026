# Stage 3.0 Auditor Report

Date: 2026-06-26
Auditor: fresh `gcl_experiment_auditor`
Mode: subagent read-only review

## Verdict

WARN

Stage 3.0 readiness 足够进入 Stage 3.1 minimal implementation / smoke-test scaffold，但不允许进入真实 pilot、GPU 训练或 Stage 3.2。当前没有已运行实验、没有 raw result、没有性能数字，因此不存在“结果 claim 无法追溯”的即时问题；主要风险是 schema/接口设计还需要在 Stage 3.1 开始前收紧。

## Blocking Issues

无 Stage 3.1 blocking issue。

但 Stage 3.2 / GPU pilot 明确仍被阻塞：`refine-logs/PILOT_ENGINEERING_PLAN.md` 要求 split JSON、统一 evaluator、预算文档、raw logger、metric freeze、failed-run logging 和 Stage 3.1 后审查全部完成；`refine-logs/EXPERIMENT_TRACKER.md` 显示这些实现项目前均为 not started。

## Non-Blocking Issues

1. Raw result schema 追溯性不足：缺少 `run_command`、`split_file`、`result_file_path`、`evaluator_seed`、early-stopping 字段、配置 hash/snapshot，以及 evaluator/early-stopping 细节。
2. Metric schema 虽区分 label-free 与 label-audit，但两者在同一文件中同时要求，且 label-audit 包含 `validation_objective_ranking`，存在 post-validation 覆盖 frozen selector metric 的实现风险。
3. Split schema 要求 `class_distribution_test`，而 shared split file 又会传给每个方法；建议 shared split 中 test distribution 置 `null`，或拆为 auditor-only metadata。
4. Transductive / inductive 假设尚未显式声明。label-free metrics 使用全图结构/特征通常是 transductive node classification，不是 label leakage，但必须写入 manifest/raw schema，并保证所有方法同等可见。
5. Method fairness 基本合理，但 GraphMAE 风险最高：evaluator、decoder、budget mismatch 必须披露。Stage 3.1 可以实现，但 smoke 通过后不能直接上 GPU。

## Required Fixes Before Stage 3.1

- 补强 raw result schema/logger：加入 `run_command`、`split_file`、`config_hash` 或 config snapshot、`evaluator_seed`、early-stopping 字段、backbone/hidden_dim/budget 或可追溯 config 指纹。
- 把 frozen label-free metric artifact 和 post-eval label-audit artifact 分离，或硬编码 selector 只能读取 `label_free_regime_metrics` 且验证 freeze hash。
- 明确 `class_distribution_test` 策略：共享 split 文件中置空，或仅存 auditor-only 文件。
- 在 manifest/schema 中声明 `evaluation_setting: transductive|inductive` 和 graph visibility。
- Stage 3.1 只能做 scaffold/synthetic smoke，不下载数据、不训练、不跑 pilot。

## Whether Stage 3.1 Minimal Implementation Is Allowed

允许，范围仅限 minimal implementation / smoke-test scaffold。GPU deployment、真实 dataset pilot 和任何性能 claim 仍不允许。

## Post-Audit Local Fixes Applied In Stage 3.0

After the auditor returned `WARN`, the following schema/document fixes were applied within Stage 3.0:

- `schemas/raw_result_schema.json` now includes run command, split file, result file path, config hash, evaluator seed, early-stopping fields, backbone/budget fields, `evaluation_setting` and `graph_visibility`.
- `schemas/metric_schema.json` now separates `label_free_regime_metrics` and `label_audit_metrics` through `artifact_type`, `selector_visible` and `freeze_hash`.
- `docs/metric_interface_stage3.md` now requires separate label-free and label-audit artifacts.
- `docs/split_schema_explanation.md` now requires `class_distribution_test` to be `null` in shared split files passed to training/selector code.
- `refine-logs/PILOT_RUN_MANIFEST_DRAFT.yaml` now declares transductive evaluation and graph visibility.
- `refine-logs/PILOT_ENGINEERING_PLAN.md` now records these safeguards as Stage 3.1 engineering requirements.
