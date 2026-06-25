# Dataset Metadata Schema Explanation

Date: 2026-06-26

## Purpose

`schemas/dataset_metadata_schema.json` records loader and local-cache metadata for Stage 3.1.5 loader/split smoke.

## Rules

- Metadata is not an experiment result.
- Metadata must not contain accuracy, loss, embeddings, objective ranking or survival decisions.
- Metadata does not contain test label distribution.
- Metadata must not be used to choose an objective winner.
- Any data download requires explicit user approval.
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
```

These files are loader/split smoke artifacts only, not raw results.
