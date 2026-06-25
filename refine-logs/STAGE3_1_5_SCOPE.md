# Stage 3.1.5 Scope

Date: 2026-06-26
Stage: Stage 3.1.5 Real Loader and Split Generation Smoke

## Scope Boundary

1. 本轮只做 real loader / split generation / non-training smoke。
2. 不自动下载数据集。
3. 不训练模型。
4. 不运行 evaluator。
5. 不运行 pilot。
6. 不使用 GPU。
7. 不克隆 baseline。
8. 不生成 accuracy。
9. 不做 objective-family ranking。
10. 不进入 Stage 3.2。
11. Stage 3.2 必须在本轮完成后经过 GPT/人工独立审查和 auditor approval 才能考虑。

## Explicit Non-Actions

本轮不调用 `/research-pipeline`、`/experiment-bridge`、`/run-experiment`、`/experiment-queue`，不训练 GRACE / BGRL / GraphMAE，不运行 GCL encoder，不运行 frozen evaluator，不下载数据，不安装依赖，不写论文，不修改 `BENCHMARK_PROTOCOL.md`，不修改 Stage 2B active idea。
