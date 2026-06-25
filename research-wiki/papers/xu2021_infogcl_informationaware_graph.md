---
type: paper
node_id: paper:xu2021_infogcl_informationaware_graph
title: "InfoGCL: Information-Aware Graph Contrastive Learning"
authors: ["Dongkuan Xu", "Wei Cheng", "Dongsheng Luo", "Haifeng Chen", "Xiang Zhang"]
year: 2021
venue: "arXiv"
external_ids:
  arxiv: "2110.15438"
  doi: null
  s2: null
tags: ["gcl", "information-bottleneck", "node-classification", "closest-work"]
added: 2026-06-25T13:48:13Z
---

# InfoGCL: Information-Aware Graph Contrastive Learning

## One-line thesis
InfoGCL uses information-bottleneck principles to analyze and unify graph contrastive learning design choices.

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

> Various graph contrastive learning models have been proposed to improve the performance of learning tasks on graph datasets in recent years. While effective and prevalent, these models are usually carefully customized. In particular, although all recent researches create two contrastive views, they differ greatly in view augmentations, architectures, and objectives. It remains an open question how to build your graph contrastive learning model from scratch for particular graph learning tasks and datasets. In this work, we aim to fill this gap by studying how graph information is transformed and transferred during the contrastive learning process and proposing an information-aware graph contrastive learning framework called InfoGCL. The key point of this framework is to follow the Information Bottleneck principle to reduce the mutual information between contrastive parts while keeping task-relevant information intact at both the levels of the individual module and the entire framework so that the information loss during graph representation learning can be minimized. We show for the first time that all recent graph contrastive learning methods can be unified by our framework. We empirically validate our theoretical analysis on both node and graph classification benchmark datasets, and demonstrate that our algorithm significantly outperforms the state-of-the-arts.

