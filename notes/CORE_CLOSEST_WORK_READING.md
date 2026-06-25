# Core Closest Work Reading

Fields are set to `UNCLEAR` when the PDF/page did not explicitly say it in this pass. No published result is marked directly comparable under our protocol.

## GRACE

- Paper: Deep Graph Contrastive Representation Learning
- Status: arXiv / widely used GCL baseline
- Official code: yes
- Main task: transductive and inductive node classification
- Core problem: learn node representations with contrastive agreement between augmented graph views
- Core mechanism: random edge dropping and feature masking with node-level contrastive loss
- Strategy: positive pairs are same node across two augmented views; negatives are other nodes
- Augmentation: edge removal and feature masking
- Encoder and evaluator: GNN encoder; frozen embeddings with L2-regularized logistic regression
- Datasets: Cora, CiteSeer, PubMed, DBLP, Reddit, PPI
- Split protocol: citation networks use random 10%/10%/80%; inductive datasets use their task splits
- Seeds: classifier/model run 20 runs; exact seed list UNCLEAR
- Early stopping: fixed pretraining epochs; early stopping UNCLEAR
- Metric: accuracy for transductive, micro-F1 for inductive
- test@best or final: final/evaluation after training; test@best validation epoch UNCLEAR
- Main result: strong node classification baseline
- Ablations: augmentation and objective variants
- Author limitations: graph augmentation choices matter
- Observed limitations: not directly comparable to project protocol unless split files and seed list are reproduced
- Closest-work risk: blocks simple stochastic augmentation novelty
- What idea is blocked: "random graph augmentations + InfoNCE is enough"
- Remaining gap: semantic validity of positives and regime-specific failure
- Need further reading: no for Stage 1.5; yes before formal baseline implementation

## GCA

- Paper: Graph Contrastive Learning with Adaptive Augmentation
- Status: WWW 2021 peer-reviewed
- Official code: yes
- Main task: node classification
- Core problem: uniform random augmentations can destroy important graph semantics
- Core mechanism: topology/feature-aware adaptive augmentation
- Strategy: same-node positives across adaptive views, contrastive negatives
- Augmentation: centrality-/feature-aware edge and feature perturbations
- Encoder and evaluator: frozen embeddings with L2-regularized logistic regression
- Datasets: Wiki-CS, Amazon-Computers, Amazon-Photo, Coauthor-CS, Coauthor-Physics
- Split protocol: Wiki-CS public splits; other four random 10%/10%/80%
- Seeds: 20 runs/different splits; exact seed list UNCLEAR
- Early stopping: UNCLEAR
- Metric: accuracy
- test@best or final: UNCLEAR
- Main result: adaptive augmentation improves GCL
- Ablations: topology and attribute adaptive components
- Author limitations: dataset-dependent augmentation
- Observed limitations: directly overlaps with augmentation-quality claims
- Closest-work risk: high for any "better augmentation" claim
- Blocked idea: centrality/feature-aware random augmentation as main contribution
- Remaining gap: semantic positive validity and false-positive audit
- Need further reading: no for Stage 1.5

## ProGCL

- Paper: ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning
- Status: ICML 2022 peer-reviewed
- Official code: yes
- Main task: transductive/inductive node classification and OGB
- Core problem: hard negative mining can select false negatives
- Core mechanism: estimate true/false negative distributions and reweight/mix negatives
- Strategy: probability-aware hard negatives
- Augmentation: inherits GCL augmentations from base frameworks
- Encoder and evaluator: embeddings with logistic classifier
- Datasets: Amazon-Photo, Amazon-Computers, Wiki-CS, Coauthor-CS, Reddit, Flickr, ogbn-Arxiv
- Split protocol: follows GCA/BGRL for transductive/inductive tasks; ogbn-Arxiv follows BGRL/OGB convention
- Seeds: reproduced baselines use 20 random splits/model initializations; exact seed list UNCLEAR
- Early stopping: BMM fitting epoch specified; downstream early stopping UNCLEAR
- Metric: accuracy / micro-F1
- test@best or final: UNCLEAR
- Main result: improves over hard-negative baselines
- Ablations: weighting/mixing and starting epoch
- Author limitations: depends on distribution estimation
- Observed limitations: false-positive side remains less addressed
- Closest-work risk: very high for false-negative/hard-negative ideas
- Blocked idea: generic false-negative-aware weighting without stronger novelty
- Remaining gap: regime-conditioned false negatives and semantic positives
- Need further reading: no for Stage 1.5

## BGRL

- Paper: Large-Scale Representation Learning on Graphs via Bootstrapping
- Status: ICLR 2022 peer-reviewed
- Official code: yes
- Main task: node classification at small and large scale
- Core problem: contrastive losses require negatives and scale poorly
- Core mechanism: online/target encoder bootstrapping with predictor
- Strategy: negative-free bootstrap
- Augmentation: graph augmentations, but no negatives
- Encoder and evaluator: frozen linear evaluation with logistic regression; semi-supervised variants also reported
- Datasets: WikiCS, Amazon Computers/Photos, Coauthor CS/Physics, ogbn-Arxiv, PPI, MAG240M
- Split protocol: WikiCS canonical splits; Amazon/Coauthor random 10/10/80; ogbn-Arxiv official chronological split; PPI predefined graph split
- Seeds: 20 random splits/initializations for many small datasets; OGB/MAG runs 3-5 seeds depending experiment
- Early stopping: fixed steps/epochs; exact early stopping mostly UNCLEAR
- Metric: accuracy/F1
- test@best or final: final/linear evaluation; test@best UNCLEAR
- Main result: competitive negative-free large-scale GCL
- Ablations: encoder, predictor, augmentations, scale
- Author limitations: meaningful augmentations still matter
- Observed limitations: collapse diagnostics mostly indirect
- Closest-work risk: high for negative-free claims
- Blocked idea: BYOL-style graph bootstrap as novelty
- Remaining gap: graph-specific collapse/oversmoothing diagnostics
- Need further reading: no for Stage 1.5

## CCA-SSG

- Paper: From Canonical Correlation Analysis to Self-supervised Graph Neural Networks
- Status: arXiv / graph SSL
- Official code: yes/UNCLEAR
- Main task: node classification
- Core problem: avoid negative sampling and MI estimators
- Core mechanism: invariance plus feature decorrelation through CCA-style objective
- Strategy: negative-free/decorrelation
- Augmentation: graph augmentations
- Encoder and evaluator: frozen encoder + logistic regression
- Datasets: Cora, CiteSeer, PubMed, Coauthor CS/Physics, Amazon Computer/Photo
- Split protocol: public splits for Cora/CiteSeer/PubMed; 1:1:9 in main text for other four, appendix says 10/10/80 for Coauthor/Amazon
- Seeds: 20 trials with random splits/initializations for some settings
- Early stopping: UNCLEAR
- Metric: test accuracy
- test@best or final: UNCLEAR
- Main result: competitive negative-free/decorrelation SSL
- Ablations: lambda / objective terms / augmentations
- Author limitations: augmentation still used
- Observed limitations: split statement has ambiguity between 1:1:9 and 10/10/80 phrasing
- Closest-work risk: high for decorrelation/no-negative ideas
- Blocked idea: CCA-like no-negative objective alone
- Remaining gap: collapse diagnostics and protocol-aligned comparison
- Need further reading: yes before formal reproduction

## Graph Barlow Twins

- Paper: Graph Barlow Twins
- Status: arXiv / status UNCLEAR
- Official code: yes/UNCLEAR
- Main task: node classification and graph SSL
- Core problem: transfer redundancy-reduction SSL to graphs
- Core mechanism: cross-correlation identity objective
- Strategy: negative-free redundancy reduction
- Augmentation: graph augmentations
- Encoder and evaluator: UNCLEAR from current pass
- Datasets: WikiCS, PPI, ogbn-products and other graph tasks mentioned
- Split protocol: partly described in PDF but exact node-classification split remains UNCLEAR in current pass
- Seeds: UNCLEAR
- Early stopping: UNCLEAR
- Metric: accuracy/F1
- test@best or final: UNCLEAR
- Main result: graph adaptation of Barlow Twins
- Ablations: augmentation and objective variants likely
- Author limitations: UNCLEAR
- Observed limitations: insufficient protocol clarity for direct comparison
- Closest-work risk: medium for redundancy-reduction ideas
- Blocked idea: direct Barlow Twins transfer
- Remaining gap: robust collapse diagnostics under node classification protocol
- Need further reading: yes

## AFGRL

- Paper: Augmentation-Free Self-Supervised Learning on Graphs
- Status: AAAI 2022 peer-reviewed
- Official code: yes
- Main task: node classification, clustering, similarity search
- Core problem: graph augmentations are arbitrary and hyperparameter-sensitive
- Core mechanism: discover positive nodes using local structural and global semantic constraints
- Strategy: augmentation-free, negative-free positive discovery
- Augmentation: none
- Encoder and evaluator: unsupervised encoder + logistic regression; reports validation-best test performance
- Datasets: WikiCS, Amazon Computers/Photo, Coauthor CS/Physics
- Split protocol: WikiCS canonical 20 splits; Amazon/Coauthor random 10/10/80 for 20 splits
- Seeds: 20 splits; exact seeds UNCLEAR
- Early stopping: evaluates every epoch; reports test when validation best
- Metric: accuracy, NMI, similarity metrics
- test@best or final: test at best validation performance
- Main result: competitive without augmentation/negatives
- Ablations: local/global semantics, candidate discovery
- Author limitations: relies on positive discovery quality
- Observed limitations: blocks naive "remove augmentation" claims
- Closest-work risk: high for augmentation-free positive mining
- Blocked idea: kNN/cluster-positive augmentation-free GCL
- Remaining gap: false-positive audit and regime boundary
- Need further reading: no for Stage 1.5

## GraphMAE

- Paper: GraphMAE
- Status: KDD 2022 peer-reviewed
- Official code: yes
- Main task: node classification and graph classification
- Core problem: contrastive SSL can be unstable; masked graph reconstruction is strong
- Core mechanism: masked feature reconstruction with scaled cosine error
- Strategy: masked graph modeling
- Augmentation: feature masking, not contrastive views
- Encoder and evaluator: frozen encoder + linear classifier; some fine-tuning/LP variants
- Datasets: Cora, CiteSeer, PubMed, ogbn-Arxiv, PPI, Reddit
- Split protocol: public splits for Cora/CiteSeer/PubMed; OGB official for ogbn-Arxiv; others follow standard settings
- Seeds: 20 random initializations for node classification; graph classification 5 runs
- Early stopping: linear classifier trained until convergence in some reproduced results
- Metric: accuracy / F1 / ROC-AUC
- test@best or final: mostly final after linear evaluation; test@best UNCLEAR
- Main result: strong masked graph SSL
- Ablations: mask ratio, SCE vs MSE, re-mask design
- Author limitations: raw reconstruction sensitivity
- Observed limitations: evaluator can differ from GCL baselines
- Closest-work risk: high for masked SSL comparisons
- Blocked idea: simple masked feature reconstruction as new contribution
- Remaining gap: identical evaluator comparison vs GCL
- Need further reading: no for Stage 1.5

## GraphMAE2

- Paper: GraphMAE2
- Status: WWW 2023 peer-reviewed
- Official code: yes
- Main task: large-scale node classification
- Core problem: raw feature reconstruction is vulnerable/noisy
- Core mechanism: multi-view re-mask decoding and latent representation prediction
- Strategy: masked/latent predictive SSL
- Augmentation: masking/re-masking
- Encoder and evaluator: linear probing and fine-tuning settings
- Datasets: ogbn-Arxiv, ogbn-Products, ogbn-Papers100M, MAG-Scholar-F
- Split protocol: official OGB splits for ogbn datasets; MAG-Scholar-F 5%/5%/40%
- Seeds: 10 trials with random seeds
- Early stopping: UNCLEAR
- Metric: accuracy
- test@best or final: UNCLEAR
- Main result: strong large-scale graph SSL
- Ablations: re-mask decoding, latent prediction
- Author limitations: more complex decoder pipeline
- Observed limitations: not directly comparable to frozen GCL unless evaluator aligned
- Closest-work risk: very high for latent prediction gap
- Blocked idea: latent masked graph prediction without stronger distinction
- Remaining gap: fair GCL-vs-MGM protocol comparison
- Need further reading: no for Stage 1.5

## MaskGAE

- Paper: What's Behind the Mask: Understanding Masked Graph Modeling for Graph Autoencoders
- Status: arXiv / CoRR
- Official code: yes/UNCLEAR
- Main task: link prediction and node classification
- Core problem: understand how masking helps graph autoencoders
- Core mechanism: masked edge modeling and theoretical relation to CL
- Strategy: masked graph modeling
- Augmentation: mask edges/paths
- Encoder and evaluator: GAE-style; node classifier details partly UNCLEAR
- Datasets: link prediction datasets plus Photo/Computer for node classification
- Split protocol: link prediction 85/5/10 edge split except Collab public; node classification uses 1:1:8 random split for Photo/Computer
- Seeds: UNCLEAR
- Early stopping: UNCLEAR
- Metric: AUC/AP for links; accuracy for node classification
- test@best or final: UNCLEAR
- Main result: masking improves GAE representations
- Ablations: edge vs path masking
- Author limitations: focused strongly on link prediction
- Observed limitations: node classification protocol narrower than project scope
- Closest-work risk: medium-high for MGM claims
- Blocked idea: masked edge GAE as new main novelty
- Remaining gap: node-classification GCL comparison under identical evaluator
- Need further reading: yes

## HLCL

- Paper: Graph Contrastive Learning under Heterophily via Graph Filters
- Status: arXiv / OpenReview; acceptance status UNCLEAR
- Official code: UNCLEAR
- Main task: homophily and heterophily node classification
- Core problem: standard GCL performs poorly on heterophilic graphs
- Core mechanism: split homophilic/heterophilic subgraphs and contrast low-/high-pass filtered views
- Strategy: heterophily-aware positives/views
- Augmentation: graph filters and feature-similarity-based subgraph construction
- Encoder and evaluator: GCL encoder + projected contrastive views; classifier/evaluator exact details UNCLEAR
- Datasets: Cora, CiteSeer, PubMed, Actor, Chameleon, Squirrel, Penn94, Twitch-gamers, Genius
- Split protocol: exact split UNCLEAR in current pass; likely benchmark-specific, but not marked directly comparable
- Seeds: UNCLEAR
- Early stopping: UNCLEAR
- Metric: accuracy
- test@best or final: UNCLEAR
- Main result: reported gains under heterophily
- Ablations: homophilic/heterophilic subgraph and filters
- Author limitations: relies on feature similarity to infer subgraphs
- Observed limitations: boundary conditions of heterophily types remain open
- Closest-work risk: very high for heterophily-aware GCL
- Blocked idea: simply adding high-/low-pass filters
- Remaining gap: when spectral/filter assumptions fail
- Need further reading: yes

## CM-GCL

- Paper: Co-Modality Graph Contrastive Learning for Imbalanced Node Classification
- Status: NeurIPS 2022 peer-reviewed
- Official code: yes
- Main task: imbalanced node classification
- Core problem: handcrafted augmentations and class imbalance hurt GCL on real graphs
- Core mechanism: inter-modality node-text contrast and intra-modality pruned/non-pruned encoder contrast
- Strategy: multimodal positives and irrelevant node-text negatives
- Augmentation: network pruning for minority mining
- Encoder and evaluator: pretrain/co-train then fine-tune GNN encoder
- Datasets: real node-text/image graphs including Instagram; exact full list in PDF
- Split protocol: 70% train, 10% validation, 20% test
- Seeds: trained ten times
- Early stopping: fixed epoch; early stopping UNCLEAR
- Metric: Macro-F1 and AUC-ROC
- test@best or final: test after training; test@best UNCLEAR
- Main result: improves imbalanced node classification
- Ablations: modality and pruning components
- Author limitations: requires rich node content modality
- Observed limitations: not same frozen evaluator; not directly comparable
- Closest-work risk: high for LLM/TAG and imbalanced GCL
- Blocked idea: using node-text positives without clearer novelty
- Remaining gap: leakage-safe and protocol-aligned semantic priors
- Need further reading: no for Stage 1.5

## G-Censor

- Paper: G-Censor: Graph Contrastive Learning with Task-Oriented Counterfactual Views
- Status: OpenReview ICLR 2023 submission; acceptance status UNCLEAR
- Official code: promised/UNCLEAR
- Main task: node property prediction
- Core problem: optimal contrastive views should be task-oriented
- Core mechanism: counterfactual positive/negative ego-graph views
- Strategy: task-oriented positive/negative view generation
- Augmentation: counterfactual view generation
- Encoder and evaluator: model-agnostic GNN framework; exact frozen/fine-tune status UNCLEAR
- Datasets: CiteSeer, Computers, Cora Full, Cora ML, DBLP, Flickr, Photo, PubMed
- Split protocol: IID results plus OOD split by Node2Vec clustering for generalizability; exact IID split UNCLEAR
- Seeds: UNCLEAR
- Early stopping: UNCLEAR
- Metric: accuracy
- test@best or final: test set accuracy; test@best UNCLEAR
- Main result: improves node property prediction and OOD split
- Ablations: counterfactual components
- Author limitations: acceptance/code status unclear
- Observed limitations: strong task-oriented view closest work
- Closest-work risk: very high for counterfactual view ideas
- Blocked idea: task-oriented counterfactual positives/negatives as sole novelty
- Remaining gap: leakage-safe view quality and relation to frozen GCL evaluator
- Need further reading: yes if Stage 2 selects G1/G2

## LangGSL

- Paper: Bridging Large Language Models and Graph Structure Learning Models for Robust Representation Learning
- Status: arXiv 2024
- Official code: UNCLEAR
- Main task: robust TAG/node representation learning
- Core problem: feature/text noise and structural noise are handled separately
- Core mechanism: LLM/LM features and pseudo-labels mutual-learning with GSLM
- Strategy: semantic supervision; not standard GCL
- Augmentation: graph structure refinement, not GCL augmentation
- Encoder and evaluator: LM + GSLM; not frozen GCL evaluator
- Datasets: Cora, Instagram, PubMed, ogbn-Arxiv and robustness settings
- Split protocol: UNCLEAR in current pass
- Seeds: UNCLEAR
- Early stopping: UNCLEAR
- Metric: accuracy/robustness
- test@best or final: UNCLEAR
- Main result: robust representation under noise
- Ablations: LM/GSLM mutual learning
- Author limitations: requires language/text signal
- Observed limitations: high leakage/contamination audit burden
- Closest-work risk: high for LLM semantic prior gaps
- Blocked idea: naive LLM pseudo-label / text feature injection
- Remaining gap: leakage-safe, split-consistent semantic priors
- Need further reading: yes

## SPGCL

- Paper: Revisiting Positive Samples in Graph Contrastive Learning
- Status: arXiv 2026 preprint
- Official code: UNCLEAR
- Main task: node classification across homophily/heterophily
- Core problem: positive sample selection in GCL
- Core mechanism: energy-guided positive sampling and multi-view representation
- Strategy: positive sample construction
- Augmentation: positive sampling rather than only graph corruption
- Encoder and evaluator: final node embedding used for training/testing; evaluator details UNCLEAR
- Datasets: Cora, CiteSeer, PubMed, Photo, Computers, CS, Actor, Chameleon, Crocodile, Cornell, Texas, Wisconsin
- Split protocol: uses geom-gcn splits for some heterophily datasets; other exact splits UNCLEAR
- Seeds: UNCLEAR
- Early stopping: UNCLEAR
- Metric: accuracy
- test@best or final: UNCLEAR
- Main result: recent positive-sample preprint
- Ablations: positive sampling components likely
- Author limitations: very recent, not peer-confirmed
- Observed limitations: strong parallel risk but protocol unclear
- Closest-work risk: high for positive construction
- Blocked idea: energy/positive-sample selection without clear delta
- Remaining gap: semantic positives and protocol-aligned validation
- Need further reading: yes

## Khan-GCL

- Paper: Khan-GCL
- Status: arXiv 2025 preprint
- Official code: UNCLEAR
- Main task: graph-level and transfer tasks; node classification relevance limited/UNCLEAR
- Core problem: MLP encoder capacity and hard negative quality
- Core mechanism: KAN encoder and coefficient-derived hard negatives
- Strategy: hard negatives
- Augmentation: semantically meaningful hard negative construction
- Encoder and evaluator: KAN-based GCL; exact node evaluator UNCLEAR
- Datasets: molecular/social graph benchmarks; node task relevance UNCLEAR
- Split protocol: downstream test ROC-AUC at best validation epoch for molecular transfer; node split UNCLEAR
- Seeds: 10 runs for downstream experiment
- Early stopping: best validation epoch for downstream ROC-AUC
- Metric: ROC-AUC / task-specific
- test@best or final: test@best validation epoch for downstream transfer
- Main result: recent preprint claims SOTA
- Ablations: KAN and hard negative components
- Author limitations: recent unreviewed evidence
- Observed limitations: not central to node classification unless graph-level transfer enters scope
- Closest-work risk: medium for hard-negative/KAN direction
- Blocked idea: KAN + hard negatives as main novelty
- Remaining gap: node-classification-specific hard-negative semantics
- Need further reading: no unless Stage 2 targets hard negatives

## Stage 1.6 DeepXiv Addendum

Raw evidence: `notes/stage1_6_deepxiv/`.

DeepXiv confirmed the following high-risk details:

- GCA: Wiki-CS uses public splits; Amazon/Coauthor use random 10/10/80; frozen logistic regression is used; results are averaged over 20 runs.
- CCA-SSG: appendix states public citation splits and 10/10/80 for Coauthor/Amazon datasets with logistic regression; split ambiguity remains because the main/appendix protocol is not identical.
- AFGRL: uses logistic regression on learned embeddings and reports test performance when validation performance is best; exact seed list remains unclear.
- MaskGAE: node classification on Photo/Computer uses 1:1:8 random splits and frozen linear classifier on embeddings; exact seeds/test@best remain unclear.
- SPGCL: uses homophily and heterophily node classification, standard GCN backbone for SSL baselines, frozen linear classifier, ten repeats, and ablations for energy-aware propagation / energy-guided positive sampling. Exact saved splits and seed identities remain unclear.
- LangGSL: uses LLM/LM and GSLM mutual learning for TAG/node classification and robustness; it is not a standard frozen GCL evaluator and remains leakage-risky.
- Graph Barlow Twins: no-negative/decorrelation risk is confirmed, but evaluator/split/seed details remain insufficient for direct comparability.

No paper is promoted to directly comparable. Stage 2 must still rerun selected baselines under project split JSON, seed list, evaluator and `test@best validation epoch`.
