"""Dataset metadata writer for Stage 3.1.5."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from gcl_diag.io.schema_validate import load_json, validate


def build_metadata(
    *,
    dataset_name: str,
    loader_backend: str,
    loader_status: str,
    local_cache_used: bool = False,
    download_attempted: bool = False,
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
    if metadata.get("download_attempted") is not False:
        raise ValueError("Stage 3.1.5 metadata must record download_attempted=false")
    validate(metadata, load_json(schema_path))
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, sort_keys=True)
        f.write("\n")
    return metadata
