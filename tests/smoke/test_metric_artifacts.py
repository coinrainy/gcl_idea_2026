from pathlib import Path

import pytest

from gcl_diag.io.schema_validate import validate_file
from gcl_diag.metrics.artifacts import (
    MetricArtifactError,
    load_selector_metrics,
    write_label_audit_artifact,
    write_label_free_artifact,
)


ROOT = Path(__file__).resolve().parents[2]


def test_label_free_artifact_selector_loads(tmp_path: Path) -> None:
    out = tmp_path / "label_free.json"
    artifact = write_label_free_artifact({}, out, schema_path=ROOT / "schemas/metric_schema.json")
    validate_file(ROOT / "schemas/metric_schema.json", out)
    loaded = load_selector_metrics(out, ROOT / "schemas/metric_schema.json")
    assert loaded == artifact["label_free_regime_metrics"]
    assert artifact["selector_visible"] is True


def test_label_audit_artifact_rejected_by_selector(tmp_path: Path) -> None:
    free_path = tmp_path / "label_free.json"
    free = write_label_free_artifact({}, free_path, schema_path=ROOT / "schemas/metric_schema.json")
    audit_path = tmp_path / "label_audit.json"
    audit = write_label_audit_artifact(
        {"validation_objective_ranking": ["GRACE", "BGRL"]},
        audit_path,
        freeze_hash=free["freeze_hash"],
        schema_path=ROOT / "schemas/metric_schema.json",
    )
    validate_file(ROOT / "schemas/metric_schema.json", audit_path)
    assert audit["selector_visible"] is False
    with pytest.raises(MetricArtifactError):
        load_selector_metrics(audit_path, ROOT / "schemas/metric_schema.json")
