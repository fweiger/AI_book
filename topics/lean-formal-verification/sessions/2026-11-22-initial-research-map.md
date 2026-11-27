# 2026-11-22｜专题立项与首轮来源地图

## 起始问题

Lean 如何在数学领域帮助形式化猜想与证明？除数学以外，哪些学科和工程领域实际使用 Lean？不同领域的研究者如何使用 Mathlib、tactics、Blueprint、程序精化、自动化和 AI Agent？

## 实际读取来源

- Lean 官方 Language Reference：确认 Lean 基于依赖类型理论、最小 Kernel 检查 proof term、tactic 输出仍由 Kernel 检查；页面当前显示 4.37.0-rc1。
- Lean 官方安装手册：确认 Elan 是 Lean version manager。
- Mathlib 官网与 Mathlib 论文入口：确认社区数学库定位。
- Lean Community Projects：确认目录列有数学形式化项目，也明确其代表性/非穷尽性质。
- Aeneas 官方项目页：确认 Charon/Aeneas 与 Lean backend 及当前 safe sequential Rust 边界。
- Rust-to-Lean Pipeline 2026 经验报告：确认生产 Rust 密码学代码抽取、形式化规格库和 AI prover 的组合流程。
- MathEconLib 官网、EconCSLib 项目页/论文入口、Econlib 项目页：确认经济学与计算经济学形式化方向。
- MathFin 官网与论文入口：确认数学金融库的覆盖范围及其证明/陈述分类设计。
- TorchLean 预印本：确认神经网络语义、Float32 和认证界限的研究方法。
- physicslib4 教程：确认 AQFT 的 Lean 定义、定理、例子及从 Blueprint 到检查定理的教学路线。
- Veil/IFP、EconLib4：仅登记候选线索，证明内容和构建尚未核实。

## 初步发现

1. Lean 不只是数学证明工具：官方参考明确将其定位同时用于研究级数学和软件验证。
2. 跨学科应用不是“把专业名词翻译成 Lean”这么简单。各领域的关键差异在于：形式化对象是什么、需要哪些假设、证明目标是什么，以及形式化模型如何连接现实程序或经验数据。
3. 可迁移的方法比单个项目更重要：类型/状态建模、规格定义、定理分解、库复用、Blueprint、实现精化、Kernel 检查、AI 候选证明与独立审查。
4. 经济学和金融数学已出现多个专门 Lean 库；MathFin 是 AI_Trader #488 可关联的金融数学资产，但其项目声明不能替代 A 股 PIT 实验。
5. 软件验证案例显示，Rust→Lean 抽取和 AI prover 可以组合，但工具链版本漂移和抽取支持范围本身也是工程风险。

## 证据等级与限制

- 本轮主要为 E1（官方文档/论文/项目说明初读）和 E0（项目线索）。
- 未对候选仓库逐一克隆、构建或运行；未完成所有许可证、commit、sorry/admit 和公理依赖审计。
- 未完成 Mathlib/MathFin 的逐定理覆盖分析；未对数学猜想项目逐条判断已证明状态。
- 没有完成独立审查；AI 自身检索和总结不等于独立 QA。

## 更新的 C-ID

新增 C018-001 至 C018-009，均保留各自来源范围与限制，详见 claims.md。

## 下一步

按唯一 GOAL_TRACKER §7：完成 M0 的版本化项目准入表，优先对 Lean/Mathlib/Elan/Lake/Blueprint 官方资料及数学、软件验证、密码学、经济金融、AI/物理代表项目锁定源码 commit、许可证、toolchain 和构建状态。不要扩大到无关领域或先做策略实验。
