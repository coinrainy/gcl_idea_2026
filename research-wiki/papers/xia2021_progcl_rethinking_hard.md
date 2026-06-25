---
type: paper
node_id: paper:xia2021_progcl_rethinking_hard
title: "ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning"
authors: ["Jun Xia", "Lirong Wu", "Ge Wang", "Jintao Chen", "Stan Z. Li"]
year: 2021
venue: "arXiv"
external_ids:
  arxiv: "2110.02027"
  doi: null
  s2: null
tags: ["gcl", "false-negative", "hard-negative", "node-classification"]
added: 2026-06-25T13:19:42Z
---

# ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning

## One-line thesis
ProGCL shows hard negatives in GCL are often false negatives and proposes probability-aware hard negative mining.

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

> Contrastive Learning (CL) has emerged as a dominant technique for unsupervised representation learning which embeds augmented versions of the anchor close to each other (positive samples) and pushes the embeddings of other samples (negatives) apart. As revealed in recent studies, CL can benefit from hard negatives (negatives that are most similar to the anchor). However, we observe limited benefits when we adopt existing hard negative mining techniques of other domains in Graph Contrastive Learning (GCL). We perform both experimental and theoretical analysis on this phenomenon and find it can be attributed to the message passing of Graph Neural Networks (GNNs). Unlike CL in other domains, most hard negatives are potentially false negatives (negatives that share the same class with the anchor) if they are selected merely according to the similarities between anchor and themselves, which will undesirably push away the samples of the same class. To remedy this deficiency, we propose an effective method, dubbed \textbf{ProGCL}, to estimate the probability of a negative being true one, which constitutes a more suitable measure for negatives' hardness together with similarity. Additionally, we devise two schemes (i.e., \textbf{ProGCL-weight} and \textbf{ProGCL-mix}) to boost the performance of GCL. Extensive experiments demonstrate that ProGCL brings notable and consistent improvements over base GCL methods and yields multiple state-of-the-art results on several unsupervised benchmarks or even exceeds the performance of supervised ones. Also, ProGCL is readily pluggable into various negatives-based GCL methods for performance improvement. We release the code at \textcolor{magenta}{\url{https://github.com/junxia97/ProGCL}}.

