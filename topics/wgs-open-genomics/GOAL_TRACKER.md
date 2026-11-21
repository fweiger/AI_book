# GOAL_TRACKER.md｜TOPIC-017 / Issue #72 / V1.2.2
> 公开研究主题的**唯一** L 级动态跟踪文件。原批准需求以规范 Issue 为准，本文件不另设第二套需求。
> 创建：2026-11-21；本轮更新：2026-11-21；requirements_revision: 1。

## 任务身份
- 规范任务 Issue：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)
- 所属源仓库：`fweiger/AI_book`
- 项目入口：`topics/wgs-open-genomics/README.md`
- 唯一 Tracker：`topics/wgs-open-genomics/GOAL_TRACKER.md`（本文件）
- 当前阶段：G9 31.5 公开 HG002 chr20 2–3Mb bcftools 1.19 + RTG 3.13 实测 E2 PASS 且独立源码二次复现；G8 数据校验保持 PASS，原 DeepVariant/hap.py 方案仍 NOT_RUN；15 域/47 来源/39 工具仍待科研深审
- 选定协议：`fweiger/AI_tasks/task-center/v1.2.2/ENTRY.md`，原实验候选分支 `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`**（续接仅从锁定版本读取，不自动跟随 HEAD）
- 本轮观察的候选分支 HEAD（协议分支）：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 初始 Issue 验证：2026-11-21，GET #72 内容可读，`requirements_revision: 1`
- 当前 Tracker blob SHA：首次创建后从 GitHub 读取；本文件不自引用当前 SHA
- 目标漂移：`D0 ALIGNED`（G9 使用已有公开数据与轻量官方工具确实验收 AC-05，结束局部 Docker 阻断，重新回归 15 域论文×工具主线）
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
| AC-02 | ≥25 个真实 GitHub 工具及清晰分类、输入用途限制 | 逐仓库 GitHub 元数据；文件回读 | PARTIAL（39 项 GitHub 源码存在性 PASS；许可证分层已有证据，全部运行 NOT_RUN；部分源码并非 OSI 自由开放） | [源码/许可目录](open-source-projects.md) · [G5 审计](cross-domain-evidence-audit-g5.md) |
| AC-03 | ≥10 条原始论文/标准，主题相联 | DOI/原始来源交叉核查；全文审计 | PARTIAL（47 篇去重 DOI/指南；G7 补 6 篇与论文争议回复；完整全文审计未完成） | [论文注册表](paper-register.md) · [G7 审计](cross-domain-evidence-audit-g7.md) |
| AC-04 | ≥8 研究方向及数据/深度/失败边界 | Q-ID 与矩阵逐项核对 | PARTIAL（15/15 域/47 篇/39 仓库静态去重 PASS；真实科学/临床复现仍 NOT_RUN） | [15 域主矩阵](evidence-capability-matrix.md) · [G7 审计](cross-domain-evidence-audit-g7.md) |
| AC-05 | 公共参考基因组最小可复现实验和证据 | GIAB HG002 + 版本化命令与 QC | **PASS（范围受限）：**真实 HG002 chr20 1Mb bcftools1.19/RTG3.13 独立 GIAB v4.2.1 BED 指标和二次运行日志、变异记录/摘要哈希一致；原 DeepVariant/hap.py 单独方案仍 NOT_RUN | [G9 原始结果与复现](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md) · [G9 实际可运行源码](scripts/run-hg002-chr20-bcftools-rtg.sh) |
| AC-06 | 专题分支、唯一 Tracker、审核 PR 和回链 | GitHub 文件、PR、INDEX、CI 校验 | PARTIAL（Draft PR #73/结构 CI PASS，尚待审核合并） | [PR #73](https://github.com/fweiger/AI_book/pull/73) |

## 2. 对上级目标的贡献
- 知识库将遗传研究的技术事实、科研证据及历史叙事放在同一可审计框架；每项使用公共源码和论文链接。
- 成功时读者能回答“有了 WGS，哪些问题在一个人身上能算，哪些必须额外采样/外部临床验证？”
- 最重要的核心问题不是单个 GitHub 仓库能否安装，而是工具、数据和证据如何共同限定研究结论。

## 3. 当前执行路径
| 阶段 | 预期结果 | 对应 AC | 证据 | 状态 | 依赖 |
|---|---|---|---|---|---|
| S1 | 15 域质量→论文→研究深度→GitHub 横向矩阵并入 Draft PR | 01–04/06 | [主矩阵](evidence-capability-matrix.md)、[47 篇论文注册表](paper-register.md)、[G4](cross-domain-evidence-audit.md)/[G5](cross-domain-evidence-audit-g5.md)/[G6](cross-domain-evidence-audit-g6.md) | PARTIAL（跨域输入证据扩展；全部程序实际运算/全文系统审计待完成） | 一致性审计及少量公共样本核验 |
| S2 | HG002 公开数据准入 → 最小 chr20 SNP/Indel E2 | 02/05 | [G8 官方数据/哈希](sessions/2026-11-21-hg002-public-data-admission-g8.md)、[G9 实测和二次复现](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md) | **PASS（仅 G9 chr20 1Mb bcftools/RTG）**，原 DeepVariant/hap.py 未测试 | 与其他 14 研究域的结论真实性独立，下一步恢复论文×源码全域研究 |
| S3 | 15 域论文×WGS 输入×代码/研究结论及许可证可靠性 | 02–04 | [15 域矩阵](evidence-capability-matrix.md)、[G7 全域一致性](cross-domain-evidence-audit-g7.md) | PARTIAL（主矩阵存在；尚缺 15 域各一份方法级证据抽审与外推边界） | G9 公共 E2 与其他领域的理论可行性必须区分，避免只研究 D01 |
| S4 | 跨工具/人群的结果比较、反证和下一版图谱 | 02–05 | 真实运行与来源日志 | TODO | 前期质量基线 |

## 4. 当前检查点
- **G9 核心实测**：[公开 HG002 真实 bcftools/RTG 原始方法、TP/FP/FN、ROC 和 SHA 证据](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md)：31.5 Ubuntu 使用 G8 官方验证数据，在 chr20 2–3Mb 1Mb 上运行 bcftools 1.19/htslib1.19 `mpileup | call` 得到 1899 个变异 VCF 记录，NIST v4.2.1 confident BED 166 段、965991 bp；RTG Tools 3.13 独立 `vcfeval` 成功。
- **未按额外 QUAL cutoff 的结果**：SNP TP-baseline/TP-call=1430/1434、FP7/FN4，Precision 0.9951、Recall 0.9972、F1 0.9962；Indel TP-baseline/TP-call=216/213、FP12/FN17，0.9467/0.9270/0.9367；合计 0.9886/0.9874/0.9880。来自官方真值 BED 范围内真实 RTG ROC 末行，**不能推断全 WGS 或其他 assay、祖源、临床准确率**。
- **源码已二次实测**：[独立最小命令脚本](scripts/run-hg002-chr20-bcftools-rtg.sh)，Git blob `819278d12b78cae97da8f27c4d49a93228b4942d` 下载一致；preflight 和真实 `run exit=0`，两次 callset 非 header 变异记录 SHA256 都是 `472eaed46a664cbb675dc2c09d224d7836c0680345f937100a0a48d6fad912b0`，RTG `summary.txt` SHA256 都是 `24dac88c2c4ad5738ffa6b2d65c3280eabf98eeda79d25a1067fe5308a515ba6`；非假造/模拟。
- **AC/阻断边界**：AC-05 原始批准目标为至少一套公开可复现最小实验，G9 限界通过 **PASS**。旧 G2 固定 DeepVariant/hap.py 完整 chr20 方案仍 NOT_RUN，Docker 大镜像阻断仅此子方案，**不得把 G9 精度冒称 DeepVariant 性能**。其他 14 个研究域论文/算法未据此验证；未接触任何个人 DNA。
- **目标与状态**：D0 ALIGNED，Issue 原 Goal/Scope/Non-goals/AC 保持；停止围绕同类 Docker 故障继续滚动排障，接下来向用户要求的 15 域研究深度回归。G9 唯一事件 [#7062643687](https://github.com/fweiger/AI_book/issues/72#issuecomment-7062643687) 已回读并同步。

## 5. 阻断与未受影响工作
| 情况 | 真实影响 | AC | 主线剩余 | 定性 |
|---|---|---|---|---|
| DeepVariant/hap.py 大镜像之前仍未完整拉取 | 仅 G2 原指定 DeepVariant 对照实验，不影响 G9 原生 bcftools/RTG | AC-05 的**其他方案** | G9 公开 E2 PASS 已满足最小 AC；不重复拉大镜像 | 局部 BLOCKED/NOT_RUN，非整任务阻断 |
| 47 来源没有逐域方法级全文审计，39 项源码实际兼容性/许可证仍待复核 | 跨域科学解释与商业可用性 | AC-02/03/04 | 以现有目录做每域定向证据核查，非盲目增加数量 | PARTIAL，当前优先主线 |
| 个人商业 WGS 文件尚未取得、且按 Non-goals 不进入公开 AI_book | 个人实际数据质量、临床/亲缘分析 | 本轮不进行私人实验 | 统一数据标准及合规公共样本 | NON-GOAL，不触碰个人敏感数据 |
## 6. 执行路径调整记录
| 时间 | 旧候选 | 实际动作/调整 | 证据 | 关联 AC | 范围改变 |
|---|---|---|---|---|---|
| G1–G3 | 初始目录与父系局部 | 确立全域 WGS 质量→论文→工具研究 | 规范 Issue G1–G3 | 01–06 | 否 |
| G4–G7 | 横向论文和源码方法审计 | 完成 15 域研究图谱和原始数据验收合同 | G4–G7 证据文件 | 02/03/04 | 否 |
| **2026-11-21/G8** | 公开 HG002 E2 实验 | 实际完成 HG002 文件 download/hash 官方 BAM MD5；Docker image 两次有界尝试未就绪，止损后不扩建平台 | [G8 真实日志/哈希](sessions/2026-11-21-hg002-public-data-admission-g8.md) | **05 PARTIAL** | 否 |
| **2026-11-21/G9** | 现有 HG002 数据与有界原生工具 | bcftools1.19/RTG3.13 公开 HG002 chr20 1Mb 独立 GIAB/true E2，二次代码实跑变异正文/摘要 SHA 一致；不再修 Docker 大镜像 | [G9 报告](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md)、[源码](scripts/run-hg002-chr20-bcftools-rtg.sh) | **05 PASS（限界）** | 否 |

## 7. 下一步
- **唯一优先动作**：从已有 [15 域证据主矩阵](evidence-capability-matrix.md) 和 [47 项原文来源](paper-register.md)、[39 项源码候选](open-source-projects.md) 中，对 **D01–D15 每域至少 1 篇最能定义方法/结论上限的一手论文/权威标准**进行**方法级抽审**，为每域补 `assay+样本/祖源+质量门槛+分析能推断什么/不能推断什么+源码真实输入/许可证+原文 DOI+证据等级`，公开形成一份 15 行可查清单；不将全部 47 篇逐字阅读说成已完成，不机械新增工具或制造新的任务中心。
- **对应未完成 AC**：AC-03 论文方法/反证的证据深度，AC-04 15 域研究深度和失败边界，AC-02 真实工具输入和许可；AC-06 Draft PR #73 审核与合并仍独立待办。
- **验收**：15/15 域有一手 DOI/标准来源与具体输入条件、统计/医学/祖源外推限制、关联既有真实 GitHub 项目（不适用时明确 NONE/OTHER_ASSAY）及不确定性标记；区分 GitHub 文档能读/E0、方法来源/E1、真实公开运行/E2（目前仅 G9 D01 小区间）。
- **为何重新排序**：G9 已取得 AC-05 真实 E2，继续围绕同一 D01/GIAB 的局部 Docker/系统开发会偏离用户最初提出的**全部方向×论文×开源工具深度图谱**；因此回归横向科学证据审计更直接推进未完成 AC。
- **不改授权**：继续同一个 Issue #72、同一个唯一 Tracker 与 Draft PR #73，不涉及个人 DNA、临床诊断，不更改原 Goal/Scope/AC。
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

## 10. 最近一次状态一致性回读
- **当前 active_event_key**：none（G9 event AI_book#72:AC05:20261121-g9-native-bcftools-rtg-e2 已完成）
- **当前 writer_owner**：none（G9 Writer chatgpt-topic017-g9-20261121 已完成）
- **当前 write_state**：SYNCED（[G9 唯一评论 #7062643687](https://github.com/fweiger/AI_book/issues/72#issuecomment-7062643687) 已 GET 回读且同 key 仅 1 条；事件声明 Tracker blob SHA fa8f8b4c161dc8a6c2fb4827ccfa00d0a7ff412f）
- **旧 Writer 停止/隔离**：不适用；首次写入者。
- **无 fencing 不允许第二 Writer 抢占未决 CLAIMED 事件。**

| 检查项 | 当前值 | 证据 | 结果 |
|---|---|---|---|
| Issue Goal/Scope/AC 与 §1 | 合同一致 | 初始 GET #72 | CONSISTENT（内容） |
| §3/§4 与真实证据 | G9 bcftools1.19/RTG3.13 真实 1Mb 独立 benchmark 与脚本二次复现，SNP/Indel metrics 和两个 SHA 一致 | G9 真实计算源代码、日志和结果报告 | PASS（仅 AC-05 公开 E2）；其余 PARTIAL |
| §5 局部阻断 | DeepVariant/hap.py 尚未成功，仅原固定子方案；G9 原生 bcftools/RTG E2 已成功 | G8 镜像终态和 G9 独立实测 | CONSISTENT |
| §6 与 §7 | G9 公开最小 E2 已通过；下一步回归 15 域每域一篇方法级论文/数据/代码审计 | G9 真实报告和未完成 AC-02/03/04 | CONSISTENT |
| §7 vs §9 历史建议 | 当前下一步唯一 | 本文件 | CONSISTENT |
| Issue 最新事件与 Tracker | G1–G9 已各自唯一回读，G9 评论 #7062643687 GET 确认为单条 | 事件声明 Tracker blob SHA fa8f8b4c161dc8a6c2fb4827ccfa00d0a7ff412f | SYNCED |

> 只有未来发生**实质进展或状态纠偏**才按协议持久化新检查点和一条事件。写入遵循 `tracker sha/CAS → CLAIMED 单 Writer → Issue 唯一评论 → 回读 → Tracker SYNCED`；不能事后称本次已完成该完整链。
