# TOPIC-018｜应用机会卡模板

> 用于记录一个具体行业应用机会。先写业务需求与形式化问题，再寻找论文和项目；不得从仓库名称反推机会。

## 1. 机会身份

- Opportunity ID：
- 行业 ID / 行业：
- 二级业务领域：
- 价值链环节：
- 机会名称：
- 版本 / 创建日期：
- 状态：DISCOVERED / SCOPED / LITERATURE_MAPPED / PROJECT_MAPPED / AUDIT_SELECTED / PROTOTYPED / VALIDATED / DROPPED

## 2. 业务场景

- 业务主体/潜在使用者：
- 具体业务流程：
- 当前如何解决：
- 痛点与失败模式：
- 错误成本（安全、财务、合规、时间、声誉等）：
- 为什么现在值得研究：

## 3. 问题形式化

- 自然语言问题：
- 核心对象：
- 输入 / 输出：
- 状态 / 事件 / 时间语义：
- 关键假设：
- 目标性质（正确性、安全性、活性、等价性、稳定性、误差界等）：
- 反例或失败条件：
- 需要专家确认的语义歧义：

## 4. Lean 适配分析

- Lean 可能承担的角色：规格 / 定理证明 / 可执行参考模型 / 程序验证 / 精化 / 证书检查 / 知识库
- 可复用的数学理论或领域定义：
- 预期证明义务：
- 与实际代码/数据/硬件的连接方式：
- Lean 相比现有工具的增量价值：
- 更适合的替代或互补工具：
- Lean 不负责保证的事项：

## 5. 证据映射（按需填写）

### 行业需求证据
- 标准 / 法规 / 技术报告：
- 企业案例 / 工程实践：
- 学术综述 / 原始论文：

### 论文映射
| 论文 | 对应问题 | 形式化对象/方法 | 结论与限制 | 证据等级 |
|---|---|---|---|---|

### 项目映射
| 项目 | Lean/其他工具 | 与论文关系 | 可复用部分 | 当前状态 | 是否需要审计 |
|---|---|---|---|---|---|

项目关系必须标记为：DIRECT_COMPANION / DIRECT_IMPLEMENTATION / RELATED_LEAN_PROJECT / ADJACENT_TOOL / NO_PROJECT_FOUND。不得把相邻工具写成 Lean 项目。

## 6. 机会价值与落地

- 预期收益：
- 主要使用者/买方：
- 现有替代方案：
- 采用驱动因素（风险、监管、成本、审计、客户要求等）：
- 集成路径：
- 维护主体：
- 主要成本与障碍：
- 可在 1–4 周内验证的最小原型：
- 原型成功标准：
- 不成功时的停止条件：

## 7. 证据成熟度

- Lean 证据：L-PROD / L-RESEARCH / L-POC / HYPOTHESIS / NO-EVIDENCE
- 一般形式化方法证据：FM-INDUSTRY / FM-RESEARCH / NONE_FOUND
- 需求证据：DIRECT_CUSTOMER / STANDARD_OR_REGULATION / INDUSTRY_CASE / ACADEMIC_MOTIVATION / INFERENCE
- 实现证据：PRODUCTION / PROTOTYPE / PAPER_ONLY / NOT_RUN
- 仍未知的关键事实：

## 8. 决策

- 当前结论：ADVANCE / HOLD / DROP / NEED_MORE_EVIDENCE
- 结论理由：
- 下一步唯一动作：
- 需要补充的论文：
- 需要映射的 GitHub 项目：
- 是否启动项目审计：YES / NO
- 审计触发理由（必须说明为什么当前方向需要它）：
