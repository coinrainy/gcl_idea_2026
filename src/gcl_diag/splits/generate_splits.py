"""Split generation/extraction scaffold for Stage 3.1.5.

This module never downloads data and never trains/evaluates models. It only
writes split JSON when metadata proves that a local dataset cache is available.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from gcl_diag.splits.split_io import write_split


def can_generate_split(metadata: dict[str, Any]) -> bool:
    return metadata.get("loader_status") == "available" and metadata.get("local_cache_used") is True


def build_custom_split_from_counts(
    *,
    dataset_name: str,
    num_nodes: int,
    train_indices: list[int],
    val_indices: list[int],
    test_indices: list[int],
    split_type: str,
    split_seed: int,
    created_by: str,
    created_at: str,
    commit_hash: str,
) -> dict[str, Any]:
    return {
        "dataset_name": dataset_name,
        "split_type": split_type,
        "split_seed": split_seed,
        "num_nodes": num_nodes,
        "train_indices": train_indices,
        "val_indices": val_indices,
        "test_indices": test_indices,
        "num_train": len(train_indices),
        "num_val": len(val_indices),
        "num_test": len(test_indices),
        "class_distribution_train": None,
        "class_distribution_val": None,
        "class_distribution_test": None,
        "created_by": created_by,
        "created_at": created_at,
        "commit_hash": commit_hash,
    }


def write_validated_split(split: dict[str, Any], path: str | Path, schema_path: str | Path = "schemas/split_schema.json") -> None:
    write_split(split, path, schema_path=schema_path)
