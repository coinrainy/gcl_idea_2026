"""Synthetic raw-result writer for Stage 3.1 scaffold."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from gcl_diag.io.schema_validate import load_json, validate


class RawResultError(ValueError):
    """Raised when a raw result record violates scaffold constraints."""


REQUIRED_DEFAULTS: dict[str, Any] = {
    "stage": "pilot",
    "evaluation_setting": "transductive",
    "graph_visibility": "synthetic embeddings only; no real graph accessed",
    "evaluator_type": "frozen_encoder_linear_evaluator",
    "early_stopping_metric": "validation_accuracy",
    "backbone": "synthetic",
    "budget_policy": "synthetic_smoke_only",
    "notes": "synthetic smoke only; no performance claim",
}


def write_raw_result(record: dict[str, Any], path: str | Path, schema_path: str | Path = "schemas/raw_result_schema.json") -> dict[str, Any]:
    full_record = {**REQUIRED_DEFAULTS, **record}
    _check_status(full_record)
    schema = load_json(schema_path)
    validate(full_record, schema)
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump(full_record, f, indent=2, sort_keys=True)
        f.write("\n")
    return full_record


def success_record(**overrides: Any) -> dict[str, Any]:
    record = _base_record()
    record.update(
        {
            "status": "success",
            "failure_reason": None,
            "best_epoch": 3,
            "valid_at_best": 0.75,
            "test_at_best": 0.5,
            "final_valid": 0.75,
            "final_test": 0.5,
            "training_time_sec": 0.0,
            "peak_memory_mb": 0.0,
        }
    )
    record.update(overrides)
    return record


def fail_record(failure_reason: str, **overrides: Any) -> dict[str, Any]:
    if not failure_reason:
        raise RawResultError("failure_reason must be non-empty for fail records")
    record = _base_record()
    record.update(
        {
            "status": "fail",
            "failure_reason": failure_reason,
            "best_epoch": None,
            "valid_at_best": None,
            "test_at_best": None,
            "final_valid": None,
            "final_test": None,
            "training_time_sec": None,
            "peak_memory_mb": None,
        }
    )
    record.update(overrides)
    return record


def _base_record() -> dict[str, Any]:
    return {
        "run_id": "synthetic-run",
        "method": "SYNTHETIC",
        "objective_family": "synthetic_only",
        "dataset": "synthetic_only",
        "split_type": "synthetic_fixed",
        "split_file": "tests/fixtures/synthetic_split.json",
        "split_seed": 0,
        "model_seed": 0,
        "config_path": "configs/pilot_scaffold.yaml",
        "config_hash": "synthetic-config-hash",
        "run_command": "python scripts/run_stage3_1_synthetic_smoke.py",
        "commit_hash": "synthetic-commit",
        "evaluator_seed": 0,
        "patience": 2,
        "max_epochs": 5,
        "pretrain_epochs": None,
        "hidden_dim": 4,
        "projection_dim": 4,
        "result_file_path": "synthetic_temp_result.json",
        "log_path": "synthetic_temp.log",
    }


def _check_status(record: dict[str, Any]) -> None:
    if record.get("stage") != "pilot":
        raise RawResultError("raw result stage must be pilot")
    if record.get("status") == "fail":
        if not record.get("failure_reason"):
            raise RawResultError("fail record requires a non-empty failure_reason")
        if record.get("test_at_best") is not None or record.get("final_test") is not None:
            raise RawResultError("fail record must set test_at_best and final_test to null")
