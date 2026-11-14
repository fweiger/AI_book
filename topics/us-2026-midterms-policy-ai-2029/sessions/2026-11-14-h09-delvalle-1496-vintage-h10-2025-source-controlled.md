# TOPIC-011｜2026-11-14 H09学区Chapter313真实版本税惠量纲与H10同源2025 CPI方向反证

## 沿原研究主线的目的
延续视频专家观点与2027—2029美国政治机制研究，不再纠结空想政商动机，而是补上H09真正有数字的**另一种德州税惠机制**，以及H10跨年混源回测核心6/7同向的**严格同源敏感性验证**。所有新事实/统计和既有内容均在未合并的PR #51研究分支，不覆盖并行H01/H03。

## H09一手资料与真实复算
直接从[Texas Comptroller Del Valle ISD Chapter313 #1496官方档案](https://comptroller.texas.gov/economy/development/prop-tax/ch313/agreement-docs-details.php?id=1496)下载两份XLSX原表：
- Reporting Year2023 CDR URL [01496-CDR-2023-1016.xlsx](https://assets.comptroller.texas.gov/dat/ch313/1496/01496-CDR-2023-1016.xlsx)，官网**2026-02-06 posted**，10595 bytes SHA`f076ff7810b24d141b33b0fe49bddbc7c47bf02402119bdfd0d75165b4b3b12c`。
- Reporting Year2025 CDR URL [01496-CDR-2025-1014.xlsx](https://assets.comptroller.texas.gov/dat/ch313/1496/01496-CDR-2025-1014.xlsx)，官网**2026-10-14 posted**，10582 bytes SHA`a0d3dcc7a071bd8400081a427acb78887bacad9cf8cd1d69ed96a5026556a432`。官网公开日都在2026-11中选以前。
- Python标准库`zipfile+ElementTree`解析CDR税年表；直接验证`Gross_Tax_Saving = Tax_Levy_Without_Limitation - Tax_Levy_With_Limitation`。2025报告版税年2022 8285753、2023 22996432、2024 43496033、2025 42608055（USD毛税负差），2022—24合计74778218 USD，2022—25含报告年为117386273 USD。2024原2023报告**预测20642965**→后2025报告历史列**43496033**，差22853068 USD；2025税年2023预估18524844→2025报告税年42608055，差24083211 USD，均**来源版本变化不等同新增政治政策或现金回流**。2025 CDR另有学区`Revenue_Protection`2024 21026358与2025 4839845及`Supplemental_Payments`各999609，不能不核实际义务就称净省多少钱。
- **坚决区分** Del Valle ISD学区Chapter313税基限制的`gross`税负差与Travis County Chapter381经济发展grant的`approved/paid/withheld/recaptured USD`。县实际现金依旧未得到，不能拿Del Valle数值填写县2020—22那9%扣留基数。
- [真实14行税年×报告vintage CSV](../cases/musk-2026/delvalle_ch313_1496_2023_vs_2025_vintages.csv)、[官方原件直取独立复算脚本](../analysis/recompute_h09_delvalle_1496_ch313_vintages.py)、[完整来源版本与税种隔离报告](../reports/2026-11-14_h09_delvalle_ch313_official_tax_saving_vintage_comparison.md)。Ubuntu MCP从GitHub取脚本后独立下载两官方原表运行`PASS`。

## H10 事前同源样本构建与可证伪结果
- 固定BLS**2025年全部11次实际CPI发布**作为事前候选总体，只有7次找到了同一家[Calculated Risk博客](https://www.calculatedriskblog.com/)的明确提前发布市场共识（2025年Jan14、Feb11、Mar11、Jun10、Jul14、Aug10、Sep09）。Apr10/May13/Oct24/Dec18保留缺失，**不借其它供应商网页回填**。官网文章带发布时日期但当前正文未另有不可变原始WARC快照，因此仍标来源版本剩余风险。
- 每个事件以该文明确记录的`headline/core CPI SA MoM consensus`减BLS当月**首次发布**的实际值，配官方Treasury从前个真实交易日至当日日收益率有符号bp。核心7期中surprise非零4次，两年期方向四期都非零，**仅2/4同向**；headline非零5次，**仅2/5同向**；两者双侧精确二项p均**1.0**。反例：2025-Jan15 headline较预期+0.1pp但2Y **-10bp**；Mar12 core较预期-0.1pp但2Y**+7bp**；Jul15 core意外-0.1但2Y**+5bp**。
- 和此前[2023—26跨机构便利10次样本](../reports/2026-11-14_h10_pre_release_forecasts_10_pit_vs_vendor_not_pit.md)核心6/7同向/p0.125构成**强烈选择偏差/不同时期敏感性检验**。此处对同一发布者只覆盖7/11，依旧小样本和**全天债券收益率并非CPI-only高频冲击**，不能得出二项研究否证Fed对CPI有因果响应；仅不支持把6/7当可交易的确定预测胜率。
- [全11期源级与空缺的2025固定队列](../data/h10_cpi_consistent_publisher_2025_pre_release_cohort.csv)、[标准库可复算脚本](../analysis/recompute_h10_2025_consistent_publisher_cpi_direction.py)及[详细说明](../reports/2026-11-14_h10_2025_uniform_publisher_cpi_surprise_direction_falsification.md)。Ubuntu真实读取Github当前代码与CSV`--stdin-csv`运行 **PASS**。

## 登记/下一轮
- 正式原始数据事件追加E112—E115（两份一手学校CDR及衍生版本差、2025单一同源CPI研究结果）；新增I层4个量：学校税年毛额、同税年报告版本差、学区收入保护项、同源核心CPI surprise对2Y方向指标；新增[VIEW-S001视频C04/C07/C09第7轮后验评估](../views/claim_reassessments_2026-11-14_round7.csv)不覆盖作者初始说法。
- 下一轮H09需要学区真实税单/收入保护实际支付和县Auditor真实grant现金；H10需要同一发布日期明确可追踪的专业共识**更全的2023—26所有月份、市场08:29和08:35的2Y/FF期货价格、同日其他公告控制**；没有前述材料就不解释真因果。旧H01–H10整体仍UNTESTED、不增加正式C-ID。
