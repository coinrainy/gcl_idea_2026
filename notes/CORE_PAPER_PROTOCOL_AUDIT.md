# Core Paper Protocol Audit

Classification labels:

- A: Directly comparable under our protocol.
- B: Historical reference only.
- C: Must rerun under our protocol.
- D: Protocol still unclear.

Default is not A. No paper below is marked directly comparable.

| Paper | Datasets | Split | Planetoid public? | 1:1:8? | Wiki-CS? | OGB? | Heterophily fixed? | Evaluator | Frozen/fine-tune | Seeds | Early stopping | test@best/final | Code | Class | Must rerun / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GRACE | Cora/CiteSeer/PubMed/DBLP/Reddit/PPI | citation random 10/10/80; inductive predefined | no | yes for citation | no | no | no | L2 logistic regression | frozen | 20 runs | fixed epochs | final/UNCLEAR | yes | C | rerun with saved split JSON and project seed list |
| GCA | Wiki-CS, Amazon, Coauthor | Wiki-CS public; others 10/10/80 | no | yes for Amazon/Coauthor | public splits | no | no | L2 logistic regression | frozen | 20 runs | UNCLEAR | UNCLEAR | yes | C | align exact split seeds/test@best |
| ProGCL | Amazon, Wiki-CS, Coauthor, Reddit, Flickr, ogbn-Arxiv | follows GCA/BGRL; OGB for ogbn-Arxiv | no | yes for some | likely/follows GCA | official for ogbn-Arxiv | no | logistic classifier | frozen | 20 random for reproduced baselines | UNCLEAR | UNCLEAR | yes | C/D | rerun; exact seeds and early stopping unclear |
| BGRL | WikiCS, Amazon, Coauthor, ogbn-Arxiv, PPI, MAG240M | WikiCS canonical; Amazon/Coauthor 10/10/80; OGB official; PPI predefined | no | yes for Amazon/Coauthor | canonical | official | no | logistic/linear model | frozen for main SSL eval; semi-supervised also | 20 small, 3-5 large | fixed steps mostly | final/UNCLEAR | yes | C | rerun GCL table; separate semi-supervised |
| CCA-SSG | Cora/CiteSeer/PubMed/Coauthor/Amazon | public citation; 1:1:9 main text vs 10/10/80 appendix for others | yes | ambiguous | no | no | no | logistic regression | frozen | 20 trials in appendix | UNCLEAR | UNCLEAR | yes/UNCLEAR | C/D | resolve split ambiguity and rerun |
| Graph Barlow Twins | WikiCS/PPI/ogbn-products etc. | partially unclear | UNCLEAR | UNCLEAR | yes | yes | no | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | yes/UNCLEAR | D | need deeper protocol extraction |
| AFGRL | WikiCS, Amazon, Coauthor | WikiCS canonical; Amazon/Coauthor 10/10/80 for 20 splits | no | yes for Amazon/Coauthor | canonical | no | no | logistic regression | frozen | 20 splits | validation-best reported | test at best validation | yes | C | rerun under project split/evaluator |
| GraphMAE | Cora/CiteSeer/PubMed/ogbn-Arxiv/PPI/Reddit | public splits for citation; OGB official | yes | no | no | official ogbn-Arxiv | no | linear classifier | frozen and some FT/LP variants | 20 init for node | classifier to convergence; early stopping UNCLEAR | final/UNCLEAR | yes | B/C | rerun frozen-evaluator GCL comparison |
| GraphMAE2 | ogbn-Arxiv/Products/Papers100M/MAG-Scholar-F | OGB official; MAG 5/5/40 | no | no | no | official | no | linear probing and fine-tuning | both | 10 random seeds | UNCLEAR | UNCLEAR | yes | B/C | compare only after evaluator alignment |
| MaskGAE | Photo/Computer for node; link datasets | node uses 1:1:8 random split for Photo/Computer | no | yes for Photo/Computer | no | no | no | GAE/classifier details UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | yes/UNCLEAR | D | need exact evaluator/seeds |
| HLCL | Cora/CiteSeer/PubMed/Actor/Chameleon/Squirrel/Penn94/Twitch/Genius | exact split UNCLEAR | UNCLEAR | UNCLEAR | no | no | likely benchmark fixed for heterophily, but not confirmed | GCL/classifier UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | D | need exact splits/evaluator |
| CM-GCL | real multimodal/imbalanced graphs | 70/10/20 | no | no | no | no | no | fine-tuned GNN encoder | fine-tuning | 10 runs | fixed epoch / UNCLEAR | final/UNCLEAR | yes | B/C | not frozen evaluator; rerun only if TAG/imbalance scope |
| G-Censor | CiteSeer, Computers, Cora Full, Cora ML, DBLP, Flickr, Photo, PubMed | IID split unclear; OOD by Node2Vec clusters | UNCLEAR | UNCLEAR | no | no | no | model-agnostic GNN | likely fine-tune | UNCLEAR | UNCLEAR | test set accuracy | UNCLEAR | D | need accepted version/code/protocol |
| LangGSL | Cora, Instagram, PubMed, ogbn-Arxiv | UNCLEAR | UNCLEAR | UNCLEAR | no | ogbn-Arxiv included | no | LM + GSLM | joint/fine-tune | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | D | leakage-safe rerun required |
| SPGCL | homophily + heterophily node datasets | geom-gcn splits for some; others UNCLEAR | UNCLEAR | UNCLEAR | no | no | yes for some heterophily | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR | D | recent preprint; exact protocol needed |
| Khan-GCL | graph/molecular datasets | graph task splits; node relevance UNCLEAR | no | no | no | no | no | KAN GCL | transfer/fine-tune | 10 runs for downstream | best validation epoch for transfer | test@best validation for ROC-AUC | UNCLEAR | B/D | not direct node-classification baseline |

## Direct Comparability

A bucket is empty. Even when a paper uses 10/10/80, published results still lack our exact saved split files, seed list, and `test@best validation epoch` agreement.

## Highest Priority Reruns Later

GRACE, GCA, ProGCL, BGRL, AFGRL, GraphMAE/GraphMAE2 and HLCL, depending on selected Stage 2 gap.
