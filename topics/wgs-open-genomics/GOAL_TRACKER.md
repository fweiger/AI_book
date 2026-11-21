# GOAL_TRACKER.md｜TOPIC-017 / Issue #72 / V1.2.2
> 公开研究主题的**唯一** L 级动态跟踪文件。原批准需求以规范 Issue 为准，本文件不另设第二套需求。
> 创建：2026-11-21；本轮更新：2026-11-21；requirements_revision: 1。

## 任务身份
- 规范任务 Issue：[AI_book #72](https://github.com/fweiger/AI_book/issues/72)
- 所属源仓库：`fweiger/AI_book`
- 项目入口：`topics/wgs-open-genomics/README.md`
- 唯一 Tracker：`topics/wgs-open-genomics/GOAL_TRACKER.md`（本文件）
- 当前阶段：G5 完成 D02/D04/D08 跨领域文献×源码×许可证审计；15 域、36 篇注册论文、39 个 GitHub 源码候选（并非全部开放许可）；真实 WGS E2 NOT_RUN
- 选定协议：`fweiger/AI_tasks/task-center/v1.2.2/ENTRY.md`，原实验候选分支 `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`**（续接仅从锁定版本读取，不自动跟随 HEAD）
- 本轮观察的候选分支 HEAD（协议分支）：`f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 初始 Issue 验证：2026-11-21，GET #72 内容可读，`requirements_revision: 1`
- 当前 Tracker blob SHA：首次创建后从 GitHub 读取；本文件不自引用当前 SHA
- 目标漂移：`D0 ALIGNED`（G5 横向覆盖此前未深审的 D02/D04/D08，直接推进 AC-02/03/04）
- 状态一致性：`CONSISTENT`（Issue #72、PR #73 和 Tracker 合同目标已回读）
- Issue 同步：`SYNCED`（G1 #7059893177、G2 #7060020787、G3 #7060148978、G4 #7060387293 分别按稳定事件键回读）

## 1. 批准目标基线
- **Goal**：建立个人 WGS 开源技术、学术论文、祖源/家谱/古 DNA、健康与复杂性状科研用途的长期可验证知识框架，明确可研究的深度和科学/临床边界。
- **Scope**：技术 QC、变异与基准、Y/mtDNA、IBD、古 DNA、医学/药物/PRS/睡眠/营养、开源项目及权威论文、公开样本实验。
- **Non-goals**：不购买检测，不处理个人原始 DNA，不公开私人健康/家族信息，不作临床诊断，不搭建新系统取代现有软件。
- **核心 AC**：以下完全参照规范 Issue #72 的 AC-01—AC-06。

| AC | 验收 | 验证方法 | 当前 | 证据 |
|---|---|---|---|---|
| AC-01 | 唯一 TOPIC-017 Issue 入口且合理查重 | GitHub 查询并回读 | PASS | [#72](https://github.com/fweiger/AI_book/issues/72) |
| AC-02 | ≥25 个真实 GitHub 工具及清晰分类、输入用途限制 | 逐仓库 GitHub 元数据；文件回读 | PARTIAL（39 项 GitHub 源码存在性 PASS；许可证分层已有证据，全部运行 NOT_RUN；部分源码并非 OSI 自由开放） | [源码/许可目录](open-source-projects.md) · [G5 审计](cross-domain-evidence-audit-g5.md) |
| AC-03 | ≥10 条原始论文/标准，主题相联 | DOI/原始来源交叉核查；全文审计 | PARTIAL（36 篇去重原始论文/指南入口，D02/D04/D08 新增 11 篇；逐篇全面系统审计未完成） | [论文注册表](paper-register.md) · [G5 审计](cross-domain-evidence-audit-g5.md) |
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
| S1 | 15 域质量→论文→研究深度→GitHub 横向矩阵并入 Draft PR | 01–04/06 | [主矩阵](evidence-capability-matrix.md)、[36 篇论文注册表](paper-register.md)、[G4 审计](cross-domain-evidence-audit.md) 与 [G5 审计](cross-domain-evidence-audit-g5.md) | PARTIAL（9 个代表领域已有方法审计，WGS 真实 E2/全文系统审计待做） | 代码真实运行和较弱领域来源待核 |
| S2 | 公开 GIAB 小范围 benchmark 的完整命令/资源设计 | 02/05 | [HG002 数据契约](benchmark-hg002.md) 与脚本 | PARTIAL | 本环境缺 Docker、公共数据 DNS；真实实验 NOT_RUN |
| S3 | 跨不同方向论文与 WGS 输入/许可证审计 | 02–04 | [G4](cross-domain-evidence-audit.md) + [G5](cross-domain-evidence-audit-g5.md) | PARTIAL（D02/D04/D08 纳入，高优先剩余 D05/D11/D13） | 待全领域证据密度和源码实际效果检验 |
| S4 | 跨工具/人群的结果比较、反证和下一版图谱 | 02–05 | 真实运行与来源日志 | TODO | 前期质量基线 |

## 4. 当前检查点
- 本轮研究实质：新增 [G5 SV/STR、母系 mtDNA、隐性携带者论文×源码审计](cross-domain-evidence-audit-g5.md)，新核 11 篇论文/指南 P026–P036 和 5 个 GitHub 源码候选 T35–T39，合计**36 篇、39 个仓库、15 域**；并非全世界总量或全部具开源许可。
- 关键方法判断：GIAB SV 12,745 ≥50bp DEL/INS 真值不涵盖全部复杂结构；Mutserve 的 mtDNA VCF 暂不输出 indel，低异质性需防 NUMTs/污染；2021/2024 ACMG 指南要求报告阴性残余风险，假基因复杂位点需补检。
- 关键许可纠偏：原 T16 ExpansionHunter 和 T39 Gauchian 为 **PolyForm Strict**；T38 InterVar README 明确仅非商业免费；T35 Truvari MIT、T36 MToolBox GPL-3.0、T37 Mutserve MIT。**源码在 GitHub 可见 ≠ 所有项目均允许自由修改分发/商用。**
- 本轮来源：NIST、ACMG、PubMed/期刊公开论文；5 个新 GitHub 仓库的 README/许可文件已读；总计 36 篇不意味着全文全部审核完。
- 仍未完成：任何 WGS 真实运行、GIAB SV/mtDNA heteroplasmy/carrier 独立基准、所有工具发行版兼容性和临床验证；Draft PR 尚未合并；没有获取个人 DNA。
- 目标 D0 ALIGNED，状态证据与 Issue Goal/Scope/AC 一致，单 Writer G5 事件待发布回读。

## 5. 阻断与未受影响工作
| 风险 | 实际影响范围 | AC | 不受影响主线 | 当前决定 |
|---|---|---|---|---|
| 当前环境缺 Docker/公网数据 DNS | GIAB/HG002 E2 真实运行 | AC-05 的真实计算 | 论文/开源许可/研究上限审计 | 局部 BLOCKED，不能升级全局 |
| 没有私人 WGS | 个人基因型推断 | 不影响研究资料整理 | 合法公开论文和数据 | 不采集私人 DNA |
| 核心位点不可判读、公开源码有非 OSI 许可 | 工具复用与医学可行动性 | AC-02/03/04 | 独立选择兼容和有授权实现 | 记录候选限制，必要时替代软件；不做临床报告 |
## 6. 执行路径调整记录
| 日期/轮次 | 旧候选优先 | 新动作或状态 | 真实依据 | AC | 是否改用户目标 |
|---|---|---|---|---|---|
| 2026-11-21/G1 | 初始知识库 | 整理开源候选与公开参考基准 | 原始 Goal/Scope/AC | 01–06 | 否 |
| 2026-11-21/G2 | 运行 GIAB chr20 | 局部环境阻断时核查 Q03 父系方法 | 容器无 Docker / 公共数据 DNS；不影响其他研究 | 02/03/05 | 否 |
| 2026-11-21/G3 | Q03 单一方向 | 横向数据质量→论文→研究深度→GitHub | 用户明确澄清，父系只是一个方向 | 02/03/04 | 否 |
| 2026-11-21/G4 | 六领域样例论文审计 | 完成六领域真实论文/源码对照并修正 PRS/PGx/HLA 错误输入假设 | 原文与官方 README/许可，交叉矩阵可核查 | 02/03/04 | 否 |

## 7. 下一步
- **唯一优先动作**：从尚未审计的 D02 结构变异/重复序列、D04 mtDNA、D08 生殖携带者方向，各选择至少一个可核论文与真实开源方法，形成同一类带样本输入、参考构建、变异 QC、可解释深度和负证据的横向审计，优先补质量与研究证据缺口而非单一父系或盲目增加软件数量。
- **未满足的 AC**：AC-02 项目全量适用性/许可证/实测；AC-03 全文方法审计；AC-04 多研究域证据深度；AC-05 正式基准运行仍 NOT_RUN；AC-06 PR 仅草稿未合并。
- **验收交付**：每个新增案例的权威论文 DOI、研究数据类型与样本数、最小 WGS 质量准入、开源实现和输入输出、参考版本、许可证/维护状态、可证实与不可证实结论；未知标 UNKNOWN。
- **依赖/风险**：仅公开可访问论文、源代码和合规参考数据；不使用个人/家族隐私 DNA，不启用外部服务、不更改批准 Goal/Scope/AC。
- **优先级理由**：G4 六领域已找到实际兼容性问题；其他高价值方向仍有空白。继续扩展**横向证据覆盖**比解决已经局部阻断的 GIAB Docker 或只研究父系更能推进原始目标。
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
- **当前 active_event_key**：none（最近完成 AI_book#72:AC02-03-04:20261121-g4-source-input-audit）
- **当前 writer_owner**：none（上一 G4 Writer chatgpt-topic017-g4-audit-20261121 已完成）
- **当前 write_state**：SYNCED（[G4 唯一事件 #7060387293](https://github.com/fweiger/AI_book/issues/72#issuecomment-7060387293) GET 回读且匹配键仅一条；事件声明 Tracker blob SHA 6cc8bb803af0a9c3d2425ecbe01ba290e8e8a193）
- **旧 Writer 停止/隔离**：不适用；首次写入者。
- **无 fencing 不允许第二 Writer 抢占未决 CLAIMED 事件。**

| 检查项 | 当前值 | 证据 | 结果 |
|---|---|---|---|
| Issue Goal/Scope/AC 与 §1 | 合同一致 | 初始 GET #72 | CONSISTENT（内容） |
| §3/§4 与真实证据 | 六领域审计/25 篇/34 工具已入 Draft PR；E2 NOT_RUN | 实际文件、来源核查 | PARTIAL |
| §5 局部阻断 | Docker/DNS 仅阻断局部实验；全部文献分析可推进 | PR 与环境约束 | CONSISTENT |
| §6 与 §7 | G4 六领域已审，下一步向未审 D02/D04/D08 横向推进 | 本轮审计与未完成 AC | CONSISTENT |
| §7 vs §9 历史建议 | 当前下一步唯一 | 本文件 | CONSISTENT |
| Issue 最新事件与 Tracker | G1/G2/G3/G4 各自唯一事件已回读；§9 的 G2/G3 历史缺口已按原 Issue 事件补录 | G4 事件声明 Tracker blob SHA 6cc8bb803af0a9c3d2425ecbe01ba290e8e8a193 | SYNCED |

> 只有未来发生**实质进展或状态纠偏**才按协议持久化新检查点和一条事件。写入遵循 `tracker sha/CAS → CLAIMED 单 Writer → Issue 唯一评论 → 回读 → Tracker SYNCED`；不能事后称本次已完成该完整链。
