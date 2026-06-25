# Stage 3.1.6 Split Report

Date: 2026-06-26

## Datasets Checked

| dataset | loader backend | split action | block reason |
| --- | --- | --- | --- |
| Cora | pyg_planetoid | written |  |
| Wiki-CS | pyg_wikics | written |  |
| Actor | pyg_actor | written |  |

## Split Files Written

- `splits/Cora/split_seed_0.json`
- `splits/Cora/split_seed_1.json`
- `splits/Cora/split_seed_2.json`
- `splits/Wiki-CS/split_seed_0.json`
- `splits/Wiki-CS/split_seed_1.json`
- `splits/Wiki-CS/split_seed_2.json`
- `splits/Actor/split_seed_0.json`
- `splits/Actor/split_seed_1.json`
- `splits/Actor/split_seed_2.json`

## Split Files Validated

- `splits/Cora/split_seed_0.json`
- `splits/Cora/split_seed_1.json`
- `splits/Cora/split_seed_2.json`
- `splits/Wiki-CS/split_seed_0.json`
- `splits/Wiki-CS/split_seed_1.json`
- `splits/Wiki-CS/split_seed_2.json`
- `splits/Actor/split_seed_0.json`
- `splits/Actor/split_seed_1.json`
- `splits/Actor/split_seed_2.json`

## Blocked Datasets

- none

## Split Types

- Cora: `custom_stratified_random_1_1_8` if available
- Wiki-CS: `official_wikics` if official masks are readable
- Actor: `heterophily_fixed` if fixed masks are readable

## Boundary Flags

- training was run: no
- evaluator was run: no
- GPU was used: no
- baseline repo was cloned: no
- accuracy/loss/performance table generated: no
- class_distribution_test written: null only
