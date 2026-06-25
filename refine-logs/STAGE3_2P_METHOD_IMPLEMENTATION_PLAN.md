# Stage 3.2P Method Implementation Plan

Date: 2026-06-26
Stage: Stage 3.2P Pilot Planning / Implementation Approval

## Current Code Status

`src/gcl_diag/methods/{grace,bgrl,graphmae}.py` currently contains Stage 3.1 placeholders only. `build_model()`, `pretrain()`, and `encode()` raise `NotImplementedError`. Stage 3.2P does not replace these placeholders.

## 4.1 Unified Principles

All future minimal method implementations must share:

- dataset loader;
- split reader;
- encoder family;
- hidden_dim;
- frozen linear evaluator;
- raw result logger;
- metric artifact writer;
- config format;
- run manifest;
- budget policy.

All methods must output frozen node embeddings for the same downstream evaluator.

## 4.2 GRACE Minimal Implementation Plan

Required metadata:

```text
objective_family: negative_based_contrastive
uses_negatives: true
requires_decoder: false
uses_target_encoder: false
augmentation: edge drop + feature mask
output: frozen node embeddings
evaluator: project unified frozen linear evaluator
```

Implementation checklist for a later Stage 3.2E request:

- implement a shared GNN encoder backbone;
- implement two-view edge drop + feature mask with fixed augmentation budget;
- implement negative-based contrastive objective with recorded temperature and sampling assumptions;
- save frozen node embeddings after pretraining;
- pass embeddings only to the unified project evaluator;
- record pretrain budget, parameter count, wall-clock time, peak memory, and raw result provenance.

## 4.3 BGRL Minimal Implementation Plan

Required metadata:

```text
objective_family: bootstrap_negative_free
uses_negatives: false
requires_decoder: false
uses_target_encoder: true
augmentation: edge drop + feature mask
output: frozen node embeddings
evaluator: project unified frozen linear evaluator
```

Implementation checklist for a later Stage 3.2E request:

- implement the same shared encoder backbone as GRACE;
- implement online / target encoder structure;
- record target encoder and EMA settings;
- use the same augmentation budget family as GRACE unless explicitly justified;
- save frozen online encoder node embeddings;
- pass embeddings only to the unified project evaluator;
- record pretrain budget, parameter count including target-state overhead, wall-clock time, peak memory, and raw result provenance.

## 4.4 GraphMAE Minimal Implementation Plan

Required metadata:

```text
objective_family: masked_graph_modeling
uses_negatives: false
requires_decoder: true
uses_target_encoder: false
augmentation: feature mask / attribute mask
output: frozen encoder embeddings
evaluator: project unified frozen linear evaluator
```

Implementation checklist for a later Stage 3.2E request:

- implement the same shared encoder backbone as GRACE / BGRL;
- implement attribute masking with fixed mask-ratio budget;
- implement decoder only for reconstruction during pretraining;
- save frozen encoder node embeddings, not decoder outputs;
- pass embeddings only to the unified project evaluator;
- record decoder architecture, decoder parameter count, mask ratio, pretrain budget, wall-clock time, peak memory, and raw result provenance.

GraphMAE official evaluator must not be used directly. GraphMAE decoder / budget / hidden_dim must be recorded in raw results. If GraphMAE uses extra decoder parameters, the budget parity report must disclose this and mark `budget_mismatch_warning` if the difference cannot be neutralized.

## 4.5 Explicitly Excluded From Stage 3.2 First Pilot

The first Stage 3.2 pilot plan must not introduce:

- ProGCL;
- GCA;
- AFGRL;
- GraphMAE2;
- LLM signal;
- new loss;
- hard-negative reweighting;
- MGM+GCL hybrid objective.

These may be future extensions or audit references only after separate approval. They are not part of Stage 3.2 first pilot.
