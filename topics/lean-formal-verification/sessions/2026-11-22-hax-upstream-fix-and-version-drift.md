# 2026-11-22｜Hax ADC 历史问题上游修复与版本漂移审查

## 本轮实际读取

- Hax Issue #1911、#1912、#1914、#1915、#1916。
- Hax PR #1925、#1927、#1933、#2142，读取状态、合并时间、描述和 commit diff。
- Hax 固定 commit 1332b8fa 的 changelog 与 commit 元数据。
- Hax main CHANGELOG，读取 0.5.0（2026-11-09）版本说明。
- rust-lean 固定 commit 的 Hax-FRI 与 ADC README、Lean toolchain 和 Lake manifest。

## 可核实事实

1. PR #1925 merged 2026-02-09：给 cast_op 增加显式类型标注，并在测试中覆盖 cast 后加法和 shift。
2. PR #1933 merged 2026-02-11：引入 specset int / specset bv、hax_mvcgen 与可切换规格集合，更新 Lean-ChaCha20 示例。
3. PR #1927 merged 2026-02-11：修复 Lean backend 模块/文件名首字母大写问题。
4. PR #2142 merged 2026-08-26：cargo hax into lean 默认 scaffold 完整 Lean package，包括 lean-toolchain、lakefile、root module、Verification/ 和 Assumptions/。
5. Hax-FRI 固定 Hax commit 1332b8fa，标题为升级 Lean 4.26.0，创建时间 2026-01-20；早于 #1925 和 #1933。因此该快照不能假定已含后续修复。
6. Hax main CHANGELOG 的 0.5.0（2026-11-09）要求 Lean 4.35.0，并列出 Lean backend breaking changes；Hax-FRI 的 Lean 4.26.0 不能直接无迁移替换。
7. ADC README 仍保留早期失败列表，现需按版本历史解释，不应当成 Hax 当前功能缺陷。

## 研究路径调整

从继续收集早期 Hax 编译失败，调整为先在旧锁定版本建立可复现基线，再创建独立升级分支，迁移到 Hax 0.5.0 / Lean 4.35.0，比较抽取、构建、specset、局部 theorem 和协议 correctness theorem。原始锁定快照不覆盖。

## 新增成果

C018-018 至 C018-022；M-04 双规格集方法卡；M-05 Hax 项目版本升级与生成结构迁移方法卡；相关 case study、field map、methods、claims 和 changelog 已更新。

## 尚未完成

- 没有运行 Hax-FRI 的旧版本构建。
- 没有在 ADC 项目验证 PR #1933 的 specset 实际使用。
- 没有升级到 Hax 0.5.0 / Lean 4.35.0。
- 没有完成 Hax-FRI FoldingCorrectness。
- 没有检查 Hax 0.5.0 与该项目 Rust/Plonky3 版本的兼容性。
- 独立 QA NOT_RUN。

## 当前结论

早期 Hax 失败记录中至少四项已有上游修复或明确工作流方案。真正尚未解决的是项目是否采用修复、版本迁移是否兼容、局部证明与协议级正确性是否闭合。下一步做旧版复现与新版迁移对照，而不是继续把已修复的 issue 当作开放障碍。
