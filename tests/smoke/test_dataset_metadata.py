from pathlib import Path

import pytest

from gcl_diag.data.metadata import build_metadata, write_metadata
from gcl_diag.io.schema_validate import validate_file


ROOT = Path(__file__).resolve().parents[2]


def test_write_missing_cache_metadata(tmp_path: Path) -> None:
    metadata = build_metadata(
        dataset_name="Cora",
        loader_backend="pyg_planetoid",
        loader_status="download_required_not_approved",
        error_message="cache missing",
    )
    assert metadata["download_attempted"] is False
    out = tmp_path / "metadata.json"
    write_metadata(metadata, out, ROOT / "schemas/dataset_metadata_schema.json")
    validate_file(ROOT / "schemas/dataset_metadata_schema.json", out)


def test_write_controlled_download_metadata(tmp_path: Path) -> None:
    metadata = build_metadata(
        dataset_name="Wiki-CS",
        loader_backend="pyg_wikics",
        loader_status="available",
        local_cache_used=False,
        download_attempted=True,
        data_access_mode="controlled_download",
        cache_path="data/WikiCS",
        download_source="pyg_official_loader",
    )
    out = tmp_path / "metadata.json"
    write_metadata(metadata, out, ROOT / "schemas/dataset_metadata_schema.json")
    validate_file(ROOT / "schemas/dataset_metadata_schema.json", out)


def test_reject_controlled_download_for_unapproved_dataset(tmp_path: Path) -> None:
    metadata = build_metadata(
        dataset_name="PubMed",
        loader_backend="pyg_planetoid",
        loader_status="available",
        download_attempted=True,
        data_access_mode="controlled_download",
    )
    with pytest.raises(ValueError):
        write_metadata(metadata, tmp_path / "metadata.json", ROOT / "schemas/dataset_metadata_schema.json")


def test_local_cache_missing_metadata_remains_valid(tmp_path: Path) -> None:
    metadata = build_metadata(
        dataset_name="Actor",
        loader_backend="pyg_actor",
        loader_status="local_cache_missing",
        download_attempted=False,
        error_message="cache missing",
    )
    out = tmp_path / "metadata.json"
    write_metadata(metadata, out, ROOT / "schemas/dataset_metadata_schema.json")
    validate_file(ROOT / "schemas/dataset_metadata_schema.json", out)
