#!/usr/bin/env python
"""Run Stage 3.1.5 split generation/extraction smoke without training."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from gcl_diag.data.loader_probe import DATASET_PROBES
from gcl_diag.splits.generate_splits import build_custom_split_from_counts, can_generate_split, write_validated_split
from gcl_diag.splits.split_io import read_split


REPORT = ROOT / "refine-logs/STAGE3_1_5_SPLIT_REPORT.md"
METADATA_DIR = ROOT / "dataset_metadata/stage3_1_5"
SPLIT_ROOT = ROOT / "splits"
SEEDS = [0, 1, 2]


def main() -> int:
    metadata = _load_metadata()
    split_files_written: list[str] = []
    split_files_validated: list[str] = []
    blocked: list[str] = []
    block_reasons: dict[str, str] = {}

    for dataset in DATASET_PROBES:
        item = metadata.get(dataset)
        if item is None:
            blocked.append(dataset)
            block_reasons[dataset] = "metadata_missing"
            continue
        if not can_generate_split(item):
            blocked.append(dataset)
            block_reasons[dataset] = item.get("loader_status", "unknown")
            continue
        if not isinstance(item.get("num_nodes"), int):
            blocked.append(dataset)
            block_reasons[dataset] = "metadata_num_nodes_unavailable_without_instantiating_loader"
            continue
        if dataset == "Cora":
            blocked.append(dataset)
            block_reasons[dataset] = "stratified_split_generation_requires_labels_and_is_not_enabled_in_stage3_1_5"
        elif dataset == "Wiki-CS":
            blocked.append(dataset)
            block_reasons[dataset] = "official_split_extraction_not_implemented_in_stage3_1_5_without_instantiating_loader"
        elif dataset == "Actor":
            blocked.append(dataset)
            block_reasons[dataset] = "fixed_split_extraction_not_implemented_in_stage3_1_5_without_instantiating_loader"

    _write_report(metadata, split_files_written, split_files_validated, blocked, block_reasons)
    return 0


def _load_metadata() -> dict[str, dict]:
    data = {}
    for dataset in DATASET_PROBES:
        path = METADATA_DIR / f"{dataset}.json"
        if path.exists():
            data[dataset] = json.loads(path.read_text(encoding="utf-8"))
    return data


def _write_report(metadata, split_files_written, split_files_validated, blocked, block_reasons) -> None:
    lines = [
        "# Stage 3.1.5 Split Report",
        "",
        "Date: 2026-06-26",
        "",
        "## Datasets Checked",
        "",
        "| dataset | loader backend | local cache status | split action | block reason |",
        "| --- | --- | --- | --- | --- |",
    ]
    for dataset in DATASET_PROBES:
        item = metadata.get(dataset, {})
        cache_status = "present" if item.get("local_cache_used") else "missing_or_unused"
        split_action = "written" if any(path.startswith(f"splits/{dataset}/") for path in split_files_written) else "not_written"
        lines.append(
            f"| {dataset} | {item.get('loader_backend', 'unknown')} | {cache_status} | "
            f"{split_action} | {block_reasons.get(dataset, '')} |"
        )
    lines.extend(["", "## Metadata Files Written", ""])
    for dataset in metadata:
        lines.append(f"- `dataset_metadata/stage3_1_5/{dataset}.json`")
    lines.extend(["", "## Split Files Written", ""])
    lines.extend(f"- `{path}`" for path in split_files_written) if split_files_written else lines.append("- none")
    lines.extend(["", "## Split Files Validated", ""])
    lines.extend(f"- `{path}`" for path in split_files_validated) if split_files_validated else lines.append("- none")
    lines.extend(["", "## Blocked Datasets", ""])
    lines.extend(f"- {dataset}: {block_reasons.get(dataset, '')}" for dataset in blocked) if blocked else lines.append("- none")
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
            "- accuracy generated: no",
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
