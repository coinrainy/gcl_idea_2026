from pathlib import Path

from gcl_diag.splits.generate_splits import build_custom_split_from_counts, write_validated_split
from gcl_diag.splits.split_io import read_split


ROOT = Path(__file__).resolve().parents[2]


def test_mock_split_generation_validates(tmp_path: Path) -> None:
    split = build_custom_split_from_counts(
        dataset_name="MockGraph",
        num_nodes=20,
        train_indices=[0, 1],
        val_indices=[2, 3],
        test_indices=list(range(4, 20)),
        split_type="custom_random_1_1_8",
        split_seed=0,
        created_by="test",
        created_at="2026-06-26T00:00:00Z",
        commit_hash="test",
    )
    out = tmp_path / "split.json"
    write_validated_split(split, out, ROOT / "schemas/split_schema.json")
    loaded = read_split(out, ROOT / "schemas/split_schema.json")
    assert loaded["class_distribution_test"] is None
