# Stage 3.1.6 Cora Fix Auditor Report

Date: 2026-06-26
Auditor: fresh `gcl_experiment_auditor`
Mode: subagent read-only review

## Verdict

WARN

## Blocking Issues

None. Stage 3.1.6 controlled dataset access and split generation is qualified after the Cora fix.

## Confirmed Evidence

- Cora metadata exists and is available.
- Cora split files exist for seeds 0, 1 and 2.
- Cora split type is `custom_stratified_random_1_1_8`.
- Cora / Wiki-CS / Actor split JSON files conform to schema and `split_io` integrity checks.
- `class_distribution_test` is `null` in all split JSON files.
- Download boundary remains limited to Cora / Wiki-CS / Actor.
- Data access still goes through PyG loaders.
- No unrelated data download, model training, evaluator run, GPU use, baseline clone, accuracy/loss/performance table or test-label metadata was found.

## Non-Blocking Issues

- Future official/custom split mixing risk remains. Stage 3.2 planning must prevent Cora custom, Wiki-CS official and Actor fixed split results from being placed in one directly comparable main table.
- Cora data-access provenance needed clarification because the fix report records raw GitHub endpoint fallback while the regenerated metadata was a local cache reread.
- No persistent stdout/stderr run log was found beyond command provenance in reports.

## Post-Audit Fixes Applied

- `refine-logs/EXPERIMENT_TRACKER.md` no longer contains the stale Cora blocked status.
- `dataset_metadata/stage3_1_6/Cora.json` now records `download_source="pyg_official_loader_cache_reread_after_raw_github_endpoint_fallback"`.
- `refine-logs/STAGE3_1_6_DATA_ACCESS_REPORT.md` now explains the Cora fallback and cache-reread provenance.

## Required Fixes Before Stage 3.2 Pilot Run

- Add a machine-checkable split-protocol guard during Stage 3.2 planning.
- Obtain separate approval before any training, evaluator, GPU, baseline clone, pilot run or performance claim.

## Whether Stage 3.2 Planning Is Allowed

Yes.

## Whether Stage 3.2 Pilot Run Is Allowed

No.
