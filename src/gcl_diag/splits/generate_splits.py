"""Split generation/extraction helpers.

This module never downloads data and never trains/evaluates models. It only
writes split JSON from already loaded dataset objects or synthetic fixtures.
"""

from __future__ import annotations

import math
from pathlib import Path
import random
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


def build_stratified_random_1_1_8_split(
    *,
    dataset_name: str,
    labels: Any,
    split_seed: int,
    created_by: str,
    created_at: str,
    commit_hash: str,
) -> dict[str, Any]:
    label_list = [int(x) for x in _to_list(labels)]
    num_nodes = len(label_list)
    class_to_indices: dict[int, list[int]] = {}
    for idx, label in enumerate(label_list):
        class_to_indices.setdefault(label, []).append(idx)
    if not class_to_indices:
        raise ValueError("labels are required for stratified split generation")
    for label, indices in class_to_indices.items():
        if len(indices) < 3:
            raise ValueError(f"class {label} has fewer than 3 nodes; cannot reserve train/val/test")

    class_counts = {label: len(indices) for label, indices in class_to_indices.items()}
    target_train = round(num_nodes * 0.1)
    target_val = round(num_nodes * 0.1)
    train_caps = {label: count - 2 for label, count in class_counts.items()}
    train_counts = _allocate_stratified_counts(class_counts, target_train, train_caps)
    val_caps = {label: class_counts[label] - train_counts[label] - 1 for label in class_counts}
    val_counts = _allocate_stratified_counts(class_counts, target_val, val_caps)

    rng = random.Random(split_seed)
    train_indices: list[int] = []
    val_indices: list[int] = []
    test_indices: list[int] = []
    for label in sorted(class_to_indices):
        indices = list(class_to_indices[label])
        rng.shuffle(indices)
        train_n = train_counts[label]
        val_n = val_counts[label]
        train_indices.extend(indices[:train_n])
        val_indices.extend(indices[train_n : train_n + val_n])
        test_indices.extend(indices[train_n + val_n :])

    train_indices.sort()
    val_indices.sort()
    test_indices.sort()
    return {
        "dataset_name": dataset_name,
        "split_type": "custom_stratified_random_1_1_8",
        "split_seed": split_seed,
        "num_nodes": num_nodes,
        "train_indices": train_indices,
        "val_indices": val_indices,
        "test_indices": test_indices,
        "num_train": len(train_indices),
        "num_val": len(val_indices),
        "num_test": len(test_indices),
        "class_distribution_train": _class_distribution(label_list, train_indices),
        "class_distribution_val": _class_distribution(label_list, val_indices),
        "class_distribution_test": None,
        "created_by": created_by,
        "created_at": created_at,
        "commit_hash": commit_hash,
    }


def build_split_from_masks(
    *,
    dataset_name: str,
    split_type: str,
    split_seed: int,
    train_mask: Any,
    val_mask: Any,
    test_mask: Any,
    labels: Any | None,
    created_by: str,
    created_at: str,
    commit_hash: str,
) -> dict[str, Any]:
    train_indices = _mask_to_indices(train_mask, split_seed)
    val_indices = _mask_to_indices(val_mask, split_seed)
    test_indices = _mask_to_indices(test_mask, split_seed)
    label_list = [int(x) for x in _to_list(labels)] if labels is not None else None
    num_nodes = _infer_num_nodes(train_mask, val_mask, test_mask, label_list)
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
        "class_distribution_train": _class_distribution(label_list, train_indices) if label_list is not None else None,
        "class_distribution_val": _class_distribution(label_list, val_indices) if label_list is not None else None,
        "class_distribution_test": None,
        "created_by": created_by,
        "created_at": created_at,
        "commit_hash": commit_hash,
    }


def write_validated_split(split: dict[str, Any], path: str | Path, schema_path: str | Path = "schemas/split_schema.json") -> None:
    write_split(split, path, schema_path=schema_path)


def _allocate_stratified_counts(class_counts: dict[int, int], target_total: int, caps: dict[int, int]) -> dict[int, int]:
    if target_total < len(class_counts):
        raise ValueError("target split size is too small to place every class")
    total = sum(class_counts.values())
    allocated: dict[int, int] = {}
    fractions: list[tuple[float, int]] = []
    for label, count in class_counts.items():
        raw = count * target_total / total
        value = max(1, math.floor(raw))
        if value > caps[label]:
            raise ValueError(f"class {label} cannot satisfy stratified split cap")
        allocated[label] = value
        fractions.append((raw - math.floor(raw), label))
    current = sum(allocated.values())
    if current > target_total:
        raise ValueError("minimum per-class allocation exceeds target split size")
    for _, label in sorted(fractions, reverse=True):
        if current == target_total:
            break
        if allocated[label] < caps[label]:
            allocated[label] += 1
            current += 1
    if current != target_total:
        raise ValueError("could not allocate requested stratified split size")
    return allocated


def _mask_to_indices(mask: Any, split_seed: int) -> list[int]:
    if mask is None:
        raise ValueError("required official/fixed split mask is unavailable")
    selected = _select_mask_column(mask, split_seed)
    values = _to_list(selected)
    return [idx for idx, value in enumerate(values) if bool(value)]


def _select_mask_column(mask: Any, split_seed: int) -> Any:
    if hasattr(mask, "dim") and callable(mask.dim):
        dim = int(mask.dim())
        if dim == 1:
            return mask
        if dim == 2:
            if split_seed >= int(mask.size(1)):
                raise ValueError(f"official split id {split_seed} is unavailable")
            return mask[:, split_seed]
    values = _to_list(mask)
    if values and isinstance(values[0], list):
        if split_seed >= len(values[0]):
            raise ValueError(f"official split id {split_seed} is unavailable")
        return [row[split_seed] for row in values]
    return mask


def _infer_num_nodes(train_mask: Any, val_mask: Any, test_mask: Any, labels: list[int] | None) -> int:
    if labels is not None:
        return len(labels)
    return max(len(_to_list(_select_mask_column(mask, 0))) for mask in (train_mask, val_mask, test_mask) if mask is not None)


def _class_distribution(labels: list[int], indices: list[int]) -> dict[str, int]:
    distribution: dict[str, int] = {}
    for idx in indices:
        key = str(labels[idx])
        distribution[key] = distribution.get(key, 0) + 1
    return dict(sorted(distribution.items(), key=lambda item: int(item[0])))


def _to_list(value: Any) -> list[Any]:
    if hasattr(value, "detach"):
        value = value.detach().cpu()
    if hasattr(value, "tolist"):
        return value.tolist()
    return list(value)
