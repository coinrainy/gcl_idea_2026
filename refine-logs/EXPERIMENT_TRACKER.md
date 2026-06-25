# Experiment Tracker

Date: 2026-06-26
Stage: Stage 3.1

No experiments have been run.

## Planned Pilot Runs

| Run ID | Status | Dataset | Regime | Method family | Method | Seeds | Purpose | Decision use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P-I03-01 | not started | Cora | homophilic citation | negative-based GCL | GRACE | 0,1,2 | future contrastive baseline under matched protocol | validation ranking only |
| P-I03-02 | not started | Cora | homophilic citation | bootstrap | BGRL | 0,1,2 | future negative-free comparison | validation ranking only |
| P-I03-03 | not started | Cora | homophilic citation | masked graph modeling | GraphMAE | 0,1,2 | future MGM comparison | validation ranking only |
| P-I03-04 | not started | Wiki-CS | non-Planetoid homophilic | all three families | GRACE/BGRL/GraphMAE | 0,1,2 | future non-citation check | validation ranking only |
| P-I03-05 | not started | Actor | heterophilic | all three families | GRACE/BGRL/GraphMAE | 0,1,2 | future heterophily boundary check | validation ranking only |
| P-I02-AUDIT | not started | same as P-I03 datasets | audit | ProGCL reference if available | ProGCL optional | 0,1,2 | future negative-validity audit only | explanation, not selector |

## Required Pre-Run Artifacts

| Artifact | Status |
| --- | --- |
| Pilot split JSON schema | drafted |
| Raw JSON logging schema | drafted |
| Metric schema | drafted |
| Metric interface | drafted |
| Pilot manifest draft | drafted |
| Pilot engineering plan | drafted |
| Pilot dataset selection | ready_for_audit |
| Pilot method selection | ready_for_audit |
| Stage 3.0 auditor report | drafted |
| Stage 3.0 readiness report | drafted |
| Schema validators | implemented |
| Synthetic split fixture | implemented |
| Split integrity checker | implemented |
| Raw result logger | implemented |
| Metric artifact writer | implemented |
| Frozen evaluator dry-run | implemented |
| Method interfaces | scaffolded |
| Config skeletons | drafted |
| Synthetic smoke tests | passed |
| Pytest smoke tests | skipped: pytest not installed |
| Actual split JSON files | not started |
| Config templates | not started |
| Metric extraction script | not started |
| Pilot summary script | not started |
| Real dataset loaders | not started |
| Real loader probe | partial: dependencies found, local caches missing |
| Dataset metadata schema | drafted |
| Dataset metadata writer | implemented |
| Dataset metadata files | written |
| Real split generation smoke | failed: no local dataset cache |
| Validated split JSON files | not written |
| Training scripts | not started |
| Real-data smoke tests | not started |
| Pilot runs | not started |
| Stage 3.2 | blocked |
| Stage 3.1.5 auditor report | blocked |
| Kill-condition checklist | specified in Stage 2B docs |

## Rules

- All runs must be labeled `pilot`.
- Failed runs must be kept.
- Test labels must not decide any pilot choice.
- Pilot results must not enter paper main tables.
- Any move to formal experiments requires a separate decision.
