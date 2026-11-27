# 2026-11-23｜第二轮递归拆分至项目级子节点

## 目标

用户明确要求递归下钻不能停在一级/二级/三级或固定数量；每条研究分支必须继续到单一问题、明确形式化对象/性质、对应论文/标准和具体 GitHub 项目。最小原型和项目审计留待用户选择后，不作为本轮验收要求。

## 任务状态与协议

- 主任务：AI_book Issue #74 / TOPIC-018。
- 固定分支：`topic/TOPIC-018/lean-formal-verification-20261122`。
- PR #75 Draft，未合并。
- Task Center V1.2.2 锁定协议 commit：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`。
- 上轮递归规则事件已同步到 Issue #74 comment #7084291199；本轮声明独立 Writer event，未修改批准 Goal/Scope/Non-goals/AC。

## 本轮成果

- 将 60 个首轮行业节点重新定义为候选父节点，不再宣称固定数量就是最终叶节点。
- 新建 `industry-recursive-split-register.md`，新增 55 个更细的子节点，覆盖 zkVM、Rust-to-Lean、LTL/工作流、SNARK 组件、BFT、金融数学/PIT、铁路、ADAS、PLC、机器人、电网、生物模型、信息论/P4、神经网络验证、AI proof search、科学计算、法律和选举等方向。
- 每个子节点均列出具体问题、形式化对象/性质、论文/标准或技术资料、GitHub 项目和 Lean/相邻工具关系。
- 建立 CANDIDATE_LEAF / LEAF_CLOSED / PAPER_GAP / PROJECT_GAP / CONTINUE_SPLIT 状态。
- 更新主地图、行业机会地图、README 和 knowledge-map 的导航与“非固定数量”说明。

## 证据与限制

- 已读取的项目 README/官方文档只用于项目映射，不代表源码、许可证、依赖或构建审计。
- OpenVM-FV、SP1-lean、Zisk-FV 的证明范围和未完成项分别标记；Zisk-FV 仍在建设中。
- 金融、PIT、法律、医疗和科学计算的部分项目映射仍是 RELATED_METHOD 或 DOMAIN_REFERENCE，不得称为 Lean 已生产采用。
- 第二轮 55 个子节点仍有 CANDIDATE_LEAF / PAPER_GAP；不能宣称全部闭合。

## 下一步唯一动作

继续逐项复核 60 个父节点和 55 个子节点的论文—项目一一关系，拆分仍包含多个独立算法/组件/目标性质的节点，优先关闭 PAPER_GAP 和宽泛父节点。项目审计和最小原型留待用户选择。
