# DeepXiv Stage 1 Completion Report

Date: 2026-06-25

## Scope

本报告只记录 Stage 1.6 的 DeepXiv 数据源补全结果。没有进入 Stage 2，没有生成研究 idea，没有克隆 baseline 仓库，没有运行实验，也没有修改 `BENCHMARK_PROTOCOL.md`。

## DeepXiv Status

- CLI: available at `/root/miniconda3/bin/deepxiv`.
- SDK: `deepxiv-sdk==0.3.1`.
- Adapter: `/root/aris_repo/tools/deepxiv_fetch.py`.
- Health check: passed.
- Search smoke test: passed.
- Paper access smoke test: `2006.04131` brief/head/Experiments passed.

Raw evidence is saved under `notes/stage1_6_deepxiv/`.

## Commands Verified

- `which deepxiv`
- `deepxiv --help`
- `deepxiv health`
- `python /root/aris_repo/tools/deepxiv_fetch.py health --json`
- `python /root/aris_repo/tools/deepxiv_fetch.py search "graph contrastive learning node classification" --max 5`
- `python /root/aris_repo/tools/deepxiv_fetch.py paper-brief 2006.04131`
- `python /root/aris_repo/tools/deepxiv_fetch.py paper-head 2006.04131`
- `python /root/aris_repo/tools/deepxiv_fetch.py paper-section 2006.04131 "Experiments"`

## Targeted Completion

DeepXiv was used for:

- 10 targeted GCL/node-classification queries.
- 12 high-risk/closest-work arXiv papers.
- brief/head/Experiments section for all target arXiv papers where available.
- Ablation/Limitations/Experimental Setup/Evaluation/Implementation Details/Appendix sections when DeepXiv could match section names.

## Important Findings

- DeepXiv confirms several protocol details that were previously only partially recovered, especially public split vs 10/10/80 usage, frozen linear/logistic evaluation, and repeated-run reporting for GRACE/GCA/CCA-SSG/AFGRL/MaskGAE/SPGCL.
- DeepXiv confirms SPGCL is a high-risk recent positive-sample paper: it reports homophily and heterophily node classification, frozen linear evaluation, ten repeats, and ablations for energy-aware propagation / energy-guided positive sampling.
- DeepXiv confirms LangGSL is high risk for LLM/TAG semantic-prior directions, but it is not a standard frozen GCL evaluator paper and has leakage/protocol risks.
- DeepXiv did not provide enough evidence to mark any published result directly comparable with the project formal protocol.

## Remaining Limits

- DeepXiv is arXiv-centric; OpenReview-only G-Censor remains `UNCLEAR`.
- Section names are paper-dependent; many Ablation/Limitations requests correctly returned section-not-found errors.
- Exact saved split files, seed lists, early stopping, and `test@best validation epoch` are still missing for several papers.
- DeepXiv retrieval is not a final novelty check and does not replace Stage 2 reviewer/auditor work.

## Verdict

Stage 1.6 data-source completion: PASS.

Stage 2 can start after the user explicitly requests it, but Stage 2 must treat all DeepXiv additions as risk boundaries, not as final method directions.
