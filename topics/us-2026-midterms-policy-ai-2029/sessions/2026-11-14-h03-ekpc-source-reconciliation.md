# 2026-11-14｜H03第十一轮：2026-01总量、2/6 B9、五月Accuracy EKPC来源差异闭合
北京、武汉MCP经已有代理取得PJM官方四工作簿（不在GitHub放原二进制），源SHA分别：
Jan14独立B9b `ee3b682929db0b59a043c8ab6d1c9776f697ab10fc86fe603a6d0d724893c4ba` 18904B，文件内部修改时间Jan13；
Feb6 corrected B9 standalone `990e2cb82d02a6c689a9e21b5c7ccb13944613f960dcc2f6eb3109e51a49d6a1` 19177B，文件内部修改时间Feb6；
2026 currently available combined B9/B9b `59a62facf819962e430101c96dd1335229d8173fb6886dd8045ced325443f607` 371564B，B9有Feb6 correction注释；
2026-May Accuracy `e0f24fe03a79af016826089c653b2c2e15e55edcb04a7bd4be5fa643136425fc` 50175B。

21年*23个一级区两对比较：唯一不一致zone EKPC和聚合RTO，两行各21个不同值。独立两附件EKPC=0、combined EKPC2026—31=-10、2032—37=-9、2038—46=-8，RTOStandalone−RTOCombined恰相反。5月Accuracy RTO整21年与JanB9b standalone完全一致。

另取得Jan14月度附件SHA d9e547…，工作表第2行明确不包括Peak Shaving Adjustments，官方PJM新闻确认EKPC为2023DY开始削峰，支持这种来源差异的解释，但无官方公告证明为何不同附件选不同PSA纳入方式。2025 PJM原报告第4页证明B9b表2025首次引入，故2023/24原版B9b并不存在。

2027原2025 B9b17721到Jan2026 standalone15866为−1855；到当前combo15856为−1865；Accuracy回顾2025v17726与2026v15866为−1860，均是预测版本，不是实物变化。2026-02-06以前B9未修订字节仍无从取得，不能计算勘误效应。

[正式报告](../reports/2026-11-14_h03_ekpc_jan_vs_feb_release_reconciliation.md)、[21年RTO+EKPC记录](../data/h03_pjm_2026_ekpc_source_reconciliation_2026_2046.csv)、[23区对照](../data/h03_pjm_2026_ekpc_zone_source_match_summary.csv)、[三种预测基线比较](../data/h03_pjm_2027_rto_baseline_publication_sensitivity.csv)、[原始来源清单](../data/h03_pjm_2026_jan_feb_publication_manifest.csv)、[复算脚本](../analysis/recompute_h03_ekpc_source_reconciliation.py)。
