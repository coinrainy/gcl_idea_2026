# Pilot Method Selection

Date: 2026-06-25
Stage: Stage 3.0

## Selection Principle

Stage 3.1 只准备最小 objective-family 对照。目标不是复现所有强 baseline，而是先验证三类 objective family 在统一 split、backbone、frozen evaluator、logging 和 metric interface 下能否公平比较。

## Selected Minimal Method Set

| method | objective family | why selected | official code availability | expected implementation source | evaluator compatibility | known protocol mismatch | engineering difficulty | pilot risk | fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GRACE | negative_based_contrastive | 经典 negative-based node-level GCL，机制简单，适合统一实现 | official / community implementations exist | Stage 3.1 优先统一 minimal implementation 或从可信实现抽取 loss/view logic | 可接入 frozen encoder + linear evaluator | 原论文 split/seed/evaluator 细节与本项目 split JSON 不完全一致 | medium-low | 若 augmentation 细节不一致，可能影响 objective-family ranking | GCA |
| BGRL | bootstrap_negative_free | 代表 bootstrap / negative-free family，和 GRACE 形成清楚 objective contrast | official / community implementations exist | Stage 3.1 优先统一 minimal implementation；teacher EMA 需独立模块 | 可接入 frozen encoder + linear evaluator | 官方可能使用不同数据集 split、encoder budget 和 evaluator | medium | EMA/batchnorm/augmentation 设置可能引入额外变量 | AFGRL |
| GraphMAE | masked_graph_modeling | 代表 masked feature reconstruction，覆盖 active idea 的 MGM 分支 | official code exists | Stage 3.1 优先 wrapper 或 minimal masked-feature objective；需统一 encoder 输出接口 | 必须改接统一 frozen linear evaluator | GraphMAE 官方 evaluator、pretrain budget、decoder 设置与 GCL 方法可能不同 | medium-high | decoder/hidden dim/budget 若不统一会破坏公平性 | GraphMAE2 |

## Audit/Fallback Methods

| method | objective family | role | constraints |
| --- | --- | --- | --- |
| GCA | negative_based_contrastive_adaptive | GRACE fallback or later adaptive augmentation comparison | Stage 3.1 不默认纳入，除非 GRACE implementation blocked |
| AFGRL | augmentation_free_negative_free | BGRL fallback | Stage 3.1 不默认纳入 |
| GraphMAE2 | masked_graph_modeling | GraphMAE stronger fallback | Stage 3.1 不默认纳入，避免 decoder complexity |
| ProGCL | negative_validity_audit_reference | `GCL-I02` audit reference only | 不作为核心方法，不进入 selector，不在 Stage 3.1 默认实现 |

## Framework Choice

Stage 3.1 应优先采用统一 minimal implementation，而不是直接拼接多个官方仓库。理由：

- GRACE/BGRL/GraphMAE 官方实现可能横跨 PyG/DGL、不同 evaluator、不同 config 习惯；
- active idea 的核心是 protocol alignment，wrapper 多仓库会增加 hidden mismatch；
- 统一实现可以共享 dataset loader、split reader、encoder、frozen evaluator、logging schema 和 metric extraction interface。

若 Stage 3.1 发现 GraphMAE 统一实现成本过高，可先使用 wrapper，但 wrapper 必须强制输出同一 embedding 格式，并禁用官方 evaluator，改用本项目 frozen linear evaluator。

## Stage 3.1 Priority

1. 统一 data/split/evaluator/logging scaffold。
2. GRACE minimal objective。
3. BGRL minimal objective。
4. GraphMAE minimal masked-feature objective or wrapper with unified evaluator.
5. ProGCL 不进入 Stage 3.1，除非 auditor 要求 I02 audit scaffold。

No code is implemented in Stage 3.0.
