# T01 · AQuA / RD-Agent(Q) 第一轮论文原文方法审计

- 日期：2026-10-29
- 任务：TOPIC-004 / Q01、Q02、Q07；GitHub Issue #3
- 状态：**主要方法章节、重要表格与 AQuA 的泄漏案例已核查；未完成全篇/全部附录/源码与独立复现实验**。
- 证据：AQuA arXiv 页面可读全文（第 3–7 节、附录 B）；RD-Agent(Q) arXiv:2505.15155v2 PDF（第 2–4 节、附录 C.4、D.2）。网页访问日期 2026-10-29。
- 约束：以下所有指标均为**原论文作者报告的数值**，并非本项目回测结果；不同 IC 定义不可直接比较。

## 1. AQuA：两套独立系统，绝不可写成“因子自动喂给模型”的现成实现

| 核查点 | 原文定位与原作者设计 | 我们的审计结论 |
|---|---|---|
| 研究型递归 | Section 3，Equation (1)：研究状态 R(t) 随实验结果更新，下一候选受其影响 | 是**同一系统的研究状态迭代**；不更新底层 LLM 权重 |
| 两个系统 | Section 3 / Discussion：Part I 为公式因子，Part II 为模型配置；无共享 agent、memory、candidate space、research state | 若将两系统合并，是**我们的新设计**，必须另设因子选择与模型训练隔离门禁 |
| 实验自由范围 | Section 3.1：人类冻结分割、特征、标签、评估器；Agent 只能提交受约束 DSL 表达式或配置差分 | 可迁移的是「智能搜索可变化，数据/评分契约不可变化」 |
| 因子分支 | Sections 4.1–4.5：Manager 串联 Data Steward、Visual Analyst、Idea Miner、Factor Evaluator、Backtest Engineer、Research Librarian | 因子 IC 约 0.190 为**加密货币 5 分钟组合信号的 validation Spearman IC**；不是独立 holdout 上可交易收益证明 |
| 模型分支 | Sections 5.1–5.6：配置驱动、训练/验证/交易回放和留出测试 | 美国股票下一 30 分钟预测，per-stock time-series Pearson IC +0.0843；作者报告 2021–2025 held-out Sharpe +2.50 @ 2bps two-leg cost；fully causal walk-forward 约 +2.0 |
| 泄漏分型 | Section 6：generation leakage（生成时偷看未来）与 selection leakage（自适应研究反复选最好测试结果） | **单靠审核 Agent 无法替代接口隔离** |
| 复现边界 | Section 5.2 / Appendix A、B / Section 7：部分确切因子表达式及模型特征细节未公开；不是真实交易业绩 | 不能宣称在本地完整复现，更不能直接迁移为 A 股收益 |

**关键错误案例（Appendix B）**：一个看似“开盘至当前分钟累计成交量 / 当日总成交量”的特征，把**收盘后才知道的全天成交量**作为当前分钟分母；另一个审核 Agent 曾将其误判为无前视。它证明“自然语言上看起来因果”与“算子在每个时间戳上确实因果”是两回事。验收时必须验证算子读取窗口与输入数据快照，不得把模型口头审核等同于程序性门禁。

**未证明之事**：论文中的跨轮曲线包含更多试验、候选池组合与经验迁移等因素；未得到与关闭研究记忆、相同预算下的严格因果消融，因此不能由 0.190 或 Sharpe 2.50 断定“记忆独立贡献了多少”。

原文：
- https://arxiv.org/abs/2608.12841 （Section 3、4、5、6、7、Appendix B）

## 2. RD-Agent(Q)：A 股研究更接近本任务，但系统仍不是交易实盘验收

| 核查点 | 原文定位 | 已核实信息 |
|---|---|---|
| 结构 | Section 2 / Figure 3 | Specification → Synthesis → Implementation (Co-STEER) → Validation (Qlib) → Analysis；因子与模型共同搜索 |
| 元调度 | Section 2.5 / Appendix A.2 | 使用上下文 Linear Thompson Sampling，在 factor 与 model 两类任务间选择；不是无约束元学习 |
| CSI300 | Section 3 | 训练 2008-01-01～2014-12-31，验证 2015-01-01～2016-12-31，测试 2017-01-01～2020-08-01；日线 |
| 2024+ 外推实验 | Appendix D.1 | CSI500 与 NASDAQ100：训练至 2021-12-31、验证 2022–2023、测试 2024-01-01～2025-06-30；**不等于已经评估 A 股盘中或 L2** |
| 指标口径 | Section 3 / Table 1 | IC、ICIR、Rank IC、Rank ICIR、ARR、IR、MDD、CR；必须在自己回测中固定定义 |
| CSI300 表 | Table 1 | R&D-Agent(Q) o3-mini：IC 0.0532、ARR 0.1421；R&D-Factor GPT-4o：IC 0.0489、ARR 0.1461（表内因子分支 ARR **高于**共同优化 o3-mini），故不能宣称“联合搜索在每个指标都最好” |
| 调度消融 | Table 3 / Appendix D.2 | o3-mini 同为 12h：random ARR 0.0897 / 33 loops、LLM ARR 0.1009 / 33 loops、Bandit ARR 0.1421 / 44 loops；**等运行时 ≠ 等试验数** |
| A 股模拟细节 | Appendix C.4.2 | 文中描述“t+1 开盘交易”和“收盘价成交”等不同时间点措辞，需审计执行细节、成本和可成交性，不得直接当盘中可执行策略 |

**需要验证的反对解释**：
1. 因子分支迭代更快，调度差异可能部分来自**有效实验轮数不同**，而非元策略更高效；
2. LLM 底层模型差异、代码生成成功率、候选空间和预算单位可能混杂调度效果；
3. 基准 CSI300 测试截至 2020-08-01，CSI500 的较新样本也不代表实时盘中 L2；
4. 论文 Appendix C.4.2 的交易时间/填价措辞需要结合源码与 Qlib 配置核对；**不能从描述自行补齐成交逻辑**。

来源：
- https://arxiv.org/pdf/2505.15155 （v2，PDF 第 3、5–9、24–26 页及 Appendix C.4）
- https://proceedings.neurips.cc/paper_files/paper/2025/hash/ac5c2b6e423883cbcacbcccf88491b78-Abstract-Datasets_and_Benchmarks_Track.html
- https://github.com/microsoft/RD-Agent （代码入口，尚未本地审计）

## 3. 初步跨文献结构对照

| 能力 | AQuA | RD-Agent(Q) | TOPIC-004 处理方式 |
|---|---|---|---|
| 候选生成 | 公式 / 配置两个不共享系统 | 因子+模型协同研发 | 初期仅以因子特征为目标；不必先重构接入 |
| 实验反馈 | 部分专属记忆与研究状态 | 知识森林、SOTA 池、失败反馈 | 结构化实验与失败账本，追踪来源 |
| 研究调度 | Part I Manager / Part II 配置循环 | two-armed contextual bandit | 与随机和固定调度对照，配平 tokens / walltime / 有效试验 |
| 数据隔离 | sealed DSL + test 不参与搜索 | 规范/验证模块，需审计具体实现 | 独立 evaluator 进程/权限与 PIT 字段强制门禁 |
| 金融外推 | Crypto 5m / 美国股票 30m | 中国 A 股日线 / 美国股票日线 | A 股盘中和 L2 属于新研究，不能继承外部收益数值 |

## 4. RSI 最低判定与反例

**过程级 RSI**：系统利用先前实验证据改变后续可执行研究候选或策略，在冻结实验合同下形成可追踪递归。AQuA 属于作者定义的这一有限类型。

**效果级 RSI（本专题更强的验收）**：在跨任务盲测、相同研究资源和独立检验下，元策略 D 对 A/B/C 基线的收益/有效假说率/鲁棒性提升有配对证据，且不能由数据泄漏、重复搜索或模型差异解释。**尚无本地证明。**

不算“效果级 RSI”的反例：
- 只增加研究次数，取最大历史 IC；
- 反复用最终测试集得分调提示词或筛选因子；
- 将两名 Agent 对未来函数的共同赞成当作无泄漏验证；
- 每轮保存日志但下一轮提案不依赖经验；
- 底层模型换代导致提升，却将其归因为研究元策略；
- 在没有对照的情况下，宣称因子与模型联合搜索自带样本外增益。

## 5. T01 剩余审计

- AQuA：锁定 arXiv 版本和作者清单；补完全附录与公开代码/可复现性声明；确认因子验证集被重复查询的具体约束。
- RD-Agent(Q)：核实 Appendix C.4 的订单时间和填价是否自洽；读取具体配置代码与外部数据依赖；核实不同实验的真实成本、预算与独立抽样次数。
- 完成全面源码/复现实验前，不把 T01 标为最终验收完成；当前为 **FIRST_PASS_METHOD_AUDITED**。
