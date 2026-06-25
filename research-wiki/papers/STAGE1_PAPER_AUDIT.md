# Stage 1 Paper Audit

本页补充 `research-wiki/papers/*.md` 中核心条目的 Stage 1 审计字段。若当前只看到题名、摘要或 OpenReview 检索片段，则不标为充分精读。

| Paper | Wiki entry | Peer status | Official code | Split explicit | Directly comparable under project protocol | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| GRACE | `zhu2020_deep_graph_contrastive` | arXiv / widely used | yes | UNCLEAR | no | 已下载 PDF；需精读实验节确认 splits/seeds/test@best |
| GCA | `zhu2020_graph_contrastive_learning` | WWW 2021 | yes | UNCLEAR | no | adaptive augmentation closest baseline |
| ProGCL | `xia2021_progcl_rethinking_hard` | ICML 2022 | yes | UNCLEAR | no | false-negative / hard-negative closest work |
| BGRL | `thakoor2021_largescale_representation_learning` | ICLR 2022 | yes | UNCLEAR | no | negative-free bootstrap closest baseline |
| GraphMAE | `hou2022_graphmae_selfsupervised_masked` | KDD 2022 | yes | UNCLEAR | no | masked graph modeling competitor |
| CCA-SSG | `zhang2021_from_canonical_correlation` | arXiv / graph SSL | yes/UNCLEAR | UNCLEAR | no | negative-free/decorrelation baseline |
| Graph Barlow Twins | `bielak2021_graph_barlow_twins` | arXiv / status UNCLEAR | yes/UNCLEAR | UNCLEAR | no | redundancy-reduction baseline |
| LangGSL | `su2024_bridging_large_language` | arXiv preprint | UNCLEAR | UNCLEAR | no | LLM/TAG closest-work risk |
| Homophily-aware Heterogeneous GCL | `wang2025_homophilyaware_heterogeneous_graph` | arXiv preprint | UNCLEAR | UNCLEAR | no | false-negative + heterophily recent risk |
| Khan-GCL | `wang2025_khangcl_kolmogorovarnold_network` | arXiv preprint | UNCLEAR | UNCLEAR | no | recent hard-negative preprint |
| SPGCL | `shan2026_revisiting_positive_samples` | arXiv preprint | UNCLEAR | UNCLEAR | no | positive-sample construction recent risk |
| Debiased Contrastive Learning | `chuang2020_debiased_contrastive_learning` | NeurIPS 2020 | yes/UNCLEAR | n/a | n/a | transfer primitive, not graph paper |
| I-JEPA | `assran2023_selfsupervised_learning_from` | CVPR 2023 | yes/UNCLEAR | n/a | n/a | latent prediction transfer primitive |
| IRM | `arjovsky2019_invariant_risk_minimization` | arXiv | yes/UNCLEAR | n/a | n/a | OOD/invariance transfer primitive |

## OpenReview-Only / Non-Wiki High-Risk Hits

| Title | Status | Link | Code | Main review visibility | Project risk |
| --- | --- | --- | --- | --- | --- |
| CM-GCL | NeurIPS 2022 Accept | https://openreview.net/forum?id=f_kvHrM4Q0 | https://github.com/graphprojects/CM-GCL | not extracted | multimodal / imbalanced node classification |
| InfoGCL | NeurIPS 2021 Poster | https://openreview.net/forum?id=519VBzfEaKW | UNCLEAR | not extracted | information-aware GCL unification |
| HLCL | Submitted to ICLR 2023 / acceptance UNCLEAR in current pass | https://openreview.net/forum?id=NzcUQuhEGef | UNCLEAR | not extracted | heterophily-aware GCL |
| G-Censor | Submitted to ICLR 2023 / acceptance UNCLEAR in current pass | https://openreview.net/forum?id=LiWGbK8_iOB | promised/UNCLEAR | not extracted | task-oriented counterfactual views |

## Direct Comparability Decision

No published result is marked directly comparable yet. Any SOTA or superiority claim must rerun baselines under `BENCHMARK_PROTOCOL.md` or prove exact split/evaluator/seed/test@best equivalence.
