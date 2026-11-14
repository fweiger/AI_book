# CASE-PRT-001｜葡萄牙帝国第一轮证据审查（M0）

**权威Issue**：[AI_book #34](https://github.com/fweiger/AI_book/issues/34) · **上位研究**：[TOPIC-010 #30](https://github.com/fweiger/AI_book/issues/30)。**数据状态：**首批历史发表于同行评审的量化结果已结构化；原始巴西黄金运出和葡萄牙年度产业/财政面板尚未下载复算。

## 首轮发现：帝国贸易可以创造财富，同时黄金可以压制制造业

有两篇结论表面冲突、实际上研究对象不同的量化论文：

- [Costa、Palma、Reis (2015)](https://academic.oup.com/ereh/article-abstract/19/1/1/2754564)：估算早期葡萄牙帝国贸易对经济增长贡献显著；在殖民扩张鼎盛时期，剔除帝国经济联系会使人均收入**至少降低约五分之一**。是作者经济计量模型估计，**不是本项目重新复算**。
- [Kedrosky、Palma (2025), Journal of Economic History](https://www.cambridge.org/core/journals/journal-of-economic-history/article/cross-of-gold-brazilian-treasure-and-the-decline-of-portugal/B98AA5BDD404B56014FAAAD1861DC427)：利用合成控制模型，估计巴西黄金冲击使1800年葡萄牙人均GDP比“没有巴西黄金”这一反事实路径**低约40%**。模型关注黄金导致实际汇率升值、国内制造业受损的**资源诅咒**，不是“帝国所有贸易从来都是净负收益”。

**两种结果可能同时为真：**贸易网络贡献正、特定资源冲击负、政府与商人的受益分配不同。葡萄牙是检验简单“军费过度延伸”模型不充分性的强反例。

## A 科技和造船
- 15世纪葡萄牙远洋导航、船舶技术、贸易据点网络使其接入既有印度洋商路；跨国知识传播与竞争必须关注荷英技术追赶，不能假设只有葡萄牙掌握核心技术。
- 工业化前后必须分开观察本土纺织制造与来自英国的毛纺产品。葡萄牙并非先靠本土机械纺织品全球出口的主力典型案例。

## B 奴役劳动、糖业与黄金
- 巴西种植园经济与跨大西洋被奴役非洲人口贸易密切相关。18世纪巴西黄金开采也大量依赖强制劳动。**这些不同劳动机制和西属安第斯mita制度不应混合**。
- 早期巴西糖业、17世纪后期至18世纪黄金的商品结构转换，是国库、出口和外部支付能力的关键变化。

## C 外交与战争
- 1580—1640葡萄牙在伊比利亚联盟共享西班牙国王；1640复辟战争、与荷兰海外据点争夺显著增加其风险。
- 与英国的1703商业安排和后续战略联盟不只是英国恶意干预的结果；[英国国家陆军博物馆](https://www.nam.ac.uk/explore/seven-years-war)记载1762葡萄牙遭西班牙入侵时英国出兵协助。
- **反例**：葡萄牙与英国经济关系密切并且得到英国军事支持，却仍未率先工业化；要研究贸易依赖、技术结构及资源诅咒，而不是“英国全面摧毁葡萄牙”。

## D 财政和货币
- [Costa等 (2024)](https://academic.oup.com/ereh/article/28/4/453/7667247)半世纪重建：葡萄牙1500—1549中央收入/GDP **含帝国2.0%、不含0.8%**；1700—1749 **5.2%与4.1%**。帝国政府收入占比和私人金银流入完全不同。
- [Kedrosky–Palma (2025)](https://www.cambridge.org/core/journals/journal-of-economic-history/article/cross-of-gold-brazilian-treasure-and-the-decline-of-portugal/B98AA5BDD404B56014FAAAD1861DC427)还引用英葡贸易数据：葡萄牙自英国进口在1699—1702每年约£355,000、1756—1760约£1,300,000；不能由名义进口额增加直接推断英国取得了同等净利润。

## E 本土制造和退出
- 黄金财富冲击可能抬升非贸易品价格、工资和实际汇率，挤出制造业；这种衰落机制可以在**帝国贸易持续贡献收入时**发生。
- 1807拿破仑入侵、王室迁移巴西和1822巴西独立属于不同事件；不能将葡萄牙帝国简化为1800年突然消失。

## 两条可证伪的竞争解释
- **H1 军费与殖民维持成本**：`government_colonial_net_transfers - defense_and_debt_service`逐时期变差。
- **H2 资源诅咒与制造业挤出**：巴西黄金到岸相对冲击对`nontradables_price`, `real_exchange_rate`, `manufacturing_exports`的作用，沿用合成控制并尝试事件研究。若H2较强，即使H1不成立，经济相对衰落也可能发生。
- **反事实问题**：失去直接统治仍可继续贸易，不能把所有英葡贸易成本都自动归咎于殖民维持成本。

**现有成果**：[13条事件](events_m0.csv)、[9项来源](source_registry_m0.csv)、[8条有来源的发表数值](metrics_m0.csv)，原始年度因果复算`NOT_RUN`。

**下一项唯一工作：** 分别重建1690—1800黄金输出、葡萄牙制造业/出口/价格和中央国库收支三套数据，以论文原始模型与工业制造部门反证检查2025约-40%的估计稳健性和2015贸易正贡献并存机制。

## 深入机制审查

- [巴西黄金、荷兰病与葡萄牙制造业：2025开放获取原论文的数值、因果链和金融边界](DUTCH_DISEASE_GOLD_TO_MANUFACTURING_V1.md)。其中区分价格/实际汇率的实证机制、王室政治资源诅咒假说，与尚未验证的主权金融危机。


## M2｜作者2019 Excel 数据审计：可复算衍生CSV和1700年源数据冲突

- [data_m2/README.md](data_m2/README.md)：原始数据授权边界、来源哈希、字段定义、已有结果与下一步
- [data_m2/gdp_benchmarks_m2.csv](data_m2/gdp_benchmarks_m2.csv)：14个关键年份、2025论文Table 1对照
- [data_m2/gdp_decadal_aggregates_m2.csv](data_m2/gdp_decadal_aggregates_m2.csv)：34组十年历史GDP/人口/CPI描述性汇总
- [data_m2/gdp_window_changes_m2.csv](data_m2/gdp_window_changes_m2.csv)：9组GDP/人口变化；[gdp_rolling_sensitivity_m2.csv](data_m2/gdp_rolling_sensitivity_m2.csv)：4种平滑
- [data_m2/gdp_source_variable_dictionary_m2.csv](data_m2/gdp_source_variable_dictionary_m2.csv)：13个Excel字段与统计口径
- [data_m2/gdp_source_manifest_m2.json](data_m2/gdp_source_manifest_m2.json)、[数据复算脚本](data_m2/reproduce_gdp_from_author_xlsx.py)：来源和输出哈希、严格版本校验

**研究数字修正：** 2019作者公开工作簿1700年人均GDP=987.2048，而2025黄金论文Table 1展示830（同源1650年约830）。此前按后者计算的1700—1750年+65.30%存在来源冲突；作者工作簿重算为**+38.95%**，1750—1800年**−33.22%**。该冲突是论文描述表格与公开历史基础数据间的不一致，**尚不证明2025年ASCM实际模型输入有错误**。2025复现包未成功取得，黄金因果参数NOT_RUN，年度财政/军费/债息仍NOT_ACQUIRED。

原始作者Excel因**未确认完整再分发许可证**，不直接上传公开仓库。本目录存的是原创可复算程序、引用指针、重点年份和衍生汇总，保留Draft PR以待独立史料与因果复核。


## M2增量：2025黄金论文官方附录的原始表转录（2026-11-14）

- [官方35页附录审计：黄金公共/私人汇款、ASCM国家权重、价格数据覆盖率](OFFICIAL_SUPPLEMENT_GOLD_FLOW_ASCM_WEIGHTS_M2_20261114.md)
- [黄金五年公共/私人流量 B.1](data_m2/gold_remittances_fiveyear_b1_1720_1804_m2.csv) · [ASCM基准与剔除西荷权重 B.3/B.4](data_m2/ascm_donor_weights_b3_b4_m2.csv) · [11种商品价格覆盖率 B.5](data_m2/commodity_price_coverage_b5_m2.csv)
- 统计边界：黄金汇回额是**流量**，包含私人转移，不是殖民净财政收入；1720–1804的公共名义汇款/全部汇款为**22.12%**（本轮对B.1逐行求和，不是税收占GDP）；ASCM模型真正的1694年处理后结果及2025 Table1 1700年GDP冲突仍待原始输入核验。


## M2后续｜黄金汇回与名义GDP分母对接（2026-11-14）

- [GOLD_REMITTANCES_TO_GDP_BRIDGE_AND_DATA_ACCESS_AUDIT_M2_20261114.md](GOLD_REMITTANCES_TO_GDP_BRIDGE_AND_DATA_ACCESS_AUDIT_M2_20261114.md)：1720—1804年黄金私人/公共汇回与同期葡萄牙名义GDP的单位、窗口、原始数据和因果边界审计，并核实openICPSR于2026年8月退役及ICPSR新平台自动流量验证阻断。
- [gold_to_nominal_gdp_fiveyear_bridge_m2.csv](data_m2/gold_to_nominal_gdp_fiveyear_bridge_m2.csv)（17期已验证衍生CSV），[reproduce_gold_gdp_bridge_m2.py](data_m2/reproduce_gold_gdp_bridge_m2.py)（实际运行、锁定作者Excel SHA256的复算脚本）。
- **1720—1804年名义黄金汇回额／同期GDP累计总额约2.9298%，其中公共渠道0.6482%、私人2.2816%。** 这是跨研究年度口径对齐的*流量比率*，**不是殖民金矿GDP增量、公共税收净率或帝国净ROI**。严格2025 ASCM及财政年度表仍未获得，不得以此替代模型复算。
