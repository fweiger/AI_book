# 2026-10-29 · T01 主要原文审计与 T02 协议草案

- 专题：TOPIC-004；Q01/Q02/Q07，关联 Q05/Q06
- 材料：AQuA Section 3–7 / Appendix B（arXiv HTML 可读原文）；RD-Agent(Q) arXiv:2505.15155v2 Section 2–4 / Appendix C.4 / D.2（PDF 原文）；均未运行源码与复现。
- 初始状态：两篇研究先前只登记为摘要级。

## 新证据

- AQuA 两系统不共享研究状态；Part I Crypto 5m 约 0.190 是 validation Spearman IC，Part II US equity 30m +0.0843 是 held-out per-stock Pearson IC。
- AQuA 附录 B 记录了盘中分母使用当日完整成交量的未来函数，AI 审核曾漏掉。
- RD-Agent(Q) 的 CSI300 日线与 Thompson Sampling 调度有原文位置；表 3 同为 12h 但随机 33 loops、Bandit 44 loops，并非实验次数相同。
- 两篇论文均不足以单独证明“研究记忆/元控制器”的独立因果贡献，也未验证当前 A 股盘中场景。

## 本轮更新

- C001：由纯设计假设 → **文献有循环机制支持，但本地增益仍待实证**。
- C002：由待原文核验 → **AQuA Section 3/6/Appendix B 有原文机制与失败案例支持**。
- C005：由一般系统要求 → **新增 AQuA Appendix B 特定未来成交量分母反例**。
- C007：由一般外部效度约束 → **明确区分 AQuA Crypto/US 与 RD-Agent(Q) A 股日线**。
- 未新增/重编号 C-ID、R-ID；topic_version 只提升 PATCH（0.1.0→0.1.1）。
- 新增 [T01 论文审计](../research/T01-paper-audit-2026-10-29.md)、[RSI 判断标准](../research/RSI-classification-criteria-v0.md)、[T02 协议草案](../research/T02-sealed-evaluator-protocol-v0.md)。

## 尚需验证

AQuA 精确版本、全部附录和封闭协议的实际实现；RD-Agent(Q) 源码、订单时点与填价一致性；实证预算配平、数据源语义、执行成本和任何 RSI 增益。没有产生本地 Alpha 回测结果。
