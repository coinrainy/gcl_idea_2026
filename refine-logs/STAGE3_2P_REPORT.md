# Stage 3.2P Report

Date: 2026-06-26
Stage: Stage 3.2P Pilot Planning / Implementation Approval

## 1. Scope

This stage only completed pilot planning / implementation approval. It did not train models, run an evaluator, run a pilot, use GPU, clone baselines, generate accuracy / loss / performance tables, perform objective-family ranking, make a survival decision, or enter Stage 3.2 execution.

## 2. Data / Split Readiness

Data and split readiness: PASS.

Metadata exists and validates for Cora, Wiki-CS, and Actor. Split files exist for seeds 0, 1, and 2 for all three datasets. All split files pass `schemas/split_schema.json` and `read_split` integrity checks, and all set `class_distribution_test=null`.

Split protocols:

- Cora: `custom_stratified_random_1_1_8`;
- Wiki-CS: `official_wikics`;
- Actor: `heterophily_fixed`.

Future results may compare methods within each dataset only. Cora custom, Wiki-CS official, and Actor fixed splits must not be placed into one directly comparable main table.

## 3. Pilot Scope

Future planned pilot scope:

- datasets: Cora, Wiki-CS, Actor;
- methods: GRACE, BGRL, GraphMAE;
- seeds: 0, 1, 2;
- total future planned runs: 27.

The pilot remains `pilot`, not formal. It cannot support SOTA, robustness, paper main-table, formal, or survival claims.

## 4. Method Implementation Plan

Stage 3.2P records minimal future implementation plans for:

- GRACE: negative-based contrastive, edge drop + feature mask, no decoder, no target encoder;
- BGRL: bootstrap negative-free, edge drop + feature mask, target encoder / EMA required;
- GraphMAE: masked graph modeling, feature / attribute mask, decoder required.

All methods must share dataset loader, split reader, encoder family, hidden_dim, frozen linear evaluator, raw result logger, metric artifact writer, config format, run manifest, and budget policy.

Excluded from the first Stage 3.2 pilot: ProGCL, GCA, AFGRL, GraphMAE2, LLM signal, new loss, hard-negative reweighting, and MGM+GCL hybrid objective.

## 5. Evaluator Plan

All SSL methods must output frozen embeddings and use the same project unified frozen linear evaluator. Evaluator training uses train indices only, early stopping uses validation only, and `test_at_best` is audit-only.

Current status: `src/gcl_diag/eval/frozen_linear.py` is still synthetic-only dry-run. Stage 3.2E must implement a real frozen linear evaluator and receive a fresh auditor review before pilot execution.

## 6. Budget Parity Plan

Future pilot configs and raw results must record shared encoder backbone, hidden_dim, projection_dim, pretrain budget, optimizer, learning rate policy, augmentation budget, mask ratio budget, GraphMAE decoder budget, wall-clock time, peak memory, and parameter counts.

GraphMAE cannot use a clearly larger encoder. Its decoder parameters must be recorded separately. BGRL target encoder / EMA state must be recorded. GRACE negative sampling / batch assumptions must be recorded. Any unavoidable mismatch must be marked with `budget_mismatch_warning`.

## 7. Metric Freeze Plan

Future Stage 3.2E must compute label-free regime metrics first, save selector-visible label-free artifacts, compute and verify `freeze_hash`, then run evaluator. Label-audit metrics must be saved separately with `selector_visible=false`. Test label metrics are prohibited.

Validation objective ranking is a pilot outcome only, not a selector input.

## 8. Result Logging Plan

Future Stage 3.2E must write one raw JSON per run under:

```text
results/raw/pilot/{dataset}/{method}/{run_id}.json
```

Failed runs must also write raw JSON. Summary scripts may read only raw JSON and must not manually copy best numbers. Pilot summaries and formal summaries must remain separate.

Stage 3.2P created no `results/` files.

## 9. Run Manifest Draft

`refine-logs/STAGE3_2P_RUN_MANIFEST_DRAFT.yaml` is draft-only and has:

```text
execution_allowed: false
```

It contains no real training command.

## 10. Execution Gate

Direct pilot execution remains blocked until all gate items are satisfied, including real method implementations, real evaluator, evaluator smoke, metric freeze implementation, raw logger integration, completed configs, reviewed manifest, reviewed budget parity, clean worktree, fresh auditor approval, explicit user request, and independent GO review.

## 11. Auditor Verdict

Fresh `gcl_experiment_auditor` verdict: WARN.

No Stage 3.2P planning blocking issue was found.

## 12. Blocking Issues

For Stage 3.2P planning: none.

For direct pilot execution: still blocked because current method code is placeholder-only, evaluator is synthetic-only, and the manifest is draft-only.

## 13. Non-Blocking Issues

- Current pilot scope uses seeds 0, 1, 2 only and cannot support formal claims.
- Stage 3.2E still needs concrete preprocessing/config freeze.
- Stage 3.2P artifacts must be committed before later use as provenance.

## 14. Whether Stage 3.2E Is Allowed

Allowed with WARN for implementation / execution preparation only.

This does not authorize real pilot execution.

## 15. Whether Direct Pilot Run Is Allowed

No. Direct Stage 3.2 pilot run remains blocked.

## 16. Next Step Recommendation

If explicitly requested later, proceed to Stage 3.2E implementation / execution preparation: implement real GRACE / BGRL / GraphMAE minimal code, real unified evaluator, metric freeze, raw logging integration, configs, and summary scripts, then submit that package to a fresh auditor before any pilot run.

## Stage 3.2P Verdict

GO.

Rationale: planning is complete, fresh auditor found no Stage 3.2P planning blocking issue, Stage 3.2E implementation / execution preparation is allowed with WARN, and direct pilot execution remains blocked.
