# Stage 3.0 Readiness Report

Date: 2026-06-26
Stage: Stage 3.0 Pilot Readiness / engineering feasibility review

## 1. Scope

本轮只做 pilot readiness，不运行实验、不运行 smoke test、不下载数据集、不克隆 baseline、不实现训练代码、不进入 Stage 3.1、不进入 Stage 3.2、不写论文。

Active idea remains `GCL-I03`; `GCL-I02` remains auxiliary negative-validity audit / fallback.

## 2. Generated Schemas

- `schemas/split_schema.json`
- `schemas/raw_result_schema.json`
- `schemas/metric_schema.json`

Explanations:

- `docs/split_schema_explanation.md`
- `docs/raw_result_schema_explanation.md`
- `docs/metric_interface_stage3.md`

Post-audit fixes were applied to improve traceability, metric artifact separation, test-distribution handling and transductive graph-visibility declaration.

## 3. Dataset Selection

Stage 3.1 minimal feasibility set:

| Dataset | Regime | Role |
| --- | --- | --- |
| Cora | homophilic citation | basic engineering sanity |
| Wiki-CS | non-Planetoid homophilic/wiki | check signal beyond citation graphs |
| Actor | heterophilic | objective-family boundary check |

Fallbacks: PubMed, Coauthor-CS, Chameleon.

No dataset has been downloaded.

## 4. Method Selection

Stage 3.1 minimal objective-family set:

| Method | Family | Role |
| --- | --- | --- |
| GRACE | negative-based contrastive | contrastive baseline |
| BGRL | bootstrap / negative-free | negative-free objective family |
| GraphMAE | masked graph modeling | MGM objective family |

Fallbacks: GCA, AFGRL, GraphMAE2. ProGCL remains I02 audit reference only and is not a core Stage 3.1 method.

No baseline repository has been cloned and no method code has been implemented.

## 5. Pilot Manifest Status

`refine-logs/PILOT_RUN_MANIFEST_DRAFT.yaml` is draft-only and explicitly not executable. It declares:

- status: `draft_only`;
- seeds: `[0, 1, 2]`;
- output directories for future raw results, summaries and metrics;
- rules: no test-label tuning, save failed runs, pilot only, no SOTA/formal claim;
- evaluation setting: `transductive`;
- graph visibility: identical graph structure/features for all methods.

## 6. Metric Leakage Boundary

Selector-visible metrics must be label-free and frozen before validation outcome:

- artifact type: `label_free_regime_metrics`;
- `selector_visible: true`;
- `metric_freeze_status: frozen_before_validation_outcome`;
- `freeze_hash` required.

Label-audit metrics must be saved separately:

- artifact type: `label_audit_metrics`;
- `selector_visible: false`;
- cannot overwrite frozen label-free artifacts.

Prohibited metrics include test label homophily, test feature-label predictability, test objective ranking and any metric computed after looking at test accuracy for survival decisions.

## 7. Raw Result Logging Plan

Future raw result JSON must include:

- `run_command`;
- `split_file`;
- `result_file_path`;
- `config_path` and `config_hash`;
- `commit_hash`;
- evaluator seed and early-stopping fields;
- backbone/budget fields;
- `evaluation_setting` and `graph_visibility`;
- failure records for failed runs.

Summary tables must be generated from raw JSON and cannot manually copy best numbers.

## 8. Auditor Verdict

Auditor verdict: WARN.

The fresh `gcl_experiment_auditor` found no Stage 3.1 blocking issue and allowed Stage 3.1 minimal implementation / smoke-test scaffold. It warned that Stage 3.2 / GPU pilot remains blocked until actual split JSONs, unified evaluator, budget documentation, raw logger, metric freeze, failed-run logging and post-Stage-3.1 audit are complete.

## 9. Blocking Issues

For Stage 3.1 minimal implementation / smoke-test scaffold: none after post-audit schema/document fixes.

For Stage 3.2 pilot: blocked until Stage 3.1 produces and validates implementation artifacts.

## 10. Non-Blocking Issues

- GraphMAE remains the highest engineering fairness risk because decoder/evaluator/budget settings can differ from GCL methods.
- Stage 3.1 must keep smoke tests synthetic or scaffold-level unless explicitly approved later.
- Real dataset pilot, GPU training and performance claims remain forbidden.
- Official split versus custom split handling must remain explicit per dataset.

## 11. Whether Stage 3.1 Minimal Implementation / Smoke Test Is Allowed

Allowed: yes, but only Stage 3.1 minimal implementation / smoke-test scaffold.

Not allowed:

- Stage 3.2 pilot run;
- GPU experiment;
- dataset download unless separately approved by the next stage request;
- baseline repository clone unless separately approved;
- formal experiment;
- performance claim;
- paper writing.

## 12. Fix Tasks If Revisiting Before Stage 3.1

No blocking fixes remain for Stage 3.1 after this report. Recommended checks at Stage 3.1 start:

- implement schema validators first;
- create synthetic fixtures before touching real datasets;
- ensure shared split files expose no test-label distribution to training/selector code;
- enforce metric artifact separation and `freeze_hash`;
- make evaluator and budget fields mandatory in logger tests.

## Stage 3.0 Verdict

GO.

This GO is limited to Stage 3.1 minimal implementation / smoke-test scaffold. It is not approval for Stage 3.2 pilot or any experiment run.
