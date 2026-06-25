# Stage 1 Literature Report

## 1. Sources Used

- Project files: `AGENTS.md`, `RESEARCH_BRIEF.md`, `BENCHMARK_PROTOCOL.md`, `STAGE0_REPORT.md`, `research-wiki/log.md`, `research-wiki/gap_map.md`, `research-wiki/query_pack.md`.
- arXiv helper: successful; searched GCL, masked graph modeling, heterophily/false-negative, and LLM/TAG queries.
- arXiv download: successful; downloaded GRACE, GCA, ProGCL, BGRL, GraphMAE PDFs to `papers/`.
- OpenReview helper: partially successful; retrieved hits including CM-GCL, InfoGCL, HLCL, G-Censor, Transductive Linear Probing, Directed GCL.
- WebSearch/WebFetch: used for cross-checking official/public web presence and cross-domain SSL primitives.
- Local library: initially empty.

## 2. Unavailable or Under-Covered Sources

- Semantic Scholar: unavailable due HTTP 429 rate limiting; venue/citation metadata coverage is incomplete.
- DeepXiv: unavailable because `deepxiv` CLI is not installed, despite ARIS wrapper existing.
- Exa: unavailable because `EXA_API_KEY` is not configured.
- OpenReview: partially rate-limited; some query directions returned empty files after 429. Status/review visibility is therefore marked `UNCLEAR` when not directly observed.

Impact: Stage 1 is sufficient for gap mapping and closest-work risk screening, but not sufficient for final related-work completeness or SOTA claims.

## 3. Core Papers Found

Core/high-risk papers recorded or summarized: 20+.

Key wiki-ingested papers include GRACE, GCA, ProGCL, BGRL, GraphMAE, CCA-SSG, Graph Barlow Twins, LangGSL, Homophily-aware Heterogeneous GCL, Khan-GCL, SPGCL, Debiased Contrastive Learning, I-JEPA and IRM.

OpenReview high-risk hits include CM-GCL, InfoGCL, HLCL and G-Censor.

## 4. Highest-Relevance Clusters

- Classic GCL baselines: DGI, MVGRL, GRACE, GCA.
- Positive/negative construction: ProGCL, SPGCL, CM-GCL, G-Censor.
- Negative-free / bootstrap: BGRL, CCA-SSG, Graph Barlow Twins, AFGRL.
- Masked/predictive graph SSL: GraphMAE, GraphMAE2, MaskGAE.
- Homophily / heterophily: HLCL and heterophily-aware GCL lines.
- Robustness / structural noise: SIGNNAP, GCA-style adaptive augmentation, LangGSL.
- LLM/TAG semantic prior: LangGSL, CM-GCL and related TAG/LLM graph learning.
- Transfer primitives: debiased contrastive learning, BYOL/SimSiam, Barlow Twins/VICReg, MAE/iBOT/I-JEPA, SwAV/DINO, Co-teaching/confident learning, IRM/GroupDRO.

## 5. Highest-Risk Closest Works

1. ProGCL: directly targets false negatives and hard negatives.
2. GCA: directly targets adaptive graph augmentation.
3. BGRL / CCA-SSG / Graph Barlow Twins: cover negative-free GCL.
4. GraphMAE2 / MaskGAE: strong masked graph modeling alternatives.
5. HLCL: closest heterophily-aware GCL work.
6. CM-GCL: closest multimodal / imbalanced node-classification GCL.
7. G-Censor: task-oriented counterfactual positive/negative views.
8. LangGSL: LLM semantic prior + graph structure learning.
9. SPGCL / Khan-GCL: recent arXiv parallel work around positives/hard negatives.

## 6. Most Important Gaps

- G1 semantic false positives in node-level GCL.
- G2 false negatives under homophily/heterophily shift.
- G3 masked graph modeling vs GCL under identical frozen evaluator.
- G4 collapse diagnostics for negative-free graph SSL.
- G5 heterophily-aware GCL boundary conditions.
- G6 leakage-safe LLM semantic priors for TAG/GCL.
- G7 worst-group robustness reporting.
- G8 cross-domain generalization under-specified.

## 7. Top Transfer Mechanisms

1. False-negative probability estimation.
2. Alignment-uniformity by graph regime.
3. Latent target prediction.
4. Teacher-student pseudo-targets with confidence audits.
5. Balanced prototype assignment.
6. Variance/covariance collapse prevention.
7. Robust sample selection for noisy positives/edges.
8. Invariant/worst-group evaluation.
9. Leakage-safe LLM/text semantic supervision.
10. Raw reconstruction vs latent prediction ablations.

## 8. Already Used vs Under-Validated Transfer

Already used in GCL: InfoNCE, stochastic/adaptive augmentation, hard-negative mining, bootstrap/no-negative learning, decorrelation, masked feature/edge modeling.

Under-validated: false-positive auditing, latent predictive targets under identical GCL evaluator, worst-group reporting over graph regimes, leakage-safe LLM semantic priors, and explicit collapse/oversmoothing diagnostics for negative-free graph SSL.

## 9. Experimental Protocol Inconsistencies

- Planetoid public splits, random splits, Wiki-CS splits, OGB official splits and heterophily fixed splits are often mixed in literature summaries.
- Many papers do not clearly expose seeds, early stopping, or `test@best validation epoch` in abstracts/snippets.
- Some methods use frozen linear probing; others fine-tune or alter features/graph structure.
- LLM/TAG papers change the input information source, so feature and leakage audits are mandatory.

## 10. Directly Comparable Public Results

None are marked directly comparable from Stage 1 alone.

Can be historical references: DGI, MVGRL, GRACE, GCA, BGRL, CCA-SSG, GraphMAE, GraphMAE2.

Cannot compare yet without exact protocol check or rerun: ProGCL, HLCL, CM-GCL, G-Censor, LangGSL, Khan-GCL, SPGCL and most recent OpenReview/arXiv hits.

## 11. Research-Wiki Updates

- Added/updated `research-wiki/papers/` entries for core GCL, masked graph, LLM/TAG and transfer-primitive papers.
- Added `research-wiki/papers/STAGE1_PAPER_AUDIT.md`.
- Updated `research-wiki/gap_map.md` with G1-G8.
- Updated `research-wiki/query_pack.md` for future `/idea-creator` use.
- Updated `research-wiki/log.md` with Stage 1 activity.

## 12. Stage 2 Recommendation

Recommend entering Stage 2 idea-discovery: YES, with constraints.

Stage 2 should start from gap candidates and closest-work risks, not from a preselected final method. It must keep the non-goal banlist: no simple gate/reweighting/adapter/residual/temperature-only tricks.

## 13. Missing Information

- Exact protocol extraction from core PDFs is still needed before formal experiments.
- Semantic Scholar / DeepXiv / Exa coverage should be retried when rate/API/CLI issues are fixed.
- OpenReview status and reviews need venue-specific follow-up for 2024-2026 submissions.

## Verdict

GO
