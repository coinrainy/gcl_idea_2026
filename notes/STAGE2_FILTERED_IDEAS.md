# Stage 2A Filtered Ideas

Date: 2026-06-25

Mechanical filter only. This does not claim final novelty.

## Hard Filter Rules Applied

Eliminate or deprioritize ideas that are only gate/reweighting/adapter/residual/temperature/backbone/augmentation-rate changes; mechanical vision SSL transplants; Cora-only; no closest-work delta; no falsification experiment; no negative-result value; test-set tuning; or LLM pseudo-label ideas without leakage audit.

## Filter Outcome

| Idea | Mechanical status | Reason |
| --- | --- | --- |
| GCL-I01 | KEEP for novelty check | Clear G1 delta and falsification; risk is high but not mechanically invalid. |
| GCL-I02 | KEEP for novelty check | Clear G2 delta; not just reweighting because it proposes relation taxonomy and validation-only audit. |
| GCL-I03 | KEEP for novelty check | Strong G3 protocol gap; benchmark-mechanism hybrid; no prohibited trick. |
| GCL-I04 | KEEP for novelty check | Clear G5 mechanism; high implementation risk but falsifiable. |
| GCL-I05 | KEEP for novelty check | Hybrid G1/G3 route; failure views become masked evidence, not only gating. |
| GCL-I06 | KEEP as companion, not top novelty check | Useful G7 diagnostic/reporting companion; may be too reporting-heavy as a main paper. |
| GCL-I07 | REVISE / lower priority | Prototype route is plausible but crowded; needs stronger check against prototypical GCL and clustering papers. |
| GCL-I08 | DEFER | Has leakage audit, so not killed mechanically, but G6 is not a main Stage 2A recommendation unless reviewer upgrades it. |
| GCL-I09 | KEEP as companion, not top novelty check | Strong G4 diagnostic, likely best as support for I03/I04 rather than a main method. |
| GCL-I10 | DEFER | Scope expands toward G8/cross-domain; not main Stage 2A route unless reviewer explicitly recommends. |

## Top Ideas Entering Targeted Novelty Check

1. GCL-I03: Protocol-aligned MGM-vs-GCL regime selector.
2. GCL-I02: Regime-conditioned negative validity boundary.
3. GCL-I01: Semantic-preserving positive validity tests.
4. GCL-I04: Heterophily-type signed relation contrast.
5. GCL-I05: Bad positive views as masked counter-evidence.

## Mechanically Killed Ideas

None. No candidate is purely a gate/reweighting/adapter/residual/temperature/backbone-swap trick, and all include a falsification experiment. GCL-I08 and GCL-I10 are deferred because they target de-prioritized G6/G8 axes.
