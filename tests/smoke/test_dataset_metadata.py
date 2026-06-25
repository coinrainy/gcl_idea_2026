from pathlib import Path

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
