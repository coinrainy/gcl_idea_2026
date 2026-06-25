# Stage 2B Claim Matrix

Date: 2026-06-25

## Claim Status Legend

- `planned`: can be tested in Stage 3 pilot.
- `unsupported`: no evidence yet.
- `blocked`: prohibited by current evidence or closest work.

## Matrix

| Claim ID | Claim | Status | Evidence needed | Allowed support level after Stage 3 pilot | Current risk |
| --- | --- | --- | --- | --- | --- |
| C1 | Published GCL/MGM comparisons are not directly comparable under this project protocol. | planned | protocol audit plus matched pilot reruns | pilot diagnostic only | medium |
| C2 | Label-free graph-regime metrics predict objective-family ranking under matched protocol. | planned | four-dataset pilot with matched split/backbone/evaluator/budget | pilot support only | medium-high |
| C3 | Label-audit metrics explain objective failures without entering training or selection. | planned | train/validation-only audit tables | pilot support only | high leakage risk |
| C4 | Negative-validity audit explains some contrastive failures. | planned | I02 audit on train/validation labeled pairs | auxiliary support only | high closest-work risk |
| C5 | The method is SOTA or robust across graph regimes. | blocked | formal 10-seed protocol, baselines and raw-result scripts | not allowed after pilot | very high |
| C6 | A new MGM+GCL hybrid objective is novel. | blocked | not pursued | not allowed | blocked by CORE/GCMAE/AUG-MAE |
| C7 | A new hard-negative reweighting method solves false negatives. | blocked | not pursued | not allowed | blocked by ProGCL/GRAPE/NML/BalanceGCL |

## Active Paper Story After Stage 2B

The only active story is:

Protocol alignment plus label-free regime diagnostics can reveal when graph SSL objective families should be used for node classification.

## Claims Explicitly Deferred

- formal accuracy improvements;
- SOTA;
- robustness;
- universal objective selection;
- cross-domain generalization;
- LLM or text-semantic gains.
