# Stage 2A Idea Report

Date: 2026-06-25

## 1. Inputs and Sources

Input files: `AGENTS.md`, `RESEARCH_BRIEF.md`, `BENCHMARK_PROTOCOL.md`, Stage 1/1.5/1.6 reports, `notes/GCL_*`, `notes/CORE_*`, `notes/CLOSEST_WORK_DELTA_TABLE.md`, `notes/DEEPXIV_*`, `research-wiki/gap_map.md`, `research-wiki/query_pack.md`, `research-wiki/log.md`, `research-wiki/papers/STAGE1_PAPER_AUDIT.md`.

Sources checked for novelty: local research-wiki, downloaded PDFs/text, DeepXiv, arXiv/WebSearch, OpenReview/WebSearch. Semantic Scholar returned HTTP 429. Exa was unavailable because `EXA_API_KEY` is empty.

No code was implemented. No experiment, pilot, GPU job, repo clone, experiment-bridge, or Stage 2B refine was run.

## 2. Raw Ideas

Generated 10 raw ideas:

- `GCL-I01`: Semantic-preserving positive validity tests.
- `GCL-I02`: Regime-conditioned negative validity boundary.
- `GCL-I03`: Protocol-aligned MGM-vs-GCL regime selector.
- `GCL-I04`: Heterophily-type signed relation contrast.
- `GCL-I05`: Bad positive views as masked counter-evidence.
- `GCL-I06`: Worst-regime relation repair.
- `GCL-I07`: Balanced semantic prototypes.
- `GCL-I08`: Leakage-safe text semantic auditor.
- `GCL-I09`: Three-way graph SSL collapse diagnostics.
- `GCL-I10`: Local environment invariance.

## 3. Filtering

No idea was mechanically killed in the first pass because all had closest-work deltas and falsification tests. After novelty check and reviewer audit:

- KILL: `GCL-I05`, `GCL-I07`, `GCL-I10`.
- REVISE / companion / defer: `GCL-I01`, `GCL-I04`, `GCL-I06`, `GCL-I08`, `GCL-I09`.
- KEEP: `GCL-I02`, `GCL-I03`.

## 4. Kept Ideas

Main candidates:

- `GCL-I03`
- `GCL-I02`

Backup:

- `GCL-I04`

## 5. Closest-Work Risk Summary

| Idea | Closest-work risk |
| --- | --- |
| GCL-I03 | GraphMAE, GraphMAE2, MaskGAE, CORE, GCMAE; must avoid "new hybrid objective" framing. |
| GCL-I02 | ProGCL, Negative Metric Learning for Graphs, counterfactual hard negatives, SPGCL, HLCL; must avoid "new reweighting" framing. |
| GCL-I04 | HLCL, GCL-OT, DSSL, HGRL, GraphACL, SPGCL; must prove a heterophily subtype diagnostic first. |
| GCL-I01 | GCA, AFGRL, G-Censor, SPGCL, CM-GCL; risks positive gate + auxiliary loss. |
| GCL-I05 | GCA/G-Censor + GraphMAE2/MaskGAE fusion risk. |

## 6. Novelty Check Results

- `GCL-I03`: score 7/10, KEEP. Honest framing is protocol-aligned objective boundary, not SOTA objective.
- `GCL-I02`: score 6.5/10, KEEP WITH REVISION. Must frame as regime boundary for harmful hard negatives.
- `GCL-I01`: score 6/10, REVISE. Needs stronger separation from G-Censor/SPGCL.
- `GCL-I04`: score 6.5/10, KEEP AS HIGH-RISK BACKUP / REVISE. Needs subtype diagnostic before method.
- `GCL-I05`: score 5.5/10, REVISE OR KILL; reviewer killed it as module fusion.

## 7. Reviewer Verdict

Fresh `gcl_scientific_reviewer` verdict:

- Main candidate 1: `GCL-I03`.
- Main candidate 2: `GCL-I02`.
- Backup: `GCL-I04`.
- Killed: `GCL-I05`, `GCL-I07`, `GCL-I10`.
- Revise/diagnostic: `GCL-I01`, `GCL-I06`, `GCL-I08`, `GCL-I09`.

## 8. Top 2 Main Candidates

## Idea GCL-I03: Protocol-Aligned MGM-vs-GCL Regime Selector

### Method in plain steps
1. Run contrastive, bootstrap and masked graph objectives under identical split, seed, backbone, evaluator and budget.
2. Compute graph-regime metrics such as feature-label predictability, edge homophily and reconstruction difficulty.
3. Test whether these metrics predict which objective works best.
4. Report objective-boundary failures instead of claiming a universal winner.

### Primary gap

G3: MGM vs GCL under identical evaluator.

### Core hypothesis

Objective choice is predictable from graph regime once protocol confounds are removed.

### Closest works

GraphMAE, GraphMAE2, MaskGAE, CORE, GCMAE, GRACE, GCA, BGRL.

### What is blocked by closest works

New masked objective, simple MGM+GCL hybrid, or published-table SOTA comparison.

### What remains open

Protocol-aligned objective boundary and diagnostic prediction under the same node classification evaluator.

### Novelty condition

Graph-regime metrics must predict objective winner beyond implementation noise.

### Falsification experiment

Same backbone/split/seed/evaluator/budget for GRACE/GCA/BGRL/GraphMAE-style variants; test whether proposed metrics predict objective ranking.

### Kill condition

Objective ranking is unrelated to the metrics or explained by implementation details.

### Expected evidence if true

Metrics predict most objective wins and reveal where published protocol differences mislead conclusions.

### Risk

MEDIUM. It is strongest as diagnostic/benchmark work, not pure method paper.

### Reviewer verdict

KEEP.

### Recommendation

KEEP as main candidate for Stage 2B refine.

## Idea GCL-I02: Regime-Conditioned Negative Validity Boundary

### Method in plain steps
1. Estimate local homophily proxy, feature similarity and structural role similarity for candidate negative pairs.
2. Partition pairs into confident negative, ambiguous relation and likely false negative.
3. Use confident negatives for contrastive training and audit ambiguous/false-negative pairs with validation labels only.
4. Compare against ProGCL-style hard-negative mining by graph regime.

### Primary gap

G2: false negatives under homophily/heterophily shift.

### Core hypothesis

Hard negatives are helpful or harmful depending on graph regime; this boundary can be predicted without training on test labels.

### Closest works

ProGCL, Negative Metric Learning for Graphs, counterfactual hard negatives, SPGCL, HLCL.

### What is blocked by closest works

Generic false-negative reweighting, hard-negative generation, or "we solve false negatives" claims.

### What remains open

When hard negatives become harmful across homophily, heterophily and role-similarity regimes.

### Novelty condition

Must explain ProGCL success/failure boundaries and not collapse into another scalar weight.

### Falsification experiment

Two homophilic and two heterophilic datasets; validation-label-only audit of predicted false-negative/ambiguous pairs against true label agreement.

### Kill condition

Predictions are random, or method behaves like ProGCL reweighting with no regime explanation.

### Expected evidence if true

Predicted harmful negatives correlate with label agreement and explain performance differences across graph regimes.

### Risk

HIGH. Closest-work pressure is severe.

### Reviewer verdict

KEEP.

### Recommendation

KEEP as main candidate for Stage 2B refine.

## 9. Backup Candidate

## Idea GCL-I04: Heterophily-Type Signed Relation Contrast

### Method in plain steps
1. Diagnose heterophily subtypes from ego-graph structure and feature patterns.
2. Treat homophilic-same, role-equivalent and heterophilic-complement relations differently.
3. Align, prototype-align or context-predict according to relation type.
4. First test whether subtype diagnostics explain failures of HLCL-style filters.

### Primary gap

G5: heterophily boundary conditions.

### Core hypothesis

Binary positive/negative GCL and high-/low-pass filters miss heterophily subtype differences.

### Closest works

HLCL, GCL-OT, DSSL, HGRL, GraphACL, SPGCL.

### What is blocked by closest works

Simple high-/low-pass filter additions and generic heterophily-aware GCL claims.

### What remains open

Subtype-specific relation semantics for node-level SSL.

### Novelty condition

Show at least one heterophily subtype where filter-based methods fail predictably.

### Falsification experiment

Subtype diagnostic on Actor/Chameleon/Squirrel/Penn94/Twitch/Genius before full method.

### Kill condition

Subtype estimates are unstable or redundant with HLCL/GCL-OT explanations.

### Expected evidence if true

Subtype diagnostics predict where HLCL/SPGCL fail and justify relation-specific training.

### Risk

HIGH.

### Reviewer verdict

REVISE.

### Recommendation

Backup only.

## 10. Not Recommended

- `GCL-I05`: KILL, module-fusion risk.
- `GCL-I07`: KILL, prototype/cluster GCL too crowded.
- `GCL-I10`: KILL, scope drifts to cross-domain/IRM.
- `GCL-I08`: defer to a separate TAG/LLM leakage-safe project.
- `GCL-I06` and `GCL-I09`: use only as companion diagnostics.
- `GCL-I01`: revise only if positive-validity score independently predicts failures.

## 11. Human Confirmation Needed

- Whether Stage 2B should refine `GCL-I03` first as a diagnostic/benchmark paper, or `GCL-I02` first as a higher-risk method paper.
- Whether backup `GCL-I04` should remain in scope or wait until heterophily-specific literature is deep-read.
- Compute budget for Stage 2B/Stage 3 planning, especially if protocol-aligned reruns are later required.

## 12. Stage 2B Recommendation

Yes, Stage 2B refine is recommended, but only for `GCL-I03` and/or `GCL-I02`, with `GCL-I04` as backup.

Do not enter experiments before Stage 2B refine.

## 13. Constraint Statement

This round did not implement code, did not run experiments, did not run pilots, did not clone baseline repositories, did not enter experiment-bridge, did not generate `refine-logs/FINAL_PROPOSAL.md`, and did not generate `refine-logs/EXPERIMENT_PLAN.md`.

## Stage 2A Verdict

GO
