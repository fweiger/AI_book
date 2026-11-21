# GOAL_TRACKER.md｜TOPIC-017 / Issue #72 / V1.2.2
> 公开研究主题的**唯一** L 级动态跟踪文件。原批准需求以规范 Issue 为准，本文件不另设第二套需求。
> 创建：2026-11-21；本轮更新：2026-11-21；requirements_revision: 1。

## 任务身份
- 规范任务 Issue：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)
- 所属源仓库：`fweiger/AI_book`
- 项目入口：`topics/wgs-open-genomics/README.md`
- 唯一 Tracker：`topics/wgs-open-genomics/GOAL_TRACKER.md`（本文件）
- 当前阶段：G7 完成 15 域证据/统计/源码一致性审计及 WGS 文件验收契约；15 域、47 篇论文/指南、39 个 GitHub 源码候选；真实 E2 NOT_RUN
- 选定协议：`fweiger/AI_tasks/task-center/v1.2.2/ENTRY.md`，原实验候选分支 `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`**（续接仅从锁定版本读取，不自动跟随 HEAD）
- 本轮观察的候选分支 HEAD（协议分支）：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 初始 Issue 验证：2026-11-21，GET #72 内容可读，`requirements_revision: 1`
- 当前 Tracker blob SHA：首次创建后从 GitHub 读取；本文件不自引用当前 SHA
- 目标漂移：`D0 ALIGNED`（G7 按原唯一下一步完成全域一致性、D01/D15 质量边界与反证审查，推进 AC-02/03/04）
- 状态一致性：`CONSISTENT`（Issue #72、PR #73 和 Tracker 合同目标已回读）
- Issue 同步：`SYNCED`（G1–G5 之前均已回读，G6 #7060913003 以唯一稳定事件键回读）

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
| AC-05 | 公共参考基因组最小可复现实验和证据 | GIAB HG002 + 版本化命令与 QC | PARTIAL（公开参考输入/命令/验收规范已提交；实际运行 NOT_RUN） | [HG002 实验规范](benchmark-hg002.md) |
| AC-06 | 专题分支、唯一 Tracker、审核 PR 和回链 | GitHub 文件、PR、INDEX、CI 校验 | PARTIAL（Draft PR #73/结构 CI PASS，尚待审核合并） | [PR #73](https://github.com/fweiger/AI_book/pull/73) |

## 2. 对上级目标的贡献
- 知识库将遗传研究的技术事实、科研证据及历史叙事放在同一可审计框架；每项使用公共源码和论文链接。
- 成功时读者能回答“有了 WGS，哪些问题在一个人身上能算，哪些必须额外采样/外部临床验证？”
- 最重要的核心问题不是单个 GitHub 仓库能否安装，而是工具、数据和证据如何共同限定研究结论。

## 3. 当前执行路径
| 阶段 | 预期结果 | 对应 AC | 证据 | 状态 | 依赖 |
|---|---|---|---|---|---|
| S1 | 15 域质量→论文→研究深度→GitHub 横向矩阵并入 Draft PR | 01–04/06 | [主矩阵](evidence-capability-matrix.md)、[47 篇论文注册表](paper-register.md)、[G4](cross-domain-evidence-audit.md)/[G5](cross-domain-evidence-audit-g5.md)/[G6](cross-domain-evidence-audit-g6.md) | PARTIAL（跨域输入证据扩展；全部程序实际运算/全文系统审计待完成） | 一致性审计及少量公共样本核验 |
| S2 | 公开 GIAB 小范围 benchmark 的完整命令/资源设计 | 02/05 | [HG002 数据契约](benchmark-hg002.md) 与脚本 | PARTIAL | 本环境缺 Docker、公共数据 DNS；真实实验 NOT_RUN |
| S3 | 跨不同方向论文与 WGS 输入/许可证审计 | 02–04 | [G4](cross-domain-evidence-audit.md) + [G5](cross-domain-evidence-audit-g5.md) + [G6](cross-domain-evidence-audit-g6.md) | PARTIAL（D05/D11/D13 已补；需核查 15 域完整映射的可靠性） | 真实 E2 和学术结论证据仍待审 |
| S4 | 跨工具/人群的结果比较、反证和下一版图谱 | 02–05 | 真实运行与来源日志 | TODO | 前期质量基线 |

## 4. 当前检查点
- **G7 实质完成**：[15 域证据一致性审计](cross-domain-evidence-audit-g7.md)和[WGS 原始数据最小交付/质量验收合同](wgs-data-acceptance-contract.md)已提交；逐文件检查 15 个 D 域、47 个不同 P-ID/DOI、39 个不同 T-ID/GitHub 仓库链接，无重复编号；这是**结构 PASS、方法证据 PARTIAL**，不是生物学真实实验。
- **重点修正**：D01 补 GIAB 273 个复杂医学基因 CMRG、ACMG 技术标准和 PCR-free 文库/深度影响；D15 区分普通短读长人类 DNA WGS 与原生 ONT 长读长修饰检测、RNA-seq、真正的宏基因组；P036 Gauchian 争议纳入 P045 开发者正式回应，结论标条件依赖且未独立测试。
- **实践可用**：按 FASTQ、BAM/CRAM、VCF/gVCF、真实 callable depth、参考构建、chrY/mtDNA/困难基因、下载保存权益形成统一厂商询证字段。没有核验 23魔方/WeGene/华大具体交付达标与否。
- **尚未完成**：47 篇逐篇全文系统审计、39 项全部许可证审查及生物信息学程序执行、GIAB 真实 Precision/Recall、个人基因组分析；全部 E2 NOT_RUN。原 Draft PR #73 未合并。没有保存/公开任何个人 DNA。
- **本轮双门禁**：D0 ALIGNED（G7 对应 AC-02/03/04 且修复已证实证据误读）；Issue 与原批准 Goal/Scope/AC 一致，G7 当前事件待同步。

## 5. 阻断与未受影响工作
| 情况 | 真实影响范围 | AC | 未阻断主线 | 决定 |
|---|---|---|---|---|
| 已知当前容器缺 Docker/公共样本 DNS 不稳定 | HG002 真实 E2 benchmark | AC-05 实测 | 静态输入契约与已有授权计算环境 | 局部 BLOCKED，不无限扩建网络平台 |
| 尚无个人真实 WGS | 个人位点 QC、医学或亲缘结论 | 当前 Non-goals | 公共参考/消费产品书面数据规格 | UNKNOWN，不索取/公开个人数据 |
| 部分 GitHub 许可证受限及 P036/P045 性能争论 | 商业源码迭代与特定复杂位点结论 | AC-02/03/04 | 公开信息核查与可授权替代工具 | 将许可与性能证据分开标记，E2 NOT_RUN |
## 6. 执行路径调整记录
| 日期/轮次 | 原路径 | 本轮已做 | 证据 | 直接 AC | Goal/Scope/AC |
|---|---|---|---|---|---|
| 2026-11-21/G1–G3 | 初始目录/HG002 和父系局部 | 用户澄清扩展至 15 域质量×论文×工具 | [G1–G3 Issue 事件](https://github.com/fweiger/AI_book/issues/72) | 01–06 | 不变 |
| 2026-11-21/G4–G6 | 跨领域代表性研究 | 论文真实数据/算法/许可证和外推限制审查 | G4–G6 的不同研究证据文件 | 02/03/04 | 不变 |
| 2026-11-21/G7 | 15 域证据一致性核验 | 完成全域静态审计、D01/D15 特别纠偏、Gauchian 双方论文及消费者 WGS 原始文件合同 | [G7 审计](cross-domain-evidence-audit-g7.md)、[质量合同](wgs-data-acceptance-contract.md) | 02/03/04 | 不变 |

## 7. 下一步
- **唯一优先动作**：针对已经存在的 [公开 HG002 chr20 benchmark 规范及脚本](benchmark-hg002.md)，以 [WGS 质量/文件验收合同](wgs-data-acceptance-contract.md)作为数据准入，优先完成**最小公开样本 E2 可执行性与实际基准**（仅经允许的数据、匹配 GRCh38/DeepVariant/GIAB v4.2.1 的真值 BED/VCF）。若已有授权运行环境可用，记录真实命令、输入版本、错误与 BED 限界 SNV/Indel precision/recall；否则只将环境限制写成 BLOCKED/NOT_RUN，避免无边界运维排障。
- **未完成 AC 与预期验收**：AC-05 的真实公共参考 E2（之前只有静态规范）；同时验收 AC-02 工具输入及 AC-04 可报告的分析边界。必须以原始日志、具体软件版本、同坐标真值与 callable BED 形成可重现 E2 证据；文档 CI/论文精度不视作本人实验结果。
- **其他待办**：AC-03 仍需系统审计 47 篇全文与冲突证据；AC-06 Draft PR #73 仍待独立审核、尚不合并。与 AC-05 无直接依赖的部分研究可以并行只读进行，但不创建新任务中心或个人基因组数据库。
- **优先级**：15 域文献和工具候选数量已经具备研究框架，最紧缺的是一个实际公开样本的可验证运行，而非继续机械增加第 48 篇论文或第 40 个仓库。
- **授权边界**：只用公开/合法样本和原有 GitHub 任务，绝不读取、上传、发布个人 FASTQ/VCF/CRAM 或亲属资料，不擅自改 Goal/Scope/AC。
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
## 10. 最近一次状态一致性回读
- **当前 active_event_key**：none（上一 G6 事件 AI_book#72:AC02-03-04:20261121-g6-ibd-sleep-exercise 已完成）
- **当前 writer_owner**：none（上一 G6 Writer chatgpt-topic017-g6-20261121 已完成）
- **当前 write_state**：SYNCED（[G6 唯一评论 #7060913003](https://github.com/fweiger/AI_book/issues/72#issuecomment-7060913003) 已 GET 回读，匹配事件键仅 1 条；事件声明 Tracker blob SHA 5fb3131db55727aeeb7bfae16c775951e4448199）
- **旧 Writer 停止/隔离**：不适用；首次写入者。
- **无 fencing 不允许第二 Writer 抢占未决 CLAIMED 事件。**

| 检查项 | 当前值 | 证据 | 结果 |
|---|---|---|---|
| Issue Goal/Scope/AC 与 §1 | 合同一致 | 初始 GET #72 | CONSISTENT（内容） |
| §3/§4 与真实证据 | G6 三域新论文和源码方法证据，41 篇与 39 项可读；E2 NOT_RUN | G6 实际研究文件与唯一 Issue 评论 | PARTIAL |
| §5 局部阻断 | Docker/DNS 仅阻断局部实验；全部文献分析可推进 | PR 与环境约束 | CONSISTENT |
| §6 与 §7 | D05/D11/D13 已审；下一步矩阵全域证据一致性核查 | G6 新文件和原 AC | CONSISTENT |
| §7 vs §9 历史建议 | 当前下一步唯一 | 本文件 | CONSISTENT |
| Issue 最新事件与 Tracker | G1–G6 原始事件各有唯一 event_key，G6 评论 #7060913003 已回读 | G6 声明 Tracker blob SHA 5fb3131db55727aeeb7bfae16c775951e4448199 | SYNCED |

> 只有未来发生**实质进展或状态纠偏**才按协议持久化新检查点和一条事件。写入遵循 `tracker sha/CAS → CLAIMED 单 Writer → Issue 唯一评论 → 回读 → Tracker SYNCED`；不能事后称本次已完成该完整链。
