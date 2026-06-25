# Dataset Metadata Schema Explanation

Date: 2026-06-26

## Purpose

`schemas/dataset_metadata_schema.json` records loader, cache and controlled data-access metadata for Stage 3.1.5 / Stage 3.1.6 loader and split readiness checks.

## Rules

- Metadata is not an experiment result.
- Metadata must not contain accuracy, loss, embeddings, objective ranking or survival decisions.
- Metadata does not contain test label distribution.
- Metadata must not be used to choose an objective winner.
- Stage 3.1.6 allows `controlled_download`, but only for Cora / Wiki-CS / Actor through PyG official dataset loaders.
- `download_attempted=true` only means dataset download/read access was attempted. It is not training, evaluation, pilot execution or experimental evidence.
- Metadata must not contain accuracy, loss, performance tables, embeddings or objective-family ranking.
- Loader failure is not an experiment failure.
- Dataset availability is not pilot readiness.
- Stage 3.2 still requires independent approval.
- Outside explicit `controlled_download`, any data download requires explicit user approval.
- Loader status failure is not an experiment failure.
- `download_attempted` must default to `false`.

## Loader Status Values

- `available`: loader dependency and local cache are available, and metadata can be read without download.
- `missing_dependency`: required backend such as PyG/DGL is unavailable.
- `local_cache_missing`: backend is available but no local cache path exists.
- `download_required_not_approved`: loader would need a download; Stage 3.1.5 must stop for that dataset.
- `loader_error`: import/cache check raised an unexpected error without downloading.
- `fixed_split_unavailable`: dataset exists but required official/fixed split is unavailable.

## Path Convention

Future metadata files should be saved under:

```text
dataset_metadata/stage3_1_5/{dataset}.json
dataset_metadata/stage3_1_6/{dataset}.json
```

These files are loader/split smoke artifacts only, not raw results.

## Controlled Download Fields

- `data_access_mode`: `no_download` by default; `controlled_download` only for the authorized Stage 3.1.6 data access task.
- `cache_path`: local project cache path under `data/` or `datasets/`.
- `download_source`: for Stage 3.1.6 this must be PyG official dataset loader access, not hand-written URL download code.
