# Stage 3.1 Auditor Report

Date: 2026-06-26
Auditor: fresh `gcl_experiment_auditor`
Mode: subagent read-only review

## Verdict

WARN

Stage 3.1 minimal scaffold is qualified. The auditor found no evidence of out-of-scope dataset download, model training, real pilot run, or baseline cloning. The warning is due to tracker/provenance wording and the fact that pytest was unavailable, not due to experimental leakage.

## Blocking Issues

Stage 3.1 scaffold: none.

Stage 3.2 / GPU pilot: still blocked. Required future blockers include real split JSON generation and validation, unified frozen evaluator across GRACE/BGRL/GraphMAE, budget documentation, true raw-result provenance, summary aggregation, and another auditor approval.

## Non-Blocking Issues

- `refine-logs/EXPERIMENT_TRACKER.md` had a small wording conflict: synthetic smoke was marked passed while generic smoke tests were still marked not started, and the stage still said Stage 3.0.
- Pytest was not run because it is not installed.
- Raw logger currently uses synthetic scaffold defaults such as `synthetic-config-hash` and `synthetic-commit`; real pilot readiness must replace these with real provenance.
- `schemas/split_schema.json` permits `class_distribution_test` to be object or null, but code-level split integrity correctly rejects non-null test distribution for shared split files.

## Required Fixes

Within Stage 3.1:

- Clean tracker stage and smoke-status wording.

Before Stage 3.2:

- Generate and validate real split JSON.
- Implement real loader smoke without unapproved downloads.
- Ensure true raw logger provenance: real commit, config hash, command and result path.
- Implement unified frozen evaluator and budget parity records.
- Implement and verify summary aggregation from raw JSON only.
- Complete a new auditor approval.

## Post-Audit Local Fixes Applied

- `refine-logs/EXPERIMENT_TRACKER.md` stage was updated to Stage 3.1.
- Generic `Smoke tests` was renamed to `Real-data smoke tests` so it no longer conflicts with `Synthetic smoke tests: passed`.

## Whether Stage 3.1.5 Is Allowed

Allowed, but only for real loader / split generation smoke. No training, no unapproved downloads, no GPU, no baseline cloning, no pilot.

## Whether Stage 3.2 Is Allowed

Not allowed / BLOCKED.
