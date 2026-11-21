# TOPIC-017｜G4：跨领域论文—原始 WGS 输入—现成代码实质审计（2026-11-21）

> 规范 Issue [#72](https://github.com/fweiger/AI_book/issues/72)；[Draft PR #73](https://github.com/fweiger/AI_book/pull/73)。**研究主线：数据质量 → 论文方法与所需外部数据 → 个人可得分析深度 → GitHub 开源实现。**
>
> **审计等级：**本轮已阅读部分论文开放全文（Exomiser/Genomiser 2025、DIETFITS 2018、ancIBD 2024 的研究方法/结果章节）和其余论文的摘要/公开方法介绍，以及 GitHub 仓库 README/LICENCE；**没有实际执行 WGS 软件，没有测个人 DNA**。文中各百分比是**论文作者报告的队列结果**，不代表本研究复现。对 DOI/源码引用均以本轮读取的出处链接为准。

## A. 方法与输入证据对照（六个实质案例）

| 审计ID / 维度 | 权威直接论文（数据与样本） | 开源实现与真实输入 | 原始 30–40× WGS 本人可做 | 关键阻断与科学上限 |
|---|---|---|---|---|
| **A01 / D07 罕见病** | [Cooperstein et al., Genome Medicine (2025), DOI:10.1186/s13073-025-01546-1](https://link.springer.com/article/10.1186/s13073-025-01546-1)：**386 名已确诊 UDN 受试者**（全外显子/全基因组）；GS 编码变异真值集中 **231 人、296 个诊断变异**，非编码集中 **39 人、60 变异**；GS 编码诊断变异 Top-10 从 **49.7% 优化至 85.5%** | [exomiser/Exomiser](https://github.com/exomiser/Exomiser)，已核最新版 release **15.1.0（2026-06-09）**；输入 **VCF + HPO 表型 + hg19/hg38 + 频率与预测数据库**；输出按表型/致病预测的候选变异/基因排序；**AGPL-3.0** | 若有高质量 VCF 与真实临床表型，可针对某个特定疑似遗传病整理候选，不应对无症状个人生成自动诊断 | 论文是**已确诊病例上的候选排序**，不是普通无症状人群发病预测；表型、家族分离/家系 VCF、ClinVar/ACMG、实验室正交验证不可省略；单人无症状并不复现论文试验 |
| **A02 / D09 药物 PGx** | [Sangkuhl et al., CPT (2020), DOI:10.1002/cpt.1568](https://doi.org/10.1002/cpt.1568)：介绍基因型及 star-allele 转换为 CPIC/DPWG 相关报告；[Twesigomwe et al., CPT (2021), DOI:10.1002/cpt.2173](https://doi.org/10.1002/cpt.2173)：**109 份 GeT-RM WGS** 验证 CYP2D6 分型，作者报告 **99% 与参考结果一致** | [PharmGKB/PharmCAT](https://github.com/PharmGKB/PharmCAT) release **v3.4.0（2026-07-14）**、**MPL-2.0**，输入标准化 PGx VCF → diplotype/表型、JSON/HTML 与指南关联；[SBIMB/StellarPGx](https://github.com/SBIMB/StellarPGx) release **v1.2.8（2025-02-12）**、**MIT**，输入索引好的高覆盖短读长 WGS **BAM/CRAM**，能分析 CYP2D6 复杂 SV/CNV，输出 star alleles | 具备真实 WGS CRAM 时可在研究环境做两段式：**StellarPGx CYP2D6 调用 → PharmCAT 的药物解释层**，按匹配的 reference/build 和官方流程导入 | **PharmCAT 官方明确反对将其 VCF-only CYP2D6 研究模式用作临床判断**；99% 是原论文特定 109 参考样本数据上的一致性，不代表另一个人的准确率；需要临床确证和药史，不能自行改药 |
| **A03 / D10 PRS / D11 睡眠** | [Lambert et al., Nature Genetics (2024), DOI:10.1038/s41588-024-01937-x](https://doi.org/10.1038/s41588-024-01937-x)：PGS Catalog 计算和祖源校准；[Jones et al. (2019), DOI:10.1038/s41467-018-08259-7](https://doi.org/10.1038/s41467-018-08259-7)：**697,828 人**晨晚型 GWAS，属于人群关联而不是个人作息 RCT | [PGScatalog/pgsc_calc](https://github.com/PGScatalog/pgsc_calc)，release **v2.3.0（2026-06-03）**、**Apache-2.0**，接受 **匹配模型等位基因的 PLINK / imputed VCF**；与 PGS Catalog 模型/祖源参考数据共同使用；**普通 WGS 的 variants-only VCF 不被原生支持** | 可以从 WGS 重新生成**参考位点信息完整且模型匹配**的兼容基因型输入；对有合格已发表权重的性状算相对分数或 z-score，并检查参考人群 | **不能“直接 WGS 变异 VCF → pgsc_calc → 有效评分”**：纯合参考位点未记录导致 score 位点 match rate 失败；需构建合格输入并验证匹配率，且以独立校准样本推断绝对风险；单人分数不能验证 AUC、不能自动给睡眠处方 |
| **A04 / D12 营养干预反证** | [Gardner et al., JAMA (2018) DIETFITS, DOI:10.1001/jama.2018.0245](https://doi.org/10.1001/jama.2018.0245)：随机分配 **609 名**超重但无糖尿病成年人，**481 人完成一年**；健康低脂/低碳减重分别约 **−5.3/−6.0 kg**；预先指定的三 SNP 基因型模式×饮食交互 **P=0.20**，基础胰岛素分泌×饮食交互 **P=0.47**（均未达显著） | 对应论文的这组 **基因型/饮食干预因果问题没有已核对的直接临床级开源“最佳饮食选择器”**；PLINK2/通用 VCF 工具仅能计算基因型，不能自动复现临床干预 | 可以判定相关 SNP 是否测到；如果有完整公开试验数据，可复制统计检验。单人 WGS 无法重新生成 609 人的随机干预结论 | **重要阴性证据**：对“遗传分型能确定低脂/低碳哪种更适合”的这一预设模式未得到支持；不等于否定所有营养遗传学；必须区分 SNP 检出与营养方案效果 |
| **A05 / D06 古 DNA/亲缘史** | [Ringbauer et al., Nature Genetics (2024), DOI:10.1038/s41588-023-01582-w](https://doi.org/10.1038/s41588-023-01582-w)：在 **4,248 个古代欧亚样本**应用；对大于 **8 cM** IBD，在有适当处理的 WGS **约 0.25× 及以上**、1240k 富集数据 **1× 及以上**条件下进行灵敏度研究，分析古代至六等亲关联 | [hringbauer/ancIBD](https://github.com/hringbauer/ancIBD)，**GPL-3.0**；输入已填补并完成相位的古 DNA 基因型概率/专用 HDF5，默认 GLIMPSE/1000G 参考；不是直接单人原始 FASTQ/VCF → 祖先人名 | 可以将现代个人数据按明确位点/祖源格式与**合法授权古群体参考数据**做谨慎比较；ancIBD 对古人-古人亲缘实验不是现代个人寻祖的直接即插即用程序 | 需要古代样本、定年/地理信息、相位/参考面板、群体偏差控制；论文的古人-古人 IBD 灵敏度不代表“今天某人与古墓主人具有可验证直系关系” |
| **A06 / D14 HLA-I 专项** | [Szolek et al., Bioinformatics (2014), DOI:10.1093/bioinformatics/btu548](https://doi.org/10.1093/bioinformatics/btu548)：HLA-I 的高分辨率分型方法；论文比较 RNA-seq、外显子与 WGS，属于算法基准，不是个人临床移植配型确认 | [FRED-2/OptiType](https://github.com/FRED-2/OptiType)，release **v1.5.0（2026-05-20）**、**BSD-3-Clause**；输入 **FASTQ 或 BAM（DNA 模式）**，输出 HLA Class-I 的结果 TSV | 提供了 D14 之前缺少的真实**专项工具**：在有足够 HLA 区域质量/正确参考数据时可计算 HLA-I 候选分型 | **不能泛化到所有 HLA-II**，也不能未经确认用于移植/药物过敏的临床决定；参考等位库与测序覆盖仍需明确 |

## B. 必须修正的两处过度乐观解释

1. 原 [主矩阵](evidence-capability-matrix.md) 曾将 `pgsc_calc` 与 WGS VCF 视作一般性直接输入。现在已从 [PGScatalog 官方 README](https://github.com/PGScatalog/pgsc_calc) 和 [输入文档](https://pgsc-calc.readthedocs.io/en/latest/how-to/prepare.html) 证实：**WGS variants-only VCF 需额外转换/补全参考位点，不是当前官方承诺的原生输入**；数据能力判定要考虑 `homozygous reference` 缺失、score match rate、祖源归一化。
2. 原 D14 仅列了 samtools、bcftools（通用底座），实际上有专项 [OptiType](https://github.com/FRED-2/OptiType) 且有 **WGS 支持论文**。因此 D14 不应再标“无已核实专项工具”，而应改为**HLA-I 专项至少 1，HLA-II 另核**。这个修正不表示 HLA-I 算法已在本项目成功运行。

## C. 软件许可、版本与真值范围（本轮真实检查）

| 源码 | 官方仓库/版本（读取时） | 许可证实际检查 | 真实运行 |
|---|---|---|---|
| Exomiser | [release 15.1.0](https://github.com/exomiser/Exomiser/releases/tag/15.1.0)，README Blob `0bba1b5e86f81cc140154c985640dec01b4469e4` | 根目录 **LICENCE** 为 AGPL-3.0（与普通 permissive license 不同；需遵守发行与服务网络条款） | NOT_RUN |
| PharmCAT | [v3.4.0](https://github.com/PharmGKB/PharmCAT/releases/tag/v3.4.0)，README Blob `35d7f7856d8cdea439ad0d2efe25b1f76cb46bbf` | **MPL-2.0** | NOT_RUN |
| StellarPGx | [v1.2.8](https://github.com/SBIMB/StellarPGx/releases/tag/v1.2.8)，README Blob `67d4c9ef0dfd124cce0bd8ec085a6e48d09f901d` | **MIT** | NOT_RUN |
| pgsc_calc | [v2.3.0](https://github.com/PGScatalog/pgsc_calc/releases/tag/v2.3.0)，README Blob `c48beb725cec8a1289dcca936f10f6d079b5c521` | **Apache-2.0**（其他依赖和参考数据另审） | NOT_RUN |
| ancIBD | [README 当前主分支](https://github.com/hringbauer/ancIBD)，README Blob `ed2c0dd750afddedcdd1c8f1595a48e60766c497` | **GPL-3.0**；未确认对应可复现 release | NOT_RUN |
| OptiType | [v1.5.0](https://github.com/FRED-2/OptiType/releases/tag/v1.5.0)，README Blob `29db5d35f190a95ff8c95d5cc3e42d790ac8dd70` | **BSD-3-Clause** | NOT_RUN |

> **注意**：记录 README blob SHA 和 GitHub release tag 只表示在核查时可追溯源文件/版本；本轮**未获取对应 release 容器 digest、未下载数据、未测试 release 代码运行。**

## D. 是否真正提高研究深度？

- **从可用性升级**：WGS 的 CRAM 而不只是筛选 VCF，对 CYP2D6 的结构/拷贝数信息极其关键；这就是 40× WGS 原始交付相对 SNP 面板/仅 PDF 报告的科学增量。
- **从“软件数”升级**：通过检查源码，确认 D14 HLA-I 实际有专项工具；也发现 D10 pgsc_calc 需要 WGS 中间数据转换。应优先修复这一类真正影响完整分析的断点，而不是盲目追逐 GitHub stars。
- **从相关变因升级**：睡眠 GWAS/营养 RCT/罕见病病例队列提供不同的统计证据层级。不能把 2019 人群关联研究包装成个人作息处方，也不能把 2025 已诊断病例中的 Top-10 比例作为无症状个人诊断准确率。
- **从家谱叙事升级**：古 DNA 软件 ancIBD 的 0.25×/8 cM/4,248 样本是古人之间 IBD 的验证场景，不能对一位现代个人直接转化为“祖先名单”。

## E. 当前结果/可复现性

- **PASS**：6 个领域案例有具体原始论文 DOI、样本/试验设计、源码项目、原始输入、真实许可/版本、方法限制；两个对个人 WGS 流程有实质影响的兼容性问题明确。
- **PARTIAL**：论文全文并非全部读取；不同 DNA 平台、祖源群体、SV/CNV/HLA 的实测准确率仍未跨平台评价；生物医学临床有效性不替代专业流程。
- **NOT_RUN**：实际任何人的 WGS、软件跑通、GIAB/PGx/HLA benchmark 和准确率重现。
- **唯一下一项建议**：将 G4 的已核结果反映至 15 域主矩阵、论文 P-ID 和 GitHub 项目清单，并选择各域关键的未覆盖数据契约（尤其 PGx CYP2D6 与 PRS WGS reference-call 恢复）准备公共基准级测试，而不构建新的软件平台。
