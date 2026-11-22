# 2026-11-22｜首批 10 个项目版本、许可证与构建入口审查

## 固定快照

审查对象为 10 个公开仓库默认分支的具体 commit；每个 commit SHA 已写入 case-studies.md。读取内容包括仓库元数据、README、可找到的 LICENSE、lean-toolchain、lakefile.lean 或 lakefile.toml。

## 关键发现

1. **Lean 版本分散**：Mathlib4 当前快照为 4.37.0-rc1；Formal Conjectures 为 4.33.1；ArkLib/Aeneas Lean backend 为 4.36.0；MathEconLib、MathFin、physicslib4 为 4.35.0；EconCSLib 为 4.30.0。
2. **Lean 3 与 Lean 4 必须区分**：Liquid Tensor Experiment 的 README 明确写明使用 Lean 3；不能将它当作 Lean 4 项目。
3. **仓库根目录不是唯一构建边界**：Aeneas 的 Lean backend 在 backends/lean，rust-lean 是多个独立子项目的集合。
4. **猜想声明不等于证明**：Formal Conjectures 的目标是形式化猜想陈述；项目 commit 说明 solved statements 不在目标范围。
5. **项目成熟度需要细分**：EconCSLib 的稳定导入接口与 OpenProblem 分离；Blueprint 中存在尚待 Lean 实现的目标。
6. **版本锁定是跨项目复现前置条件**：不同项目固定不同 Lean/Mathlib 版本，不能以全局最新版替换项目 toolchain。

## 元数据审查结果

- 10 个仓库均读取了默认分支和固定 commit SHA。
- 10 个 README 已读取。
- 7 个仓库在根目录找到 Apache-2.0 LICENSE；Liquid Tensor、Aeneas、rust-lean 的根 LICENSE 路径未找到，记录为许可待核，不推断无许可。
- 7 个仓库在根目录找到 Lean 4 toolchain；Aeneas 在 backends/lean 子目录找到 v4.36.0；Liquid Tensor 是 Lean 3 legacy；rust-lean 是多子项目集合，根 toolchain 不适用/未找到。
- 7 个仓库找到根 Lake 配置；Aeneas 找到嵌套 Lean backend Lake 配置；Liquid Tensor 和 rust-lean 根 Lake 配置未找到。
- Mathlib 的固定 commit 返回 bors success。其他项目的当前状态查询未返回 status contexts；这不等于其 CI 不存在。
- 本轮没有在本地运行任何项目构建，所有项目 build status 均 NOT_RUN。

## 新增/更新主张

新增 C018-010 至 C018-014；图谱版本升级至 0.2.0，增加跨项目版本准入和 Lean 3/Lean 4 边界节点。

## 未完成事项

- 未逐一检查 lake-manifest.json、完整传递依赖和第三方许可证。
- 未检查所有项目的 sorry/admit、axiom audit 和 theorem statement fidelity。
- 未完成 Aeneas/Rust-lean 子项目的实际 Rust→Lean 验证复现。
- 未本地构建 Mathlib、ArkLib、MathEconLib、EconCSLib、MathFin 或 physicslib4。
- 未完成独立 QA。

## 当前结论

M0 的首批来源准入从“只有项目名称”推进到“10 个固定 commit + README + 部分 toolchain/license/Lake 配置”。仍为 E1 级源码元数据审查，不是 E2 构建通过。下一步应补齐特殊仓库的子项目/许可证路径，并对至少一个 Lean 4 项目做可复现构建。
