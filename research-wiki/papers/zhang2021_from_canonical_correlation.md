---
type: paper
node_id: paper:zhang2021_from_canonical_correlation
title: "From Canonical Correlation Analysis to Self-supervised Graph Neural Networks"
authors: ["Hengrui Zhang", "Qitian Wu", "Junchi Yan", "David Wipf", "Philip S. Yu"]
year: 2021
venue: "arXiv"
external_ids:
  arxiv: "2106.12484"
  doi: null
  s2: null
tags: ["gcl", "negative-free", "decorrelation", "node-classification"]
added: 2026-06-25T13:19:49Z
---

# From Canonical Correlation Analysis to Self-supervised Graph Neural Networks

## One-line thesis
CCA-SSG replaces instance discrimination with feature-level correlation objectives and avoids negatives.

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

> We introduce a conceptually simple yet effective model for self-supervised representation learning with graph data. It follows the previous methods that generate two views of an input graph through data augmentation. However, unlike contrastive methods that focus on instance-level discrimination, we optimize an innovative feature-level objective inspired by classical Canonical Correlation Analysis. Compared with other works, our approach requires none of the parameterized mutual information estimator, additional projector, asymmetric structures, and most importantly, negative samples which can be costly. We show that the new objective essentially 1) aims at discarding augmentation-variant information by learning invariant representations, and 2) can prevent degenerated solutions by decorrelating features in different dimensions. Our theoretical analysis further provides an understanding for the new objective which can be equivalently seen as an instantiation of the Information Bottleneck Principle under the self-supervised setting. Despite its simplicity, our method performs competitively on seven public graph datasets. The code is available at: https://github.com/hengruizhang98/CCA-SSG.

