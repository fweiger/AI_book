# RD-Agent(Q) 源码与回测协议审计

- 审计日期：2026-10-29
- 状态：SOURCE_AUDIT_PARTIAL；静态源码链路已核查，未运行 RD-Agent/Qlib，不代表已复现实验。
- 论文：R&D-Agent-Quant, arXiv:2505.15155，重点核对 Appendix C.4.2 与 D.2。
- RD-Agent 代码锚点：2025-05-29 的提交 [6e42d523](https://github.com/microsoft/RD-Agent/commit/6e42d523a85df67aa13927abbf0894564c71880)。
- Qlib 代码锚点：2026-10-08 的提交 [5435523](https://github.com/microsoft/qlib/commit/54355232463878d2eebb91fe0ee5fa7fa1f5976c)。
- 核心原则：将“静态代码可见的风险”与“运行时已证明的错误”分开；以下未运行回测。

## P0-A · 默认公开代码路径存在反复使用测试集指标进行研究反馈的高风险

可复核调用链：

1. RD-Agent(Q) 历史配置将训练期设为 2008–2014、验证期设为 2015–2016、测试期设为 2017-01-01 至 2020-08-01；因子标签为 Ref($close, -2) / Ref($close, -1) - 1。
2. Qlib 的 SignalRecord 调用 model.predict(dataset)，而 Qlib BaseModel.predict 的默认 segment 是 test；SignalRecord 也以 test 段取 label。SigAnaRecord 因此计算的是 test 段 IC/Rank IC。
3. PortAnaRecord 的 backtest 配置也明确使用 2017–2020 测试区间，输出带成本的收益指标。
4. RD-Agent 的 Qlib workspace 读取最新 recorder 的全部 metrics 到 experiment.result；因子反馈器使用 experiment.result 与 SOTA 比较，QuantHypothesisGen 又从最近实验的 result 提取 metrics，更新 bandit 并选择下一轮 factor/model 行动。

源码入口：
- [RD-Agent historical config](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/experiment/factor_template/conf.yaml)
- [RD-Agent quant proposal](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/proposal/quant_proposal.py)
- [RD-Agent result extraction](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/experiment/workspace.py)
- [Qlib SignalRecord / SigAnaRecord / PortAnaRecord](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/workflow/record_temp.py)
- [Qlib BaseModel.predict](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/model/base.py)

**审计判断：** 默认公开链路看起来会让研究循环反复接触同一个 test 段的预测与回测指标，再据此选择 SOTA、生成反馈或更新调度器。这属于严重的自适应测试集选择风险；在正式确认论文报告的运行是否采用不同的隔离配置之前，不能直接断言作者最终结果已被完全污染，但我们自己的框架必须禁止这种路径。

**本项目修正：** 把开发反馈与外层盲测彻底分离。研究控制器只接触训练/验证阶段的冻结评分；外层 test 结果由独立 evaluator 在方案锁定后评估。若 test 结果被查看后继续修改研究策略，该测试期即转为开发数据，不能再称独立盲测。

## P0-B · 两期前瞻标签与时间分段之间缺少显式 purge / embargo

标签 Ref($close, -2) / Ref($close, -1) - 1 使用未来两个交易日的收盘价。公开配置只声明 train/valid/test 的日期范围，没有显式 purge 或 embargo 参数。Qlib 的 DatasetH 按日期区间调用 handler.fetch；DataHandler 先载入 handler 时间范围内的数据，再按 segment 取片段。因此，分段末端的标签可能引用下一段的价格。

**状态：高可信边界风险，仍需用固定 Qlib 版本和真实交易日历做边界单元测试。** 对本项目，purge 长度应由目标的最远未来依赖决定；若标签用到 T+h，则至少剔除跨界的 h 个交易日样本，再根据标签重叠与交易持有期决定是否需要更长 embargo。不得机械复制论文日期切分。

源码入口：
- [Qlib DatasetH](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/__init__.py)
- [Qlib DataHandler](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/dataset/handler.py)

## P1-A · 交易时点、成交价与标签必须按执行链路定义

论文 Appendix C.4.2 的文字同时提到 t+1 开盘调仓与收盘价成交。历史配置明确使用 deal_price=close。Qlib TopkDropoutStrategy 在当前交易步读取前一交易步的信号，并把订单时间范围设为当前交易步；Exchange 按配置的 close 字段取成交价。

因此，实际代码配置指向“前一日信号 → 当前交易步的收盘价成交”，不能把论文中的“开盘”描述直接当成成交价格。论文文字与配置/框架的精确对应关系仍需作者运行配置或原始实验日志确认。

本项目每个任务必须分别记录：
- signal_available_at：信号所有输入实际可用的最晚时点；
- decision_time：决策发生时点；
- earliest_order_time：不含未来信息的最早下单时点；
- fill_time / fill_price_rule：模拟撮合时间与价格来源；
- label_start / label_end：收益标签实际覆盖的价格区间。

源码入口：
- [Qlib TopkDropoutStrategy](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/contrib/strategy/signal_strategy.py)
- [Qlib Exchange](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py)

## P1-B · Bandit 评分的时序、量纲与指标命名需要重做或独立验证

历史实现中：

- Metrics.as_vector 将 IC、ICIR、Rank IC、Rank ICIR、ARR、IR、负 MDD、最后一项比例组成状态向量；固定权重直接作用于不同量纲的原始数值。
- extract_metrics_from_experiment 中的变量 sharpe = ARR / (-MDD)，其数学定义是 Calmar Ratio，而不是 Sharpe Ratio；变量名容易误导后续维护。
- 年化收益指标键使用了带尾随空格的字符串，并以 0.0 作为缺失默认值。因子反馈器使用的指标键不带该尾随空格。必须在实际 recorder 输出上断言键一致，否则缺失指标可能静默变成 0。
- prepare_context 从最近完成的实验提取 metric，然后以同一 metric 调用 controller.record(metric, prev_action)，随后 controller.decide(metric)。因此用于更新历史 action 的上下文是实验后的指标，而非该 action 执行前冻结的状态；奖励也是固定权重下的绝对分数，没有显式计算相对行动前 SOTA 的增量。

**审计判断：** 不能据此认定 bandit 无效，但不能把该实现当作已经证明“边际研究效率”的标准。我们的 D 组应使用行动前可观测的 context，使用验证集上的预注册增量效用作为反馈，归一化各指标尺度，并将外层 test 完全排除于调度更新。

源码入口：
- [RD-Agent bandit](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/proposal/bandit.py)
- [RD-Agent quant proposal](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/proposal/quant_proposal.py)
- [RD-Agent feedback](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/developer/feedback.py)

## P1-C · 默认因子流水线不是现成的分钟 / Tick-L2 研究引擎

公开默认数据生成脚本使用 Qlib 的日频数据，字段为 open/close/high/low/volume/factor；factor data processor 对包含一分钟间隔的输出会走拒绝分支。因此不能把该默认流水线直接接到我们的分钟/Tick/L2 数据上，并假定语义与评估正确。

迁移策略：保留现有数据接入与存储；通过独立 adapter 输出统一的 Hypothesis / Feature / Experiment 接口。日线研究与盘中研究分开定义可得时点、标签和成交协议，不重构已有数据接入层。

源码入口：
- [RD-Agent daily data generation](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/experiment/factor_data_template/generate.py)
- [RD-Agent factor data processor](https://github.com/microsoft/RD-Agent/blob/6e42d523a85df67aa13927abbf0894564c71880/rdagent/scenarios/qlib/developer/utils.py)

## P1-D · 默认成交成本与涨跌停模型是简化设定

历史配置使用统一 0.095 限价阈值、买入成本 0.0005、卖出成本 0.0015、最低费用 5，且未显式配置 impact_cost 或 volume_threshold。Qlib Exchange 的 impact_cost 默认值为 0；TopkDropoutStrategy 默认 only_tradable=False、forbid_all_trade_at_limit=True。该配置不等于按板块/证券类型/历史制度变化精确建模的 A 股撮合，也没有为大资金冲击提供专属容量模型。

我们的协议必须在正式收益结论前核验历史涨跌幅规则、停牌/涨跌停可成交性、佣金/印花税、滑点/冲击、参与率和 T+1 卖出限制。未核验时只允许报告信号研究指标，不允许把结果称为可交易净收益。

## 本轮结论与行动优先级

1. **P0：封闭外层测试集。** 研究反馈、SOTA 替换、Bandit 更新不能读取最终盲测指标。
2. **P0：标签边界 purge。** 对 T+h 标签至少核验 h 个交易日的跨界样本，保留边界单元测试。
3. **P0：完成数据契约。** 先明确具体任务使用日线、分钟还是 Tick/L2，真实字段、available_at、交易规则和数据版本。
4. **P1：重构 Bandit 评估合同。** 行动前状态、行动、预算、验证集增量奖励、外层测试必须分离。
5. **P1：适配现有数据。** 不复制 RD-Agent 的数据接入，不直接使用其默认日线处理器跑分钟/Tick/L2。
6. **未完成项：** 未运行论文代码、未读取用户机器上的真实字段、未运行任何本地 A 股回测；上述结论来自公开源码静态审计。


## 第三轮补充：现有 A 股数据源的实际准入状态

从已存在的项目 `A股市场行为自动发现与概率统计研究系统_PRD_v1.0_20260925` 读取其 `01_data_contract/DATA_CONTRACT.md`、`DATA_PROFILE.csv` 和 `input_schema.md` 后，确认：

- 分钟核心候选源为 `raw_stock_minute`，路径 `/data/data3t/data/A股分钟线/`，CSV 字段为 `open,high,low,close,amount,volume`；分钟量为股、金额为 CNY，价格为原始未复权口径。
- 已画像日期为 2026-09-01：5,988 个成员、1,437,120 行、每成员 240 行；按当日 Qlib 股票主表过滤后 5,553 个个股代码全部出现，另有 435 个主表外成员。
- 归档清单覆盖 5,630/5,632 个日历日期，缺 2005-06-15 和 2013-11-13；全历史成员内容尚未逐日核验。2026-09-01 存在 219 个 `volume=0 & amount>0` bar，需保留并标记 volume 不可信。
- 原始 CSV 没有时间列，行序到分钟结束时点的映射只有样本交叉核验；原始历史数据也没有真实 `available_at` / receive timestamp。
- 同一数据合同明确日频资金流仍未准入、L2 逐笔档案延后；不得将其当作本轮已验证输入。

证据来源：现有项目 `01_data_contract/DATA_CONTRACT.md`（第 5–23 行）、`DATA_PROFILE.csv`（第 2–5 行）、`input_schema.md`（第 3–31 行）。以上是源项目既有审计结论，不是本轮重新扫描原始分钟 ZIP 的结果。当前 RSI 数据契约只补齐已知候选映射，仍保持阻塞。


## 第四轮补充：纠正源项目旧数据合同与较新验收报告之间的状态差异

最初读取的 `01_data_contract/DATA_CONTRACT.md` 是 2026-09-25 的 M00 文档，其中仍写有 M02/M03 后续门槛。继续读取同一项目的正式验收产物后，发现更近的状态证据：

- `reports/M02分钟序列标准化验收报告.md`（2026-09-25）明确 M02 为 `PASS_WITH_SCOPE_LIMITS`，扫描了 5,630 个现存归档日期，形成 3,602,865,840 行 canonical 数据；问题成员被隔离。它对数据页做的是 31 个交易日抽查，不是所有历史行逐一解码。
- `reports/M03行为切片验收报告.md`（2026-10-24）明确 M03 为 `PASS_WITH_SCOPE_LIMITS`，处理 5,630 个日期分区；全量 footer/schema/清单闭合通过，但数据页完整解码限于 12 个选定日期（8 个非空、4 个空边界），且保留 178 个空 canonical 分区。
- 因此，旧 DATA_CONTRACT/DATA_GAPS 中“尚未完成 M02/M03”的表述已过时；应以正式验收报告与 README 中的最新进度为准，同时保留抽样解码、隔离成员、缺档和空分区的边界。
- 这修正了“全历史 M02 manifest 尚未完成”的错误表述，但**不解决本专题的独立阻塞**：分钟原始源没有 receive_time/available_at，源快照/日历/股票池版本尚未绑定到本专题，且任务标签、切分、执行成本与盲测权限仍未冻结。

本轮只读取了项目文档和报告，没有重新扫描原始 ZIP/7z、没有修改用户的本地研究项目，也没有启动行为发现或回测。
