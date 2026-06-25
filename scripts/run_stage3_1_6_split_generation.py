#!/usr/bin/env python
"""Generate or extract Stage 3.1.6 split JSON files without training."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from gcl_diag.data.controlled_loaders import load_controlled_dataset
from gcl_diag.splits.generate_splits import build_split_from_masks, build_stratified_random_1_1_8_split, write_validated_split
from gcl_diag.splits.split_io import read_split


DATA_ACCESS_MODE = "controlled_download"
DATASETS = ["Cora", "Wiki-CS", "Actor"]
SEEDS = [0, 1, 2]
SPLIT_ROOT = ROOT / "splits"
REPORT = ROOT / "refine-logs/STAGE3_1_6_SPLIT_REPORT.md"


def main() -> int:
    commit = _commit_hash()
    created_at = _now()
    rows: list[dict[str, str]] = []
    split_files_written: list[str] = []
    split_files_validated: list[str] = []
    blocked: dict[str, str] = {}

    for dataset_name in DATASETS:
        result = load_controlled_dataset(dataset_name, project_root=ROOT, data_access_mode=DATA_ACCESS_MODE)
        if result.loader_status != "available" or result.data is None:
            blocked[dataset_name] = result.error_message or result.loader_status
            rows.append(_row(dataset_name, result.loader_backend, "not_written", blocked[dataset_name]))
            continue
        try:
            written, validated = _write_dataset_splits(dataset_name, result.data, created_at, commit)
        except Exception as exc:  # noqa: BLE001 - report dataset-specific split blocker.
            blocked[dataset_name] = str(exc)
            rows.append(_row(dataset_name, result.loader_backend, "not_written", str(exc)))
            continue
        split_files_written.extend(written)
        split_files_validated.extend(validated)
        rows.append(_row(dataset_name, result.loader_backend, "written", ""))

    _write_report(rows, split_files_written, split_files_validated, blocked)
    return 0


def _write_dataset_splits(dataset_name: str, data, created_at: str, commit: str) -> tuple[list[str], list[str]]:
    written: list[str] = []
    validated: list[str] = []
    for seed in SEEDS:
        if dataset_name == "Cora":
            split = build_stratified_random_1_1_8_split(
                dataset_name="Cora",
                labels=data.y,
                split_seed=seed,
                created_by="stage3_1_6_controlled_split_generation",
                created_at=created_at,
                commit_hash=commit,
            )
        elif dataset_name == "Wiki-CS":
            split = build_split_from_masks(
                dataset_name="Wiki-CS",
                split_type="official_wikics",
                split_seed=seed,
                train_mask=getattr(data, "train_mask", None),
                val_mask=getattr(data, "val_mask", None),
                test_mask=getattr(data, "test_mask", None),
                labels=getattr(data, "y", None),
                created_by="stage3_1_6_controlled_split_generation",
                created_at=created_at,
                commit_hash=commit,
            )
        elif dataset_name == "Actor":
            split = build_split_from_masks(
                dataset_name="Actor",
                split_type="heterophily_fixed",
                split_seed=seed,
                train_mask=getattr(data, "train_mask", None),
                val_mask=getattr(data, "val_mask", None),
                test_mask=getattr(data, "test_mask", None),
                labels=getattr(data, "y", None),
                created_by="stage3_1_6_controlled_split_generation",
                created_at=created_at,
                commit_hash=commit,
            )
        else:
            raise ValueError(f"unsupported dataset: {dataset_name}")

        out = SPLIT_ROOT / dataset_name / f"split_seed_{seed}.json"
        write_validated_split(split, out, ROOT / "schemas/split_schema.json")
        read_split(out, ROOT / "schemas/split_schema.json")
        rel = str(out.relative_to(ROOT))
        written.append(rel)
        validated.append(rel)
    return written, validated


def _row(dataset: str, backend: str, action: str, block_reason: str) -> dict[str, str]:
    return {
        "dataset": dataset,
        "loader_backend": backend,
        "split_action": action,
        "block_reason": block_reason,
    }


def _write_report(
    rows: list[dict[str, str]],
    split_files_written: list[str],
    split_files_validated: list[str],
    blocked: dict[str, str],
) -> None:
    lines = [
        "# Stage 3.1.6 Split Report",
        "",
        "Date: 2026-06-26",
        "",
        "## Datasets Checked",
        "",
        "| dataset | loader backend | split action | block reason |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['dataset']} | {row['loader_backend']} | {row['split_action']} | {row['block_reason']} |"
        )
    lines.extend(["", "## Split Files Written", ""])
    lines.extend(f"- `{path}`" for path in split_files_written) if split_files_written else lines.append("- none")
    lines.extend(["", "## Split Files Validated", ""])
    lines.extend(f"- `{path}`" for path in split_files_validated) if split_files_validated else lines.append("- none")
    lines.extend(["", "## Blocked Datasets", ""])
    lines.extend(f"- {dataset}: {reason}" for dataset, reason in blocked.items()) if blocked else lines.append("- none")
    lines.extend(
        [
            "",
            "## Split Types",
            "",
            "- Cora: `custom_stratified_random_1_1_8` if available",
            "- Wiki-CS: `official_wikics` if official masks are readable",
            "- Actor: `heterophily_fixed` if fixed masks are readable",
            "",
            "## Boundary Flags",
            "",
            "- training was run: no",
            "- evaluator was run: no",
            "- GPU was used: no",
            "- baseline repo was cloned: no",
            "- accuracy/loss/performance table generated: no",
            "- class_distribution_test written: null only",
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
