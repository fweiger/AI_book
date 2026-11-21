# TOPIC-017｜研究主张及证据状态
> 当前为初始证据整理，未有个人样本、无原始流程实测；编号稳定，不将待验证命题说成结论。

| C-ID | 主张 | 证据与链接 | 当前状态 | 最强限制/反例 |
|---|---|---|---|---|
| C017-001 | 人类单倍体参考基因组约 31 亿碱基；90 Gb 是累计测序碱基量，不是文件 GB | [GRCh38 参考信息](https://www.ncbi.nlm.nih.gov/grc/human/data?asm=GRCh38) | E1/技术定义 | 参考与可调用区域不同 |
| C017-002 | 公开 WGS 流程能产生 SNV/Indel 候选并进行 benchmark | [Sarek](https://github.com/nf-core/sarek)，[NIST GIAB](https://www.nist.gov/programs-projects/genome-bottle) | E0/E1；E2 NOT_RUN | 需特定平台/样本 QC |
| C017-003 | Y 单倍群可追溯特定父系分支，但不能单独证明名人直系后代 | [Yleaf](https://doi.org/10.1093/molbev/msy080)，[Y-LineageTracker](https://doi.org/10.1186/s12859-021-04057-z) | E1 | 演化树与姓氏族谱不是同一种证据 |
| C017-004 | 古 DNA 可以研究历史亲缘与群体关系，但共祖不等于直接先祖 | [ancIBD](https://doi.org/10.1038/s41588-023-01582-w) | E1 | 低覆盖、样本数和参考面板限制 |
| C017-005 | 疾病变异解释需 ACMG/AMP 和临床确证，单一 AI 注释不能诊断 | [ACMG/AMP 2015](https://doi.org/10.1038/gim.2015.30) | E1 | 变异外显率/环境/表型 |
| C017-006 | PRS 必须评估祖源迁移及独立验证；单人样本只能计算不能独立验证预测性能 | [PRS portability 2024](https://doi.org/10.1038/s41576-023-00637-2) | E1 | 未测量真实预测准确率 |
| C017-007 | 睡眠晨晚倾向具有 GWAS 遗传相关性，但不等于精确安排个人睡眠 | [Chronotype GWAS 2019](https://doi.org/10.1038/s41467-018-08259-7) | E1 | 环境/行为/其他因素 |
| C017-008 | 标准短读长 WGS 不会直接测量甲基化、RNA 表达、个人当前临床生理状态 | [GATK 流程](https://gatk.broadinstitute.org/hc/en-us/articles/360035894711-About-the-GATK-Best-Practices) | E1/技术界限 | 特殊文库/长读长方案另论 |
