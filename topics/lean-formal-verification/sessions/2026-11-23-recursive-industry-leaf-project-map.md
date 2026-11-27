# 2026-11-23｜行业递归下钻至 GitHub 项目叶节点 v0.2

## 用户明确要求

不能只把一级行业拆到二级，也不能停在三级；必须沿着行业—业务领域—细分领域—具体场景—具体问题持续下钻，直到每条研究分支到达实际 GitHub 项目。论文和项目都必须映射。项目内部审计、最小原型和生产集成可留待用户选择方向后处理。

## 任务恢复与协议

- 主任务：AI_book Issue #74，TOPIC-018。
- 分支：`topic/TOPIC-018/lean-formal-verification-20261122`；PR #75 Draft。
- Task Center V1.2.2 锁定协议 commit：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`。
- 本轮恢复时 PR head：`b56c96dcd97c3ea22d817ddff3d6067a25885622`；Knowledge-base integrity Run #1294、Lean PIT Run #63 success。
- 未修改批准 Goal/Scope/Non-goals/AC，沿用原 Issue #74 与同一 Tracker。

## 递归结构与叶节点规则

行业 → 业务领域 → 细分领域 → 场景 → 具体问题 → 形式化对象/目标性质 → 论文/标准 → GitHub 项目。深度可变。每个叶节点必须有实际 GitHub 项目，项目关系区分 Lean 直接应用、Lean 研究、Lean 基础设施、相邻形式化工具和行业参考实现。没有直接 Lean 项目时，必须如实标记，不得冒充 Lean 采用。

## 本轮交付

- 新建 `industry-leaf-project-map.md`：12 个一级行业、60 个最小研究单元，逐条列出具体问题、形式化对象、论文/标准或原始资料、GitHub 项目和关系标签。
- 更新主框架、行业机会地图、机会卡模板、README、knowledge-map、field-map、field-evidence-matrix、bibliography 与 sessions 索引。
- 现有 22 个方向级矩阵继续作为下钻起始证据；新行业叶节点地图作为行业覆盖主表。

## 证据边界

- GitHub 项目映射不等于源码审计、许可证审计、clean build 或证明完整性验收。
- 已明确标记 Lean 3 历史项目、归档仓库、早期 proof-of-concept、相邻工具和行业参考实现。
- 60 个叶节点是首轮覆盖，不宣称行业穷尽；论文—项目的直接 companion 关系仍需逐条复核。

## 下一步唯一动作

逐项核对 60 个叶节点的论文—项目关系，补充仓库用途/来源/版本锚点；继续拆细仍然过宽的叶节点，直到每个终点都有明确问题、论文和 GitHub 项目。项目审计和最小原型留待用户选定方向后。
