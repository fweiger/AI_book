# TOPIC-017｜WGS 数据质量 × 论文证据 × 研究方向 × 开源工具（主矩阵 v0.1）

> **核心逻辑：先审 WGS 能力，再审学术研究的输入条件及可达到的解释深度，最后匹配可复用的 GitHub 项目。** 父系 Y 只是研究域 D03，不是全专题总主线。
>
> **收录口径（2026-11-21）：15 个研究域、22 篇已登记的具体论文/指南/综述、32 个已核 GitHub 项目。** 本表中各方向的论文/工具数量是**当前登记且有关联的条目数**，不是全球全部论文/项目；同一篇论文和项目可跨域复用，不能把各行数字相加。论文原始题录见 [P-ID 注册表](paper-register.md)，项目详情见 [32 个 GitHub 目录](open-source-projects.md)。论文中使用芯片、古 DNA、人群统计或临床数据的结果**不能因消费者拥有一份 40× WGS 就自动复现**。

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
| **D01 原始 WGS/小变异与 QC** | 2 | 12（约 7） | 标准 SNV/Indel 调用、技术真值 benchmark | GIAB、匹配参考、有效深度 |
| **D02 SV/CNV/STR** | 2 | 7（4） | 结构变异与部分重复区候选 | 复杂区真值/长读长 |
| **D03 父系 Y** | 2 | 5（3） | 单倍群、末端分支、private SNP 候选 | 多个父系样本/校准/家谱 |
| **D04 母系 mtDNA** | 1 | 3（1） | 线粒体单倍群 | mtDNA QC、母系对照 |
| **D05 常染色体 IBD/亲缘** | 1 | 3（1） | 共享 DNA 片段与亲缘统计 | 至少两位授权样本/相位 |
| **D06 古 DNA/群体与迁徙** | 3 | 5（3） | 古今群体模型、IBD 与祖源假说 | AADR、时空样本与竞争模型 |
| **D07 罕见病/致病变异** | 4 | 5（2） | 功能注释及候选致病排序 | ClinVar/ACMG、表型和确证 |
| **D08 隐性遗传病携带/生殖风险** | 3 | 3（2） | 已知隐性病携带候选 | 伴侣检测/遗传咨询/补检 |
| **D09 药物基因组学** | 2 | 3（1） | 部分代谢基因型和用药指南关联 | 复杂基因分型、药史/临床 |
| **D10 复杂疾病 PRS** | 4 | 5（4） | 应用外部模型计算个人分数 | 祖源匹配、独立队列校准 |
| **D11 睡眠/晨晚型** | 2 | 3（0 个已验证睡眠专项） | 统计性晨晚倾向，非精确作息预测 | 有效 PGS、睡眠日志 |
| **D12 营养/饮食/代谢** | 2 | 3（0 个已验证饮食处方专项） | 部分代谢位点及群体关联 | 表型与随机对照试验 |
| **D13 运动/体质等复杂性状** | 2 | 3（0 个已验证运动处方专项） | 有条件的已有 PGS 倾向评分 | 长期表型和群体验证 |
| **D14 HLA/免疫复杂基因区** | 0 | 2（0 个专项） | 目前仅可做通用位点 QC | 专项 HLA caller、论文与真值 |
| **D15 甲基化/转录组/微生物组** | 0 | 0 | **普通短读长 WGS 无直接测量能力** | 必须增加其他检测技术 |

## C. 论文 → 工具 → 可研究程度：首轮真实对应

| 维度 | 已验证题录的原始来源（P-ID，见注册表） | 对应现有 GitHub 工具（项目名称） | 不能越过的科学界限 |
|---|---|---|---|
| D01 | P001 Sarek；P002 DRAGEN | nf-core/sarek、fastp、FastQC、MultiQC、BWA-MEM2、samtools、bcftools、mosdepth、DeepVariant、GATK、hap.py、dna-seq-benchmark | 需要 GIAB 真值；DRAGEN 是技术比较基准，**不算在 32 个开放项目中** |
| D02 | P002 DRAGEN；P003 Manta | samtools、bcftools、GATK、Manta、DELLY、CNVkit、ExpansionHunter | Manta 仓库已归档；短读长重复区受限 |
| D03 | P005 Yleaf；P006 Y-LineageTracker | samtools、bcftools、Yleaf、Y-LineageTracker、yhaplo | 分支树不证明具体历史人物 |
| D04 | P007 Haplogrep 3 | samtools、bcftools、Haplogrep3 | 仅直接母系；非全部母系族谱 |
| D05 | P008 hap-IBD | bcftools、hap-IBD、PLINK2 | 单人不能判断未知第二人 IBD |
| D06 | P009 ancIBD；P010 qpAdm；P011 2025 迁徙综述 | nf-core/eager、ancIBD、ADMIXTOOLS2、hap-IBD、PLINK2 | 需要参照群体；遗传相似不等于个体迁徙 |
| D07 | P004 VEP；P012 ACMG；P013 ACMG SF；P021 Exomiser | bcftools、DeepVariant、GATK、VEP、Exomiser | 变异注释不是诊断 |
| D08 | P012 ACMG；P013 ACMG SF；P021 Exomiser | bcftools、VEP、Exomiser | 检测阴性仍可能有残余风险 |
| D09 | P014 PharmCAT；P015 PharmCAT 临床支持 | bcftools、VEP、PharmCAT | 不自行改药，复杂 star alleles 需确认 |
| D10 | P016 PRS-CSx；P017 跨人群；P018 eMERGE；P022 All of Us 2026 | PLINK2、PRS-CS、PRS-CSx、bigsnpr、pgsc_calc | 一人可计算但不能训练或校准预测准确率 |
| D11 | P019 697828 人昼夜节律 GWAS；P017 PRS 外推综述 | PLINK2、bigsnpr、pgsc_calc | 目前三个都是通用评分底座，不是临床验证睡眠处方器 |
| D12 | P020 DIETFITS 随机试验；P017 PRS 综述 | PLINK2、bigsnpr、pgsc_calc | **DIETFITS 未支持预设基因型能挑选较优减重饮食**，必须收录阴性证据 |
| D13 | P017 PRS 综述；P022 All of Us 2026 | PLINK2、bigsnpr、pgsc_calc | 多基因评分不决定个人运动天赋或训练计划 |
| D14 | **专项论文缺口：0** | samtools、bcftools（仅通用底座） | 暂不以通用工具充当 HLA 分型 |
| D15 | **直接测量证据缺口：0** | **普通 WGS 本身不够** | 不伪造甲基化/表达或微生物测量 |

## D. 用 4 个实例检验这套框架是否真正成立

**疾病**：高质量 SNV/Indel → [VEP 原文 P004](paper-register.md) 变异效应注释 → [ACMG P012](paper-register.md) 证据分级 → Exomiser 提出候选疾病基因 → 还需表型与临床确证。不是 `VCF → AI → 确诊`。

**PRS**：样本已有高质量基因型 + 公开 [PGS Catalog](https://www.pgscatalog.org/) 分数 → PRS-CSx/pgsc_calc 运行 → 仅获得按既有模型计算的风险指标；在不同祖源中还需独立队列校准，单人无法得到真实 AUC。

**睡眠**：2019 [697828 人 GWAS](https://doi.org/10.1038/s41467-018-08259-7) 支持晨晚型相关位点 → 利用适合祖源的权重做评分 → 不能预测准确入睡时点；需要实际睡眠记录。

**营养的反证**：[2018 DIETFITS 随机试验](https://doi.org/10.1001/jama.2018.0245) 609 名参与者的预设基因型模式**未显著改变**低脂/低碳饮食减重结果。不能只找支持营销报告的正向论文，负结果也应进入证据矩阵。

## E. 最小数据模型与后续复现策略

对每个实际研究问题保留这几个字段即可，无须额外开发项目管理系统：

`domain_id | question_id | gate_id | data_type/build/coverage | P-ID/DOI | paper_study_type/N/ancestry | required_reference_data | tools_and_commits | input/output | validation_method | evidence_grade | negative_evidence | claim_limit`

**不是**做 15×32 个任务笛卡尔积。只有真实论文、开源 README、代码支持某个用途时才建立关联；允许零项目、零论文，后续补齐。最优先补的是各个维度的**论文条件和可研究深度**，再为已经成立的研究问题复用工具。

已存在的 [HG002 技术基准](benchmark-hg002.md) 仍然有效，但它只验证 D01 的 chr20 小变异，不应因这一条实验阻断而把全部其他维度停下来。下一轮应按 D01–D15 的覆盖缺口，优先挑选代表性高证据论文与开源实现做跨领域核验，保证研究不偏向父系单个子题。
