# DeepXiv Fix Report

Date: 2026-06-25

## Problem

Stage 1.5 recorded DeepXiv as unavailable because the `deepxiv` CLI was missing.

## Fix

Installed the SDK into the active Python environment:

```bash
python3 -m pip install deepxiv-sdk
```

Installed version:

```text
deepxiv, version 0.3.1
```

The CLI is now available at:

```text
/root/miniconda3/bin/deepxiv
```

## Adapter Compatibility

The ARIS adapter `/root/aris_repo/tools/deepxiv_fetch.py` initially failed search with:

```text
deepxiv returned invalid JSON output
```

Cause: `deepxiv search --mode hybrid --format json` prints a deprecation notice before JSON in SDK 0.3.1. The adapter was patched to stop passing the deprecated `--mode` argument.

## Verification

The following checks passed:

```bash
deepxiv --version
python3 /root/aris_repo/tools/deepxiv_fetch.py health --json
python3 /root/aris_repo/tools/deepxiv_fetch.py search "graph contrastive learning" --max 2
python3 /root/aris_repo/tools/deepxiv_fetch.py paper-brief 2006.04131
```

Verified capabilities:

- API health check: success
- Search: success
- Paper brief: success

## Status

DeepXiv is now available for future Stage 2 / literature-retrieval use.
