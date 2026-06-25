# Source Recovery Report

Stage 1.5 目标是有限补强 Stage 1 的数据源缺口，不做全领域重新扫库。

## Semantic Scholar

检查方式：使用 `/root/aris_repo/tools/semantic_scholar_fetch.py`，降低为每次 `--max 1`，仅查 high-risk closest work，并在两次查询间 sleep。

| Query | Result | Metadata recovered | Impact |
| --- | --- | --- | --- |
| `GRACE Deep Graph Contrastive Representation Learning` | failed | HTTP 429 | 不继续刷接口 |
| `ProGCL Rethinking Hard Negative Mining in Graph Contrastive Learning` | failed | HTTP 429 | 不继续刷接口 |
| `BGRL Large-Scale Representation Learning on Graphs via Bootstrapping` | success | title, authors, year=2021, venue=ICLR, ArXiv id `2102.06514`, citationCount=324, S2 URL, TLDR | 补充 BGRL venue/citation/S2 metadata |

Conclusion: Semantic Scholar remains partially unavailable due rate limiting. Only BGRL metadata was recovered. No broad S2 sweep was performed.

## DeepXiv

Commands:

```bash
which deepxiv || true
deepxiv --help || true
```

Original Stage 1.5 result: `deepxiv` CLI not found. ARIS wrapper exists at `/root/aris_repo/tools/deepxiv_fetch.py`, but it requires the missing CLI.

Fix after Stage 1.5: installed `deepxiv-sdk==0.3.1`, patched the ARIS adapter to avoid the deprecated `--mode` argument, and verified health/search/paper-brief.

Current status: available.

Compensation is no longer required for future DeepXiv-backed retrieval, although prior Stage 1/1.5 reports remain valid historical snapshots.

## Exa

Command:

```bash
echo ${EXA_API_KEY:-}
```

Result: empty. Exa unavailable; no API key was fabricated.

Compensation: use arXiv, OpenReview, official PDF pages, and WebSearch.

## OpenReview Recovery

| Paper | Status | Review visibility | PDF | Code | Reviewer concerns | Novelty impact |
| --- | --- | --- | --- | --- | --- | --- |
| CM-GCL | accepted, NeurIPS 2022 | OpenReview says 20 replies; helper did not extract review text | OpenReview + NeurIPS official PDF available | https://github.com/graphprojects/CM-GCL | review details not extracted | high risk for multimodal / imbalanced node-classification GCL |
| InfoGCL | accepted, NeurIPS 2021 Poster | review text not extracted | NeurIPS official PDF and arXiv available | UNCLEAR | review details not extracted | medium-high risk for information-aware GCL framing |
| HLCL | OpenReview submission and arXiv available; acceptance status UNCLEAR | OpenReview says replies exist, but no final decision recovered | OpenReview/arXiv PDF available | UNCLEAR | not extracted | high risk for heterophily-aware GCL |
| G-Censor | submitted to ICLR 2023; acceptance status UNCLEAR | OpenReview says replies exist, but no final decision recovered | OpenReview PDF available | promised in submission, not confirmed | not extracted | high risk for task-oriented counterfactual views |
| Transductive Linear Probing | accepted, LoG 2022 Oral | not extracted | OpenReview PDF available | UNCLEAR | not extracted | medium risk for few-shot node classification use of GCL embeddings |
| Directed Graph Contrastive Learning | accepted, NeurIPS 2021 Poster | not extracted | NeurIPS official PDF available | UNCLEAR | not extracted | medium risk if directed graphs enter scope |

## PDF Recovery

Newly downloaded/read PDFs include AFGRL, CCA-SSG, Graph Barlow Twins, GraphMAE2, MaskGAE, HLCL, LangGSL, Khan-GCL, SPGCL, InfoGCL, CM-GCL and G-Censor. Text was extracted with `pypdf` into `notes/stage1_5_pdf_text/`.

## Remaining Coverage Risk

S2 citation/DOI coverage remains incomplete. OpenReview review details remain under-extracted. DeepXiv is now available for future follow-up retrieval. This does not block Stage 2 gap ideation, but it does block SOTA claims and any direct comparability claim.
