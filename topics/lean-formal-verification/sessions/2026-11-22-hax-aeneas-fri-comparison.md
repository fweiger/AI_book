# 2026-11-22｜Hax / Aeneas 同源 FRI 对照与 Hax ADC 上游修复审计

## 研究目标与范围

在 TOPIC-018 #74 的 M0/M2/M3 范围内，核验 Hax ADC 历史 PoC 的问题是否已被上游修复，并对同一段 Plonky3 FRI arity 选择 Rust 源码进行 Hax 与 Aeneas 的受控对照。固定主仓库 commit：`Verified-zkEVM/rust-lean@49a83d2a231c24f8a26a694ca2badaa36fb3914d`。

## 关键证据

### Hax ADC

- 历史 PoC README commit `79b95fe8ad1d31f483281863546d3f03f8136224`，日期 2026-02-03；Cargo.toml 引用 hax-lib Git version 0.3.6；本轮未找到 Cargo.lock。
- Hax #1925 merged 2026-02-09，修复 cast_op 类型标注与 shift/add 实例问题。
- Hax #1927 merged 2026-02-11，保留 Rust crate/module 小写命名。
- Hax #1933 merged 2026-02-11，增加 specset int/bv 与 hax_mvcgen。
- Hax #1938 merged 2026-02-12，增加默认 Lean proof 和 proof_method 属性。
- Hax #1959 merged 2026-02-19，将 ADC 示例加入 Hax 官方 examples。其源码采用纯 Lean Hoare triple、`hax_mvcgen.specset "bv"`、`hax_mvcgen` 和 `bv_decide`；toolchain 为 Lean 4.28.0-rc1，包含 Lake manifest 和 Makefile。
- #1913 维护者建议 tuple positional projections `.1/.2`；PR #1917 关闭未合并。#1916 由维护者解释为预期 RustM 表示，建议 mvcgen + @[spec] 归一化。

### 同源 FRI 对照

- Hax/Aeneas 的 Rust `compute_log_arity_for_round` 源文件 blob SHA 相同：`80cb7baefc6bfc7d41a507fc6dc10d4d4181f468`。
- Hax：Lean 4.26.0；Hax commit `1332b8fa19967234232473d0d3ec88e4d8ce8424`（2026-01-20）；manifest 固定 ArkLib/Mathlib 等 revision。该 Hax pin 在 commit graph 上不包含后续 #1925/#1933 merge commits。
- Hax extracted function 无显式 sorry/axiom；BasicProofs 有 9 个 sorry；ArkLib FoldingCorrectness 有两个实质性证明（target distance、max bound）和 4 个 sorry。
- Aeneas：Lean 4.28.0；manifest 版本 1.1.0，锁定 19 个依赖，包含 Aeneas `c23de9324fbe4d3630fc532e5216a0568b9beb5c`、ArkLib `27ff62470e9947f72ddd978db458ee622f8bdcd1`、Mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`。
- Aeneas FoldArity generated source 无显式 sorry/axiom；BasicProofs 六个 theorem + 三个 examples，静态扫描无 sorry/admit/axiom/opaque。证明主要用 generalize/cases/bind_tc_ok/Std.Usize.sub_spec/simp/omega。
- Aeneas ArkLib FoldingCorrectness 因 Aeneas 与 Batteries/Mathlib 的 `BitVec.toNat_pow` 冲突而分开 target；包含 3 个 axioms、1 个 opaque、4 个 sorry。它不是完整的同一 Lean 环境端到端桥接证明。
- 两条 pipeline 的核心定理均以输入高度不等式和函数成功返回作为前提；不等于对任意输入的 panic-freedom 或完整 FRI 协议安全性证明。

## CI / Build 状态

- rust-lean 固定 commit 的 workflow runs 查询返回空列表，combined status 查询也未返回状态上下文；不能推断 CI 不存在。
- 本轮执行环境没有 Lean/Lake/Elan/Rust/Cargo 可执行文件，未能在当前环境构建。
- Hax/Aeneas build 均为 NOT_RUN；源码 proof term、上游报告与实际 Kernel build 必须分开记录。

## 结论

1. Hax ADC 的历史 issue 清单已过时；当前可复用方法应以 Hax 官方 lean_adc example 为准。
2. 对这一同源控制流函数，Aeneas 的局部 BasicProofs 源码完成度明显更高；但这只是一个函数的受控样本，不能泛化为工具整体优劣。
3. 两条 FRI pipeline 都未完成完整多轮协议、实际多项式折叠与 prover/verifier 的形式化证明。
4. Aeneas 的 ArkLib bridge 通过 axioms/opaque 分离目标，需优先消除桥接公理或给出 refinement proof。
5. Hax-FRI 固定 Hax 版本早于后续关键修复；若要升级，必须同时迁移 Lean/Mathlib/ArkLib/CompPoly 依赖，不能只替换 Hax commit。

## 新增资产

- 更新 case-studies / field-map / methods / claims / bibliography / README / knowledge graph。
- 新增方法卡 M-04 至 M-07。
- 更新 C018-016/017 并新增 C018-018 至 C018-025。
- 图谱升级至 0.4.0，增加 Hax/Aeneas 对照与 ADC 证明路径。

## 未完成

- 未执行 Hax/Aeneas 的 Lake build。
- 未运行 `#print axioms`，静态计数不等同于 Lean 的传递公理审计。
- 未独立复现 Hax 官方 lean_adc Makefile。
- 未证明 FRI polynomial foldNth、domain step、multi-round consistency 和完整 prover/verifier correctness。
- 未完成非主要研究者独立 QA。

## 当前唯一下一步候选

在有 Lean 4.28.0、Elan、Lake 和 Rust/Cargo 的隔离 Runner 环境中，先构建 Aeneas `fold_arity_lean` 的 BasicProofs target；保存工具链、manifest、完整 build log，并对六个 theorem 执行 `#print axioms`。若该 target 通过，再单独构建 ArkLib target，明确记录 axiomatized bridge，不将其算作端到端 PASS。
