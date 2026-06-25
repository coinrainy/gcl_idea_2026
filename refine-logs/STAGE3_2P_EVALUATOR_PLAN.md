# Stage 3.2P Evaluator Plan

Date: 2026-06-26
Stage: Stage 3.2P Pilot Planning / Implementation Approval

## Current Evaluator Status

`src/gcl_diag/eval/frozen_linear.py` is still a synthetic-only dry-run scaffold. It uses a deterministic nearest-centroid shape check on synthetic embeddings and is not a real frozen linear evaluator for GCL methods.

Stage 3.2E must implement a real frozen linear evaluator and pass a new auditor review before any pilot execution.

## Unified Evaluator Rule

All SSL methods must output frozen embeddings. The downstream evaluator must be the same project unified frozen linear evaluator for GRACE, BGRL, and GraphMAE.

GraphMAE official evaluator must not be substituted for the project evaluator.

## Data Use Rules

- Evaluator training uses train indices only.
- Early stopping uses validation only.
- `test_at_best` is logged only for later audit and must not choose hyperparameters, checkpoint, epoch, objective family, augmentation strength, or survival decision.
- Failed evaluator or method runs still write raw result records with `status=fail`.

## Required Evaluator Fields

Every future raw result must record:

- `evaluator_seed`;
- `max_epochs`;
- `patience`;
- `early_stopping_metric`;
- `valid_at_best`;
- `test_at_best`;
- `final_valid`;
- `final_test`.

The output must conform to `schemas/raw_result_schema.json`.

## Stage 3.2P Boundary

Stage 3.2P does not implement the real evaluator and does not run the existing synthetic evaluator. This document only defines the required evaluator plan for a later Stage 3.2E request.
