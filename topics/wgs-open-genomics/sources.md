# TOPIC-017｜原始论文、权威规范与公共数据库

> 来源层级：DOI/官方项目为直接来源入口；本轮核对题名、摘要或机构项目说明，**不声称已逐篇阅读全文，也不伪造实验结果**。下列证据的适用范围需逐篇展开。
>
> **目前以 [36 篇不重复论文 P-ID 注册表](paper-register.md) 为论文计数源、以 [15 方向主矩阵](evidence-capability-matrix.md) 与 [G4 实质审计](cross-domain-evidence-audit.md)、[G5 D02/D04/D08 审计](cross-domain-evidence-audit-g5.md) 为论文—工具关系源。** 本文件为阅读入口/补充来源，不应与 P-ID 注册表相加宣称论文总数。

## 技术与基准
1. Hanssen et al. (2024), *Scalable and efficient DNA sequencing analysis on different compute infrastructures aiding variant discovery*, [DOI 10.1093/nargab/lqae031](https://doi.org/10.1093/nargab/lqae031) — Sarek：大规模可复现 variant workflow。
2. [Broad Institute GATK Best Practices](https://gatk.broadinstitute.org/hc/en-us/articles/360035894711-About-the-GATK-Best-Practices) — WGS 的清洗、比对、变异发现步骤；官网方法标准。
3. [NIST Genome in a Bottle](https://www.nist.gov/programs-projects/genome-bottle) — HG002 等真值与 benchmark；不是所有序列区域都有真值。

## 家谱、古 DNA 与人群历史
- [Y 染色体工具与谱系时钟：一手 README 对照和推断边界](y-chromosome-methods.md)。
- [Poznik (2016) yhaplo 算法 bioRxiv 预印本 DOI 10.1101/088716](https://doi.org/10.1101/088716)；注意项目 README 的非商业使用许可。
4. Ralf et al. (2018), *Yleaf: Software for Human Y-Chromosomal Haplogroup Inference from Next-Generation Sequencing Data*, [DOI 10.1093/molbev/msy080](https://doi.org/10.1093/molbev/msy080) — Y 染色体单倍群。
5. Chen et al. (2021), *Y-LineageTracker: a high-throughput analysis framework for Y-chromosomal next-generation sequencing data*, [DOI 10.1186/s12859-021-04057-z](https://doi.org/10.1186/s12859-021-04057-z) — Y-SNP/Y-STR。
6. Haplogrep 3 (2023), *Nucleic Acids Research*, [PubMed 37070190](https://pubmed.ncbi.nlm.nih.gov/37070190/) — mtDNA 谱系。
7. Ringbauer et al. (2024), *Accurate detection of identity-by-descent segments in human ancient DNA*, [DOI 10.1038/s41588-023-01582-w](https://doi.org/10.1038/s41588-023-01582-w) — 古 DNA IBD，必须区分古代样本实际年龄与 TMRCA。
8. [Allen Ancient DNA Resource (AADR)](https://doi.org/10.7910/DVN/FFIDCW) — 古人群对照与样本版本、公共数据授权。

## 罕见病、药物与临床边界
9. Richards et al. (2015), *Standards and guidelines for the interpretation of sequence variants*, [DOI 10.1038/gim.2015.30](https://doi.org/10.1038/gim.2015.30) — ACMG/AMP 五级变异分类，**不等同自动诊断**。
10. ACMG Secondary Findings v3.3 (2025), [DOI 10.1016/j.gim.2025.101454](https://doi.org/10.1016/j.gim.2025.101454) — 非预期次要发现的临床建议与边界。
11. [PharmCAT 官方文档](https://pharmcat.clinpgx.org/) 和 [CPIC 官方](https://cpicpgx.org/) — star allele / drug-gene association；没有专业临床流程不改变处方。
12. [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) · [ClinGen](https://clinicalgenome.org/) · [gnomAD](https://gnomad.broadinstitute.org/) — 变异分类、基因疾病证据和频率；必须固定版本。

## 复杂疾病、多基因与昼夜节律
13. *Improving Polygenic Prediction in Ancestrally Diverse Populations* (2022), [DOI 10.1038/s41588-022-01054-7](https://doi.org/10.1038/s41588-022-01054-7) — PRS-CSx 跨祖源预测。
14. *Principles and methods for transferring polygenic risk scores across global populations* (2024), [DOI 10.1038/s41576-023-00637-2](https://doi.org/10.1038/s41576-023-00637-2) — 可迁移性与人群偏差。
15. *Selection, optimization and validation of ten chronic disease polygenic risk scores...* (2024), [DOI 10.1038/s41591-024-02796-z](https://doi.org/10.1038/s41591-024-02796-z) — eMERGE 真实队列验证框架。
16. Jones et al. (2019), *Genome-wide association analyses of chronotype in 697,828 individuals*, [DOI 10.1038/s41467-018-08259-7](https://doi.org/10.1038/s41467-018-08259-7) — 351 个关联位点，但不能精确预测个人作息。
17. [PGS Catalog](https://www.pgscatalog.org/) — 模型版本、样本人群和评分文件；模型总量不等于全部可临床使用。

## 必须补的核验工作
每篇逐一记录研究设计、队列 N、祖源构成、质量控制、数据时间/范围、模型/基准、正反证据、外推边界、论文许可证、是否原文阅读全文。可借用上述项目的工具/数据，但不得把论文摘要当作全文验证。
