# TOPIC-017｜2026-11-21 G3：恢复数据—论文—方向—开源的横向研究目标

## 原始澄清
用户明确要求：从**拿到何种质量 WGS 数据**开始，搜寻**有哪些可适配的权威论文、这些论文实际能研究多深**，最后按每个分析维度整理已有 GitHub 实现，从前人成果上迭代；父系溯源只是独立例子，不能成为全项目唯一主线。

## 本轮原始证据与操作
- 恢复并 GET 已有 [Issue #72](https://github.com/fweiger/AI_book/issues/72)、唯一 [GOAL_TRACKER.md](../GOAL_TRACKER.md)、[Draft PR #73](https://github.com/fweiger/AI_book/pull/73)，对齐锁定的 AI_tasks V1.2.2 入口 commit `f0e5ccb90c54265dcd07abb9a975c903eb031ccf`；原 Issue Goal/Scope/AC 均保持。
- 查阅官方 [NHGRI-EBI GWAS Catalog](https://www.ebi.ac.uk/gwas/docs/about/)、[PGS Catalog](https://www.pgscatalog.org/about/)、[NIST GIAB](https://www.nist.gov/programs-projects/genome-bottle)、[PharmCAT](https://pharmcat.clinpgx.org/methods/)，核查相关记录结构和研究先验。
- 对照 [Sarek](https://doi.org/10.1093/nargab/lqae031)、[Yleaf](https://doi.org/10.1093/molbev/msy080)、[Haplogrep 3](https://doi.org/10.1093/nar/gkad284)、[hap-IBD](https://doi.org/10.1016/j.ajhg.2020.02.010)、[PharmCAT](https://doi.org/10.1002/cpt.1568)、[VEP](https://doi.org/10.1186/s13059-016-0974-4)、[PRS-CSx](https://doi.org/10.1038/s41588-022-01054-7)、[慢病 PRS eMERGE](https://doi.org/10.1038/s41591-024-02796-z)、[chronotype GWAS](https://doi.org/10.1038/s41467-018-08259-7) 与 [DIETFITS RCT 阴性研究](https://doi.org/10.1001/jama.2018.0245) 等直接论文入口；**并未逐篇阅读全文或完成定量 meta-analysis**。
- 新增 [22 篇去重论文/指南注册表](../paper-register.md)、[15 方向研究交叉矩阵](../evidence-capability-matrix.md)，关联现有已核实存在的 32 个 GitHub 项目。每个研究域标记可用 WGS 数据前提、实际论文数、候选工具数、专项工具数、个人推断上限及缺少的外部样本/表型。
- 例如睡眠/营养依赖 GWAS/RCT 证据；复杂疾病模型需要外部队列和祖源校准；标准短读长 WGS 不直接测甲基化与转录组。

## 已验证及边界
- **PASS**：Markdown 研究数据/论文/项目映射文件创建成功，GitHub 逐文件回读与结构 CI 待本轮最终检查。
- **PARTIAL**：20+ 论文 DOI / 原文入口得到首轮核对，但尚未逐篇系统性评估全文；各域论文/项目数为**已策展的去重记录**而非全球项目总数。
- **NOT_RUN**：真实 WGS 分析、22 篇全文人工审读、全部软件实际运行、跨祖源统计验证。
- **BLOCKED（局部）**：此前 HG002 Docker/DNS 环境限制不影响横向文献、方向研究。
- **目标偏差**：上轮“聚焦父系 Y”不足以推进其他研究域，属于局部优先级偏离（D1 风险）；本轮依据用户明确澄清调整为横向 D0，不修改 Goal/Scope/AC。
- **隐私**：仅公共论文、开源源代码和公开基准；没有上传个人或亲属的 DNA/医疗信息。

## 后续方法
以 [主矩阵](../evidence-capability-matrix.md) 为索引，下一步是审计**不同领域各一个代表案例**的原始论文数据条件、参考数据获取、代码输入与证据级别，再扩充被确认有价值而当前缺失的专项工具；不创建 15 个独立业务 Issue，也不追求覆盖工具组合的笛卡尔积。
