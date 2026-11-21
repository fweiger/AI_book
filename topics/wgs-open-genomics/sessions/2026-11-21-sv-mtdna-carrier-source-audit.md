# 2026-11-21｜TOPIC-017 G5：SV、母系 mtDNA、遗传病携带者与许可审计

- **规范入口**：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)，[Draft PR #73](https://github.com/fweiger/AI_book/pull/73)，锁定 AI_tasks V1.2.2 commit `f0e5ccb90c54265dcd07abb9a975c903eb031ccf`。
- **目标**：从高质量个人 30–40× WGS 数据出发，审计 D02 结构变异/CNV/STR、D04 母系 mtDNA 和 D08 隐性携带者 3 个领域的论文实际数据、算法源码输入和最大可靠推断深度，不局限于父系。
- **公开一手论文**：[NIST GIAB 2020 SV](https://doi.org/10.1038/s41587-020-0538-8)、[Truvari 2022](https://doi.org/10.1186/s13059-022-02840-6)、[ExpansionHunter 2019](https://doi.org/10.1093/bioinformatics/btz431)、[MToolBox 2014](https://doi.org/10.1093/bioinformatics/btu483)、[gnomAD mtDNA 2022](https://doi.org/10.1101/gr.276013.121)、[mtDNA WGS vs targeted 2021](https://doi.org/10.1016/j.mito.2021.01.006)、[mtDNA caller benchmark 2022](https://doi.org/10.3389/fgene.2022.692257)、[ACMG carrier 2021](https://doi.org/10.1038/s41436-021-01203-z)、[ACMG 2024 technical standard](https://doi.org/10.1016/j.gim.2024.101137)、[InterVar 2017](https://doi.org/10.1016/j.ajhg.2017.01.004)、[2025 independent Gauchian negative study](https://doi.org/10.1038/s42003-025-08059-y)。
- **GitHub 直接核验**：Truvari、MToolBox、Mutserve、InterVar、Gauchian 5 个仓库真实存在；README/许可逐一读取。**MIT**：Truvari、Mutserve；**GPL-3.0**：MToolBox；**README 商业许可受限**：InterVar；**PolyForm Strict**：Gauchian，以及此前登记的 ExpansionHunter。源码存在不自动证明符合普通开放许可。
- **新发现与更正**：Truvari 是 SV VCF 对照/基准，不是 caller；GIAB 高可信 12,745 DEL/INS 不代表全部结构变异；Mutserve 的 VCF 不输出 indel；mtDNA 1% 调用阈值不是检出灵敏度；ACMG carrier 阴性有残余风险；复杂 GBA1 假基因位点的 Gauchian 漏报报告受到开发者正式回应的测试深度质疑（P036/P045）；只能记为**条件依赖的未独立解决争议**，不能直接泛化到所有 30× WGS。
- **研究交付**：[G5 三域详细审计](../cross-domain-evidence-audit-g5.md)、[更新后的 15 域主矩阵](../evidence-capability-matrix.md)、[P001-P036 论文注册表](../paper-register.md)、[T01-T39 源码与许可证目录](../open-source-projects.md)。
- **计数口径**：当前总计 **36 篇已登记 DOI/指南**、**39 个 GitHub 源码候选**、原 15 个研究域。不能说 39 项全部可自由复用、不能说 36 是全世界相关论文总数。
- **验证状态**：G5 项目存在/许可来源核查 PASS；部分直接论文方法与数据设计 E1/PARTIAL；所有 WGS 实际计算、公开真值基准及临床准确率 E2+/NOT_RUN。
- **隐私**：AI_book 公开仓库没有私人 FASTQ/BAM/CRAM/VCF 或亲属身份。
- **下一步候选**：横向填 D05 常染色体 IBD、D11 睡眠、D13 运动复杂性状的学术论文/源码/研究深度空缺。GitHub 状态与 Tracker 以本轮事件回读为准。
