# Stage 3.1.6 Scope

Date: 2026-06-26
Stage: Stage 3.1.6 Controlled Dataset Access Resolution

## Scope Boundary

1. 本轮只解决数据访问、dataset metadata、split JSON 生成与校验。
2. 允许 `controlled_download`，且仅限 Cora / Wiki-CS / Actor。
3. 不训练模型。
4. 不运行 evaluator。
5. 不运行 pilot。
6. 不使用 GPU。
7. 不克隆 baseline。
8. 不生成 accuracy / loss / performance table。
9. 不做 objective-family ranking。
10. 不进入 Stage 3.2。
11. 即使本轮 GO，也最多允许进入 Stage 3.2 planning / implementation approval，不允许直接 pilot run。

## Allowed Data Access

只允许通过 PyG 官方 dataset loader 访问数据：

- Cora: `torch_geometric.datasets.Planetoid(root="data/Planetoid", name="Cora")`
- Wiki-CS: `torch_geometric.datasets.WikiCS(root="data/WikiCS")`
- Actor: `torch_geometric.datasets.Actor(root="data/Actor")`

不允许手写 URL 下载脚本，不允许下载其他数据集，不允许安装依赖。
