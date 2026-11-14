# H09｜Del Valle ISD Chapter313 第1496号：真实州官方学区税惠报告、报告版本修订与县补助分离（2026-11-14）

> **直接从 Texas Comptroller 官方官网取回并用 SHA256 核对两个原始 School District Cost Data Report (CDR) XLSX，使用 Python 标准库解析，逐税年计算两种版本的 `Gross_Tax_Saving = Tax_Levy_Without_Limitation − Tax_Levy_With_Limitation`，所有行复算PASS。** 这是学区财产税估值限制下的税负差（毛额），**不是Travis County Chapter381拨付给Tesla的现金grant，更不是净已实现可自由支配资金**。

## 项目与一手资料
- [Texas Comptroller 项目#1496（Tesla Inc / Colorado River Project LLC）官方档案](https://comptroller.texas.gov/economy/development/prop-tax/ch313/agreement-docs-details.php?id=1496)，**Del Valle Independent School District, Chapter 313**，和另一个[Travis County 2020经济发展协议 Chapter381 #0005328](https://comptroller.texas.gov/economy/development/search-tools/ch380-381/economic-development-agreements-details.php?agreement=0005328)分成**两个政策项目/现金核算对象**。
- [2023报告年度的CDR原始Excel](https://assets.comptroller.texas.gov/dat/ch313/1496/01496-CDR-2023-1016.xlsx)，Texas Comptroller官网**2026-02-06 posted**，字节10595，SHA256 `f076ff7810b24d141b33b0fe49bddbc7c47bf02402119bdfd0d75165b4b3b12c`。
- [2025报告年度的CDR原始Excel](https://assets.comptroller.texas.gov/dat/ch313/1496/01496-CDR-2025-1014.xlsx)，官网**2026-10-14 posted**，字节10582，SHA256 `a0d3dcc7a071bd8400081a427acb78887bacad9cf8cd1d69ed96a5026556a432`；这份资料**在2026-11中期选举之前**已经公开，不能当作2027政治变化的产物。
- 官方 XLSX 表头包括`Tax_Year`、`Tax_Levy_Without_Limitation`、`Tax_Levy_With_Limitation`、`Gross_Tax_Saving`、`Revenue_Protection`、`Supplemental_Payments`等。所有后两项是**另列的学区补偿/附加支付科目**，未给出完整净现金归属前不得随意减总额或与县级补助求和。

## 2025报告年度的主要数字

| Tax Year | 原表 Gross Tax Saving（USD） | Revenue Protection（USD） | Supplemental Payments（USD） | 截至报告时的性质 |
|---|---:|---:|---:|---|
| 2022 | **8,285,753** | 8,544,355 | 999,609 | 报告中列出的历史税年数字，不是本研究独立审计现金 |
| 2023 | **22,996,432** | 16,947,002 | 999,609 | 历史税年报告数字 |
| 2024 | **43,496,033** | 21,026,358 | 999,609 | 历史税年报告数字 |
| 2025 | **42,608,055** | 4,839,845 | 999,609 | 2025报告年度的当前税年数字，尚非独立实付凭证 |
| 2026 | **38,297,737** | 0 | 999,609 | **未来税年预测**，不可当2026实际税惠或付款 |

### 不要混淆毛税收节省与净企业现金收益
2024税年官方表列`Tax_Levy_Without_Limitation=65,816,557`美元、`Tax_Levy_With_Limitation=22,320,524`美元，两者相减为毛税收节省**43,496,033美元**。2025税年的相应值为`66,085,963−23,477,908 =42,608,055`美元。它们是同一个**估值限制模型**下的毛税负差，并非Travis县另行向项目法人实际拨付的补助。学区`Revenue Protection`和`Supplemental Payments`等条款可能影响项目净经济效益，必须结合实际付款及合同条款建立**独立学校项目净流量表**，不能因为毛数很大就直接推算Tesla集团利润多了相同金额。

## 关键来源版本差（不能忽略的PIT问题）

| Tax Year | 2023报告版本的毛税收节省 | 2025报告版本的毛税收节省 | 同一税年的版本差 | 2025相对旧版 |
|---|---:|---:|---:|---:|
| 2022 | 8,285,753 | 8,285,753 | 0 | 0% |
| 2023 | 22,996,432 | 22,996,432 | 0 | 0% |
| **2024** | **20,642,965** | **43,496,033** | **+22,853,068** | **+110.706%** |
| **2025** | **18,524,844** | **42,608,055** | **+24,083,211** | **+130.005%** |
| 2026 | 16,618,536 | 38,297,737 | +21,679,201 | +130.452% |

注意：**2023报告版本里的2024、2025、2026是当时对未来税年的预计值**，2025报告版本则将2024和2025作为回顾/当期税年记录。这种差异首先应当解释为不同时间的信息集/评估和报告口径更新，**没有证据证明是政府因党派变化临时扩张或削减补贴**；不能把旧版未来预测与新版历史报告等同于一场“新增优惠政策”。即使当前税年显示Gross Tax Saving，也不能未经纳税/补偿/合同实付核查视为最终企业所得。

按2025报告版本，**2022—2024**税年毛节省之和 **74,778,218美元**；若包含**2025报告当前税年**，2022—2025为 **117,386,273美元**。该累计数字**仅为报告内不同税年的毛税差**，不是已回流现金，也不是Travis县Ch381的现金补助。和[县2022官方零支付/2025新闻仍未发款的历史状态](2026-11-14_h09_county_official_2022_zero_rebates_baseline.md)并不矛盾，因为**法律主体/税种/支付方式不同**。

## 实证结论/反证
- **证实了一条具有量化规模的独立优惠渠道**：Del Valle ISD 的Chapter313估值限制有成体系的官方年度报告，而且不同报告时点金额变化很大。这直接否定“Travis县grant未发=Tesla在Texas没有任何实际税负减免”的过度推断。
- **没有证实**该税惠于2027新德州政府/国会时期被撤回、也未验证税负差最终净进入上市公司现金流；因已有2026-10-14公开的2025报告，至少不能把其2022—2025毛额归因于2026-11之后的新政策。
- 对比任何新政治冲击，应分别冻结2026-11-02以前**同一项目、同一税年、同一报告版本**的优惠基准、学区补偿义务、实际税单、资产估值，再观察新政策的正式生效及公司财务变化。
- H09完整`2027政治变化→该优惠正式调整→Tesla净现金流或投资增量冲击`仍`UNTESTED`。**Travis County Ch381 grant截至2026-11的实付和扣款USD仍未拿到，且不能从此学校CDR推算。**

## 复算与机器化数据
- [两版报告同税年14行对比CSV](../cases/musk-2026/delvalle_ch313_1496_2023_vs_2025_vintages.csv)；每行含报表posted date、税年、毛额、学区Revenue Protection/Supplemental Payments、原件SHA、历史/报告当前/未来预测标记和项目法域。
- [纯Python stdlib官方XLSX直接抓取/SHA/OOXML解析/税负恒等式及版本差复算](../analysis/recompute_h09_delvalle_1496_ch313_vintages.py)：Ubuntu MCP实际在当前分支上运行，校验结果 **PASS**。项目#1496两份源报告XLSX没有复制进公开仓库，只保留官方URL、SHA和必要数据表。
- **下一轮应取**：Ch313年度纳税单/学区现金补偿/已支付Supplemental Payments与收入保护实付，分清`gross tax difference`和`net benefit`；Travis County Chapter381继续向县Auditor/PBO取原始付款流水，不从学区资料替代。
