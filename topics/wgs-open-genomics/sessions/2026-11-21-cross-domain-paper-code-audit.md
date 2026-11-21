# 2026-11-21 G4｜跨领域代表论文与 GitHub 输入兼容性审计

**规范任务**：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)；[Draft PR #73](https://github.com/fweiger/AI_book/pull/73)。协议锁定：`AI_tasks@f0e5ccb90c54265dcd07abb9a975c903eb031ccf`。

## 原目标与本轮动作
按用户指定的“WGS 数据质量 → 权威论文 → 研究维度与研究深度 → 现有 GitHub 软件”体系，核查**不同领域各一份代表性直接证据**，尤其真实样本输入/参考构建、论文 cohort N、研究结论能否直接迁移到单人 30–40× WGS、软件许可和可复现性。

## 实际查看并提取的一手资料
- [Cooperstein et al. 2025 Genome Medicine 全文](https://link.springer.com/article/10.1186/s13073-025-01546-1)：UDN 386 已诊断 probands；GS 编码候选集 231 人/296 个诊断变异，Top-10 49.7→85.5% 是作者优化参数后的排序表现。
- [DIETFITS 2018 JAMA 原文/NIH PMC](https://jamanetwork.com/journals/jama/fullarticle/2673150)：随机 609 人、完成 481，三 SNP 模式 P=0.20，INS-30×饮食 P=0.47（负结果）。
- [Ringbauer et al. 2024 ancIBD](https://pubmed.ncbi.nlm.nih.gov/38123640/)：4,248 个古代样本；>8cM、WGS 大约 0.25× 条件与 ancient-specific imputation/phase；**不能从单人直接认古代祖先**。
- [Sangkuhl et al. 2020 PharmCAT](https://pubmed.ncbi.nlm.nih.gov/31306493/)，[PharmCAT 最新官方方法/FAQ](https://pharmcat.clinpgx.org/faqs/)：CYP2D6 结构变异造成 VCF-only 临床不可用的重大限制。
- [StellarPGx 官方 README](https://github.com/SBIMB/StellarPGx)及[Twesigomwe et al. 2021 论文](https://doi.org/10.1002/cpt.2173)：索引 BAM/CRAM，高覆盖 WGS、SV/CNV/star alleles；原论文 109 个 GeT-RM 样本 99% 的一致性是特定 benchmark。
- [PGS Catalog Calculator 官方 README](https://github.com/PGScatalog/pgsc_calc) 与[WGS 输入说明](https://pgsc-calc.readthedocs.io/en/latest/how-to/prepare.html)：**variant-only WGS VCF 不原生支持**，缺纯合参考位点，需准备专门基因型数据/验证分数位点匹配率。
- [OptiType 官方 README](https://github.com/FRED-2/OptiType)、[Szolek et al. 2014 论文](https://doi.org/10.1093/bioinformatics/btu548)：HLA class I 直接适用 NGS DNA FASTQ/BAM，有 HLA-II 范围限制。

GitHub 直接读取 README/licence 并核：Exomiser AGPL-3.0/15.1.0、PharmCAT MPL-2.0/v3.4.0、StellarPGx MIT/v1.2.8、pgsc_calc Apache-2.0/v2.3.0、ancIBD GPL-3.0（release 未核）、OptiType BSD-3-Clause/v1.5.0；**这些是 GitHub 公开元数据或 licence 文件所能支持的核验，不是运行许可的法律解释、也不代表已部署。**

## 提交成果
1. [cross-domain-evidence-audit.md](../cross-domain-evidence-audit.md) ：6 个代表方向的真实数据约束、原文 cohort N、算法输入/输出、许可证、研究上限。
2. [evidence-capability-matrix.md](../evidence-capability-matrix.md)：修复 D10 的 WGS variants-only VCF 错误假设、D09 的 CYP2D6 复合变异，以及 D14 HLA-I 的真实专项工具。
3. [paper-register.md](../paper-register.md) 新增 P023 OptiType、P024 StellarPGx、P025 PGScalc 方法原文；去重计 25 项。
4. [open-source-projects.md](../open-source-projects.md) 新增 T33 StellarPGx 与 T34 OptiType；去重计 34 项。

## 方法边界 / 负证据
- 2025 Exomiser Top-10 提升是已确诊罕见病病例中的**候选变异排名**，不是无症状消费者的诊断灵敏度。
- PharmCAT CYP2D6 的 VCF-only 输出不能替代 CNV/SV-aware 测量和临床确认。
- pgsc_calc WGS 输入转换是未验证的后续工作，不能说支持原始 WGS CRAM/FASTQ 一键输入。
- DIETFITS 负证据仅适用于研究里的预设基因模式、低脂/低碳及研究人群，不否定全部个性化饮食研究。
- ancIBD 论文评估古人-古人 IBD，不能直接推断现代个体有某位已知古人直系关系。
- HLA-I OptiType 没有证明 HLA-II 能被直接分析或可供临床移植判断。

## 本轮状态
- **PASS**：源码存在性与许可证文件/所述 release 核对，学术研究设计及官方文档输入范围的首轮核查，文件提交及相关文档更新；实际 PR 结构 CI 回读另行核验。
- **PARTIAL**：仅完成跨领域六个代表场景；尚未逐篇审完 25 篇论文全文，或系统统计全世界相关论文/工具。
- **NOT_RUN**：本人或公开基准 WGS 真实运行、软件 accuracy benchmark、GPU/CPU 实测与临床诊断。
- **隐私**：无任何私人 DNA/健康原始数据接触，AI_book 仍公开只收论文与工具研究材料。
- **D0**：本轮切实推进 AC-02/03/04 横向研究覆盖，遵守原 Goal。HG002 运行环境缺 Docker/DNS 是 AC-05 子问题，非全局阻断。
- **唯一下一步候选**：以高价值缺口为主，选 D02 SV/STR、D04 mtDNA、D08 生殖携带者等尚无深入审计方向，继续核验论文、适用位点、开源源码与非可计算部分；另对 pgsc_calc 参考位点恢复以及 CYP2D6 流程制定公开测试的判据，不另建平台。
