# Research Brief

## Problem Statement

图对比学习在节点分类中的效果高度依赖图增强、正负样本定义、
结构与语义一致性假设以及下游评测协议。

本项目不以简单替换增强、增加权重或堆叠模块为目标，而是寻找一个：
1. 可明确描述的现有机制缺陷；
2. 针对该缺陷的最小充分方法；
3. 可通过诊断实验和反事实消融验证的机制性贡献。

## Primary Research Question

什么因素限制了现有图对比学习在不同图结构、标签稀缺或结构噪声条件下的节点分类泛化？
能否设计一个统一、可验证、可复现的学习机制解决该问题？

## Search Axes

以下只是检索方向，不预设任何一个一定创新：

- 假正样本与假负样本。
- 无负样本或 bootstrap GCL 的表征坍塌与偏置。
- 同配图和异配图中的语义一致性差异。
- 图增强是否破坏任务相关结构。
- masked graph modeling 与 contrastive learning 的互补性。
- prototype、cluster 或 class-conditional 对比目标。
- 结构噪声和语义噪声的分离。
- alignment-uniformity 在图数据上的失配。
- LLM 语义先验是否能提供独立于图结构的训练信号。
- 跨数据集或跨图域泛化。

## Primary Task

- 节点分类。
- 主实验优先采用公认划分和评测协议。
- 同配、异配和较大规模设置均需考虑。
- 低标签或噪声实验仅在它们直接支持核心机制时加入。

## Non-Goals

- 仅添加一个 gate、temperature、权重函数或 residual。
- 仅把视觉自监督目标机械移植到图上。
- 只在 Cora/CiteSeer/PubMed 上取得单 seed 提升。
- 依赖不公平调参、不同 backbone 或不同 split。
- 为追求表格结果堆叠多个无法单独解释的模块。
- 在没有最新查新的情况下声明 novelty。
- 把 pilot 结果写成正式结论。

## Desired Contribution

优先顺序：

1. 一个明确的新机制或新问题定义。
2. 能解释何时有效、何时失效的诊断分析。
3. 有竞争力的节点分类结果。
4. 可接受的额外时间和显存成本。
5. 有可能扩展到其他图任务，但不强行加入主论文。

## Compute and Timeline

- GPU: TBD
- 单卡显存: TBD
- 可用 GPU 数: TBD
- 预计总 GPU-hours: TBD
- 预计研究周期: TBD
- 目标 venue: 2026 顶会/顶刊，暂不绑定具体 venue

## Evidence Standard

idea 只有同时满足以下条件才能进入正式实验：

- 有明确的 closest work 和技术差异。
- 有低成本 falsification experiment。
- pilot 信号在至少两类图设置中不冲突。
- 增益不能仅由参数量、额外特征或更大搜索预算解释。
- 方法去掉核心机制后应出现可预测的性能或表征变化。
