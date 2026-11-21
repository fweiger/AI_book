# GOAL_TRACKER.md｜TOPIC-017 / Issue #72 / V1.2.2
> 公开研究主题的**唯一** L 级动态跟踪文件。原批准需求以规范 Issue 为准，本文件不另设第二套需求。
> 创建：2026-11-21；本轮更新：2026-11-21；requirements_revision: 1。

## 任务身份
- 规范任务 Issue：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)
- 所属源仓库：`fweiger/AI_book`
- 项目入口：`topics/wgs-open-genomics/README.md`
- 唯一 Tracker：`topics/wgs-open-genomics/GOAL_TRACKER.md`（本文件）
- 当前阶段：HG002 chr20 公开基准规范及脚本已提交；Q03 Y 工具方法核查已完成；真实分析 NOT_RUN
- 选定协议：`fweiger/AI_tasks/task-center/v1.2.2/ENTRY.md`，原实验候选分支 `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`**（续接仅从锁定版本读取，不自动跟随 HEAD）
- 本轮观察的候选分支 HEAD（协议分支）：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 初始 Issue 验证：2026-11-21，GET #72 内容可读，`requirements_revision: 1`
- 当前 Tracker blob SHA：首次创建后从 GitHub 读取；本文件不自引用当前 SHA
- 目标漂移：`D0 ALIGNED`（所做工作直接对应 AC-02/03/04/06，尚无局部目标挤占）
- 状态一致性：`CONSISTENT`（Issue #72、PR #73 和 Tracker 合同目标已回读）
- Issue 同步：`SYNCED`（Issue #72 已回读，唯一 event_key 评论 #7059893177 已回读且只有一条）

## 1. 批准目标基线
- **Goal**：建立个人 WGS 开源技术、学术论文、祖源/家谱/古 DNA、健康与复杂性状科研用途的长期可验证知识框架，明确可研究的深度和科学/临床边界。
- **Scope**：技术 QC、变异与基准、Y/mtDNA、IBD、古 DNA、医学/药物/PRS/睡眠/营养、开源项目及权威论文、公开样本实验。
- **Non-goals**：不购买检测，不处理个人原始 DNA，不公开私人健康/家族信息，不作临床诊断，不搭建新系统取代现有软件。
- **核心 AC**：以下完全参照规范 Issue #72 的 AC-01—AC-06。

| AC | 验收 | 验证方法 | 当前 | 证据 |
|---|---|---|---|---|
| AC-01 | 唯一 TOPIC-017 Issue 入口且合理查重 | GitHub 查询并回读 | PASS | [#72](https://github.com/fweiger/AI_book/issues/72) |
| AC-02 | ≥25 个真实 GitHub 工具及清晰分类、输入用途限制 | 逐仓库 GitHub 元数据；文件回读 | PARTIAL（32 项存在性 PASS；适配运行 NOT_RUN） | [工具草稿](open-source-projects.md) |
| AC-03 | ≥10 条原始论文/标准，主题相联 | DOI/原始来源交叉核查；全文审计 | PARTIAL（入口整理 PASS，全文未逐篇阅读） | [论文目录](sources.md) |
| AC-04 | ≥8 研究方向及数据/深度/失败边界 | Q-ID 与矩阵逐项核对 | PARTIAL（框架已入草稿，待独立审查） | [矩阵](research-matrix.md) |
| AC-05 | 公共参考基因组最小可复现实验和证据 | GIAB HG002 + 版本化命令与 QC | PARTIAL（公开参考输入/命令/验收规范已提交；实际运行 NOT_RUN） | [HG002 实验规范](benchmark-hg002.md) |
| AC-06 | 专题分支、唯一 Tracker、审核 PR 和回链 | GitHub 文件、PR、INDEX、CI 校验 | PARTIAL（Draft PR #73/结构 CI PASS，尚待审核合并） | [PR #73](https://github.com/fweiger/AI_book/pull/73) |

## 2. 对上级目标的贡献
- 知识库将遗传研究的技术事实、科研证据及历史叙事放在同一可审计框架；每项使用公共源码和论文链接。
- 成功时读者能回答“有了 WGS，哪些问题在一个人身上能算，哪些必须额外采样/外部临床验证？”
- 最重要的核心问题不是单个 GitHub 仓库能否安装，而是工具、数据和证据如何共同限定研究结论。

## 3. 当前执行路径
| 阶段 | 预期结果 | 对应 AC | 证据 | 状态 | 依赖 |
|---|---|---|---|---|---|
| S1 | 研究框架、32 工具及论文矩阵进入专题 PR | 01–04/06 | [PR #73](https://github.com/fweiger/AI_book/pull/73)、GitHub Actions 结构 PASS | PARTIAL | 审核/论文及工具更深复核尚未完成 |
| S2 | 公开 GIAB 小范围 benchmark 的完整命令/资源设计 | 02/05 | [HG002 数据契约](benchmark-hg002.md) 与脚本 | PARTIAL | 本环境缺 Docker、公共数据 DNS；真实实验 NOT_RUN |
| S3 | 选择典型父系与医学方向做模型/来源级复核 | 03–05 | [Q03 父系工具核查](y-chromosome-methods.md) | PARTIAL | 待公共 chrY 数据与方法复现 |
| S4 | 跨工具/人群的结果比较、反证和下一版图谱 | 02–05 | 真实运行与来源日志 | TODO | 前期质量基线 |

## 4. 当前检查点
- **本轮实际完成**：公开 HG002 35× chr20 BAM、GRCh38 no-alt、NIST GIAB v4.2.1 VCF/BED、DeepVariant 1.10.0、hap.py 0.3.12 的固定复现实验规范；可显式 preflight/fetch/run 的 Bash 脚本；Q03 父系 Yleaf、Y-LineageTracker、yhaplo 的真实输入、版本与年代算法比较。
- **验证事实**：本地脚本 bash -n 和 preflight 成功；官方方法 README/部分论文摘要已读；纠正 yhaplo 的预印本 DOI。没有个人 WGS 数据。
- **未完成**：当前运行环境没有 Docker、Google 公共数据域名 DNS 不可解析；真实 HG002 下载、变异调用和 Precision/Recall/F1 均 NOT_RUN；公开 chrY 对照实验未运行；全文论文与许可证审计未完成。
- **目标贡献**：AC-05 的设计/输入/验收条件有可核文件，AC-02/03/04 获得 Q03 方法证据。
- **目标偏差**：D0 ALIGNED（直接推进未完成 AC，不派生新系统）；**状态一致性**：CONSISTENT（基于 Issue 合同与可读文件；新事件待同步）。

## 5. 阻断与未受影响工作
| 问题 | 实际影响范围 | 对应 AC | 未受影响的研究 | 决定 |
|---|---|---|---|---|
| 本环境无 Docker / Google 数据主机 DNS 失败 | 仅阻断本机 HG002 真正 E2 运行 | AC-05 真实执行 | Q03 公开父系方法、学术论文及数据源审查 | BLOCKED（仅当前计算环境）；不反复拓展运维排查 |
| 当前未取得私人 WGS | 个人基因型解读 | 不影响现有 AC | 全部公开数据及方法研究 | 无须个人样本 |
| 部分工具许可证与论文全文待核 | 工具选型与医学结论 | AC-02/03 | 已明确的技术基线、Q03 脉络 | 标 PARTIAL，不冒充验证 |

## 6. 执行路径调整记录
| 时间 | 原路径 | 调整 | 理由 | 对 AC | 用户批准 |
|---|---|---|---|---|---|
| 2026-11-21 | 新建专题 | 先建证据框架，再用公共参考样本实验 | 最小可验证路径，保护私人数据 | 不改变 Goal/AC | 不需要额外目标变更 |

## 7. 唯一当前下一步
- **唯一优先动作**：在保留 Draft PR #73 待审核的前提下，建立 S2 公共 GIAB HG002 的最小 benchmark 技术规范：accession/许可、GRCh38 reference、软件版本、命令、资源预算、precision/recall；不调用个人数据。
- **对应 AC**：AC-05（公开样本技术验证）；AC-06 的草稿文件/结构 PASS，仍须审核。
- **未完成**：仍无公开数据运行证据；已有结构 CI PASS，不能替代 WGS benchmark。
- **预期交付和判据**：PR URL、结构验证日志及最小实验文档；不虚构 WGS 性能。
- **依赖**：GitHub 草稿与公共参考数据可下载性；无私人样本依赖。
- **替代主线**：若公共测试数据受阻，核查 Q03/Q07 的原始方法论文与仓库参数，不构造冗余系统。
- **优先级理由**：先拿到可审查版本和第一条真实计算证据，优于扩充更多未运行链接。
- **局部边界**：最多按一次明确参数/下载问题进行排查，不能无限开展目录重构。

## 8. 每轮恢复核对
- [ ] 用锁定 `f0e5ccb90c54265dcd07abb9a975c903eb031ccf` 获取 Task Center V1.2.2 入口与续接协议，核对 Sticky Assignment；不自动改协议。
- [ ] 回读规范 [Issue #72](https://github.com/fweiger/AI_book/issues/72) Goal/Scope/AC，最新评论、PR 和本 Tracker SHA。
- [ ] 核查真实源码、论文、数据、实验与 CI 结果，不能仅依本文件自报。
- [ ] 判断目标偏差 D0/D1/D2/UNKNOWN、状态一致性、阻断影响与未完成 AC。
- [ ] 重选唯一优先动作，历史建议只是候选；写入必须 CAS，并遵守单 Writer 事件声明。
- [ ] 不公开个人 WGS、基因型、家族身份和医疗信息。

## 9. 检查点历史（追加，不覆盖）
| 时间/批次 | 实际工作结果 | AC 贡献 | 证据 | 漂移与状态 | 本轮建议下一步 |
|---|---|---|---|---|---|
| 2026-11-21/G1 | Issue #72 已创建回读；确认 32 个 GitHub 项目存在；15 个文件 Draft PR #73 与结构 CI PASS；Issue 已补 PR/Tracker 链接；不含个人数据 | 01–04/06 初步 | [#72](https://github.com/fweiger/AI_book/issues/72)，专题草稿 | D0；初始化待同步 | GIAB HG002 公开基准规范（PR 待审不阻断独立研究） |

## 10. 最近一次状态一致性回读
- **当前 active_event_key**：none（上一事件：AI_book#72:AC01-04-06:20261121-initial-research-draft 已完成）
- **当前 writer_owner**：none（上一事件 Writer：chatgpt-topic017-initial）
- **当前 write_state**：SYNCED（[唯一进度事件](https://github.com/fweiger/AI_book/issues/72#issuecomment-7059893177) 已回读，匹配 event_key 评论 1 条；事件声明 Tracker SHA 为 698f01ed3a3c030925f55692bd595e37fdc3ad17）
- **旧 Writer 停止/隔离**：不适用；首次写入者。
- **无 fencing 不允许第二 Writer 抢占未决 CLAIMED 事件。**

| 检查项 | 当前值 | 证据 | 结果 |
|---|---|---|---|
| Issue Goal/Scope/AC 与 §1 | 合同一致 | 初始 GET #72 | CONSISTENT（内容） |
| §3/§4 与真实证据 | 32 仓库存在，未运行 | GitHub 元数据与文献 | PARTIAL |
| §5 局部阻断 | 无私人数据不妨碍公共基准 | Scope | CONSISTENT |
| §6 与 §7 | 当前路线先专题/后 GIAB | 本文件 | CONSISTENT |
| §7 vs §9 历史建议 | 当前下一步唯一 | 本文件 | CONSISTENT |
| Issue 最新事件与 Tracker | PR #73、索引和 Issue 链接一致；唯一事件 #7059893177 已存在 1 条 | 事件含 Tracker 声明 SHA 698f01ed3a3c030925f55692bd595e37fdc3ad17 | SYNCED |

> 只有未来发生**实质进展或状态纠偏**才按协议持久化新检查点和一条事件。写入遵循 `tracker sha/CAS → CLAIMED 单 Writer → Issue 唯一评论 → 回读 → Tracker SYNCED`；不能事后称本次已完成该完整链。
