---
type: paper
node_id: paper:shan2026_revisiting_positive_samples
title: "Revisiting Positive Samples in Graph Contrastive Learning: From the Perspective of Message Passing"
authors: ["Lianze Shan", "Ningchong Wang", "Jitao Zhao", "Di Jin", "Dongxiao He"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2606.10284"
  doi: null
  s2: null
tags: ["gcl", "positive-mining", "recent", "preprint", "node-classification"]
added: 2026-06-25T13:20:06Z
---

# Revisiting Positive Samples in Graph Contrastive Learning: From the Perspective of Message Passing

## One-line thesis
SPGCL revisits positive samples in GCL and reports broad node-classification evaluations, but is very recent preprint.

## Problem / Gap
_TODO._

## Method
_TODO._

## Key Results
_TODO._

## Assumptions
_TODO._

## Limitations / Failure Modes
_TODO._

## Reusable Ingredients
_TODO._

## Open Questions
_TODO._

## Claims
_TODO._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
_TODO._

## Abstract (original)

> Graph Contrastive Learning (GCL), which trains graph encoders by maximizing similarity between positive samples and minimizing it between negative ones, has emerged as a mainstream graph pre-training paradigm. It is widely recognized that positive samples are essential in GCLs. Ideally, maximizing the similarity of positive samples enables graph encoders to capture intrinsic semantic and patterns of graph data. However, we discover an interesting phenomenon: GCLs can achieve competitive performance even without positive samples. This motivates us to revisit the fundamental mechanism of positive samples in GCLs. From the perspective of Dirichlet energy, we theoretically finds that message passing, a key mechanism in graph encoders, trivializes the maximization of positive samples, preventing GCLs from effectively learning from positive samples. To address this, we propose SPGCL to mitigate the trivialization caused by message passing and restore the learning efficacy of positive samples. Specifically, we find that high Dirichlet energy features help positive samples provide effective learning signals while low Dirichlet energy features contribute little to positive learning signal but is useful for positive sampling. Based on this, SPGCL propagates only high Dirichlet energy features and uses low energy features to construct a probability matrix for reliable positive sampling. Extensive experiments demonstrate the effectiveness of SPGCL.

