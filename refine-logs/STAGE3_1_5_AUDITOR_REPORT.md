# Stage 3.1.5 Auditor Report

Date: 2026-06-26
Auditor: fresh `gcl_experiment_auditor`
Mode: subagent read-only review

## Verdict

BLOCKED

The auditor found no evidence of automatic download, model training, evaluator run, GPU use, baseline cloning, or fabricated result numbers. However, Stage 3.1.5 did not complete the core real loader / split generation smoke because Cora, Wiki-CS and Actor all lack local caches and no real split JSON was written or validated.

## Blocking Issues

- Cora, Wiki-CS and Actor are all `download_required_not_approved`.
- No real split JSON was written.
- No split JSON was validated.
- Stage 3.2 planning and pilot run are not allowed.

## Non-Blocking Issues

- `split_schema.json` still allowed `class_distribution_test` to be object or null, although code rejected non-null values.
- The future Cora split branch used deterministic index rotation rather than true stratified random splitting.
- The Stage 3.1.5 report needed explicit loader/split smoke command provenance.

## Post-Audit Fixes Applied

- `schemas/split_schema.json` now requires `class_distribution_test` to be `null`.
- `docs/split_schema_explanation.md` now states that `class_distribution_test` must be `null` in schema.
- `scripts/run_stage3_1_5_split_smoke.py` no longer writes placeholder Cora splits and instead blocks Cora split generation until labels can be safely read from approved local cache.
- `refine-logs/STAGE3_1_5_REPORT.md` now records the loader/split smoke commands and schema-validation command.

## Required Fixes

- Explicitly approve controlled downloads or provide local Cora / Wiki-CS / Actor cache paths.
- Rerun Stage 3.1.5 after data access is resolved.
- Generate and validate real split JSON with explicit `split_type` and `class_distribution_test=null`.
- Keep official and custom splits separated.
- Complete a new independent auditor review before Stage 3.2 planning or pilot execution.

## Whether Stage 3.2 Planning Is Allowed

No.

## Whether Stage 3.2 Pilot Run Is Allowed

No.
