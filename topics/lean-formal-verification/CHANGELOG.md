# TOPIC-018｜变更记录

- **2026-11-22，v0.1.0（Draft）**：建立 Lean 形式化证明与跨学科应用专题框架；创建规范研究 Issue #74；初步读取 Lean 官方语言参考、Elan 安装手册、Mathlib、Lean 项目目录、Aeneas、Rust-to-Lean 经验报告、经济学/金融数学、TorchLean 和 physicslib4 等来源。当前仅为来源级初筛；未完成逐项目构建、许可证审计、独立复现或独立 QA。


- **2026-11-22，v0.2.0（Draft）**：完成首批 10 个代表仓库的默认分支 commit、README、toolchain、LICENSE 和 Lake 配置入口级审查；发现 Lean 3/Lean 4 混用、项目版本分散在 4.30.0—4.37.0-rc1、Aeneas 使用嵌套 Lean backend、rust-lean 为多子项目集合；新增 C018-010 至 C018-014 和版本化准入表。除 Mathlib bors status success 外，其他项目未获得可用 status context；所有本地构建 NOT_RUN，许可/依赖/证明状态审计未全部完成。


- **2026-11-22，v0.2.1（Draft）**：补充 8 个 Lean 4 项目的 Lake manifest 解析结果，记录 Mathlib 与关键传递依赖的精确 commit revision；新增 C018-015。进一步确认可复现性至少需要项目 commit + lean-toolchain + lake-manifest 三者，单独记录 Lean 版本不足。所有项目实际构建仍 NOT_RUN。
