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

cat >> AGENTS.md <<'EOF'

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
- 除了GCN等监督方法，其他方法必须使用相同 split、相同 evaluator、相同 seed 列表和可比较训练预算。
- 没有官方划分时，必须保存并版本化 split 文件。
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

所有决策写入 DECISION_LOG.md。
失败 idea 写入 research-wiki，避免后续重复生成。
EOF

## Data Split Rules

- 主实验默认采用 stratified random 1:1:8 split，即 train / validation / test = 10% / 10% / 80%。
- 所有方法必须使用完全相同的 split 文件。
- split 文件必须保存并版本化，不能运行时临时随机生成后不保存。
- 正式实验默认使用 seeds 0-9。
- 每个 seed 对应固定 split，并用于所有 baseline 和本方法。
- Wiki-CS、OGB 和异配图 fixed-split benchmark 优先遵循官方或公认划分。
- Planetoid public split 和 random 1:1:8 split 不能混在同一主表直接比较。
- 所有结果必须显式标注 split 类型。
- 若 split 协议不一致，禁止宣称方法优于对方。
