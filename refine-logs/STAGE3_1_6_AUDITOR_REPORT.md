# Stage 3.1.6 Auditor Report

Date: 2026-06-26
Auditor: fresh `gcl_experiment_auditor`
Mode: subagent read-only review

## Verdict

WARN

## Blocking Issues

- Cora 未生成实际 split 文件，阻塞任何包含 Cora 的 Stage 3.2 pilot/GPU run。
- 直接 Stage 3.2 pilot run 仍未获授权。

## Non-Blocking Issues

- 下载范围合规：代码白名单仅 Cora / Wiki-CS / Actor，且通过 PyG official loader。
- 未发现训练、evaluator、GPU、baseline clone、accuracy/loss/performance table。
- Metadata 未包含 test label distribution；代码禁止相关字段。
- Wiki-CS/Actor split JSON schema 与完整性校验通过；`class_distribution_test=null`。
- Official split 与 custom split 存在未来混用风险，但当前未生成性能表，不构成泄漏。

## Required Fixes

- GPU/pilot 前必须解决 Cora：重新通过 PyG Planetoid 或显式批准的本地 cache 生成并校验 `custom_stratified_random_1_1_8` split，或正式缩小 Stage 3.2 范围并记录不跑 Cora。
- Stage 3.2 执行前必须新增独立批准、run manifest、固定 split policy，禁止把 Cora custom、Wiki-CS official、Actor fixed 放入同一直接可比主表。
- GPU 部署前固定当前代码/artifact provenance，避免 dirty worktree 下的 split provenance 不可复现。

## Whether Stage 3.2 Planning Is Allowed

Yes.

## Whether Stage 3.2 Pilot Run Is Allowed

No.
