# TOPIC-017｜个人 30–40× 短读长 WGS 最小交付与分析准入表（v0.1）

> 面向将来采购/验收 23魔方、WeGene、华大等机构的**同一标准询证表**。不假定上述任一商业品牌已经交付具体格式或达到本要求，也不将论文质量指标视作商家承诺。公开 AI_book 只记录标准/模板，**不得上传实际个人基因文件与隐私报告**。方法来源：[G7 D01/D15 全域审计](cross-domain-evidence-audit-g7.md)、[ACMG NGS 技术标准](https://doi.org/10.1038/s41436-021-01139-4)、[NIST GIAB](https://www.nist.gov/programs-projects/genome-bottle)。

## 1. 向厂商明确索取的字段（可使用表格逐家书面确认）

| 级别 | 请求字段（尽可能确切名称） | 缺失后对研究的影响 |
|---|---|---|
| A：原始完整性 | `FASTQ.gz R1/R2`、文件大小、read count、bases、SHA256、是否按 lane 提供 | 只给 PDF/芯片 SNP/少量 CSV 时不能从头做 WGS QC 与重新比对；FASTQ 出口与隐私条件需书面明确 |
| A：比对复现 | 全基因组 **BAM/CRAM + index**；参考 `GRCh38/hg38` 或指定 build 与 reference FASTA/MD5；PE/read length、PCR-free 与否 | CRAM 需正确 reference；只有 VCF 无法检查 chrY/mtDNA/结构/复杂基因 read 层证据 |
| A：短变异复用 | 原始/经筛选 `VCF.gz + .tbi`、最好含参考区间的 `gVCF`；software commit/release、过滤与 No-call 定义 | **variants-only VCF 没列出参考位点，不代表这些 SNP 已得到可靠阴性基因型**；PRS/IBD/PGx 部分工具要求更完整 genotypes |
| A：有效质量 | `raw Q30 / mapped bases / duplicates / insert size / align rate / mean/median autosome effective coverage`，`P(>=10x),P(>=20x),P(>=30x)` 与 MAPQ 筛选口径 | 平均 40× 无法回答关键基因可判读率；`Gb` 测序碱基≠`GB` 磁盘大小 |
| B：专项覆盖 | chrY NRY callable SNP/regions、mtDNA depth/heteroplasmy 方法、HLA-I、CYP2D6/GBA1 等复杂区域与 repeat/copy-number calling 质量 | 无需因个别特殊基因不支持否定整个 WGS，但要**逐领域降级，不能宣称所有区域可用** |
| B：真值与外部验证 | 公开同平台/同文库/相近深度 GIAB HG002 benchmark；truth VCF+BED、精确 reference build、SNV/Indel 分开 metrics 与 CMRG 特殊区域 | 没有这些证据，只能说“有工具输出”，不能说全基因组或医学敏感位点精度已验证 |
| A：数据权利与交付 | 可以多次下载原始序列/CRAM/gVCF？下载期限、额外费用、数据删除与留存、第三方上传权利、商用衍生限制 | 某些厂商可能只交报告/限期下载；没有书面确认不得将其当可长期迭代的个人数据资产 |

> **A/B 是采购分析优先级，不是医学检测等级**。真正的“合格”应按预期研究目的分类：若仅做父系单倍群，高质量 chrY BAM/CRAM 价值高；若做 PRS，须有完整或可恢复的模型 SNP 基因型与祖源校准；若做 PGx 的 CYP2D6，则需 CNV/SV 专项 caller 和临床验证。**没有一个统一 30×/40× 阈值能保证全部研究方向通过。**

## 2. 现有软件如何转化为可检查的客观结果

| 原始交付 | 已存在项目 | 仅凭软件可直接得到的检查 | 无法直接证明 |
|---|---|---|---|
| FASTQ | [fastp](https://github.com/OpenGene/fastp) | `fastp.json / fastp.html`，Q20/Q30、GC、接头、原始与处理后的读段比例 | 生殖/医学位点的变异真值 |
| BAM/CRAM+参考 | [samtools](https://github.com/samtools/samtools) + [mosdepth](https://github.com/brentp/mosdepth) | `samtools stats/flagstat`、`mosdepth.summary/dist/regions`，含区域 ≥10×/20×/30× 统计 | 每个位点的变异 caller 精度、难区域检出率 |
| BAM/CRAM + 正确模型 | [DeepVariant](https://github.com/google/deepvariant) | SNV/Indel `VCF/gVCF`，按参考/模型输出 genotype | HLA/结构变异/全部复杂重复的通用检出 |
| 公共 GIAB 参考数据+truth BED+VCF | [hap.py](https://github.com/Illumina/hap.py) | 在 benchmark BED 内按 SNV/Indel 分类计算 Precision/Recall/F1 | BED 以外区域精准度，或消费者个人数据的真实变异真值 |
| 高覆盖 CRAM+其他人群数据 | 已选 Yleaf/Mutserve/hap-IBD/pgsc_calc 等 | 每个方向进一步取需要的数据建立独立准入，不直接共享一个“合格”状态 | 单人不能凭空得到人际 IBD，普通 WGS VCF 不能直接进入所有 PRS 软件 |

## 3. 绝对不能在购买后从普通短读长 WGS 原始文件“直接再算出来”的资料

- 当前组织 **RNA 表达**：需要相应样本 RNA-seq；基因组调控位点预测不等于实测。
- 当前组织 **DNA 甲基化、表观遗传年龄**：需要 WGBS/EM-seq/甲基化阵列，或专门保留修饰信号的原生长读长 assay。普通标准 ACGT 短读长 FASTQ 没有原始修饰电流信息。
- 可信的 **肠道菌群组成/感染诊断**：要采样相应组织、宏基因组或针对性方法、阴阳性对照；人类 WGS 非人 reads 可能存在但不应直接解释成健康/肠道群落。
- 个人真实 **蛋白丰度、代谢物及当前生理状态**：需要相应检测和表型记录；DNA 相关 SNP 只能产生假说。

## 4. 最小可验收使用方式

对每个厂商只收集它自己提供的**书面参数与格式样本**，统一入表：`company_product / genome_depth_claim / raw_base_yield / effective_depth / FASTQ / CRAM+BAM / VCF / gVCF / genome_build / callable_20x / chrY_QC / mtDNA_QC / retrieval_cost / retention / privacy`。未知项填 **UNKNOWN**，不推测品牌差异；数据未买到之前，不可能完成针对个人文件的独立质量评估。

**当前状态**：规格与对应开源软件原始 README 的静态关系有来源；任何厂商具体交付效果、报告真实数据与个人样本 QC 均 `NOT_RUN/UNKNOWN`。
