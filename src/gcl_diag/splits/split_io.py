"""Split file reader/writer and integrity checks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from gcl_diag.io.schema_validate import SchemaValidationError, load_json, validate


class SplitIntegrityError(ValueError):
    """Raised when a split file violates project integrity rules."""


def read_split(path: str | Path, schema_path: str | Path = "schemas/split_schema.json") -> dict[str, Any]:
    split = load_json(path)
    schema = load_json(schema_path)
    validate(split, schema)
    check_split_integrity(split)
    return split


def write_split(split: dict[str, Any], path: str | Path, schema_path: str | Path = "schemas/split_schema.json") -> None:
    schema = load_json(schema_path)
    validate(split, schema)
    check_split_integrity(split)
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump(split, f, indent=2, sort_keys=True)
        f.write("\n")


def check_split_integrity(split: dict[str, Any]) -> None:
    split_type = split.get("split_type")
    if not isinstance(split_type, str) or not split_type:
        raise SplitIntegrityError("split_type must be explicitly recorded")

    if split.get("class_distribution_test") is not None:
        raise SplitIntegrityError("shared split files must set class_distribution_test to null")

    num_nodes = split["num_nodes"]
    train = _indices(split, "train_indices")
    val = _indices(split, "val_indices")
    test = _indices(split, "test_indices")

    _check_count(split, "num_train", train)
    _check_count(split, "num_val", val)
    _check_count(split, "num_test", test)

    for name, values in [("train", train), ("val", val), ("test", test)]:
        for idx in values:
            if idx < 0 or idx >= num_nodes:
                raise SplitIntegrityError(f"{name} index {idx} outside [0, {num_nodes})")

    if train & val or train & test or val & test:
        raise SplitIntegrityError("train/val/test indices must be pairwise disjoint")


def _indices(split: dict[str, Any], key: str) -> set[int]:
    try:
        return set(int(x) for x in split[key])
    except (KeyError, TypeError, ValueError) as exc:
        raise SplitIntegrityError(f"{key} must be a list of integer node indices") from exc


def _check_count(split: dict[str, Any], key: str, values: set[int]) -> None:
    if split[key] != len(values):
        raise SplitIntegrityError(f"{key}={split[key]} does not match index count {len(values)}")
