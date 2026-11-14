# H09｜Del Valle ISD的Tesla Chapter313替代税款PILOT实收记录与CDR税年对账（2026-11-14）

## 核心实证突破

这轮已从Texas Comptroller的“税负有/无限制毛额预测”进一步找到学区正式财务报告中的Tesla PILOT收款/收入。用Ubuntu MCP直接取回原始EMMA PDF，验证SHA256，并从Tesla Chapter313协议附注提取“received a PILOT”，从年度收入表读取比较数据。这里是学区收到/确认的相关收入，而非公司收到的补贴、银行单笔交易记录或最终企业净税负。

| 财政年度结束6月30日 | Tesla相关PILOT美元 | 原始依据 |
|---|---:|---|
| FY2022 | 999,609 | [学区FY2022官方AFR](https://emma.msrb.org/P11685898.pdf) Chapter313附注 |
| FY2023 | 9,543,964 | [FY2024学区AFR](https://emma.msrb.org/P21874726.pdf)上年收入比较列；FY2023自身AFR尚待独立核 |
| FY2024 | 17,946,611 | 同上FY2024当年收入表、Tesla协议附注 |
| FY2025 | 23,002,842 | [学区FY2025 AFR](https://emma.msrb.org/P31547867.pdf)当年收入表及Tesla协议附注 |
| **总计** | **51,493,026** | 四个不同财政年学区所报告的PILOT收入之和 |

学区[官网财务报表索引](https://www.dvisd.net/departments/business-office/forms)亦公开FY2022—25年度AFR。三份EMMA PDF原始SHA256依次为：
- FY2022：a4f60f7208a36affd9baed1f647a06d575ce7e44c4f9268e9db1f3dfaafcdd32
- FY2024：1671cbc7b922df1b6dad519bc2b56f8cef9857f97ba643874c1b99f9ee6b194b
- FY2025：dc5909585a8e84d06e60a669fa2cb9c1f331f745f98831b8bb5213afb84cffae

## 同Texas Comptroller Chapter313报告的跨期间候选核对

按学区财政年度FY(t)对照税年TaxYear(t−1)的独立Texas Comptroller [第1496号2025 School District Cost Data Report](https://assets.comptroller.texas.gov/dat/ch313/1496/01496-CDR-2025-1014.xlsx)（XLSX SHA a0d3dcc7a071bd8400081a427acb78887bacad9cf8cd1d69ed96a5026556a432）中Revenue Protection + Supplemental Payments。此配对属于有历史算术证据的**候选时钟关系**，没有税单/ACH号码时不能正式确定每笔付款的税年归属。

| 学区FY | 候选CDR TaxYear | 报告Revenue Protection | Supplemental | 合计 | 学区FY PILOT | 差额 |
|---|---|---:|---:|---:|---:|---:|
| 2022 | 2021 | 0 | 999,609 | 999,609 | 999,609 | 0 |
| 2023 | 2022 | 8,544,355 | 999,609 | 9,543,964 | 9,543,964 | 0 |
| 2024 | 2023 | 16,947,002 | 999,609 | 17,946,611 | 17,946,611 | 0 |
| **2025** | **2024** | **21,026,358** | **999,609** | **22,025,967** | **23,002,842** | **+976,875，未对平** |

前三个财政年完全匹配，是候选跨年映射的重要算术线索；但FY2025相差976,875美元，不能手工“补平”。可能原因包括税额评估、报告版本、补偿调整及会计期间差异，目前未取得证明任何一个原因的收款/税单明细。

注意：学区CDR报告税年2024 Gross Tax Saving为**43,496,033美元**，并另列收入保护**21,026,358**和补充支付**999,609**。这三项来自学校价值限制的不同毛额/合同义务，**并非同一个现金钱包**。FY2025 PILOT虽与其时间相邻，也不能直接用Gross Saving减去FY PILOT宣称已独立审核的企业净优惠。

## 两套完全不同的法律合约

- **Del Valle ISD School Chapter313 #1496**：Tesla项目学区M&O可税价值限制所带来的报告毛税差和企业向学区支付/学区记载收到的PILOT。2022—25财报四年收入合计51,493,026美元，不能当学区政府给企业的补助。
- **Travis County Chapter381 #0005328**：县政府与Colorado River Project LLC的另一项有条件经济发展grant，2026-04-07县委员已通过对2020—22合格grant的9%扣留决议；县实际已发/扣留/已发后追回美元仍未从Auditor账本取得。**禁止把学区2024税年毛差或FY2025 PILOT填进县的9%基数**。

## 对H09候选政治机制的影响及下一任务

这项真实报告否定了“因为Travis县还没发返利，所以Tesla在整个德州没有真实有规模的Chapter313履约资金”的泛化前提。学区历年确实记录了相关收入，学区税收优惠机制在中期选举以前持续运行；但**没有证据证明2027政治变化撤销了任何学区既有权利，也没有证明Tesla净现金利益等于毛税差**。

下一步应独立核FY2023原始财报、FY2025差额976,875美元的税单和学区账目、2026后新会计报表，同时继续找县Auditor项目grant已发/withheld/recaptured三类真实美元。正式H09政治→公司现金流因果仍UNTESTED。

## 复算资产

[官方PDF与CDR原始SHA/数值对账四行CSV](../cases/musk-2026/delvalle_school_afr_pilot_FY2022_2025_vs_ch313_cdr.csv)；
[Python源码：直接下载3份原始PDF和2025 CDR XLSX、计算SHA、提取财报注释/比较值并复算对账残差](../analysis/recompute_h09_delvalle_school_pilot_afr_reconciliation.py)，Ubuntu MCP实际执行PASS。本结果是年度报告层次，不是银行凭证逐笔确认。
