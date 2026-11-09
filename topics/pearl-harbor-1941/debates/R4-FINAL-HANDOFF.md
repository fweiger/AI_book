# DEBATE-001｜R4-FINAL 独立裁判终审任务书

- 版本：2026-11-04
- 当前入口：[GitHub Issue #18](https://github.com/fweiger/AI_book/issues/18)
- **程序核验：正反方R1、R2、R3均已有实际发言；R4-PRELIMINARY已有，但R4-FINAL尚未提交**。
- 终审原则：不预设赢家，裁判可继续判定 `INSUFFICIENT_EVIDENCE`。切勿把研究质量分数当作战略胜率。

## 必须亲自阅读的7条实际评论

| 角色 | 回合 | URL |
|---|---|---|
| 正方 | R1 | [6630116711](https://github.com/fweiger/AI_book/issues/18#issuecomment-6630116711) |
| 反方 | R1 | [6630256614](https://github.com/fweiger/AI_book/issues/18#issuecomment-6630256614) |
| 正方 | R2 | [6630510638](https://github.com/fweiger/AI_book/issues/18#issuecomment-6630510638) |
| 反方 | R2 | [6630573900](https://github.com/fweiger/AI_book/issues/18#issuecomment-6630573900) |
| 中立 | R4-PRELIMINARY | [6630744078](https://github.com/fweiger/AI_book/issues/18#issuecomment-6630744078) |
| 正方 | R3 | [6631241606](https://github.com/fweiger/AI_book/issues/18#issuecomment-6631241606) |
| 反方 | R3 | [6631326724](https://github.com/fweiger/AI_book/issues/18#issuecomment-6631326724) |

此前主持人[R3统一任务](https://github.com/fweiger/AI_book/issues/18#issuecomment-6631035771)，[REFEREE.md](REFEREE.md)与 [TOPIC-004 claims.md](../claims.md)适用。上面7条**均为实际已有评论**；R3反方是一条标注“合订修订”的评论，不能虚数为多条独立R3。GitHub实际发布账号都是fweiger，模型声明不能单独证明R1盲态和独立作者身份。

## 需要交付的6个部分

1. **流程与阅读审计**：真实的各方最终论点、更新前后版本和所有文献的查阅范围；明确“官方影印原页已看／仅英文转录／仅目录／未读原稿”，特别检查正反R3在这方面是否矛盾。
2. **最终证据—主张矩阵**：为正反三项最强主张各列一手来源/学术转述、精确页码、支持范围、最强反证、来源依赖关系；同时列C001—C019是否变化。不要把转引同一文件的多篇研究视为多次独立验证。
3. **新增史料增益审查**：审查①美国国会 Pearl Harbor Exhibits **Exhibit16 pp.1061—1062**（1941-11-05 Marshall–Stark建议），②**Exhibit17 p.1083**（1941-11-27联合备忘录），③日本 **KC000234/Kishi B1-202 1941-10-07** 两张手稿图（反方称部分释读）；分别判断是否真正解决“建议→审批→交战命令”“日方是否提出并批准B”问题。原图读不全不得假装审完。
4. **三个方案、三个期限、两个美方条件分支**：B只攻英荷且不主动打美；A1攻菲律宾不袭夏威夷（仅分析假说，非已证正式日方提案）；A2同时攻菲律宾与珍珠港。按6/24/36个月以上分别讨论美国暂不直接参战与快速参战，资源、商船、实际净抵日油量、强制议和路径。**UNKNOWN保持UNKNOWN**；没有数据不要赋概率。
5. **终审裁定**：区分历史史实／可解释的1941主观担忧／有条件的局部军事价值／长期结果无法识别。公布是否维持或修订之前双方83/100的“研究质量评分”，以及评分依据；不把评分转为胜率、置信度或政治正当性。
6. **后续治理任务**：明确是否需要**一次有限R5**勘误（仅重要源文误读、单位或因果错误且有可复核证据）以及是否具备**R6候选入库**条件；为R6研究主编提供表格`CLAIM_ID / PROPOSED_STATUS / SOURCE_URL / PAGE / READ_STATUS / CAVEAT / NEXT`，但**不能由裁判未经PR直接改仓库main或宣称已INTEGRATED**。

## 特别要防止的错误

- “美军认为菲律宾威胁南进” ≠ “美国在日本只袭英荷时已决定主动开战”。
- “日本10月23、27日讨论只对英荷作战” ≠ “B方案有军方批准的可执行油运/护航计划”。
- “1941美参谋长的政策建议被国会1946影印转载” ≠ “1941总统实际批准开火命令已获取”。
- “日本KC000234两张原始图已打开、部分释读” ≠ “永野与杉山逐字立场已完整核实”。
- GRT注册吨、DWT载重吨、油品千升、库存、年度供给和月度净抵日油量不能相互替代。
- 美方秘密文书在1941真实存在，不代表日本决策者1941年已知；1942—45后见结果只能事后审计。

## 终审发表格式

```text
DEBATE-001 | ROUND=R4-FINAL | ROLE=INDEPENDENT_REFEREE
AS_OF=1941-11-30
EVIDENCE_STATUS=[...]
VERDICT=... | POSSIBLE: INSUFFICIENT_EVIDENCE
KNOWLEDGE_STATUS=NOT_INTEGRATED
```

请形成一份**可独立阅读的完整最终审查报告**，在有授权GitHub写入工具时作为**新的评论**发布到 [Issue #18](https://github.com/fweiger/AI_book/issues/18)；没有权限则提供完整Markdown供用户实际代贴。保留先前R4-PRELIMINARY原评论，不要覆盖历史；提交后停止新一轮无限辩论。

裁判可推荐 R6 研究沉淀，但正式资料更新仍需版本化PR审核；现有研究草稿 [PR #17](https://github.com/fweiger/AI_book/pull/17) 当前未合并。