# Stage 3.1.6 Report

Date: 2026-06-26
Stage: Stage 3.1.6 Controlled Dataset Access Resolution

## 1. Scope

本轮只解决 controlled dataset access、dataset metadata、split JSON 生成与校验。没有训练模型，没有运行 evaluator，没有运行 pilot，没有使用 GPU，没有克隆 baseline，没有生成 accuracy / loss / performance table，没有做 objective-family ranking，没有进入 Stage 3.2。

## 2. Data Access Mode

`DATA_ACCESS_MODE=controlled_download`

仅允许通过 PyG 官方 dataset loader 访问 Cora / Wiki-CS / Actor。没有手写任意下载脚本，没有下载非目标数据集，没有安装新依赖。Cora 修复时仍使用 `torch_geometric.datasets.Planetoid`，在 PyG 默认 `github.com/.../raw/...` 端点超时后，将同一 PyG loader 的 `Planetoid.url` 切换到同一官方 `kimiyoung/planetoid` 仓库的 `raw.githubusercontent.com` 端点完成下载。Actor 的 PyG 官方 loader 内部使用 Film/Actor 源文件，这是 approved Actor loader 的正常数据源路径，不是额外 baseline 或无关数据集下载。

## 3. Dataset Access Results

| Dataset | Backend | Download attempted | Download/read success | Status | Cache path |
| --- | --- | --- | --- | --- | --- |
| Cora | `pyg_planetoid` | yes | yes | `available` | `data/Planetoid` |
| Wiki-CS | `pyg_wikics` | yes | yes | `available` | `data/WikiCS` |
| Actor | `pyg_actor` | yes | yes | `available` | `data/Actor` |

## 4. Metadata Files

- `dataset_metadata/stage3_1_6/Cora.json`
- `dataset_metadata/stage3_1_6/Wiki-CS.json`
- `dataset_metadata/stage3_1_6/Actor.json`

All metadata files validate against `schemas/dataset_metadata_schema.json`. Metadata contains no test label distribution, accuracy, loss, performance table, embedding, objective ranking or survival decision.

## 5. Split Files

| Dataset | Split type | Split files | Validation |
| --- | --- | --- | --- |
| Cora | `custom_stratified_random_1_1_8` | `splits/Cora/split_seed_0.json`, `splits/Cora/split_seed_1.json`, `splits/Cora/split_seed_2.json` | passed |
| Wiki-CS | `official_wikics` | `splits/Wiki-CS/split_seed_0.json`, `splits/Wiki-CS/split_seed_1.json`, `splits/Wiki-CS/split_seed_2.json` | passed |
| Actor | `heterophily_fixed` | `splits/Actor/split_seed_0.json`, `splits/Actor/split_seed_1.json`, `splits/Actor/split_seed_2.json` | passed |

All written split files validate against `schemas/split_schema.json` and `src/gcl_diag/splits/split_io.py`. In every written split file, `class_distribution_test` is `null`.

## 6. Boundary Checks

- Model training run: no
- Evaluator run: no
- Pilot run: no
- GPU used: no
- Baseline repo cloned: no
- Accuracy generated: no
- Loss generated: no
- Performance table generated: no
- Objective-family ranking: no
- Test label distribution stored: no

## 7. Commands Run

```bash
python scripts/run_stage3_1_6_controlled_data_access.py
python scripts/run_stage3_1_6_split_generation.py
for f in dataset_metadata/stage3_1_6/*.json; do python scripts/validate_artifacts.py --schema schemas/dataset_metadata_schema.json --json "$f"; done
for f in splits/*/split_seed_*.json; do python scripts/validate_artifacts.py --schema schemas/split_schema.json --json "$f"; done
```

No `train.py`, `run_experiment.py`, evaluator, GPU command, baseline clone, pip install or conda install command was run.

## 8. Current Blocking Issues

- No dataset-access blocker remains for Cora / Wiki-CS / Actor metadata and split JSON generation.
- Stage 3.2 pilot execution is still blocked until a separate approval.
- Protocol warning: Stage 3.2 execution must not mix Cora custom, Wiki-CS official and Actor fixed splits in one directly comparable main table.

## 9. Stage 3.2 Permission

Stage 3.2 planning / implementation approval: allowed.

Stage 3.2 pilot run: not allowed.

This GO does not authorize training, evaluator runs, GPU usage, baseline cloning, pilot execution or performance claims.

## 10. Next Step Recommendation

Proceed only to Stage 3.2 planning / implementation approval review. Do not run pilot until a later independent review approves Stage 3.2 execution.

## Stage 3.1.6 Verdict

GO.

Rationale: all three target datasets, Cora / Wiki-CS / Actor, completed metadata + validated split JSON, and no out-of-scope training/evaluator/GPU/baseline/performance action occurred.

## Auditor Verdict

Fresh `gcl_experiment_auditor` verdict: WARN.

Stage 3.2 planning is allowed. Stage 3.2 pilot run is not allowed.

## Stage 3.1.6R Reconciliation Note

Stage 3.1.6R post-fix auditor reconciliation supersedes the older Cora split-missing auditor finding for current artifact status.

Current reconciled status:

- `dataset_metadata/stage3_1_6/Cora.json`, `dataset_metadata/stage3_1_6/Wiki-CS.json`, and `dataset_metadata/stage3_1_6/Actor.json` validate successfully.
- `splits/Cora/split_seed_{0,1,2}.json`, `splits/Wiki-CS/split_seed_{0,1,2}.json`, and `splits/Actor/split_seed_{0,1,2}.json` exist and validate successfully.
- Fresh Stage 3.1.6R `gcl_experiment_auditor` verdict: WARN, with no reconciliation blocking issue.
- Previous Cora inconsistency: resolved.
- Stage 3.2 planning / implementation approval: allowed.
- Direct Stage 3.2 pilot run: blocked.
