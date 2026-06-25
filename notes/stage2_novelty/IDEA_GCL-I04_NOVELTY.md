# Novelty Check: GCL-I04

## Proposed Idea

Heterophily-type signed relation contrast: replace binary positive/negative relations with relation types such as homophilic-same, role-equivalent and heterophilic-complement, then train with alignment/prototype/context-prediction targets.

## Core Claims

1. Heterophily has multiple SSL-relevant types that high-/low-pass filters do not fully capture.
2. Some heterophilic relations should be predicted as context rather than directly aligned.
3. Signed relation taxonomy can explain when HLCL/SPGCL-style methods fail.

## Query Formulations Used

Full matrix: `notes/stage2_novelty/query_matrix.tsv`. Raw DeepXiv outputs: `notes/stage2_novelty/deepxiv_search/`.

## Sources Checked

- arXiv/WebSearch: HLCL, DSSL, HGRL, GraphACL, GCL-OT, homophily-aware heterogeneous GCL, HeroCL, relation-aware heterophily learning.
- DeepXiv: 9 targeted `GCL-I04` queries.
- OpenReview/WebSearch: HLCL OpenReview pages and local OpenReview search records.
- Local wiki/PDF: HLCL, SPGCL, homophily-aware heterogeneous GCL, directed GCL references.
- Semantic Scholar: API returned HTTP 429.
- Exa: unavailable because `EXA_API_KEY` is empty.

## Closest Prior Works

| Paper | Overlap | True delta |
| --- | --- | --- |
| HLCL | High-/low-pass filter views for GCL under heterophily | I04 must show heterophily subtypes not explained by graph filters. |
| DSSL / HGRL / GraphACL | Heterophily-aware graph SSL/representation learning | Need deep read before method claim. |
| GCL-OT | Multi-granular heterophily for text-attributed graphs | Strong recent risk for heterophily taxonomy, especially TAG. |
| Homophily-aware heterogeneous GCL / HeroCL | Heterophily-aware contrastive learning beyond simple graphs | I04 should stay node-classification simple/homogeneous unless expanded deliberately. |
| SPGCL | Positive sampling across homophily/heterophily | I04 must define signed relations beyond energy-guided positives. |

## Overlap

High with heterophily-aware SSL. The signed multi-relation framing may be novel if it avoids simple filtering and provides subtype-specific falsification.

## True Delta

The delta is a relation ontology for heterophily, not high-/low-pass filtering. The paper must show at least one subtype where filter-based methods fail for predictable reasons.

## Novelty Score

6.5/10.

## Risk of Being Considered Incremental

High due to HLCL, GCL-OT and heterophily-aware SSL papers.

## Recommendation

KEEP AS HIGH-RISK BACKUP.

## What Framing Would Be Honest

"A heterophily subtype taxonomy with relation-specific contrastive targets."

## What Framing Is Prohibited

- "High-pass/low-pass plus contrastive loss."
- "Heterophily-aware GCL" without subtype evidence.
- Mixing TAG/text heterophily claims without leakage controls.

## Minimum Additional Novelty Check

Deep-read GCL-OT, DSSL, HGRL and GraphACL before Stage 2B if this becomes a top candidate.
