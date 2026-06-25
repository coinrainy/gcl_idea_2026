# Stage 3.1 Scaffold Report

Date: 2026-06-26
Stage: Stage 3.1 Minimal Scaffold Implementation and Synthetic Smoke

## 1. Scope

本轮只实现最小工程脚手架和 synthetic smoke。没有下载真实数据集，没有训练 GRACE / BGRL / GraphMAE，没有运行 pilot，没有生成 performance claim，没有进入 Stage 3.2。

## 2. New Code Files

- `src/gcl_diag/io/schema_validate.py`
- `src/gcl_diag/splits/split_io.py`
- `src/gcl_diag/logging/raw_result_logger.py`
- `src/gcl_diag/metrics/artifacts.py`
- `src/gcl_diag/eval/frozen_linear.py`
- `src/gcl_diag/methods/base.py`
- `src/gcl_diag/methods/grace.py`
- `src/gcl_diag/methods/bgrl.py`
- `src/gcl_diag/methods/graphmae.py`
- `scripts/validate_artifacts.py`
- `scripts/run_stage3_1_synthetic_smoke.py`
- `tests/smoke/*.py`
- `tests/fixtures/synthetic_split.json`

## 3. New Config Files

- `configs/methods/grace.yaml`
- `configs/methods/bgrl.yaml`
- `configs/methods/graphmae.yaml`
- `configs/pilot_scaffold.yaml`

All configs are scaffold-only and point to `synthetic_only`.

## 4. Synthetic Smoke Result

Status: passed.

Command run:

```bash
python scripts/run_stage3_1_synthetic_smoke.py
```

Additional check:

```bash
python scripts/validate_artifacts.py --schema schemas/split_schema.json --json tests/fixtures/synthetic_split.json
```

`python -m pytest tests/smoke -q` was attempted but skipped because pytest is not installed. No dependency was installed.

## 5. Whether Real Data Was Accessed

No.

## 6. Whether Training Was Run

No.

## 7. Whether GPU Was Used

No.

## 8. Whether Baseline Was Cloned

No.

## 9. Schema Validator Status

Implemented. It uses the Python standard library and supports the schema subset needed by this project, including required fields, types, enum, const, oneOf, allOf, conditional metric artifact checks, array uniqueness and additional-property rejection.

## 10. Split Validator Status

Implemented. It checks:

- train / val / test disjointness;
- index counts;
- index range;
- explicit `split_type`;
- `class_distribution_test = null` for shared split files.

## 11. Raw Result Logger Status

Implemented. It writes synthetic success and fail records conforming to `schemas/raw_result_schema.json`. Fail records require non-empty `failure_reason` and set `test_at_best` / `final_test` to `null`.

## 12. Metric Artifact Separation Status

Implemented. Label-free metric artifacts are selector-visible and frozen with a non-empty `freeze_hash`. Label-audit artifacts are selector-invisible. `load_selector_metrics(path)` rejects label-audit artifacts.

## 13. Evaluator Dry-Run Status

Implemented. The evaluator runs only on synthetic embeddings and returns fields compatible with raw result schema: `best_epoch`, `valid_at_best`, `test_at_best`, `final_valid`, `final_test`.

## 14. Method Placeholders Status

Implemented. GRACE, BGRL and GraphMAE placeholders declare objective-family metadata. `build_model()`, `pretrain()` and `encode()` raise `NotImplementedError("Stage 3.1 scaffold only; real training is not implemented.")`.

## 15. Current Blocking Issues

For Stage 3.1 scaffold: none known after synthetic smoke.

For Stage 3.1.5: fresh auditor review returned `WARN` with no blocking issue after tracker wording cleanup.

For Stage 3.2 pilot: still blocked. Real dataset loader readiness, split generation smoke, unified evaluator review, and independent approval are still required.

## 16. Whether Next Stage Is Allowed

Allowed to request Stage 3.1.5 only, per fresh `gcl_experiment_auditor` verdict `WARN` with no Stage 3.1 blocking issue.

Stage 3.2 pilot run is not allowed.

## Stage 3.1 Verdict

GO.

This GO is limited to requesting Stage 3.1.5 real loader / split generation readiness. It is not approval for real pilot runs, GPU training, baseline cloning, performance tables, or formal claims.

## Auditor Verdict

Fresh `gcl_experiment_auditor` verdict: WARN.

Blocking issues for Stage 3.1 scaffold: none.

Stage 3.1.5 allowed: yes, limited to real loader / split generation smoke.

Stage 3.2 allowed: no, still blocked.
