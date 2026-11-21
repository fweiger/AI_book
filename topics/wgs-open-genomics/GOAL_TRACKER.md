# GOAL_TRACKER.md｜TOPIC-017 / Issue #72 / V1.2.2
> 公开研究主题的**唯一** L 级动态跟踪文件。原批准需求以规范 Issue 为准，本文件不另设第二套需求。
> 创建：2026-11-21；本轮更新：2026-11-21；requirements_revision: 1。

## 任务身份
- 规范任务 Issue：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)
- 所属源仓库：`fweiger/AI_book`
- 项目入口：`topics/wgs-open-genomics/README.md`
- 唯一 Tracker：`topics/wgs-open-genomics/GOAL_TRACKER.md`（本文件）
- 当前阶段：G11 已完成 D03/D04/D09/D10 四款代表源码的真实输入格式、质量条件、输出、许可证与公开测试入口 E0 核查；4/4 E0 PASS、E1 方法 PARTIAL、四工具 E2 NOT_RUN；继承 G10 15 域/47 DOI/39 源码和 G9 D01 chr20 1Mb 公开 E2 PASS
- 选定协议：`fweiger/AI_tasks/task-center/v1.2.2/ENTRY.md`，原实验候选分支 `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`**（续接仅从锁定版本读取，不自动跟随 HEAD）
- 本轮观察的候选分支 HEAD（协议分支）：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 初始 Issue 验证：2026-11-21，GET #72 内容可读，`requirements_revision: 1`
- 当前 Tracker blob SHA：首次创建后从 GitHub 读取；本文件不自引用当前 SHA
- 目标漂移：`D0 ALIGNED`（G11 直接执行原 §7 四领域输入合同审计，不改变 Goal/Scope/AC）
- 状态一致性：`CONSISTENT`（Issue #72、PR #73 和 Tracker 合同目标已回读）
- Issue 同步：`SYNCED`（G1–G12 事件已回读；G12 唯一事件 [#7069462498](https://github.com/fweiger/AI_book/issues/72#issuecomment-7069462498)，同 key 仅 1 条）

## 1. 批准目标基线
- **Goal**：建立个人 WGS 开源技术、学术论文、祖源/家谱/古 DNA、健康与复杂性状科研用途的长期可验证知识框架，明确可研究的深度和科学/临床边界。
- **Scope**：技术 QC、变异与基准、Y/mtDNA、IBD、古 DNA、医学/药物/PRS/睡眠/营养、开源项目及权威论文、公开样本实验。
- **Non-goals**：不购买检测，不处理个人原始 DNA，不公开私人健康/家族信息，不作临床诊断，不搭建新系统取代现有软件。
- **核心 AC**：以下完全参照规范 Issue #72 的 AC-01—AC-06。

| AC | 验收 | 验证方法 | 当前 | 证据 |
|---|---|---|---|---|
| AC-01 | 唯一 TOPIC-017 Issue 入口且合理查重 | GitHub 查询并回读 | PASS | [#72](https://github.com/fweiger/AI_book/issues/72) |
| AC-02 | ≥25 个真实 GitHub 工具及清晰分类、输入用途限制 | 逐仓库 GitHub 元数据；文件回读 | PARTIAL（39 项不同源码候选存在性 PASS；G10 复核代表工具 GitHub README/实际输入与部分既有许可；G11 四款源码许可证与输入已核；G12 Haplogrep3 v3.3.2 官方 H100 VCF CLI 功能回归与 expected 输出逐字节匹配 PASS；其余工具/许可证仍未全量审计） | [G10 方法×源码输入审计](cross-domain-method-evidence-audit-g10.md) · [39 项代码目录](open-source-projects.md) |
| AC-03 | ≥10 条原始论文/标准，主题相联 | DOI/原始来源交叉核查；全文审计 | PARTIAL（47 个 DOI/指南已登记；G10 从中为 15 域各抽 1 篇一手方法/摘要/部分正文并核正 P005 原文 DOI；完整 47 篇全文/附录仍未系统审计） | [G10 15 域方法核查](cross-domain-method-evidence-audit-g10.md) · [论文注册表](paper-register.md) |
| AC-04 | ≥8 研究方向及数据/深度/失败边界 | Q-ID 与矩阵逐项核对 | PARTIAL（G10 已为 15/15 域建立代表一手 DOI×assay×外部队列×WGS 数据质量×GitHub 输入×科学结论边界；G11 四域 E0 输入已核；G12 D04 VCF→haplogroup CLI 功能回归 PASS，但独立准确率 E2 NOT_RUN；各域独立基准仍仅 D01 G9 1Mb E2） | [G10 全域代表方法审计](cross-domain-method-evidence-audit-g10.md) · [主矩阵](evidence-capability-matrix.md) |
| AC-05 | 公共参考基因组最小可复现实验和证据 | GIAB HG002 + 版本化命令与 QC | **PASS（范围受限）：**真实 HG002 chr20 1Mb bcftools1.19/RTG3.13 独立 GIAB v4.2.1 BED 指标和二次运行日志、变异记录/摘要哈希一致；原 DeepVariant/hap.py 单独方案仍 NOT_RUN | [G9 原始结果与复现](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md) · [G9 实际可运行源码](scripts/run-hg002-chr20-bcftools-rtg.sh) |
| AC-06 | 专题分支、唯一 Tracker、审核 PR 和回链 | GitHub 文件、PR、INDEX、CI 校验 | PARTIAL（Draft PR #73/结构 CI PASS，尚待审核合并） | [PR #73](https://github.com/fweiger/AI_book/pull/73) |

## 2. 对上级目标的贡献
- 知识库将遗传研究的技术事实、科研证据及历史叙事放在同一可审计框架；每项使用公共源码和论文链接。
- 成功时读者能回答“有了 WGS，哪些问题在一个人身上能算，哪些必须额外采样/外部临床验证？”
- 最重要的核心问题不是单个 GitHub 仓库能否安装，而是工具、数据和证据如何共同限定研究结论。

## 3. 当前执行路径
| 阶段 | 预期结果 | 对应 AC | 证据 | 状态 | 依赖 |
|---|---|---|---|---|---|
| S1 | 15 域质量→论文→研究深度→GitHub 横向矩阵并入 Draft PR | 01–04/06 | [主矩阵](evidence-capability-matrix.md)、[47 个 P-ID](paper-register.md)、[G10 15 域方法对应](cross-domain-method-evidence-audit-g10.md) | PARTIAL（15/15 代表方法 E1 对齐 PASS；剩余 32 篇全文/数据库及各域实际执行待审） | 需完成更深一手论文和实际软件的输入兼容性核验 |
| S2 | HG002 公开数据准入 → 最小 chr20 SNP/Indel E2 | 02/05 | [G8 官方数据/哈希](sessions/2026-11-21-hg002-public-data-admission-g8.md)、[G9 实测和二次复现](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md) | **PASS（仅 G9 chr20 1Mb bcftools/RTG）**，原 DeepVariant/hap.py 未测试 | 与其他 14 研究域的结论真实性独立，下一步恢复论文×源码全域研究 |
| S3 | 15 域论文×WGS 输入×代码/研究结论及许可证可靠性 | 02–04 | [主矩阵](evidence-capability-matrix.md)、[G10 逐域一手方法](cross-domain-method-evidence-audit-g10.md) | PARTIAL（G10 15/15 域代表论文/源码方法输入已核；G11 四工具 E0 合同已核；G12 D04 Haplogrep3 v3.3.2 官方 H100 CLI 功能回归 PASS，独立准确率 E2 NOT_RUN；其余论文、许可证与 E2 尚待审） | 评估并有界复现 D04 上游 Mutserve v2.0.3 官方 CRAM 回归输入；若缺少索引且不能在临时目录解决则停止，不做系统安装 |
| S4 | 跨工具/人群的结果比较、反证和下一版图谱 | 02–05 | 真实运行与来源日志 | TODO | 前期质量基线 |

## 4. 当前检查点
- **G10 真实交付**：[D01–D15 每域代表一手方法/样本/祖源/WGS 数据质量/现有源码输入/证据上限审计](cross-domain-method-evidence-audit-g10.md) 和 [本轮来源日志](sessions/2026-11-21-15domain-primary-methods-audit-g10.md) 已提交到原 Draft PR；从 47 个 P-ID 中选出 D01–D15 对应 15 篇 DOI/指南，每域清晰区分 SINGLE_WGS / EXTERNAL / OTHER_ASSAY 和 E0/E1/E2。并非完成其余 32 篇全文系统复核。
- **重要纠错**：P005 Yleaf 方法原文 DOI 为 `10.1093/molbev/msy032`（PubMed PMID 29518227）；旧 `10.1093/molbev/msy080` 是 Erratum，不得当方法论文。已更新原 P-ID 注册表、sources 和主矩阵，P-ID/DOI 仍 47 个且无重复。
- **代码与个人 WGS 准入纠错**：本轮实际读取 bcftools、Truvari、Yleaf、Mutserve、hap-IBD、ADMIXTOOLS2、VEP、InterVar、StellarPGx、pgsc_calc、OptiType、PRS-CSx、PLINK2 的 GitHub README/仓库信息；pgsc_calc 官方明确当前不直接支持 WGS genotype 输入；样本单人并不满足 hap-IBD 多人相位/遗传图谱、qpAdm 群体参照、营养干预/运动训练/睡眠表型的论文研究合同。
- **质量门禁和统计**：实际文件回读/解析 **D01–D15 15 个唯一领域、47 个不同 P-ID/DOI、39 个不同 GitHub 仓库、15/15 抽审 P-ID 均在注册表内**：结构 PASS。部分论文仅按原始摘要/已展示方法段核，**E1/PARTIAL**，所有 D02–D15 源码运行 E2 NOT_RUN。G9 D01 chr20 1Mb bcftools/RTG E2 PASS 保留，原 DeepVariant/hap.py NOT_RUN。
- **现有阻断与目标状态**：不处理个人 DNA；没有对 47 篇全文/39 仓库全部依赖/许可证做系统性审计，不假报“全球全部工具或论文”。D0 ALIGNED、与原 Issue Goal/Scope/AC CONSISTENT；G10 唯一进度事件 [#7064791856](https://github.com/fweiger/AI_book/issues/72#issuecomment-7064791856) 已回读并同步。

- **G11 真实新增**：[D03/D04/D09/D10 四领域 WGS 输入合同](four-domain-wgs-input-contract-g11.md) 已在同一 PR 提交。Yleaf、Haplogrep3、StellarPGx、pgsc_calc 四款工具实际 README/源码/许可证/公开测试入口已查；E0 4/4 PASS，E1 论文已初审但方法深度 PARTIAL，E2 0/4 NOT_RUN。发现 StellarPGx README SIM001 与当前 test.config HG03130 不同，不能直接当单一复现实验。未新增论文/工具/个人基因数据。
- **G12 真实新增**：[Haplogrep3 v3.3.2 H100 官方 VCF CLI 复现](sessions/2026-11-22-haplogrep3-h100-cli-functional-g12.md)：31.5 Ubuntu/Java21，固定 release SHA、H100.vcf、PhyloTree FU rCRS 1.3 package digest；CLI exit=0，主输出与 QC 输出均与同 tag expected **逐字节一致**。标准 rCRS 17.0 与 FU rCRS 1.3 的 Quality 分别 0.8351/0.8356，已定位树版本影响。该 fixture 仅 14 条已调用 MT 变异，不含 read depth；QC 0.84 低于 0.9 阈值；官方 expected 不是独立真值，故 CLI 功能 PASS、独立准确率 E2 NOT_RUN。

## 5. 阻断与未受影响工作
| 问题 | 影响范围 | 对应 AC | 继续可以推进的部分 | 状态 |
|---|---|---|---|---|
| 既有 47 项中剩余 32 项未逐篇全文系统审计、实际医学/统计外推边界不统一 | AC-03/04 的全面证据完整性 | 03/04 | 15 域代表方法已有，可优先审最影响决策的负证据和缺口 | PARTIAL |
| 39 个现有 GitHub 软件许可证/复杂输入及跨祖源模型仍未完成全量运行/审查 | 软件可复用性与输入质量 | 02/04 | G12 已完成 D04 VCF→haplogroup 功能回归；下一缺口为上游 BAM/CRAM→VCF caller，拟有界核验 Mutserve v2.0.3 公共 CRAM 测试；其余 35 项工具与独立 accuracy 仍待审 | PARTIAL |
| Docker DeepVariant/hap.py 固定早期路径仍未完整 | 仅其指定的额外对照实验 | 05 部分额外研究 | G9 原生 bcftools/RTG 最小 E2 已 PASS | 局部 NOT_RUN，非本轮研究阻断 |
| 用户私人商业 WGS 文件不在本项目 Scope 中 | 个人质量/医疗/亲缘实测 | Non-goals | 公开标准、数据准入与学术方法 | 不请求/不公开 |

## 6. 执行路径调整记录
| 时间 | 旧候选 | 实际动作/调整 | 证据 | 关联 AC | 范围改变 |
|---|---|---|---|---|---|
| G1–G3 | 初始目录与父系局部 | 确立全域 WGS 质量→论文→工具研究 | 规范 Issue G1–G3 | 01–06 | 否 |
| G4–G7 | 横向论文和源码方法审计 | 完成 15 域研究图谱和原始数据验收合同 | G4–G7 证据文件 | 02/03/04 | 否 |
| **2026-11-21/G8** | 公开 HG002 E2 实验 | 实际完成 HG002 文件 download/hash 官方 BAM MD5；Docker image 两次有界尝试未就绪，止损后不扩建平台 | [G8 真实日志/哈希](sessions/2026-11-21-hg002-public-data-admission-g8.md) | **05 PARTIAL** | 否 |
| **2026-11-21/G9** | 现有 HG002 数据与有界原生工具 | bcftools1.19/RTG3.13 公开 HG002 chr20 1Mb 独立 GIAB/true E2，二次代码实跑变异正文/摘要 SHA 一致；不再修 Docker 大镜像 | [G9 报告](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md)、[源码](scripts/run-hg002-chr20-bcftools-rtg.sh) | **05 PASS（限界）** | 否 |
| **2026-11-21/G10** | G9 E2 后回归 15 域代表方法审计 | 逐域核 15 篇一手论文真实 assay、祖源/队列、单人 WGS 输入、GitHub 兼容性与外推边界；P005 原文/勘误 DOI 修正 | [G10 报告](cross-domain-method-evidence-audit-g10.md)、[日志](sessions/2026-11-21-15domain-primary-methods-audit-g10.md) | 02/03/04 PARTIAL（方法结构 15/15 PASS） | 否 |

| **2026-11-22/G11** | G10 四个代表方向静态数据合同 | Yleaf/Haplogrep3/StellarPGx/pgsc_calc 实际输入/参考/许可/测试核验；澄清官方测试不等于独立准确率，Stellar 文档/配置不一致 | [G11 四域合同](four-domain-wgs-input-contract-g11.md) | 02/03/04 PARTIAL（四工具 E0 PASS，E2 NOT_RUN） | 否 |
| **2026-11-22/G12** | D04 Haplogrep3 官方 VCF 分类功能复现 | v3.3.2 + H100 VCF + phylotree-fu-rcrs@1.3；主输出与 QC 均与官方 expected SHA256 完全一致；标准 rCRS17.0 与 FU1.3 的质量分数不同，确认树版本敏感；独立准确率未验证 | [G12 CLI 功能复现日志](sessions/2026-11-22-haplogrep3-h100-cli-functional-g12.md) | AC-02/04 PARTIAL；功能回归 PASS；准确率 E2 NOT_RUN | 否 |

## 7. 下一步
- **唯一优先动作（G13）**：对 D04 上游 **Mutserve v2.0.3** 做一次有界官方公开 CRAM 功能回归：固定 GitHub release/tag，使用官方 `test.cram` / `test1.cram`、rCRS reference 和同版本 `test-data/mtdna/cram/output/variants.txt` / `variants.vcf`，先验证文件哈希和输入索引条件，再运行 `mutserve call` 并比较输出。不得将同仓库 expected 文件称为独立准确率真值。
- **为什么选它**：G12 已验证 Haplogrep3 的 VCF→haplogroup/QC 阶段；真正缺口是上游从 read-level mtDNA CRAM/BAM 产生变异。Mutserve 官方仓库已提供公开 CRAM 和同仓库 expected 结果，适合用一个小范围测试确认实际输入和输出。该动作推进 AC-02/04，不再重复安装/扩展 Haplogrep 平台。
- **边界与停止条件**：Mutserve README 明确其 VCF 输出**不包含 indels**，主要覆盖 SNV/异质位点；本轮只能验 SNV/heteroplasmy 功能，不能宣称 mtDNA 全变异类型完成。README 要求 sorted/indexed CRAM/BAM，而仓库 CRAM 输入目录未见 CRAI、31.5 当前 PATH 未发现 samtools；若必须建索引且无法在临时目录使用已存在的独立工具完成，则报告 BLOCKED，不做系统级安装、不搭平台。
- **跨域防止目标锁定**：G11/G12 已分别推进四域静态输入和 D04 下游功能；G13 仅允许这一项上游依赖验证。完成或受阻后重新比较 D09 StellarPGx（有公开 HG03130/SIM001 BAM 和 reference）、D10 PGS WGS 兼容性及其余 11 域/32 篇论文，避免连续把研究范围锁在 D04。
- **关联 AC**：AC-02/03/04 PARTIAL；AC-05 仅 G9 D01 HG002 chr20 1Mb 独立 GIAB E2 PASS；AC-06 Draft PR #73 未合并。原 Goal/Scope/Non-goals/AC 不变。

## 8. 每轮恢复核对
- [ ] 用锁定 `f0e5ccb90c54265dcd07abb9a975c903eb031ccf` 获取 Task Center V1.2.2 入口与续接协议，核对 Sticky Assignment；不自动改协议。
- [ ] 回读规范 [Issue #72](https://github.com/fweiger/AI_book/issues/72) Goal/Scope/AC，最新评论、PR 和本 Tracker SHA。
- [ ] 核查真实源码、论文、数据、实验与 CI 结果，不能仅依本文件自报。
- [ ] 判断目标偏差 D0/D1/D2/UNKNOWN、状态一致性、阻断影响与未完成 AC。
- [ ] 重选唯一优先动作，历史建议只是候选；写入必须 CAS，并遵守单 Writer 事件声明。
- [ ] 不公开个人 WGS、基因型、家族身份和医疗信息。

## 9. 检查点历史（追加，不覆盖）
| 时间/批次 | 实际工作结果 | AC 贡献 | 原始证据 | 漂移/状态 | 当轮候选下一步 |
|---|---|---|---|---|---|
| 2026-11-21/G1 | 首轮创建 AI_book Issue #72 与 Draft PR #73，收录最初 32 个仓库和研究框架 | 01/02/03/04/06 PARTIAL | [Issue #72](https://github.com/fweiger/AI_book/issues/72)；[G1 事件 #7059893177](https://github.com/fweiger/AI_book/issues/72#issuecomment-7059893177) | D0；已回读 | 公开 HG002 最小基准 |
| 2026-11-21/G2 | HG002 chr20 公开基准规范+脚本；Yleaf、Y-LineageTracker、yhaplo 方法核查；真实实验未运行 | 02/03/05 PARTIAL | [G2 事件 #7060020787](https://github.com/fweiger/AI_book/issues/72#issuecomment-7060020787) | D0；已回读 | 父系公开样本输入 |
| 2026-11-21/G3 | 用户明确横向研究目标，建立 15 域数据质量×论文×GitHub 主矩阵；22 论文/32 项工具 | 02/03/04 PARTIAL | [G3 事件 #7060148978](https://github.com/fweiger/AI_book/issues/72#issuecomment-7060148978) | D0；已回读 | 跨领域论文与源码审计 |
| 2026-11-21/G4 | 完成六领域方法、许可与输入核查；补 StellarPGx/OptiType，25 论文/34 项 | 02/03/04 PARTIAL | [G4 事件 #7060387293](https://github.com/fweiger/AI_book/issues/72#issuecomment-7060387293) | D0；已回读 | SV/mtDNA/携带者 |
| 2026-11-21/G5 | 完成 D02/D04/D08 的原始证据与许可限制；36 论文/39 个源码候选 | 02/03/04 PARTIAL | [G5 事件 #7060680525](https://github.com/fweiger/AI_book/issues/72#issuecomment-7060680525) | D0；已回读 | 现代 IBD、睡眠、运动 |
| 2026-11-21/G6 | 深核 D05 相位 IBD、D11 睡眠 GWAS/PRS、D13 运动行为与训练反应模型，新增 P037–P041；41 论文/39 仓库 | 02/03/04 PARTIAL | [G6 审计](cross-domain-evidence-audit-g6.md)、[本轮日志](sessions/2026-11-21-ibd-sleep-exercise-paper-code-audit.md) | D0 ALIGNED，Issue G6 事件待同步；E2 NOT_RUN | 15 域证据/输入/许可一致性审计 |
| 2026-11-21/G7 | 15 域/47 DOI/39 仓库交叉索引去重 PASS；D01 GIAB/ACMG/PCR-free 质量、D15 非直接组学边界、Gauchian 质疑/回应纠偏；原始文件验收合同 | AC-02/03/04 PARTIAL | [G7 审计](cross-domain-evidence-audit-g7.md)、[文件合同](wgs-data-acceptance-contract.md)、[证据日志](sessions/2026-11-21-wgs-quality-cross-evidence-audit.md) | D0/CONSISTENT（G7 同步待验证），E2 NOT_RUN | 公共 HG002 chr20 真实小变异 benchmark |

| 2026-11-21/G8 | 31.5 真实 HG002 chr20 8 文件下载/本地 SHA256 全 PASS、官方 GCS BAM MD5 匹配；原脚本续传最小修复；两镜像受限拉取均受控停止，E2 NOT_RUN | AC-05 PARTIAL | [G8 真实公共数据准入证据](sessions/2026-11-21-hg002-public-data-admission-g8.md)、[脚本](scripts/run-giab-hg002-chr20.sh) | D0/CONSISTENT，需同步唯一事件 | 一次有界轻量原生/小镜像 E2；不成功则 AC03 文献方法审计 |

| 2026-11-21/G9 | 真正完成公开 HG002 chr20 1Mb bcftools 变异调用+RTG 独立 GIAB/ROC SNP F1 0.9962、Indel F1 0.9367，脚本二次复现记录/汇总 SHA 一致；原 DeepVariant 尚未运行 | AC-05 PASS（1Mb 有界 E2），AC-03/04 仍 PARTIAL | [G9 实测和输入/输出哈希](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md)、[可运行脚本](scripts/run-hg002-chr20-bcftools-rtg.sh) | D0 ALIGNED/CONSISTENT，Issue G9 事件待同步 | 审核 D01–D15 每域一个一手方法/数据/实现边界 |

| 2026-11-21/G10 | 从 47 个 P-ID 中审 D01–D15 各 1 篇一手方法/assay/祖源/结论及软件输入；更正 P005 原始 DOI msy032（msy080 实为勘误）；官方 pgsc_calc README 明示不直接支持 WGS | AC-02/03/04 PARTIAL；方法结构 15/15 PASS | [G10 15 域方法报告](cross-domain-method-evidence-audit-g10.md)、[G10 来源日志](sessions/2026-11-21-15domain-primary-methods-audit-g10.md) | D0 ALIGNED；G10 事件同步待核验 | D03/D04/D09/D10 单份 WGS 输入质量及可研究深度核验 |

| 2026-11-22/G11 | 四个代表 GitHub 工具文件级输入合同和真实 LICENSE/测试入口；4/4 E0 PASS、E2 0/4 NOT_RUN | AC-02/03/04 PARTIAL | [G11 四领域合同](four-domain-wgs-input-contract-g11.md) | D0 ALIGNED/CONSISTENT；G11 Writer 待同步 | D04 官方公开 VCF 有界 CLI 功能复现 |

| 2026-11-22/G12 | D04 Haplogrep3 v3.3.2 官方 H100 VCF CLI 功能回归；固定 FU rCRS 1.3 后主输出/QC 与官方 expected 逐字节匹配；树版本改变质量分数；独立准确率 E2 NOT_RUN | AC-02/04 PARTIAL（功能回归 PASS） | [G12 运行日志](sessions/2026-11-22-haplogrep3-h100-cli-functional-g12.md) | D0 ALIGNED/CONSISTENT，G12 事件待同步 | D04 上游 Mutserve v2.0.3 官方 CRAM 有界功能回归 |

## 10. 最近一次状态一致性回读
- **当前 active_event_key**：none（G12 `AI_book#72:AC02-03-04:20261122-g12-haplogrep3-h100-cli-functional` 已完成）
- **当前 writer_owner**：none（G12 Writer `chatgpt-topic017-g12-20261122` 已完成）
- **当前 write_state**：`SYNCED`（[G12 唯一事件 #7069462498](https://github.com/fweiger/AI_book/issues/72#issuecomment-7069462498) GET 回读，同 `event_key` 仅 1 条；发布前 Tracker blob SHA `2f2a1a43afc3b8bb041df748aa69e3ea1cad4c10`）
- **单 Writer 交接**：G12 唯一 Writer 发布后清理；G11/G10 均已完成并清理；无未决 CLAIMED。
- **证据路径**：[G12 Haplogrep3 H100 CLI 功能复现](sessions/2026-11-22-haplogrep3-h100-cli-functional-g12.md)；原始 GitHub release/test/tree SHA、实际命令、exit code、输出 SHA、expected 比对和失败边界均记录。

| 检查项 | 当前值 | 证据 | 结果 |
|---|---|---|---|
| 原 Issue Goal/Scope/AC / 协议 | #72 requirements_revision=1；V1.2.2 锁定 commit `f0e5ccb90c54265dcd07abb9a975c903eb031ccf` 不变 | GET Issue + 锁定 ENTRY/CONTINUE | CONSISTENT |
| G12 真实增量 | Haplogrep3 v3.3.2 官方 H100 VCF CLI exit=0；FU rCRS 1.3；主/QC 输出逐字节匹配；独立准确率 E2 NOT_RUN | [G12 报告](sessions/2026-11-22-haplogrep3-h100-cli-functional-g12.md) | FUNCTIONAL PASS / E2 NOT_RUN |
| 当前唯一下一步 | §7 Mutserve v2.0.3 官方 CRAM 上游功能回归，有索引/indel停止条件；完成后回到跨域优先级 | §7 / §9 | D0 ALIGNED |
| G12 Tracker 与 Issue | 稳定 key 唯一 #7069462498，Writer 声明与发布评论一致，最终清理 | [#7069462498](https://github.com/fweiger/AI_book/issues/72#issuecomment-7069462498) + 最新 Tracker | SYNCED |

> PR #73 仍为 Draft，未合并；GitHub 结构 CI 不等于 Haplogrep3 科学准确率验证。
