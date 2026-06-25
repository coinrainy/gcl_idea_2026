# Novelty Check: GCL-I05

## Proposed Idea

Bad positive views as masked counter-evidence: low-consistency augmentations are not aligned or discarded; they become masked latent prediction targets that teach which context should not be made invariant.

## Core Claims

1. Failed positive augmentations contain task-relevant counter-evidence.
2. Failure-driven masking is distinct from random/adaptive masking in GraphMAE/GCA.
3. Positive failure prediction can improve robustness to structural/feature noise.

## Query Formulations Used

Full matrix: `notes/stage2_novelty/query_matrix.tsv`. Raw DeepXiv outputs: `notes/stage2_novelty/deepxiv_search/`.

## Sources Checked

- arXiv/WebSearch: GraphMAE, GraphMAE2, MaskGAE, GCA, G-Censor, GCMAE, Rethinking Graph MAE through alignment/uniformity, augmentation-aware GSSL.
- DeepXiv: 9 targeted `GCL-I05` queries.
- OpenReview/WebSearch: G-Censor, graph masked autoencoder records.
- Local wiki/PDF: GCA, GraphMAE/2, MaskGAE, G-Censor, InfoGCL.
- Semantic Scholar: API returned HTTP 429.
- Exa: unavailable because `EXA_API_KEY` is empty.

## Closest Prior Works

| Paper | Overlap | True delta |
| --- | --- | --- |
| GCA | Avoids corrupting important topology/features | I05 must show failed views become useful targets, not merely avoided. |
| G-Censor | Task-oriented counterfactual views | Strong overlap with "counter-evidence"; must distinguish masked latent failure learning. |
| GraphMAE / GraphMAE2 | masked feature/latent graph modeling | I05 must show failure-driven masks are better than random/remask targets. |
| MaskGAE | masked edge/path modeling | Strong overlap if counter-evidence is edge/path mask. |
| GCMAE / contrastive masked reconstruction | combines masked and contrastive objectives | Blocks simple hybrid-objective framing. |

## Overlap

High. This is the most fusion-like top idea and risks looking like GCA + GraphMAE + G-Censor.

## True Delta

The only credible delta is to use positive-alignment failure as the source of masked targets and show that this target selection predicts label-relevant context better than random/adaptive masking.

## Novelty Score

5.5/10.

## Risk of Being Considered Incremental

High.

## Recommendation

REVISE OR KILL unless reviewer sees a sharper mechanism.

## What Framing Would Be Honest

"A failure-driven diagnostic variant that tests whether bad augmentations reveal label-relevant context."

## What Framing Is Prohibited

- "Novel hybrid of GCL and MGM."
- "Counterfactual masked GCL" without separating from G-Censor.
- Any claim that failed positives are known from test labels.

## Minimum Additional Novelty Check

Check augmentation-aware GSSL, GCMAE/CORE, and task-oriented counterfactual view papers before keeping.
