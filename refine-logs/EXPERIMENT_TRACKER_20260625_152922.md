# Experiment Tracker

Date: 2026-06-25
Stage: Stage 2B

No experiments have been run.

## Planned Pilot Runs

| Run ID | Status | Dataset | Regime | Method family | Method | Seeds | Purpose | Decision use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P-I03-01 | planned | Cora or PubMed | homophilic citation | negative-based GCL | GRACE or GCA | 0,1,2 | contrastive baseline under matched protocol | validation ranking only |
| P-I03-02 | planned | Cora or PubMed | homophilic citation | bootstrap | BGRL or AFGRL | 0,1,2 | negative-free comparison | validation ranking only |
| P-I03-03 | planned | Cora or PubMed | homophilic citation | masked graph modeling | GraphMAE or GraphMAE2 | 0,1,2 | MGM comparison | validation ranking only |
| P-I03-04 | planned | Wiki-CS or Coauthor-CS | homophilic larger/wiki | all three families | TBD | 0,1,2 | check non-Planetoid stability | validation ranking only |
| P-I03-05 | planned | Actor or Chameleon | heterophilic | all three families | TBD | 0,1,2 | heterophily boundary | validation ranking only |
| P-I03-06 | planned | Squirrel/Texas/Cornell/Penn94 | heterophilic or mixed | all three families | TBD | 0,1,2 | boundary robustness | validation ranking only |
| P-I02-AUDIT | planned | same as P-I03 datasets | audit | ProGCL reference if available | ProGCL optional | 0,1,2 | negative-validity audit only | explanation, not selector |

## Required Pre-Run Artifacts

| Artifact | Status |
| --- | --- |
| Pilot split JSON files | not started |
| Config templates | not started |
| Raw JSON logging schema | not started |
| Metric extraction script | not started |
| Pilot summary script | not started |
| Kill-condition checklist | specified in Stage 2B docs |

## Rules

- All runs must be labeled `pilot`.
- Failed runs must be kept.
- Test labels must not decide any pilot choice.
- Pilot results must not enter paper main tables.
- Any move to formal experiments requires a separate decision.
