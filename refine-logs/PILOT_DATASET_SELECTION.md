# Pilot Dataset Selection

Date: 2026-06-25
Stage: Stage 3.0

## Selection Principle

Stage 3.1 minimal feasibility set 最多选择 3 个数据集，目标是覆盖不同 graph regime 并降低工程风险。选择标准不是预期效果，而是加载路径清楚、split 协议可记录、能快速暴露 objective-family boundary 是否可测。

## Selected Minimal Feasibility Set

| dataset | regime | reason for inclusion | split protocol | official split or custom split | expected loader source | risk | fallback dataset |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cora | homophilic citation graph | 经典小图，工程 sanity 成本最低，适合先验证统一 evaluator、logging、metric extraction 是否工作 | pilot 使用 custom stratified random 1:1:8 split，保存 `splits/Cora/split_seed_{seed}.json`；不与 Planetoid public split 混表 | custom split for pilot；若使用 public split 必须另表标注 | PyG Planetoid or DGL Cora loader in Stage 3.1 | public split 与 custom split 容易混淆；小图可能过于简单 | PubMed |
| Wiki-CS | non-Planetoid homophilic/wiki-style graph | 检查信号是否不只来自 citation graph；已有常见 public splits，且 BGRL/GCA 文献中常见 | 优先 official Wiki-CS splits；若为了统一 1:1:8 另造 split，必须标注 `custom random 1:1:8 split` 并不得与 official split 混比 | official split preferred | PyG WikiCS loader or DGL WikiCS loader in Stage 3.1 | official split 数量和 evaluator 细节需统一；特征/标签处理要记录 | Coauthor-CS |
| Actor | heterophilic graph | 最小异配设置，用于暴露 objective-family boundary 是否跨同配/异配成立 | 优先使用公认 fixed splits；若 loader 不提供统一 fixed split，则保存 custom split JSON 并标注为 custom | official/fixed split preferred, custom only if necessary | PyG Actor / heterophily benchmark loader in Stage 3.1 | split 来源容易不一致；异配 benchmark 版本差异可能影响可比性 | Chameleon |

## Excluded For Stage 3.1

- PubMed: 作为 Cora fallback，不与 Cora 同时进入最小集，避免第一轮过重。
- Coauthor-CS: 作为 Wiki-CS fallback。
- Chameleon/Squirrel/Texas/Cornell/Penn94: 作为 Actor fallback 或 Stage 3.2 扩展候选，不进入 Stage 3.1 minimal set。

## Protocol Notes

- 不下载数据集。
- 不生成真实 split 文件。
- Stage 3.1 若发现 loader 不稳定，应优先替换 fallback，而不是扩大数据集数量。
- 不允许为了追求效果选择数据集。
- 不允许把 official split 与 custom split 放入同一可比表。
