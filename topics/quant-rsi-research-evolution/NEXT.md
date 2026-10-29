# TOPIC-004 · 研究任务看板

## T01 / P0 — 研究层 RSI 的文献审计与判定表（首轮方法已核；全文/代码未验收）

输入：S01 AQuA 和 S02 R&D-Agent(Q) 版本明确的原始论文、附录、源码文档。

步骤：
1. 核对作者、版本、章节、数据域、候选搜索空间、预算和结果的完整出处。
2. 重建论文真实的研究循环、研究记忆与评估器；区别自动化、因子搜索和元研究策略更新。
3. 给出 RSI 最低标准：在**未见任务、预算配平、固定评估**下的可检验增益，并提供至少 3 个反例。
4. 更新 C001/C002/C007，提出最强竞争解释，记录 session 与 CHANGELOG。

验收：两篇论文的定位证据表、RSI/非 RSI 判定表、3 个反例及未核实项；未读到原文则不报完成。

## T02 / P0 — 冻结评估与消融试验设计（尚未执行）

设计四组：固定工作流、等预算随机/普通搜索、固定工作流+记忆、完整研究策略 RSI。冻结任务池、股票池、切分、标签、成本、盲测与预算。定义有效新假设产出率、可复现率、Rank IC/ICIR、净收益、失败重复率和研究算力账本。多重检验与盲测访问审计为硬门禁。

验收：可复核的预注册实验协议、泄漏清单、拒绝/停止规则。**不能编造指标值和样例数据**。

## T03 / P1 — 原创书稿首两章（尚未执行）

在 T01/T02 完成后，按 [12 章目录](book-outline.md) 撰写第 01、02 章，逐条注明来源/反例/不确定性与稳定 C-ID。不得把文章摘要当原文已核实。

## T04 / P1 — 研究知识结构与 A 股数据语义（尚未执行）

定义 Hypothesis、Experiment、Evidence、Failure、Knowledge、Evolution 六对象及版本接口；验证日线、分钟、逐笔数据中每个字段的含义和最早可得时间。优先复用既有数据接入与回放能力，不重复建接入层、不开展未经授权的真实账户实验。

## 交付与质量门禁

每一轮先读相关原文，保留独立反证、修订 C-ID/图谱、写 session/CHANGELOG，并执行 python3 scripts/validate_library.py。结构检查不证明金融研究结果有效。任务尚无执行结果。

## 2026-10-29 新增已完成文档

- [T01：主要原文方法审计](research/T01-paper-audit-2026-10-29.md)：阅读了 AQuA、RD-Agent(Q) 关键原文与表格，尚缺源码/全部附录审计，不能将任务标记为整体完成。
- [Q01：RSI 最低标准和非 RSI 反例](research/RSI-classification-criteria-v0.md)：已形成判定表；效果级 RSI 仍需真实盲测。
- [T02：冻结评估与消融草案](research/T02-sealed-evaluator-protocol-v0.md)：完成协议设计，真实数据范围/预算/隔离尚未核实，不能执行回测。

**下一动作（P0）**：核验 RD-Agent(Q) 附录的交易时点与源码，再审计 AQuA 版本/未公开配置；随后取得当前可用数据字段定义和时间戳，以批准 T02 冻结参数。


## 2026-10-29 第二轮：源码审计与可执行数据契约

- [RD-Agent/Qlib 源码审计](research/RD-Agent-source-audit-2026-10-29.md)：公开默认链路存在反复使用 test 指标反馈的高风险；同时发现标签边界 purge、Bandit 奖励时序和日线数据路径限制。
- [A 股数据契约模板](research/a-share-data-contract-v0.json)：daily/minute/tick 三类字段角色、时间可得性、标签切分、执行成本与门禁均已结构化，但真实字段尚未映射。
- [验证脚本](../../scripts/validate_quant_contract.py)：CI 运行结构检查；正式实验预检应运行 --strict。脚本不代表数据源本身已验证。

**P0 下一步：**
1. 明确第一轮实验的 required_frequencies（daily / minute / tick），然后从真实数据源文档与现有采集代码逐字段映射 source_field。
2. 确定标签定义与最远未来依赖，生成 purge/embargo 和测试集不可读权限。
3. 冻结执行时点、历史涨跌幅、费用、滑点/冲击和容量合同。
4. 之后再运行 A/B/C/D 消融。当前 contract status 为 BLOCKED_ON_DATA_CONTRACT，禁止把该阶段称为回测已启动。


## 2026-10-29 第三轮：基于现有数据合同补齐候选字段映射

- 从现有项目 `A股市场行为自动发现与概率统计研究系统_PRD_v1.0_20260925/01_data_contract/DATA_CONTRACT.md` 与 `DATA_PROFILE.csv` 读取到真实分钟源：`raw_stock_minute`，路径 `/data/data3t/data/A股分钟线/`，字段 `open,high,low,close,amount,volume`。
- 已把分钟候选源字段、量纲、原始未复权口径、归档日覆盖、已知缺档与样本级时间映射证据写入数据契约。
- `available_at` 在原始历史归档中不存在；不能把事件时间冒充真实可用时间。现有项目的 M02/M03 验收报告均为 `PASS_WITH_SCOPE_LIMITS`，但 M02 仅抽查部分原始数据页、M03 仅完整解码 12 个选定日期；本轮仍需保留这些范围限制。由于 `available_at`、源快照哈希和任务/执行协议未冻结，`required_frequencies` 仍为空，状态仍为 `BLOCKED_ON_DATA_CONTRACT`。
- 日频资金流在来源血缘/BJ 覆盖未核实前未准入；L2 归档在源项目中仍属后续阶段，不得混入当前契约。
- 预检器补充了必需字段角色、门禁完整性、日期顺序和错误类型保护，并新增回归测试；CI 成功只证明结构与回归检查通过。


## 2026-10-29 第四轮：数据源就绪度与盲测暴露审计

- 新增 [A 股 RSI 数据源准入与首轮实验就绪度](research/ashare-data-readiness-2026-10-29.md)。
- 继续读取既有项目 M02/M03 正式验收报告和机器可读 QA 摘要后，纠正旧 M00 文档与后续验收报告的状态冲突：M02/M03 均为 `PASS_WITH_SCOPE_LIMITS`，不是仍待启动；但 M02 数据页独立抽查 31 日、M03 完整解码 12 个选定日期，且存在隔离成员和 178 个空 canonical 分区。
- 已记录 M02 manifest/QA 与 M03 QA、runner/config 哈希，明确它们不是原始 ZIP/7z 全量数据的 hash。
- 现有 M04 已查看过多个历史时期的特征/收益结果，不能把这些时期直接当成 RSI 试验的未见盲测。
- 建议分钟 OHLCVA 作为首轮候选输入，但不替用户冻结任务族或期限；`required_frequencies` 仍为空，正式回测继续禁止。
