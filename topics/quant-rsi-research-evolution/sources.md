# TOPIC-004 · 来源台账与证据等级

## 可独立定位的公开研究（2026-10-29 已做部分原文审计）

- **S01**：[AQuA: Recursively Self-Improving Quantitative Trading Research Agents（2026，arXiv:2608.12841）](https://arxiv.org/abs/2608.12841)。已读取 arXiv 可访问全文 Section 3–7 和 Appendix B 的相关原文，重要机制与结果数值定位见 [T01](research/T01-paper-audit-2026-10-29.md)；精确版本、全部附录和代码仍待核查。
- **S02**：[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization（Microsoft Research；NeurIPS 2025）](https://www.microsoft.com/en-us/research/publication/rd-agent-quant-a-multi-agent-framework-for-data-centric-factors-and-model-joint-optimization/)。已读取 [arXiv:2505.15155v2 PDF](https://arxiv.org/pdf/2505.15155) 的 Section 2–4 与 Appendix C.4/D.2 关键原文和表格；[代码入口](https://github.com/microsoft/RD-Agent)，未本地复现。
- **S03**：[Agentic Quantitative Trading: A Survey of Workflows, Systems, and Evaluation（2026）](https://arxiv.org/abs/2608.31041)。摘要级研究地图，尚待核验全文。

## 仅作为选题来源的历史讨论

- **H01**：2026-09-14，Quant RSI 平台、AQuA、封闭验证和研究记忆。
- **H02**：2026-10-20，RSI 文献方法、point-in-time、自动反证与失败记忆。
- **H03**：2026-10-26，Atlas Wang / XTX 金融市场 RSI 转载讨论、Harness 和 Quant-RSI Kernel。
- 历史内容未提供可核实的对话 URL 或完整原始版本；不虚构对话 ID，不把转载摘要当成原作者已核查结论。

## 允许的证据级别

- 公开元数据/摘要级：仅能确认研究入口及作者摘要自述。
- 待原文核验：尚未逐段核查正式原文、实验、附录或源码。
- 研究设计：我们提出的实施方案、角色分工、约束和写作提纲。
- 实验支持：真实数据与冻结协议下可复核的独立结果。**目前无**。

仅储存合法引用、原创笔记与链接；不得复制受版权保护的全书/论文大段文本或上传私人机器地址及凭据。

## 新增审计产物（不是独立实验）

- [T01 文献方法审计（首轮）](research/T01-paper-audit-2026-10-29.md)
- [过程级/结果级 RSI 判定与反例](research/RSI-classification-criteria-v0.md)
- [T02 冻结评估协议 v0](research/T02-sealed-evaluator-protocol-v0.md)

原文定位的内容不意味着全部章节已阅读，论文作者报告的指标不提升为本地「实验支持」。


## S04 · RD-Agent(Q) 源码与 Qlib 执行链路（2026-10-29 静态审计）

- [RD-Agent 2025-05-29 源码锚点](https://github.com/microsoft/RD-Agent/commit/6e42d523a85df67aa13927abbf0894564c71880)：论文对应的历史代码提交。
- [历史回测配置](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/experiment/factor_template/conf.yaml)：CSI300、未来两期收盘价标签、close 成交、固定费用与 2017–2020 回测区间。
- [Bandit 实现](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/proposal/bandit.py) 与 [QuantHypothesisGen](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/proposal/quant_proposal.py)：状态、奖励和下一动作的静态代码路径。
- [Qlib SignalRecord / SigAnaRecord / PortAnaRecord](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/record_temp.py)、[DatasetH](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/__init__.py)、[TopkDropoutStrategy](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/strategy/signal_strategy.py) 与 [Exchange](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py)：信号、分段、成交价与交易限制执行路径。
- [论文 HTML](https://arxiv.org/html/2505.15155)：Appendix C.4.2 与 D.2。

审计报告：[RD-Agent-source-audit-2026-10-29.md](research/RD-Agent-source-audit-2026-10-29.md)。以上是公开代码静态审计，尚未运行源码，也未取得作者原始实验日志。
