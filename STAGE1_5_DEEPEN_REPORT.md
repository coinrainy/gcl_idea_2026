# Stage 1.5 Deepen Report

## 1. Sources Recovered

- arXiv/PDF coverage improved: downloaded and parsed AFGRL, CCA-SSG, Graph Barlow Twins, GraphMAE2, MaskGAE, HLCL, LangGSL, Khan-GCL, SPGCL, InfoGCL, CM-GCL and G-Censor PDFs.
- Semantic Scholar partially recovered: BGRL metadata returned with ICLR venue, arXiv ID, citation count and TLDR.
- OpenReview status improved for Directed GCL and Transductive Linear Probing via web/OpenReview search.

## 2. Sources Still Unavailable

- Semantic Scholar remains rate-limited for most queries: repeated HTTP 429.
- DeepXiv was unavailable during Stage 1.5 because `deepxiv` CLI was not installed; it has since been fixed by installing `deepxiv-sdk==0.3.1` and patching the ARIS adapter for SDK 0.3.1 JSON output.
- Exa remains unavailable: `EXA_API_KEY` is empty.
- OpenReview reviews were not reliably extracted; HLCL and G-Censor final acceptance status remain `UNCLEAR`.

## 3. Compensation

- Used downloaded arXiv PDFs and official conference/OpenReview PDFs.
- Extracted PDF text locally with `pypdf`.
- Used OpenReview/WebSearch snippets for status checks.
- Preserved `UNCLEAR` where exact protocol or decision was not explicit.
- DeepXiv is now available for future supplemental retrieval.

## 4. High-Risk Closest Works Read

Covered: GRACE, GCA, ProGCL, BGRL, CCA-SSG, Graph Barlow Twins, AFGRL, GraphMAE, GraphMAE2, MaskGAE, HLCL, CM-GCL, G-Censor, LangGSL, SPGCL and Khan-GCL.

## 5. Protocol Fields Clarified

- GRACE: random 10/10/80 citation split, frozen logistic evaluator, 20 runs, fixed epochs.
- GCA: Wiki-CS public splits; other datasets random 10/10/80; frozen logistic evaluator; 20 runs.
- ProGCL: follows GCA/BGRL-style splits; reproduced baselines use 20 random splits/model initializations.
- BGRL: WikiCS canonical, Amazon/Coauthor random 10/10/80, OGB official, PPI predefined; frozen linear evaluation.
- CCA-SSG: public citation splits; main text says 1:1:9 for other datasets, appendix says 10/10/80.
- AFGRL: WikiCS canonical; Amazon/Coauthor 10/10/80; validation-best test; logistic regression.
- GraphMAE: public citation splits and OGB official; frozen linear classifier; 20 random initializations.
- GraphMAE2: OGB official splits; MAG-Scholar-F 5/5/40; 10 trials.
- MaskGAE: Photo/Computer node classification uses 1:1:8 random split.
- CM-GCL: 70/10/20 split, ten runs, fine-tuned GNN, Macro-F1/AUC.
- Khan-GCL: 10 downstream runs and test ROC-AUC at best validation epoch for transfer setting.

## 6. Still UNCLEAR

- Exact seed lists for almost all papers.
- `test@best validation epoch` agreement for most GCL/SSL papers.
- Early stopping for most papers.
- Graph Barlow Twins full node protocol.
- HLCL exact split/evaluator/seeds and final OpenReview status.
- G-Censor IID split/seeds/early stopping/final status.
- LangGSL leakage-safe split/evaluator/seeds.
- SPGCL evaluator/seeds/early stopping.

## 7. Gap Novelty Boundaries

- G1: must separate from GCA/AFGRL/CM-GCL/G-Censor; simple positive heuristics are blocked.
- G2: must separate from ProGCL/HLCL/SPGCL; generic hard-negative reweighting is blocked.
- G3: must compare MGM and GCL under identical frozen evaluator; simple masked reconstruction is blocked.
- G4: must add graph-specific collapse diagnostics beyond BGRL/CCA-SSG/GBT/AFGRL.
- G5: must explain heterophily boundary conditions beyond HLCL filters.
- G6: must provide leakage-safe LLM/TAG protocol; naive pseudo-label use is blocked.
- G7: can be a reporting/diagnostic companion, not necessarily a standalone method.
- G8: should be deferred unless cross-domain is explicitly selected.

## 8. Gaps to Prioritize for Stage 2

Priority: G1, G2, G3 and G5.

Companion diagnostics: G4 and G7.

Defer or treat cautiously: G6 and G8.

## 9. Stage 2 Recommendation

Recommend entering Stage 2 idea-discovery: YES, with constraints.

Stage 2 must use the closest-work delta boundaries and cannot generate simple gate/reweighting/adapter/residual/temperature-only ideas. It should not claim direct comparability to published results unless exact split/evaluator/seeds/test@best are matched or baselines are rerun.

## Verdict

GO
