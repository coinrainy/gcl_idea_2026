# GCL Literature Map

本地图覆盖 GCL 节点分类相关工作、近期并行工作和可迁移 SSL 机制。状态字段只使用已观察到的公开信息；OpenReview 状态不清时标记为 `UNCLEAR`。

## Source Coverage

- Local PDFs: 初始无本地 PDF；本轮下载 `2006.04131`, `2010.14945`, `2110.02027`, `2102.06514`, `2205.10803`。
- arXiv: 成功；用于核心 GCL、masked graph、LLM/TAG、heterophily 查询。
- OpenReview: 部分成功；关键词搜索命中 HLCL、CM-GCL、InfoGCL、G-Censor 等，但 API 429 限制导致 LLM/false-negative 查询部分为空。
- Semantic Scholar: HTTP 429，不可用。
- DeepXiv: CLI 缺失，不可用。
- Exa: 缺少 API key，不可用。

## Core Paper Table

| Cluster | Paper | Year | Venue/status | Code | Main task | Core mechanism | Node-classification relation | Project relation | Closest-work risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Classic GCL | DGI: Deep Graph Infomax | 2019 | ICLR, peer-reviewed | yes/likely | node classification | global-local MI maximization | classic transductive node SSL baseline | establishes pre-GRACE SSL baseline | any MI-style method must compare historically |
| Classic GCL | MVGRL | 2020 | ICML, peer-reviewed | yes/likely | node/graph classification | contrast node/graph views from diffusion | node classification benchmark baseline | diffusion view competitor | diffusion already handles structure signal |
| Classic GCL | GRACE: Deep Graph Contrastive Representation Learning | 2020 | arXiv / widely used | yes | node classification | random edge/feature drop + InfoNCE | directly targeted | baseline for augmentation GCL | simple augmentation can be strong |
| Classic GCL | GCA: Graph Contrastive Learning with Adaptive Augmentation | 2021 | WWW, peer-reviewed | yes | node classification | topology/feature-aware augmentation | directly targeted | closest augmentation-aware baseline | adaptive augmentation may cover many simple gap claims |
| Information GCL | InfoGCL | 2021 | NeurIPS poster | unclear | graph/node classification | information bottleneck view of GCL | includes node tasks | closest theory/unification work | general IB framing may overlap mechanism claims |
| False negatives | ProGCL | 2021/2022 | ICML, peer-reviewed | yes | node/graph classification | probability-aware hard negative mining | directly relevant to node contrast | closest false-negative risk | any negative mining idea must beat or differ from ProGCL |
| Negative-free | BGRL | 2021/2022 | ICLR, peer-reviewed | yes | node classification, large graphs | BYOL-style bootstrapping | directly targeted | negative-free baseline | already removes negatives and scales |
| Negative-free | CCA-SSG | 2021 | arXiv / graph SSL | yes/unclear | node classification | CCA/correlation objective | directly targeted | no-negative baseline | decorrelation objective already tested |
| Negative-free | Graph Barlow Twins | 2021 | arXiv / peer status unclear | yes/unclear | node/graph tasks | Barlow Twins on graphs | relevant | redundancy-reduction baseline | simple transfer already exists |
| Augmentation-free | AFGRL | 2023 | AAAI, peer-reviewed | yes/unclear | node classification | neighbor discovery without augmentation | directly targeted | nearest no-augmentation GCL | may invalidate "augmentation not needed" novelty |
| Masked graph | GraphMAE | 2022 | KDD, peer-reviewed | yes | node classification | masked feature reconstruction | directly targeted | strong non-contrastive SSL competitor | masked reconstruction may outperform GCL |
| Masked graph | MaskGAE | 2022 | arXiv / CoRR | yes/unclear | link prediction, node classification | masked edge modeling in GAE | relevant | connects GAE and CL | edge masking may already cover structure prediction |
| Masked graph | GraphMAE2 | 2023 | WWW, peer-reviewed | yes | node classification, OGB | remask decoding + latent prediction | directly targeted | strongest masked SSL competitor | latent prediction primitive already used |
| Heterophily | HLCL: Graph CL under Heterophily via Graph Filters | 2023 | ICLR submission / arXiv, status unclear from search | unclear | node classification | high/low-pass graph filters | directly targeted for heterophily | closest heterophily-aware GCL | graph filters may cover spectral heterophily gap |
| Heterogeneous/false negative | Homophily-aware Heterogeneous GCL | 2025 | arXiv preprint | unclear | heterogeneous node representation | homophily-aware false-negative mitigation | relevant but heterogeneous | recent parallel risk | may overlap false-negative + homophily axis |
| Imbalance/TAG | CM-GCL | 2022 | NeurIPS accept via OpenReview | yes | imbalanced node classification | node-text modality + pruning | directly node classification | closest multimodal/imbalance GCL | text modality already used to form positives |
| Task-oriented views | G-Censor | 2023 | ICLR submission / status unclear | promised/unclear | node property prediction | counterfactual task-oriented views | directly targeted | closest task-oriented augmentation | strong risk for counterfactual view claims |
| Directed graphs | Directed Graph Contrastive Learning | 2023/2024 | OpenReview hit, status unclear | unclear | directed node tasks | Laplacian perturbation/curriculum | relevant under directed setting | structure-preserving augmentation risk | not core unless directed graphs included |
| Robust/noise | SIGNNAP | 2020/2023 | arXiv | yes | node classification | stability and identifiability under perturbation | directly relevant | robustness baseline | already contrasts perturbation stability |
| LLM/TAG | LangGSL | 2024 | arXiv | unclear | robust node representation | LLM features/pseudo-labels + GSL | TAG node classification | closest LLM semantic prior risk | may cover LLM-cleaned features |
| Recent hard negative | Khan-GCL | 2025 | arXiv preprint | unclear | graph/node tasks unclear | KAN + semantic hard negatives | relevant but not enough protocol clarity | recent parallel hard-negative risk | recent arXiv, not peer-confirmed |
| Positive mining | SPGCL | 2026 | arXiv preprint | unclear | node classification | positive sample selection | very relevant but future/preprint | parallel positive-construction risk | must not overclaim novelty without checking |

## Category Notes

1. 经典 GCL：DGI/MVGRL/GRACE/GCA 定义主 baseline floor。
2. 近三年节点分类：AFGRL、GraphMAE2、HLCL、CM-GCL、LangGSL、Khan-GCL、SPGCL 是重点风险池。
3. Augmentation-based GCL：GRACE/GCA/RGCL/G-Censor 说明“更好增强”本身已拥挤。
4. Positive / negative construction：ProGCL、SPGCL、CM-GCL、counterfactual views 是高风险 closest works。
5. False positive / false negative：false negative 已有 ProGCL；false positive、semantic-positive 仍缺系统协议。
6. Negative-free / bootstrap：BGRL、CCA-SSG、GBT、AFGRL 说明不能只声称“无负样本”。
7. Masked graph modeling：GraphMAE/GraphMAE2/MaskGAE 是非对比 SSL 的强竞争簇。
8. Prototype / clustering：SwAV/DINO primitive 在 GCL 中已有部分迁移，但节点分类协议常不统一。
9. Homophily / heterophily：HLCL 是核心风险；需要按 graph regime 分析而非只加 spectral filter。
10. Structural noise / robustness：SIGNNAP、LangGSL、robust GSL/TAG 工作说明噪声处理要区分结构噪声和语义噪声。
11. Low-label node classification：few-shot/transductive probing和标签稀缺工作相关，但不能替代主 GCL 协议。
12. Cross-domain graph representation：GCC/G5/IRM-style transfer有启发，主论文需谨慎扩展。
13. LLM/text semantics：TAG/LLM 方向有潜力，但 contamination、pseudo-label leakage、split consistency 是主要风险。
14. 视觉/文本 SSL 迁移：最值得保留 latent prediction、prototype balancing、confidence/noise estimation、worst-group reporting。

## OpenReview Supplement

| Title | Year | Venue/status | OpenReview | Code | Review visibility | Relation | Novelty risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CM-GCL | 2022 | NeurIPS Accept | https://openreview.net/forum?id=f_kvHrM4Q0 | https://github.com/graphprojects/CM-GCL | reviews not extracted by helper | imbalanced node classification with node-text contrast | high for multimodal GCL |
| InfoGCL | 2021 | NeurIPS Poster | https://openreview.net/forum?id=519VBzfEaKW | unclear | reviews not extracted | information-aware unification | medium-high |
| HLCL | 2023 | Submitted to ICLR 2023 / UNCLEAR acceptance | https://openreview.net/forum?id=NzcUQuhEGef | unclear | reviews not extracted | heterophily-aware GCL | high |
| G-Censor | 2023 | Submitted to ICLR 2023 / UNCLEAR acceptance | https://openreview.net/forum?id=LiWGbK8_iOB | unclear/promised | reviews not extracted | task-oriented counterfactual views | high |
| Transductive Linear Probing | 2022 | LoG Oral | https://openreview.net/forum?id=dK8vOIBENa3 | unclear | reviews not extracted | few-shot node classification with GCL pretraining | medium |
| Directed Graph Contrastive Learning | 2023/2024 | OpenReview hit / UNCLEAR | https://openreview.net/forum?id=yLEcG62ANX | unclear | reviews not extracted | directed graph view generation | medium if directed graphs used |

## Closest-Work Risks

- Any positive/negative construction claim must be separated from ProGCL, SPGCL, CM-GCL, and G-Censor.
- Any heterophily claim must be separated from HLCL and supervised heterophily GNN baselines.
- Any negative-free claim must be separated from BGRL, CCA-SSG, Graph Barlow Twins, and AFGRL.
- Any masked/predictive claim must benchmark GraphMAE2 and MaskGAE under identical evaluator/split.
- Any LLM semantic-prior claim must avoid leakage and compare against LangGSL/TAG baselines.
