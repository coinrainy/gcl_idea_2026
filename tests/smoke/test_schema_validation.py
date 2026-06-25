import json
from pathlib import Path

import pytest

from gcl_diag.io.schema_validate import SchemaValidationError, validate_file


ROOT = Path(__file__).resolve().parents[2]


def test_validate_synthetic_split_fixture() -> None:
    validate_file(ROOT / "schemas/split_schema.json", ROOT / "tests/fixtures/synthetic_split.json")


def test_missing_field_fails(tmp_path: Path) -> None:
    broken = json.loads((ROOT / "tests/fixtures/synthetic_split.json").read_text())
    broken.pop("split_type")
    path = tmp_path / "broken.json"
    path.write_text(json.dumps(broken), encoding="utf-8")
    with pytest.raises(SchemaValidationError):
        validate_file(ROOT / "schemas/split_schema.json", path)


def test_illegal_raw_stage_fails(tmp_path: Path) -> None:
    from gcl_diag.logging.raw_result_logger import success_record

    raw = success_record(stage="formal")
    path = tmp_path / "raw.json"
    path.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(SchemaValidationError):
        validate_file(ROOT / "schemas/raw_result_schema.json", path)


def test_illegal_metric_artifact_type_fails(tmp_path: Path) -> None:
    from gcl_diag.metrics.artifacts import write_label_free_artifact

    artifact_path = tmp_path / "metric.json"
    artifact = write_label_free_artifact({}, artifact_path, schema_path=ROOT / "schemas/metric_schema.json")
    artifact["artifact_type"] = "label_audit_and_free_mixed"
    artifact_path.write_text(json.dumps(artifact), encoding="utf-8")
    with pytest.raises(SchemaValidationError):
        validate_file(ROOT / "schemas/metric_schema.json", artifact_path)
