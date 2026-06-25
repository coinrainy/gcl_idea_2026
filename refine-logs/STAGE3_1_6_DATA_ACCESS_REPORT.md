# Stage 3.1.6 Data Access Report

Date: 2026-06-26
Data access mode: `controlled_download`

## Datasets Checked

| dataset | loader backend | download attempted | download/read success | download source | local cache path | loader status | error |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cora | pyg_planetoid | yes | yes | pyg_official_loader_cache_reread_after_raw_github_endpoint_fallback | data/Planetoid | available |  |
| Wiki-CS | pyg_wikics | yes | yes | pyg_official_loader | data/WikiCS | available |  |
| Actor | pyg_actor | yes | yes | pyg_official_loader | data/Actor | available |  |

## Metadata Files Written

- `dataset_metadata/stage3_1_6/Cora.json`
- `dataset_metadata/stage3_1_6/Wiki-CS.json`
- `dataset_metadata/stage3_1_6/Actor.json`

## Blocked Datasets

- none

## Split Files Written

- none by data access script

## Split Files Validated

- none by data access script

## Boundary Flags

- training was run: no
- evaluator was run: no
- GPU was used: no
- baseline repo was cloned: no
- accuracy/loss/performance table generated: no
- downloaded datasets outside Cora/Wiki-CS/Actor: no
- loader source: PyG official dataset loaders only

## Cora Provenance Note

Cora initially triggered the PyG Planetoid fallback path because the default `github.com/.../raw/...` endpoint timed out. The fallback still used `torch_geometric.datasets.Planetoid`, with `Planetoid.url` temporarily set to the same official `kimiyoung/planetoid` repository through `raw.githubusercontent.com`. The final metadata regeneration read the local PyG cache produced by that fallback, so the Cora metadata records `pyg_official_loader_cache_reread_after_raw_github_endpoint_fallback`.
