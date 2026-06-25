# GCL-I08: Leakage-Safe Text Semantic Auditor

- Stage: Stage 2A
- Status: REVISE / DEFER
- Primary gap: G6
- Closest works: LangGSL, CM-GCL, TAPE/TAG LLM methods
- Reviewer verdict: REVISE

## Summary

Use frozen text embeddings only as pair-validity auditors, not pseudo-label teachers.

## Why Deferred

Leakage audit could become the whole paper, and G6 is not a main Stage 2A priority. Useful only if the project explicitly pivots to TAG/LLM protocol work.

## Falsification

Compare graph-only, frozen text auditor and pseudo-label teacher under the same split/evaluator. If only pseudo-labels help, safe auditor is insufficient.
