# Stage 2B Decision

Date: 2026-06-25
Stage: Stage 2B refine
Executor: Codex using `/research-refine-pipeline` under user constraints

## Final Verdict

GO to Stage 3 pilot.

This is GO only for a pilot-stage falsification plan. It is not approval for formal experiments, SOTA claims, paper writing, or experiment execution.

## Active Idea

SELECT `GCL-I03`: Protocol-aligned MGM-vs-GCL regime selector.

Refined active idea name: Protocol-Aligned Graph SSL Regime Diagnostic.

`GCL-I02` is not selected as the dominant idea. It is retained as an auxiliary negative-validity audit and fallback route. The merge decision is:

- No full merge of `GCL-I03 + GCL-I02`.
- Use `GCL-I02` only to audit whether the contrastive side of `GCL-I03` fails because of invalid negatives.
- Do not add ProGCL-like hard-negative reweighting as a core mechanism.

## Dominant Contribution

The dominant contribution is a protocol-aligned, label-free regime diagnostic that predicts when masked graph modeling, negative-based contrastive learning, or bootstrap graph SSL is the safer objective family for node classification after split, backbone, evaluator, seed, and budget are fixed.

This is a boundary/diagnostic contribution, not a new universal SSL loss.

## Why SELECT GCL-I03

`GCL-I03` is selected because:

- It is reviewer priority 1.
- Its novelty risk is medium rather than high if framed honestly as protocol-aligned objective-boundary work.
- It directly targets a known comparability gap: GraphMAE-style masked models and GRACE/GCA/BGRL-style GCL methods are often compared through incompatible protocols.
- It has a low-cost Stage 3 pilot falsifier: if label-free regime metrics cannot predict objective ranking under the same protocol, the idea dies quickly.

## Why Not SELECT GCL-I02 As Main

`GCL-I02` remains promising but is not the main route because:

- Its closest-work pressure is high: ProGCL, GRAPE, Negative Metric Learning for Graphs, BalanceGCL, counterfactual hard negatives, SPGCL, HLCL, HomoGCL and affinity-uncertainty hard-negative mining already cover much of the negative-sampling space.
- A main-method version would easily collapse into another hard-negative weighting method.
- Its best role in Stage 2B is diagnostic: explain whether negative invalidity is one reason contrastive objectives lose in certain graph regimes.

## Label-Free Metrics vs Label-Audit Metrics

Label-free regime metrics are allowed to drive the Stage 3 pilot selector and may be computed before using labels:

- feature-neighborhood smoothness;
- edge feature similarity distribution;
- feature reconstruction difficulty under a fixed masked-feature probe;
- structural reconstruction difficulty under a fixed edge/path probe;
- degree skew, clustering, connectedness, and local role entropy;
- augmentation stability under fixed perturbation budget;
- embedding uniformity/alignment proxies computed without class labels.

Label-audit metrics are not selector inputs and not training signals. They are split-restricted checks used only to interpret and falsify:

- train/validation-only label homophily;
- train/validation-only feature-label predictability;
- validation-only negative-pair label agreement for `GCL-I02` audit;
- validation-only objective winner under frozen linear evaluator.

Test labels must not be used for selecting metrics, choosing objectives, tuning hyperparameters, changing epoch, or deciding whether the idea survives.

## Closest-Work Risk

`GCL-I03` risk: GraphMAE, GraphMAE2, MaskGAE, AUG-MAE, CORE, GCMAE and GAE benchmark papers block any claim that a new masked objective or MGM+GCL hybrid is novel.

`GCL-I02` risk: ProGCL, GRAPE, Negative Metric Learning for Graphs, BalanceGCL, counterfactual hard negatives, SPGCL, HLCL, HomoGCL and affinity-uncertainty hard-negative mining block generic false-negative reweighting claims.

Therefore the proposal must stay narrow:

- claim protocol-normalized objective-boundary prediction;
- do not claim universal superiority;
- do not claim a new negative sampler;
- do not claim SOTA from pilot results.

## Stage 3 Entry Condition

Stage 3 may begin only as a pilot after this decision. Required before any pilot run:

- freeze the pilot configuration separately from formal protocol;
- save split JSON files for pilot seeds;
- implement result logging before running methods;
- keep all results labeled `pilot`;
- pre-register kill conditions in `refine-logs/STAGE2B_PILOT_PLAN.md`.

## Kill Conditions

Kill the active idea directly if Stage 3 pilot shows any of the following:

- label-free regime metrics do not predict objective-family ranking better than chance or a dataset-ID baseline;
- objective ranking is unstable across pilot seeds or explained by implementation/runtime budget differences;
- masked, contrastive and bootstrap results become indistinguishable under matched protocol;
- the only useful predictors are label-audit metrics, which would make the selector label-leaky;
- the I02 audit shows negative-validity metrics are random or simply duplicate ProGCL-style weights;
- a new closest work is found that already provides the same protocol-aligned label-free objective selector.

## Decision Summary

Final active idea: `GCL-I03`.

Dominant contribution: protocol-aligned label-free graph SSL regime diagnostic for objective-family selection.

Auxiliary mechanism: `GCL-I02` validation-only negative-validity audit for explaining contrastive failures.

Decision: GO to Stage 3 pilot only.
