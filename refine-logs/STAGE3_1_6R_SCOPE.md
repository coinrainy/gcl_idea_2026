# Stage 3.1.6R Scope

Date: 2026-06-26
Stage: Stage 3.1.6R Post-fix Auditor Reconciliation

## Scope Boundary

1. 本轮只做 post-fix auditor reconciliation。
2. 本轮只检查已有 metadata 和 split JSON。
3. 本轮不下载数据。
4. 本轮不训练模型。
5. 本轮不运行 evaluator。
6. 本轮不运行 pilot。
7. 本轮不使用 GPU。
8. 本轮不克隆 baseline。
9. 本轮不生成 accuracy / loss / performance table。
10. 本轮不进入 Stage 3.2。
11. 本轮目标是解决 Stage 3.1.6 report 与 auditor report 的不一致。
12. 即使 reconciliation 通过，也最多允许进入 Stage 3.2 planning / implementation approval，不允许直接 pilot run。

## Reconciliation Target

`refine-logs/STAGE3_1_6_REPORT.md` 已记录 Cora / Wiki-CS / Actor 均有 metadata 与 validated split JSON；但 `refine-logs/STAGE3_1_6_AUDITOR_REPORT.md` 仍保留修复前的历史判断，即 Cora 未生成实际 split 文件。本轮只核查 artifacts 当前状态，并让 fresh `gcl_experiment_auditor` 重新审查该不一致是否已经解决。
