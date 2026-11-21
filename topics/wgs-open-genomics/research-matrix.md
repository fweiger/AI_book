# TOPIC-017｜研究方向 × 技术深度 × 科学边界

> 本表中的“深度”是**可拓展研究层级**，不是当前已运行/验收结果。工具与论文详见同目录文件。

| 研究域 | 仅有一个人 WGS 能做 | 进一步深入需要什么 | 关键方法 / 项目 | 证据与失败边界 |
|---|---|---|---|---|
| 1. WGS 数据与技术质量 | 质量、覆盖、变异识别、chrY callable bases | GIAB HG002、另一技术平台 | Sarek / DeepVariant / GATK / hap.py | 无对照真值无法估算个人所有错误 |
| 2. 父系 Y 染色体 | 单倍群定位、未知下游候选 SNP | 高覆盖 chrY、其他父系样本、完整树/家谱 | Yleaf / Y-LineageTracker / yhaplo | 共组年代有置信区间；不能仅凭单倍群确定人名 |
| 3. 母系 mtDNA | 线粒体单倍群、部分杂合/异质性候选 | 高覆盖 mtDNA、母系亲属样本 | Haplogrep3 | 单一母系链不等于全部母系祖先 |
| 4. 常染色体亲缘 | 预处理分型、相位与校验 | 已授权的亲属/群体样本 | PLINK2 / hap-IBD | 一个人无法推断与未入库者的 IBD |
| 5. 古 DNA 与人口史 | 与公开古群体比较、可检验群体来源假说 | AADR/古样本质量、时空/参考队列 | nf-core/eager / ancIBD / ADMIXTOOLS2 | 样本偏差；古共祖≠墓主人直系祖先 |
| 6. 致病变异 | ClinVar/gnomAD 注释、候选评级 | 临床表型、实验室复核、家族共分离 | VEP / Exomiser / ACMG | 不能由 AI 自动确诊或指导治疗 |
| 7. 药物反应 | PGx 基因型、star allele 候选 | 医师、药史、表型、用药指南 | PharmCAT / CPIC | 不能自行改药，复杂 CNV 基因可能需补充检测 |
| 8. 复杂疾病 PRS | 在给定模型下计算理论评分 | 匹配祖源的模型与独立验证队列 | PLINK2 / PRS-CSx / pgsc_calc | 单人无法验证 AUC、校准与因果 |
| 9. 睡眠 / 营养 / 运动 | 查阅 GWAS 位点、建立审慎倾向假说 | 睡眠日志、表型/环境、临床数据 | PGS Catalog / bigsnpr + 文献 | 精确入睡时刻/专属食谱没有充分证据 |
| 10. SV/CNV/STR 与非编码区 | 短读长结构变异与部分重复序列候选 | 长读长、正交验证、复杂参考 | DELLY / CNVkit / ExpansionHunter | 短读长重复/复杂区域可能不可准确解析 |
| 11. 单细胞、转录、甲基化、微生物 | 标准 WGS 只能提供间接线索 | RNA-seq、甲基化组、单细胞组学等 | 其他技术，不可冒称 WGS 已测 | 不从 DNA 序列推断实时表达/衰老时钟/菌群 |

## 技术实验（仅公共/合成样本）
**优先最小实验规范已形成**：[HG002 chr20 实验契约](benchmark-hg002.md)；使用 Google 官方已比对的公开 35× HG002 chr20 BAM（故不进行 FASTQ 质控/原始比对）→ DeepVariant 单样本 WGS → hap.py 与 NIST v4.2.1 GRCh38 标准真值在规定 BED 上计算 SNP/INDEL Precision、Recall、F1、UNK。**本轮下载与实际变异计算 NOT_RUN；不能视作全基因组/chrY 基准。**

**记录**：公开 accession + 数据授权、BAM/CRAM/FASTQ hash、参考 GRCh38 FASTA hash、软件 image digest、CPU/RAM/硬盘预算、实际运行命令/错误及精度。不能用小染色体或合成数据的成功代替完整 30× WGS 验收。

## 个人 WGS 数据边界
现实实验中私人基因组数据应保留于访问控制的私有环境。本公开仓库**只记录开源工具说明、验证方法和经授权的公共样本结果**。
