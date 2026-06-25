# Stage 1.5 Paper Audit

No paper is marked directly comparable under the project protocol.

| Paper | Wiki entry | Status | Code | Protocol recovered | Still UNCLEAR | Directly comparable | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GRACE | `zhu2020_deep_graph_contrastive` | arXiv / classic | yes | random 10/10/80 for citation; frozen logistic; 20 runs; fixed epochs | exact seeds, test@best | no | must rerun |
| GCA | `zhu2020_graph_contrastive_learning` | WWW 2021 | yes | Wiki-CS public; others 10/10/80; frozen logistic; 20 runs | early stopping, test@best | no | high augmentation risk |
| ProGCL | `xia2021_progcl_rethinking_hard` | ICML 2022 | yes | follows GCA/BGRL style; 20 random splits/model initializations for reproduced baselines | exact seed list, early stopping, test@best | no | high false-negative risk |
| BGRL | `thakoor2021_largescale_representation_learning` | ICLR 2022 | yes | WikiCS canonical; Amazon/Coauthor 10/10/80; OGB official; frozen linear/logistic | test@best mostly unclear | no | S2 metadata recovered |
| CCA-SSG | `zhang2021_from_canonical_correlation` | arXiv | yes/UNCLEAR | public citation; 1:1:9 main text vs 10/10/80 appendix for others; frozen logistic | split ambiguity, early stopping | no | rerun required |
| Graph Barlow Twins | `bielak2021_graph_barlow_twins` | arXiv / UNCLEAR | yes/UNCLEAR | partial dataset info | evaluator/seeds/splits | no | still D-class |
| AFGRL | `lee2021_augmentationfree_selfsupervised_learning` | AAAI 2022 | yes | WikiCS canonical; Amazon/Coauthor 10/10/80; logistic; validation-best test | exact seed list | no | blocks augmentation-free positive mining |
| GraphMAE | `hou2022_graphmae_selfsupervised_masked` | KDD 2022 | yes | public citation splits; OGB official; frozen linear classifier; 20 random initializations | test@best | no | strong MGM baseline |
| GraphMAE2 | `hou2023_graphmae2_decodingenhanced_masked` | WWW 2023 | yes | OGB official; MAG 5/5/40; 10 trials | early stopping, frozen/fine-tune separation | no | latent prediction risk |
| MaskGAE | `li2022_whats_behind_mask` | arXiv/CoRR | yes/UNCLEAR | Photo/Computer node classification uses 1:1:8 random split | evaluator/seeds/test@best | no | more link-prediction centered |
| HLCL | `yang2023_graph_contrastive_learning` | arXiv/OpenReview UNCLEAR | UNCLEAR | datasets recovered | exact splits/evaluator/seeds/status | no | high heterophily risk |
| CM-GCL | audit-only | NeurIPS 2022 | yes | 70/10/20; ten runs; fine-tunes GNN; Macro-F1/AUC | exact early stopping | no | not frozen evaluator |
| G-Censor | audit-only | OpenReview ICLR 2023 submission; status UNCLEAR | promised/UNCLEAR | OOD split by Node2Vec clusters; IID table datasets | IID split, seeds, early stopping | no | high task-oriented view risk |
| LangGSL | `su2024_bridging_large_language` | arXiv 2024 | UNCLEAR | datasets recovered | split/evaluator/seeds/leakage protocol | no | LLM/TAG risk |
| SPGCL | `shan2026_revisiting_positive_samples` | arXiv 2026 | UNCLEAR | some heterophily split sources recovered | evaluator/seeds/early stopping | no | recent positive-sample risk |
| Khan-GCL | `wang2025_khangcl_kolmogorovarnold_network` | arXiv 2025 | UNCLEAR | 10 runs and test@best validation for downstream ROC-AUC | node-classification relevance/protocol | no | less central to node classification |

## S2 Recovery

Semantic Scholar recovered BGRL metadata: ICLR venue, arXiv id `2102.06514`, citationCount 324, and S2 URL. Other core queries hit HTTP 429 and were not repeatedly retried.

## OpenReview Status

CM-GCL: accepted NeurIPS 2022. InfoGCL: NeurIPS 2021 Poster. Transductive Linear Probing: LoG 2022 Oral. Directed GCL: NeurIPS 2021 Poster. HLCL and G-Censor remain `UNCLEAR` for final acceptance status in this pass.

## Stage 1.6 DeepXiv Addendum

DeepXiv raw evidence is stored in `notes/stage1_6_deepxiv/`.

Newly strengthened risk boundaries:

- SPGCL (`2606.10284`): strongest recent positive-sample risk. DeepXiv confirms frozen linear evaluation, ten repeats and ablations, but exact saved split files and seed identities remain missing.
- LangGSL (`2410.12096`): strongest LLM/TAG semantic-prior risk. DeepXiv confirms TR/TI robustness and LLM/GSLM comparisons, but leakage-safe protocol remains unresolved.
- MaskGAE (`2205.10053`): node classification protocol is clearer for Photo/Computer 1:1:8 and frozen linear classifier, but still not directly comparable.
- GCA/CCA-SSG/AFGRL: DeepXiv confirms important evaluator/split details, but no result meets project direct-comparability requirements.

Audit verdict remains: A-class direct comparability is empty.
