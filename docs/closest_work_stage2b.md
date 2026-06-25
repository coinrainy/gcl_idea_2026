# Closest Work Assessment for Stage 2B

Date: 2026-06-25

## Active Idea

Active idea: `GCL-I03`.

Auxiliary audit: `GCL-I02`.

## I03 Closest-Work Risk

| Work family | Risk | Stage 2B boundary |
| --- | --- | --- |
| GraphMAE / GraphMAE2 | masked graph modeling already strong for node classification | do not claim a new masked objective |
| MaskGAE | masked edge/path modeling already covers reconstruction variants | do not make edge reconstruction the novelty |
| AUG-MAE / alignment-uniformity analysis | already connects GraphMAE behavior to contrastive geometry | do not claim alignment/uniformity analysis alone |
| CORE / GCMAE | already mixes contrastive and generative objectives | do not propose MGM+GCL hybrid as novelty |
| Revisiting/benchmarking graph autoencoders | increases benchmark and protocol pressure | make strict project protocol and label-free selector central |
| GRACE/GCA/BGRL | representative contrastive/bootstrap baselines | use as controlled comparison, not as weak baselines |

## I02 Closest-Work Risk

| Work family | Risk | Stage 2B boundary |
| --- | --- | --- |
| ProGCL | probability-aware hard negatives already address false negatives | do not propose another scalar true-negative weight |
| GRAPE | expansive adaptive hard-negative mining beyond homophily | use I02 as audit, not another miner |
| Negative Metric Learning for Graphs | learnable metric for distinguishing false negatives | do not add a learned negative metric in pilot |
| BalanceGCL | hard-negative and semantic-positive generation | avoid balanced hard-negative generation claims |
| Counterfactual hard negatives | synthetic hard-negative generation already covered | do not generate hard negatives as central claim |
| SPGCL / HLCL / HomoGCL | heterophily and homophily-aware contrastive variants | do not claim generic heterophily-aware negative handling |

## External Spot Check

Recent source spot check supports the high-risk boundary:

- Negative Metric Learning for Graphs explicitly targets false negatives with a learnable negative metric network: https://arxiv.org/abs/2505.10307
- GRAPE targets expansive and adaptive hard-negative mining for GCL: https://openreview.net/forum?id=VROWvRu0Fy
- BalanceGCL targets balanced hard negatives and fine-grained semantic-aware positives: https://ojs.aaai.org/index.php/AAAI/article/view/39674
- AUG-MAE connects GraphMAE and GCL through alignment/uniformity analysis: https://arxiv.org/abs/2402.07225
- CORE integrates contrastive learning into masked feature reconstruction: https://arxiv.org/abs/2512.13235
- Revisiting and Benchmarking Graph Autoencoders raises GAE benchmark/protocol pressure: https://openreview.net/forum?id=lYXhiCYkPn

No exact source was found in this spot check that kills the narrow Stage 2B thesis: a protocol-aligned, label-free objective-family regime diagnostic for node classification. This is not a complete final novelty audit.

## Risk Verdict

`GCL-I03` remains viable for Stage 3 pilot if the project avoids method-fusion claims.

`GCL-I02` remains too crowded as a main method but useful as an audit component.
