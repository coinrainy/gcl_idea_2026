# Experiment Plan

Date: 2026-06-25
Scope: Stage 3 pilot planning only

## Status

This is not a formal experiment plan. It is a pilot plan derived from Stage 2B refine.

No experiment has been run.

## Goal

Run the minimum pilot needed to decide whether `GCL-I03` deserves further development.

## Main Pilot Question

Can label-free graph-regime metrics predict objective-family ranking under a matched node-classification protocol?

## Methods To Compare

Required:

- one negative-based GCL method: GRACE or GCA;
- one negative-free/bootstrap method: BGRL or AFGRL;
- one masked graph modeling method: GraphMAE or GraphMAE2.

Optional:

- ProGCL only as an I02 audit reference;
- MaskGAE only if edge reconstruction is needed for a selected graph.

## Pilot Dataset Grid

Use four datasets maximum in the first pilot:

| Regime | Candidate datasets | Purpose |
| --- | --- | --- |
| Homophilic citation | Cora, PubMed | simple protocol sanity and classic GCL setting |
| Homophilic larger or wiki | Wiki-CS, Coauthor-CS | check whether signal survives beyond Planetoid |
| Heterophilic small | Actor, Chameleon | test objective boundary under low homophily |
| Heterophilic or mixed | Squirrel, Texas, Cornell, Penn94 | test boundary stability |

## Protocol Controls

- Save split JSON files before running.
- Use pilot seeds `0,1,2`.
- Use same encoder family and hidden dimension where possible.
- Use frozen encoder plus linear evaluator for all SSL methods.
- Use same evaluator early stopping rule.
- Use comparable pretraining epochs and compute budget.
- Log raw result JSON files.
- Mark every run as `pilot`.

## Metric Collection

Before labels:

- compute label-free graph-regime metrics listed in `docs/metric_leakage_audit_stage2b.md`;
- freeze these metrics before looking at validation ranking.

After training/evaluation:

- compute validation objective ranking;
- compute label-audit metrics only on train/validation labels;
- compute I02 negative-validity audit only on train/validation labeled node pairs.

## Analysis Plan

1. Rank objective families per dataset by validation accuracy under matched protocol.
2. Fit or manually assess a low-complexity rule from label-free metrics to objective-family winner.
3. Compare against chance, dataset-ID baseline and simple feature-dimension/graph-size baselines.
4. Inspect whether label-audit metrics explain failure cases.
5. Decide GO/REVISE/PIVOT/KILL before any formal experiment.

## Success Gate

Proceed only if:

- label-free metrics predict objective family on most pilot datasets;
- objective differences are not artifacts of budget, capacity or evaluator mismatch;
- label-audit metrics support interpretation but are not necessary for prediction.

## Kill Gate

Kill if:

- prediction fails;
- prediction requires labels;
- objective differences vanish under protocol matching;
- I02 audit is random or redundant;
- closest work invalidates the diagnostic novelty.

## Formal Experiment Boundary

Formal experiments require a separate future gate:

- `BENCHMARK_PROTOCOL.md` status must become `Frozen`;
- baseline reproduction must be credible;
- 10-seed runs must be planned;
- summary scripts must derive tables from raw JSON/CSV;
- claim matrix must be updated after pilot.
