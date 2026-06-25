# Stage 2B Refine Report

Date: 2026-06-25

## Scope

This report refines the two Stage 2A kept candidates:

- `GCL-I03`: Protocol-aligned MGM-vs-GCL regime selector.
- `GCL-I02`: Regime-conditioned negative validity boundary.

No Stage 2A ideation was repeated. No `idea-discovery`, `research-pipeline`, `experiment-bridge`, experiment run, or paper writing was performed.

## Inputs Used

- `AGENTS.md`
- `RESEARCH_BRIEF.md`
- `BENCHMARK_PROTOCOL.md`
- `STAGE2_IDEA_REPORT.md`
- `notes/STAGE2_REVIEWER_REPORT.md`
- `notes/STAGE2_RAW_IDEAS.md`
- `notes/CLOSEST_WORK_DELTA_TABLE.md`
- `notes/stage2_novelty/IDEA_GCL-I03_NOVELTY.md`
- `notes/stage2_novelty/IDEA_GCL-I02_NOVELTY.md`
- `research-wiki/log.md`
- `research-wiki/query_pack.md`

## Starting Evidence

Stage 2A selected `GCL-I03` and `GCL-I02` as the two kept candidates. The reviewer ranked `GCL-I03` first and `GCL-I02` second.

`GCL-I03` has the cleaner paper shape if it is framed as a protocol-aligned diagnostic/benchmark contribution. Its risk is that reviewers may see it as another masked graph modeling comparison unless the project proves the strict protocol and label-free regime prediction are the actual contribution.

`GCL-I02` has stronger method flavor but much higher closest-work pressure. Recent hard-negative and false-negative papers make a main-method claim risky unless the idea clearly explains when hard-negative mining fails rather than proposing another weight.

## Refine Choice

The final active idea is `GCL-I03`.

`GCL-I02` is retained only as a supporting audit that asks: when contrastive objectives lose under matched protocol, is negative-pair invalidity a plausible explanation?

This is not a full merge. The dominant contribution remains `GCL-I03`.

## Refined Problem Anchor

Graph SSL papers often compare masked graph modeling, negative-based contrastive learning and bootstrap learning under different splits, evaluators, seeds, backbones and budgets. As a result, published tables do not tell us when an objective family is actually suitable for node classification.

The refined problem is: can label-free graph-regime measurements predict objective-family suitability once protocol confounds are removed?

## Refined Thesis

Under a fixed node-classification protocol, different graph SSL objective families fail for different graph regimes. A small label-free diagnostic suite can predict these regimes well enough to decide which objective family deserves further development, while validation-label audits explain failures without leaking labels into the selector.

## Dominant Contribution

Protocol-Aligned Graph SSL Regime Diagnostic:

1. Run representative objective families under the same split, seed, backbone, evaluator and budget.
2. Compute label-free graph-regime metrics before downstream labels are used.
3. Test whether those metrics predict objective ranking.
4. Use label-audit metrics only for interpretation and falsification.

## What Is Intentionally Rejected

- A new masked reconstruction objective.
- A new MGM+GCL hybrid loss.
- A new ProGCL-style negative reweighting method.
- A pseudo-label or LLM-assisted selector.
- Any pilot-stage SOTA or robustness claim.

## I03 and I02 Relationship

`GCL-I03` supplies the main question and paper spine: objective-family boundary under matched protocol.

`GCL-I02` supplies one diagnostic lens for the contrastive branch: negative validity may explain where InfoNCE-style methods fail. It does not decide the objective, does not train the main selector, and does not introduce a new negative sampler in Stage 3 pilot.

## Metric Boundary

The original Stage 2A wording mentioned feature-label predictability and edge homophily. Stage 2B refines this to avoid leakage:

- label-free proxies may be used by the selector;
- label-derived metrics are audit-only;
- validation labels may explain but not decide;
- test labels are never used for tuning, selection or survival decisions.

## Closest-Work Risk Assessment

For `GCL-I03`, the main risk comes from GraphMAE, GraphMAE2, MaskGAE, AUG-MAE, CORE, GCMAE and GAE benchmark/rethinking papers. They block claims about masked objectives, alignment-uniformity analysis and simple hybridization.

For `GCL-I02`, the main risk comes from ProGCL, GRAPE, Negative Metric Learning for Graphs, BalanceGCL, counterfactual hard negatives, SPGCL, HLCL, HomoGCL and affinity-uncertainty hard-negative mining. They block generic false-negative and hard-negative mining claims.

The safe novelty boundary is the combination of:

- strict protocol alignment;
- label-free regime prediction;
- explicit separation between selector metrics and label audits;
- objective-family boundary rather than method fusion.

## Stage 3 Pilot Shape

The Stage 3 pilot should be small and falsifying:

- datasets: two homophilic and two heterophilic or mixed-regime datasets;
- objectives: one negative-based contrastive method, one bootstrap method, one masked graph modeling method;
- protocol: identical split, seed, backbone, evaluator and budget;
- seeds: pilot seeds only, suggested `0,1,2`;
- status label: `pilot`;
- decision basis: validation ranking and label-free predictor behavior, not test-set tuning.

## Verdict

GO to Stage 3 pilot.

This GO is conditional on the pilot remaining a pilot. Formal experiments require a later Stage 3/4 gate and protocol freeze.
