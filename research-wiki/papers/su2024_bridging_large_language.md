---
type: paper
node_id: paper:su2024_bridging_large_language
title: "Bridging Large Language Models and Graph Structure Learning Models for Robust Representation Learning"
authors: ["Guangxin Su", "Yifan Zhu", "Wenjie Zhang", "Hanchen Wang", "Ying Zhang"]
year: 2024
venue: "arXiv"
external_ids:
  arxiv: "2410.12096"
  doi: null
  s2: null
tags: ["llm", "tag", "graph-structure-learning", "node-classification", "robustness"]
added: 2026-06-25T13:19:51Z
---

# Bridging Large Language Models and Graph Structure Learning Models for Robust Representation Learning

## One-line thesis
LangGSL combines LLM-derived features/pseudo-labels with graph structure learning for robust TAG representation learning.

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

> Graph representation learning, involving both node features and graph structures, is crucial for real-world applications but often encounters pervasive noise. State-of-the-art methods typically address noise by focusing separately on node features with large language models (LLMs) and on graph structures with graph structure learning models (GSLMs). In this paper, we introduce LangGSL, a robust framework that integrates the complementary strengths of pre-trained language models and GSLMs to jointly enhance both node feature and graph structure learning. In LangGSL, we first leverage LLMs to filter noise in the raw data and extract valuable cleaned information as features, enhancing the synergy of downstream models. During the mutual learning phase in LangGSL, the core idea is to leverage the relatively small language model (LM) to process local attributes and generate reliable pseudo-labels and informative node embeddings, which are then integrated into the GSLM's prediction phase. This approach enriches the global context and enhances overall performance. Meanwhile, GSLM refines the evolving graph structure constructed from the LM's output, offering updated labels back to the LM as additional guidance, thus facilitating a more effective mutual learning process. The LM and GSLM work synergistically, complementing each other's strengths and offsetting weaknesses within a variational information-maximizing framework, resulting in enhanced node features and a more robust graph structure. Extensive experiments on diverse graph datasets of varying scales and across different task scenarios demonstrate the scalability and effectiveness of the proposed approach.

