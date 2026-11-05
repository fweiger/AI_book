# TOPIC-006 · 金融 AI 的能力边界：可信数据、领域学习、可验证建模与预测

- 创建日期：2026-11-05
- 专题版本：**0.1.1**
- 状态：**DISCUSSION_ONLY / NEEDS_EVIDENCE**
- 讨论主帖：[AI_book Issue #22](https://github.com/fweiger/AI_book/issues/22)
- 原始素材：[Joseph Kim, How OpenAI Built ChatGPT for Bankers and Analysts](https://www.youtube.com/watch?v=opHmX7qClzE)
- 来源等级：一手演讲及公开产品陈述已定位；学术论文以公开摘要和可读网页为依据，**未宣称全部精读**。

## 核心问题

**金融数据达到可信、完整、及时、可审计之后，要让 AI 在金融模型构建、持续分析和高难度前瞻预测中达到专业级可靠性，究竟还缺哪些能力？**

本专题围绕三组张力组织讨论：
1. 数据作为行业 AI 的必要投入，能否单独解释分析质量？**数据准确并不保证预测准确**。
2. 金融领域训练的增益，是否真正超过基础模型 + 精确检索 + 计算工具 + Skills 的增益？
3. “能生成财务 Excel/报告”“能长期承担项目”“能超越专家预测”是不同的能力门槛，不得混为一谈。

## 五层研究链（待检验的结构假说）

1. **数据层**：准确、完整、及时、版本化、point-in-time、财务口径、权限与来源；
2. **知识/模型层**：金融语义、会计与估值规则、专业数据理解、必要时后训练；
3. **执行层**：检索、MCP、程序计算、Skills、工作簿与报告生成；
4. **验证/Agent 层**：跨表公式检查、审计、恢复、持续任务状态、人工授权；
5. **预测/决策层**：事前预测封存、样本外、基准、人类专家对照、风险及真实成本。

## 三项 2027 预测（不是事实）

- **P1**：金融人员越来越少通过手工操作 Excel / PowerPoint 来生产财务模型与推介材料，重点是交付工作流而不是文件格式本身。
- **P2**：金融 Agent 逐渐像长期共事的分析师：保留上下文、管理分配任务、主动跟进。
- **P3**：模型在企业盈利预测、商品价格判断、投资想法等关键前瞻性任务超过顶级人类专家。

详细原话和时间戳见 [sources.md](sources.md)，任务和反证见 [questions.md](questions.md)、[claims.md](claims.md) 与 [NEXT.md](NEXT.md)。以上预测均待独立、预注册和样本外验证。2026年10月的 [MBABench 2.0](https://arxiv.org/abs/2610.31711) 表明复杂专业工作簿构建依然困难，不能以“能写入 .xlsx”代表达到专业交付质量。

## 如何参与

请在 [讨论 Issue #22](https://github.com/fweiger/AI_book/issues/22) 评论，格式建议：`TOPIC-006 / Qxx / Hx或P1-P3 / 主张 / 可核查来源 / 证伪条件 / 未知项`。独立观点和自动化实验不能取代原始证据、专业审计或真正的样本外检验。

- [2026-11-05：八条金融 AI 主线与证据地图](landscape-2026-11-05.md)
- [全行业多 Agent 研究协议](multi-agent-protocol-2026-11-05.md)
- [问题列表](questions.md)
- [待审计论点](claims.md)
- [来源台账](sources.md)
- [知识图谱](knowledge-map.md) / [机器图谱](knowledge-graph.json)
- [研究路径](reading-path.md)
- [下一步](NEXT.md)
- [过程记录](sessions/README.md)
- [版本记录](CHANGELOG.md)

仓库公开；不得发布个人本地路径、付费/私有财务数据、账号密钥或大段受版权保护的转写。未经合并的草稿不能标记 INTEGRATED。
