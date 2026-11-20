# TOPIC-016 · GOAL_TRACKER.md

> 唯一动态跟踪文件（Task Center V1.2.2 L 级试点，非已发布协议）。规范批准目标以 [AI_book Issue #70](https://github.com/fweiger/AI_book/issues/70) 为准；本文件不建立第二套目标。用户可据此跨会话恢复研究。

## 任务身份

- Task ID: `AI-BOOK-TOPIC-016-AI-SOCIAL-CONSCIOUSNESS`
- 规范 Issue: https://github.com/fweiger/AI_book/issues/70
- 所属源仓库: `fweiger/AI_book`
- 研究入口: [首轮核查草稿](../../topics/ai-social-consciousness-transition/initial-claim-audit.md)
- 本文件路径: `task-goals/issue-70/GOAL_TRACKER.md`
- 当前阶段: `M1_FIRST_PASS_PARTIAL`（历史与 AI 证据核对）
- 创建/最近更新: 2026-11-21
- 批准需求: `r0-20261121-user`
- 协议路径/分支: `task-center/v1.2.2/ENTRY.md` @ `experiment/task-center-v1.2.2-continue-goal-guard-20261119`
- **锁定协议 commit SHA**: `f0e5ccb90c54265dcd07abb9a975c903eb031ccf`
- 首次观察分支 HEAD: `f0e5ccb90c54265dcd07abb9a975c903eb031ccf`（后续新 HEAD 不自动升级）
- 最新 Issue 读取时间及修订: 2026-11-21 / `r0-20261121-user`；已 GET 回读 #70 双向链接
- Tracker 当前 blob SHA: 以 GitHub `fetch_file` 实际返回为准；不可在文件中自引用生成 SHA
- 目标漂移: `D0`（首轮核对直接支持 AC-01~03；后续需再次判断）
- 状态一致性: `CONSISTENT`（#70/Tracker/研究文档已双向回读，初始事件正在同步）
- Issue 同步状态: `SYNCED`（规范 Issue 首轮事件已发布并 GET 回读 1 条、Tracker 单 Writer 有效）

## 1. 批准目标基线

- **Goal**: 核查视频作者以生产力、旧权威、媒介、思想生产者四要素解释历史及 AI 社会意识/价值转型的框架；区分史实、因果、类比、规范与预测，形成可持续讨论的问题—论点—证据—反对意见结构。
- **Scope**: 春秋战国、文艺复兴/宗教改革、近代《新青年》、当代 AI 研究；概念辨析及替代解释。
- **Non-goals**: 不预认定「集体意识革命」已发生；不预测自动化时间表；不扩展为其他科技/心理/政策项目；不公开本地转写全文和设备路径；不重做 TOPIC-015。
- **AC 以规范 Issue 的 AC-01~05 原文为准**；文件此处只列简写，不修改验收：
  
| AC | 内容 | 验证方法 | 当前状态 | 证据 |
| --- | --- | --- | --- | --- |
| AC-01 | 忠实重建四条件与逻辑箭头 | 论点-机制-来源表 | PARTIAL | 首轮 audit §1 |
| AC-02 | 不少于三组历史对照/时间/反例 | 逐案例来源核对 | PARTIAL | audit §2 |
| AC-03 | 不少于两份 AI 实证及外推边界 | 原研究样本/方法对照 | PARTIAL | audit §3 |
| AC-04 | 至少两种替代解释与概念争论 | 反证与反对意见 | PARTIAL | audit §4–5（未独立复核） |
| AC-05 | 草稿+来源账本可回读、PR 审查 | GitHub GET+独立复核 | PARTIAL | 当前分支（PR 待验证） |

## 2. 目标贡献

本专题以历史学的时序、社会学机制与哲学上的主体性概念，检验一种新出现的 AI 时代社会解释。目标不是找到大师的替代品，而是检验「独立判断」与「解释权重新分配」是否真正发生。完成标准是**可反驳、可查来源**，不是论断足够宏大。

## 3. 当前执行路径

| 阶段 | 预期结果与 AC | 验证 | 状态 |
| --- | --- | --- | --- |
| M0 建题 | #70 / AC-05 入口 | GitHub Issue GET | PASS |
| M1 逐点查证 | 四条件、历史时序、AI 实证 / AC-01~03 | 来源定位与反例矩阵 | PARTIAL |
| M2 讨论与审阅 | 替代解释、主体性概念、可否证比较 / AC-04~05 | 争论记录、草稿 PR、独立审核 | NOT_RUN |

## 4. 当前检查点

- 最近一轮/本轮实质完成: 从用户提供的原始转写中提取核心机制，获取先秦史、文艺复兴史、教会大分裂、北京大学新文化运动、QJE 2025 与 CHI 2025 的初批来源，建立了首轮 audit 文档。
- 已核验: C03 的印刷传播晚于意大利早期文艺复兴；C04 的 1378 双教皇与后来的第三条线应区分；C06/C07 有岗位/自报级实证而非文明级定论。
- 未验证: 原始程乐松演讲影音；系统性比较/反例；各章完整史料精读；「集体意识革命」的测量定义；独立审稿。
- 对原目标贡献: 直接推进 AC-01~03，预防历史年代错误外推至 AI。
- 目标漂移: `D0`——动作与未完成 AC 直接关联，非围绕单例无限扩展。
- 状态一致性: 已 GET 核对 Issue #70、Tracker、研究草稿及 Draft PR #71；初始基线一致，事件同步仍待完成。

## 5. 阻断与未受影响工作

| 问题 | 影响范围/AC | 不受影响工作 | 决定 |
| --- | --- | --- | --- |
| 未获得程乐松原始影音 | C09 引言出处 / AC-01 局部 | C01–C08 的历史/AI 原研究核查 | 标二手/待核，不阻断核心机制研究 |
| 部分历史著作仅浏览摘要 | AC-02 引用深度局部 | 研究问题、可见时间事实与反例 | 不声称逐章原文核验，后续定向补足 |
| 「集体意识」无可操作定义 | AC-04 | 历史事实与 AI 任务级数据 | 保持 H 假说，下一阶段处理 |

## 6. 路径调整记录

无：保持初始用户授权目标和 AC，新增细节仅作核验路径，不扩展为旁支项目。

## 7. 唯一当前下一步

- **动作**：补读 C01/C02/C03 的至少两份学术章节或原典定位，形成先秦与文艺复兴/宗教改革的「时间—生产/制度—权威—媒介—思想生产者—反例」**可比较因果证据矩阵**。
- **对应 AC**：尚未完成的 AC-01、AC-02；当前 M1。
- **为什么优先**：它直接检验作者四条件是否只是同期并存、还是有可论证的先后和机制；在此之前直接推断 AI 意识革命容易过度推理。
- **可观察交付与成功标准**：在初轮 audit 中新增对照矩阵；每条来源标真实可见章节/摘要、冲突事实、反例与推断等级，至少两历史场景；不允许未经原文核对的直接引语。
- **所需来源**：[SEP Chinese Legalism](https://plato.stanford.edu/entries/chinese-legalism/)、[Met Renaissance](https://www.metmuseum.org/toah/ht/08/eustc.html)、[Cambridge Printing](https://www.cambridge.org/core/books/abs/cambridge-history-of-renaissance-philosophy/conditions-of-enquiry-printing-and-censorship/47FE6DBC2D7D7AB78BA8650431927B25)。
- **若局部来源受阻**：仍可完成另一案例和 C07 概念的对立观点梳理，但不能降低来源真实性标准。
- **终止局部搜索边界**：同一案例两轮无法取得原章节、没有主线证据增量时，切换到已可验证案例并重评优先级；不得把搜不到资料当作新项目。

## 8. 每轮继续前核对

- [ ] GET #70 原批准 Goal/Scope/AC、评论/事件，核对 Task ID。
- [ ] GET 当前 Tracker 与 Git SHA；严格按锁定 commit 读取 V1.2.2 入口与 CONTINUE。
- [ ] 复核实际 source/PR、来源级别与研究证据，不凭旧聊天断言。
- [ ] 独立判断 `D0/D1/D2/UNKNOWN`、`CONSISTENT/STATE_CONFLICT/UNKNOWN` 与阻断边界。
- [ ] 重新选择**一个**最能推进未完成 AC 的动作；按 SHA/CAS 与单 Writer 规则同步新进展。

## 9. 检查点历史（追加）

| 日期/批次 | 已完成 | AC 贡献 | 证据 | 偏差/一致性与阻断 | 当时建议下一步 |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 / initial | 创建 #70；将首轮历史与 AI 来源审计写入专题草稿分支 | AC-01~03 PARTIAL | [Issue #70](https://github.com/fweiger/AI_book/issues/70) / [audit](../../topics/ai-social-consciousness-transition/initial-claim-audit.md) | D0；初次互链回读待核，局部原文未得 | 完成两历史案例的因果矩阵 |
| 2026-11-21 / M1-audit-event | 已 GET 确认 #70/Tracker/PR、唯一 Writer 已在 Tracker CLAIMED 后发布唯一进度事件，并 GET 只发现 1 条同键评论 | AC-01~03 PARTIAL；G1 同步完成 | [event](https://github.com/fweiger/AI_book/issues/70#issuecomment-7053356363)；event_key: `AI-BOOK-TOPIC-016-AI-SOCIAL-CONSCIOUSNESS:M1:initial-evidence-20261121` | D0 / CONSISTENT；原史料/独立审稿未完成 | 下次重新判断当前 AC 优先级 |

## 10. 最近一次状态一致性摘要

- active_event_key: `none`（上一事件已同步完成；历史键见本节下方与 §9）
- writer_owner: `none`（当前无待发布事件声明）
- write_state: `SYNCED`（首轮事件 #7053356363 已核对唯一出现）
- 旧 Writer fencing: 不适用；未来若出现已 CLAIMED 且失联，遵守 V1.2.2 禁止未证明停用的抢占规则。
- 最近一次已同步事件：`AI-BOOK-TOPIC-016-AI-SOCIAL-CONSCIOUSNESS:M1:initial-evidence-20261121` / [GitHub 评论 #7053356363](https://github.com/fweiger/AI_book/issues/70#issuecomment-7053356363)。本次状态 `SYNCED` 仅指本轮 GitHub 写入核对，不代表研究 AC 学术验收通过。

| 项目 | 核对值 | 证据 | 结果 |
| --- | --- | --- | --- |
| Issue 目标 vs §1 | 批准目标/AC 一致 | #70 与 Tracker | PASS |
| §3/4 实证与阶段 | M1 PARTIAL | audit | PASS（状态对照） |
| §5 局部阻断 | 不阻断其余历史核验 | audit | PASS（边界对照） |
| §6/7 | 原始目标不变，唯一下一步是历史因果矩阵 | 本文件 | PASS（状态对照） |
| §7 与 §9 | 历史建议与当前优先动作一致 | 本文件 | PASS（状态对照） |
| Issue 与 PR/Tracker 回链 | #70 / PR #71 / Tracker 可回读；事件评论唯一匹配 | [#70 进度事件](https://github.com/fweiger/AI_book/issues/70#issuecomment-7053356363) | `SYNCED` |
