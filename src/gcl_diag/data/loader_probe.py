"""Non-downloading dataset loader probes for Stage 3.1.5."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import importlib.util
from pathlib import Path
from typing import Any


STATUSES = {
    "available",
    "missing_dependency",
    "local_cache_missing",
    "loader_error",
    "download_required_not_approved",
}


@dataclass(frozen=True)
class LoaderProbeResult:
    dataset_name: str
    loader_backend: str
    loader_status: str
    cache_path: str
    local_cache_used: bool
    download_attempted: bool
    error_message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


DATASET_PROBES = {
    "Cora": {
        "backend": "pyg_planetoid",
        "dependency": "torch_geometric",
        "class_import": "torch_geometric.datasets.Planetoid",
        "cache_paths": ["data/Planetoid/Cora", "data/Cora", "datasets/Planetoid/Cora", "datasets/Cora"],
    },
    "Wiki-CS": {
        "backend": "pyg_wikics",
        "dependency": "torch_geometric",
        "class_import": "torch_geometric.datasets.WikiCS",
        "cache_paths": ["data/WikiCS", "data/Wiki-CS", "datasets/WikiCS", "datasets/Wiki-CS"],
    },
    "Actor": {
        "backend": "pyg_actor",
        "dependency": "torch_geometric",
        "class_import": "torch_geometric.datasets.Actor",
        "cache_paths": ["data/Actor", "datasets/Actor"],
    },
}


def probe_dataset(dataset_name: str, root: str | Path = ".") -> LoaderProbeResult:
    spec = DATASET_PROBES[dataset_name]
    dependency = spec["dependency"]
    if importlib.util.find_spec(dependency) is None:
        return _result(dataset_name, spec, "missing_dependency", root, f"{dependency} is not importable")
    try:
        _check_loader_import(spec["class_import"])
    except Exception as exc:  # noqa: BLE001 - report import failures without masking.
        return _result(dataset_name, spec, "loader_error", root, str(exc))

    cache_path = _first_existing_cache(root, spec)
    if not cache_path.exists():
        return _result(
            dataset_name,
            spec,
            "download_required_not_approved",
            root,
            f"local cache missing at candidates {_cache_candidates(root, spec)}; download not approved",
        )
    return _result(dataset_name, spec, "available", root, None, local_cache_used=True)


def probe_all(root: str | Path = ".") -> list[LoaderProbeResult]:
    return [probe_dataset(name, root=root) for name in DATASET_PROBES]


def _check_loader_import(import_path: str) -> None:
    module_name, attr = import_path.rsplit(".", 1)
    module = __import__(module_name, fromlist=[attr])
    getattr(module, attr)


def _result(
    dataset_name: str,
    spec: dict[str, str],
    status: str,
    root: str | Path,
    error_message: str | None,
    local_cache_used: bool = False,
) -> LoaderProbeResult:
    if status not in STATUSES:
        raise ValueError(f"unknown loader status: {status}")
    cache_path = _first_existing_cache(root, spec)
    return LoaderProbeResult(
        dataset_name=dataset_name,
        loader_backend=spec["backend"],
        loader_status=status,
        cache_path=str(cache_path),
        local_cache_used=local_cache_used,
        download_attempted=False,
        error_message=error_message,
    )


def _cache_candidates(root: str | Path, spec: dict[str, str | list[str]]) -> list[str]:
    return [str(Path(root) / path) for path in spec["cache_paths"]]


def _first_existing_cache(root: str | Path, spec: dict[str, str | list[str]]) -> Path:
    candidates = [Path(path) for path in _cache_candidates(root, spec)]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]
