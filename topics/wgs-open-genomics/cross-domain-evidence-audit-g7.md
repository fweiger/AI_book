# TOPIC-017｜G7：15 域证据一致性、WGS 质量准入与非直接组学测量（2026-11-21）

> **研究合同不变**：[Issue #72](https://github.com/fweiger/AI_book/issues/72) / [Draft PR #73](https://github.com/fweiger/AI_book/pull/73)。遵守数据质量→论文研究设计→个人可用结论→GitHub 现成代码四层关系。此次为文献/代码的静态核查与不一致修正，**没有任何基因组软件真实运行或临床验证**。

## 1. 交叉索引自检：不是所有已收录条目都已可运行

基于 GitHub PR 分支的 `paper-register.md` 和 `open-source-projects.md` 逐行核对：G6 时 **15 个 D 域、41 个 P-ID/不同 DOI、39 个 T-ID/不同 GitHub 仓库链接**；本轮新增直接必要的质量/反证/多组学文献为 P042–P047，更新后 **47 个注册来源、39 个源码仓库候选、15 域**。本目录的论文数量是策展范围，**既不是 PubMed 相关论文总数，也不是所有条目都全文检阅**。已确认有些源码采用非 OSI 许可，不能全部叫“可自由复用开源”。

15 域的静态映射核对：D01/D02/D03/D04/D05/D06/D07/D08/D09/D10/D11/D12/D13/D14/D15 **15/15 均有独立的行和质量限制**；但“行存在”只是 E0/E1 文档完整性，不等于每一域具备可独立执行且经过验证的端到端管线。数量跨行重复引用论文/工具，故**不得累计各行计数求全局唯一论文或工具数**。

## 2. D01：为什么“厂商称 30×/40× + 90–150 Gb”不是完整的科研质量合同？

| 技术维度 | 应索取或在原始数据上核查 | 当前能使用的现有源码 | 对应原始证据与限制 |
|---|---|---|---|
| 测序原始量 | `total bases in PF reads`、PE150/读长、FASTQ Q30、adapter、GC bias、library PCR-free、重复率 | [fastp](https://github.com/OpenGene/fastp) FASTQ → JSON/HTML；[MultiQC](https://github.com/MultiQC/MultiQC) 汇总 | [PCR-free vs PCR WGS 2022, P044](https://doi.org/10.1097/MD.0000000000028972) 用 NA12878 多种文库/下采样比较。样本/平台研究结果**不代表任一厂商保底精度** |
| 比对与可判读覆盖 | ref genome build/fasta hash、去重后有效 depth、MAPQ、`fraction >=10×/20×/30×`、sex chromosomes/chrY/chrM、低复杂区域与参考缺口 | [samtools](https://github.com/samtools/samtools)、[mosdepth](https://github.com/brentp/mosdepth) BAM/CRAM → chromosome/region depth & coverage histogram | mosdepth README 明确可从 BAM/CRAM 产生 per-base/per-region/coverage thresholds；**平均 depth 不替代每个位点 callable status** |
| SNV/Indel 调用 | 针对数据平台正确模型/参考，逐位点 DP/GQ/AD/MQ、过滤/NO_CALL、是否含 reference homozygotes/gVCF | [DeepVariant](https://github.com/google/deepvariant) BAM/CRAM → VCF/gVCF、[nf-core/sarek](https://github.com/nf-core/sarek) | 单人 variants-only VCF 缺乏“未记录位置已被正确判参考”的证据；不能直接用于所有 PRS/IBD |
| 常规 benchmark | GIAB 对应样本、`NISTv4.2.1 / build / confident BED / truth VCF`，在相同有效区域分别计算 SNV 与 Indel precision/recall | [Illumina/hap.py](https://github.com/Illumina/hap.py) VCF+VCF+BED+reference；[GIAB](https://www.nist.gov/programs-projects/genome-bottle) | [NIST FAQ](https://www.nist.gov/programs-projects/faqs-genome-bottle)：benchmarks 中不等于整个基因组都有“真值”；BED 外不能算 TN/阴性，也不等于变异不存在 |
| 复杂医学基因 | 专项 `gene-by-gene callable intervals`、假基因/重复段、难比对区、SV class、位点检测证据 | 现有通用 caller/基准仅部分适配，不能宣称全部覆盖 | [GIAB CMRG 2022, P042](https://doi.org/10.1038/s41587-021-01158-1) 为 **273 个复杂医学基因**建立单独 benchmark；原通用基准遗漏多种困难区域 |
| 临床转移边界 | 实验室检测有效区域、变异类型的 analytical validation、已知/未知遗传病和群体效度 | 不能从“软件跑通”推定 | [ACMG 2021 NGS 技术标准, P043](https://doi.org/10.1038/s41436-021-01139-4) 按样本/用途规定 QC、覆盖限制与必要确认 |

**必须区分单位与分母**：`90–150 Gb` 如果厂商指 *gigabases*（测序碱基），不是 `90–150 GB` 文件磁盘占用；人类单倍体参考约 3.1 Gb。`read bases / reference length` 只能估算原始覆盖倍率，不能等同过滤后有效/可调用深度。尤其与 chrY、mtDNA、HLA、CYP2D6 等专项区间检出率不可以互换。

**已核实的论文级定量例子，不是个人实测**：P044 用 PCR-free vs PCR-based 的 NA12878、MGISEQ-2000 平台及约 40× 下采样比较，给出复杂区域测量差异。作者报告在其样本下 ACMG 59 基因的 **≥10× 全编码覆盖比例** PCR-free 为 98.30%，PCR-based 为 93.22%；对该 59 基因列表使用 ≥20× 标准时又降至 79.66% vs 57.63%（具体范围依论文定义）。**这不是所有消费者 40× 数据的真实参数**，恰好证明应按覆盖阈值/基因逐项判断。

## 3. D15：并非“所有 WGS 都无法测甲基化”，而是平台与 assay 不同

| 生物学问题 | 普通 Illumina/MGI **未做甲基化化学处理的短读长人基因组 DNA WGS**能做 | 不可直接可靠测量 | 需要的不同 assay / 一手依据 |
|---|---|---|---|
| **当前 DNA 甲基化 / 表观年龄** | 可研究基因序列与表观状态的遗传关联，仅能提出遗传假设 | 当前个体 CpG 甲基化水平、组织特异表观年龄 | WGBS/EM-seq/EPIC array；**原生 ONT/PacBio 某些条件下可直接检出修饰**，不同于普通短读长 WGS。[长读长修饰评测 P046](https://doi.org/10.1186/s13059-024-03207-9) |
| **当前 RNA 表达 / 剪接体数量** | DNA 中可研究调控位点、预测性功能影响 | “哪一个基因今天实际表达多少”的测量结果 | **RNA-seq**（NHGRI 官方 [RNA-seq 定义](https://www.genome.gov/genetics-glossary/RNA-seq)），并须对应组织、时间、表型 |
| **肠道菌群与临床感染** | 人体 WGS 如果有非人来源 reads，只能作为污染/感染等**极有限、需确认的线索**，而不是绝对“完全无微生物信号” | 对粪便群落的可靠物种/菌株定量、功能组成，以及临床病原诊断 | 独立采集相应组织/粪便样本，16S 或 shotgun metagenomic DNA/RNA sequencing、host depletion 与阴阳性对照；[宏基因组综述 P047](https://doi.org/10.1007/s00335-021-09889-x) |
| **蛋白质水平/代谢物/生理年龄状态** | 可定位与蛋白/代谢性状相关的 DNA 位点或假说 | 当前蛋白丰度、血浆代谢物浓度、近期疾病/营养状态 | proteomics、metabolomics、临床实验室与持续监测数据 |

**非常关键的表述修正**：
- 过去矩阵写“D15 甲基化/转录组/微生物组 普通短读长 WGS 无直接测量能力”，其精神大体正确，但容易让人误解“所有 WGS 平台不行”或“生物样本里的非人 reads 绝对不存在”。严格说应限定为**普通短读长、人类 DNA、未处理的常规测序 assay**。原生纳米孔测序可观察电流信号中的修饰；但如果交付只剩 **FASTQ 中标准 A/C/G/T 碱基字母**，就不能凭序列文本自动恢复原始电流/修饰信息。
- D15 的 0 个“直接适配标准短读长 WGS”的专项软件不表示科学上没有 RNA-seq、甲基化或宏基因组开源工具，而是**这些工具需要不同的原始生物学测量**，不应为了扩大 39 项 WGS 工具库将其混入可执行列表。

## 4. 额外的跨域学术争议纠偏：Gauchian（D08）

此前 G5 文档引述 **2025 年 [Tayebi et al., DOI 10.1038/s42003-025-08059-y](https://doi.org/10.1038/s42003-025-08059-y)**，论文报告经验证 GBA1 样本中某些罕见变异/重组可能漏检；这属于**研究作者的具体数据/条件结论**，不能未经核查上升为“所有 30×/40× Gauchian 都不可靠”。开发方同期 [Toffoli et al. 正式回应, P045 DOI 10.1038/s42003-025-08060-5](https://doi.org/10.1038/s42003-025-08060-5) 指出部分比较采用了不符合预期的旧低覆盖（约 <10×）数据，而其工具目标数据约 30×。

因此对 P036/P045 应记录为**有争议的性能陈述/存在特定条件的负证据，独立充分覆盖的真值复核 NOT_RUN**；两篇论文都保留，不能将任一方的单独声明等同独立验收。与此无关的“Gauchian 使用 PolyForm Strict”版权/许可问题可直接以其 LICENSE 作独立判断。

## 5. D01–D15 全域交叉审计检查点

| 维度 | 现有最低研究输入/外部数据 | 关键已登记 P-ID / 工具 | 目前可可靠陈述 | 主缺口与等级 |
|---|---|---|---|---|
| D01 WGS QC | FASTQ、BAM/CRAM、build、覆盖与 GIAB | P001/P002/P042/P043/P044；fastp/mosdepth/DeepVariant/hap.py | 按区间做 QC、短变异基准方法成立 | 未真实跑 HG002；E1/PARTIAL |
| D02 SV/STR | 配对 read、有效复杂区、各类别 truth | P026–P028；DELLY/Truvari/ExpansionHunter | 一部分 DEL/INS/STR；分类型基准 | 长读长/STR 真值与软件许可；E1 |
| D03 父系 Y | chrY 高可判读 SNP 与真实参考树 | P005/P006；Yleaf/Y-LineageTracker | 单人分支分类可作为候选，家谱需其他证据 | 公共男性样本复现；E1 |
| D04 母系 mtDNA | mtDNA depth、NUMTs、AF、污染 | P007/P029–P032；Mutserve/MToolBox | 母系单倍群、异质性候选分开处理 | 真值和组织一致性；E1 |
| D05 IBD/亲缘 | 多人合法授权、phased GT、遗传图谱 | P008；hap-IBD | 单人 HBD，双人以上可研究 IBD | 多样本真值、短片段假阳性；E1 |
| D06 古 DNA | 外部古样本、时期/地点、相位及对照 | P009–P011；ancIBD/ADMIXTOOLS | 群体关系/混合模型有研究价值 | 不能给私人祖先姓名；E1 |
| D07 罕见病 | 高质量变异、HPO、病例证据 | P004/P012/P013/P021；VEP/Exomiser | 候选变异排序 | 未临床确认，健康人不能复现病例准确率；E1 |
| D08 隐性携带 | callable 各基因、复杂变异、临床规范 | P033–P036/**P045 回应**；VEP/InterVar/Gauchian | 有候选，阴性有残余风险 | Gauchian 负证据有正式回应；E1/PARTIAL |
| D09 PGx | 星型等位/拷贝数/BAM/CRAM | P014/P015/P024；PharmCAT/StellarPGx | 药物基因型研究 | 特别是 CYP2D6 VCF-only 限制；E1 |
| D10 PRS | 合格常染色体基因型、模型和参考 | P016–P018/P022/P025；pgsc_calc | 合格模型上的相对分数 | WGS variants-only VCF 不原生支持；E1 |
| D11 睡眠 | 评分 SNP 与真实可穿戴/睡眠日志 | P019/P037/P038；PLINK/bigsnpr | 群体晨晚型等倾向 | 不可预测个人钟点；E1 |
| D12 饮食 | 对照 RCT 与个人表型 | P020；通用 SNP 工具 | 可研究基因型与干预交互 | DIETFITS 特定基因型负结果；E1 |
| D13 运动 | 训练表型、运动强度、祖源模型 | P039–P041；PLINK/bigsnpr | 运动行为/反应的假设研究 | 样本内 49% ≠ 外推效果；E1 |
| D14 HLA-I | HLA 区域有效 reads/数据库 | P023；OptiType | 部分 HLA-I 候选分型 | 不覆盖 HLA-II/临床配型；E1 |
| D15 非直接组学 | 不同组织/不同 modality assay | P046/P047；当前 WGS 目录无可直接适用软件 | 对 **普通短读长人类 DNA WGS** 可判定缺少直接测量 | ONT 原生修饰/非人 reads 需要例外分类；E1 |

**完整性状态**：15/15 行均能用上游数据门槛约束论文及工具，属于**结构 PASS、科学方法 E1/PARTIAL**。表中 47 个 P-ID 与 39 个 T-ID 经全局去重；单行多次引用不重复计数。没有进行 E2/真实基因组程序运行，不能对个人 WGS 提供实际准确率结论。

## 6. 现存问题与下一步
- **有明确来源的修复**：D01 无医学困难区基准、D15 的绝对式“不能测”、P036 忽视 P045 正式回应等问题已在本文件指出；要同步回主矩阵和论文注册表。
- **未做**：41+ 条研究的全部全文逐页审计、39 个 GitHub release 的所有依赖许可证、机器运行、外部队列验证和个人诊断，均仍 E1/PARTIAL 或 E2 NOT_RUN。
- **下一步唯一候选**：对用户将来采购的任一 30–40× WGS 交付建立**最小数据质量验收清单**与对应开源输出映射（可做静态 mock/公共数据），并优先选择 NIST GIAB HG002 的 **D01** 实际区域内基准或高价值 D09 PGx 公开参考作 E2；若执行环境仍无 Docker/DNS，则不扩大运维，先提供可迁移的纯命令/输入契约。
