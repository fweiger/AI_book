# GOAL_TRACKER.md｜TOPIC-017 / Issue #72 / V1.2.2
> 公开研究主题的**唯一** L 级动态跟踪文件。原批准需求以规范 Issue 为准，本文件不另设第二套需求。
> 创建：2026-11-21；本轮更新：2026-11-21；requirements_revision: 1。

## 任务身份
- 规范任务 Issue：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)
- 所属源仓库：`fweiger/AI_book`
- 项目入口：`topics/wgs-open-genomics/README.md`
- 唯一 Tracker：`topics/wgs-open-genomics/GOAL_TRACKER.md`（本文件）
- 当前阶段：G10 完成 D01–D15 每域代表一手论文的方法/assay/队列/数据输入/GitHub 适配与外推边界审计，纠正 P005 Yleaf 原文 DOI；15 域/47 去重 DOI/39 源码保持；G9 仅 D01 1Mb 公共 E2 PASS
- 选定协议：`fweiger/AI_tasks/task-center/v1.2.2/ENTRY.md`，原实验候选分支 `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`**（续接仅从锁定版本读取，不自动跟随 HEAD）
- 本轮观察的候选分支 HEAD（协议分支）：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 初始 Issue 验证：2026-11-21，GET #72 内容可读，`requirements_revision: 1`
- 当前 Tracker blob SHA：首次创建后从 GitHub 读取；本文件不自引用当前 SHA
- 目标漂移：`D0 ALIGNED`（G10 直接执行上一 §7 的 15 域代表原文方法级审计，推进未完成 AC-02/03/04，未延伸 D01 局部容器工程）
- 状态一致性：`CONSISTENT`（Issue #72、PR #73 和 Tracker 合同目标已回读）
- Issue 同步：`SYNCED`（G1–G8 事件均已回读，G9 唯一事件 #7062643687 按稳定键回读）

## 1. 批准目标基线
- **Goal**：建立个人 WGS 开源技术、学术论文、祖源/家谱/古 DNA、健康与复杂性状科研用途的长期可验证知识框架，明确可研究的深度和科学/临床边界。
- **Scope**：技术 QC、变异与基准、Y/mtDNA、IBD、古 DNA、医学/药物/PRS/睡眠/营养、开源项目及权威论文、公开样本实验。
- **Non-goals**：不购买检测，不处理个人原始 DNA，不公开私人健康/家族信息，不作临床诊断，不搭建新系统取代现有软件。
- **核心 AC**：以下完全参照规范 Issue #72 的 AC-01—AC-06。

| AC | 验收 | 验证方法 | 当前 | 证据 |
|---|---|---|---|---|
| AC-01 | 唯一 TOPIC-017 Issue 入口且合理查重 | GitHub 查询并回读 | PASS | [#72](https://github.com/fweiger/AI_book/issues/72) |
| AC-02 | ≥25 个真实 GitHub 工具及清晰分类、输入用途限制 | 逐仓库 GitHub 元数据；文件回读 | PARTIAL（39 项不同源码候选存在性 PASS；G10 复核代表工具 GitHub README/实际输入与部分既有许可；全部 39 项的许可证/实际算法仍未验收，部分并非 OSI 开源） | [G10 方法×源码输入审计](cross-domain-method-evidence-audit-g10.md) · [39 项代码目录](open-source-projects.md) |
| AC-03 | ≥10 条原始论文/标准，主题相联 | DOI/原始来源交叉核查；全文审计 | PARTIAL（47 个 DOI/指南已登记；G10 从中为 15 域各抽 1 篇一手方法/摘要/部分正文并核正 P005 原文 DOI；完整 47 篇全文/附录仍未系统审计） | [G10 15 域方法核查](cross-domain-method-evidence-audit-g10.md) · [论文注册表](paper-register.md) |
| AC-04 | ≥8 研究方向及数据/深度/失败边界 | Q-ID 与矩阵逐项核对 | PARTIAL（G10 已为 15/15 域建立代表一手 DOI×assay×外部队列×WGS 数据质量×GitHub 输入×科学结论边界；各域实际效果仅 D01 G9 1Mb E2） | [G10 全域代表方法审计](cross-domain-method-evidence-audit-g10.md) · [主矩阵](evidence-capability-matrix.md) |
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
| S3 | 15 域论文×WGS 输入×代码/研究结论及许可证可靠性 | 02–04 | [主矩阵](evidence-capability-matrix.md)、[G10 逐域一手方法](cross-domain-method-evidence-audit-g10.md) | PARTIAL（G10 15/15 域代表论文/源码方法输入已核；剩余 32 篇、全部 39 项完整许可与 E2 尚待审） | 优先核对单人可用领域的输入数据契约和科研上限 |
| S4 | 跨工具/人群的结果比较、反证和下一版图谱 | 02–05 | 真实运行与来源日志 | TODO | 前期质量基线 |

## 4. 当前检查点
- **G10 真实交付**：[D01–D15 每域代表一手方法/样本/祖源/WGS 数据质量/现有源码输入/证据上限审计](cross-domain-method-evidence-audit-g10.md) 和 [本轮来源日志](sessions/2026-11-21-15domain-primary-methods-audit-g10.md) 已提交到原 Draft PR；从 47 个 P-ID 中选出 D01–D15 对应 15 篇 DOI/指南，每域清晰区分 SINGLE_WGS / EXTERNAL / OTHER_ASSAY 和 E0/E1/E2。并非完成其余 32 篇全文系统复核。
- **重要纠错**：P005 Yleaf 方法原文 DOI 为 `10.1093/molbev/msy032`（PubMed PMID 29518227）；旧 `10.1093/molbev/msy080` 是 Erratum，不得当方法论文。已更新原 P-ID 注册表、sources 和主矩阵，P-ID/DOI 仍 47 个且无重复。
- **代码与个人 WGS 准入纠错**：本轮实际读取 bcftools、Truvari、Yleaf、Mutserve、hap-IBD、ADMIXTOOLS2、VEP、InterVar、StellarPGx、pgsc_calc、OptiType、PRS-CSx、PLINK2 的 GitHub README/仓库信息；pgsc_calc 官方明确当前不直接支持 WGS genotype 输入；样本单人并不满足 hap-IBD 多人相位/遗传图谱、qpAdm 群体参照、营养干预/运动训练/睡眠表型的论文研究合同。
- **质量门禁和统计**：实际文件回读/解析 **D01–D15 15 个唯一领域、47 个不同 P-ID/DOI、39 个不同 GitHub 仓库、15/15 抽审 P-ID 均在注册表内**：结构 PASS。部分论文仅按原始摘要/已展示方法段核，**E1/PARTIAL**，所有 D02–D15 源码运行 E2 NOT_RUN。G9 D01 chr20 1Mb bcftools/RTG E2 PASS 保留，原 DeepVariant/hap.py NOT_RUN。
- **现有阻断与目标状态**：不处理个人 DNA；没有对 47 篇全文/39 仓库全部依赖/许可证做系统性审计，不假报“全球全部工具或论文”。D0 ALIGNED、与原 Issue Goal/Scope/AC CONSISTENT；G10 唯一进度事件待同步。

## 5. 阻断与未受影响工作
| 问题 | 影响范围 | 对应 AC | 继续可以推进的部分 | 状态 |
|---|---|---|---|---|
| 既有 47 项中剩余 32 项未逐篇全文系统审计、实际医学/统计外推边界不统一 | AC-03/04 的全面证据完整性 | 03/04 | 15 域代表方法已有，可优先审最影响决策的负证据和缺口 | PARTIAL |
| 39 个现有 GitHub 软件许可证/复杂输入及跨祖源模型仍未完成全量运行/审查 | 软件可复用性与输入质量 | 02/04 | 已读取一批 README；对重点 D03/D04/D09/D10 现成方法做有界输入核验 | PARTIAL |
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

## 7. 下一步
- **唯一优先动作**：以 [G10 15 域方法证据清单](cross-domain-method-evidence-audit-g10.md) 中的原有 D03（父系 Y）、D04（mtDNA）、D09（PGx）、D10（PGS/PRS）四个在单份短读长 WGS 上**最可能给研究性个体结果但数据条件不同**的领域为代表，核准**原始文件级输入质量合同与分析深度排序**：每域选择 1 个既有 GitHub 工具，分别写出 `minimum_input/expected_output/callable-quality/external-reference/evidence-grade/license/known-limit` 及 1 份可用公开基准或合法样本是否实际存在的证据；不用个人 DNA，暂不安装运行 4 个完整平台。
- **为何优先及验收**：G10 的 15 域代表性论文已完成方法 E1 横向初审，最大下一步缺口是“实际买到一份 30–40× WGS 能否用现成工具达到该论文的分析层级”。四个领域覆盖 Y/mtDNA/复杂药物基因型/外部统计模型四类完全不同的技术门槛，能形成可用于其余域的统一输入审计模板。必须每域给出处链接和是否可执行的 `PASS/PARTIAL/NOT_RUN/BLOCKED`，不虚构 E2 或承诺个人临床结论。
- **关联未完成 AC**：AC-02 真实软件输入及法律许可，AC-03 原文/方法/反证完整性，AC-04 研究边界和 WGS 质量迁移；AC-06 Draft PR #73 仍未合并。G10 未全审的 32 篇仍排队，不因本轮四域重点失去 15 域总框架。
- **限制**：若原有仓库 README 已能排除输入兼容性，就以静态证据结论止步，不无界部署软件或再建平台；无足够可用公共样本则 E2 NOT_RUN，保留原 Goal/Scope/AC，不上传个人 DNA。

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

## 10. 最近一次状态一致性回读
- **当前 active_event_key**：AI_book#72:AC02-03-04:20261121-g10-15domain-methods
- **当前 writer_owner**：chatgpt-topic017-g10-20261121
- **当前 write_state**：CLAIMED（G10 当前单 Writer 准备唯一 Issue 事件，前 G9 #7062643687 已回读）
- **旧 Writer 停止/隔离**：不适用；首次写入者。
- **无 fencing 不允许第二 Writer 抢占未决 CLAIMED 事件。**

| 检查项 | 当前值 | 证据 | 结果 |
|---|---|---|---|
| Issue Goal/Scope/AC 与 §1 | 合同一致 | 初始 GET #72 | CONSISTENT（内容） |
| §3/§4 与真实证据 | G10 15/15 域代表 P-ID/真实方法和源码输入审计、P005 DOI 修复且 47 DOI/39 repo 去重核对；G9 1Mb E2 保持 | G10 报告/注册表/工具目录与 G9 真实结果 | PARTIAL（15 域方法结构 PASS，其余 E2 NOT_RUN） |
| §5 局部阻断 | 47 篇未全部全文、39 项未全做输入/许可/运行实证；旧 DeepVariant 局部未运行 | G10 15 域代表审计、G9 实测和原 Non-goals | CONSISTENT |
| §6 与 §7 | G10 15 域代表论文/数据/代码审计已完成；下一步 4 种互补个人 WGS 数据契约方法级对照 | G10 一手来源、现有工具和未完成 AC-02/03/04 | CONSISTENT |
| §7 vs §9 历史建议 | 当前下一步唯一 | 本文件 | CONSISTENT |
| Issue 最新事件与 Tracker | G1–G9 原始事件已回读；G10 新事件 CLAIMED 尚待评论回读 | G10 稳定 event_key + 单 Writer 声明 | ISSUE_SYNC_PENDING |

> 只有未来发生**实质进展或状态纠偏**才按协议持久化新检查点和一条事件。写入遵循 `tracker sha/CAS → CLAIMED 单 Writer → Issue 唯一评论 → 回读 → Tracker SYNCED`；不能事后称本次已完成该完整链。
