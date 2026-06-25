---
type: paper
node_id: paper:hou2022_graphmae_selfsupervised_masked
title: "GraphMAE: Self-Supervised Masked Graph Autoencoders"
authors: ["Zhenyu Hou", "Xiao Liu", "Yukuo Cen", "Yuxiao Dong", "Hongxia Yang", "Chunjie Wang", "Jie Tang"]
year: 2022
venue: "arXiv"
external_ids:
  arxiv: "2205.10803"
  doi: null
  s2: null
tags: ["masked-graph-modeling", "node-classification", "generative-ssl"]
added: 2026-06-25T13:19:49Z
---

# GraphMAE: Self-Supervised Masked Graph Autoencoders

## One-line thesis
GraphMAE demonstrates masked feature reconstruction as a strong graph SSL alternative to contrastive objectives.

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

> Self-supervised learning (SSL) has been extensively explored in recent years. Particularly, generative SSL has seen emerging success in natural language processing and other AI fields, such as the wide adoption of BERT and GPT. Despite this, contrastive learning-which heavily relies on structural data augmentation and complicated training strategies-has been the dominant approach in graph SSL, while the progress of generative SSL on graphs, especially graph autoencoders (GAEs), has thus far not reached the potential as promised in other fields. In this paper, we identify and examine the issues that negatively impact the development of GAEs, including their reconstruction objective, training robustness, and error metric. We present a masked graph autoencoder GraphMAE that mitigates these issues for generative self-supervised graph pretraining. Instead of reconstructing graph structures, we propose to focus on feature reconstruction with both a masking strategy and scaled cosine error that benefit the robust training of GraphMAE. We conduct extensive experiments on 21 public datasets for three different graph learning tasks. The results manifest that GraphMAE-a simple graph autoencoder with careful designs-can consistently generate outperformance over both contrastive and generative state-of-the-art baselines. This study provides an understanding of graph autoencoders and demonstrates the potential of generative self-supervised pre-training on graphs.

