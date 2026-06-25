# Stage 3.0 Scope

Date: 2026-06-25
Stage: Stage 3.0 Pilot Readiness / engineering feasibility review

## Scope Boundary

1. 本轮只做 pilot readiness，不运行实验。
2. Stage 3.1 才允许做最小代码实现 / smoke test。
3. Stage 3.2 才允许真正 pilot run。
4. formal 实验必须在 pilot GO 之后另行审批。
5. 所有未来 pilot 结果都必须标记为 `pilot`，不进入论文主表。
6. test labels 不能用于 selector、调参、survival decision。

## Explicit Non-Actions

本轮不调用 `/research-pipeline`、`/experiment-bridge`、`/run-experiment`、`/experiment-queue`，不运行 GPU 实验，不运行 pilot，不运行 smoke test，不克隆 baseline 仓库，不实现训练代码，不下载数据集，不修改 `BENCHMARK_PROTOCOL.md`，不修改 Stage 2B active idea，不进入 Stage 3.1，不进入 paper writing。

## Allowed Outputs

本轮只允许创建 pilot 前置工程设计、schema、manifest draft、方法/数据集选择、readiness report 和 auditor 审查记录。
