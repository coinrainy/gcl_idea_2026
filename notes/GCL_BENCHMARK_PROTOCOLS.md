# GCL Benchmark Protocols

本文件整理近年 GCL / graph SSL 节点分类论文的实验协议。若论文或检索片段未明确说明 split、evaluator、seeds、early stopping 或 test@best，统一标为 `UNCLEAR`，不根据常见做法推断。

## Compatibility Classes

- Directly comparable: 明确同任务、同 split、同 evaluator、seed/early stopping/test@best 足够清楚。
- Historical reference: 任务相关但 split/evaluator/seed 或年份协议不同，不能直接放主表比较。
- Protocol unclear: 关键信息缺失，需精读 PDF 或复现实验前确认。

## Protocol Matrix

| Paper | Datasets | Split protocol | Planetoid public | 1:1:8 | Wiki-CS | OGB | Heterophily fixed split | Metric | test@best/final | Early stopping | Evaluator | Seeds | Report | Baseline evaluator same? | Comparable under our protocol |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DGI | Cora/CiteSeer/PubMed/PPI etc. | UNCLEAR from current pass | likely public/standard | UNCLEAR | no | no | no | Accuracy/F1 | UNCLEAR | UNCLEAR | logistic/linear probe likely | UNCLEAR | often mean | UNCLEAR | Historical reference |
| MVGRL | citation + graph datasets | UNCLEAR | likely public/standard | UNCLEAR | no | no | no | Accuracy | UNCLEAR | UNCLEAR | linear evaluator likely | UNCLEAR | mean±std likely | UNCLEAR | Historical reference |
| GRACE | Cora/CiteSeer/PubMed/Coauthor/Amazon/PPI | explicit enough only after PDF check; arXiv abstract says transductive and inductive | likely uses standard citation splits | UNCLEAR | no | no | no | Accuracy/F1 | UNCLEAR | UNCLEAR | frozen encoder + linear classifier likely | UNCLEAR | mean±std likely | mostly yes for GCL baselines | Protocol unclear until exact split confirmed |
| GCA | citation/coauthor/Amazon/PPI | UNCLEAR in current pass | likely standard citation splits | UNCLEAR | no | no | no | Accuracy/F1 | UNCLEAR | UNCLEAR | linear evaluator likely | UNCLEAR | mean±std likely | yes for GCL baselines likely | Protocol unclear |
| ProGCL | node + graph benchmarks | UNCLEAR | likely standard citation splits | UNCLEAR | no | maybe no | no | Accuracy | UNCLEAR | UNCLEAR | GCL evaluator likely | UNCLEAR | mean±std likely | yes likely | Protocol unclear; closest baseline to reproduce |
| BGRL | large-scale graph SSL benchmarks | UNCLEAR | possibly public/standard | UNCLEAR | possible | possible | no | Accuracy/F1 | UNCLEAR | UNCLEAR | linear evaluator | UNCLEAR | mean±std likely | yes likely | Protocol unclear, but essential negative-free baseline |
| CCA-SSG | citation/coauthor/Amazon | UNCLEAR | likely standard | UNCLEAR | no | no | no | Accuracy | UNCLEAR | UNCLEAR | linear evaluator | UNCLEAR | mean±std likely | yes likely | Protocol unclear |
| Graph Barlow Twins | graph/node benchmarks | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | no | Accuracy | UNCLEAR | UNCLEAR | linear/frozen likely | UNCLEAR | UNCLEAR | UNCLEAR | Protocol unclear |
| AFGRL | node classification benchmarks | UNCLEAR | likely public/standard | UNCLEAR | maybe | no | no | Accuracy | UNCLEAR | UNCLEAR | augmentation-free SSL evaluator | UNCLEAR | mean±std likely | yes likely | Protocol unclear |
| GraphMAE | citation/coauthor/OGB etc. | UNCLEAR in current pass | likely standard for citation | UNCLEAR | possible | yes in graph SSL line | no | Accuracy | UNCLEAR | UNCLEAR | linear/evaluator varies | UNCLEAR | mean±std likely | not always same with GCL | Historical unless re-run |
| GraphMAE2 | larger OGB + standard graph SSL | partly explicit in abstract for OGB-Papers100M; exact split requires PDF | no for OGB | no | possible | official split likely | no | Accuracy | UNCLEAR | UNCLEAR | decoder/evaluator protocol varies | UNCLEAR | mean±std likely | not always same | Must re-run or exact-check |
| MaskGAE | link prediction + node classification | UNCLEAR | UNCLEAR | UNCLEAR | no | maybe no | no | Accuracy/AUC | UNCLEAR | UNCLEAR | GAE SSL evaluator | UNCLEAR | UNCLEAR | UNCLEAR | Historical reference unless exact protocol found |
| HLCL | heterophily benchmark graphs | UNCLEAR from OpenReview/arXiv snippets | no | maybe no | no | maybe large graphs | yes likely for heterophily | Accuracy | UNCLEAR | UNCLEAR | GCL evaluator | UNCLEAR | mean±std likely | yes likely | Need exact fixed splits before comparison |
| CM-GCL | imbalanced real-world graphs/TAG | OpenReview abstract; exact split UNCLEAR | no | UNCLEAR | no | no | no | imbalance metrics likely | UNCLEAR | UNCLEAR | fine-tuned GNN encoder | UNCLEAR | mean±std likely | task-specific | Historical/closest work, not directly comparable yet |
| G-Censor | eight node-property datasets | OpenReview abstract only; exact split UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | Accuracy | UNCLEAR | UNCLEAR | model-agnostic GNN | UNCLEAR | UNCLEAR | UNCLEAR | Protocol unclear |
| LangGSL | diverse graph datasets | arXiv abstract only; exact split UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | Accuracy/robustness | UNCLEAR | UNCLEAR | LM + GSLM joint | UNCLEAR | UNCLEAR | not same evaluator | Not directly comparable without re-run |
| Khan-GCL | multiple graph datasets/tasks | arXiv abstract only | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | task metrics | UNCLEAR | UNCLEAR | KAN encoder GCL | UNCLEAR | UNCLEAR | UNCLEAR | Recent preprint, protocol unclear |
| SPGCL | node classification datasets | arXiv metadata only | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | Accuracy | UNCLEAR | UNCLEAR | GCL evaluator | UNCLEAR | UNCLEAR | UNCLEAR | Recent/future preprint; check carefully |

## Direct Comparison Buckets

### Directly Comparable Now

None from literature tables alone. The current Stage 1 pass did not extract enough exact split/evaluator/seed/early-stopping detail to declare any published number directly comparable under `BENCHMARK_PROTOCOL.md`.

### Historical Reference

DGI, MVGRL, GRACE, GCA, BGRL, CCA-SSG, GraphMAE, GraphMAE2 and MaskGAE are essential historical or closest baselines, but their published numbers should not be copied into our main table without confirming or re-running the exact protocol.

### Protocol Unclear / Cannot Compare Yet

HLCL, CM-GCL, G-Censor, LangGSL, Khan-GCL and SPGCL are high-risk closest works whose paper-level protocol must be checked before claims.

## Main Inconsistencies Found

1. Citation network papers often use public Planetoid splits or unspecified standard splits; our default random `1:1:8` cannot be mixed with them.
2. Some graph SSL papers report linear probing; others fine-tune the encoder. These must be separate tables.
3. Seed counts and early stopping are frequently missing from snippets/abstracts.
4. OGB official splits and heterophily fixed splits should not be collapsed into the random split table.
5. LLM/TAG papers often change feature generation, pseudo-labeling, and graph construction, so evaluator equality alone is insufficient.

## Stage 2 Implication

Before any performance claim, reproduce or rerun baselines under the project split/evaluator. Published numbers are useful for closest-work risk analysis, not SOTA claims.
