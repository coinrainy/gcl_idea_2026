#!/usr/bin/env python
"""Run Stage 3.1 synthetic-only smoke checks.

This script intentionally uses only synthetic fixtures and temporary output
directories. It must not download datasets, train GCL encoders, clone baselines
or write real pilot results.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import traceback
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from gcl_diag.eval.frozen_linear import FrozenLinearEvaluator
from gcl_diag.io.schema_validate import validate_file
from gcl_diag.logging.raw_result_logger import fail_record, success_record, write_raw_result
from gcl_diag.metrics.artifacts import (
    MetricArtifactError,
    load_selector_metrics,
    write_label_audit_artifact,
    write_label_free_artifact,
)
from gcl_diag.methods import BGRLPlaceholder, GRACEPlaceholder, GraphMAEPlaceholder
from gcl_diag.splits.split_io import read_split


REPORT_PATH = ROOT / "refine-logs/STAGE3_1_SMOKE_REPORT.md"


def main() -> int:
    checks: list[tuple[str, Callable[[], None]]] = [
        ("validate synthetic split fixture", check_split_fixture),
        ("validate synthetic label-free metric artifact", check_label_free_metric),
        ("selector loader rejects label-audit artifact", check_selector_rejects_audit),
        ("run frozen evaluator on synthetic embeddings", check_frozen_evaluator),
        ("write and validate synthetic raw results", check_raw_results),
        ("method placeholders block real training", check_method_placeholders),
    ]
    passed: list[str] = []
    failed: list[str] = []
    details: list[str] = []

    for name, fn in checks:
        try:
            fn()
        except Exception as exc:  # noqa: BLE001 - smoke report should capture all failures.
            failed.append(name)
            details.append(f"### {name}\n\nFAILED: `{type(exc).__name__}: {exc}`\n\n```text\n{traceback.format_exc()}\n```")
        else:
            passed.append(name)
            details.append(f"### {name}\n\nPASSED")

    write_report(passed, failed, details)
    if failed:
        return 1
    return 0


def check_split_fixture() -> None:
    validate_file(ROOT / "schemas/split_schema.json", ROOT / "tests/fixtures/synthetic_split.json")
    read_split(ROOT / "tests/fixtures/synthetic_split.json", ROOT / "schemas/split_schema.json")


def check_label_free_metric() -> None:
    with tempfile.TemporaryDirectory(prefix="stage3_1_metric_") as tmp:
        out = Path(tmp) / "label_free.json"
        write_label_free_artifact({}, out, schema_path=ROOT / "schemas/metric_schema.json")
        validate_file(ROOT / "schemas/metric_schema.json", out)
        load_selector_metrics(out, ROOT / "schemas/metric_schema.json")


def check_selector_rejects_audit() -> None:
    with tempfile.TemporaryDirectory(prefix="stage3_1_metric_") as tmp:
        tmp_path = Path(tmp)
        label_free = write_label_free_artifact({}, tmp_path / "label_free.json", schema_path=ROOT / "schemas/metric_schema.json")
        write_label_audit_artifact(
            {"validation_objective_ranking": ["GRACE", "BGRL", "GraphMAE"]},
            tmp_path / "label_audit.json",
            freeze_hash=label_free["freeze_hash"],
            schema_path=ROOT / "schemas/metric_schema.json",
        )
        try:
            load_selector_metrics(tmp_path / "label_audit.json", ROOT / "schemas/metric_schema.json")
        except MetricArtifactError:
            return
        raise AssertionError("label-audit artifact was accepted by selector loader")


def check_frozen_evaluator() -> None:
    embeddings = [
        [0.0, 0.0],
        [0.1, 0.0],
        [1.0, 1.0],
        [1.1, 1.0],
        [0.0, 0.2],
        [1.2, 0.9],
        [0.2, 0.1],
        [1.0, 0.8],
        [0.1, 0.2],
        [1.1, 1.1],
        [0.2, 0.0],
        [1.2, 1.0],
    ]
    labels = [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    result = FrozenLinearEvaluator(evaluator_seed=0, max_epochs=5, patience=2).evaluate(
        embeddings,
        labels,
        train_indices=[0, 1, 2, 3],
        val_indices=[4, 5, 6, 7],
        test_indices=[8, 9, 10, 11],
    )
    if result.best_epoch != 3:
        raise AssertionError("unexpected synthetic best_epoch")


def check_raw_results() -> None:
    with tempfile.TemporaryDirectory(prefix="stage3_1_raw_") as tmp:
        tmp_path = Path(tmp)
        success_path = tmp_path / "success.json"
        fail_path = tmp_path / "fail.json"
        write_raw_result(
            success_record(run_id="synthetic-success", result_file_path=str(success_path)),
            success_path,
            ROOT / "schemas/raw_result_schema.json",
        )
        write_raw_result(
            fail_record("synthetic failure", run_id="synthetic-fail", result_file_path=str(fail_path)),
            fail_path,
            ROOT / "schemas/raw_result_schema.json",
        )
        validate_file(ROOT / "schemas/raw_result_schema.json", success_path)
        validate_file(ROOT / "schemas/raw_result_schema.json", fail_path)
        fail_payload = json.loads(fail_path.read_text(encoding="utf-8"))
        if fail_payload["test_at_best"] is not None or fail_payload["final_test"] is not None:
            raise AssertionError("fail raw result must not contain test metrics")


def check_method_placeholders() -> None:
    for cls in [GRACEPlaceholder, BGRLPlaceholder, GraphMAEPlaceholder]:
        method = cls()
        for action in [method.build_model, method.pretrain, method.encode]:
            try:
                action()
            except NotImplementedError as exc:
                if "Stage 3.1 scaffold only" not in str(exc):
                    raise
            else:
                raise AssertionError(f"{method.method_name}.{action.__name__} did not block real training")


def write_report(passed: list[str], failed: list[str], details: list[str]) -> None:
    pytest_available = importlib.util.find_spec("pytest") is not None
    lines = [
        "# Stage 3.1 Synthetic Smoke Report",
        "",
        "Date: 2026-06-26",
        "",
        "## Commands Run",
        "",
        "- `python scripts/run_stage3_1_synthetic_smoke.py`",
        "",
        "## Passed Checks",
        "",
    ]
    lines.extend(f"- {item}" for item in passed)
    if not passed:
        lines.append("- none")
    lines.extend(["", "## Failed Checks", ""])
    lines.extend(f"- {item}" for item in failed)
    if not failed:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Dependencies Used",
            "",
            "- Python standard library",
            f"- pytest available: {pytest_available}",
            "- numpy/torch/sklearn: not required by smoke runner",
            "",
            "## Boundary Flags",
            "",
            "- real dataset accessed: no",
            "- training run: no",
            "- GPU used: no",
            "- baseline repo cloned: no",
            "- real pilot run: no",
            "- performance claim generated: no",
            "",
            "## Detailed Check Log",
            "",
        ]
    )
    lines.extend(details)
    if failed:
        lines.extend(
            [
                "",
                "## Fix Suggestions",
                "",
                "- Inspect failed check tracebacks above.",
                "- Fix only synthetic scaffold issues; do not download data or run training.",
            ]
        )
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
