---
type: paper
node_id: paper:hou2023_graphmae2_decodingenhanced_masked
title: "GraphMAE2: A Decoding-Enhanced Masked Self-Supervised Graph Learner"
authors: ["Zhenyu Hou", "Yufei He", "Yukuo Cen", "Xiao Liu", "Yuxiao Dong", "Evgeny Kharlamov", "Jie Tang"]
year: 2023
venue: "arXiv"
external_ids:
  arxiv: "2304.04779"
  doi: null
  s2: null
tags: ["masked-graph-modeling", "node-classification", "graphmae2", "closest-work"]
added: 2026-06-25T13:48:10Z
---

# GraphMAE2: A Decoding-Enhanced Masked Self-Supervised Graph Learner

## One-line thesis
GraphMAE2 improves masked graph autoencoding with re-mask decoding and latent prediction on large node-classification benchmarks.

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

> Graph self-supervised learning (SSL), including contrastive and generative approaches, offers great potential to address the fundamental challenge of label scarcity in real-world graph data. Among both sets of graph SSL techniques, the masked graph autoencoders (e.g., GraphMAE)--one type of generative method--have recently produced promising results. The idea behind this is to reconstruct the node features (or structures)--that are randomly masked from the input--with the autoencoder architecture. However, the performance of masked feature reconstruction naturally relies on the discriminability of the input features and is usually vulnerable to disturbance in the features. In this paper, we present a masked self-supervised learning framework GraphMAE2 with the goal of overcoming this issue. The idea is to impose regularization on feature reconstruction for graph SSL. Specifically, we design the strategies of multi-view random re-mask decoding and latent representation prediction to regularize the feature reconstruction. The multi-view random re-mask decoding is to introduce randomness into reconstruction in the feature space, while the latent representation prediction is to enforce the reconstruction in the embedding space. Extensive experiments show that GraphMAE2 can consistently generate top results on various public datasets, including at least 2.45% improvements over state-of-the-art baselines on ogbn-Papers100M with 111M nodes and 1.6B edges.

