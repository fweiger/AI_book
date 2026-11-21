# TOPIC-017｜G5：结构变异、母系 mtDNA 与生殖携带者跨领域证据核查（2026-11-21）

> 规范研究任务 [Issue #72](https://github.com/fweiger/AI_book/issues/72)；源文件 [Draft PR #73](https://github.com/fweiger/AI_book/pull/73)。依用户批准路线：**实际 WGS 质量条件 → 一手论文设计/真值 → 研究能达到的深度 → GitHub 源码适用性/许可 → 未验证的边界**。
>
> 本轮只读公开论文/官方源码说明/许可证，并对现有研究文档作修改。**没有个人 DNA、没有公开参考 WGS 实际分析，没有临床诊断、没有精度复现。** 下面具体数字均为**原作者研究样本或 benchmark**，绝非本项目实验输出。

## 一、D02｜SV、CNV、STR：短读长 30–40× WGS 到底可测多深？

### 论文与基准
- **P026**：[Zook et al. 2020, *Nature Biotechnology*, DOI 10.1038/s41587-020-0538-8](https://doi.org/10.1038/s41587-020-0538-8)：NIST/GIAB 整合 **19 种方法**形成序列解析的 **12,745 个 ≥50 bp** 高可信 insertion/deletion，其中 7,281 insertion、5,464 deletion。**该基准不完整涵盖**大 CNV、倒位、易位、复杂重复和大片段重复区域；因此 12,745 不是“人类所有结构变异总数”。
- **P027**：[English et al. 2022, *Genome Biology*, DOI 10.1186/s13059-022-02840-6](https://doi.org/10.1186/s13059-022-02840-6)：Truvari 比较 SV 等位表示、benchmark 与跨样本合并；过度宽松合并会掩盖不同变异，污染频率估计。
- **P028**：[Dolzhenko et al. 2019, *Bioinformatics*, DOI 10.1093/bioinformatics/btz431](https://doi.org/10.1093/bioinformatics/btz431)：ExpansionHunter 用序列图与 BAM/CRAM read 支持对已定义的 STR 位点进行 genotyping；位点 catalog、read length 与扩增复杂度限制上限。
- 可选后续：[Dolzhenko et al. 2020, *Genome Biology*, DOI 10.1186/s13059-020-02017-z](https://doi.org/10.1186/s13059-020-02017-z) 提出 ExpansionHunter Denovo 用短读长全基因组探测未知 repeat expansion；**未进入本轮去重 P-ID 计数**。

### 已核源码及实际输入
| 实现 | 当前官方所述输入→输出 | 状态/许可 | 重要解释 |
|---|---|---|---|
| [Illumina/ExpansionHunter](https://github.com/Illumina/ExpansionHunter)（原 T16） | 均衡比对 BAM/CRAM + 参考 FASTA + repeat catalog → 目标 STR 估计 | **PolyForm Strict 1.0.0**；**不是允许自由修改和分发的常见 OSI 开源许可**；源码可见不代表可无约束地迭代 | 专项 STR 软件，部分扩增长度超过 reads/insert 的情况下需要正交或长读长验证；旧目录“32 开源”应改为 GitHub 可访问源码候选 |
| [ACEnglish/truvari](https://github.com/ACEnglish/truvari)（新增 T35） | **两个 SV VCF.gz + reference FASTA** → SV matching/benchmark/merge/stratified metrics | **MIT**（LICENSE 文件实核） | **它是比对与评价器，不是从原始 FASTQ/BAM 做 SV calling 的算法** |
| [dellytools/delly](https://github.com/dellytools/delly)（原 T14） | BAM/CRAM → SV VCF 候选 | 许可和实际运行另审 | 可以作为 caller 候选，不能把 caller 的 VCF 与真值指标混为同一输出 |
| [Illumina/manta](https://github.com/Illumina/manta)（原 T13） | 对短读长配对比对识别 SV | 仓库已归档；不作为当前积极维护主线 | 源码存在 ≠ 推荐生产/临床 |

### WGS 数据质量准入
- 原始数据必须有 **read length / paired-end / insert-size / depth distribution / mapping quality / duplicate ratio / alignment reference**，以及相应 SV class 的可判读区间。
- **不能拿 SNV 级别 Q30 或平均 40× 推断 SV/CNV/STR 检出率**。在重复区/片段重复区，短读长假阳性、漏检与位点大小偏差可能显著增加。
- **SV 必须按类型分层**：DEL、INS、DUP、INV、CNV、STR 分开报告，分别说明 GIAB truth BED 的覆盖范围；不以单一 recall 概括所有。
- 研究层级：L1 caller 候选 → L2 同一参考/真值的 SV F1（按 size/type） → L3 多平台/长读长对照 → L4 专项临床确认。**目前只到论文和数据规范 E1，E2 未运行**。

## 二、D04｜mtDNA：母系单倍群 ≠ 低频异质性可靠检出

### 论文与科研深度
- **P007**（已登记）：[Haplogrep 3, 2023, DOI 10.1093/nar/gkad284](https://doi.org/10.1093/nar/gkad284)：mtDNA haplogroup/quality QC，支持 VCF/FASTA 等；是母系分类，不是完整疾病诊断。
- **P029**：[Calabrese et al. 2014 MToolBox, DOI 10.1093/bioinformatics/btu483](https://doi.org/10.1093/bioinformatics/btu483)：从 WGS/WES 提取 mtDNA 读段，针对 NUMTs 处理，输出 mtDNA 变异、异质性比例和置信区间。
- **P030**：[Laricchia et al. 2022 gnomAD mtDNA, DOI 10.1101/gr.276013.121](https://doi.org/10.1101/gr.276013.121)：分析 **56,434 个 WGS 样本**，明确低异质性结果可能由 NUMTs、污染、误比对造成；**核基因组平均深度并不能代表 mtDNA 深度**，且血液/组织差异影响解释。
- **P031**：[WGS vs targeted mtDNA, *Mitochondrion* 2021, DOI 10.1016/j.mito.2021.01.006](https://doi.org/10.1016/j.mito.2021.01.006)：**1,499 名参与者**的 WGS 与线粒体靶向测序对比，适用于评估 WGS 与独立靶向技术的一致性。
- **P032**：[multiple mtDNA caller benchmark, *Frontiers in Genetics* 2022, DOI 10.3389/fgene.2022.692257](https://doi.org/10.3389/fgene.2022.692257)：用已知组成的人工 mtDNA 基准比较 Mutserve、MToolBox 等；不同异质性阈值及 caller 的错误率不同，不是“标称 1% 阈值就 1% 高可信检测”。

### 已核 GitHub 实现
| 实现 | 输入 → 输出 | 许可核验 | 未解决的风险 |
|---|---|---|---|
| [genepi/haplogrep3](https://github.com/genepi/haplogrep3)（原 T20） | mtDNA FASTA/VCF/txt → Haplogroup+QC | MIT | 需要与上游 variants 有效性、树版本匹配；不应用公共网页上传个人原始文件 |
| [mitoNGS/MToolBox](https://github.com/mitoNGS/MToolBox)（新增 T36） | WGS/WES reads + 核/线粒体参考 → mtDNA variants + heteroplasmy fraction 与 CI/单倍群 | **GPL-3.0**，仓库 `LICENCE.txt` 实核 | 早期依赖/GRCh37 默认及 NUMTs 处理需要复现与维护审计 |
| [seppinho/mutserve](https://github.com/seppinho/mutserve)（新增 T37） | **已排序索引 BAM/CRAM** → VCF.gz/txt，检测同质/异质 mtDNA | **MIT** | VCF 明确**暂不包含 indel**（README）；默认 `--level 0.01` 只是输出下限，**绝不是 1% 变异检测准确率保证** |

### 必需 QC 和证据深度
- 对同一 CRAM 明确 **chrM/MT contig 名称、rCRS/RSRS/GRCh37/GRCh38 参考与坐标、mtDNA 有效覆盖、污染与 NUMTs 风险**。
- 对 heteroplasmy 保留 `alternate_read_count / depth / strand_balance / AF / caller_filters / contamination / CI`；逐位点重复度和组织依赖性不能省略。
- 母系群组可以先凭高可信近同质位点分类；但**微小异质性可能是体细胞/组织依赖或测序伪影**，不能由母系 haplogroup 自行推导神经系统疾病和生理年龄。
- 深度 L1 Haplogrep classification → L2 Mutserve/MToolBox 双 caller 比较 → L3 靶向测序或合成异质性标准集验证 → L4 适格临床咨询/实验室复核。目前 E1，不声称 L2/L3 已做。

## 三、D08｜隐性遗传病携带者：WGS 不能把“无报告风险”当成“无携带”

### 两项官方指南和软件证据
- **P033**：[Gregg et al. ACMG practice resource (2021), DOI 10.1038/s41436-021-01203-z](https://doi.org/10.1038/s41436-021-01203-z)：ACMG 提出统一面向孕前/妊娠阶段提供 **Tier 3 相关常染色体隐性/X 连锁携带者筛查**；指出阴性结果只能降低而不能完全消除残余风险，风险受人群携带频率和位点检测率影响。
- **P034**：[ACMG laboratory technical standard (2024), DOI 10.1016/j.gim.2024.101137](https://doi.org/10.1016/j.gim.2024.101137)：**多种检测技术组合**才能覆盖不同变异类型/难以分型的基因；并非给一份 40× VCF 就能在所有基因上得到完整阴性结果。
- **P035**：[Li & Wang InterVar, *AJHG* (2017), DOI 10.1016/j.ajhg.2017.01.004](https://doi.org/10.1016/j.ajhg.2017.01.004)：根据 ACMG/AMP 2015 证据提供候选变异自动化解释和**人工调整步骤**；不等于无需人工就自动给出临床携带者结论。
- **P036（争议中的负向报告）**：[Tayebi et al. 2025, DOI 10.1038/s42003-025-08059-y](https://doi.org/10.1038/s42003-025-08059-y)：在其测试样本/设置中报告 Gauchian 对部分罕见变异与复杂重组可能漏报；**P045 开发者正式回应**：[Toffoli et al. 2025, DOI 10.1038/s42003-025-08060-5](https://doi.org/10.1038/s42003-025-08060-5) 指出部分旧低覆盖（<10×）数据并不符合约 30× WGS 的预期适用条件。两份来源必须并列留存，尚无本项目独立充分覆盖样本的性能结论。

### 输入/源码与开源许可风险
| 源码 | 输入 → 输出 | 实际许可证与限制 | 适用定位 |
|---|---|---|---|
| [Ensembl/ensembl-vep](https://github.com/Ensembl/ensembl-vep)（原 T25） | 变异 VCF → 功能/转录本注释 | 本轮未重审 LICENSE | 编码和剪接位点的候选注释，不自动鉴定携带者 |
| [exomiser/Exomiser](https://github.com/exomiser/Exomiser)（原 T26） | VCF+HPO 表型 → 可疑疾病变异排序 | AGPL-3.0；本轮沿用 G4 LICENSE 审计 | 对**已怀疑的表型诊断**有用，无症状携带者筛查不可直接复用其成功率 |
| [WGLab/InterVar](https://github.com/WGLab/InterVar)（新增 T38） | VCF 或 ANNOVAR 格式 → ACMG 证据辅助评级 | **README 明确非商业使用免费、商业需作者授权；依赖 ANNOVAR/OMIM 另有许可**。源码可见，**不能列为无条件可商用开源** | 仅候选辅助评级，必须逐条人工核实、特别是 VUS/基因-疾病关联 |
| [Illumina/Gauchian](https://github.com/Illumina/Gauchian)（新增 T39） | **标准约 30× 及以上** WGS BAM/CRAM + 参考 build → GBA1/GBAP1 复杂重组/拷贝数与已知变异候选 | **PolyForm Strict 1.0.0**，源码公开但**限制修改与分发**；不能当可自由迭代的 OSI 项目 | 针对假基因复杂区域的研究用对照工具；2025 独立论文报告漏检、开发者正式回应指出部分低覆盖测试不适用；**不能未经独立确认用于个人临床排除结论** |

### 携带者 WGS 准入与残余风险
- 必须逐基因建立清单：**全部高可信编码区域覆盖、单核苷酸/小 Indel 的 callable status、CNV/SV、重复扩增、复杂假基因、性染色体、剪接/深内含子位点**。厂商说“40× WGS”不能替代逐基因可检测范围与质量确认。
- “没有报告 P/LP 变异”与“所有基因未携带致病变异”是不同命题。建议记录 `screened_gene_panel / variant_types_assayed / analytical_sensitivity / population_carrier_freq / residual_risk`，并用实际实验室检出率/祖源参考估算阴性残余风险，不填假值。
- **夫妻共同携带**同一常染色体隐性病的风险解释，需要至少两人合法自主检测与医学遗传咨询；本项目只研究方法，不获取亲属或配偶 DNA。
- 深度 L1 SNV/Indel 候选 + VEP/ClinVar → L2 专项 CNV/伪基因位点 caller+人工证据判读 → L3 专业生殖筛查/必要 MLPA 或其他靶向技术验证 → L4 临床咨询、相关行动。**当前没有任何人实际携带者筛查结果。**

## 四、非常重要的许可归类纠偏（所有方向共用）
目前原目录总计**39 个已在 GitHub 确认存在的源码/项目仓库**（此前 34 个，本轮新增 T35–T39 5 个），**绝不等同 39 个均为 OSI 开源许可、可无限制商用/修改的项目**。已实际证实：
- **明确标准许可证的新增项目**：Truvari MIT、MToolBox GPL-3.0、Mutserve MIT。
- **源码公开但修改/商业使用受限**：InterVar 非商用免费/商业另授权；Gauchian PolyForm Strict（限制分发修改）；原 T16 ExpansionHunter 也是 PolyForm Strict。其余仓库未全量审许可证不得算作“开放许可证已核项目”。
- **适用性区别**：Truvari 是 SV VCF benchmark/merge，非 SV caller；Haplogrep3 是 mtDNA haplogroup classifier，非 mtDNA low-VAF caller；InterVar 是 ACMG 规则辅助、非承载临床全证据的判断者。
- 这对“从前人代码迭代”很关键：**先检查许可再评估复用成本**，源代码可见不等于允许分发衍生商业软件。

## 五、G5 证据层次与可复现性
- **E0 / PASS**：新增五个真实 GitHub 仓库存在性；README/LICENCE 已读；明确的参考数据格式/软件限制得到源码证据。
- **E1 / PARTIAL**：11 篇新增原始论文/行业专业标准的题录、关键方法与样本规模已由期刊、PubMed/PMC 或 ACMG/NIST 官方来源核对；全文方法审计并非所有论文均完成。
- **E2 / NOT_RUN**：未用 GIAB SV、公开合成 mtDNA 或 carrier truth data 跑实际工具；无独立 precision/recall。
- **E3/E4 / NOT_RUN**：未跨测序平台验证、未临床复核或咨询；不作任何个人诊疗建议。
- **局部限制**：先前 Docker/公网 DNS 影响本地大型 benchmark，不影响本轮横向质量—论文—项目研究。

## 六、当前研究范围与唯一后续方向
- 跨领域已审计 D02/D04/D08（本轮）及先前 G4 六案例。现有论文 P001–P036 去重登记；工具 T01–T39 为源码可见候选目录。
- **下一步优先对象**：检查剩余未深入的 D05 现代常染色体 IBD、D11 睡眠、D13 运动复杂性状的“真实个人数据可分析上限”；各选最强支持与反证，尽可能回到原始论文所用样本与模型，而不是为扩大项目总数重复添加工具。
- 将来如要做 E2，应优先安排三个不同类型的小规模**公开样本**：GIAB SV truth / 合成 mtDNA 异质性 / 确知的 carrier/复杂伪基因参考；每个实验只验证自己的适用位点，不混合到“全 WGS 精度”指标。
