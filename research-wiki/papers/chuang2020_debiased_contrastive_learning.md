---
type: paper
node_id: paper:chuang2020_debiased_contrastive_learning
title: "Debiased Contrastive Learning"
authors: ["Ching-Yao Chuang", "Joshua Robinson", "Lin Yen-Chen", "Antonio Torralba", "Stefanie Jegelka"]
year: 2020
venue: "Advances in Neural Information Processing Systems (2020)"
external_ids:
  arxiv: "2007.00224"
  doi: null
  s2: null
tags: ["method-transfer", "false-negative", "debiased-contrastive"]
added: 2026-06-25T13:20:08Z
---

# Debiased Contrastive Learning

## One-line thesis
Debiased contrastive learning corrects same-class false negative bias without labels.

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

> A prominent technique for self-supervised representation learning has been to contrast semantically similar and dissimilar pairs of samples. Without access to labels, dissimilar (negative) points are typically taken to be randomly sampled datapoints, implicitly accepting that these points may, in reality, actually have the same label. Perhaps unsurprisingly, we observe that sampling negative examples from truly different labels improves performance, in a synthetic setting where labels are available. Motivated by this observation, we develop a debiased contrastive objective that corrects for the sampling of same-label datapoints, even without knowledge of the true labels. Empirically, the proposed objective consistently outperforms the state-of-the-art for representation learning in vision, language, and reinforcement learning benchmarks. Theoretically, we establish generalization bounds for the downstream classification task.

