# TOPIC-005 数据合同 v0：禁止伪造时间序列

## 输入表（每条一国一年一口径）

```text
country              GB / US
time_period          历史原始标记，如 FY1946/47、FY2026
period_end_date      YYYY-MM-DD，原始财政年度末
statistical_release  统计发布日期或版本号
source_org           来源机构
source_url           可直接核查的链接
debt_concept         gross_federal / publicly_held / PSND / general_gov_gross ...
government_coverage  central/federal/general/public_sector 等
net_or_gross         net / gross
debt_stock_currency  本币名义债务存量（缺失留空）
gdp_currency         口径匹配的名义GDP（缺失留空）
debt_to_gdp_pct      来源给出的比率或可明确重算比率
observation_type     actual / preliminary / forecast
reference_note       分母年、单位、重分类、舍入与断点说明
```

没有来源观测值的数据点不得以插值或模拟值充当历史事实；用于演示公式的计算必须明确标注**假设性情景**且参数有来源或由用户指定。

## 计算要求

1. 官方源连续时间序列先做口径审计（机构、net/gross、财政年度、占GDP的比率分母）。
2. 原始年份曲线和事件对齐比较必须分开展示，事件对齐必须公开所选原点以及何以有意义。
3. 债务率分解时：`b_t = ((1+i_t)/(1+g_t))*b_(t-1)-s_t+sf_t`。仅在数据定义与单位一致的前提下计算。
4. 真实增长、通胀、名义增长不得混称；债务利率采用按存量定义一致的有效名义利率。
5. 缺少初级余额、其他资产或汇率估值数据时，残差可以报告但不能自动解释为具体财政机制。
6. 对美国2026相关数值必须分别保留CBO公众持有债务与总联邦债务两条序列，不将101%和123%视为矛盾。
7. 所有成果记录数据下载时刻、文件哈希、代码版本及可复算结果；不上传无法授权的私人文件。

## 当前数据状态

仅已定位官方文字/表格线索，**未完成全量时间序列下载、计算、回测或统计检验**。不能输出伪造的债务分解百分比。
