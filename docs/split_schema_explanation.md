# Split Schema Explanation

Date: 2026-06-25

## Purpose

`schemas/split_schema.json` defines the required JSON structure for every future pilot split file.

## Rules

- Pilot split 也必须保存，不能运行时临时随机 split 后不落盘。
- Official split 和 custom split 必须显式标注在 `split_type`。
- 所有方法必须共用同一 split 文件。
- Split 文件必须优先保存为 JSON。
- Test labels 不得用于 selector、调参、survival decision。
- Planetoid public split、custom random 1:1:8 split、Wiki-CS official split、heterophily fixed split 不得混入同一可比表。

## Required Path Convention

Future split files should use:

```text
splits/{dataset}/split_seed_{seed}.json
```

Stage 3.0 does not create actual split files.

## Field Notes

- `dataset_name`: canonical dataset name used by run manifests and raw results.
- `split_type`: must distinguish official fixed split, Wiki-CS official split, Planetoid public split, and custom random 1:1:8 split.
- `split_seed`: seed used to create or select the split. For official splits, record the official split id or mapped integer.
- `train_indices`, `val_indices`, `test_indices`: node indices only; no masks hidden in binary tensor files.
- `class_distribution_*`: may be `null` only if labels are unavailable at split creation time. If computed, labels must be train/validation/test membership labels only and must not affect selector design.
- `class_distribution_test`: must be `null` in the split schema. If test distribution is ever needed, it belongs in a separate auditor-only metadata file that is not read by training, selector, metric-freeze or survival-decision code.
- `commit_hash`: code commit that generated the split file.

## Integrity Checks Required Later

Stage 3.1 implementation should validate that:

- train, validation and test indices are disjoint;
- index counts match `num_train`, `num_val`, `num_test`;
- all indices are within `[0, num_nodes)`;
- every method reads the same split file path for the same dataset and seed.
