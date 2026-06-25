# Stage 3.1.6R Split Recheck

Date: 2026-06-26
Stage: Stage 3.1.6R Post-fix Auditor Reconciliation

## Schema Validation Command

```bash
for f in splits/Cora/split_seed_*.json splits/Wiki-CS/split_seed_*.json splits/Actor/split_seed_*.json; do
  python scripts/validate_artifacts.py --schema schemas/split_schema.json --json "$f"
done
```

## Integrity Validation

Each split file was also read with `src/gcl_diag/splits/split_io.py::read_split`, which validates schema and checks:

- explicit `split_type`;
- `class_distribution_test=null`;
- `num_train`, `num_val`, `num_test` match index counts;
- train / val / test are pairwise disjoint;
- every index is in `[0, num_nodes)`.

## Split Files Checked

| file | exists | schema validation | read_split integrity | split_type | seed | counts match | disjoint | indices in range | class_distribution_test |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `splits/Cora/split_seed_0.json` | yes | PASS | PASS | custom_stratified_random_1_1_8 | 0 | yes | yes | yes | null |
| `splits/Cora/split_seed_1.json` | yes | PASS | PASS | custom_stratified_random_1_1_8 | 1 | yes | yes | yes | null |
| `splits/Cora/split_seed_2.json` | yes | PASS | PASS | custom_stratified_random_1_1_8 | 2 | yes | yes | yes | null |
| `splits/Wiki-CS/split_seed_0.json` | yes | PASS | PASS | official_wikics | 0 | yes | yes | yes | null |
| `splits/Wiki-CS/split_seed_1.json` | yes | PASS | PASS | official_wikics | 1 | yes | yes | yes | null |
| `splits/Wiki-CS/split_seed_2.json` | yes | PASS | PASS | official_wikics | 2 | yes | yes | yes | null |
| `splits/Actor/split_seed_0.json` | yes | PASS | PASS | heterophily_fixed | 0 | yes | yes | yes | null |
| `splits/Actor/split_seed_1.json` | yes | PASS | PASS | heterophily_fixed | 1 | yes | yes | yes | null |
| `splits/Actor/split_seed_2.json` | yes | PASS | PASS | heterophily_fixed | 2 | yes | yes | yes | null |

## Split Files Missing

None.

## Split Type Summary

- Cora: `custom_stratified_random_1_1_8`.
- Wiki-CS: `official_wikics`.
- Actor: `heterophily_fixed`.

## Seed Coverage

- Cora: seeds 0, 1, 2 present and validated.
- Wiki-CS: seeds 0, 1, 2 present and validated.
- Actor: seeds 0, 1, 2 present and validated.

## Verdict

PASS.

Rationale: all nine split files exist, pass schema validation, pass `read_split` integrity validation, have expected split types, cover seeds 0/1/2 for all three datasets, and keep `class_distribution_test=null`.
