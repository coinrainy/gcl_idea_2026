---
type: paper
node_id: paper:li2022_whats_behind_mask
title: "What's Behind the Mask: Understanding Masked Graph Modeling for Graph Autoencoders"
authors: ["Jintang Li", "Ruofan Wu", "Wangbin Sun", "Liang Chen", "Sheng Tian", "Liang Zhu", "Changhua Meng", "Zibin Zheng", "Weiqiang Wang"]
year: 2022
venue: "arXiv"
external_ids:
  arxiv: "2205.10053"
  doi: null
  s2: null
tags: ["masked-graph-modeling", "maskgae", "node-classification", "closest-work"]
added: 2026-06-25T13:48:11Z
---

# What's Behind the Mask: Understanding Masked Graph Modeling for Graph Autoencoders

## One-line thesis
MaskGAE studies masked edge modeling and connects masked graph autoencoding with contrastive learning.

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

> The last years have witnessed the emergence of a promising self-supervised learning strategy, referred to as masked autoencoding. However, there is a lack of theoretical understanding of how masking matters on graph autoencoders (GAEs). In this work, we present masked graph autoencoder (MaskGAE), a self-supervised learning framework for graph-structured data. Different from standard GAEs, MaskGAE adopts masked graph modeling (MGM) as a principled pretext task - masking a portion of edges and attempting to reconstruct the missing part with partially visible, unmasked graph structure. To understand whether MGM can help GAEs learn better representations, we provide both theoretical and empirical evidence to comprehensively justify the benefits of this pretext task. Theoretically, we establish close connections between GAEs and contrastive learning, showing that MGM significantly improves the self-supervised learning scheme of GAEs. Empirically, we conduct extensive experiments on a variety of graph benchmarks, demonstrating the superiority of MaskGAE over several state-of-the-arts on both link prediction and node classification tasks.

