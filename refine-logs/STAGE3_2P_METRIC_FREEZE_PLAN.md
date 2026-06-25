# Stage 3.2P Metric Freeze And Label-Audit Plan

Date: 2026-06-26
Stage: Stage 3.2P Pilot Planning / Implementation Approval

## Source Policy

This plan follows `docs/metric_interface_stage3.md` and `schemas/metric_schema.json`.

Stage 3.2P does not compute real metrics.

## Future Stage 3.2E Order

Future Stage 3.2E must:

1. compute label-free regime metrics first;
2. save a label-free artifact;
3. compute `freeze_hash`;
4. freeze the label-free artifact before evaluator runs;
5. run method pretraining and unified evaluator only after freeze;
6. save label-audit metrics separately;
7. ensure selector reads only the label-free artifact;
8. set label-audit artifact `selector_visible=false`;
9. never compute test label metrics;
10. treat validation objective ranking only as pilot outcome, not selector input.

## Selector-Visible Artifact

Allowed selector-visible artifact:

```text
artifact_type: label_free_regime_metrics
selector_visible: true
metric_freeze_status: frozen_before_validation_outcome
```

The selector loader must verify `freeze_hash` before analysis.

## Label-Audit Artifact

Label-audit artifacts may use train/validation labels only and must be:

```text
artifact_type: label_audit_metrics
selector_visible: false
```

They may explain failures but must not drive training, objective choice, metric redesign, hyperparameter tuning, or survival decisions.

## Prohibited

- test label homophily;
- test feature-label predictability;
- test objective ranking;
- any metric computed after looking at test accuracy for survival decisions.
