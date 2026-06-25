"""Dataset metadata writer for loader and split readiness stages."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from gcl_diag.io.schema_validate import load_json, validate


APPROVED_CONTROLLED_DOWNLOAD_DATASETS = {"Cora", "Wiki-CS", "Actor"}
FORBIDDEN_METADATA_FIELDS = {
    "accuracy",
    "loss",
    "performance",
    "performance_table",
    "embedding",
    "embeddings",
    "objective_ranking",
    "test_label_distribution",
    "class_distribution_test",
}


def build_metadata(
    *,
    dataset_name: str,
    loader_backend: str,
    loader_status: str,
    local_cache_used: bool = False,
    download_attempted: bool = False,
    data_access_mode: str = "no_download",
    cache_path: str | None = None,
    download_source: str | None = None,
    num_nodes: int | None = None,
    num_edges: int | None = None,
    num_features: int | None = None,
    num_classes: int | None = None,
    has_labels: bool | None = None,
    has_masks_or_official_splits: bool | None = None,
    split_source: str | None = None,
    error_message: str | None = None,
    created_at: str = "2026-06-26T00:00:00Z",
    commit_hash: str = "unknown",
) -> dict[str, Any]:
    return {
        "dataset_name": dataset_name,
        "loader_backend": loader_backend,
        "loader_status": loader_status,
        "local_cache_used": local_cache_used,
        "download_attempted": download_attempted,
        "data_access_mode": data_access_mode,
        "cache_path": cache_path,
        "download_source": download_source,
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "num_features": num_features,
        "num_classes": num_classes,
        "has_labels": has_labels,
        "has_masks_or_official_splits": has_masks_or_official_splits,
        "split_source": split_source,
        "evaluation_setting": "transductive",
        "graph_visibility": "metadata probe only; no training/evaluator/pilot run",
        "error_message": error_message,
        "created_at": created_at,
        "commit_hash": commit_hash,
    }


def write_metadata(
    metadata: dict[str, Any],
    path: str | Path,
    schema_path: str | Path = "schemas/dataset_metadata_schema.json",
) -> dict[str, Any]:
    _validate_metadata_boundaries(metadata)
    validate(metadata, load_json(schema_path))
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, sort_keys=True)
        f.write("\n")
    return metadata


def _validate_metadata_boundaries(metadata: dict[str, Any]) -> None:
    forbidden = FORBIDDEN_METADATA_FIELDS & set(metadata)
    if forbidden:
        raise ValueError(f"metadata must not contain performance/test-label fields: {sorted(forbidden)}")
    if metadata.get("download_attempted") is True:
        if metadata.get("data_access_mode") != "controlled_download":
            raise ValueError("download_attempted=true requires data_access_mode=controlled_download")
        if metadata.get("dataset_name") not in APPROVED_CONTROLLED_DOWNLOAD_DATASETS:
            raise ValueError("controlled download is only allowed for Cora, Wiki-CS and Actor")
