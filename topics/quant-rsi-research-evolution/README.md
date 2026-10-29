# TOPIC-004 · AI 量化研究的递归自我改进：从 Alpha 发现到研究系统自进化

- 创建于：2026-10-29
- topic_version：0.1.4；状态：SOURCE_AUDIT_PARTIAL（论文与公开源码调用链已部分核查，未全面运行/复现，没有本地回测）
- 形态：原创专题书工作区 + 研究任务；不是已经出版的书，不登记 B-ID。
- 历史线索：2026-09-14、2026-10-20、2026-10-26 的 Quant-RSI、AQuA、研究记忆、Harness 和元研究策略讨论。

## 核心问题

**在数据、研究预算与盲测协议一致时，AI 能否通过积累证据和修正研究策略，在未见任务上发现更多独立、可重复、扣费后有价值的 Alpha？**

本专题的 RSI 限定为**研究流程与研究策略的改进**；不是单纯增加搜索次数、训练模型权重或为既有因子反复调参。论文中的报告结果不能视作已在 A 股复现。

## 工作入口

- [研究问题 Q01–Q07](questions.md) · [原创专题书十二章提纲](book-outline.md)
- [阅读路线](reading-path.md) · [公开来源与历史对话线索](sources.md)
- [论点 C001–C008](claims.md) · [知识图谱](knowledge-map.md) · [JSON 图谱](knowledge-graph.json)
- [T01 原文方法审计](research/T01-paper-audit-2026-10-29.md) · [RSI 判定表](research/RSI-classification-criteria-v0.md)
- [RD-Agent/Qlib 源码审计](research/RD-Agent-source-audit-2026-10-29.md) · [A 股数据源就绪度](research/ashare-data-readiness-2026-10-29.md)
- [T02 冻结评估草案](research/T02-sealed-evaluator-protocol-v0.md) · [A 股数据契约](research/a-share-data-contract-v0.json)
- [第一轮任务 NEXT](NEXT.md) · [对话记录](sessions/README.md) · [版本日志](CHANGELOG.md)

## 双闭环研究设计（尚未实现）

1. **内层候选研究**：Research Intake → Hypothesis Planner → Experiment Builder → Sealed Evaluator → Failure Diagnostician → Research Memory → 新假设。
2. **外层研究策略**：Meta Controller 从训练期研究轨迹改进选题、资源分配与实验策略；用从未观察的独立任务、等计算预算的对照实验验证增益。
3. **治理门禁**：固定数据切分、标签定义、评估器、成本、盲测访问、代码版本。模型间共识并不构成独立证据；研究反馈不得读取外层测试集。

## 关联数据层和边界

- 日线：A 股因子、Rank IC / ICIR、T+1～T+5、成本/分组检验。
- 分钟：信号最早可得时间、流式计算、早盘识别、回放一致性。
- Tick / L2：订单失衡、承接/撤单、执行指纹；不推断账户身份。
- [TOPIC-002 微观结构](../market-microstructure-orderflow/README.md) 是经济机制来源，不重建现成数据接入，不复制书籍。
- RD-Agent 默认因子流水线为日线；分钟/Tick-L2 必须经过数据契约和独立 adapter，不直接复用默认回测。
- 未核实来源不得写为已精读，未运行实验不得宣称 RSI 有效；不得公开凭据、私有路径和受版权保护的完整材料。

**当前正式实验状态：BLOCKED_ON_DATA_CONTRACT。先完成真实字段、PIT 时间语义、标签切分与执行成本核验，再进入 A/B/C/D 消融。**
