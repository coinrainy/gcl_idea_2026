# Stage 3.1.6R Metadata Recheck

Date: 2026-06-26
Stage: Stage 3.1.6R Post-fix Auditor Reconciliation

## Command

```bash
for f in dataset_metadata/stage3_1_6/*.json; do
  python scripts/validate_artifacts.py --schema schemas/dataset_metadata_schema.json --json "$f"
done
```

## Metadata Files Checked

| file | dataset_name | schema validation | data_access_mode | download_attempted | loader_status | local_cache_used | cache_path | forbidden fields found |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `dataset_metadata/stage3_1_6/Actor.json` | Actor | PASS | controlled_download | true | available | true | `data/Actor` | none |
| `dataset_metadata/stage3_1_6/Cora.json` | Cora | PASS | controlled_download | true | available | true | `data/Planetoid` | none |
| `dataset_metadata/stage3_1_6/Wiki-CS.json` | Wiki-CS | PASS | controlled_download | true | available | true | `data/WikiCS` | none |

## Forbidden Field Check

Checked fields:

- `accuracy`
- `loss`
- `performance`
- `performance_table`
- `objective_ranking`
- `test_label_distribution`
- `class_distribution_test`

No checked metadata file contains forbidden performance, objective-ranking, or test-label-distribution fields.

## Verdict

PASS.

Rationale: all three metadata files validate against `schemas/dataset_metadata_schema.json`, use only the approved dataset names Cora / Wiki-CS / Actor, record `data_access_mode=controlled_download`, `download_attempted=true`, `loader_status=available`, `local_cache_used=true`, and contain no forbidden result or test-distribution fields.
