# TOPIC-010 | M0/P0 数据字典与准入规则

- 规范 Issue：[AI_book #30](https://github.com/fweiger/AI_book/issues/30)
- 任务中心：[Task Center V1](https://github.com/fweiger/AI_tasks/blob/main/task-center/v1/ENTRY.md)
- 当前状态：**初始史料事件样本 / 非全量年表 / 未做跨国实证**
- 本轮资料：25份机构来源登记、33个事件节点、1张大西洋奴隶贸易估计数据小样本。
- 本轮实际采集窗口：1492—1765年事件；运输数据1601—1775年。研究总体范围1450—1850尚未覆盖完整。

## events_m0.csv 字段

| 字段 | 语义及约束 |
| --- | --- |
| `event_id` | 稳定、唯一事件ID（IR-001 ...）。 |
| `start_year`, `end_year` | YYYY整数；区间端点包括在内；`start_year <= end_year`。 |
| `date_precision` | `year` 仅指事件年份精度；`period` 指历史过程/战事跨年；绝不把区间中值伪装为确切年份。 |
| `country_actor` | 事件相关的欧洲国家；多方使用分号隔开，**不是这时这些国家真实疆域或现代国名的恒定口径**。 |
| `territory` | 事件地理区域（当代地名用于定位时不得误判为当时领土统治）。 |
| `main_domain` | `A`技术、`B`殖民/人口/贸易、`C`战争/政治、`D`财政能力，主线只有一个。 |
| `related_domain` | 可选次线；防止同一事件在四线被重复计数。 |
| `event_title`, `evidence_summary` | 事件和不超过一段的来源可核实概括；不自动构建因果箭头。 |
| `source_id` | 对应 `sources_m0.csv` 的实际引用；当前一事件一主来源，未来允许扩展为独立关联表。 |
| `limitations` | 记录无法从该史实直接推断的更强命题、估计精度问题或缺口。 |

**资料层级**：`sources_m0.csv` 中的档案目录/法案摘录最接近原始记录；国家博物馆和官方历史年表属于机构整理的二次史料。对话中产生的理论比较与因果猜想**没有**被记为史料证据。

## slave_carriers_m0.csv 口径

- 数据取自 [SlaveVoyages: Estimates](https://legacy.slavevoyages.org/assessment/estimates) 的**Selected National Carriers**选项，原始时间窗为每25年，记录是跨大西洋被强制运输的**估计人数**。
- `spain_uruguay`、`portugal_brazil`、`great_britain`、`netherlands`、`france` 均沿用来源的承运分组；包括历史政体/后继国，不等同国家在各年度的法律辖域。
- `all_national_carriers_total` 是该来源表中**所有**承运分组的同期总计，包含未列在此数据子集中的美国及丹麦/波罗的海等类别，因此五国分项**不必**恰好加总至总计。
- 人数是**流量的历史重建估计**，不是殖民地受控人口、奴役人口存量、移民数量、资本收益或殖民财政收入。
- 不将25年合计强行分摊成逐年记录；不得用某一时期的承运国份额代表全年/整个时代的人口控制权。

## 必须保持独立的指标族

1. `sovereignty_claim` / `effective_control` / `port_and_trading_post` 不同。
2. `captives_transported` / `enslaved_population_stock` / `colonized_population` 不同。
3. `EIC_or_VOC_revenue` / `colonial_tax_collected` / `metropolitan_treasury_revenue` 不同。
4. `tax_per_capita` / `total_tax_revenue` / `debt_borrowing_capacity` / `military_spend` 不同。
5. `innovation_date` / `adoption_date` / `productivity_growth_date` / `imperial_peak_date` 不同。

## 分期及可比性

- 1492—1599：葡西早期殖民扩张，做背景期；1600—1765：重点识别；1766—1850：反向反馈期**本批未采完**。
- 1707年之前使用 England/Scotland 等历史实体；1707年之后 Great Britain，不作未审计的时间序列直接拼接。荷兰共和国、法国王国、葡萄牙王国也应保留当时的政体字段，未来单独建立 country_historical_id。
- 对于无法核实的指标用 `unknown` 或空值并解释；不将观察缺失记为零。
- 经济史数据需保留来源自带计价单位、地域、币制、口径、频率及推算方法，转换为银克/人或GDP比例前进行交叉复算。

## 当前证据审查结论（不涉及因果权重）

1. 1600年英国东印度公司、1602年荷兰VOC和1664年法国东印度公司成立时间，显示不同国家的公司体系有先后发展。
2. 1651年航海条例是国家试图改变贸易承运格局的制度证据，不能仅凭法条判定执行效果。
3. 1694年英格兰银行成立和对法战争融资有官方一手机构史记载；不直接意味着工业投资获得同等资本。
4. 1709年焦炭冶铁、1712年蒸汽抽水属于**工业革命常用起点1760年之前**的实用技术突破。
5. 大西洋奴隶贸易早期英国不领先，18世纪中期英国在承运人数上的份额显著扩大；这仍不能直接推断其所控制殖民人口或利润规模。

## 仍然缺失

- 五国1500—1850可比的**年度**财政收入/支出/海军军费/国债/利率数据及各自会计边界。
- 技术人才跨行业迁移的工匠名册、造船厂—金属加工—蒸汽机厂的具体联通证据。
- 殖民控制的有效边界和受控人口随时间变动的档案基础。
- 工业化起点定义及工业产出/劳动生产率数据的一致性审计。

**唯一下一动作：** 从 Karaman & Pamuk、葡萄牙财政重建、英国财政史等研究提取原始表和数据许可，先建立财政数据跨国可比性矩阵，不用跨口径数字直接比较。
