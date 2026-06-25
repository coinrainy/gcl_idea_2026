# Stage 2B Pilot Plan

Date: 2026-06-25
Status: planned only
Experiment label: `pilot`

## Objective

Falsify the refined `GCL-I03` thesis before any formal experiment:

Can label-free graph-regime metrics predict which graph SSL objective family performs best under an identical node-classification protocol?

## Non-Goals

- Do not claim SOTA.
- Do not write paper tables.
- Do not tune on test labels.
- Do not run 10-seed formal experiments.
- Do not add a new loss unless the diagnostic survives pilot.
- Do not promote `GCL-I02` into a hard-negative reweighting method during this pilot.

## Pilot Dataset Set

Use a small, diverse pilot set:

- homophilic citation graph: Cora or PubMed;
- homophilic/coauthor or wiki-style graph: Wiki-CS or Coauthor-CS if convenient;
- heterophilic graph: Actor or Chameleon;
- heterophilic or mixed-regime graph: Squirrel, Texas, Cornell, Penn94 or a comparable fixed-split benchmark.

Final selection should prefer datasets with easy local loading and known split conventions. If a dataset lacks official splits, save pilot split JSON files before any run.

## Pilot Methods

Minimum objective families:

- negative-based contrastive: GRACE or GCA;
- bootstrap/negative-free: BGRL or AFGRL;
- masked graph modeling: GraphMAE or GraphMAE2.

Optional only if budget permits:

- ProGCL as a contrastive hard-negative reference for the I02 audit;
- MaskGAE if edge reconstruction is central to the selected dataset.

## Matched Protocol

All pilot methods must use:

- same dataset preprocessing;
- same pilot split files;
- same pilot seed list, suggested `0,1,2`;
- same encoder family and hidden dimension where possible;
- same frozen encoder plus linear evaluator;
- comparable pretraining budget;
- same early stopping rule for evaluator;
- raw JSON logging before summary tables.

Pilot results must be stored with `status: pilot`.

## Label-Free Regime Metrics

Compute before downstream label use:

- edge feature similarity mean and variance;
- one-hop and two-hop feature-neighborhood smoothness;
- degree skew and degree entropy;
- clustering coefficient and connected component statistics;
- structural role entropy from local degree/triangle/ego features;
- fixed masked-feature reconstruction difficulty;
- fixed edge/path reconstruction difficulty if available;
- augmentation stability under a fixed perturbation budget;
- representation rank, variance and uniformity proxies without labels.

These metrics may be used to predict objective-family ranking.

## Label-Audit Metrics

Use only train/validation labels and only after pre-registering the pilot:

- train/validation label homophily;
- train/validation feature-label predictability;
- validation objective ranking under frozen linear evaluator;
- validation-only negative-pair label agreement for I02 audit;
- validation-only ambiguous-pair precision and recall for predicted harmful negatives.

Label-audit metrics must not enter training or selector inputs.

## Pilot Decision Tests

Primary test:

- label-free metrics should predict the best objective family across pilot datasets better than chance and better than a trivial dataset-size or feature-dimension baseline.

Secondary tests:

- predicted masked-model wins should align with high reconstruction signal and stable feature-neighborhood structure;
- predicted contrastive wins should align with stable augmentations and lower negative ambiguity;
- predicted bootstrap wins should align with settings where negative pairs are unreliable but representation collapse diagnostics remain healthy;
- I02 audit should explain contrastive failures without becoming a training component.

## Minimal Success Condition

Proceed beyond pilot only if:

- at least three of four pilot datasets show objective ranking patterns consistent with label-free regime metrics;
- results are not dominated by runtime budget, parameter count or implementation instability;
- label-audit metrics support the interpretation without being necessary for prediction;
- I02 audit adds explanation for contrastive failures on at least one dataset without duplicating ProGCL-style weights.

## Direct Kill Conditions

Kill the active idea if:

- objective ranking is unrelated to label-free metrics;
- label-free metrics only work after adding label-audit information;
- method ranking flips arbitrarily across pilot seeds;
- matched-protocol differences are too small to analyze;
- the pilot winner is explained by extra capacity, extra epochs or evaluator mismatch;
- I02 audit is random, redundant with ProGCL, or requires validation labels for training;
- a direct closest work already makes the same protocol-aligned label-free objective-selection claim.

## Pilot Output Expected Later

When the pilot is actually run, produce:

- raw result JSON files;
- split JSON files;
- a pilot-only summary table;
- a metric-prediction table;
- an I02 audit table;
- a GO/REVISE/PIVOT/KILL decision.

This plan does not run the pilot.
