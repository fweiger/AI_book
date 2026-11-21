# TOPIC-017｜34 个已核实 GitHub 开源项目：问题、文件、输出和局限

> 2026-11-21 使用已连接 GitHub 仓库元数据逐一核实存在，**原始 32/32 与 G4 新增 2/2 的仓库存在性 PASS**；**运行测试、许可证适配、性能基准仍 NOT_RUN**。本目录只是经过确认的候选池，不是 GitHub 全量统计。高质量 WGS 的投入应放在原始数据质量和分析复现，不要仅按 stars 排序。

## 基础流程/质控/基准（12）

| # | GitHub 项目 | 输入 | 可得到的东西 | 核心局限 |
|---:|---|---|---|---|
| 1 | [nf-core/sarek](https://github.com/nf-core/sarek) | FASTQ/BAM/CRAM | 综合变异检测与注释流水线 | 需核查依赖、运行环境与参考版本 |
| 2 | [OpenGene/fastp](https://github.com/OpenGene/fastp) | FASTQ | 读段质控、过滤 | 质量提升不等于遗传准确性验证 |
| 3 | [s-andrews/FastQC](https://github.com/s-andrews/FastQC) | FASTQ | 测序质量报告 | 仅质控报告 |
| 4 | [MultiQC/MultiQC](https://github.com/MultiQC/MultiQC) | 各工具 QC 文件 | 聚合报告 | 不独立做遗传推断 |
| 5 | [bwa-mem2/bwa-mem2](https://github.com/bwa-mem2/bwa-mem2) | FASTQ+FASTA | 短读长参考比对 | 重复区与参考版本限制 |
| 6 | [samtools/samtools](https://github.com/samtools/samtools) | BAM/CRAM | 排序索引统计查看 | 不单独给临床结论 |
| 7 | [samtools/bcftools](https://github.com/samtools/bcftools) | VCF/BCF/BAM | 变异处理、规范化和统计 | 需一致参考等位基因版本 |
| 8 | [brentp/mosdepth](https://github.com/brentp/mosdepth) | BAM/CRAM | 测序覆盖/深度统计 | 深度≠准确率 |
| 9 | [google/deepvariant](https://github.com/google/deepvariant) | BAM/CRAM+reference | SNV/Indel 调用 | 模型版本和训练平台适配 |
| 10 | [broadinstitute/gatk](https://github.com/broadinstitute/gatk) | BAM/CRAM+reference | HaplotypeCaller/基因组分析 | 需按预处理/过滤最佳实践 |
| 11 | [Illumina/hap.py](https://github.com/Illumina/hap.py) | VCF+benchmark truth | SNV/Indel precision/recall | 只能在真值覆盖区域评估 |
| 12 | [snakemake-workflows/dna-seq-benchmark](https://github.com/snakemake-workflows/dna-seq-benchmark) | 测试样本+truth | 基准实验工作流 | 测试集与真实客户样本存在域差异 |

## 结构变异与重复序列（4）

| # | GitHub 项目 | 输入 | 可得到的东西 | 核心局限 |
|---:|---|---|---|---|
| 13 | [Illumina/manta](https://github.com/Illumina/manta) | WGS mapped reads | SV/Indel calling | 仓库已归档；维护/兼容风险 |
| 14 | [dellytools/delly](https://github.com/dellytools/delly) | BAM/CRAM | SV 调用 | 短读长复杂区域受限 |
| 15 | [etal/cnvkit](https://github.com/etal/cnvkit) | BAM/read coverage | CNV 分析 | 须确认 WGS 模式和归一化参考 |
| 16 | [Illumina/ExpansionHunter](https://github.com/Illumina/ExpansionHunter) | WGS reads | 目标重复位点检测 | 短读长扩增大小可能不准确 |

## 父系与母系（4）

| # | GitHub 项目 | 输入 | 可得到的东西 | 核心局限 |
|---:|---|---|---|---|
| 17 | [genid/Yleaf](https://github.com/genid/Yleaf) | Y reads/BAM/VCF | Y haplogroup | 分支解析依赖树版本与位点覆盖 |
| 18 | [Shuhua-Group/Y-LineageTracker](https://github.com/Shuhua-Group/Y-LineageTracker) | chrY variants/reads | Y-SNP、Y-STR 分析 | 非谱系文献历史证明 |
| 19 | [23andMe/yhaplo](https://github.com/23andMe/yhaplo) | Y genotype calls | Y haplogroup 分类 | 终端分支取决于 SNP 集与树 |
| 20 | [genepi/haplogrep3](https://github.com/genepi/haplogrep3) | mtDNA variants/FASTA | 母系 mtDNA haplogroup | 非全部母系家族史 |

## 古 DNA / IBD / 人口历史（4）

| # | GitHub 项目 | 输入 | 可得到的东西 | 核心局限 |
|---:|---|---|---|---|
| 21 | [nf-core/eager](https://github.com/nf-core/eager) | 古 DNA reads | 古 DNA 损伤/污染及分析 | 不是现代 WGS 的必要预处理 |
| 22 | [hringbauer/ancIBD](https://github.com/hringbauer/ancIBD) | 古 DNA 格式/相位与参考 | 古样本 IBD 片段分析 | 需要多个样本及合适参考面板 |
| 23 | [uqrmaie1/admixtools](https://github.com/uqrmaie1/admixtools) | 群体 SNP 矩阵 | f 统计/qpAdm 人口史模型 | 需要独立参考群体和模型敏感性 |
| 24 | [browning-lab/hap-ibd](https://github.com/browning-lab/hap-ibd) | 相位基因型数据 | 两人及以上 IBD 检测 | 单人无法计算亲缘匹配 |

## 医学变异与药物（3）

| # | GitHub 项目 | 输入 | 可得到的东西 | 核心局限 |
|---:|---|---|---|---|
| 25 | [Ensembl/ensembl-vep](https://github.com/Ensembl/ensembl-vep) | VCF+注释cache | 变异效应注释 | 注释不是致病性临床分级 |
| 26 | [exomiser/Exomiser](https://github.com/exomiser/Exomiser) | VCF+HPO | 候选罕见病变异优先级 | 需要表型和临床确认 |
| 27 | [PharmGKB/PharmCAT](https://github.com/PharmGKB/PharmCAT) | 标准化 VCF/PGx | 药物基因组学与指南关联 | star alleles/复杂基因/临床确认 |

## 群体遗传与多基因风险（5）

| # | GitHub 项目 | 输入 | 可得到的东西 | 核心局限 |
|---:|---|---|---|---|
| 28 | [chrchang/plink-ng](https://github.com/chrchang/plink-ng) | 基因型矩阵 | PCA/QC/PRS计算 | 单人不构成有效人群统计 |
| 29 | [getian107/PRScs](https://github.com/getian107/PRScs) | GWAS summary + LD | 贝叶斯 PRS 权重 | 祖源匹配影响校准 |
| 30 | [getian107/PRScsx](https://github.com/getian107/PRScsx) | 跨祖源 GWAS | 跨祖源 PRS 模型 | 外部验证仍必要 |
| 31 | [privefl/bigsnpr](https://github.com/privefl/bigsnpr) | 大规模基因型 + 参考 | LDpred2/高效基因型计算 | 需人群与合适 LD |
| 32 | [PGScatalog/pgsc_calc](https://github.com/PGScatalog/pgsc_calc) | PGS 模型+基因型 | PGS Catalog 评分计算 | 不能直接诊断/必然发病 |

## G4 新核验：药物复杂基因与 HLA-I 专项（2）

| # | GitHub 项目 | 输入 | 可得到的东西 | 核心局限与证据 |
|---:|---|---|---|---|
| 33 | [SBIMB/StellarPGx](https://github.com/SBIMB/StellarPGx) | **高覆盖短读长 WGS BAM/CRAM**、匹配参考 genome build | CYP2D6 等药物代谢基因 star alleles、部分 CNV/SV 信息；[方法论文 P024](https://doi.org/10.1002/cpt.2173) | **MIT、已核 release v1.2.8**；论文 GeT-RM 109 样本校验不等于该用户准确率；与 PharmCAT 分层配合。详见 [G4 审计](cross-domain-evidence-audit.md) |
| 34 | [FRED-2/OptiType](https://github.com/FRED-2/OptiType) | **DNA FASTQ 或已比对 BAM** | HLA **Class I** 分型结果 TSV；[方法论文 P023](https://doi.org/10.1093/bioinformatics/btu548) | **BSD-3-Clause、已核 release v1.5.0**；不覆盖 HLA-II；仍需真实样本/正交验证 |

> 分组说明：T33 同属药物 D09，T34 属于 HLA-I D14；新增原因是发现对个人 WGS 有实质意义的原先功能缺口，而非追求工具数。6 个旧类别 32 项不变，34 项总数为 32+2。**软件实际执行仍 NOT_RUN。**

## 不同研究需求的最小组合
- **先看 WGS 实测质量**：FASTQ → fastp/FastQC → BWA-MEM2 → samtools/mosdepth → MultiQC；必要时以 nf-core/sarek 执行。
- **标准 SNV/Indel**：DeepVariant / GATK → bcftools norm → GIAB/hap.py 对照。
- **父系**：从 Y 染色体 callable regions 出发 → Yleaf、Y-LineageTracker/yhaplo 交叉核对，非计算工具自动证明历史名人。
- **母系**：mtDNA reads/variants → Haplogrep3；警惕 NUMTs 和异质性。
- **古 DNA**：nf-core/eager 专门处理古样本，不应给现代个人样本机械套用；群体 qpAdm / ancIBD 需公共样本矩阵。
- **健康**：Ensembl VEP/Exomiser/PharmCAT 生成候选，依 ClinVar/ClinGen、ACMG/CPIC 指南与临床专业复核。
- **PRS 与睡眠**：PGS Catalog 与合适的 GWAS/LD/祖源数据；**pgsc_calc 当前不能原生读取普通 WGS variants-only VCF**，需要生成模型可匹配、保留纯合参考位点的基因型输入，再评估位点 match rate；强调模型校准与外部验证。

## 未来逐仓深度核查字段
`repo_url` / commit或release SHA / license / last_active / dependency / docker_digest / min_CPU_RAM_storage / genome_build / input_format / expected_output / example_dataset / benchmark / linked_publication / limitations / E0-E4 evidence / code_review_notes。

**状态**：E0 目录核验完成；各仓实际可运行性 NOT_RUN。