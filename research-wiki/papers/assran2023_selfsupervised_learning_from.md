---
type: paper
node_id: paper:assran2023_selfsupervised_learning_from
title: "Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture"
authors: ["Mahmoud Assran", "Quentin Duval", "Ishan Misra", "Piotr Bojanowski", "Pascal Vincent", "Michael Rabbat", "Yann LeCun", "Nicolas Ballas"]
year: 2023
venue: "arXiv"
external_ids:
  arxiv: "2301.08243"
  doi: null
  s2: null
tags: ["method-transfer", "masked-modeling", "latent-prediction", "vision-ssl"]
added: 2026-06-25T13:20:07Z
---

# Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

## One-line thesis
I-JEPA predicts latent targets rather than raw pixels, a transferable masked/predictive SSL primitive.

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

> This paper demonstrates an approach for learning highly semantic image representations without relying on hand-crafted data-augmentations. We introduce the Image-based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from images. The idea behind I-JEPA is simple: from a single context block, predict the representations of various target blocks in the same image. A core design choice to guide I-JEPA towards producing semantic representations is the masking strategy; specifically, it is crucial to (a) sample target blocks with sufficiently large scale (semantic), and to (b) use a sufficiently informative (spatially distributed) context block. Empirically, when combined with Vision Transformers, we find I-JEPA to be highly scalable. For instance, we train a ViT-Huge/14 on ImageNet using 16 A100 GPUs in under 72 hours to achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction.

