# 2026-10-29 · RD-Agent(Q) 源码审计与数据契约

- 专题：TOPIC-004；关联 Q01/Q02/Q05/Q06/Q07、C002/C005/C006/C007/C008
- 范围：RD-Agent 2025-05-29 公开代码锚点、Qlib 2026-10-08 公开代码锚点与论文 Appendix C.4.2 / D.2。
- 方法：静态源码链路审计；未在本地安装或运行 RD-Agent/Qlib，未读取用户机器上的数据，未执行 A 股回测。

## 本轮新增关键发现

1. **测试集反复进入研究反馈是最高优先级风险。** Qlib SignalRecord 的默认预测段是 test，SigAnaRecord 以该段标签计算 IC；PortAnaRecord 使用测试期回测；RD-Agent 又把 experiment.result 用于 SOTA 比较和下一轮 action selection。公开默认链路因此存在适应性测试集选择风险。论文报告是否使用了其他隔离配置，仍待实验日志/作者配置核验。
2. **标签跨分段边界风险。** 标签用到未来两期收盘价，配置无显式 purge/embargo；必须增加交易日历边界测试，禁止直接把固定日期切分视为无泄漏。
3. **Bandit 奖励定义需要重审。** 现有代码使用绝对指标的加权分数，缺少显式的 SOTA 增量；context 与 reward 都来自最近已完成实验指标，且内部名为 sharpe 的比例实为 ARR/|MDD|。尾随空格指标键也需要运行时断言。
4. **默认数据通路是日线。** 数据生成脚本读取日频 OHLCV；因子处理器拒绝包含一分钟间隔的结果。不能直接把它当成分钟/Tick-L2 研究框架。

## 本轮更新

- 新增 [RD-Agent 源码审计](../research/RD-Agent-source-audit-2026-10-29.md)。
- 新增 [A 股数据契约模板](../research/a-share-data-contract-v0.json) 与标准库验证器。
- T02 协议新增测试集隔离、purge/embargo、Bandit 奖励与日线/盘中 adapter 的硬门禁。
- 所有 source_field 与执行成本仍为未映射状态；formal_run_allowed=false；没有本地收益结果。
