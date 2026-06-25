import json
from pathlib import Path

import pytest

from gcl_diag.splits.split_io import SplitIntegrityError, read_split, write_split


ROOT = Path(__file__).resolve().parents[2]


def test_read_synthetic_split() -> None:
    split = read_split(ROOT / "tests/fixtures/synthetic_split.json", ROOT / "schemas/split_schema.json")
    assert split["dataset_name"] == "synthetic_only"
    assert split["class_distribution_test"] is None


def test_write_split_roundtrip(tmp_path: Path) -> None:
    split = read_split(ROOT / "tests/fixtures/synthetic_split.json", ROOT / "schemas/split_schema.json")
    out = tmp_path / "split.json"
    write_split(split, out, ROOT / "schemas/split_schema.json")
    assert read_split(out, ROOT / "schemas/split_schema.json")["num_nodes"] == 18


def test_reject_test_class_distribution(tmp_path: Path) -> None:
    split = json.loads((ROOT / "tests/fixtures/synthetic_split.json").read_text())
    split["class_distribution_test"] = {"0": 4, "1": 4}
    path = tmp_path / "bad_split.json"
    path.write_text(json.dumps(split), encoding="utf-8")
    with pytest.raises(SplitIntegrityError):
        read_split(path, ROOT / "schemas/split_schema.json")


def test_reject_overlapping_indices(tmp_path: Path) -> None:
    split = json.loads((ROOT / "tests/fixtures/synthetic_split.json").read_text())
    split["val_indices"] = [5, 6, 7, 8]
    path = tmp_path / "bad_split.json"
    path.write_text(json.dumps(split), encoding="utf-8")
    with pytest.raises(SplitIntegrityError):
        read_split(path, ROOT / "schemas/split_schema.json")
