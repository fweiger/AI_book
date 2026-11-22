# 2026-11-22｜Rust→Lean 的 Hax-FRI 与 ADC 子项目方法审查

## 实际读取的文件

- rust-lean 仓库 README：确认它是多个独立项目的集合，各子项目分别用 Hax 或 Aeneas 抽取 Rust 到 Lean。
- hax-FRI/README.md：读取 Plonky3 FRI folding 的抽取和 ArkLib 集成说明。
- hax-FRI/lean/P3FriProofs/lean-toolchain：Lean 4.26.0。
- hax-FRI/lean/P3FriProofs/lakefile.toml 与 lake-manifest.json：锁定 Hax、ArkLib、Mathlib 等依赖 revision。
- hax-annotations-adc/README.md 与 src/lib.rs：读取 u32 adc 函数、pre/post 条件、Hax theorem annotation 和 hax_bv_decide 使用方法。

## 新发现

1. Hax-FRI 将 Plonky3 的 Rust FRI folding 代码抽取为 Lean，并连接 ArkLib 的 FRI 规格；README 报告 BasicProofs.lean 有 6 个 theorem、3 个 examples 且构建成功，但最终 FoldingCorrectness theorem 仍 TODO。
2. Hax ADC 示例将 32-bit carry arithmetic 的规格写在 Rust 中：carry ∈ {0,1}，并验证 a+b+carry = sum+2^32×carry_out。
3. Hax ADC 使用 hax_lib::lean::after 将 theorem 注入抽取后的 Lean 文件，并尝试 hax_bv_decide bit-blasting；拆分 adc_pre/adc_post 有利于 Lean 展开和证明。
4. README 记录了真实失败模式：u32/u64 cast、shift、tuple projection、monadic binds、identifier 命名以及 tactic 对 BitVec fragment 的支持。
5. 这两例说明“Rust 抽取”“Lean 文件编译”“局部算术证明”“协议级正确性证明”必须分别验收。

## 新增方法卡与主张

- M-01：Hax annotations + bit-blasting 验证定宽算术。
- M-02：Rust extraction → Lean model → protocol specification。
- M-03：项目版本 + manifest 双锁定。
- 新增 C018-016、C018-017；图谱升级到 0.3.0，增加 Rust→Lean 和 BitVec bit-blasting 方法节点。

## 限制

- 本轮仅读取固定 commit 的 README、源码与配置；未运行 Hax、Lean 或 lake build。
- Hax-FRI 的“BasicProofs builds”来自上游 README，未独立复现。
- FoldingCorrectness 仍是上游 README 标记的 TODO，不能报告为完整验证。
- Hax ADC README 列出的 issue 状态需要另行核对最新上游状态。

## 下一步

在隔离的 Lean 4.26.0 环境中复现 hax-FRI/P3FriProofs 的依赖获取与构建；先区分基础证明文件是否可构建，再确认 FoldingCorrectness 是否仍未完成。若环境不可用，明确标记 NOT_RUN，不把上游 README 代替独立测试。
