# Metric Leakage Audit for Stage 2B

Date: 2026-06-25

## Purpose

Separate metrics that may drive the `GCL-I03` selector from metrics that may only audit or interpret results.

## Label-Free Regime Metrics

These metrics may be computed before label use and may be selector inputs in the Stage 3 pilot:

| Metric | Label use | Intended role | Leakage risk |
| --- | --- | --- | --- |
| Edge feature similarity | none | estimate local semantic smoothness proxy | low |
| One-hop feature-neighborhood smoothness | none | detect whether local aggregation preserves features | low |
| Two-hop feature-neighborhood smoothness | none | detect broader smoothing regime | low |
| Degree skew and entropy | none | identify hub/long-tail structure | low |
| Clustering coefficient | none | identify local closure | low |
| Connected component statistics | none | detect disconnected or sparse regimes | low |
| Structural role entropy | none | detect role-similarity ambiguity | low |
| Fixed masked-feature reconstruction difficulty | none | estimate MGM suitability | low |
| Fixed edge/path reconstruction difficulty | none | estimate structure reconstruction signal | low |
| Augmentation stability under fixed budget | none | estimate GCL view validity | low |
| Label-free embedding rank/variance/uniformity proxies | none | collapse/smoothing diagnostics | low |

## Label-Audit Metrics

These metrics must not be selector inputs, training losses, hyperparameter signals, or survival criteria by themselves:

| Metric | Allowed labels | Intended role | Leakage rule |
| --- | --- | --- | --- |
| Label homophily | train/validation only | interpret graph regime | audit only |
| Feature-label predictability | train/validation only | interpret whether labels align with features | audit only |
| Validation objective ranking | validation only | pilot outcome measurement | not a selector input |
| Negative-pair label agreement | train/validation only | I02 false-negative audit | audit only |
| Ambiguous-pair precision/recall | train/validation only | explain contrastive failure | audit only |

## Prohibited Metrics

- Any metric using test labels.
- Any metric using validation labels inside pretraining.
- Any metric that changes objective choice after looking at test performance.
- Any LLM/TAG pseudo-label signal unless a separate leakage model is written first.

## Refine Correction

Stage 2A listed feature-label predictability and edge homophily as possible regime metrics. Stage 2B corrects this:

- feature-label predictability is label-audit only;
- label homophily is label-audit only;
- feature homophily and feature-neighborhood smoothness are label-free proxies and may be selector inputs.

## Audit Verdict

The Stage 2B proposal is acceptable only if the selector uses label-free metrics. If the pilot succeeds only with label-audit metrics, the active idea should be killed or rewritten as a purely retrospective analysis.
