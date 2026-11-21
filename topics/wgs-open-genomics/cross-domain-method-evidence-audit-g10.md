# TOPIC-017｜G10：15 个研究域 × 一手方法 × WGS 输入 × GitHub 复用能力审计

> 日期：2026-11-21。合同：[Issue #72](https://github.com/fweiger/AI_book/issues/72) / [Draft PR #73](https://github.com/fweiger/AI_book/pull/73)。按 [唯一 Tracker](GOAL_TRACKER.md) 前一轮 §7，**不增加新研究域、不以堆数量代替研究深度**。截至本轮保留 **D01–D15 共 15 域、47 个去重 P-ID DOI/指南、39 个不同 GitHub 源码候选**；不同域复用同一研究/工具，不能跨行相加。

## 0. 核对方法和证据口径

**用户原要求的研究链条**：**实际买到的约 30–40× 短读长人类 DNA WGS 数据质量 → 论文所用 assay/队列/外部表型 → 能回答的问题和科学上限 → GitHub 实现的真实输入/输出 → 独立验证**。不能因能取得 FASTQ、BAM/CRAM、variants-only VCF 或 40× 平均深度就假设每篇论文可按个人样本原样复现。

- **论文 E1 方法查验**：按本轮可实际打开的期刊原文 HTML、PubMed/PMC 一手摘要或方法段核对下列 15 个代表 P-ID。**方法摘取的深度不均等**：PubMed 摘要、正式标准摘要、部分全文段落，不声称完成全部 47 篇全文/补充材料、复算统计或系统综述。原始 DOI 和页面链接均逐行列出，允许独立回读。
- **源码 E0 输入核验**：按本轮 GitHub 对应库默认分支 README / Repo metadata 核对 13 个有代表性的现成工具（涵盖多数不同输入契约），许可证采用[既有目录](open-source-projects.md)中的已有核验状态；**本轮没有对全部 39 个仓库的 LICENSE/依赖逐项重新完成法律核查**。工具目前可读取 ≠ 实际运行通过。
- **唯一 E2**：承接 [G9 公开 HG002 chr20 1Mb bcftools 1.19 + RTG 3.13 的实际 VCF/真值比较与二次复现](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md)，只属于 **D01 的有限样本/小变异**。其余 D02–D15 的算法仍 E2 `NOT_RUN`，不能从论文内的准确率替换成本项目实测。
- **方法级风险标记**：`SINGLE_WGS`（单人原始数据可以做研究候选）、`EXTERNAL`（还需合法第二人/人群/表型/训练/临床数据）、`OTHER_ASSAY`（普通短读长 DNA WGS 不具该直接测量），以及 `UNCERTAIN`（许可/精度/跨祖源/版本仍待验证）。这三类不是互斥：如群体 PRS 用外部模型后能给单人的分数，但无法仅凭单人测序完成模型训练和临床校准。

## 1. 15 域逐项方法证据卡（各至少 1 个既有 P-ID 和现成项目）

| 域/论文 | 一手研究真实输入、方法和样本 | 买到一份合格短读长 WGS 可以做 / 还需什么 | 既有 GitHub 输入及限制 | 可成立结论与否定边界 / 证据 |
|---|---|---|---|---|
| **D01 WGS/QC** · [P042 CMRG](https://doi.org/10.1038/s41587-021-01158-1) | NIST/GIAB 用 **HG002** 的高质量长读长单倍型分辨组装构建 **273 个困难常染色体医学基因**特殊基准；官方另外提供分 build 的 confident BED 与 truth VCF，**论文的 HiFi 组装不是消费者普通短读长 assay**。 | **SINGLE_WGS**：FASTQ→QC、配对比对 BAM/CRAM→有效覆盖/位点判读，再对统一真值范围做短变异精度实验；**没有相同参考/真值/位点覆盖不能报全基因组精度**。 | [bcftools](https://github.com/samtools/bcftools) BAM+FASTA→VCF；[mosdepth](https://github.com/brentp/mosdepth) BAM/CRAM→深度；比较器 [RTG Tools](https://github.com/RealTimeGenomics/rtg-tools) VCF+truth+BED+reference SDF（**G9 已真实用 RTG，尚未列入固定 39 仓库目录总数**）。 | **E2 仅 G9 一般区 chr20 2–3Mb、965991 bp**：SNP F1=0.9962、Indel F1=0.9367；不能冒称验证 P042 273 困难基因或全 WGS。 |
| **D02 SV/CNV/STR** · [P026 GIAB SV](https://doi.org/10.1038/s41587-020-0538-8) | NIST 综合 **19 种跨技术/方法**形成 HG002 **12,745 个 ≥50 bp** 的复杂区域筛选后 **7,281 插入+5,464 缺失**评估集，**不等于所有 SV 类别的真值**。 | **SINGLE_WGS + EXTERNAL truth**：有 read-level BAM/CRAM、insert size/split-read/depth 等可给 DEL/INS/CNV/STR 候选，须按 SV class/长度/困难区分级；部分结构与大重复需长读长及正交确认。 | [DELLY](https://github.com/dellytools/delly) BAM→SV VCF；[Truvari](https://github.com/ACEnglish/truvari) 是 **SV VCF+FASTA→benchmark/collapse**，**不是 BAM→SV caller**；ExpansionHunter 对已知 catalog 限定且 PolyForm Strict 使用受限。 | **E1/PARTIAL**：部分 DEL/INS 比对合法，不能将 12745 变异真值直接作为 CNV、INV、全部 STR 扩增的评估范围；E2 NOT_RUN。 |
| **D03 父系 Y** · [P005 Yleaf 原论文](https://doi.org/10.1093/molbev/msy032) | 原论文 Ralf et al. 2018 **DOI msy032、PMID 29518227**，根据 Y 非重组区 SNP/公开系统树进行 haplogroup 分类；另有[官方 2018 勘误 DOI msy080](https://doi.org/10.1093/molbev/msy080)，**此前注册表将勘误误作原论文，本轮纠正**。 | **SINGLE_WGS**：以 chrY 高可信 mapped reads、GRCh37/38 坐标和树版本支持父系单倍群/候选下游 SNP；**EXTERNAL** 家族/人口数据库、其他合法男性样本和历史证据才可作更细亲缘、TMRCA 校准。 | [Yleaf](https://github.com/genid/Yleaf) 官方 README 实际接受 **BAM/CRAM**（示例 `Yleaf -bam file.bam --reference_genome hg38`），还可其他序列格式；[Y-LineageTracker](https://github.com/Shuhua-Group/Y-LineageTracker) 另有 Y-SNP/Y-STR 任务。 | **E1**：确定某 Y 分支≠识别姓名/每代祖先/家族史；不把男性 Y 位点未覆盖解释为阴性；E2 NOT_RUN。 |
| **D04 母系 mtDNA** · [P030 gnomAD mtDNA](https://doi.org/10.1101/gr.276013.121) | 基于 **56,434 个 WGS** 建立 mtDNA 变异频率；论文说明 **mtDNA copy number、NUMTs、细胞系污染**及多数血液样本导致误读；排除 mtCN <50、>500 或污染>2% 等特定数据。 | **SINGLE_WGS**：从同一 BAM/CRAM 的 chrM reads 做单倍群、同质/异质候选；需逐样本实际 mt depth、NUMTs、污染/组织来源及异质比例支持，**不能复制 gnomAD 的队列筛选阈值当个人医疗标准**。 | [Mutserve](https://github.com/seppinho/mutserve) README 要求 **sorted+indexed BAM/CRAM + rCRS 参考**，输出变异 VCF/txt；既有目录已记录部分 indel 输出限制；[Haplogrep3](https://github.com/genepi/haplogrep3) 分类。 | **E1**：母系 haplogroup 不是全部母系家族史；血液异质性≠所有组织，低比例 calls 不直接诊断；E2 NOT_RUN。 |
| **D05 常染色体 IBD/亲缘** · [P008 hap-IBD](https://doi.org/10.1016/j.ajhg.2020.02.010) | Browning et al. 在**多人已相位基因型**研究人际 IBD；论文讨论大人群中 **2–4 cM** 短片段检出及误差；并非单个 WGS 自己可找到陌生亲属。 | **EXTERNAL** 必须有合法授权的第二人/群体 genotype；与 genetic map 匹配；单人可研究自身 HBD/ROH，但 **HBD 不代表已经发现现实亲属**。 | [hap-IBD](https://github.com/browning-lab/hap-ibd) README：VCF 每记录有 **GT、全部 phased、无 missing allele**，加 **PLINK 格式 cM genetic map**；普通 variants-only 单人 VCF 不满足。 | **E1**：IBD 阈值要审查 marker 及 map、IBS 误判；真实亲缘需要其他样本与授权；E2 NOT_RUN。 |
| **D06 古 DNA/人口史** · [P010 qpAdm 性能评估](https://doi.org/10.1093/genetics/iyaa045) | 2021 原文用**模拟/多群体参照**验证 qpAdm 混合比例模型的统计表现与**参考/来源群体选择**敏感性；不是单人 WGS 的历史迁徙记载。 | **EXTERNAL**：现代 WGS 转共同 SNP panel+外部古 DNA/AADR/参考群体，审模型、时间、样本覆盖和竞争方案；不能用单人 haplogroup 断言某个具体古人是直系亲属。 | [ADMIXTOOLS2](https://github.com/uqrmaie1/admixtools) README 提供 **EIGENSTRAT/PACKEDANCESTRYMAP 或 PLINK 群体 genotype** → f2/qpAdm/qpGraph；[ancIBD](https://github.com/hringbauer/ancIBD) 则要求古样本等特定处理。 | **E1**：能检验某群体混合模型是否相容，不等于认定唯一历史来源或个人迁徙路线；E2 NOT_RUN。 |
| **D07 罕见病/变异解释** · [P012 ACMG/AMP 2015](https://doi.org/10.1038/gim.2015.30) | ACMG/AMP 临床标准基于群体频率、功能证据、家系共分离、表型和数据库等组合，将序列变异分为**五级**；并区分 predicted damaging 与真正 disease pathogenic。 | **SINGLE_WGS** 可注释筛出候选，**EXTERNAL** 需要临床表型/HPO、疾病遗传模式、家系或功能/正交证据和专业复核；未测出/有疑义位点不能按阴性处理。 | [Ensembl VEP](https://github.com/Ensembl/ensembl-vep) `vep -i input.vcf -o out.txt -offline` + 注释缓存输出 consequence；[Exomiser](https://github.com/exomiser/Exomiser) 需要 phenotype/HPO 辅助排序。 | **E1**：VEP 注释/Exomiser 排名 ≠ pathogenic 分级 ≠ 罕见病诊断；E2 NOT_RUN。 |
| **D08 携带者/生育遗传风险** · [P033 ACMG Carrier 2021](https://doi.org/10.1038/s41436-021-01203-z) | **临床专业资源而非 WGS 算法准确率研究**：建议对孕前/孕期提供 Tier 3 携带者筛查，并报告 panel 范围、方法局限与残余风险；需考虑伴侣携带状态、不同变异检测方法和咨询。 | **SINGLE_WGS** 可研究可判读基因的候选致病等位；**EXTERNAL** 临床级解析、复杂变异验证、伴侣/家系结果与同病风险条件；单人普通 WGS VCF 不构成完整临床 carrier panel。 | [InterVar](https://github.com/WGLab/InterVar) 支持 VCF/ANNOVAR→ACMG 证据辅助，**仅免费非商用、ANNOVAR 数据库另限权**；[Gauchian](https://github.com/Illumina/Gauchian) GBA1 假基因区域，**P036 负面论文与 P045 开发者回应并列，性能争议未解且 PolyForm Strict**。 | **E1**：检测阴性≠零残余风险；P033 指南不能替代实验室测序验证；E2 NOT_RUN。 |
| **D09 药物基因组 PGx** · [P024 StellarPGx](https://doi.org/10.1002/cpt.2173) | Nextflow 图算法+覆盖+star allele 组合对 **109 份 CDC GeT-RM WGS** 的 **CYP2D6 diplotype** 做方法验证；须与复杂拷贝数/假基因及参考条件配套，不是药物临床结局试验。 | **SINGLE_WGS** 高质量 full BAM/CRAM、相符参考可候选 PGx star allele；**EXTERNAL** CPIC/PharmGKB 更新指南、药史与临床验证，不能将序列候选变成用药修改指令。 | [StellarPGx](https://github.com/SBIMB/StellarPGx) README **只支持高覆盖短读长 WGS、indexed BAM/CRAM**，当时不支持普通 exome/panel/long read；已有目录 MIT；[PharmCAT](https://github.com/PharmGKB/PharmCAT) 对格式化 PGx 基因型做后续解释。 | **E1**：普通 SNP-only VCF 不足以可靠处理 CYP2D6 CNV/SV；GeT-RM 109 样本的结果不是任意用户药物反应精度；E2 NOT_RUN。 |
| **D10 复杂疾病/PGS** · [P025 PGS Catalog Calculator](https://doi.org/10.1038/s41588-024-01937-x) | PGS Catalog 方法项目整合已发表权重、基因型变异匹配和**参考祖源/分布归一化**，并不声称可从一个人基因组训练群体预测模型。 | **SINGLE_WGS+EXTERNAL**：有授权 PGS 权重、完整可恢复的目标基因型/等位基因构建和祖源校准可计算一个分数；**模型训练/验证/绝对疾病风险**需要外部大队列和结局资料。 | [pgsc_calc](https://github.com/PGScatalog/pgsc_calc) README 明写 **“Whole genome sequencing (WGS) data are not currently supported”**，对已 imputed SNP genotypes/PLINK/合格 VCF 设计；存在 gVCF 准备讨论但不是普通 WGS variants-only VCF 原生可用；[PRS-CSx](https://github.com/getian107/PRScsx) 需多祖源 GWAS summary+LD。 | **E1**：输出 PGS 不等于确定患病或可直接临床校准；不同祖源转移偏差，单人 WGS 不能复现 GWAS；E2 NOT_RUN。 |
| **D11 睡眠/晨晚型** · [P019 Chronotype GWAS](https://doi.org/10.1038/s41467-018-08259-7) | **697,828 个欧洲祖源自评晨晚型**（UKB 449,734 + 23andMe 248,098）GWAS，另有活动记录子队列和遗传评分关联；研究的是**晨晚型偏好与睡眠时序群体分布**，不是单人入睡时间预测器。 | **SINGLE_WGS+EXTERNAL**：有匹配的效应等位/权重可做研究性偏好评分，但仍需祖源参照与个体睡眠日志、腕表等实际表型；不能由 DNA 断言今晚入睡时间或治疗效果。 | [PLINK2](https://github.com/chrchang/plink-ng) VCF/PGEN 与 PGS weight 做基因型评分；[pgsc_calc](https://github.com/PGScatalog/pgsc_calc) 须先满足 compatible/imputed 输入，**普通 WGS VCF 不直接支持**。 | **E1**：晨晚型、失眠、时长三种 phenotype 不可混为一个“睡眠基因”；极端人群的平均作息差异≠个人分钟级预测；E2 NOT_RUN。 |
| **D12 饮食与营养个性化** · [P020 DIETFITS RCT](https://doi.org/10.1001/jama.2018.0245) | **609 名受试者随机低脂 vs 低碳，481 人完成 12 个月**；测试预设 genotype pattern/胰岛素分泌与干预的交互，基因型 `P=0.20`、胰岛素分泌 `P=0.47`，**没有支持这些指标替个人选择最佳减重饮食**。 | **SINGLE_WGS** 可以报告文献涉及的 SNP 候选；若要评估个人是否响应某饮食，需 **EXTERNAL 实测饮食、体重和随机干预表型**，不能以模型输出替代 RCT 阴性结论。 | [PLINK2](https://github.com/chrchang/plink-ng)/[bigsnpr](https://github.com/privefl/bigsnpr) 可做通用基因型统计；**39 项既有目录无被该 RCT 独立验证的“个人减重饮食选择”专用软件**。 | **E1/负证据**：在该试验中不支持预定分型交互，并不等于所有营养遗传研究都无效；E2 NOT_RUN。 |
| **D13 运动/体质** · [P039 身体活动 GWAS](https://doi.org/10.1038/s41588-022-01165-1) | **51 项研究、最多 703,901 人、99 loci**，研究自报中高强度闲暇活动、屏幕时间/久坐，样本按论文约 **94% 欧洲祖源**；**研究活动习惯不是运动训练后的 VO₂max 反应**。 | **SINGLE_WGS+EXTERNAL**：可研究现有群体活动倾向权重，实际能力/训练效果需测量运动表现、运动前后队列及跨祖源验证；单人的 DNA 不足以制定个体训练计划。 | [PLINK2](https://github.com/chrchang/plink-ng)、[bigsnpr](https://github.com/privefl/bigsnpr)、[pgsc_calc](https://github.com/PGScatalog/pgsc_calc) 为**通用**基因型/PGS 工具，没有从 WGS 直接生成经过外部验证的运动处方。 | **E1**：活动 GWAS、训练反应、运动能力是不同表型，不能把 P040 HERITAGE 样本内 49% 方差当独立可迁移准确率；E2 NOT_RUN。 |
| **D14 HLA/复杂免疫区域** · [P023 OptiType](https://doi.org/10.1093/bioinformatics/btu548) | 2014 HLA 方法通过**整数线性规划**在已观测的 RNA/DNA NGS 序列中联立选择 HLA **Class I** 等位，论文做方法样本测试，旧研究/参考库不能作为个人 40× 自动临床准确率。 | **SINGLE_WGS**：若 HLA 区域质量/参考 allele DB 适用，reads 可以做 **HLA-A/B/C 研究性分型**；HLA-II、临床移植配型及复杂区验真不由此保证。 | [OptiType](https://github.com/FRED-2/OptiType) README 提供 **FASTQ 或 mapped BAM**（`optitype run -i mapped.bam --dna`），BSD-3-Clause；可选 **CPLEX 商业求解器**，或 CBC，依赖策略需分开。 | **E1**：不能把部分 HLA-I 研究型别外推成 HLA-II 或移植临床合格报告；E2 NOT_RUN。 |
| **D15 普通 DNA WGS 不能直接测的多组学** · [P046 长读长修饰对照](https://doi.org/10.1186/s13059-024-03207-9) | 实证涉及 **7,179 个 ONT 长读长样本、132 同次血样 oxBS、50 PacBio SMRT**；研究通过**特定长读长平台的原生修饰检测信号**验证 CpG methylation，**并非一般 30–40× Illumina/MGI 短读长 FASTQ 的直接信息**。 | **OTHER_ASSAY**：普通短读长人类 DNA WGS 只能给 DNA 序列，不能把当前 CpG 甲基化、组织 RNA 表达、完整肠道菌群或蛋白浓度从 ACGT 文本逆算出来；需原生长读长修饰 assay / WGBS、RNA-seq、相应样本的宏基因组、蛋白组等。 | **39 个以普通短读长 WGS 为对象的目录里无可从既有 DNA FASTQ 直接生成这些真实表型的对应工具**；不能为了凑开源项目数把 RNA-seq/ONT 甲基化工具标记成 WGS 数据直接兼容。 | **E1/ASSAY_MISMATCH**：特定 ONT WGS 确能测部分 DNA 修饰，所以“所有 WGS 都不能测甲基化”也错误；普通 DNA WGS 非人 reads 即使存在，亦不等于可靠肠道菌群检测。 |

## 2. 单份 WGS 数据的真正研究层级（跨域可复用）

| 实现能力 | 当前 15 域对应 | 数据质量/外部依赖 | 可接受的交付陈述 |
|---|---|---|---|
| **L1 个人序列直接读数** | D01、D03、D04、D07、D08、D09、D14、部分 D02 | FASTQ/BAM/CRAM、位点 callable、核/线粒体/特殊区域质量 | “得到合格区间内的候选 genotype / haplogroup / star allele / HLA-I type”，不能直接临床确证 |
| **L2 单人数据 + 外部模型** | D10、D11、D12、D13、部分 D06 | 已发表的相符权重/人群参照、构建一致、祖源与表型边界 | “可计算或探索候选性状相关评分”，不是个人发病、睡觉钟点或运动处方 |
| **L3 本质需要多人/群体数据** | D05 人际 IBD、D06 qpAdm/AADR、D10 训练与外部校准、D08 生育对偶风险 | 多人合法授权样本/参考群体/临床结果/真实表型 | “在充分外部数据下检验共同祖源/群体模型/携带风险”，单人无法原样复现 |
| **L4 WGS 不是该 assay** | D15 当前修饰、表达、微生物群等 | 其他生物样本、平台和测量技术 | “普通短读长人类 DNA WGS 不直接测该指标”，将额外所需 assay 明确列出 |

> **不要误解 L1–L4 是“科学价值排名”或所有域互斥的标签**。这是数据实际可获得性和解释层级；临床/隐私/法律门槛与它们正交。专业干预需要与医学证据链独立验证。

## 3. 本轮已证实的数据与文献引用错误

**D03 / P005 原文 DOI 错配（已修复到原注册表和 sources.md）**：

- 原登记 `P005 = 10.1093/molbev/msy080`，PubMed [PMID 29518227](https://pubmed.ncbi.nlm.nih.gov/29518227/) 核实 **Ralf et al. 2018 原始论文为 `10.1093/molbev/msy032`，35(5):1291–1294**。
- `10.1093/molbev/msy080` 实为对该原文的 **Erratum，35(7):1820**，不是另一篇独立的 Yleaf 方法论文。已改 P005 原 DOI，保留勘误说明。不新增一个 P-ID 凑计数，全球去重 DOI 仍应 47。
- 本轮另发现 [pgsc_calc 官方 README](https://github.com/PGScatalog/pgsc_calc) 比主矩阵原口吻更明确：*普通 WGS 数据当前不受支持*。以前“variants-only VCF 不直接支持”的说法是必要但不够完整的提示。**有讨论可将 WGS 转合适 gVCF/兼容格式，不等于官方原生支持已验证**。D10/D11/D12/D13 必须先过模型 SNP genotype 的实质可得性检查。

## 4. 仍有的认识论缺口（不能假称已完成）

1. **论文深度**：15/15 代表 DOI 的一手期刊/PMC/PubMed/正式标准被重新定位并核对关键摘要/部分正文方法，**并非 47/47 全文逐章审阅、全量统计验证、补充资料或系统综述**。P019/P020/P039 的大样本统计并非单人 WGS 算法准确率。
2. **源码深度**：本轮审阅了可访问 GitHub README 和部分 repo 元数据以核输入限制，**所有 39 个的最新依赖/许可证/可商用性/恶意代码安全及 Linux/macOS 实测未覆盖**。G9 仅 bcftools/RTG E2（且 RTG 未计入固定 39 候选）。
3. **数据与隐私**：除 HG002 chr20 1Mb，**没有任何个人或亲属样本**；没有从真实用户文件、外部祖源或疾病资料计算个体医学/行为概率。
4. **统计性**：即使 G9 区域 SNP/Indel F1 看起来高，也不能给 D02–D15 贴 E2 PASS，更不支持外推到困难区、短重复扩增、不同祖源或临床敏感位点。

## 5. 基于用户原始研究目标的下一阶段唯一建议

**不要转入“安装 39 个软件”的无边界工程**。沿 15 域矩阵，针对高风险/高科研收益但仍未有实际输入验证的 **D03 父系（tree 与数据库）、D04 mtDNA、D09 PGx、D10 PRS**，在相同 WGS 数据合同框架下做一次**工具可操作输入检查和研究对象覆盖上限排序**（先 E0/E1，小样本合法公开数据可用时再 E2）。若真正的目标是提高论文系统审阅完整度，则先审其他 32 篇最影响解释的原文和反证，而非根据论文数量完成率自动升级。

当前结果应同步同一规范 Issue #72 / 同一 Tracker，不允许创建另一个研究主业务 Issue。原 Issue Goal、Scope、Non-goals、AC 与协议 SHA 均不变。
