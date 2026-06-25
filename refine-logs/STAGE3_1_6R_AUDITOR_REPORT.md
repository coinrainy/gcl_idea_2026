# Stage 3.1.6R Auditor Report

Date: 2026-06-26
Auditor: fresh `gcl_experiment_auditor`
Mode: subagent read-only review

## Verdict

WARN.

## Whether Previous Cora Inconsistency Is Resolved

Yes.

The previous Stage 3.1.6 auditor report preserved the historical judgment that Cora did not have actual split files. Current artifacts and Stage 3.1.6R recheck reports show that `splits/Cora/split_seed_{0,1,2}.json` exist, pass schema validation, pass `read_split` integrity validation, use `split_type=custom_stratified_random_1_1_8`, and keep `class_distribution_test=null`.

## Audit Checklist

| Check | Auditor conclusion |
| --- | --- |
| Cora split JSON exists | PASS |
| Cora split JSON passes schema and integrity | PASS |
| Wiki-CS split JSON exists | PASS |
| Actor split JSON exists | PASS |
| all split `class_distribution_test` values are null | PASS |
| Cora split type is `custom_stratified_random_1_1_8` | PASS |
| Wiki-CS split type is `official_wikics` | PASS |
| Actor split type is `heterophily_fixed` | PASS |
| metadata excludes test label distribution | PASS |
| only Cora / Wiki-CS / Actor were read/downloaded | PASS |
| access uses PyG loaders | PASS |
| unrelated data download found | no |
| model training found | no |
| evaluator run found | no |
| GPU use found | no |
| baseline clone found | no |
| accuracy / loss / performance table found | no |
| future official/custom split mixing risk | WARN |
| Stage 3.2 planning | allowed |
| direct Stage 3.2 pilot run | not allowed |

## Blocking Issues

None for Stage 3.1.6R reconciliation.

## Non-Blocking Issues

- The old `refine-logs/STAGE3_1_6_AUDITOR_REPORT.md` still contains the historical Cora split-missing finding and must be treated as superseded by this report for the Cora artifact status.
- Cora custom split, Wiki-CS official split, and Actor fixed split still create a future comparison-risk if mixed in one directly comparable main table.
- Current split coverage is seeds 0, 1, 2 only. This is sufficient for Stage 3.2 planning / pilot preparation, but not sufficient for formal results under the benchmark protocol.
- Stage 3.1.6R artifacts must be committed before any later GPU deployment or pilot approval uses them as provenance.

## Required Fixes

- Add a correction note to `refine-logs/STAGE3_1_6_AUDITOR_REPORT.md` pointing to this Stage 3.1.6R auditor report.
- Keep Stage 3.2 pilot execution blocked until a separate approval and run manifest exist.
- Preserve the split-policy warning: do not put Cora custom, Wiki-CS official, and Actor fixed split results in one directly comparable main table.
- Formal experiments still require the protocol's 10-seed formal setup, baseline readiness, fair search budget, and automatic result aggregation.

## Whether Stage 3.2 Planning Is Allowed

Yes.

## Whether Stage 3.2 Pilot Run Is Allowed

No.
