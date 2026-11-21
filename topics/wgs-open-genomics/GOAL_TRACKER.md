# GOAL_TRACKER.md｜TOPIC-017 / Issue #72 / V1.2.2
> 公开研究主题的**唯一** L 级动态跟踪文件。原批准需求以规范 Issue 为准，本文件不另设第二套需求。
> 创建：2026-11-21；本轮更新：2026-11-21；requirements_revision: 1。

## 任务身份
- 规范任务 Issue：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)
- 所属源仓库：`fweiger/AI_book`
- 项目入口：`topics/wgs-open-genomics/README.md`
- 唯一 Tracker：`topics/wgs-open-genomics/GOAL_TRACKER.md`（本文件）
- 当前阶段：15 方向 WGS 数据质量→论文→研究深度→GitHub 证据矩阵 v0.1 已提交；特定 WGS 实验仍 NOT_RUN
- 选定协议：`fweiger/AI_tasks/task-center/v1.2.2/ENTRY.md`，原实验候选分支 `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`**（续接仅从锁定版本读取，不自动跟随 HEAD）
- 本轮观察的候选分支 HEAD（协议分支）：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 初始 Issue 验证：2026-11-21，GET #72 内容可读，`requirements_revision: 1`
- 当前 Tracker blob SHA：首次创建后从 GitHub 读取；本文件不自引用当前 SHA
- 目标漂移：`D0 ALIGNED`（本轮根据用户澄清从 Q03 局部分支回到所有研究域，推进 AC-02/03/04）
- 状态一致性：`CONSISTENT`（Issue #72、PR #73 和 Tracker 合同目标已回读）
- Issue 同步：`SYNCED`（G1 #7059893177、G2 #7060020787 已按不同稳定事件键分别回读）

## 1. 批准目标基线
- **Goal**：建立个人 WGS 开源技术、学术论文、祖源/家谱/古 DNA、健康与复杂性状科研用途的长期可验证知识框架，明确可研究的深度和科学/临床边界。
- **Scope**：技术 QC、变异与基准、Y/mtDNA、IBD、古 DNA、医学/药物/PRS/睡眠/营养、开源项目及权威论文、公开样本实验。
- **Non-goals**：不购买检测，不处理个人原始 DNA，不公开私人健康/家族信息，不作临床诊断，不搭建新系统取代现有软件。
- **核心 AC**：以下完全参照规范 Issue #72 的 AC-01—AC-06。

| AC | 验收 | 验证方法 | 当前 | 证据 |
|---|---|---|---|---|
| AC-01 | 唯一 TOPIC-017 Issue 入口且合理查重 | GitHub 查询并回读 | PASS | [#72](https://github.com/fweiger/AI_book/issues/72) |
| AC-02 | ≥25 个真实 GitHub 工具及清晰分类、输入用途限制 | 逐仓库 GitHub 元数据；文件回读 | PARTIAL（32 项存在性 PASS；15 方向工具关联已建，实际运行 NOT_RUN） | [工具目录](open-source-projects.md) · [交叉矩阵](evidence-capability-matrix.md) |
| AC-03 | ≥10 条原始论文/标准，主题相联 | DOI/原始来源交叉核查；全文审计 | PARTIAL（22 篇具体论文/指南题录与摘要级核验；逐篇全文审计未完成） | [论文注册表](paper-register.md) |
| AC-04 | ≥8 研究方向及数据/深度/失败边界 | Q-ID 与矩阵逐项核对 | PARTIAL（15 域质量/论文/方向/项目关联已提交；待独立证据审计） | [15 域主矩阵](evidence-capability-matrix.md) |
| AC-05 | 公共参考基因组最小可复现实验和证据 | GIAB HG002 + 版本化命令与 QC | PARTIAL（公开参考输入/命令/验收规范已提交；实际运行 NOT_RUN） | [HG002 实验规范](benchmark-hg002.md) |
| AC-06 | 专题分支、唯一 Tracker、审核 PR 和回链 | GitHub 文件、PR、INDEX、CI 校验 | PARTIAL（Draft PR #73/结构 CI PASS，尚待审核合并） | [PR #73](https://github.com/fweiger/AI_book/pull/73) |

## 2. 对上级目标的贡献
- 知识库将遗传研究的技术事实、科研证据及历史叙事放在同一可审计框架；每项使用公共源码和论文链接。
- 成功时读者能回答“有了 WGS，哪些问题在一个人身上能算，哪些必须额外采样/外部临床验证？”
- 最重要的核心问题不是单个 GitHub 仓库能否安装，而是工具、数据和证据如何共同限定研究结论。

## 3. 当前执行路径
| 阶段 | 预期结果 | 对应 AC | 证据 | 状态 | 依赖 |
|---|---|---|---|---|---|
| S1 | 15 域质量→论文→研究深度→GitHub 横向矩阵并入 Draft PR | 01–04/06 | [主矩阵](evidence-capability-matrix.md)、[论文注册表](paper-register.md)、[PR #73](https://github.com/fweiger/AI_book/pull/73) | PARTIAL（草稿已交；学术审计/合并待完成） | 方法证据与源码执行待核 |
| S2 | 公开 GIAB 小范围 benchmark 的完整命令/资源设计 | 02/05 | [HG002 数据契约](benchmark-hg002.md) 与脚本 | PARTIAL | 本环境缺 Docker、公共数据 DNS；真实实验 NOT_RUN |
| S3 | 选择典型父系与医学方向做模型/来源级复核 | 03–05 | [Q03 父系工具核查](y-chromosome-methods.md) | PARTIAL | 待公共 chrY 数据与方法复现 |
| S4 | 跨工具/人群的结果比较、反证和下一版图谱 | 02–05 | 真实运行与来源日志 | TODO | 前期质量基线 |

## 4. 当前检查点
- 本轮成果：新建 [15 域 WGS 质量-论文-深度-工具主矩阵](evidence-capability-matrix.md) 与 [22 篇去重论文注册表](paper-register.md)；与原 32 项 GitHub 候选仓库关联；按各域标记质量准入、样本需求、深度和负证据。
- 原 Issue #72 的研究组织方法已根据用户本轮澄清同步；Goal、Scope、Non-goals、AC 和锁定协议未改变。
- 实际核验：官方 GWAS/PGS Catalog、NIST、PharmCAT 及部分原始论文题录/研究方法；22 篇尚未逐篇完成全文审计；本文献数量不代表全球总数。
- 未完成：32 项源码逐项许可证/运行、GIAB 真实精度、论文深读及 PR 独立审核；本轮没有处理任何个人 DNA。
- 状态：D0 ALIGNED；原来仅优先处理 Q03 父系研究的局部偏向已由用户澄清纠正；以跨领域主矩阵继续 AC-02/03/04。

## 5. 阻断与未受影响工作
| 问题 | 真实范围 | AC | 仍可执行 | 决定 |
|---|---|---|---|---|
| 当前执行环境无 Docker/公网 DNS | 仅限制 HG002 真实 E2 benchmark | AC-05 的真实运行 | 论文、主矩阵、公开方法核查 | 局部 BLOCKED，不扩展为全局阻断 |
| 无个人 DNA | 私人个体推断 | 不影响知识框架 | 合法公开论文和基准 | 不采集私人数据 |
| 论文全文/许可证未全核实 | 结论强度与工具选择 | AC-02/03 | 选不同领域代表案例深读 | PARTIAL，不虚报可运行性 |
## 6. 执行路径调整记录
| 时间 | 原路径 | 调整 | 原因与证据 | 对 AC 的影响 | 是否需要用户批准 |
|---|---|---|---|---|---|
| 2026-11-21 | 新建专题 | 先建证据框架，再用公共参考样本实验 | 保护私人数据 | 不改 Goal/AC | 否 |
| 2026-11-21/G2 | 优先完成 HG002 实验 | 保留已提交的固定复现脚本；实际执行环境受阻时优先推进 Q03 父系公开数据方法 | Docker/DNS 是局部真实阻断，不影响 Y 工具文献审查 | AC-05 设计与 AC-02/03/04 Q03 均推进 | 否 |

## 7. 下一步
- **唯一优先动作**：为 Q03/Y01–Y02 找到许可明确、可核验 accession、参考版本一致且 chrY 覆盖足够的公开男性测序样本，建立 Yleaf / Y-LineageTracker 的相同输入、SNP 位点、参考树版本的可复现交叉验证契约。
- **未满足 AC**：AC-02、AC-03 和 AC-04 中关于父系工具实际适用性、论文证据及研究深度的部分；AC-05 已有设计文档，但 E2 仍 NOT_RUN。
- **验收交付**：公开样本来源/授权、chrY callable SNP 数/参考 build、工具 release 或 commit、输入输出约束、预期对照表和失败条件。
- **依赖**：真实、公开、合法数据；**不依赖**本机 Docker 修复或个人基因组。
- **阻断时继续**：研究 Y-SNP 与 Y-STR TMRCA 的不同统计模型/置信区间来源，不搭建额外设施。
- **优先级依据**：保留 HG002 E2 的环境阻断，优先推进未阻断的原始寻祖研究目标；新增工具项目数量不是本阶段瓶颈。
- **局部止损**：只检索少量可核验公共样本；找不到则写来源缺口，不无限寻找。

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
- **当前 active_event_key**：none（上一 G2 事件 AI_book#72:AC05-Q03:20261121-hg002-spec-ymethod 已完成）
- **当前 writer_owner**：none（G2 Writer 已完成：chatgpt-topic017-continue-20261121）
- **当前 write_state**：SYNCED（[G2 唯一评论 #7060020787](https://github.com/fweiger/AI_book/issues/72#issuecomment-7060020787) 已回读；事件声明 Tracker SHA a1369b6b0cb9db08cde5212df7c436b4cfedc2b9）
- **旧 Writer 停止/隔离**：不适用；首次写入者。
- **无 fencing 不允许第二 Writer 抢占未决 CLAIMED 事件。**

| 检查项 | 当前值 | 证据 | 结果 |
|---|---|---|---|
| Issue Goal/Scope/AC 与 §1 | 合同一致 | 初始 GET #72 | CONSISTENT（内容） |
| §3/§4 与真实证据 | HG002 规范与 Q03 Y 工具证据存在，实际 E2 NOT_RUN | 本次文件与本地预检 | PARTIAL |
| §5 局部阻断 | 当前容器 Docker/DNS 仅阻断此处 E2，Q03 可继续 | 环境实测与资料 | CONSISTENT |
| §6 与 §7 | HG002 设计已成，下一步公开父系 chrY 输入契约 | 本文件 | CONSISTENT |
| §7 vs §9 历史建议 | 当前下一步唯一 | 本文件 | CONSISTENT |
| Issue 最新事件与 Tracker | G1/G2 事件分别唯一回读 | G2 事件声明 Tracker SHA a1369b6b0cb9db08cde5212df7c436b4cfedc2b9 | SYNCED |

> 只有未来发生**实质进展或状态纠偏**才按协议持久化新检查点和一条事件。写入遵循 `tracker sha/CAS → CLAIMED 单 Writer → Issue 唯一评论 → 回读 → Tracker SYNCED`；不能事后称本次已完成该完整链。
