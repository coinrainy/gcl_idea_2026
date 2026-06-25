---
type: paper
node_id: paper:bielak2021_graph_barlow_twins
title: "Graph Barlow Twins: A self-supervised representation learning framework for graphs"
authors: ["Piotr Bielak", "Tomasz Kajdanowicz", "Nitesh V. Chawla"]
year: 2021
venue: "Knowledge-Based Systems, Volume 256, 28 November 2022, 109631"
external_ids:
  arxiv: "2106.02466"
  doi: null
  s2: null
tags: ["gcl", "negative-free", "redundancy-reduction"]
added: 2026-06-25T13:19:50Z
---

# Graph Barlow Twins: A self-supervised representation learning framework for graphs

## One-line thesis
Graph Barlow Twins transfers redundancy-reduction SSL to graphs without negative samples.

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

> The self-supervised learning (SSL) paradigm is an essential exploration area, which tries to eliminate the need for expensive data labeling. Despite the great success of SSL methods in computer vision and natural language processing, most of them employ contrastive learning objectives that require negative samples, which are hard to define. This becomes even more challenging in the case of graphs and is a bottleneck for achieving robust representations. To overcome such limitations, we propose a framework for self-supervised graph representation learning - Graph Barlow Twins, which utilizes a cross-correlation-based loss function instead of negative samples. Moreover, it does not rely on non-symmetric neural network architectures - in contrast to state-of-the-art self-supervised graph representation learning method BGRL. We show that our method achieves as competitive results as the best self-supervised methods and fully supervised ones while requiring fewer hyperparameters and substantially shorter computation time (ca. 30 times faster than BGRL).

