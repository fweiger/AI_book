# 2026-11-21｜TOPIC-017 G7：全域论文、WGS 质量与非直接组学一致性审计

**任务**：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)；[Draft PR #73](https://github.com/fweiger/AI_book/pull/73)；协议锁定 `AI_tasks@f0e5ccb90c54265dcd07abb9a975c903eb031ccf`。

## 直接恢复并核实的研究源
- 先 GET 同一 Issue、唯一 Tracker、最新 PR head、G1–G6 唯一事件、D01–D15 [原主矩阵](../evidence-capability-matrix.md)、P001–P041 文献及 T01–T39 源码目录；要求的唯一 G7 动作是**一致性校验**而非继续无边界增加研究量。
- 按原论文/官方标准核 [GIAB CMRG](https://doi.org/10.1038/s41587-021-01158-1)、[ACMG NGS 2021](https://doi.org/10.1038/s41436-021-01139-4)、[PCR-free WGS 对照](https://doi.org/10.1097/MD.0000000000028972)、[原生长读长甲基化方法](https://doi.org/10.1186/s13059-024-03207-9)、[宏基因组](https://doi.org/10.1007/s00335-021-09889-x)、[Gauchian 质疑 P036](https://doi.org/10.1038/s42003-025-08059-y)及[开发者回应 P045](https://doi.org/10.1038/s42003-025-08060-5)。
- 对现有 [fastp](https://github.com/OpenGene/fastp)、[mosdepth](https://github.com/brentp/mosdepth)、[hap.py](https://github.com/Illumina/hap.py)、[DeepVariant](https://github.com/google/deepvariant)、[nf-core/sarek](https://github.com/nf-core/sarek) 的公开 README 读取原始输入、输出契约。没有运行。
- 规范统计前目录经读取/静态解析证实：15 个 D 行、41 个不同 P-ID/DOI、39 个不同 T-ID/仓库，无重复；更新 6 篇后为 47 个 P-ID，仍 39 源码仓库。

## 本轮实质修复
1. [G7 跨 15 域证据审计](../cross-domain-evidence-audit-g7.md) 逐行记录对应论文、质量门槛、工具及科学上限；区分文档 E1 与真实程序 E2。
2. [数据采购与文件质量合同](../wgs-data-acceptance-contract.md) 绑定 FASTQ/BAM/CRAM/gVCF、平均/分位覆盖、参考 build、商业交付权、困难基因/chrY/mtDNA 的差异化准入，**不假设某厂商已达标**。
3. [P-ID 注册表](../paper-register.md) 新增 P042–P047：CMRG 273 复杂医学基因、ACMG、PCR-free 测序真实差异、Gauchian 开发者回应、原生长读长甲基化及宏基因组；各 DOI 经具体一手页面核对，无重复。
4. [主矩阵](../evidence-capability-matrix.md) 改正 D01 5 篇、D08 8 篇、D15 2 篇和 D15 相关例外；[G5 审计](../cross-domain-evidence-audit-g5.md)、[项目目录](../open-source-projects.md) 与 P036 条目补足对 Gauchian 质疑及正式回应的双向记录。
5. 发现一个必须记住的边界：**普通人类短读长未处理 DNA WGS ≠ 所有 WGS 类型**；原生 ONT 长读长测序可采集甲基化修饰信号。但普通短读长 FASTQ 不能把未知的表达组/甲基化信息从 ACGT 文本恢复；非人 reads 可能作为污染/特殊微生物线索，但不能当可靠肠道菌群检测。

## 状态
- **PASS（结构）**：47 个 P-ID 对应不同 DOI、39 项 GitHub 候选无重复、15 个方向有研究质量限制；现有源码 README 可核；本轮新旧条目源文件写入。
- **PARTIAL（学术）**：引证数据和部分原始方法可核，但非 47 篇全文系统综述；没有实际实验的 precision/recall。
- **NOT_RUN（实测）**：不处理私人 DNA、没有跑 GIAB/DeepVariant、没有 HLA/PGx/PRS/IBD/甲基化/菌群样本基准。
- **D0 ALIGNED**：本轮直接实现先前 §7 的 15 域横向质量一致性动作，不改原 Goal/Scope/AC/协议、不建新任务/平台。
- **下一步候选**：优先将已有静态质量合同衔接到**一份合法公开的 HG002 参考数据及限界 benchmark**的最小 E2 运行；本机历史 Docker/DNS 局部阻断不等于生物学研究不可继续，若依赖不满足要标可迁移而非无界修网络。由唯一 Tracker §7 最终确定。
