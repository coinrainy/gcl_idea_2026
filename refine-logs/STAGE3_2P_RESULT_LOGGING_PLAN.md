# Stage 3.2P Raw Result And Summary Aggregation Plan

Date: 2026-06-26
Stage: Stage 3.2P Pilot Planning / Implementation Approval

## Future Raw Result Rule

Every future Stage 3.2E run must write one raw JSON file conforming to `schemas/raw_result_schema.json`.

Failed runs must also write raw JSON with:

```text
status: fail
failure_reason: non-empty
test_at_best: null
final_test: null
```

## Fixed Future Paths

```text
results/raw/pilot/{dataset}/{method}/{run_id}.json
results/summary/pilot/
results/metrics/pilot/
```

Stage 3.2P must not create these real result files.

## Summary Aggregation Rule

- Summary scripts may read only raw JSON files.
- No manual copying of best numbers is allowed.
- Pilot summary and formal summary must be separate.
- Pilot summary must not enter a paper main table.
- Pilot summaries must keep `pilot` status visible and must not support SOTA, robustness, or formal claims.

## Required Raw Result Provenance

Each future raw JSON must include at minimum:

- `run_id`;
- `stage=pilot`;
- `method`;
- `objective_family`;
- `dataset`;
- `split_type`;
- `split_file`;
- `split_seed`;
- `model_seed`;
- `config_path`;
- `config_hash`;
- `run_command`;
- `commit_hash`;
- evaluator fields;
- backbone / hidden_dim / projection_dim / budget fields;
- `training_time_sec`;
- `peak_memory_mb`;
- `result_file_path`;
- `log_path`.

## Stage 3.2P Boundary

This plan creates no `results/` artifacts and no performance table.
