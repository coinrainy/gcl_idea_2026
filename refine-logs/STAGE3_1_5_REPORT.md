# Stage 3.1.5 Report

Date: 2026-06-26
Stage: Stage 3.1.5 Real Loader and Split Generation Smoke

## 1. Scope

本轮只做 real loader / split generation / non-training smoke。没有自动下载数据集，没有训练模型，没有运行 evaluator，没有使用 GPU，没有克隆 baseline，没有运行 pilot，没有生成 accuracy，没有做 objective-family ranking。

## 2. Environment Dependency Check

Commands run:

```bash
which python || true
python --version || true
python - <<'PY'
import importlib.util
for pkg in ["torch", "torch_geometric", "dgl", "numpy", "sklearn"]:
    print(pkg, "FOUND" if importlib.util.find_spec(pkg) else "MISSING")
PY
python scripts/probe_stage3_1_5_loaders.py
python scripts/run_stage3_1_5_split_smoke.py
for f in dataset_metadata/stage3_1_5/*.json; do python scripts/validate_artifacts.py --schema schemas/dataset_metadata_schema.json --json "$f"; done
python -m json.tool schemas/split_schema.json >/dev/null
python -m json.tool schemas/dataset_metadata_schema.json >/dev/null
python -m compileall -q src scripts tests
git diff --check
find splits results -maxdepth 5 -type f 2>/dev/null | sort
pytest -q tests/smoke/test_loader_probe_no_download.py tests/smoke/test_dataset_metadata.py tests/smoke/test_split_generation_synthetic_and_mock.py
```

`pytest` was not available in the current environment (`pytest: command not found`), so no pytest test suite was executed and no dependency was installed. `compileall`, JSON schema syntax checks, artifact validation and `git diff --check` passed. The `find splits results ...` check returned no files.

| Dependency | Status |
| --- | --- |
| Python | `/root/miniconda3/bin/python`, `Python 3.10.8` |
| torch | FOUND |
| torch_geometric | FOUND |
| dgl | FOUND |
| numpy | FOUND |
| sklearn | FOUND |

No dependency was installed.

## 3. Loader Probe Results

| Dataset | Backend | Loader status | Local cache | Download attempted |
| --- | --- | --- | --- | --- |
| Cora | pyg_planetoid | download_required_not_approved | missing | no |
| Wiki-CS | pyg_wikics | download_required_not_approved | missing | no |
| Actor | pyg_actor | download_required_not_approved | missing | no |

PyG and DGL are installed, but the required local dataset caches were not found at the checked project-local paths. The scripts stopped at cache check and did not instantiate loaders in a way that would download data.

## 4. Dataset Metadata Results

Metadata files written and schema-validated:

- `dataset_metadata/stage3_1_5/Cora.json`
- `dataset_metadata/stage3_1_5/Wiki-CS.json`
- `dataset_metadata/stage3_1_5/Actor.json`

The metadata files contain loader/cache status only. They contain no test label distribution, accuracy, loss, embedding, objective ranking, training result or survival decision.

## 5. Split Generation / Extraction Results

No split JSON files were written.

Reason: all three target datasets require download or pre-populated local cache. Download was not approved, so split generation/extraction was blocked.

## 6. Datasets Available

None.

## 7. Datasets Blocked

- Cora: `download_required_not_approved`
- Wiki-CS: `download_required_not_approved`
- Actor: `download_required_not_approved`

## 8. Whether Any Download Occurred

No. `download_attempted=false` for all metadata files.

## 9. Whether Any Model Was Trained

No.

## 10. Whether Evaluator Was Run

No.

## 11. Whether GPU Was Used

No.

## 12. Whether Baseline Was Cloned

No.

## 13. Whether Any Accuracy Was Generated

No.

## 14. Current Blocking Issues

- No target dataset local cache is available.
- No true split JSON can be generated or extracted without approved data access.
- Cora custom stratified 1:1:8 split generation is intentionally disabled until labels can be safely read from an approved local cache.
- Stage 3.2 planning cannot proceed because the GO criterion requires at least two datasets with loader metadata and validated split JSON.

## 15. Whether Stage 3.2 Is Allowed

No. Stage 3.2 pilot run is not allowed.

Stage 3.2 planning is also not allowed from the current state because zero datasets produced validated split JSON.

## 16. Next Step Recommendation

Choose one explicit data-access route:

- approve controlled dataset download for Cora, Wiki-CS and Actor; or
- provide local caches under the checked paths; or
- specify alternative local cache paths to probe.

After local data is available, rerun Stage 3.1.5 loader/split smoke. Do not train or run pilot until a later independent review approves Stage 3.2 planning and then Stage 3.2 execution.

## Stage 3.1.5 Verdict

BLOCKED.

This block is due to missing local dataset caches and unapproved downloads, not due to model failure or experimental results.
