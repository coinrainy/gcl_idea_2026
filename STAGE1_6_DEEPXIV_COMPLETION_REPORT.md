# Stage 1.6 DeepXiv Completion Report

Date: 2026-06-25

## Scope

This stage completed DeepXiv-enhanced literature and protocol recovery. It did not enter Stage 2, did not generate a research idea, did not clone baseline repositories, did not run experiments, and did not modify `BENCHMARK_PROTOCOL.md`.

## DeepXiv Final Status

- CLI available: yes, `/root/miniconda3/bin/deepxiv`.
- Adapter available: yes, `/root/aris_repo/tools/deepxiv_fetch.py`.
- Health check: passed.
- Search: passed.
- Paper brief/head/section reads: passed for arXiv target papers when matching sections exist.
- Raw evidence: `notes/stage1_6_deepxiv/`.

## New Or Updated Files

- `notes/DEEPXIV_STAGE1_COMPLETION_REPORT.md`
- `notes/DEEPXIV_TARGETED_SEARCH.md`
- `notes/stage1_6_deepxiv/`
- `notes/CORE_CLOSEST_WORK_READING.md`
- `notes/CORE_PAPER_PROTOCOL_AUDIT.md`
- `notes/CLOSEST_WORK_DELTA_TABLE.md`
- `research-wiki/query_pack.md`
- `research-wiki/gap_map.md`
- `research-wiki/log.md`
- `research-wiki/papers/STAGE1_PAPER_AUDIT.md`
- `AGENTS.md`
- `STAGE1_6_DEEPXIV_COMPLETION_REPORT.md`

## Protocol Verdict

`BENCHMARK_PROTOCOL.md` remains valid and unchanged.

No published result found through DeepXiv is directly comparable under the project protocol because exact saved split JSON, identical seed list, and confirmed `test@best validation epoch` are still missing.

## Auditor-Style Verdict

Verdict: PASS for Stage 1.6 completion.

Blocking issue: none for completing Stage 1.6.

Risk warning: SPGCL, LangGSL, HLCL, G-Censor, GraphMAE/GraphMAE2/MaskGAE, AFGRL/CCA-SSG/Graph Barlow Twins remain strong closest-work constraints for Stage 2. They must be treated as novelty boundaries, not as direct baselines until rerun under the project protocol.

## Remaining UNCLEAR Fields

- G-Censor: OpenReview-only status/protocol/code remain `UNCLEAR`.
- HLCL: acceptance status, exact split/evaluator/seed protocol remain `UNCLEAR`.
- LangGSL: leakage protocol, exact split/evaluator/seed settings remain `UNCLEAR`.
- SPGCL: exact saved splits, seed identities, and test@best rule remain `UNCLEAR`.
- Graph Barlow Twins: exact evaluator/split/seed details remain insufficient for direct comparability.
- Several older papers still lack exact seed identities and saved split files.

## Stage 2 Recommendation

Stage 2 can proceed only after an explicit user request.

Recommended Stage 2 priorities remain:

- G1 semantic false positives.
- G2 false negatives under homophily/heterophily.
- G3 MGM vs GCL under identical evaluator.
- G5 heterophily boundary conditions.

Use G4/G7 as diagnostics and treat G6 as leakage-risky.

## Final Decision

Stage 1.6 decision: GO for future Stage 2 literature-to-gap ideation, but this report does not start Stage 2.
