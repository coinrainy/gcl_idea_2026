# Stage 3.1.5 Loader Report

Date: 2026-06-26

## Datasets Checked

| dataset | loader backend | local cache status | loader status | download attempted | error |
| --- | --- | --- | --- | --- | --- |
| Cora | pyg_planetoid | missing_or_unused | download_required_not_approved | false | local cache missing at candidates ['/root/autodl-tmp/gcl_idea_2026/data/Planetoid/Cora', '/root/autodl-tmp/gcl_idea_2026/data/Cora', '/root/autodl-tmp/gcl_idea_2026/datasets/Planetoid/Cora', '/root/autodl-tmp/gcl_idea_2026/datasets/Cora']; download not approved |
| Wiki-CS | pyg_wikics | missing_or_unused | download_required_not_approved | false | local cache missing at candidates ['/root/autodl-tmp/gcl_idea_2026/data/WikiCS', '/root/autodl-tmp/gcl_idea_2026/data/Wiki-CS', '/root/autodl-tmp/gcl_idea_2026/datasets/WikiCS', '/root/autodl-tmp/gcl_idea_2026/datasets/Wiki-CS']; download not approved |
| Actor | pyg_actor | missing_or_unused | download_required_not_approved | false | local cache missing at candidates ['/root/autodl-tmp/gcl_idea_2026/data/Actor', '/root/autodl-tmp/gcl_idea_2026/datasets/Actor']; download not approved |

## Metadata Files Written

- `dataset_metadata/stage3_1_5/Cora.json`
- `dataset_metadata/stage3_1_5/Wiki-CS.json`
- `dataset_metadata/stage3_1_5/Actor.json`

## Split Files Written

- none by loader probe

## Split Files Validated

- none by loader probe

## Blocked Datasets

- Cora
- Wiki-CS
- Actor

## Boundary Flags

- training was run: no
- evaluator was run: no
- GPU was used: no
- baseline repo was cloned: no
- download attempted: no
