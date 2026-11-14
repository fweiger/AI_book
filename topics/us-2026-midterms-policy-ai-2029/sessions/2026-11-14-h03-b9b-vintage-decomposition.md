# 2026-11-14｜H03第十轮：2025/2026两个原始B9/B9b分量变动

在北京Windows MCP通过已有代理直接下载两份PJM工作簿：2025原版 SHA a9a797f2d3cf34154db466b74e045d1334dfebede87ec6dc3739805093474ef5，2026当前可下载版SHA 59a62facf819962e430101c96dd1335229d8173fb6886dd8045ced325443f607。B9/B9b分别抽取RTO DOM AEP COMED PS PL的2026—2035目标，形成60行面板，报告及校验文件已落盘。

2026原版B9原文明确2026-02-06修正embedded计算错误，所以当前XLSX不能直接标记为2026-01-14首次公开同一数据版本。

RTO目标2027：2025 B9额外13668、B9b总17721（差4053）；2026B9额外10785、B9b总15856（差5071）。版本修订Δabove=-2883、Δembedded-related=+1018、Δtotal=-1865MW。DOM总+740,AEP-902,COMED+49,PS-197,PL-1134,OtherRTO-421，六区闭合。

目标2028/29总变化-2138/-2122，2030/35 +1755/+9555，说明近期与长期预测不同方向。

2026 accuracy retrospect RTO 2027=15866 vs当前原版B9b15856，相差10MW；各目标2026—31差10、2032—35差9，重要分区DOM/AEP/COMED/PS/PL全匹配。原因未确认，不能当现实负荷新增/删除。

研究只比较模型版本，不是物理实现或联邦政策因果。完整[报告](../reports/2026-11-14_h03_b9b_vintage_decomposition_2025_2026.md)、[60行数据](../data/h03_pjm_2025_2026_original_b9_b9b_revisions.csv)、[区级贡献](../data/h03_pjm_2027_original_zone_revision_contributions.csv)、[回顾差异](../data/h03_pjm_2026_original_vs_accuracy_rto.csv)及[复算脚本](../analysis/recompute_h03_b9b_vintage_decomposition.py)。

## 追加官方算法源核验
[PJM 2026-01-23 LAS第28页](https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2026/20260123/20260123-item-03---pjm-2026-long-term-load-forecast---presentation.pdf)证明对有DC历史的区域，建模先清除EIA商业和PJM小时历史里的DC再加总规划负荷；B9来自保留DC历史的敏感性模型与最终预测的差。这支持统计分解恒等式的解释，但不能把B9b−B9当客户真实表计，或从1/23演示推算2/6勘误MW。官方原文属于2026年中期选举前证据。
