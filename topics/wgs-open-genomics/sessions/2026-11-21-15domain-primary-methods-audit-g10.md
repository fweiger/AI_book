# 2026-11-21｜TOPIC-017 G10：15 域一手论文×数据条件×开源输入方法级审计

- **规范身份**：同一 [AI_book Issue #72](https://github.com/fweiger/AI_book/issues/72) · [Draft PR #73](https://github.com/fweiger/AI_book/pull/73) · 既有 `GOAL_TRACKER.md` · AI_tasks V1.2.2 锁定 `f0e5ccb90c54265dcd07abb9a975c903eb031ccf`。
- **上一轮唯一动作**：G9 HG002 D01 公开 E2 已完成，转向 D01–D15 每域 1 篇现有权威一手论文/指南，核真实 assay、样本/祖源、可迁移研究上限、Github 项目和输入契约。未创建新研究方向/软件项目/任务。
- **本轮原始入口**：先 GET 权威 Issue、G9 评论、Tracker、PR head `85dc7c4bbc9b0d650f82da9666063d612c964d39`、[主矩阵](../evidence-capability-matrix.md)、[原文 P-ID](../paper-register.md)、[39 项软件](../open-source-projects.md)。对照原始 DOI 期刊/PMC/PubMed/学会原文和可用 GitHub README，部分文章核摘要/方法，非全部全文及附录。
- **主要交付**：[G10 D01–D15 全域科学证据表](../cross-domain-method-evidence-audit-g10.md)。逐行关联 P042/P026/P005/P030/P008/P010/P012/P033/P024/P025/P019/P020/P039/P023/P046。分为 SINGLE_WGS、EXTERNAL 和 OTHER_ASSAY，并区分论文 E1 与实际 D01 G9 1Mb E2。
- **已验证纠错**：P005 Yleaf 方法论文 DOI 原为 `10.1093/molbev/msy032`（PMID 29518227），先前登记的 `msy080` 是勘误；修正注册表/sources，并在矩阵留勘误提示。另一重要输入边界：pgsc_calc 默认分支 README 明示 `Whole genome sequencing (WGS) data are not currently supported`，不能简单将普通 WGS variants-only VCF 当可评估完整 PGS 的输入。
- **候选软件真实性**：本轮实际 GET 了 bcftools、Truvari、Yleaf、Mutserve、hap-IBD、ADMIXTOOLS2、Ensembl VEP、InterVar、StellarPGx、pgsc_calc、OptiType、PRS-CSx、PLINK2 的 GitHub README/Repo metadata；没有重新执行每个或对全部 39 项 LICENSE/依赖做商用法律核查。D15 普通短读长 DNA WGS 对动态组学无直接测量来源。
- **明确科学上限**：D05 需要合法第二人且 phased GT/genetic map；D06 qpAdm 是群体模型而非个人古代身份；D08 临床 carrier screen 需伴侣/不同技术与残余风险；D10 PGS 的祖源校准与 genotype input；D11/12/13 GWAS/RCT 表型不同且不直接提供睡眠钟点、饮食或运动处方；D14 OptiType 仅 HLA-I；D15 ONT 原生修饰测量不能由普通 ACGT WGS 重建。
- **静态验证**：15 个独立 D01–D15 行、15 个现有代表 P-ID，全部回查 [47 个注册 DOI](../paper-register.md)；对应软件已核现有 README；没有新增 P-ID 或 GitHub 项目。报告中的 E1/方法并非实验复算，不能以 15/15 推论 47/47 已全文核实。
- **状态**：D0 ALIGNED；AC-02/03/04 `PARTIAL`，但本轮 15 域代表性方法证据矩阵具备，AC-05 G9 公开 1Mb E2 PASS（不支持 DeepVariant/hap.py）；AC-06 Draft PR 未合并。原 Goal/Scope/AC 不变，没有个人 DNA 写进公开仓库。
- **唯一下一步候选**：对 D03/D04/D09/D10 四个最可能利用个人 WGS 且限制不同的领域完成**基于实际交付文件契约的可操作输入和研究深度分层排序**，同时保留对剩余 32 篇论文的有界反证检查；不回到 D01 无限扩展 Docker/基准。
