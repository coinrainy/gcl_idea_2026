#!/usr/bin/env python
"""Run Stage 3.1.6 controlled PyG dataset access without training."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from gcl_diag.data.controlled_loaders import DATASET_SPECS, load_controlled_dataset, metadata_fields
from gcl_diag.data.metadata import build_metadata, write_metadata


DATA_ACCESS_MODE = "controlled_download"
DATASETS = ["Cora", "Wiki-CS", "Actor"]
METADATA_DIR = ROOT / "dataset_metadata/stage3_1_6"
REPORT = ROOT / "refine-logs/STAGE3_1_6_DATA_ACCESS_REPORT.md"


def main() -> int:
    commit = _commit_hash()
    created_at = _now()
    results = []
    metadata_files = []

    for dataset_name in DATASETS:
        result = load_controlled_dataset(dataset_name, project_root=ROOT, data_access_mode=DATA_ACCESS_MODE)
        fields = metadata_fields(result)
        metadata = build_metadata(
            dataset_name=result.dataset_name,
            loader_backend=result.loader_backend,
            loader_status=result.loader_status,
            local_cache_used=result.local_cache_used,
            download_attempted=result.download_attempted,
            data_access_mode=DATA_ACCESS_MODE,
            cache_path=str(result.cache_path.relative_to(ROOT)) if result.cache_path.is_relative_to(ROOT) else str(result.cache_path),
            download_source=result.download_source,
            error_message=result.error_message,
            created_at=created_at,
            commit_hash=commit,
            **fields,
        )
        out = METADATA_DIR / f"{dataset_name}.json"
        write_metadata(metadata, out, ROOT / "schemas/dataset_metadata_schema.json")
        metadata_files.append(str(out.relative_to(ROOT)))
        results.append((result, metadata))

    _write_report(results, metadata_files)
    return 0


def _write_report(results, metadata_files: list[str]) -> None:
    lines = [
        "# Stage 3.1.6 Data Access Report",
        "",
        "Date: 2026-06-26",
        "Data access mode: `controlled_download`",
        "",
        "## Datasets Checked",
        "",
        "| dataset | loader backend | download attempted | download/read success | download source | local cache path | loader status | error |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for result, _ in results:
        success = "yes" if result.loader_status == "available" else "no"
        cache_path = str(result.cache_path.relative_to(ROOT)) if result.cache_path.is_relative_to(ROOT) else str(result.cache_path)
        lines.append(
            f"| {result.dataset_name} | {result.loader_backend} | yes | {success} | "
            f"{result.download_source} | {cache_path} | {result.loader_status} | {result.error_message or ''} |"
        )

    lines.extend(["", "## Metadata Files Written", ""])
    lines.extend(f"- `{path}`" for path in metadata_files)
    blocked = [result.dataset_name for result, _ in results if result.loader_status != "available"]
    lines.extend(["", "## Blocked Datasets", ""])
    lines.extend(f"- {name}" for name in blocked) if blocked else lines.append("- none")
    lines.extend(
        [
            "",
            "## Split Files Written",
            "",
            "- none by data access script",
            "",
            "## Split Files Validated",
            "",
            "- none by data access script",
            "",
            "## Boundary Flags",
            "",
            "- training was run: no",
            "- evaluator was run: no",
            "- GPU was used: no",
            "- baseline repo was cloned: no",
            "- accuracy/loss/performance table generated: no",
            "- downloaded datasets outside Cora/Wiki-CS/Actor: no",
            "- loader source: PyG official dataset loaders only",
        ]
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _commit_hash() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "unknown"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


if __name__ == "__main__":
    raise SystemExit(main())
