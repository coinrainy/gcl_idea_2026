# Novelty Check: GCL-I01

## Proposed Idea

Semantic-preserving positive validity tests: accept positive augmented views only when structural consistency, feature stability and masked-latent context predictability agree.

## Core Claims

1. Positive-pair semantic validity is under-audited in node-level GCL.
2. Masked latent context prediction can identify augmentations that break task semantics.
3. Failed positive views should be diagnosed rather than silently aligned or discarded.

## Query Formulations Used

Full matrix: `notes/stage2_novelty/query_matrix.tsv`. Raw DeepXiv outputs: `notes/stage2_novelty/deepxiv_search/`.

## Sources Checked

- arXiv/WebSearch: GCA, AFGRL, G-Censor, SPGCL, GraphCL, "good view" / CtrlGCL, InfoNCE semantically guided graph CL.
- DeepXiv: 9 targeted `GCL-I01` queries.
- OpenReview/WebSearch: G-Censor OpenReview; HLCL/G-Censor Stage 1 sources.
- Local wiki/PDF: GRACE/GCA/AFGRL/G-Censor/CM-GCL/SPGCL notes and PDFs.
- Semantic Scholar: API returned HTTP 429.
- Exa: unavailable because `EXA_API_KEY` is empty.

## Closest Prior Works

| Paper | Overlap | True delta |
| --- | --- | --- |
| GCA | Adaptive edge/feature augmentation to preserve important structure | I01 must go beyond centrality/feature-importance augmentation. |
| AFGRL | Augmentation-free local/global positive discovery | I01 must not reduce to kNN/cluster positive mining. |
| G-Censor | Task-oriented counterfactual positive/negative ego-graph views | Very strong closest work; I01 must focus on protocol-aligned validity audit and masked-latent test. |
| SPGCL | Recent positive-sample construction across homophily/heterophily | Strong risk for positive construction claims. |
| Good-view / CtrlGCL / augmentation-quality papers | Define or learn beneficial views | Blocks generic "better view" framing. |

## Overlap

High with GCA/G-Censor/SPGCL on view/positive construction. Medium with GraphMAE-style masked latent prediction. The combined positive-validity audit is not clearly found as an established node-classification GCL protocol, but it is close to several lines.

## True Delta

The delta is an explicit positive-validity audit with a masked-latent criterion under frozen evaluator, not another adaptive augmentation.

## Novelty Score

6/10.

## Risk of Being Considered Incremental

High unless the masked-latent validity test proves predictive and differs from G-Censor/task-oriented views.

## Recommendation

REVISE.

## What Framing Would Be Honest

"A positive-pair validity audit and training constraint for node-level GCL."

## What Framing Is Prohibited

- "Better graph augmentation."
- "Semantic positives" without separating from AFGRL/SPGCL/G-Censor.
- Any claim that requires test labels to identify bad positives.

## Minimum Additional Novelty Check

Read G-Censor, CtrlGCL/good-view papers, SPGCL and semantically guided InfoNCE papers before Stage 2B.
