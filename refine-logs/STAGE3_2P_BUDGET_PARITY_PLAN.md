# Stage 3.2P Budget Parity Plan

Date: 2026-06-26
Stage: Stage 3.2P Pilot Planning / Implementation Approval

## Goal

Future pilot results must not be explained by one objective family receiving a larger encoder, wider search space, more epochs, different evaluator, or hidden extra capacity.

## Shared Budget Fields

Future Stage 3.2E configs and raw results must record:

- shared encoder backbone;
- hidden_dim;
- projection_dim;
- pretrain_epochs or equivalent step budget;
- optimizer;
- learning rate policy;
- augmentation budget;
- mask ratio budget;
- decoder budget for GraphMAE;
- wall-clock/time logging;
- peak memory logging;
- parameter count logging.

## Method-Specific Budget Risks

### GRACE

- Record negative sampling / full-batch assumptions.
- Record contrastive temperature and projection head.
- Use the shared encoder family and hidden_dim.
- Keep augmentation budget comparable to BGRL.

### BGRL

- Record target encoder and EMA settings.
- Record online and target-state overhead separately where possible.
- Use the shared encoder family and hidden_dim.
- Keep augmentation budget comparable to GRACE.

### GraphMAE

- GraphMAE must not use a clearly larger encoder.
- Decoder architecture and decoder parameter count must be recorded separately.
- Mask ratio budget must be fixed before validation outcomes.
- If decoder capacity, pretrain objective, or reconstruction budget makes exact parity impossible, the pilot report must include `budget_mismatch_warning`.

## Search-Space Rule

Do not expand the hyperparameter search space for one method to create an advantage. Any future search budget must be listed per method before execution and audited before results are interpreted.

## Reporting Rule

If any budget cannot be made comparable, the pilot report must state the mismatch and must not make a clean objective-family superiority claim.
