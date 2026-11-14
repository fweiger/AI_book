# CASE-PRT-001｜M2 1720—1804年黄金汇款与葡萄牙名义GDP匹配：描述性证据及ICPSR 2026迁移审计

> 2026-11-14；权威 Issue：https://github.com/fweiger/AI_book/issues/34；Draft PR：https://github.com/fweiger/AI_book/pull/38  
> 状态：**17_PERIOD_GOLD_GDP_BRIDGE_PASS / REPRODUCER_EXACT_HASH_PASS / CAUSAL_ASCM_NOT_RUN / ICPSR_MIGRATED_ACCESS_BLOCKED**。以下全部是历史重建的*描述性比值*，不是新的因果资源诅咒估计、国库税收占GDP或殖民净投资回报率。

## 1. 研究问题与数据主体

上轮已从2025 JEH官方在线附录表B.1转录1720–1804年17个五年窗口的葡萄牙黄金汇回额，分公共/私人，按名义/1720不变价。原表单位为**百万 réis**，不是英镑、黄金质量或每年税收。对应文件：[gold_remittances_fiveyear_b1_1720_1804_m2.csv](data_m2/gold_remittances_fiveyear_b1_1720_1804_m2.csv)。

这次实际从作者**2019原始Excel** `palmareis_JEH_2019.xlsx`（83,313 bytes，SHA-256=`ee80439059ebfa3f67f870430671098fe6c853000be64d2605111285ee63045c`）的工作表`GDPs` **H列**读取1527–1850年葡萄牙各年*名义GDP，单位同样为百万 réis*。2019作者工作簿公开链接：https://drive.google.com/file/d/17M1nrjx-6B7fIMJGNTJ6tle6TtWNkLA7/view；文章：https://doi.org/10.1017/S0022050719000056。

黄金依据：Kedrosky & Palma (2025) Supplement B.1，官方PDF第31页：https://static.cambridge.org/content/id/urn%3Acambridge.org%3Aid%3Aarticle%3AS0022050725100764/resource/name/S0022050725100764sup001.pdf，原始PDF SHA-256=`6209adcdc8628d8be011e74838f6e156987bebd4b684f083691dce007b115aac`；论文：https://doi.org/10.1017/S0022050725100764。

文件为两项已公开研究数据的跨表对接，**不能将二者误报为互相独立的原始档案证据**；2025附录B.1的实际金额来源于更早的Costa等历史整理，并不是2025作者新发现的黄金运输账簿。

## 2. 可重复计算公式与输出

对于每个五年窗 `W=[t,t+4]`：

- `G_W = SUM_{y∈W}(nominal GDP_y million réis)`，直接来自2019作者Excel `GDPs!H`。这是五个年度名义GDP总和，不是五年平均GDP。
- `Gold_W = Private_W + Public_W`，来自2025出版附录B.1的**五年汇回流量**（百万 réis）。
- `I_W = 100 × Gold_W / G_W`，`I_W^public = 100 × Public_W / G_W`。
- `pcGDP_W = arithmetic mean_{y∈W}(real GDP per capita_y)`，作者Excel `GDPs!B`，**不作人口加权**。
- 全期总比率 `I_1720:1804 = 100 × Σ_W Gold_W / Σ_W G_W`，**GDP加权的分组汇总**而不是17个比率的简单平均。

新增 [gold_to_nominal_gdp_fiveyear_bridge_m2.csv](data_m2/gold_to_nominal_gdp_fiveyear_bridge_m2.csv) 含17个完整五年期间，包含同期名义GDP分母、公开汇款额、公共/私人强度、人均GDP窗口均值以及数据来源字段。

新增 [reproduce_gold_gdp_bridge_m2.py](data_m2/reproduce_gold_gdp_bridge_m2.py) 用 Python 标准库从**用户另行下载**的2019作者Excel与本目录公开B.1 CSV计算并重建上述17行：

```bash
python3 reproduce_gold_gdp_bridge_m2.py \
  --source /local/path/palmareis_JEH_2019.xlsx \
  --gold-file gold_remittances_fiveyear_b1_1720_1804_m2.csv \
  --output /tmp/gold_bridge.csv
```

该脚本复用同目录 [reproduce_gdp_from_author_xlsx.py](data_m2/reproduce_gdp_from_author_xlsx.py) 的严格读取函数与作者工作簿SHA锁，拒绝意外输入版本；检查324年连续范围、17个五年窗口连续性、私人+公共与合计的一致性、名义GDP计量尺度和总汇回金额校验。

## 3. 实际运行的描述性结果

| 1720–1804年85年累计名义量 | 百万 réis | 该流量／同期名义GDP总额 |
|---|---:|---:|
| 葡萄牙名义GDP年值累计 | 9,251,397.552 | 100%（分母） |
| 巴西黄金私人名义汇回额 | 211,080 | **2.2816%** |
| 巴西黄金公共名义汇回额 | 59,965 | **0.6482%** |
| 巴西黄金总名义汇回额 | **271,045** | **2.9298%** |

注意：**黄金转移支付流量不等于葡萄牙新增价值创造**，不能将总流量占同期GDP的2.93%理解为“黄金占GDP贡献率”；更不能将0.6482%公共汇回强度解释成葡萄牙国库净税收率。

### 三个可比历史窗口

| 年份范围 | 黄金总汇回／同期GDP | 公共汇回／同期GDP | 公共汇回／同期黄金汇回 |
|---|---:|---:|---:|
| 1720–1749（30年） | 5.1121% | 1.0090% | 19.7370% |
| 1750–1779（30年） | 3.5259% | 0.8420% | 23.8805% |
| 1780–1804（25年） | 0.6636% | 0.1849% | 27.8628% |

最后一段仅25年，所以原始黄金**绝对合计不能直接与30年对照**；这里用每期黄金累计值除以同期GDP累计值，分母已匹配同一个日期窗口。

两个高低值对比：
- **1740–1744**：总黄金汇回29,456百万 réis；当期名义GDP累计463,777.040185百万 réis；相对强度 **6.3513%**；人均GDP五年均值≈1,267.145（1990 GK国际元）。
- **1790–1794**：总黄金汇回1,310百万 réis；名义GDP累计669,423.428327百万 réis；相对强度 **0.1957%**；人均GDP五年均值≈1,106.864。
- 1740–1744与1790–1794的黄金汇回强度从6.3513%降至0.1957%（按比率衡量约**−96.92%**）。这不是“黄金产量跌96.92%”，也不是“财政收入下降96.92%”。

### 非单调时间变化及与产业损伤的时间顺序

- **1780–1784**黄金相对GDP强度1.1827%，人均GDP≈1,238.80；
- **1785–1789**黄金相对GDP强度0.2532%，人均GDP≈1,243.61（小幅回升）；
- **1790–1794**黄金强度0.1957%，人均GDP≈1,106.86；
- **1800–1804**黄金强度0.9698%，人均GDP≈899.44。

因此，黄金汇回显著缩减与葡萄牙人均GDP下行并非每期即时一对一对应。**这与已经失去制造业学习机会的长期滞后假说相容，却同样允许战争、制度、市场及冲击后的其他解释**。不能仅以滞后叙述补足未识别的因果链。

## 4. 关联强度的负面控制：时间趋势一加入，表面相关显著减弱

作为诊断而**非显著性证明**，以17个不重叠五年期的 `Gold_W/GDP_W` 与 `pcGDP_W` 进行简单Pearson相关：
- **全17期：r≈+0.5596**；
- 去掉末尾3个五年期（只保留1720–1789年14期）：**r≈+0.2031**；
- 分别对两条序列先线性回归5年期编号，再对其残差计算相关：**r≈+0.2891**。

相关系数对样本期和时间趋势非常敏感。17期数据存在强烈序列相关、持续性国别宏观趋势和共同冲击；**不把简单Pearson的经典t检验p值当作因果证据，也不据正相关推翻作者相对于未获黄金合成反事实的长期资源诅咒推断**。2025论文的核心估计必须通过1694处理点的可复现ASCM模型来评价。

## 5. 2026年ICPSR迁移与访问问题的实证记录

本轮核实权威ICPSR公告：旧 openICPSR.org 服务**已于2026年8月退役**，历史公开研究迁入ICPSR新站；JEH的旧数据入口不再是稳定下载方式。官方介绍：https://www.icpsr.umich.edu/sites/icpsr/openicpsr-has-moved

2025论文的正式包归档编号仍是**ICPSR 209481**，首发标识 `https://doi.org/10.3886/E209481V1`。ICPSR搜索结果显示其为self-published/public，发布日2024-10-04；作者本人公开论文清单提供Replication package链接：https://sites.google.com/site/npgpalma/publications。

本轮网络诊断发现：
- `https://www.icpsr.umich.edu/sites/jeh/view/studies/209481`、加`/versions/V1`、及`/sites/icpsr/view/studies/209481`：**HTTP 403，响应页标题为 `Just a moment...`（网站自动流量验证）**；
- 原 `https://www.openicpsr.org/openicpsr/project/209481/version/V1/download` 和`/download`：也返回**HTTP 403**；
- `https://www.icpsr.umich.edu/sites/search/studies?q=209481`：**HTTP 200**，只能确认公共目录可访问，不是证明下载了复现文件；
- **实际ZIP、代码、模型输入、README清单均未获得**。在没有新平台真实可获取文件之前，不能虚构ASCM执行记录或断言作者2025 Table1 1700=830被用于回归。2019作者原表同年≈987.20的展示冲突仍为 `SOURCE_CONFLICT_OPEN`。

可执行后续：通过新ICPSR JEH专题研究页面的合法公开下载按钮、研究者本人正式页面或联系归档人员取得209481最新发布版本及文件清单，记录版本、SHA256、许可，再复现模型及对照权重。旧 openICPSR 下载脚本是**旧站流程**，不能保证适配2026新平台；对反机器人挑战不做规避性操作。

## 6. 计量/会计红队边界与结论

1. **单位**：`réis`不是`real GDP 1990 GK dollars`。本桥接选择同为名义**百万 réis**的公开黄金汇回和2019作者Excel `GDPs!H`，未使用真实GDP/人均GDP作为分母。
2. **窗口**：黄金是五年期流量；分母必须为匹配五个年份名义GDP之和，不能使用单个年份GDP或平均GDP造成五倍错误。
3. **统计范围**：公开表B.1记载的是经过历史来源整理的私人及公共汇回，可能漏记走私、未记渠道及以其他形态转移的收益，**不等同巴西全矿产、全殖民贸易规模**。
4. **GDP历史重建风险**：2019年名义GDP来自间接历史测量；黄金表B.1用早期资料整理，两者可检验货币和时间单位，但**并非完全独立的现代国民账户调查**。
5. **殖民财政净额未识别**：缺少王室收入分项、巴西征税、官员薪饷、航运保险、债务成本、军费等，不能计算帝国财政净ROI；公共汇回也不能全部视为可支配税收。
6. **因果识别**：本次是descriptional matching，不使用处理组/对照组、工具变量或动态预趋势的反事实识别。对1694黄金ASCM的−40%估计的严格结论仍是 `NOT_RUN`。
7. **版本合规**：源作者XLSX引用其公开链接并使用哈希锁，未复制到公开repo；作者2025官方完整PDF未镜像。提交仅为本研究的原创程序、对接汇总与有出处的短数据转录。

### 验证

- 实际从83,313字节2019作者Excel与官方17期黄金短表，运行`reproduce_gold_gdp_bridge_m2.py`：**PASS**，`ROWS=17`，`GDP_85Y=9,251,397.551606`百万réis，三个累计比率=2.929774%、0.648172%、2.281601%。
- 独立计算与脚本输出CSV**字节完全一致**，输出文件SHA-256=`bbf1d77cbe014f22ed5d0ffbf1bd311cad253ee956911e83266ca12d62f3b162`；脚本SHA-256=`ccd49e95c5d25b1f51884f38cb772e6eca901ee0d81e6b83e06d4b738038a157`。
- GitHub新文件回读确认两个文件Git blob SHA与经本地运行校验的精确文件字节相同（脚本`f774c2b037b7bebf99dad8918a907c484357bd48`，CSV`f611053cf104ba0c202e3e35c320634331799913`）。
- 本轮未取得原始贸易品/非贸易品地区价格表、ICPSR复现包、财政年度全口径，均记 `NOT_ACQUIRED`；ASCM与净财政ROI `NOT_RUN`。

**下一唯一实证步骤**：合法取得新平台JEH 209481最新公开复现包，版本锁定后回答2025年回归程序1700年输入究竟用830还是987.20，并执行1694基准及排除Spain/Holland复算，含1755地震、1701—1714战争的敏感性审计。保持#34 OPEN，#38 Draft，main不合并。