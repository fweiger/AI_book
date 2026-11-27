# 2026-11-22｜8 个 Lean 4 项目 Lake manifest 与依赖 revision 审查

## 范围

在 M0 已固定的 10 个仓库快照中，继续检查 8 个 Lean 4 项目的 Lake manifest：Mathlib4、Formal Conjectures、Aeneas Lean backend、ArkLib、MathEconLib、EconCSLib、MathFin、physicslib4。

## 实际结果

- 8 个项目的 lake-manifest.json 均可在对应固定 commit 读取并解析。
- 每个 manifest 都记录 Lake manifest schema/version、packagesDir 和包级 Git revision。
- 已抽取 Mathlib 与关键外部依赖 revision，写入 case-studies.md。
- 发现不同项目即使使用相近的 Lean 版本，仍可能固定不同 Mathlib commit 和传递依赖 commit。
- Liquid Tensor 是 Lean 3 legacy；rust-lean 是多子项目集合，本轮没有把它们的根目录 NOT_FOUND 误报为项目无锁文件。

## 方法论结论

一个 Lean 项目的最低可复现版本指纹至少应包括：

1. 项目 Git commit；
2. lean-toolchain；
3. lakefile.lean 或 lakefile.toml；
4. lake-manifest.json；
5. 构建命令、环境与实际日志。

仅有 README、Lean 版本号或 lakefile 中的依赖声明，不足以保证依赖树可复现。

## 限制

- 本轮没有运行 lake update、lake exe cache get 或 lake build。
- 没有验证 manifest 中所有依赖 commit 是否仍可访问。
- 没有检查所有第三方依赖许可证。
- 没有完成 Aeneas/Rust-lean 子项目的 end-to-end 抽取和证明。
- 本轮没有独立 QA。

## 证据与状态

- 新增 C018-015。
- 8 个 manifest 的 blob SHA 和 Mathlib revision 见 case-studies.md。
- 当前为 E1（固定源码文件读取与解析）；项目构建仍 NOT_RUN。
