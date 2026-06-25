"""Metric artifact writer and selector-safe loader."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from gcl_diag.io.schema_validate import load_json, validate


class MetricArtifactError(ValueError):
    """Raised when metric artifacts violate leakage boundaries."""


LABEL_FREE_FIELDS = [
    "edge_feature_similarity_mean",
    "edge_feature_similarity_std",
    "one_hop_feature_smoothness",
    "two_hop_feature_smoothness",
    "degree_skew",
    "degree_entropy",
    "clustering_coefficient_mean",
    "connected_component_count",
    "structural_role_entropy",
    "masked_feature_reconstruction_difficulty",
    "edge_reconstruction_difficulty",
    "augmentation_stability_score",
    "embedding_rank_proxy",
    "embedding_variance_proxy",
    "uniformity_proxy",
]

LABEL_AUDIT_FIELDS = [
    "train_val_label_homophily",
    "train_val_feature_label_predictability",
    "validation_objective_ranking",
    "negative_pair_label_agreement",
    "ambiguous_pair_precision",
    "ambiguous_pair_recall",
]

PROHIBITED = {
    "test_label_homophily": "prohibited",
    "test_feature_label_predictability": "prohibited",
    "test_objective_ranking": "prohibited",
    "any_metric_computed_after_looking_at_test_accuracy_for_survival_decision": "prohibited",
}


def write_label_free_artifact(
    metrics: dict[str, Any],
    path: str | Path,
    *,
    dataset: str = "synthetic_only",
    split_type: str = "synthetic_fixed",
    split_seed: int = 0,
    created_at: str = "2026-06-26T00:00:00Z",
    commit_hash: str = "synthetic-commit",
    schema_path: str | Path = "schemas/metric_schema.json",
) -> dict[str, Any]:
    payload = {field: metrics.get(field) for field in LABEL_FREE_FIELDS}
    artifact = {
        "dataset": dataset,
        "artifact_type": "label_free_regime_metrics",
        "selector_visible": True,
        "freeze_hash": _hash_payload(payload),
        "split_type": split_type,
        "split_seed": split_seed,
        "created_at": created_at,
        "commit_hash": commit_hash,
        "metric_freeze_status": "frozen_before_validation_outcome",
        "label_free_regime_metrics": payload,
        "label_audit_metrics": None,
        "prohibited_metrics": PROHIBITED,
    }
    return _write_artifact(artifact, path, schema_path)


def write_label_audit_artifact(
    metrics: dict[str, Any],
    path: str | Path,
    *,
    freeze_hash: str,
    dataset: str = "synthetic_only",
    split_type: str = "synthetic_fixed",
    split_seed: int = 0,
    created_at: str = "2026-06-26T00:00:00Z",
    commit_hash: str = "synthetic-commit",
    schema_path: str | Path = "schemas/metric_schema.json",
) -> dict[str, Any]:
    payload = {field: metrics.get(field) for field in LABEL_AUDIT_FIELDS}
    artifact = {
        "dataset": dataset,
        "artifact_type": "label_audit_metrics",
        "selector_visible": False,
        "freeze_hash": freeze_hash,
        "split_type": split_type,
        "split_seed": split_seed,
        "created_at": created_at,
        "commit_hash": commit_hash,
        "metric_freeze_status": "frozen_before_validation_outcome",
        "label_free_regime_metrics": None,
        "label_audit_metrics": payload,
        "prohibited_metrics": PROHIBITED,
    }
    return _write_artifact(artifact, path, schema_path)


def load_selector_metrics(path: str | Path, schema_path: str | Path = "schemas/metric_schema.json") -> dict[str, Any]:
    artifact = load_json(path)
    validate(artifact, load_json(schema_path))
    if artifact.get("artifact_type") != "label_free_regime_metrics":
        raise MetricArtifactError("selector can only load label_free_regime_metrics artifacts")
    if artifact.get("selector_visible") is not True:
        raise MetricArtifactError("selector artifact must have selector_visible=true")
    if artifact.get("metric_freeze_status") != "frozen_before_validation_outcome":
        raise MetricArtifactError("selector artifact must be frozen before validation outcome")
    if not artifact.get("freeze_hash"):
        raise MetricArtifactError("selector artifact requires a non-empty freeze_hash")
    expected_hash = _hash_payload(artifact["label_free_regime_metrics"])
    if artifact["freeze_hash"] != expected_hash:
        raise MetricArtifactError("selector artifact freeze_hash does not match payload")
    return artifact["label_free_regime_metrics"]


def _write_artifact(artifact: dict[str, Any], path: str | Path, schema_path: str | Path) -> dict[str, Any]:
    validate(artifact, load_json(schema_path))
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump(artifact, f, indent=2, sort_keys=True)
        f.write("\n")
    return artifact


def _hash_payload(payload: dict[str, Any]) -> str:
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()
