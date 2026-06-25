# Novelty Check: GCL-I02

## Proposed Idea

Regime-conditioned negative validity boundary: classify candidate negatives by homophily proxy, feature similarity and structural role similarity, then use confident negatives differently from ambiguous/likely false-negative relations.

## Core Claims

1. False-negative harm in GCL is regime-dependent rather than uniform.
2. Role similarity and local homophily proxy add information beyond ProGCL-style similarity/BMM hardness.
3. Validation-only negative-validity audit can predict when hard negatives help or hurt.

## Query Formulations Used

Full matrix: `notes/stage2_novelty/query_matrix.tsv`. Raw DeepXiv outputs: `notes/stage2_novelty/deepxiv_search/`.

## Sources Checked

- arXiv/WebSearch: ProGCL, Negative Metric Learning for Graphs, counterfactual hard negatives, GRAPE, degree-bias/hard-to-learn nodes, quantity/quality/variety negative selection.
- DeepXiv: 9 targeted `GCL-I02` queries.
- OpenReview/WebSearch: GRAPE OpenReview hard-negative paper; local OpenReview Stage 1 sources.
- Local research-wiki and downloaded PDFs: ProGCL, HLCL, SPGCL, GCA/BGRL references.
- Semantic Scholar: API returned HTTP 429.
- Exa: unavailable because `EXA_API_KEY` is empty.

## Closest Prior Works

| Paper | Overlap | True delta |
| --- | --- | --- |
| ProGCL | Estimates true-negative probability and fixes hard-negative mining | I02 must predict regime-specific harmfulness, not merely another probability weight. |
| GRAPE / expansive adaptive hard negative mining | Explores false negatives beyond homophily and adaptive hard negatives | Strong risk; I02 must show relation taxonomy is more explanatory. |
| Negative Metric Learning for Graphs | Recent direct negative-sampling/metric risk | Must be checked deeply before implementation. |
| Counterfactual Hard Negative Samples for GCL | Generates hard negatives | I02 should avoid synthetic hard-negative generation as the central claim. |
| SPGCL / HLCL | Positive construction and heterophily filters | I02 can remain distinct if focused on negative boundary and validation audit. |

## Overlap

Very high with ProGCL and recent hard-negative papers on the problem. Medium-high with heterophily-aware works. The "role similarity + regime boundary + validation-only audit" framing is the possible delta.

## True Delta

Not "better negative weighting." The delta must be a falsifiable taxonomy of when negatives are valid/harmful across graph regimes.

## Novelty Score

6.5/10.

## Risk of Being Considered Incremental

High. Reviewers will cite ProGCL first, then GRAPE/negative metric learning/counterfactual hard negatives.

## Recommendation

KEEP WITH REVISION.

## What Framing Would Be Honest

"A regime-conditioned diagnostic and training rule for negative validity, explaining where ProGCL-style hard-negative mining succeeds or fails."

## What Framing Is Prohibited

- "We solve false negatives in GCL."
- "Hard negative reweighting for graphs."
- Any claim that uses validation labels for training rather than audit.

## Minimum Additional Novelty Check

Deep-read Negative Metric Learning for Graphs, GRAPE and BalanceGCL before Stage 2B.
