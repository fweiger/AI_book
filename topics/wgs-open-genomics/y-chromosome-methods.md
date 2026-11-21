# TOPIC-017 / Q03｜Y 染色体开源方法：能识别分支，不自动证明家谱

> 2026-11-21。规范任务：[Issue #72](https://github.com/fweiger/AI_book/issues/72)；[Draft PR #73](https://github.com/fweiger/AI_book/pull/73)。方法论文与仓库 README 已核查；**没有运行私人 Y 数据、没有验证某个家族谱系**。

## 一、把“寻祖”拆成四种不同的研究问题
1. **Y 单倍群分类**（单人足以进行）：`BAM/CRAM/VCF + chrY SNP calls + 参考树版本` → 已证实衍生型/祖先型/未测到 SNP → 当前树上最深可支持节点；此结论不包含任何家谱姓名。
2. **多名男性父系分叉关系**（至少两位授权样本）：共享/私有 Y-SNP 和独立质量证据 → 分支嵌套、平行关系；若候选位点无覆盖不能硬判“没有突变”。
3. **共同祖先时间**：多个样本的可比较可靠位点、过滤规则、突变率或 Y-STR 统计模型、代际长度、年代校准 → 估计及区间。**单人终端单倍群不等于获得精确 TMRCA**。
4. **历史迁徙、改姓、名人祖先**：DNA 的分支/年代 + 地理样本覆盖 + 族谱/碑刻/档案独立证明；“共组”不直接证明随军迁徙、入赘、改变姓氏。

## 二、三个已存在开源项目的真实分工
| 工具 | 官方输入与参考版本 | 能做 | 不能直接做 | 关键来源 |
|---|---|---|---|---|
| [genid/Yleaf](https://github.com/genid/Yleaf) | BAM、CRAM、FASTQ、VCF（具体要看版本），支持 hg19/hg38/T2T；可以选 yfull/ftdna/isogg 树 | 从序列/分型判定 Y 单倍群；部分版本支持树图、private SNP | 单独证明某姓起源/古人直系身份；不确保商业私有库匹配 | [官方 README](https://github.com/genid/Yleaf/blob/master/README.md)，[2018 论文](https://doi.org/10.1093/molbev/msy080) |
| [Shuhua-Group/Y-LineageTracker](https://github.com/Shuhua-Group/Y-LineageTracker) | BAM/VCF 等，明确输入参考基因组 build；Y-SNP 与 Y-STR | `classify`、`phylo`、`time` (NRY 分支分化时间)、`tmrca` (Y-STR 单倍型共祖时间)、`genostr` | 无多个样本的情况下不能凭一人计算近亲家谱分支或对照组 TMRCA | [官方 README](https://github.com/Shuhua-Group/Y-LineageTracker/blob/main/README.md)，[2021 论文](https://pubmed.ncbi.nlm.nih.gov/33750289/) |
| [23andMe/yhaplo](https://github.com/23andMe/yhaplo) | 项目文档说明 ISOGG 定位预期为 **hg19/GRCh37**；支持索引 VCF/BCF、样本主导基因型文件 | 批量或单人 Y 单倍群分类 | **不能把 GRCh38 chrY 坐标直接塞进 GRCh37 模型而不转换**；文档警告仅变异位点 VCF 与低 Y 覆盖可能造成错误判断 | [官方 README](https://github.com/23andMe/yhaplo/blob/master/README.md)、[2016 bioRxiv 方法预印本](https://doi.org/10.1101/088716) |

**特别重要的兼容问题**：对比工具时必须固定 `reference_build / contig_style / tree_source / tree_revision / SNP table version / callable bases / min_read_depth / alt/ancestral logic`。不同数据库对同一谱系节点可能命名不同；只有共有的实际遗传位点才可严格对照。不能将旧版 yhaplo 的 hg19 坐标与 Yleaf 的 hg38 判定直接比较。

## 三、技术输入分辨率对照
- **只有 SNP array 或 variants-only VCF**：没有证据证明未出现于 VCF 的 Y SNP 已被测到并确定是参考等位；Yleaf README 特别提醒单 panel VCF 的 reference inference 会误判，需要 `--no-ref-inference` 之类的明确处理；yhaplo README 也警告这种不完整输入。
- **标准 WGS BAM/CRAM**：可直接观察目标 SNP 的 read depth、等位平衡、比对质量，但 chrY 高重复区域和未覆盖位置仍可能不可判。
- **多个父系男性高质量 chrY**：可以比较共享祖先型、下游衍生型与各自私有突变；统计年代仍依赖模型/测序区域匹配。
- **商业数据库**（如 23魔方、YFull 或 FTDNA）：增量价值来自已授权的其他用户样本、私有分支树、样本地理与家谱信息；仅拥有一份 WGS 原始文件并不能自动取得这些专有样本或重新创建其业务数据库。

## 四、年代方法必须区分
`Y-LineageTracker time` 使用 NRY SNP 树/分子钟/校准的时间推断；`Y-LineageTracker tmrca` 是 **Y-STR 单倍型**的共祖时间估计，采用 rho/ASD 等统计方式。两者的突变机制、误差来源、参考树和数据需求不同，**不能直接套用同一公式与同一突变率**。官方 README 对 Y-STR TMRCA 的默认代际长度和突变率有示例，但这并不说明所有祖系可用这些默认值。

YFull 官方说明其年龄估计会按可用 SNP、特殊过滤区域与质量过滤不同地计入突变，且识别 public/private SNP。见 [YFull 教程](https://www.yfull.com/tutorial/)；消费者获得的商业 TMRCA 是**该平台当前样本/模型/过滤条件下的统计估计**，必须报告置信区间与版本，而非历史确切年份。

## 五、可以复现的验证矩阵（尚未运行）
| 测试 ID | 输入 | 验证目标 | 成功/失败证据 |
|---|---|---|---|
| Y01 | 同一公共 chrY BAM + 与之匹配的 reference | Yleaf hg38 下游分支与支持/反对 SNP | 软件版本、callable 区、真实输出、拒绝位点 |
| Y02 | 同一个公共人的 chrY 可兼容调用文件 | Y-LineageTracker 与 Yleaf 的一致/分歧 | SNP 位点同坐标转换后的差异表 |
| Y03 | 经过验证的 GRCh37 参考/基因型 | yhaplo 分类及低覆盖警告 | 是否可检测 SNP、派生路径、未判定比率 |
| Y04 | 至少两份合法公开且可比较的父系样本 | 树的平行/祖先关系与 TMRCA 是否可重复 | 共同/私有 SNP、置信区间、突变率敏感性 |
| Y05 | 测序数据 + 独立族谱/史料 | DNA 是否真的支持某一历史迁徙假说 | 有正反两套证据，不能靠姓氏一致判定 |

## 六、当前证据与下一步
- **E0/E1**：Yleaf、Y-LineageTracker、yhaplo 的仓库 README 与对应方法论文的可检索内容已对照，明确区分三种工具的输入与输出。
- **E2 NOT_RUN**：未下载公共 chrY WGS、未执行 Y01–Y05、未独立验证任何 TMRCA；禁止使用营销宣传推定精度。
- **下一项最高价值**：优先选一组带明确定义的**公开男性 chrY 数据/参考分支**，构建 Y01/Y02 的共同输入和相同坐标/树版本的交叉比对，实际执行只限已具备环境/授权的计算资源；否则继续独立审查方法论文与数据可用性，不把单人共组说成家谱。
