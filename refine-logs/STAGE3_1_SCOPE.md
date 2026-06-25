# Stage 3.1 Scope

Date: 2026-06-26
Stage: Stage 3.1 Minimal Scaffold Implementation and Synthetic Smoke

## Scope Boundary

1. 本轮只实现最小工程脚手架。
2. 本轮只允许 synthetic smoke。
3. 本轮不下载真实数据集。
4. 本轮不训练 GRACE / BGRL / GraphMAE。
5. 本轮不运行 pilot。
6. 本轮不生成 performance claim。
7. 本轮不进入 Stage 3.2。
8. Stage 3.2 必须经过 GPT/人工独立审查后另行批准。

## Explicit Non-Actions

本轮不调用 `/research-pipeline`、`/experiment-bridge`、`/run-experiment`、`/experiment-queue`，不运行 GPU 实验，不运行真实 pilot，不下载真实数据集，不克隆 baseline 仓库，不跑 Cora / Wiki-CS / Actor 真实训练，不实现 ProGCL，不写论文，不修改 `BENCHMARK_PROTOCOL.md`，不修改 Stage 2B active idea。
