# TOPIC-010 · D财政线数据准入（2026-11-14）

**状态：候选数据源矩阵已建；年度原始财政数据未下载、未清洗、未合并、未回归。**

## 已验证的来源

1. [英国财政责任办公室 OBR：300年英国财政数据](https://obr.uk/article/300-years-of-uk-public-finance-data/)及[下载页](https://obr.uk/data/)：数据包覆盖约1700年起的税收、支出、借款和债务；这是目前英国D线的首选完整长序列入口。注意不是所有字段都可能逐年无缺。
2. [Karaman & Pamuk（2013）](https://doi.org/10.1017/S0003055413000312)：以新整理的欧洲早期国家**中央财政税收**数据讨论战争、经济结构与政体的交互作用。论文对象是早期财政能力而不是工业化因果结果。原始12国分项仍待逐表核验。
3. [葡萄牙国家财政重建（2024）](https://academic.oup.com/ereh/article/28/4/453/7667247)与[ICPSR开放复现包](https://www.icpsr.umich.edu/sites/icpsr/view/studies/198143/versions/V1)：1367—1844年，区分财政收入组成、支出及地方财政；适用于葡萄牙反例测试。复现包页面可访问，但尚未下载文件。
4. [英格兰银行“千年宏观数据”](https://www.bankofengland.co.uk/statistics/research-datasets)：包含不同时间起点的英国宏观金融系列；不能误称所有变量从1086年起。
5. [荷兰国家档案 VOC](https://www.nationaalarchief.nl/onderzoeken/zoekhulpen/overzicht-van-voc-archieven-1594-1814)：可用于公司/船队贸易经济研究，但**不是荷兰政府收入数据**，不能直接与OBR国库财政比较。
6. [2026年 Govrev 全球历史税收数据](https://www.cambridge.org/core/journals/european-journal-of-political-research/article/financing-the-state-government-tax-revenue-from-1800-to-2012/3ECB24E0026C258AC660B88673A9E63C)：1800—2012年的31国中央财政收入；只能与本题后期历史部分衔接。

[候选数据源矩阵 CSV](fiscal_source_admission_m0.csv) 共12条，区分国家、时期、候选变量、来源口径、获取状态与下一步校验。

## 识别上的实质约束

`财政收入高`、`人均财政收入高`、`财政收入占GDP高`、`政府借款利率低`、`海军开支高`不等价。要解释长期海外竞争能力，至少需比较：
- 中央财政收入占GDP（税基和政体口径一致后）
- 债务余额及利息服务占财政收入
- 军费占政府总支出、海军经费的绝对和相对规模
- 战时增量融资、信用成本与税款抵押安排

**实证下一步：** 首先获取OBR与ICPSR的文件清单和原表，以及Karaman–Pamuk的可引用年度/十年财政重建表。逐字段审查国家边界、货币、银克转换、名义/实际和时间频率，然后才能绘制五国财政趋势图。

## 额外发现：因果结构不应只看战争或政体单变量

Karaman & Pamuk 2013的同行评审论文摘要报告，战争压力、经济结构与政治制度之间存在**交互作用**：政治制度对财政能力的影响取决于都市化商业经济或农业经济背景。这可以挑战“英国仅因制度不同而获得财政优势”的简化解释；此处仅报告作者结论，未经本专题独立复算。

## V2数据准入更新（2026-11-14）

- 新增BoE千年宏观数据库A1年度表公开DataHub镜像条目，Ubuntu联网实取并解析22,487条记录、65个变量；用于[1689—1850年度数据研究](boe_annual_fiscal_audit_v2.md)。源CSV校验SHA256见研究报告。
- 此来源属于**第三方整理的官方数据镜像**而非原Excel逐格审计；原Bank of England .xlsx URL HTTP200，但只核验了文件头及长度，未完成工作簿列头说明交叉核对。
- OBR历史财政Excel、葡萄牙ICPSR完整包依然未取得；不要将年度公共债务/净借款误当作税收或海军军费。
