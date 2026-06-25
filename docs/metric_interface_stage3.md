# Metric Interface for Stage 3

Date: 2026-06-25

## Purpose

This interface separates selector-eligible label-free metrics from audit-only label metrics. It is designed for future Stage 3.1 implementation and Stage 3.2 pilot runs. Stage 3.0 does not compute metrics.

## Save Format

Future metric files should follow `schemas/metric_schema.json`. Label-free and label-audit metrics must be saved as separate artifacts:

```text
results/metrics/pilot/{dataset}/split_seed_{seed}_label_free.json
results/metrics/pilot/{dataset}/split_seed_{seed}_label_audit.json
```

## Freeze Rule

Label-free metrics must be computed and frozen before validation objective ranking is inspected. A metric file is selector-eligible only when:

```text
metric_freeze_status: frozen_before_validation_outcome
artifact_type: label_free_regime_metrics
selector_visible: true
```

Any metric changed after looking at validation or test outcomes must be marked invalid for selector use. Label-audit files must have `selector_visible: false` and must not overwrite or replace the frozen label-free file. Stage 3.1 implementation should verify the `freeze_hash` of the label-free file before selector analysis.

## Label-Free Regime Metrics

| metric | when computed | uses labels | selector input allowed | leakage risk | notes |
| --- | --- | --- | --- | --- | --- |
| edge_feature_similarity_mean | before training | no | yes | low | feature similarity over graph edges |
| edge_feature_similarity_std | before training | no | yes | low | dispersion of edge feature similarity |
| one_hop_feature_smoothness | before training | no | yes | low | feature-neighborhood consistency |
| two_hop_feature_smoothness | before training | no | yes | low | broader smoothing proxy |
| degree_skew | before training | no | yes | low | structural regime |
| degree_entropy | before training | no | yes | low | degree diversity |
| clustering_coefficient_mean | before training | no | yes | low | local closure |
| connected_component_count | before training | no | yes | low | graph fragmentation |
| structural_role_entropy | before training | no | yes | medium-low | must use topology/features only |
| masked_feature_reconstruction_difficulty | before validation outcome | no | yes | medium | probe must be fixed before outcome |
| edge_reconstruction_difficulty | before validation outcome | no | yes | medium | probe must be fixed before outcome |
| augmentation_stability_score | before validation outcome | no | yes | medium | perturbation budget must be fixed |
| embedding_rank_proxy | after unsupervised pretraining, before labels | no | yes | medium | cannot depend on evaluator labels |
| embedding_variance_proxy | after unsupervised pretraining, before labels | no | yes | medium | collapse diagnostic |
| uniformity_proxy | after unsupervised pretraining, before labels | no | yes | medium | label-free representation geometry |

## Label-Audit Metrics

These metrics may explain results but must not be selector inputs, training losses, tuning signals, or survival criteria by themselves.

| metric | when computed | allowed labels | selector input allowed | leakage risk | notes |
| --- | --- | --- | --- | --- | --- |
| train_val_label_homophily | after split creation | train/validation only | no | high if misused | audit-only regime interpretation |
| train_val_feature_label_predictability | after split creation | train/validation only | no | high if misused | audit-only |
| validation_objective_ranking | after evaluator runs | validation only | no | high if used to redesign selector | pilot outcome measurement |
| negative_pair_label_agreement | after split creation | train/validation only | no | high if used in training | I02 audit only |
| ambiguous_pair_precision | after split creation | train/validation only | no | high if used in training | I02 audit only |
| ambiguous_pair_recall | after split creation | train/validation only | no | high if used in training | I02 audit only |

## Prohibited Metrics

The following must not be computed for selector, tuning or survival decisions:

- `test_label_homophily`
- `test_feature_label_predictability`
- `test_objective_ranking`
- any metric computed after looking at test accuracy for survival decision

## Pilot Use

Future pilot analysis should:

1. compute label-free metrics;
2. save metric JSON with `metric_freeze_status: frozen_before_validation_outcome`;
3. compute and store a `freeze_hash`;
4. run methods and frozen evaluator;
5. compute validation ranking;
6. save label-audit metrics to a separate `selector_visible: false` artifact;
7. use label-audit metrics only to explain failures;
8. write GO / REVISE / PIVOT / KILL without test-label tuning.
