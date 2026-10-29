# TOPIC-004 · 跨材料阅读路线

## 路线 A：定义 RSI / Q01

先核查 [AQuA 原始论文入口](https://arxiv.org/abs/2608.12841) 关于研究层级递归改进、两套研究循环及封闭评估器的设计。对照 [微软 R&D-Agent(Q) 论文说明](https://www.microsoft.com/en-us/research/publication/rd-agent-quant-a-multi-agent-framework-for-data-centric-factors-and-model-joint-optimization/) 的研究/开发/反馈环节。**已定位公开元数据及摘要，正文与附录尚未逐段核验。**

产物：可证伪的 RSI 定义、至少 3 个不算 RSI 的反例；修订 C001、C007。

## 路线 B：独立验证 / Q02、Q07

核查数据切分、候选数量、模型/标签与成本定义、预算、评价者访问权限；设计固定流程 / 随机搜索 / 固定流程+记忆 / 完整 RSI 四组等预算消融。保留未见任务的最终盲测集。

产物：评估协议草案、泄漏审计表和停机门禁，而不是凭论文自述生成本地收益。

## 路线 C：失败与元研究策略 / Q03、Q04

研究如何表示 Hypothesis、Experiment、Evidence、Failure、Knowledge、Evolution；对比保留正结果、完整轨迹与负结果的增量价值；记录遗忘、知识过期与回滚。

产物：概念数据契约与消融计划，**不依赖虚构样例数据**。

## 路线 D：金融特征的跨频率映射 / Q05、Q06

从日频开始，按字段语义与最早可得时间逐步延伸到分钟和 L2。参考 [TOPIC-002](../market-microstructure-orderflow/README.md)，核实 T+1、撮合、停牌、涨跌停和成本条件；目前不预设数据接口、样本数或研究结果。

产物：真实数据字段与预测标签契约，以及以后可执行的回放-流式一致性验收。

任何路线均需区分论文作者观点、历史讨论和我们的独立研究设计。
