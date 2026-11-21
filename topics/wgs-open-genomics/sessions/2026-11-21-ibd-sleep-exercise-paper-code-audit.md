# 2026-11-21｜TOPIC-017 G6：现代 IBD、睡眠与运动表型论文×源码输入审计

- **规范身份**：[AI_book Issue #72](https://github.com/fweiger/AI_book/issues/72)、[Draft PR #73](https://github.com/fweiger/AI_book/pull/73)、锁定 `AI_tasks@f0e5ccb90c54265dcd07abb9a975c903eb031ccf`，同一 `GOAL_TRACKER.md`。
- **原目标对应**：沿“WGS 质量 → 权威论文 → 可研究深度 → GitHub 可复用实现”核查此前未深入的 D05 常染色体 IBD、D11 睡眠、D13 运动。
- **已回读一手材料**：[hap-IBD 原论文](https://doi.org/10.1016/j.ajhg.2020.02.010)、[hap-IBD README](https://github.com/browning-lab/hap-ibd)、[PLINK2 README](https://github.com/chrchang/plink-ng)、[pgsc_calc README](https://github.com/PGScatalog/pgsc_calc)；[晨晚型 2019](https://doi.org/10.1038/s41467-018-08259-7)、[时长 2019](https://doi.org/10.1038/s41467-019-08917-4)、[睡眠 PRS 芬兰 2023](https://doi.org/10.3390/clockssleep5010002)、[活动行为 GWAS 2022](https://doi.org/10.1038/s41588-022-01165-1)、[HERITAGE 2011](https://doi.org/10.1152/japplphysiol.00973.2010)、[Predict-HIIT 2021](https://doi.org/10.1186/s12929-021-00733-7)。来自 PubMed/期刊页面/开放论文部分方法正文及官方 README；**未逐篇全文系统评价**。
- **实质交付**：[G6 研究审计](../cross-domain-evidence-audit-g6.md)；[主矩阵](../evidence-capability-matrix.md) D05/D11/D13 重新按真实输入和证据层级分类；[论文注册](../paper-register.md) 新增 P037–P041。**当前去重范围 41 篇论文/指南、39 个 GitHub 源码候选、15 域**，不是全行业覆盖。
- **真实发现**：hap-IBD 的人际 IBD 必须具备至少两份合法样本、phased GT、无缺失等位和匹配参考的遗传图谱；单人 HBD/ROH 不等于找到近亲。2019 chronotype GWAS 697828 / 351 loci，25min 为两端人群平均值；2019 sleep duration GWAS 446118/78 loci，芬兰 33493 sleep PRS 有特定人群转移边界。2022 身体活动 GWAS 至多 703901 人/99 loci **研究活动习惯而非运动训练效果**；HERITAGE 473 人 21 SNP 49% 为研究样本内拟合，独立预测能力不足。
- **源码/许可**：hap-IBD Apache-2.0、PLINK2 GPLv3、pgsc_calc Apache-2.0 已核官方 README；pgsc_calc 不原生兼容普通 WGS variants-only VCF。因已有合适通用工具，本轮**没有新增 GitHub 仓库**，避免为追求数量造成无谓维护。
- **负证据与边界**：单人无法做人际 IBD；睡眠 PGS 不能准确预测个人作息；HERITAGE 样本内 R² 不能作外部验证，活动 GWAS ≠ 训练处方；欧洲/芬兰训练人群结果不能自动外推东亚消费者。
- **状态**：E0 GitHub 源码/输入/许可核查 PASS；E1 原文与代表设计 PARTIAL；**E2 实际 DNA 运行 NOT_RUN**；D0 ALIGNED/状态与规范任务一致；无个人 DNA、没有修改 Goal/Scope/AC 或建新任务。
- **下一研究候选**：按 15 域完成度做交叉一致性审计，优先重新检验 D01 WGS 质量、D15 非 WGS 直接组学边界，以及 P-ID/工具/论文输入的数据质量；公开样本实证仍待可用环境。
