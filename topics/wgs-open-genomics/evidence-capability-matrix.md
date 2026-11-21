# TOPIC-017｜WGS 数据质量 × 论文证据 × 研究方向 × 开源工具（主矩阵 v0.1）

> **核心逻辑：先审 WGS 能力，再审学术研究的输入条件及可达到的解释深度，最后匹配可复用的 GitHub 项目。** 父系 Y 只是研究域 D03，不是全专题总主线。
>
> **收录口径（2026-11-21）：15 个研究域、47 篇已登记的具体论文/指南/综述、39 个已核存在 GitHub 源码仓库（其中部分不具标准开源许可证）。** 本表中各方向的论文/工具数量是**当前登记且有关联的条目数**，不是全球全部论文/项目；同一篇论文和项目可跨域复用，不能把各行数字相加。论文原始题录见 [P-ID 注册表](paper-register.md)，项目详情见 [39 个 GitHub 源码候选及许可目录](open-source-projects.md)。论文中使用芯片、古 DNA、人群统计或临床数据的结果**不能因消费者拥有一份 40× WGS 就自动复现**。

## A. WGS 数据质量准入层

| Gate | 原始资料与必要技术条件 | 可支持的研究 | 不满足时的处理 |
|---|---|---|---|
| G00 数据溯源 | FASTQ/CRAM/BAM/VCF、样本授权、文件 hash、平台与参考基因组构建、原始 QC | 全部 | 只有 PDF/筛选 SNP 就降级，不冒称有完整 WGS |
| G01 SNV/Indel | 位点 depth、mapping/base quality、去重有效深度与覆盖广度；GRCh38 等 genome build 与调用软件一致 | 技术、疾病、药物、PRS、部分表型 | 目标位点没测到/不可靠标 NO_CALL；不因平均 40× 强行填值 |
| G02 SV/CNV/STR | 短读长/片段长度、复杂/重复区域可分析性、读段对和 CNV 覆盖 | 结构变异、部分罕见病、PGx | 复杂区域需长读长或正交验证 |
| G03 chrY | Y 非重组区 callable bases、SNP 支持/反对 read、参考树/坐标版本 | 父系谱系 | 未测到下游分支不能伪称阴性或精确共祖年份 |
| G04 mtDNA | 线粒体 depth、NUMTs 干扰和异质性处理 | 母系谱系 | 可判读部分与未判读部分分开 |
| G05 外部群体/亲属 | 合法授权的第二人/群体样本、phasing、LD 与祖源匹配 | IBD、古 DNA、PRS 比较 | 只有单人 WGS 不能凭空形成寻亲库/GWAS |
| G06 文献匹配 | 论文是否用 WGS/芯片/WES/古 DNA，队列 N、祖源、参考构建、预测验证与数据版本 | **全部方向的可转移结论** | 数据类型不符时只能借鉴算法，不能移植实证结论 |
| G07 表型与临床 | 疾病诊断信息、真实睡眠/营养表现、药史、独立临床或随机试验证据 | 医学、药物、睡眠、营养 | 只有基因型不能推出个体医疗或生活方式处方 |

> 注意：深度或 Q30 不能代表全基因组所有区域均可判读。覆盖与准确率要分位点、变异种类和参考版本审核。

## B. 研究方向总表：当前关联论文和 GitHub 数量

表中 **专项** 指针对该研究域直接实现核心方法的现有候选项目数；其余通常是通用 QC/统计/变异工具。专项 ≠ 真实运行通过 ≠ 临床验证。

| ID / 研究维度 | 本项目已收录论文 | 已关联 GitHub（其中专项） | 数据合格时能研究到哪一步 | 继续深入必需资料 |
|---|---:|---:|---|---|
| **D01 原始 WGS/小变异与 QC** | 5 | 12（约 7） | FASTQ 质控、有效覆盖与 GIAB/CMRG 限定区域 SNV/Indel benchmark | PCR-free/平台、有效深度、单基因可判读区与统一真值 BED |
| **D02 SV/CNV/STR** | 5 | 8（4+1 个 SV 比较工具） | 部分 DEL/INS/CNV/STR 候选；Truvari 可评价但不是 caller | 按 SV class 的真值/复杂区/长读长，许可限制 |
| **D03 父系 Y** | 2 | 5（3） | 单倍群、末端分支、private SNP 候选 | 多个父系样本/校准/家谱 |
| **D04 母系 mtDNA** | 5 | 5（3 个 mtDNA 专项） | 单倍群 + 同质/异质变异候选；NUMTs/污染要过滤 | mtDNA 实际深度、独立 caller、靶向验证 |
| **D05 常染色体 IBD/亲缘** | 1 | 3（1） | 单人可研究部分 HBD/ROH；人际 IBD 需其他样本 | 授权多人 phased GT、无缺失等位及匹配 cM 遗传图谱 |
| **D06 古 DNA/群体与迁徙** | 3 | 5（3） | 古今群体模型、IBD 与祖源假说 | AADR、时空样本与竞争模型 |
| **D07 罕见病/致病变异** | 4 | 5（2） | 功能注释及候选致病排序 | ClinVar/ACMG、表型和确证 |
| **D08 隐性遗传病携带/生殖风险** | 8 | 5（含 2 个有使用限制的专项候选） | 候选致病变异及部分复杂假基因位点；阴性无法排除携带 | ACMG 2021/2024、残余风险、正交验证、配偶筛查；Gauchian 原研究和正式回应 |
| **D09 药物基因组学** | 3 | 4（2） | 部分代谢基因型和用药指南关联 | 复杂基因分型、药史/临床 |
| **D10 复杂疾病 PRS** | 5 | 5（4） | 应用外部模型计算个人分数 | 祖源匹配、独立队列校准 |
| **D11 睡眠/晨晚型** | 4 | 3（0 个已验证睡眠处方专项） | 已发表评分的晨晚型/时长/失眠遗传倾向；不预测个人入睡钟点 | 有效祖源匹配 PGS、位点 match rate、睡眠日志/可穿戴表型 |
| **D12 营养/饮食/代谢** | 2 | 3（0 个已验证饮食处方专项） | 部分代谢位点及群体关联 | 表型与随机对照试验 |
| **D13 运动/体质等复杂性状** | 5 | 3（0 个已验证运动处方专项） | 身体活动行为 GWAS/已有 PGS；VO2max 训练反应需要独立训练队列复现 | 真实活动/训练前后表型、外部祖源验证 |
| **D14 HLA/免疫复杂基因区** | 1 | 3（1 个 HLA-I 专项） | OptiType 可进行 HLA-I 候选分型；HLA-II 仍缺专项证明 | HLA 区域质量、临床真值；HLA-II 需另找工具/论文 |
| **D15 甲基化/转录组/微生物组** | 2 | 0（当前普通短读长 WGS 输入无专项直接适配） | 不能由普通短读长**人类 DNA WGS**直接测动态甲基化/基因表达/完整菌群；原生长读长平台有修饰检测例外 | WGBS/EM-seq/ONT native signal、RNA-seq、真实微生物样本宏基因组 |

## C. 论文 → 工具 → 可研究程度：首轮真实对应

| 维度 | 已验证题录的原始来源（P-ID，见注册表） | 对应现有 GitHub 工具（项目名称） | 不能越过的科学界限 |
|---|---|---|---|
| D01 | P001 Sarek；P002 DRAGEN；**P042 GIAB CMRG 273 基因、P043 ACMG 2021 测序技术标准、P044 PCR-free 约40×原始技术比较** | nf-core/sarek、fastp、FastQC、MultiQC、BWA-MEM2、samtools、bcftools、mosdepth、DeepVariant、GATK、hap.py、dna-seq-benchmark | 先区分 raw Gb bases 与磁盘 GB，再核有效深度/≥10×/20× callable；GIAB + 对应 BED 仅代表有真值部分，难基因须 CMRG；商业 40× 非自动过关；DRAGEN 不列作自由源码 |
| D02 | P002 DRAGEN；P003 Manta；**P026 GIAB SV、P027 Truvari、P028 ExpansionHunter** | samtools、bcftools、GATK、Manta、DELLY、CNVkit、ExpansionHunter（**PolyForm Strict**）、**Truvari（MIT；SV 比对而非 caller）** | GIAB 主要验证 ≥50 bp DEL/INS，不含全部 SV；重复扩增与复杂区受限，且部分源码限制修改/分发 |
| D03 | P005 **Yleaf 原文 msy032（旧 msy080 为勘误）**；P006 Y-LineageTracker | samtools、bcftools、Yleaf、Y-LineageTracker、yhaplo | 分支树不证明具体历史人物 |
| D04 | P007 Haplogrep 3；**P029 MToolBox、P030 gnomAD mtDNA、P031 WGS vs targeted、P032 mtDNA callers benchmark** | samtools、bcftools、Haplogrep3、**MToolBox（GPL-3.0）、Mutserve（MIT）** | 需单独核查 mtDNA depth、NUMTs、污染和 heteroplasmy CI；Mutserve VCF 不含 indels；母系 haplogroup 不是疾病诊断 |
| D05 | P008 hap-IBD | bcftools、hap-IBD（Apache-2.0）、PLINK2（GPLv3） | hap-IBD 输入为**无缺失、完整 phased GT 的多人 VCF 和相同构建的 cM map**；单人只可研究自身 HBD/ROH，不能发现陌生亲属 |
| D06 | P009 ancIBD；P010 qpAdm；P011 2025 迁徙综述 | nf-core/eager、ancIBD、ADMIXTOOLS2、hap-IBD、PLINK2 | 需要参照群体；遗传相似不等于个体迁徙 |
| D07 | P004 VEP；P012 ACMG；P013 ACMG SF；P021 Exomiser | bcftools、DeepVariant、GATK、VEP、Exomiser | 变异注释不是诊断 |
| D08 | P012 ACMG；P013 ACMG SF；P021 Exomiser；**P033 ACMG Carrier 2021、P034 ACMG Lab 2024、P035 InterVar、P036 Gauchian 质疑、P045 Gauchian 开发者正式回应** | bcftools、VEP、Exomiser、**InterVar（非商用免费）、Gauchian（PolyForm Strict）** | 变异阴性仍有残余风险；Gauchian 的漏检研究与开发者的低覆盖/适用条件回应应并列核查；争议尚无本项目独立复现，不能单方盖棺定论 |
| D09 | P014 PharmCAT；P015 PharmCAT 临床支持；**P024 StellarPGx** | bcftools、VEP、PharmCAT、**StellarPGx（WGS BAM/CRAM）** | CYP2D6 SV/CNV 不能仅从 PharmCAT 普通 VCF 研究模式直接可靠分型；先专项 caller，再解释；不得自行改药 |
| D10 | P016 PRS-CSx；P017 跨人群；P018 eMERGE；P022 All of Us 2026；**P025 PGS Catalog Calculator** | PLINK2、PRS-CS、PRS-CSx、bigsnpr、pgsc_calc | **pgsc_calc 官方 README 当前明确不支持 WGS 数据直接输入**；需把 WGS 转成符合其文档的完整、可信、imputed/兼容基因型输入，不能仅将 variants-only VCF 改名；一人可在适配后计算，不能训练或校准预测准确率 |
| D11 | P019 697828 人晨晚型 GWAS；P017 PRS 跨祖源综述；**P037 446118 人睡眠时长 GWAS；P038 芬兰 33493 人睡眠 PRS 可迁移性** | PLINK2、bigsnpr、pgsc_calc（Apache-2.0，**官方当前不支持直接以 WGS 数据作为目标输入**） | 晨晚型、睡眠时长、失眠是不同 phenotype；25 分钟是晨晚型遗传评分两端人群的平均差异，不能预测具体个人睡觉钟点 |
| D12 | P020 DIETFITS 随机试验；P017 PRS 综述 | PLINK2、bigsnpr、pgsc_calc | **DIETFITS 未支持预设基因型能挑选较优减重饮食**，必须收录阴性证据 |
| D13 | P017 PRS 综述；P022 All of Us 2026；**P039 活动行为 GWAS 703901 人；P040 HERITAGE VO₂max 训练 473 人；P041 Predict-HIIT n507** | PLINK2、bigsnpr、pgsc_calc | 活动/久坐行为 ≠ 身体素质 ≠ 训练反应；HERITAGE 21 SNP 样本内 49% 方差解释率**不是独立预测准确率**，不能生成个人训练处方 |
| D14 | **P023 OptiType（HLA-I）** | samtools、bcftools、**OptiType** | 已找到 HLA-I 的直接 WGS 方法与代码；**不覆盖 HLA-II 或真实临床确证** |
| D15 | **P046 原生长读长甲基化方法比较；P047 宏基因组科学综述；NHGRI RNA-seq 官方定义另计为标准资源** | **普通短读长人类 DNA WGS：无可直接测动态组学的既有目录工具** | 区分原生 ONT 甲基化 signal 与普通 Illumina/MGI FASTQ 碱基；普通人类 DNA WGS 非人 reads 只是需排污染的有限线索，不能得到完整菌群画像 |

## D. 新增一手证据核查（2026-11-21）

已完成 [G4 六领域论文×原始 WGS 输入×代码真实契约审计](cross-domain-evidence-audit.md)。该审计核对 **Exomiser（临床 HPO）、PharmCAT + StellarPGx（CYP2D6 BAM/CRAM）、pgsc_calc（WGS VCF 不原生支持）、DIETFITS 2018 阴性 RCT、ancIBD（古 DNA 已相位填补）及 OptiType（HLA-I）**；记录源码版本、许可证和论文原始样本设计；**没有实际运行个人/公共 WGS**。

**对原计划的两项技术修正**：
1. `pgsc_calc` 的官方 README 显示 **WGS 的 variants-only VCF 不是原生合格输入**，需要依官方方法准备完整基因型（涵盖纯合参考位点并核验匹配率），不是通常所说“给一个 VCF 就能算 PRS”。
2. CYP2D6 的可靠分型涉及 SV/CNV，保留 BAM/CRAM 使 StellarPGx 等专项工具有用；PharmCAT VCF-only CYP2D6 模式属研究尝试，不能供临床决策。HLA-I 有真实专项 OptiType 软件及论文，HLA-II 能力待补。

## E. G5 横向证据核查（D02/D04/D08）

详见 [G5 SV/STR、母系 mtDNA、隐性携带者原始论文×开源代码×许可证审计](cross-domain-evidence-audit-g5.md)：

- **D02**：NIST/GIAB 19 种方法整合的 12,745 个 ≥50 bp 高可信插入缺失，不是全人类全部 SV；Truvari 是 SV VCF 比对工具而非检测器；ExpansionHunter 实际为 **PolyForm Strict** 许可，不应直接作为可自由迭代商业开源底座。
- **D04**：MToolBox/Mutserve 对原始 WGS BAM/CRAM 有互补价值；56,434 人 gnomAD 研究表明 mtDNA NUMTs、污染、覆盖率和低异质性误报需要特别处理。
- **D08**：2021/2024 ACMG 指南明确 WGS 的阴性残余风险和复杂病原位点补检；InterVar 仅非商业使用免费，Gauchian 不允许自由修改/分发，且独立 2025 研究报告漏检，而开发者正式回应认为部分比对数据覆盖不足；须同时审查测试条件。

**许可分类重大修订**：GitHub 仓库存在性目前 39/39，但其中至少 T16/T39（PolyForm Strict）及 T38（非商用免费/需额外授权）不是可自由商用/再分发的普通开源许可证。因此“39 个可直接复用开源项目”这一表述不成立，所有候选必须先以 LICENSE 审计分组。真实程序运行仍 NOT_RUN。

## F. G6 现代 IBD/睡眠/运动论文—源码适配核查

新增 [G6 三方向完整审计](cross-domain-evidence-audit-g6.md)。与此前 G4/G5 不同，本轮**未增加 GitHub 仓库数量**，而是对 hap-IBD、PLINK2、pgsc_calc 的真实输入/许可证及现有论文可迁移性进行核查。新增 5 篇文献 P037–P041（G6 当时累计 41 篇）；G7 根据确有缺口继续增加 P042–P047，目前总数 47 篇，工具仍 39 个。D05 的人际 IBD 需要多人授权及相位基因型，单人 HBD 不等于发现近亲；D11 需区分晨晚型与睡眠时长；D13 活动习惯 GWAS 不能解释具体训练方案反应。

## G. G7 全矩阵质量与跨模态审计（2026-11-21）

详见 [G7 全 15 域证据一致性审计与 D01/D15 详情](cross-domain-evidence-audit-g7.md)。重新定位 D01 的 GIAB/CMRG 变异真值和 G00–G07 质量门槛；**普通短读长 DNA WGS 不能直接测组织 RNA 表达/甲基化/肠道微生物群**，但原生 ONT 信号可直接测修饰、WGS 中非人 reads 仍可能提供非临床微生物线索，不能使用绝对化“一切 WGS 均不可测”的表述。Gauchian 2025 负证据已补开发者正式回应 P045。该审计仅 E1 文献/代码层级，WGS E2 `NOT_RUN`。

## H. G10：15 域代表论文的 assay、队列、源码与外推边界深度核验（2026-11-21）

**[查看 G10 全 15 域代表论文方法审计](cross-domain-method-evidence-audit-g10.md)**。覆盖 D01–D15 每域≥1 篇已登记的一手 DOI/权威标准，并对应已有软件实际输入、单人 WGS 的可研究范围、额外队列/临床/其他 assay 前提与限制。**P005 Yleaf 原文 DOI 从误用的勘误 msy080 校正为 msy032**；PGS Catalog Calculator README 明示 WGS 目前不直接支持。15 域/47 P-ID/39 仓库数量不变；方法/E1 的真实性不等于源码 E2 全面运行，通过 G9 实测的仍只有 D01 chr20 1 Mb SNV/Indel。

## I. 用 4 个实例检验这套框架是否真正成立

**疾病**：高质量 SNV/Indel → [VEP 原文 P004](paper-register.md) 变异效应注释 → [ACMG P012](paper-register.md) 证据分级 → Exomiser 提出候选疾病基因 → 还需表型与临床确证。不是 `VCF → AI → 确诊`。

**PRS**：样本已有高质量基因型 + 公开 [PGS Catalog](https://www.pgscatalog.org/) 分数 → PRS-CSx/pgsc_calc 运行 → 仅获得按既有模型计算的风险指标；在不同祖源中还需独立队列校准，单人无法得到真实 AUC。

**睡眠**：2019 [697828 人 GWAS](https://doi.org/10.1038/s41467-018-08259-7) 支持晨晚型相关位点 → 利用适合祖源的权重做评分 → 不能预测准确入睡时点；需要实际睡眠记录。

**营养的反证**：[2018 DIETFITS 随机试验](https://doi.org/10.1001/jama.2018.0245) 609 名参与者的预设基因型模式**未显著改变**低脂/低碳饮食减重结果。不能只找支持营销报告的正向论文，负结果也应进入证据矩阵。

## J. 最小数据模型与后续复现策略

对每个实际研究问题保留这几个字段即可，无须额外开发项目管理系统：

`domain_id | question_id | gate_id | data_type/build/coverage | P-ID/DOI | paper_study_type/N/ancestry | required_reference_data | tools_and_commits | input/output | validation_method | evidence_grade | negative_evidence | claim_limit`

**不是**做 15×39 个任务笛卡尔积。只有真实论文、开源 README、代码支持某个用途时才建立关联；允许零项目、零论文，后续补齐。最优先补的是各个维度的**论文条件和可研究深度**，再为已经成立的研究问题复用工具。

已存在的 [HG002 技术基准](benchmark-hg002.md) 仍然有效，但它只验证 D01 的 chr20 小变异，不应因这一条实验阻断而把全部其他维度停下来。下一轮应按 D01–D15 的覆盖缺口，优先挑选代表性高证据论文与开源实现做跨领域核验，保证研究不偏向父系单个子题。
