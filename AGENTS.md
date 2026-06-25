<!-- ARIS-CODEX:BEGIN -->
## ARIS Codex Skill Scope
ARIS Codex packages installed in this project: skills-codex
Managed entries: 80
Manifest: `.aris/installed-skills-codex.txt`
ARIS repo root: `/root/aris_repo`
Project skill path: `.agents/skills/<skill-name>`
For ARIS Codex workflows, prefer the project-local skills under `.agents/skills/`.
When a skill needs ARIS helper scripts, resolve the repo root from the manifest or set it explicitly:
`ARIS_REPO=$(awk -F'\t' '$1=="repo_root"{print $2; exit}' "/root/autodl-tmp/gcl_idea_2026/.aris/installed-skills-codex.txt")`
Do not edit or delete symlinked skills in place; update upstream or rerun:
`bash /root/aris_repo/tools/install_aris_codex.sh "/root/autodl-tmp/gcl_idea_2026" --reconcile`
For copied Codex installs, use:
`bash /root/aris_repo/tools/smart_update_codex.sh --project "/root/autodl-tmp/gcl_idea_2026"`
<!-- ARIS-CODEX:END -->

## 项目记录

- 2026-06-25：初始化 GitHub 上传流程，新增 `.gitignore`，排除本机缓存、实验输出、大模型权重以及 `.agents/skills/` 绝对路径符号链接；保留 `.aris` 清单用于后续重建 ARIS 技能环境。
- 2026-06-25：补充 GCL 节点分类研究契约、benchmark 协议、research brief 与 Codex reviewer 配置，并同步本次更新到 GitHub。
- 2026-06-25：初始化 `research-wiki/` 持久研究知识库，创建论文、idea、实验、claim 与关系图目录，后续文献、想法、实验和 claim 需持续写入该知识库。
- 2026-06-25：修复 Stage 0 初始化协议，删除误写入的 shell heredoc 文本，并将阶段决策、协议变更、失败 idea 和证据状态统一记录到 `research-wiki/`。
- 2026-06-25：完成 Stage 1 文献调研与 research-wiki 更新，生成 GCL 文献地图、benchmark protocol 对照、gap candidates、method transfer pool 和 Stage 1 报告；记录外部源可用性与不可用影响。
- 2026-06-25：完成 Stage 1.5 数据源修复与 closest-work 精读，补充 high-risk 论文 PDF、协议审计、closest-work delta 表和 query_pack；仍禁止将 published result 视为 directly comparable，除非后续按项目协议重跑或完全证明一致。
- 2026-06-25：修复 DeepXiv 数据源，安装 `deepxiv-sdk==0.3.1`，并修补 ARIS DeepXiv adapter 的 deprecated `--mode` JSON 兼容问题；`health`、`search`、`paper-brief` 均验证通过。
- 2026-06-25：完成 Stage 1.6 DeepXiv 增强文献与协议补全，保存 raw retrieval 到 `notes/stage1_6_deepxiv/`，更新 closest-work/protocol/delta/wiki 记录；本轮未进入 Stage 2，未生成 idea，未运行实验。
- 2026-06-25：完成 Stage 2A gap-driven idea discovery，生成 10 个候选 idea、5 份 targeted novelty check、fresh `gcl_scientific_reviewer` 审查和 research-wiki idea 记录；主候选为 `GCL-I03` 与 `GCL-I02`，备选为 `GCL-I04`，本轮未进入 Stage 2B、未实现代码、未运行实验。
- 2026-06-25：将 GitHub 仓库 `coinrainy/gcl_idea_2026` 可见性从 private 修改为 public，并通过 `gh repo view` 验证当前状态为 `PUBLIC`。
- 2026-06-25：完成 Stage 2B refine 决策，SELECT `GCL-I03` 作为 active idea，`GCL-I02` 降为辅助 negative-validity audit / fallback；生成 `refine-logs/` 与 `docs/` 下的 Stage 2B 决策、pilot plan、claim matrix、metric leakage audit、closest-work 和 kill-argument 文档；本轮未运行实验、未写论文。

# GCL Node Classification Research Contract

## Research Objective

本项目研究图对比学习用于节点分类，目标是形成一个问题定义清晰、
机制创新明确、实验可证伪、具有 2026 年顶会/顶刊投稿潜力的方法。

SOTA 不是预设事实，只能由严格、公平、可追溯的正式实验支持。

## Primary Scope

- 主任务：节点分类。
- 主线：图对比学习。
- 重点关注：正负样本构造、无负样本学习、图增强、masked graph modeling、prototype learning、同配/异配鲁棒性、结构噪声、语义一致性、LLM 语义先验。
- 每篇论文只保留一个主贡献和一个直接支持性贡献。

## Experimental Status Labels

所有实验必须标记为：

- smoke：只检查代码能否运行。
- pilot：用于判断 idea 是否继续，不支持论文性能 claim。
- development：用于开发和调参，不支持最终 claim。
- formal：固定协议后的正式结果，可进入论文表格。

禁止把 smoke、pilot、development 结果称为 SOTA、robust 或 comprehensive。

## Evaluation Integrity

- 只允许使用数据集真实标签和公认官方评测脚本。
- 禁止使用 test set 选择模型、超参数、epoch 或增强强度。
- 所有方法必须使用相同 split 和相同 seed 列表。
- GCL 方法必须使用相同 frozen-encoder evaluator。
- GCN、GAT、GraphSAGE 等监督 baseline 不使用 GCL 的 frozen-encoder evaluator，但必须使用相同 split、相同 early stopping 规则和可比较训练预算。
- 没有官方划分时，必须保存并版本化 split 文件，优先使用 JSON 格式。
- 每次运行保存 commit、配置、seed、命令、日志、结果文件路径。
- 汇总表必须从原始 JSON/CSV 自动生成，不能手工复制最佳结果。
- 正式小型/中型实验默认 10 seeds，报告 mean±std 和每个 seed 原始值。
- 不删除失败结果或负结果。

## Baseline Rules

- 在实现主方法前，必须先复现最强相关 baseline。
- baseline 复现明显低于原论文时，不能据此宣称优于该 baseline。
- 优先使用作者代码或可信复现实现。
- 必须记录参数量、训练时间、显存和调参预算。
- 本方法不能拥有明显更大的搜索空间而不披露。

## Reviewer Routing

当需要 reviewer 时：

- novelty 和方法审查使用 fresh gcl_scientific_reviewer。
- 实验完整性审查使用 fresh gcl_experiment_auditor。
- result-to-claim 审查使用 fresh gcl_claim_reviewer。
- 独立 verdict 之间不得复用同一个 reviewer agent。
- reviewer 只接收文件路径、审查目标和输出格式。
- 不向 reviewer 提供 executor 的总结或希望得到的结论。

## Decision Discipline

每个阶段必须给出：

- GO
- REVISE
- PIVOT
- KILL
- BLOCKED

所有阶段决策写入 `research-wiki/log.md`，并在对应的 idea / experiment / claim 页面中保留状态。
失败 idea 必须写入 `research-wiki/ideas/`，避免后续重复生成。

## Data Split Rules

- 主实验默认采用 stratified random 1:1:8 split，即 train / validation / test = 10% / 10% / 80%。
- 所有方法必须使用完全相同的 split 文件。
- split 文件必须保存为 JSON 并版本化，不能运行时临时随机生成后不保存。
- 正式实验默认使用 seeds 0-9。
- 每个 seed 对应固定 split，并用于所有 baseline 和本方法。
- Wiki-CS、OGB 和异配图 fixed-split benchmark 优先遵循官方或公认划分。
- Planetoid public split 和 random 1:1:8 split 不能混在同一主表直接比较。
- 所有结果必须显式标注 split 类型。
- 若 split 协议不一致，禁止宣称方法优于对方。
