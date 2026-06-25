# Stage 3.2P Data / Split Readiness

Date: 2026-06-26
Stage: Stage 3.2P Pilot Planning / Implementation Approval

## Commands

```bash
for f in dataset_metadata/stage3_1_6/*.json; do
  python scripts/validate_artifacts.py --schema schemas/dataset_metadata_schema.json --json "$f"
done

for f in splits/Cora/split_seed_*.json splits/Wiki-CS/split_seed_*.json splits/Actor/split_seed_*.json; do
  python scripts/validate_artifacts.py --schema schemas/split_schema.json --json "$f"
done
```

Each split was also read with `src/gcl_diag/splits/split_io.py::read_split`.

## Metadata Readiness

| Dataset | Metadata file | Exists | Schema validation | Loader status |
| --- | --- | --- | --- | --- |
| Cora | `dataset_metadata/stage3_1_6/Cora.json` | yes | PASS | available |
| Wiki-CS | `dataset_metadata/stage3_1_6/Wiki-CS.json` | yes | PASS | available |
| Actor | `dataset_metadata/stage3_1_6/Actor.json` | yes | PASS | available |

## Split Readiness

| Dataset | Seed | Split file | Exists | Schema validation | read_split integrity | split_type | class_distribution_test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cora | 0 | `splits/Cora/split_seed_0.json` | yes | PASS | PASS | `custom_stratified_random_1_1_8` | null |
| Cora | 1 | `splits/Cora/split_seed_1.json` | yes | PASS | PASS | `custom_stratified_random_1_1_8` | null |
| Cora | 2 | `splits/Cora/split_seed_2.json` | yes | PASS | PASS | `custom_stratified_random_1_1_8` | null |
| Wiki-CS | 0 | `splits/Wiki-CS/split_seed_0.json` | yes | PASS | PASS | `official_wikics` | null |
| Wiki-CS | 1 | `splits/Wiki-CS/split_seed_1.json` | yes | PASS | PASS | `official_wikics` | null |
| Wiki-CS | 2 | `splits/Wiki-CS/split_seed_2.json` | yes | PASS | PASS | `official_wikics` | null |
| Actor | 0 | `splits/Actor/split_seed_0.json` | yes | PASS | PASS | `heterophily_fixed` | null |
| Actor | 1 | `splits/Actor/split_seed_1.json` | yes | PASS | PASS | `heterophily_fixed` | null |
| Actor | 2 | `splits/Actor/split_seed_2.json` | yes | PASS | PASS | `heterophily_fixed` | null |

## Split Protocol Warning

Cora / Wiki-CS / Actor use different split protocols:

- Cora: custom stratified random 1:1:8.
- Wiki-CS: official Wiki-CS splits.
- Actor: heterophily fixed splits.

Future results can compare GRACE / BGRL / GraphMAE within each dataset under that dataset's fixed split files. They must not put Cora custom, Wiki-CS official, and Actor fixed results into one directly comparable main table to claim unified SOTA or a cross-dataset winner.

## Verdict

PASS.

No metadata or split blocker was found for Stage 3.2P planning. This readiness does not authorize Stage 3.2 execution.
