# GOAL_TRACKER.md｜TOPIC-017 / Issue #72 / V1.2.2
> 公开研究主题的**唯一** L 级动态跟踪文件。原批准需求以规范 Issue 为准，本文件不另设第二套需求。
> 创建：2026-11-21；本轮更新：2026-11-21；requirements_revision: 1。

## 任务身份
- 规范任务 Issue：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)
- 所属源仓库：`fweiger/AI_book`
- 项目入口：`topics/wgs-open-genomics/README.md`
- 唯一 Tracker：`topics/wgs-open-genomics/GOAL_TRACKER.md`（本文件）
- 当前阶段：研究框架初始建档、Draft PR 审核前；技术实测尚未运行
- 选定协议：`fweiger/AI_tasks/task-center/v1.2.2/ENTRY.md`，原实验候选分支 `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`**（续接仅从锁定版本读取，不自动跟随 HEAD）
- 本轮观察的候选分支 HEAD（协议分支）：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 初始 Issue 验证：2026-11-21，GET #72 内容可读，`requirements_revision: 1`
- 当前 Tracker blob SHA：首次创建后从 GitHub 读取；本文件不自引用当前 SHA
- 目标漂移：`D0 ALIGNED`（所做工作直接对应 AC-02/03/04/06，尚无局部目标挤占）
- 状态一致性：`UNKNOWN`（首次写入后待完整 PR/回链回读）
- Issue 同步：`ISSUE_SYNC_PENDING`（初始合同已创建；待 PR 与 Tracker 互链核验）

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
| AC-05 | 公共参考基因组最小可复现实验和证据 | GIAB HG002 + 版本化命令与 QC | NOT_RUN | [研究设计](research-matrix.md) |
| AC-06 | 专题分支、唯一 Tracker、审核 PR 和回链 | GitHub 文件、PR、INDEX、CI 校验 | PARTIAL（分支/文件正在入库、PR 待建） | [#72](https://github.com/fweiger/AI_book/issues/72) |

## 2. 对上级目标的贡献
- 知识库将遗传研究的技术事实、科研证据及历史叙事放在同一可审计框架；每项使用公共源码和论文链接。
- 成功时读者能回答“有了 WGS，哪些问题在一个人身上能算，哪些必须额外采样/外部临床验证？”
- 最重要的核心问题不是单个 GitHub 仓库能否安装，而是工具、数据和证据如何共同限定研究结论。

## 3. 当前执行路径
| 阶段 | 预期结果 | 对应 AC | 证据 | 状态 | 依赖 |
|---|---|---|---|---|---|
| S1 | 研究框架、32 工具及论文矩阵进入专题 PR | 01–04/06 | 专题草稿与 #72 | PARTIAL | PR 回链与结构检查 |
| S2 | 公开 GIAB 小范围 benchmark 的完整命令/资源设计 | 02/05 | 公开基准/软件版本记录 | TODO | 不需要私人数据 |
| S3 | 选择典型父系与医学方向做模型/来源级复核 | 03–05 | Q03/Q07 研究笔记 | TODO | 数据许可与合法公开样本 |
| S4 | 跨工具/人群的结果比较、反证和下一版图谱 | 02–05 | 真实运行与来源日志 | TODO | 前期质量基线 |

## 4. 当前检查点
- 最近完成：2026-11-21 研究主题立项和首轮工具/论文框架核查。
- 本轮实际成果：Issue #72 已建且 GET 回读；32 个 GitHub repo 存在性检查；知识目录、图谱及草稿材料创建。
- 经证实：GitHub 中 32 项仓库存在（Manta 已归档）；权威论文/数据库存在；无私有样本输入。
- 尚未验证：32 项算法的可运行/实际质量/许可证细节、逐论文全文、GIAB 真值 benchmark、PR 结构 CI（初始化时）。
- 目标贡献：直接对应原 Goal 的工具、论文、深度研究框架，而非局部排障。
- 漂移：D0；状态：UNKNOWN（等待 PR 与 Issue/Tracker 回读）。

## 5. 阻断与未受影响工作
| 问题 | 影响范围 | 影响 AC | 未受影响仍能继续 | 决定 |
|---|---|---|---|---|
| 目前没有个人 WGS 数据 | 真实个人推断 | 不影响 01–04/06；05 用公共样本 | 文献、公开 GIAB 基准 | 不申请用户私人 DNA |
| 未完成独立端到端实验 | 真实算法表现 | 05 | 分类和证据矩阵 | 诚实标 NOT_RUN |
| 具体工具许可证和版本未细审 | 软件选型 | 02/05 | 原始论文整理 | 后续按实际使用工具逐一核查 |

## 6. 执行路径调整记录
| 时间 | 原路径 | 调整 | 理由 | 对 AC | 用户批准 |
|---|---|---|---|---|---|
| 2026-11-21 | 新建专题 | 先建证据框架，再用公共参考样本实验 | 最小可验证路径，保护私人数据 | 不改变 Goal/AC | 不需要额外目标变更 |

## 7. 唯一当前下一步
- **唯一优先动作**：完成 TOPIC-017 草稿 PR 的索引/结构校验与回链，然后把 S2 的 GIAB HG002 最小 benchmark 输入数据、软件版本、命令和性能指标固化为可运行规范。
- **对应 AC**：AC-06（草稿交付与验收）→ AC-05（公共样本可复现技术验证）。
- **未完成**：仍无公开数据运行证据、没有完整 CI 验收。
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
| 2026-11-21/G1 | Issue #72 已创建回读；确认 32 个 GitHub 项目存在；论文/问题框架及专题草稿写入独立分支；不含个人数据 | 01–04/06 初步 | [#72](https://github.com/fweiger/AI_book/issues/72)，专题草稿 | D0；初始化待同步 | PR 审核/结构检查 → GIAB 小样本基准 |

## 10. 最近一次状态一致性回读
- **当前 active_event_key**：none
- **当前 writer_owner**：none
- **当前 write_state**：NONE（尚未发布任务进度事件；本文件第一次创建，不虚称 SYNCED）
- **旧 Writer 停止/隔离**：不适用；首次写入者。
- **无 fencing 不允许第二 Writer 抢占未决 CLAIMED 事件。**

| 检查项 | 当前值 | 证据 | 结果 |
|---|---|---|---|
| Issue Goal/Scope/AC 与 §1 | 合同一致 | 初始 GET #72 | CONSISTENT（内容） |
| §3/§4 与真实证据 | 32 仓库存在，未运行 | GitHub 元数据与文献 | PARTIAL |
| §5 局部阻断 | 无私人数据不妨碍公共基准 | Scope | CONSISTENT |
| §6 与 §7 | 当前路线先专题/后 GIAB | 本文件 | CONSISTENT |
| §7 vs §9 历史建议 | 当前下一步唯一 | 本文件 | CONSISTENT |
| Issue 最新事件与 Tracker | 初始尚无正式同步事件 | 待 PR 回链 | ISSUE_SYNC_PENDING |

> 只有未来发生**实质进展或状态纠偏**才按协议持久化新检查点和一条事件。写入遵循 `tracker sha/CAS → CLAIMED 单 Writer → Issue 唯一评论 → 回读 → Tracker SYNCED`；不能事后称本次已完成该完整链。
