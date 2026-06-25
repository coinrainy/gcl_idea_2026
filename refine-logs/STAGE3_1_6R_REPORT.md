# Stage 3.1.6R Reconciliation Report

Date: 2026-06-26
Stage: Stage 3.1.6R Post-fix Auditor Reconciliation

## 1. Scope

本轮只做 post-fix auditor reconciliation，只检查已有 metadata 和 split JSON。没有下载数据，没有训练模型，没有运行 evaluator，没有运行 pilot，没有使用 GPU，没有克隆 baseline，没有生成 accuracy / loss / performance table，没有进入 Stage 3.2。

## 2. Why Stage 3.1.6R Was Needed

`refine-logs/STAGE3_1_6_REPORT.md` 已记录 Cora / Wiki-CS / Actor 均有 metadata 与 validated split JSON；但 `refine-logs/STAGE3_1_6_AUDITOR_REPORT.md` 仍保留修复前结论，写着 Cora 未生成实际 split 文件。本轮目标是重新核查当前 artifacts，并用 fresh auditor 解决这两个文档之间的不一致。

## 3. Metadata Recheck

Result: PASS.

Checked files:

- `dataset_metadata/stage3_1_6/Cora.json`
- `dataset_metadata/stage3_1_6/Wiki-CS.json`
- `dataset_metadata/stage3_1_6/Actor.json`

All metadata files validate against `schemas/dataset_metadata_schema.json`. All use approved dataset names, `data_access_mode=controlled_download`, `download_attempted=true`, `loader_status=available`, and `local_cache_used=true`. No forbidden fields were found: no accuracy, loss, performance table, objective ranking, test label distribution, or `class_distribution_test`.

## 4. Split Recheck

Result: PASS.

All nine split files exist, validate against `schemas/split_schema.json`, and pass `src/gcl_diag/splits/split_io.py::read_split` integrity checks.

| Dataset | Seeds | Split type | Status |
| --- | --- | --- | --- |
| Cora | 0, 1, 2 | `custom_stratified_random_1_1_8` | PASS |
| Wiki-CS | 0, 1, 2 | `official_wikics` | PASS |
| Actor | 0, 1, 2 | `heterophily_fixed` | PASS |

For every split, train / val / test indices are pairwise disjoint, counts match index-list lengths, indices are within `[0, num_nodes)`, and `class_distribution_test=null`.

## 5. Boundary Check

Result: PASS.

No `results/` files, raw experiment result files, training logs, evaluator outputs, GPU traces, baseline clone artifacts, accuracy/loss/performance tables, or pilot outputs were found. Text-search matches were limited to prohibition text, benchmark/docs text, literature notes, approved PyG dataset cache files, or existing scaffold/schema files.

## 6. Fresh Auditor Verdict

Fresh `gcl_experiment_auditor` verdict: WARN.

The auditor found no Stage 3.1.6R blocking issue. The WARN items are future-facing: old auditor report needs a correction note, split-protocol mixing remains a risk, seeds 0/1/2 are not formal coverage, and Stage 3.1.6R artifacts should be committed before any later GPU deployment.

## 7. Cora Inconsistency Resolution

Resolved.

The old Cora split-missing finding is superseded by Stage 3.1.6R. Current Cora artifacts are:

- `splits/Cora/split_seed_0.json`
- `splits/Cora/split_seed_1.json`
- `splits/Cora/split_seed_2.json`

All three Cora split files pass schema and integrity validation.

## 8. Blocking Issues

None for Stage 3.1.6R reconciliation.

## 9. Stage 3.2 Planning Permission

Allowed.

This only permits Stage 3.2 planning / implementation approval. It does not authorize training, evaluator runs, GPU usage, baseline cloning, pilot execution, result tables, or performance claims.

## 10. Direct Stage 3.2 Pilot Permission

Not allowed.

Direct Stage 3.2 pilot run remains blocked until a separate approval and run manifest exist.

## 11. Next Step Recommendation

Proceed only to Stage 3.2 planning / implementation approval if explicitly requested. Keep direct pilot execution blocked. Before any future run, preserve the warning that Cora custom, Wiki-CS official, and Actor fixed splits must not be placed into one directly comparable main table.

## Stage 3.1.6R Verdict

GO.

Rationale: metadata and split rechecks passed, fresh auditor no longer reports Cora split missing as a current artifact issue, boundary check found no out-of-scope training/evaluator/GPU/baseline/performance action, and Stage 3.2 planning is allowed while direct pilot execution remains blocked.
