# Stage 3.1.6 Cora Fix Report

Date: 2026-06-26

## Scope

本次只修复 Cora data-access / split blocker。没有训练模型，没有运行 evaluator，没有运行 pilot，没有使用 GPU，没有克隆 baseline，没有生成 accuracy / loss / performance table。

## Fix

Cora 的 PyG Planetoid 默认端点 `https://github.com/kimiyoung/planetoid/raw/master/data` 反复触发 `FSTimeoutError`。修复方式是在 `src/gcl_diag/data/controlled_loaders.py` 中保留 `torch_geometric.datasets.Planetoid` 官方 loader，不手写下载器；仅当默认端点失败时，把 `Planetoid.url` 临时切换为同一官方 `kimiyoung/planetoid` 仓库的 raw endpoint：

```text
https://raw.githubusercontent.com/kimiyoung/planetoid/master/data
```

随后仍由 PyG Planetoid loader 执行下载、处理和读取。下载完成后再次运行 Stage 3.1.6 data/split scripts，Cora 从本地 PyG cache 正常读取。

## Result

- Cora metadata: `dataset_metadata/stage3_1_6/Cora.json`
- Cora split files:
  - `splits/Cora/split_seed_0.json`
  - `splits/Cora/split_seed_1.json`
  - `splits/Cora/split_seed_2.json`
- Split type: `custom_stratified_random_1_1_8`
- Counts per split: train 271 / val 271 / test 2166
- `class_distribution_test`: `null`

## Validation

All Stage 3.1.6 metadata and split files validate against project schemas and `split_io`.

## Boundary Flags

- Training run: no
- Evaluator run: no
- Pilot run: no
- GPU used: no
- Baseline repo cloned: no
- Accuracy/loss/performance table generated: no
- Non-target dataset downloaded: no

## Remaining Gate

Stage 3.2 planning / implementation approval may be considered. Stage 3.2 pilot run is still not allowed without separate approval.
