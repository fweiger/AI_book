# TOPIC-010 · 英国财政—战争年度数据：1689—1850年第一轮审计（V2）

> **状态：年度公开数据已实际读取并提取；原始BoE Excel只验证下载地址返回文件头，未逐格核对；OBR与ICPSR完整工作簿仍未取得。** 
> 关联权威 [Issue #30](https://github.com/fweiger/AI_book/issues/30) · [Draft PR #31](https://github.com/fweiger/AI_book/pull/31) · 研究维度D财政/债务与C战争关联。

## 1. 真实数据获取及来源层级

1. **一级机构来源**：[Bank of England: A Millennium of Macroeconomic Data, v3.1](https://www.bankofengland.co.uk/statistics/research-datasets)，原始Excel地址 `https://www.bankofengland.co.uk/-/media/boe/files/statistics/research-datasets/a-millennium-of-macroeconomic-data-for-the-uk.xlsx`。2026-11-14通过Ubuntu联网发起GET：HTTP 200，`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`，`Content-Length=27,533,690`，开头ZIP魔数`PK\x03\x04`。**该原始工作簿尚未完成全量下载和工作表导入核算。**
2. **本次实际解析的机器可读来源**：[DataHub/DataHub mirror of BoE A1 Annual](https://datahub.io/economic-history/millennium-macroeconomic-data-uk/_r/-/data/annual.csv)（[数据包元数据](https://datahub.io/economic-history/millennium-macroeconomic-data-uk/_r/-/datapackage.json)）。通过Ubuntu联网完整读取CSV（2,855,467 bytes），CSV原文件SHA256 `b772d31a4a0133ca046bb22b0e44d2d8dbcde4a701345dc18709f3a4ce788725`，总`22,487`数据行、`65`个不同指标。按 `variable_id` 筛选，不从名称相同的两条GDP序列任意删掉其一。
3. **无法获取的来源**：[OBR Historical Public Finances](https://obr.uk/data/) 下载端点HTTP 403；官方网页历史文字仍可读；政府网页存档镜像下载端点HTTP 405。[葡萄牙Costa等(2024) ICPSR 198143](https://www.icpsr.umich.edu/sites/icpsr/view/studies/198143/versions/V1) 公开详情页可访问，但传统`openicpsr`的全包下载端点HTTP 403。**不得称以上原始财政工作簿已下载。**

## 2. 本次提交的年度可读数据

- [财政原始字段子集：1689—1850，162个年份](data/boe_millennium_annual_fiscal_1689_1850_v1.csv)。列涵盖公共部门净借入、公共债务面值、中央政府债务面值与市值、Consols长期国债收益率。数值从DataHub年度CSV逐行提取，未插值。
  - 公共部门净借入/净借出：162/162（1689起；**借出为正、借入为负**）。
  - 公共部门债务名义面值：160/162（1691起）。
  - 中央政府债务：124/162（1727起；**财政年度末**，不与日历年末变量盲目对齐）。
  - Consols长期收益率：148/162（1703起，年度平均，不等同当年新增政府借款的加权成本）。
- [年度债务/GDP敏感性1700—1749](data/boe_debt_gdp_1700_1749_v1.csv) · [1750—1799](data/boe_debt_gdp_1750_1799_v1.csv) · [1800—1850](data/boe_debt_gdp_1800_1850_v1.csv)。共151年，所有151个年份包含两套名义GDP的债务比率计算，均有原始分母；名称相近的`nominal-uk-gdp-at-market-prices`与`...-2`为DataHub整理版两个不同变量ID，其**明确地域/历史界线差异还需要查原工作簿A1备注核实**。
- [战争/相对和平描述统计：10个区间](data/boe_war_peace_windows_descriptive_v1.csv)。从相同源数据按固定时间窗求和、均值并计算年度债务变化，不对战争因果作识别。

### 复算公式

`debt_to_gdp_v1_pct = 100 × public_sector_debt_calendar_yearend_par_gbp_m / nominal_gdp_v1_gbp_m`

`debt_to_gdp_v2_pct = 100 × public_sector_debt_calendar_yearend_par_gbp_m / nominal_gdp_v2_gbp_m`

`net_borrowing_to_gdp_v1_pct = -100 × public_sector_net_lending_calendar_gbp_m / nominal_gdp_v1_gbp_m`

`window_delta_debt = debt_at_window_end − debt_at_year_preceding_window_start`

`window_cumulative_borrowing = -Σ public_sector_net_lending_calendar_gbp_m`

**债务存量差与累计净借款不必相等。** 还包含会计调整、估值、公共部门范围、时间口径及其他stock-flow reconciliation。未完成一致性调和前不能把差额简单写作战争成本。

## 3. 与OBR 2023债务比率的定点交叉比对

| 代表年份 | BoE/DataHub债务/GDP（GDP版本1） | GDP版本2 | OBR文字基准 |
| --- | ---: | ---: | --- |
| 1700 | 21.76% | 22.42% | 1700/01约22% |
| 1750 | 82.31% | 84.84% | — |
| 1760 | 94.52% | 97.42% | — |
| 1780 | 121.71% | 125.45% | — |
| 1800 | 143.48% | 147.88% | — |
| 1815 | 184.30% | 164.64% | 1815接近180% |
| 1850 | 150.81% | 134.92% | — |

OBR [2023年历史财政综述](https://articles.obr.uk/300-years-of-uk-public-finance-data/index.html)给出1700/01约22%、1815接近180%。BoE镜像数据计算的第一版GDP分母在两端接近官方叙述；**这只是有限定点的方向验证，不能据此推断所有年份定义相同**。对第二条GDP历史口径，1815年的敏感性差异达到19.66个百分点；任何对“1815债务/GDP精确峰值”的陈述必须锁定分母与地域口径。

## 4. 战争期间财政变化（英国名义公共部门债务；百万英镑）

| 历史窗口 | 债务期初 | 期末 | 存量变动 | 同期累计净借款 | 年均Consols收益率 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 西班牙王位继承战争子区间1703—1714 | 17.70 | 50.43 | +32.72 | 29.88 | 6.68% |
| 奥地利王位继承战争1740—1748 | 51.16 | 81.13 | +29.98 | 25.33 | 3.25% |
| 七年战争1756—1763 | 77.23 | 144.20 | +66.97 | 56.59 | 3.56% |
| 美国独立战争1775—1783 | 137.93 | 257.52 | +119.59 | 73.10 | 4.48% |
| 法国革命及拿破仑战争1793—1815 | 267.18 | 888.72 | +621.53 | 412.71 | 4.84% |

以上仅是时间窗内**同现**的量化现象。西班牙王位继承战争史学常用1701—1714，本表刻意从1703开始以保障长债收益率数据可读，不得将该子区间误称完整战争统计。相对和平时期可能有其他地区冲突、殖民战争，不能称绝对和平。

重要观察：英国在多次战争期间债务累计明显增加，但可用的长期国债收益率并未与名义债务余额同比放大。此点与“存在可维持的政府融资市场”相容，**尚不能证明信用机制独立导致工业革命**。

## 5. 尚未解决的因果问题与数据缺口

- **OBR与Costa财政收入/GDP冲突仍未解决**：OBR称18世纪平均税负约8%GDP；Costa Table3中英格兰中央政府收入/GDP为1700—1749年5.7%、1750—1799年6.6%。二者数据范围、政府边界、GDP基期与聚合方式均须核对；本轮BoE A1年度 headline csv**没有1700—1800逐年税收总量变量**，不能用债务数据替代税收数据。
- **同频跨国仍不足**：荷兰、葡萄牙、法国、西班牙没有与英国同口径的1689—1850年逐年税收/军费/债券收益率面板。跨国比较暂保持Costa与Broadberry已发表50年/十年表。
- **战争不等同工业革命原因**：要检验战争融资是否促进机械制造，需增加军工订单、民用工厂分布、行业产量与技术采纳年份，设立荷兰和法国控制组。
- **出处独立性**：本批CSV属于BoE第三方DataHub整理版，原Excel可访问但未核对逐格一致。整个数据管道不应标记为完整一级数据审计通过。

## 6. 实际QA及下一项工作

- 已在远端将CSV全量解析，按`variable_id`验证唯一性，拒绝NaN与异常巨大数值，并保留缺失；本轮提取是`run_script` Python标准库`csv`运行结果。
- GitHub回读检验：初始财政表162行，派生三个文件分别50/50/51行；债务率与净借款比值公式可重新逐年复算。
- 后续对【仓库 CI】与【独立史学真实性】分别报状态，不能互相替代。

**唯一下一动作：** 为英国获取官方原Excel的A1元数据和税收/军费明细，或找到合法可用的1700—1800税收及军费年度原表；优先明确两条名义GDP序列的地域定义，并解决OBR—Costa税收/GDP的差异。其后再开展战争融资与工业化因果识别。
