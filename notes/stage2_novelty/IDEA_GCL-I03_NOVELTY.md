# Novelty Check: GCL-I03

## Proposed Idea

Protocol-aligned MGM-vs-GCL regime selector: compare contrastive, bootstrap and masked graph objectives under identical split/backbone/evaluator/budget, then test whether graph-regime metrics predict which objective wins.

## Core Claims

1. Objective ranking between GCL and MGM is confounded by protocol mismatch.
2. Feature-label predictability, edge homophily and reconstruction difficulty can predict whether MGM or GCL is preferable.
3. A protocol-aligned selector/failure analysis is a contribution beyond rerunning GraphMAE.

## Query Formulations Used

For each claim, the novelty check used technical-term, closest-work and mechanism queries. Full query matrix is in `notes/stage2_novelty/query_matrix.tsv`; DeepXiv raw search outputs are in `notes/stage2_novelty/deepxiv_search/`.

## Sources Checked

- arXiv/WebSearch: GraphMAE, GraphMAE2, MaskGAE, generative+contrastive graph SSL, GCMAE, CORE, alignment-uniformity masked GAE.
- DeepXiv: 9 targeted queries under `GCL-I03`.
- OpenReview/WebSearch: graph masked autoencoder and GSSL hits; no direct exact protocol-selector match found.
- Local research-wiki: `gap_map.md`, `query_pack.md`, `STAGE1_PAPER_AUDIT.md`.
- Downloaded PDFs/text: `notes/stage1_5_pdf_text/2205.10803.txt`, `2304.04779.txt`, `2205.10053.txt`, GRACE/GCA/BGRL texts.
- Semantic Scholar: API returned HTTP 429.
- Exa: unavailable because `EXA_API_KEY` is empty.

## Closest Prior Works

| Paper | Overlap | True delta |
| --- | --- | --- |
| GraphMAE / GraphMAE2 | masked feature/latent graph SSL; compares against contrastive baselines | Does not provide project-level same split/seed/evaluator audit across objectives as the main contribution. |
| MaskGAE | masked edge/path modeling and node classification | Narrower node protocol; not a general GCL-vs-MGM regime selector. |
| GCMAE / generative+contrastive graph SSL | combines generative and contrastive paradigms | More method-combination oriented; can threaten novelty if I03 becomes a hybrid objective instead of a diagnostic-selector paper. |
| Rethinking Graph Masked Autoencoders through Alignment and Uniformity | analyzes masked graph autoencoders through CL geometry | Strong risk for the alignment-uniformity part; I03 must add protocol-aligned node classification regime prediction. |
| CORE: Contrastive Masked Feature Reconstruction on Graphs | mixes contrastive and masked reconstruction | Blocks simple "combine MGM and GCL" framing. |

## Overlap

High overlap with the GraphMAE family on masked objectives and with GCMAE/CORE on combining generative and contrastive losses. Medium overlap with papers analyzing alignment/uniformity. Lower overlap with the specific claim that a protocol-controlled regime metric predicts objective winners.

## True Delta

The honest delta is not a new SSL loss. It is a protocol-aligned diagnostic/benchmark contribution: identify graph regimes where GCL vs MGM objective choice matters after evaluator/split/backbone are fixed.

## Novelty Score

7/10.

## Risk of Being Considered Incremental

Medium. It becomes incremental if framed as "GraphMAE plus contrastive" or "objective selector" without a rigorous protocol audit and falsification.

## Recommendation

KEEP.

## What Framing Would Be Honest

"A protocol-aligned study and lightweight regime diagnostic for deciding when masked graph modeling vs contrastive graph SSL is appropriate for node classification."

## What Framing Is Prohibited

- "New SOTA graph SSL objective."
- "Masked modeling is better than GCL" based on published tables.
- "Combining MGM and GCL is novel."

## Minimum Additional Novelty Check

Before Stage 2B, search specifically for 2024-2026 papers on automated graph SSL objective selection and graph SSL benchmark protocols.
