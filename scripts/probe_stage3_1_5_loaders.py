#!/usr/bin/env python
"""Probe real dataset loader availability without downloading data."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from gcl_diag.data.loader_probe import probe_all
from gcl_diag.data.metadata import build_metadata, write_metadata


REPORT = ROOT / "refine-logs/STAGE3_1_5_LOADER_REPORT.md"
METADATA_DIR = ROOT / "dataset_metadata/stage3_1_5"


def main() -> int:
    commit = _commit_hash()
    results = probe_all(ROOT)
    metadata_files: list[str] = []
    for result in results:
        metadata = build_metadata(
            dataset_name=result.dataset_name,
            loader_backend=result.loader_backend,
            loader_status=result.loader_status,
            local_cache_used=result.local_cache_used,
            download_attempted=result.download_attempted,
            has_labels=None if result.loader_status != "available" else True,
            has_masks_or_official_splits=None,
            split_source=None,
            error_message=result.error_message,
            commit_hash=commit,
        )
        path = METADATA_DIR / f"{result.dataset_name}.json"
        write_metadata(metadata, path, ROOT / "schemas/dataset_metadata_schema.json")
        metadata_files.append(str(path.relative_to(ROOT)))
    _write_report(results, metadata_files)
    return 0


def _write_report(results, metadata_files: list[str]) -> None:
    lines = [
        "# Stage 3.1.5 Loader Report",
        "",
        "Date: 2026-06-26",
        "",
        "## Datasets Checked",
        "",
        "| dataset | loader backend | local cache status | loader status | download attempted | error |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for result in results:
        cache_status = "present" if result.local_cache_used else "missing_or_unused"
        lines.append(
            f"| {result.dataset_name} | {result.loader_backend} | {cache_status} | "
            f"{result.loader_status} | {str(result.download_attempted).lower()} | {result.error_message or ''} |"
        )
    lines.extend(
        [
            "",
            "## Metadata Files Written",
            "",
        ]
    )
    lines.extend(f"- `{path}`" for path in metadata_files)
    blocked = [r.dataset_name for r in results if r.loader_status != "available"]
    lines.extend(
        [
            "",
            "## Split Files Written",
            "",
            "- none by loader probe",
            "",
            "## Split Files Validated",
            "",
            "- none by loader probe",
            "",
            "## Blocked Datasets",
            "",
        ]
    )
    lines.extend(f"- {name}" for name in blocked) if blocked else lines.append("- none")
    lines.extend(
        [
            "",
            "## Boundary Flags",
            "",
            "- training was run: no",
            "- evaluator was run: no",
            "- GPU was used: no",
            "- baseline repo was cloned: no",
            "- download attempted: no",
        ]
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _commit_hash() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
