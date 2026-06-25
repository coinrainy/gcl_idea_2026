# Kill Arguments for Stage 2B

Date: 2026-06-25

## Strongest Rejection Memo

The active idea may be rejected because it sounds like a benchmark study rather than a method. GraphMAE, GraphMAE2, MaskGAE, AUG-MAE, CORE and GAE benchmark papers already compare or connect masked and contrastive objectives. If the proposed metrics are obvious graph statistics, reviewers may argue that the work only reruns known baselines under another protocol. If label-derived metrics such as homophily or feature-label predictability are needed to predict the winner, the selector is not label-free and may leak validation information. If `GCL-I02` becomes central, the project enters a crowded hard-negative mining literature where ProGCL, GRAPE, Negative Metric Learning for Graphs and BalanceGCL are more direct method papers. Finally, if the matched protocol makes all objective families perform similarly, the main thesis disappears.

## Conditions That Kill Immediately

- No predictive relation between label-free metrics and objective-family ranking.
- Selector requires label homophily, feature-label predictability or validation labels.
- Objective differences vanish under matched protocol.
- Ranking flips across pilot seeds with no interpretable regime pattern.
- Runtime budget, parameter count or evaluator mismatch explains the apparent winner.
- I02 audit duplicates ProGCL weights or Negative Metric Learning behavior.
- A closest work is found with the same protocol-aligned label-free objective selector.

## Conditions That Force REVISE

- Metrics predict only homophilic datasets but fail on heterophilic datasets.
- Metrics predict the winner but not the failure reason.
- I02 audit explains failures but adds no value to I03 selector.
- Pilot works only on Planetoid-style citation graphs.
- One objective implementation is too weak to make comparisons credible.

## Conditions That Force PIVOT

- The label-free metrics strongly predict only negative-invalidity regimes, making `GCL-I02` the real story.
- MGM-vs-GCL differences are mostly explained by representation collapse diagnostics, making `GCL-I09` a better companion route.
- Heterophily subtype, not objective family, explains most failures, making `GCL-I04` the better future route.

## Defensive Framing If Pilot Succeeds

Do not say:

- "our method is SOTA";
- "masked modeling is better than contrastive learning";
- "we solve false negatives";
- "we introduce a new hybrid SSL objective."

Say:

- "under matched protocol, objective-family suitability is regime-dependent";
- "label-free graph diagnostics provide a falsifiable objective-boundary signal";
- "validation-label audits explain but do not train or select";
- "pilot evidence supports further development, not final claims."
