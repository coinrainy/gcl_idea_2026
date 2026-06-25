# Stage 3.1.6 Data Access Report

Date: 2026-06-26
Data access mode: `controlled_download`

## Datasets Checked

| dataset | loader backend | download attempted | download/read success | local cache path | loader status | error |
| --- | --- | --- | --- | --- | --- | --- |
| Cora | pyg_planetoid | yes | no | data/Planetoid | loader_error | FSTimeoutError: FSTimeoutError() |
| Wiki-CS | pyg_wikics | yes | yes | data/WikiCS | available |  |
| Actor | pyg_actor | yes | yes | data/Actor | available |  |

## Metadata Files Written

- `dataset_metadata/stage3_1_6/Cora.json`
- `dataset_metadata/stage3_1_6/Wiki-CS.json`
- `dataset_metadata/stage3_1_6/Actor.json`

## Blocked Datasets

- Cora

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
