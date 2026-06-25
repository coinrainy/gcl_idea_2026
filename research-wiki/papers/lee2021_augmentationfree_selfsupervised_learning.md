---
type: paper
node_id: paper:lee2021_augmentationfree_selfsupervised_learning
title: "Augmentation-Free Self-Supervised Learning on Graphs"
authors: ["Namkyeong Lee", "Junseok Lee", "Chanyoung Park"]
year: 2021
venue: "arXiv"
external_ids:
  arxiv: "2112.02472"
  doi: null
  s2: null
tags: ["gcl", "augmentation-free", "negative-free", "node-classification", "closest-work"]
added: 2026-06-25T13:48:09Z
---

# Augmentation-Free Self-Supervised Learning on Graphs

## One-line thesis
AFGRL removes explicit graph augmentations and negatives by discovering structurally and semantically related positive nodes.

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

> Inspired by the recent success of self-supervised methods applied on images, self-supervised learning on graph structured data has seen rapid growth especially centered on augmentation-based contrastive methods. However, we argue that without carefully designed augmentation techniques, augmentations on graphs may behave arbitrarily in that the underlying semantics of graphs can drastically change. As a consequence, the performance of existing augmentation-based methods is highly dependent on the choice of augmentation scheme, i.e., hyperparameters associated with augmentations. In this paper, we propose a novel augmentation-free self-supervised learning framework for graphs, named AFGRL. Specifically, we generate an alternative view of a graph by discovering nodes that share the local structural information and the global semantics with the graph. Extensive experiments towards various node-level tasks, i.e., node classification, clustering, and similarity search on various real-world datasets demonstrate the superiority of AFGRL. The source code for AFGRL is available at https://github.com/Namkyeong/AFGRL.

