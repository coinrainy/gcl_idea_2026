# Closest-Work Delta Table

This table defines novelty boundaries only. It does not propose final methods.

| Gap ID | Closest works | What they already solve | What they do not solve | Blocked claim | Still-open claim | Minimum novelty condition for Stage 2 | Must-run falsification experiment | Risk after reading |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G1 semantic false positives | GCA, AFGRL, CM-GCL, G-Censor | adaptive augmentations; augmentation-free positives; multimodal positives; task-oriented counterfactual views | systematic positive semantic-validity audit under frozen node evaluator | "better positives via simple feature/structure heuristic" | positive validity may fail differently across graph regimes | show a measurable semantic-positive failure not covered by adaptive augmentation or AFGRL/G-Censor | correlate positive consistency diagnostics with downstream accuracy under fixed split/evaluator | HIGH |
| G2 false negatives under homophily/heterophily | ProGCL, HLCL, SPGCL, homophily-aware heterogeneous GCL | false-negative-aware hard mining; graph-filter heterophily views; positive sampling | unified regime-conditioned false negative/positive boundary | "hard negative reweighting solves GCL negatives" | negative validity may depend on homophily/feature/text regime | separate from ProGCL by predicting when negative mining is harmful/helpful | validation-only false-negative estimates vs label agreement by homophily bin | HIGH |
| G3 MGM vs GCL identical evaluator | GraphMAE, GraphMAE2, MaskGAE | strong masked feature/edge/latent prediction | strict apples-to-apples GCL vs MGM under same split/evaluator/backbone | "masked reconstruction alone is a new GCL contribution" | objective choice may explain protocol-normalized differences | isolate objective difference with frozen evaluator and identical backbone | rerun GRACE/GCA/BGRL/GraphMAE variants on same split/seed/evaluator | MEDIUM-HIGH |
| G4 negative-free collapse diagnostics | BGRL, CCA-SSG, Graph Barlow Twins, AFGRL | remove negatives; decorrelate features; discover positives | graph-specific collapse/oversmoothing diagnostics beyond accuracy | "negative-free GCL is novel" | collapse may manifest as graph smoothing/rank loss by regime | define graph representation diagnostics that predict failures | compare rank/variance/eigenspectrum vs accuracy across regimes | MEDIUM |
| G5 heterophily boundary conditions | HLCL, directed GCL, supervised heterophily GNNs | filters/augmentation for heterophily and directed structure | boundaries of heterophily types and failure modes | "add high-pass/low-pass filter for heterophily" | different heterophily types may require different SSL assumptions | taxonomy + evidence of failure not explained by HLCL filters | evaluate same SSL objectives across Actor/Chameleon/Squirrel/Penn94/Twitch/Genius with fixed splits | HIGH |
| G6 leakage-safe LLM semantic priors | LangGSL, CM-GCL, TAG/LLM graph learning | use text/LLM features and node-text contrast | leakage-safe, split-consistent GCL evaluation | "LLM pseudo-labels improve GCL" | text semantics may help detect false positives/negatives if audited | explicit leakage model and ablation against frozen text embeddings | compare graph-only, text-embedding, LLM pseudo-label under no-test-label/no-contamination rules | HIGH |
| G7 worst-group robustness | HLCL, robust GNNs, GroupDRO-style reporting | improves some heterophily/noise settings | worst-group reporting for GCL claims | "mean accuracy proves robustness" | robust GCL may fail on minority graph regimes | define groups without test leakage and report worst-bin effects | bin by homophily/noise/degree/label scarcity and report worst-bin accuracy | MEDIUM |
| G8 cross-domain generalization | BGRL large-scale, GCC/G5, IRM | graph pretraining/transfer at scale | protocol-aligned domain generalization for node classification | "works across datasets" from same-domain tables | graph SSL invariances may transfer only under certain domain shifts | specify source/target graph domains and invariant assumptions | pretrain on one graph family, freeze/evaluate on another with controlled evaluator | HIGH |

## Stage 2 Priority

Prioritize G1, G2, G3 and G5. Treat G6 as promising but leakage-risky. Keep G7 as reporting/diagnostic companion. Defer G8 unless Stage 2 explicitly targets cross-domain settings.

## Stage 1.6 DeepXiv Delta Check

DeepXiv search and section reads did not kill any Stage 1.5 gap, but they raised the bar for novelty:

- G1: simple positive/augmentation changes are more strongly blocked by GMA/GMCL, GPA, iGCL, AFGRL and G-Censor-like task-oriented views.
- G2: generic negative reweighting is more strongly blocked by ProGCL, SPGCL, negative metric learning and counterfactual hard negatives.
- G3: MGM remains a valid comparison gap only if GRACE/GCA/BGRL/GraphMAE/GraphMAE2/MaskGAE are rerun under identical project protocol.
- G5: heterophily claims must separate from HLCL, GCL-OT, GraphACL/DSSL/HGRL-style baselines and SPGCL heterophily tables.
- G6: LLM semantic-prior work must begin with a leakage model, not with a performance claim.

No final Stage 2 method is proposed here.
