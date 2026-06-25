"""Controlled PyG dataset access for Stage 3.1.6.

This module only permits Cora, Wiki-CS and Actor through official PyG dataset
loaders. It does not train models, run evaluators or clone external code.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


APPROVED_DATASETS = {"Cora", "Wiki-CS", "Actor"}
DATASET_SPECS = {
    "Cora": {
        "backend": "pyg_planetoid",
        "root": "data/Planetoid",
        "split_source": "custom_stratified_random_1_1_8",
    },
    "Wiki-CS": {
        "backend": "pyg_wikics",
        "root": "data/WikiCS",
        "split_source": "official_wikics",
    },
    "Actor": {
        "backend": "pyg_actor",
        "root": "data/Actor",
        "split_source": "heterophily_fixed",
    },
}


@dataclass
class ControlledDataset:
    dataset_name: str
    loader_backend: str
    loader_status: str
    root: Path
    cache_path: Path
    local_cache_used: bool
    download_attempted: bool
    download_source: str
    dataset: Any | None
    data: Any | None
    error_message: str | None = None


def load_controlled_dataset(
    dataset_name: str,
    *,
    project_root: str | Path,
    data_access_mode: str,
    root: str | Path | None = None,
) -> ControlledDataset:
    if dataset_name not in APPROVED_DATASETS:
        raise ValueError(f"dataset is not approved for controlled access: {dataset_name}")
    if data_access_mode != "controlled_download":
        raise ValueError("Stage 3.1.6 real data access requires data_access_mode=controlled_download")

    project_root = Path(project_root).resolve()
    spec = DATASET_SPECS[dataset_name]
    requested_root = root if root is not None else spec["root"]
    resolved_root = _resolve_allowed_root(project_root, requested_root)
    cache_ready_before = _has_processed_cache(dataset_name, resolved_root)

    try:
        dataset, download_source = _instantiate_pyg_dataset(dataset_name, resolved_root)
        data = dataset[0]
    except Exception as exc:  # noqa: BLE001 - record loader failure without fallback.
        return ControlledDataset(
            dataset_name=dataset_name,
            loader_backend=spec["backend"],
            loader_status="loader_error",
            root=resolved_root,
            cache_path=resolved_root,
            local_cache_used=cache_ready_before,
            download_attempted=True,
            download_source="pyg_official_loader",
            dataset=None,
            data=None,
            error_message=_format_exception(exc),
        )

    return ControlledDataset(
        dataset_name=dataset_name,
        loader_backend=spec["backend"],
        loader_status="available",
        root=resolved_root,
        cache_path=resolved_root,
        local_cache_used=cache_ready_before,
        download_attempted=True,
        download_source=download_source,
        dataset=dataset,
        data=data,
    )


def metadata_fields(result: ControlledDataset) -> dict[str, Any]:
    dataset = result.dataset
    data = result.data
    if result.loader_status != "available" or dataset is None or data is None:
        return {
            "num_nodes": None,
            "num_edges": None,
            "num_features": None,
            "num_classes": None,
            "has_labels": None,
            "has_masks_or_official_splits": None,
            "split_source": None,
        }
    return {
        "num_nodes": int(data.num_nodes),
        "num_edges": int(data.edge_index.size(1)) if hasattr(data, "edge_index") and data.edge_index is not None else None,
        "num_features": int(dataset.num_features),
        "num_classes": int(dataset.num_classes),
        "has_labels": hasattr(data, "y") and data.y is not None,
        "has_masks_or_official_splits": _has_any_split_mask(data),
        "split_source": DATASET_SPECS[result.dataset_name]["split_source"],
    }


def _instantiate_pyg_dataset(dataset_name: str, root: Path) -> tuple[Any, str]:
    if dataset_name == "Cora":
        return _load_cora_planetoid(root)

    if dataset_name == "Wiki-CS":
        from torch_geometric.datasets import WikiCS

        return WikiCS(root=str(root)), "pyg_official_loader"
    if dataset_name == "Actor":
        from torch_geometric.datasets import Actor

        return Actor(root=str(root)), "pyg_official_loader"
    raise ValueError(f"unsupported dataset: {dataset_name}")


def _load_cora_planetoid(root: Path) -> tuple[Any, str]:
    from torch_geometric.datasets import Planetoid

    try:
        return Planetoid(root=str(root), name="Cora"), "pyg_official_loader"
    except Exception as primary_exc:  # noqa: BLE001 - allow official raw endpoint retry.
        fallback_url = "https://raw.githubusercontent.com/kimiyoung/planetoid/master/data"
        original_url = Planetoid.url
        try:
            Planetoid.url = fallback_url
            return Planetoid(root=str(root), name="Cora"), "pyg_official_loader_raw_github_endpoint"
        except Exception as fallback_exc:  # noqa: BLE001
            raise RuntimeError(
                "Cora PyG Planetoid failed via default endpoint and raw GitHub endpoint; "
                f"default_error={_format_exception(primary_exc)}; "
                f"raw_endpoint_error={_format_exception(fallback_exc)}"
            ) from fallback_exc
        finally:
            Planetoid.url = original_url


def _resolve_allowed_root(project_root: Path, root: str | Path) -> Path:
    candidate = Path(root)
    if not candidate.is_absolute():
        candidate = project_root / candidate
    candidate = candidate.resolve()
    allowed_roots = [(project_root / "data").resolve(), (project_root / "datasets").resolve()]
    if not any(candidate == allowed or allowed in candidate.parents for allowed in allowed_roots):
        raise ValueError(f"dataset root must be inside project data/ or datasets/: {candidate}")
    return candidate


def _has_any_split_mask(data: Any) -> bool:
    return any(getattr(data, name, None) is not None for name in ("train_mask", "val_mask", "test_mask"))


def _has_processed_cache(dataset_name: str, root: Path) -> bool:
    processed_dirs = [root / "processed"]
    if dataset_name == "Cora":
        processed_dirs.insert(0, root / "Cora" / "processed")
    return any(path.exists() and any(path.iterdir()) for path in processed_dirs)


def _format_exception(exc: Exception) -> str:
    text = str(exc).strip()
    if text:
        return f"{type(exc).__name__}: {text}"
    return f"{type(exc).__name__}: {exc!r}"
