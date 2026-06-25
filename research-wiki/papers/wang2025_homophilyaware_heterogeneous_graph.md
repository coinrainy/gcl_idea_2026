---
type: paper
node_id: paper:wang2025_homophilyaware_heterogeneous_graph
title: "Homophily-aware Heterogeneous Graph Contrastive Learning"
authors: ["Haosen Wang", "Chenglong Shi", "Can Xu", "Surong Yan", "Pan Tang"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2501.08538"
  doi: null
  s2: null
tags: ["gcl", "heterophily", "heterogeneous", "false-negative"]
added: 2026-06-25T13:19:56Z
---

# Homophily-aware Heterogeneous Graph Contrastive Learning

## One-line thesis
Homophily-aware heterogeneous GCL highlights persistent false-negative issues in heterogeneous graph contrastive learning.

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

> Heterogeneous graph pre-training (HGP) has demonstrated remarkable performance across various domains. However, the issue of heterophily in real-world heterogeneous graphs (HGs) has been largely overlooked. To bridge this research gap, we proposed a novel heterogeneous graph contrastive learning framework, termed HGMS, which leverages connection strength and multi-view self-expression to learn homophilous node representations. Specifically, we design a heterogeneous edge dropping augmentation strategy that enhances the homophily of augmented views. Moreover, we introduce a multi-view self-expressive learning method to infer the homophily between nodes. In practice, we develop two approaches to solve the self-expressive matrix. The solved self-expressive matrix serves as an additional augmented view to provide homophilous information and is used to identify false negatives in contrastive loss. Extensive experimental results demonstrate the superiority of HGMS across different downstream tasks.

