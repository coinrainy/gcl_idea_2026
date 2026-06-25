from gcl_diag.data.loader_probe import probe_dataset


def test_probe_does_not_download(tmp_path) -> None:
    result = probe_dataset("Cora", root=tmp_path)
    assert result.download_attempted is False
    assert result.loader_status in {
        "missing_dependency",
        "local_cache_missing",
        "loader_error",
        "download_required_not_approved",
        "available",
    }
