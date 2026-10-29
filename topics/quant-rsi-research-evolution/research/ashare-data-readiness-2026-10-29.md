# A 股 RSI 研究的数据源准入与首轮实验就绪度（2026-10-29）

## 结论

当前能从现有项目证据中确认的最低成本候选输入是 **原始 1 分钟 OHLCVA**。这只是候选路径，不是已冻结的实验选择。该输入的 M02/M03 处理链已通过 `PASS_WITH_SCOPE_LIMITS`，但它不能自动满足 RSI 研究的点时点、标签、盲测和可交易收益要求。

本报告初始审计时，TOPIC-004 尚未确认首轮任务，因此 `required_frequencies=[]`。2026-10-30 用户确认分钟 OHLCVA 双轨任务后，机器可读契约将 `required_frequencies` 更新为 `["minute"]`，仅表示设计选择；正式准入仍阻塞：

- `status = BLOCKED_ON_DATA_CONTRACT`
- `required_frequencies = ["minute"]`（设计选择，不代表正式准入）
- `formal_run_allowed = false`

## 1. 已有输入与真实边界

### A. 原始分钟行情 — 可作为候选核心输入

- 源 ID：`raw_stock_minute`
- 路径：`/data/data3t/data/A股分钟线/`
- 原始 CSV 字段：`open,high,low,close,amount,volume`
- 单位：`volume` 为股，`amount` 为 CNY；价格为未复权日内价格。
- M02 处理产物：5,630 个归档日期，3,602,865,840 行 canonical 数据、15,011,941 个证券日；1,458,212 个有效主表证券日没有对应源成员，作为覆盖缺口保留。
- 已知隔离：475,299 个 schema-mismatch 成员跨 177 个日期；11,052 个重复归一化 BJ 成员；3,145 个 OHLC-invalid 成员；46 个行数不符成员；4 个解析错误成员；1 个非 CSV 成员。
- M03：5,630 个日期的清单/输出闭合检查通过，但保留 178 个空 canonical 分区。M02 独立数据页 QA 抽查 31 日；M03 数据页完整解码仅覆盖 12 个选定日期。
- 时间：原始 CSV 无时间列，交易日和分钟结束时间从归档日期及行序推导。样本交叉核对支持行序映射，但不能把它误称为源端真实时间戳。
- 关键缺口：没有真实 `receive_time` / `available_at` / revision timestamp。任何回放必须把可用时点和延迟模型作为明确假设记录。

对应既有证据：
- `reports/M02分钟序列标准化验收报告.md`
- `reports/M03行为切片验收报告.md`
- `03_sequence_normalization/output/final_qa_summary.json`
- `03_sequence_normalization/output/archive_manifest.jsonl`
- `04_behavior_slicing/output/final_qa_summary.json`

QA 工件、manifest、M03 runner/config 的 SHA256 已写入 `a-share-data-contract-v0.json` 的 `processing_provenance`。这些哈希是处理证据版本，不是原始 ZIP/7z 全量内容的哈希。

### B. 日频资金流 — 当前不得纳入

现有文件画像覆盖 2010-01-04 至 2026-09-24，14,071,063 行、5,840 个代码；382,704 行至少一个数值字段为空。文件含 13,087 条 `.BJ` 记录，而公开字段文档描述 SH/SZ。由于本地文件血缘、北交所覆盖和缺失成因未核实，当前状态是 `NOT_ADMITTED`。不得将空值填零，也不得将其与分钟行为直接 join。

### C. 东财分钟资金流 — 不可用

既有项目记录的原始 COS 路径当前不可访问。派生输出不能替代原始来源、字段语义与覆盖审计，因此不能用来构造当前输入契约。

### D. L2 逐笔 / 委托 / 盘口 — 暂缓

既有项目记录了 2026-09-01 至 2026-09-22 的 16 个大型 7z 归档，但本轮未重新读取或审计其 schema。它们不是本轮已准入输入；不能假设其字段、时序或完整性已验证。

## 2. 对 RSI 研究设计的影响

不能直接把既有 M04 结果期当作全新盲测。现有研究项目已查看过 2022、2023、2024、2025 及 2026 年若干时期的特征/收益结果；这些日期即使在文件系统中仍可访问，也不能自动被称为“未见测试集”。

要验证研究系统是否真正自我改进，必须把两个层次分开：

1. **研究开发反馈**：可以使用训练/开发区间，帮助生成假设、诊断失败和调整研究策略。
2. **外层独立评估**：只能在任务、候选空间、预算、标签、成本与研究策略冻结后，由独立 evaluator 计算；不向研究控制器回传单次试验的外层 test 指标。

如果测试结果被研究代理看到并据此修改策略，该测试集就变成开发数据，不再是独立盲测。

## 3. 还不能冻结的条件

1. 首轮任务究竟评估哪一类新假设：分钟行为特征、已有 M04 方法的改进，还是独立的日线因子研究。
2. 对应的 `required_frequencies` 与目标收益期限；不应在没有任务定义时把 daily/minute/tick 一并强制接入。
3. `available_at` 的回放规则和延迟假设；原始分钟文件本身不含这个字段。
4. 原始快照 hash、日历版本、股票池版本和 source version；处理 QA 哈希不能替代 raw data hash。
5. 标签表达式、信号/入场/退出时间、purge/embargo、历史涨跌幅限制、费用、滑点、冲击和容量规则。
6. 外层盲测的访问权限与审计日志，确保 test 指标不会进入 proposal、SOTA 选择或 Bandit 更新。

## 4. 建议的下一步

先把 **分钟 OHLCVA** 作为首轮候选输入，复用已有 canonical/M03 输出，不重建数据接入层；先做一个**新的、未被现有 M04 结果直接选优过的任务族**，并把最终测试输出封装给独立 evaluator。日频资金流和 L2 保持排除，直到各自准入门槛完成。

这只是推荐路径；在任务族和目标期限确定之前，不把它写成已批准的 `required_frequencies`，不运行正式回测。


## 5. 2026-10-30 双轨任务对齐后的状态更新

用户已确认首轮任务族为分钟 OHLCVA 行为特征发现，预测期限 T+1/T+3/T+5，并选择两项独立实验：A 盘中滚动特征、B T 日全天聚合特征。机器可读数据契约现将 `required_frequencies=["minute"]` 作为**设计选择**，不代表该数据源已完成本专题的正式准入；状态仍为 `BLOCKED_ON_DATA_CONTRACT`，`formal_run_allowed=false`。

详细定义见 [双轨实验设计](experiment-plan-v0.1.md)；历史暴露见 [历史研究暴露登记](historical-exposure-register-v0.1.md)；盲测访问边界见 [独立评估器访问控制计划](sealed-evaluator-access-plan-v0.1.md)。
