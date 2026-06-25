# Benchmark Protocol

## 1. Status

当前状态：`Draft`

进入正式实验前必须改为：

```text
Frozen
```

协议冻结后，不得因为结果不理想而修改：

* 数据划分；
* seed 列表；
* evaluator；
* early stopping；
* baseline 选择；
* 超参数搜索空间；
* 结果汇总方式。

任何协议变更必须写入 `DECISION_LOG.md`。

---

## 2. Task

本项目研究：

```text
图对比学习用于节点分类
```

默认设置：

* 任务：节点分类；
* 主要评价指标：Accuracy；
* 主要报告方式：`test@best validation epoch`；
* 正式结果：10 seeds mean±std；
* 主表只允许使用 `formal` 实验结果。

---

## 3. Experiment Labels

所有实验必须标记为以下一种：

| Label         | 含义              | 可否进主表 |
| ------------- | --------------- | ----- |
| `smoke`       | 检查代码能否运行        | 否     |
| `pilot`       | 快速判断 idea 是否有信号 | 否     |
| `development` | 开发、调参、debug     | 否     |
| `formal`      | 协议冻结后的正式实验      | 是     |

禁止把 `smoke`、`pilot`、`development` 结果用于 SOTA 或主 claim。

---

## 4. Data Split Policy

### 4.1 Default Split

主实验默认采用：

```text
train : validation : test = 1 : 1 : 8
```

即：

```text
10% / 10% / 80%
```

默认使用：

```text
stratified random split
```

即尽量保持各类别比例一致。

### 4.2 Split Consistency

所有方法必须使用完全相同的 split 文件，包括：

* 本方法；
* baseline；
* ablation；
* diagnostic variants。

禁止每个方法单独随机划分。

### 4.3 Split Seeds

正式实验默认 seed：

```text
0,1,2,3,4,5,6,7,8,9
```

必须区分：

| Seed         | 含义                       |
| ------------ | ------------------------ |
| `split_seed` | 控制数据划分                   |
| `model_seed` | 控制模型初始化、dropout、增强和训练随机性 |

推荐：

```text
split_seed = model_seed = seed
```

但结果文件中必须分别记录。

### 4.4 Split Files

所有 split 必须保存，不能运行时临时生成后丢弃。

推荐路径：

```text
splits/{dataset}/split_seed_{seed}.pt
splits/{dataset}/split_seed_{seed}.json
```

每个 split 至少记录：

```text
dataset_name
split_type
split_seed
train_mask
val_mask
test_mask
num_train
num_val
num_test
class_distribution
```

---

## 5. Public Split Exceptions

部分数据集不默认使用 1:1:8。

### 5.1 Planetoid Public Split

Cora、CiteSeer、PubMed 如果使用 Planetoid public split，必须单独标注。

规则：

* Planetoid public split 不能和 1:1:8 random split 直接比较；
* 若主实验采用 1:1:8，所有方法必须在 1:1:8 下重跑；
* public split 结果只能作为辅助复现或历史参考。

### 5.2 Wiki-CS

Wiki-CS 优先使用官方 public splits。

如果额外构造 1:1:8，必须标注为：

```text
custom random 1:1:8 split
```

不能与官方 split 结果混合比较。

### 5.3 OGB Datasets

OGB 数据集优先使用：

```text
official split + official evaluator
```

不默认改成 1:1:8。

### 5.4 Heterophily Benchmarks

异配图数据集若已有公认 fixed splits，优先使用 fixed splits。

规则：

* fixed split 和 random split 不混合比较；
* 若自定义划分，必须标注为 custom split；
* 与已有论文结果比较时，必须确认 split 协议一致。

---

## 6. Evaluation Protocol

### 6.1 Main Metric

默认主指标：

```text
Accuracy
```

如类别不平衡明显，可补充：

```text
Macro-F1
Balanced Accuracy
```

### 6.2 test@best

主表默认报告：

```text
test@best validation epoch
```

含义：

```text
选择验证集表现最好的 epoch，
报告该 epoch 对应的测试集结果。
```

禁止报告：

```text
所有 epoch 中最高 test accuracy
```

除非明确标注为 oracle analysis，且不能进入主表。

### 6.3 Early Stopping

必须记录：

```text
early_stopping_metric
patience
max_epochs
best_epoch
valid_at_best
test_at_best
final_test
```

---

## 7. GCL Evaluation

所有 GCL 方法必须使用相同下游 evaluator。

默认推荐：

```text
frozen encoder + linear evaluator
```

必须记录：

```text
encoder
hidden_dim
projection_dim
augmentation
contrastive_loss
temperature
negative_or_positive_sampling
pretrain_epochs
evaluator_type
evaluator_seed
```

如果使用 fine-tuning，必须单独建表，不能和 frozen evaluation 混合比较。

---

## 8. Baseline Protocol

正式实验前必须复现关键 baseline。

每个 baseline 记录：

```text
paper_result
code_source
commit_hash
dataset
split
metric
our_result
gap_from_paper
possible_reason_for_gap
```

公平性要求：

* 相同 split；
* 相同 evaluator；
* 相同 seed 列表；
* 相同或可比较的训练预算；
* 相同特征输入；
* 相同 preprocessing；
* 明确的超参数搜索空间。

如果 baseline 复现明显低于原论文，不能直接用该弱结果声称本方法更优。

---

## 9. Formal Results

正式实验必须满足：

* 协议已冻结；
* split 文件已保存；
* seed 列表已固定；
* evaluator 已锁定；
* baseline 已复现；
* 结果汇总脚本已实现；
* 不再根据 test set 调整方法。

正式结果报告：

```text
mean
std
per-seed results
valid_at_best
test_at_best
final_test
```

默认格式：

```text
mean ± std
```

---

## 10. Result Files

每次运行必须保存原始结果。

推荐路径：

```text
results/raw/{dataset}/{method}/{run_id}.json
```

每个结果文件至少包含：

```text
run_id
method
dataset
split_type
split_seed
model_seed
config_path
commit_hash
best_epoch
valid_at_best
test_at_best
final_test
status
log_path
```

汇总结果保存到：

```text
results/summary/
```

论文表格必须由脚本从原始 JSON/CSV 自动生成，不能手工复制最佳数字。

---

## 11. Ablation Requirements

每个核心模块都必须有消融。

最低要求：

```text
base method
full method
remove core component
replace core component with simple alternative
lambda=0 or equivalent degeneration
```

如果删除某模块后结果不变，则不能声称该模块是核心贡献。

---

## 12. SOTA Claim Rule

只有同时满足以下条件，才能使用：

```text
SOTA
state of the art
new best result
```

必要条件：

1. 同任务；
2. 同数据集；
3. 同 split；
4. 同 evaluator；
5. 相同或公平的调参预算；
6. formal 结果；
7. 多 seed 稳定；
8. 最新相关工作已检查；
9. 结果可追溯到原始文件；
10. `SOTA_LEDGER.md` 标注为 directly comparable。

否则只能使用：

```text
competitive
strong under our protocol
improves over reproduced baselines
preliminary
```

---

## 13. Prohibited Practices

禁止：

* test set 调参；
* 混用 public split 和 random split；
* 只报告最好 seed；
* 删除失败 seed；
* 不保存 split 文件；
* 不保存原始结果；
* 本方法和 baseline 使用不同 evaluator；
* 本方法拥有更大搜索空间但不披露；
* pilot 结果进入主表；
* development 结果支持 SOTA claim；
* 手工从日志中挑最好数字；
* 把不同协议下的结果直接比较。

---

## 14. Stage Gate

进入下一阶段的最低要求：

| Stage   | 通过条件                        |
| ------- | --------------------------- |
| Stage 0 | 协议文件、wiki、reviewer audit 完成 |
| Stage 1 | 文献地图和 gap matrix 完成         |
| Stage 2 | 选出 1 个主 idea 和 1 个备选 idea   |
| Stage 3 | Problem Anchor 和实验计划冻结      |
| Stage 4 | baseline 复现可信               |
| Stage 5 | pilot 支持机制假设                |
| Stage 6 | formal 结果支持主 claim          |

若任一阶段出现 `FAIL` 或 `BLOCKED`，不得进入下一阶段。
