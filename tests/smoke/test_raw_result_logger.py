from pathlib import Path

import pytest

from gcl_diag.io.schema_validate import validate_file
from gcl_diag.logging.raw_result_logger import RawResultError, fail_record, success_record, write_raw_result


ROOT = Path(__file__).resolve().parents[2]


def test_write_success_record(tmp_path: Path) -> None:
    out = tmp_path / "success.json"
    write_raw_result(success_record(run_id="success"), out, ROOT / "schemas/raw_result_schema.json")
    validate_file(ROOT / "schemas/raw_result_schema.json", out)


def test_write_fail_record(tmp_path: Path) -> None:
    out = tmp_path / "fail.json"
    record = fail_record("synthetic failure", run_id="fail")
    assert record["test_at_best"] is None
    assert record["final_test"] is None
    write_raw_result(record, out, ROOT / "schemas/raw_result_schema.json")
    validate_file(ROOT / "schemas/raw_result_schema.json", out)


def test_fail_record_requires_reason() -> None:
    with pytest.raises(RawResultError):
        fail_record("")
