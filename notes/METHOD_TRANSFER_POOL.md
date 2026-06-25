# Method Transfer Literature Pool

本文件只整理可迁移机制 primitive，不生成最终研究 idea。筛选标准：机制能映射到 GCL 节点分类，且不是简单 gate / adapter / residual trick。

## Source Status

- arXiv: 可用；已下载 5 篇核心 GCL PDF 到 `papers/`。
- Semantic Scholar: 请求触发 HTTP 429，未能稳定返回结构化结果。
- DeepXiv: wrapper 存在，但本机缺少 `deepxiv` CLI，未能使用。
- Exa: 缺少 `EXA_API_KEY`，未能使用。
- WebSearch / WebFetch: 已用于补充跨领域和 OpenReview/官方页面线索。

## Transfer Papers

| Title | Year | Venue | Field | Core mechanism | Solves in original field | Transferable primitive | Possible mapping to GCL node classification | Risk if transferred naively | Closest GCL work | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contrastive Predictive Coding / InfoNCE | 2018 | arXiv / representation learning | Vision/audio/NLP SSL | classify true future/positive among negatives | scalable MI-style representation learning | temperature, negative pool, density-ratio view | audit whether graph negatives are semantically valid under homophily/heterophily | false negatives dominate small graphs | GRACE, MVGRL, GCA | MEDIUM |
| Understanding Contrastive Representation Learning through Alignment and Uniformity | 2020 | ICML | Vision SSL theory | decompose CL into alignment and uniformity | explains instance discrimination geometry | alignment-uniformity diagnostics | measure when GCL improves uniformity but hurts class/structure semantics | can become descriptive metric only | GRACE analyses, XSimGCL | HIGH |
| Debiased Contrastive Learning | 2020 | NeurIPS | Vision SSL | correct same-class false-negative bias | mitigates unlabeled false negatives | debiased negative weighting | estimate node-level false-negative probability from graph/text/feature neighborhoods | bad estimator leaks labels or overfits homophily | ProGCL | HIGH |
| Hard Negative Mixing for Contrastive Learning | 2020 | NeurIPS | Vision SSL | synthesize hard negatives | improves discrimination | controlled hard-negative construction | generate hard graph negatives by semantic-preserving perturbation | can create impossible graph semantics | ProGCL, Khan-GCL | MEDIUM |
| Bootstrap Your Own Latent (BYOL) | 2020 | NeurIPS | Vision SSL | online/target networks, predictor, stop-gradient | negative-free SSL without collapse | target encoder momentum and prediction asymmetry | graph bootstrap objective without negative sampling | graph smoothing may hide collapse or class mixing | BGRL | MEDIUM |
| SimSiam | 2021 | CVPR | Vision SSL | stop-gradient plus predictor | simpler negative-free SSL | collapse audit with no negatives | isolate whether graph augmentation is needed once stop-gradient exists | small transductive graphs may overfit identity | BGRL, AFGRL | MEDIUM |
| Barlow Twins | 2021 | ICML | Vision SSL | cross-correlation identity target | redundancy reduction without negatives | decorrelation / redundancy penalty | feature-level graph SSL objective avoiding false negatives | may ignore local graph semantics | Graph Barlow Twins | LOW |
| VICReg | 2022 | ICLR | Vision SSL | variance, invariance, covariance losses | explicit collapse prevention | variance floor + covariance decorrelation | combine graph view invariance with collapse diagnostics | tuning losses can become unprincipled | CCA-SSG, GBT | MEDIUM |
| Masked Autoencoders (MAE) | 2022 | CVPR | Vision SSL | high-ratio masking and reconstruction | scalable masked visual pretraining | mask ratio and asymmetric decoder | test whether masking node features/edges preserves task semantics | raw reconstruction rewards nuisance attributes | GraphMAE, MaskGAE | HIGH |
| iBOT | 2022 | ICLR | Vision SSL | online tokenizer and masked token prediction | semantic pseudo-targets for masked views | teacher pseudo-target under masking | replace raw feature reconstruction with latent graph targets | teacher may encode graph bias | GraphMAE2 | MEDIUM |
| I-JEPA | 2023 | CVPR | Vision SSL | latent prediction instead of pixel reconstruction | predictive SSL with semantic latent targets | predict representation of masked region | graph latent prediction for masked ego-graphs/subgraphs | may collapse without careful target variance | GraphMAE2 | HIGH |
| DeepCluster | 2018 | ECCV | Vision SSL | iterative clustering as pseudo-labels | representation learning via cluster assignments | offline cluster pseudo-targets | detect graph semantic communities without labels | cluster may equal degree/popularity | SUGRL/prototype GCL | MEDIUM |
| SwAV | 2020 | NeurIPS | Vision SSL | online swapped assignments to prototypes | avoids pairwise negatives | balanced prototype assignment | node prototypes across augmented graph views | prototype imbalance in long-tail classes | prototype/cluster GCL | HIGH |
| DINO | 2021 | ICCV | Vision SSL | teacher-student self-distillation | emergent semantic grouping | momentum teacher pseudo-targets | use teacher graph/text embeddings as soft semantic anchors | teacher confirmation bias | BGRL-style graph SSL | MEDIUM |
| Co-teaching | 2018 | NeurIPS | Noisy supervision | two networks exchange small-loss samples | robust learning under label noise | disagreement-based sample filtering | identify unreliable positives/negatives or noisy edges | may drop minority/heterophilic nodes | robust GCL, GCA | MEDIUM |
| Confident Learning | 2021 | JMLR | Noisy labels | estimate label noise from predicted probabilities | dataset error detection | noise/confidence matrix | estimate pseudo-label / pseudo-positive reliability | requires calibrated predictions | LLM pseudo-label TAG works | HIGH |
| Invariant Risk Minimization | 2019 | arXiv | OOD/DG | learn invariant predictors across environments | reduce spurious correlations | environment-wise invariance test | use graph domains/augmentations as environments for failure diagnosis | environment construction may be arbitrary | RGCL, cross-domain GNN | HIGH |
| GroupDRO | 2020 | ICLR | Robust/OOD | optimize worst-group risk | improves minority group robustness | worst-split / worst-domain reporting | report worst graph family or worst homophily bin | groups may be unavailable | heterophily-aware GCL | MEDIUM |
| Language model pseudo-labeling for TAGs | 2023-2025 | arXiv / conferences | LLM/TAG | LLM-generated labels/features | improves text-attributed graph learning | semantic prior independent of graph topology | audit whether text semantics can detect false positives/negatives | LLM labels may leak benchmark labels or use hidden supervision | LangGSL, TAPE-like TAG works | HIGH |

## Top 10 Transferable Primitives

1. False-negative probability estimation without labels.
2. Alignment-uniformity diagnostics split by homophily/heterophily bins.
3. Latent target prediction instead of raw feature reconstruction.
4. Teacher-student pseudo-targets with collapse and confidence audits.
5. Prototype assignment with class/degree/popularity balance constraints.
6. Environment-wise invariance checks across graph domains or structure regimes.
7. Robust sample selection for noisy positives and graph augmentations.
8. Variance/covariance collapse prevention for negative-free GCL.
9. LLM/text semantic reliability signals for TAGs.
10. Worst-group reporting over graph regimes rather than only mean accuracy.

## Clearly Poor Transfer Directions

- Purely adding a gate, adapter, residual, temperature schedule, or reweighting layer without a falsifiable mechanism.
- Directly copying image augmentations to graphs without preserving node-label semantics.
- Using LLM pseudo-labels without auditing benchmark contamination, calibration, and supervision leakage.
- Optimizing only global uniformity when node labels are local/semantic and heterophily-sensitive.

## Already Used by GCL

- InfoNCE / instance discrimination: GRACE, GCA, MVGRL.
- Adaptive graph augmentations: GCA and related augmentation learning work.
- Negative-free/decorrelation: BGRL, CCA-SSG, Graph Barlow Twins, AFGRL.
- Hard/false negative mining: ProGCL and recent hard-negative GCL variants.
- Masked graph modeling: GraphMAE, GraphMAE2, MaskGAE.
- Prototype/cluster hints: several cluster/prototype GCL works, but protocols are often not directly comparable.

## Possible Gap Seeds

- False positives are less systematically audited than false negatives.
- Latent predictive SSL is not fully benchmarked against GCL under identical frozen-evaluator node classification protocols.
- Heterophily-aware GCL often targets special graph regimes but does not prove when homophily assumptions fail.
- LLM semantic priors are promising for TAGs, but leakage-safe, split-consistent evaluation remains underdeveloped.
