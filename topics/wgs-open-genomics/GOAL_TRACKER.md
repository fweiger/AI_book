# GOAL_TRACKER.md｜TOPIC-017 / Issue #72 / V1.2.2
> 公开研究主题的**唯一** L 级动态跟踪文件。原批准需求以规范 Issue 为准，本文件不另设第二套需求。
> 创建：2026-11-21；本轮更新：2026-11-21；requirements_revision: 1。

## 任务身份
- 规范任务 Issue：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)
- 所属源仓库：`fweiger/AI_book`
- 项目入口：`topics/wgs-open-genomics/README.md`
- 唯一 Tracker：`topics/wgs-open-genomics/GOAL_TRACKER.md`（本文件）
- 当前阶段：G8 在 31.5 实际完成 HG002 chr20 官方公开 BAM/参考/真值 8 文件下载、全部 SHA-256 复核和 BAM 官方 GCS MD5 对照；DeepVariant/hap.py 镜像未成功，实际变异评分 E2 NOT_RUN
- 选定协议：`fweiger/AI_tasks/task-center/v1.2.2/ENTRY.md`，原实验候选分支 `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`**（续接仅从锁定版本读取，不自动跟随 HEAD）
- 本轮观察的候选分支 HEAD（协议分支）：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 初始 Issue 验证：2026-11-21，GET #72 内容可读，`requirements_revision: 1`
- 当前 Tracker blob SHA：首次创建后从 GitHub 读取；本文件不自引用当前 SHA
- 目标漂移：`D0 ALIGNED`（G8 执行原 AC-05 公共 HG002 真实数据准入，限定镜像下载尝试并停止重复排障）
- 状态一致性：`CONSISTENT`（Issue #72、PR #73 和 Tracker 合同目标已回读）
- Issue 同步：`SYNCED`（G1–G6 先前均已回读；G7 唯一事件 #7061902307 已按稳定事件键回读）

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
| AC-05 | 公共参考基因组最小可复现实验和证据 | GIAB HG002 + 版本化命令与 QC | PARTIAL（8 项真实公开文件下载、本地 SHA256 全通过、官方 BAM MD5 对照 PASS；镜像拉取未完成，变异调用及 Precision/Recall NOT_RUN） | [G8 真实数据准入证据](sessions/2026-11-21-hg002-public-data-admission-g8.md) · [实验规范](benchmark-hg002.md) |
| AC-06 | 专题分支、唯一 Tracker、审核 PR 和回链 | GitHub 文件、PR、INDEX、CI 校验 | PARTIAL（Draft PR #73/结构 CI PASS，尚待审核合并） | [PR #73](https://github.com/fweiger/AI_book/pull/73) |

## 2. 对上级目标的贡献
- 知识库将遗传研究的技术事实、科研证据及历史叙事放在同一可审计框架；每项使用公共源码和论文链接。
- 成功时读者能回答“有了 WGS，哪些问题在一个人身上能算，哪些必须额外采样/外部临床验证？”
- 最重要的核心问题不是单个 GitHub 仓库能否安装，而是工具、数据和证据如何共同限定研究结论。

## 3. 当前执行路径
| 阶段 | 预期结果 | 对应 AC | 证据 | 状态 | 依赖 |
|---|---|---|---|---|---|
| S1 | 15 域质量→论文→研究深度→GitHub 横向矩阵并入 Draft PR | 01–04/06 | [主矩阵](evidence-capability-matrix.md)、[47 篇论文注册表](paper-register.md)、[G4](cross-domain-evidence-audit.md)/[G5](cross-domain-evidence-audit-g5.md)/[G6](cross-domain-evidence-audit-g6.md) | PARTIAL（跨域输入证据扩展；全部程序实际运算/全文系统审计待完成） | 一致性审计及少量公共样本核验 |
| S2 | HG002 公开数据准入 → 最小 chr20 SNP/Indel E2 | 02/05 | [G8 下载/哈希实证](sessions/2026-11-21-hg002-public-data-admission-g8.md)、[规范与脚本](benchmark-hg002.md) | PARTIAL（输入真实 PASS；Docker 镜像未就绪；E2 NOT_RUN） | 31.5 Docker/DNS 已可用，新的局部阻断仅为镜像下载完成与精度实跑 |
| S3 | 跨不同方向论文与 WGS 输入/许可证审计 | 02–04 | [G4](cross-domain-evidence-audit.md) + [G5](cross-domain-evidence-audit-g5.md) + [G6](cross-domain-evidence-audit-g6.md) | PARTIAL（D05/D11/D13 已补；需核查 15 域完整映射的可靠性） | 真实 E2 和学术结论证据仍待审 |
| S4 | 跨工具/人群的结果比较、反证和下一版图谱 | 02–05 | 真实运行与来源日志 | TODO | 前期质量基线 |

## 4. 当前检查点
- **G8 实质成果**：[31.5 真实公共 HG002 数据下载/字节校验记录](sessions/2026-11-21-hg002-public-data-admission-g8.md) 已提交。按原锁定脚本数据清单下载 8 项公开文件，`fetch exit=0`、`sha256sum -c` 全 PASS、压缩文件 `gzip -t` PASS；Google 官方 GCS BAM MD5 与本地完全一致。未上传任何 DNA 至公开 GitHub。
- **脚本真实性**：运行前获取的原脚本 Git blob SHA `fdb01d3f8ccd4996af23110678f713d777ceff07` 与仓库一致，preflight/b​ash-n PASS；原脚本真实下载中发现续传缺口后，临时复制增加 curl resume，真实 .part 从 422596608 bytes 续传成功；已将一个 `--continue-at -` 参数最小修复到同一 PR 脚本，修后 blob `e74f5b29f5a1e62acc9be3827a2733cd9cd06435`。
- **运行限制**：31.5 Docker 29.1.3、16 CPU、磁盘和公开 GCS/NCBI 连通；前轮报告的**此容器无 Docker/DNS 不再是全局或 31.5 阻断**。`google/deepvariant:1.10.0` 第一次镜像拉取超时，有限续拉及 hap.py 镜像拉取均未取得最终 digest；本轮明确停止，并复核全部 Job terminal，不能宣称镜像 ready/基准成功。
- **科研级别**：`DATA_ADMISSION_PASS`；`CONTAINER_IMAGE_BLOCKED`；`DEEPVARIANT_NOT_RUN`；`HAP_PY_NOT_RUN`；无 TP/FP/FN、Precision/Recall/F1；AC-05 仍 PARTIAL/NOT_RUN（算法部分）。15 域/47 论文/39 源码目录不变。
- **目标与状态**：D0 ALIGNED，按原 Goal 完成 AC-05 的必要真实数据进展；唯一规范 Issue 原 Goal/Scope/AC 不变，E2 阻断只影响实际 benchmark。G8 新单 Writer 事件待发布。

## 5. 阻断与未受影响工作
| 问题 | 影响范围 | AC | 不受影响工作 | 本轮判断 |
|---|---|---|---|---|
| DockerHub 镜像层多次有进度但均未取得最终 digest，拉取进程已停止 | DeepVariant/hap.py 实际 chr20 E2 | AC-05 真实 caller/benchmark | HG002 已在 31.5 完整、可复算 hash；其余 15 域研究 | **局部 BLOCKED**；禁止继续无界 Docker 镜像/代理排障 |
| 某些环境无 Docker 或 DNS | 限该环境可执行性 | 不影响 31.5 数据接入 PASS | 已授权 31.5 与公共学术研究 | 旧范围限定，不得继续声称全系统无法联网 |
| 个人商业 WGS 尚无 | 个人位点和医学判断 | 本轮 Non-goals | 公开 HG002 和论文/算法准入研究 | 不采集、不公开个人 DNA |

## 6. 执行路径调整记录
| 时间 | 旧候选 | 实际动作/调整 | 证据 | 关联 AC | 范围改变 |
|---|---|---|---|---|---|
| G1–G3 | 初始目录与父系局部 | 确立全域 WGS 质量→论文→工具研究 | 规范 Issue G1–G3 | 01–06 | 否 |
| G4–G7 | 横向论文和源码方法审计 | 完成 15 域研究图谱和原始数据验收合同 | G4–G7 证据文件 | 02/03/04 | 否 |
| **2026-11-21/G8** | 公开 HG002 E2 实验 | 实际完成 HG002 文件 download/hash 官方 BAM MD5；Docker image 两次有界尝试未就绪，止损后不扩建平台 | [G8 真实日志/哈希](sessions/2026-11-21-hg002-public-data-admission-g8.md) | **05 PARTIAL** | 否 |

## 7. 下一步
- **唯一优先动作**：利用已存 31.5 且经官方 BAM MD5/本地 SHA256 核验的 HG002 chr20 数据，做**一次有界的现有轻量开源变异调用和 GIAB v4.2.1 区域基准执行路径核验**：优先寻找机器现有可直接用的已授权原生工具或小镜像（不得重拉刚才失败的大镜像、不得安装常驻平台）；若能跑通，记录软件版本、输入、命令与按 SNP/INDEL 区分的真实 TP/FP/FN/Precision/Recall/F1；若不可行，明确 `E2 BLOCKED`，将主线切回未完成 AC-03 论文方法级审查。
- **对应 AC**：AC-05 公共真实 E2 执行和失败证据；AC-02 输入/许可证实操；AC-03 体系论文核查为局部 E2 无法推进的替代未阻断主线。
- **成功标准**：至少一个**非模拟**小变异 query callset、与官方 GIAB v4.2.1 truth+confident BED 对齐的独立 caller/benchmark 输出及完整日志；不能用 GIAB truth 自己对自己评分、不能填论文结果、不能以 preflight/镜像层校验冒充真实科学精度。
- **结束条件**：如果环境缺少轻量现成方法或数据兼容性不足，只将阻断写到 AC-05，不再追求更多镜像代理、服务器或者重复启动不受控异步任务。
- **权限/边界**：只用公开合法样本和原既有 Issue/Tracker/PR，私有 DNA 不公开；不改用户原 Goal/Scope/AC。
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

## 10. 最近一次状态一致性回读
- **当前 active_event_key**：AI_book#72:AC05:20261121-g8-hg002-data-admission
- **当前 writer_owner**：chatgpt-topic017-g8-20261121
- **当前 write_state**：CLAIMED（G8 当前唯一事件待规范 Issue 评论与 GET 回读；此前 G7 已完成）
- **旧 Writer 停止/隔离**：不适用；首次写入者。
- **无 fencing 不允许第二 Writer 抢占未决 CLAIMED 事件。**

| 检查项 | 当前值 | 证据 | 结果 |
|---|---|---|---|
| Issue Goal/Scope/AC 与 §1 | 合同一致 | 初始 GET #72 | CONSISTENT（内容） |
| §3/§4 与真实证据 | G8 公开 HG002 8 输入下载/哈希及官方 MD5 PASS，DeepVariant/hap.py E2 NOT_RUN | 本轮 31.5 实际运行证据与 G8 日志 | PARTIAL |
| §5 局部阻断 | 31.5 数据端解除旧 DNS/Docker 阻断；镜像未取得 digest 只阻断调用/评分 | 实测 31.5 环境、Job 终态 | CONSISTENT |
| §6 与 §7 | G8 数据下载成功；下一步优先有界轻量公开基准而非 Docker 无限重试 | G8 日志与原 AC-05 | CONSISTENT |
| §7 vs §9 历史建议 | 当前下一步唯一 | 本文件 | CONSISTENT |
| Issue 最新事件与 Tracker | G1–G7 已回读；G8 CLAIMED 待评论及回读 | G8 event_key + Writer 声明 | ISSUE_SYNC_PENDING |

> 只有未来发生**实质进展或状态纠偏**才按协议持久化新检查点和一条事件。写入遵循 `tracker sha/CAS → CLAIMED 单 Writer → Issue 唯一评论 → 回读 → Tracker SYNCED`；不能事后称本次已完成该完整链。
