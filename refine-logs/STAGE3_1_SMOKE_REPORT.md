# Stage 3.1 Synthetic Smoke Report

Date: 2026-06-26

## Commands Run

- `python scripts/run_stage3_1_synthetic_smoke.py`
- `python -m pytest tests/smoke -q` attempted after synthetic smoke; skipped as unavailable because pytest is not installed.

## Passed Checks

- validate synthetic split fixture
- validate synthetic label-free metric artifact
- selector loader rejects label-audit artifact
- run frozen evaluator on synthetic embeddings
- write and validate synthetic raw results
- method placeholders block real training

## Failed Checks

- none

## Dependencies Used

- Python standard library
- pytest available: False
- numpy/torch/sklearn: not required by smoke runner

## Boundary Flags

- real dataset accessed: no
- training run: no
- GPU used: no
- baseline repo cloned: no
- real pilot run: no
- performance claim generated: no

## Detailed Check Log

### validate synthetic split fixture

PASSED
### validate synthetic label-free metric artifact

PASSED
### selector loader rejects label-audit artifact

PASSED
### run frozen evaluator on synthetic embeddings

PASSED
### write and validate synthetic raw results

PASSED
### method placeholders block real training

PASSED
