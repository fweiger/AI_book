# TOPIC-017｜变更记录
- **2026-11-21，v0.1.0（Draft）**：创建问题驱动框架；32 个 GitHub 仓库存在性核验；权威原文/指南初步来源清单；标记 E2/真实运行 NOT_RUN。规范业务入口：[Issue #72](https://github.com/fweiger/AI_book/issues/72)。

- **2026-11-21，v0.1.1（Draft）**：AC-05 新增由 Google DeepVariant/NIST GIAB 官方样本支撑的 chr20 35× 基准数据契约、preflight/fetch/run 脚本及方法学边界；本地脚本语法/预检 PASS，因无 Docker/DNS、正式下载与 DeepVariant/hap.py 实验 NOT_RUN；详见 [benchmark-hg002.md](benchmark-hg002.md) 和 [当日证据日志](sessions/2026-11-21-giab-benchmark-spec.md)。

- **2026-11-21，v0.1.1（Draft、同轮补充）**：Q03 一手 README 与方法论文核验后，增加 [Y 染色体研究方法对照](y-chromosome-methods.md)，明确 yhaplo GRCh37 坐标要求、Yleaf variants-only VCF 风险、Y-LineageTracker 的 SNP divergence time 和 Y-STR TMRCA 区别。无真实 chrY 计算，不提升到 E2。

- **2026-11-21，v0.1.2（Draft）**：根据用户澄清，确立**数据质量→论文→研究维度/深度→开源项目**为全专题主线；新增 [15 方向主矩阵](evidence-capability-matrix.md) 与 [22 篇论文 P-ID 注册表](paper-register.md)，明确跨域去重、零证据缺口及营养随机试验阴性证据。父系/chr20 改作独立子案例，不改变原 Goal/Scope/AC；仍未跑真实个人/公开 WGS。

- **2026-11-21，v0.1.3（Draft）**：完成 [跨领域六案例原始论文×源码输入审计](cross-domain-evidence-audit.md)：Exomiser、PharmCAT/StellarPGx、pgsc_calc、DIETFITS、ancIBD、OptiType；识别 pgsc_calc 不是直接 WGS variants-only VCF 计算器、PharmCAT CYP2D6 VCF-only 研究模式不适于临床，新增 [StellarPGx](https://github.com/SBIMB/StellarPGx) 与 [OptiType](https://github.com/FRED-2/OptiType) 两个专项项目及 3 篇对应论文。首轮登记 **15 域 / 25 篇论文 / 34 个 GitHub 项目**；仍未进行实际 WGS 运行，原 Goal/Scope/AC 保持。

- **2026-11-21，v0.1.4（Draft）**：完成 [G5 D02/D04/D08 原始论文×源码×许可证审计](cross-domain-evidence-audit-g5.md)；新增 11 篇题录/标准 P026–P036 和五个源码项目 T35–T39，现有 **15 域 / 36 篇论文 / 39 个源码仓库候选**。修正 ExpansionHunter/Gauchian PolyForm Strict 与 InterVar 非商用免费限制；Truvari 为 SV VCF benchmark 非 caller，Mutserve VCF 不包含 indel；均未实际运行 WGS。

- **2026-11-21，v0.1.5（Draft）**：完成 [G6 D05/D11/D13 文献×源码输入审计](cross-domain-evidence-audit-g6.md)；新增 P037–P041 5 篇论文，当前 **15 域 / 41 篇去重论文 / 39 个 GitHub 源码候选**。本轮重点确认 hap-IBD 必须使用完整 phased 多人 GT + genetic map 才能做人与人 IBD，单人仅可研究 HBD/ROH；睡眠 GWAS 和运动活动 GWAS 均不能直接转化成个体时间表或训练处方；HERITAGE 21-SNP 样本内方差解释率不能当样本外预测准确率。开源仓库无虚假新增，E2 WGS 实际运行仍 NOT_RUN。

- **2026-11-21，v0.1.6（Draft）**：按 G6 唯一下一步完成 [G7 D01/D15 15 域一致性审计](cross-domain-evidence-audit-g7.md)，新增 [WGS 最小交付/采购数据质量合同](wgs-data-acceptance-contract.md)，核对 GIAB CMRG、ACMG 临床测序标准、PCR-free 库构建和跨模态 assay；补齐 Gauchian 2025 质疑与正式回应两方证据。新增 6 个确有用途的 DOI/标准 P042–P047；当前 **15 域 / 47 篇已登记论文 / 39 个 GitHub 源码候选**，未因统计而新增软件。结构检查与引用核对不能代表真实个人/公开 WGS E2，后者仍 NOT_RUN。

- **2026-11-21，G8 / Draft**：31.5 有真实 Docker 与 GCS/NCBI 访问，原 HG002 chr20 8 项公开数据全部下载完成，本地 SHA-256 `-c` 全通过且 BAM GCS 官方 MD5 一致。基于真实失败改进脚本 `curl --continue-at -`。DeepVariant/hap.py 容器拉取两次有限尝试未最终完成，相关 Jobs 均已终止；`DATA_ADMISSION_PASS`，**实际算法基准 `NOT_RUN`**。依据 [G8 运行证据](sessions/2026-11-21-hg002-public-data-admission-g8.md) 而不是复述早期环境阻断。

- **2026-11-21，G9 / Draft**：G8 公开 HG002 8 文件及 MD5/SHA 数据不重复下载；31.5 在系统外临时目录使用 bcftools 1.19/htslib 1.19，下载 RTG 官方轻量版 3.13，真实执行 chr20 2–3 Mb `mpileup | call` 和 GIAB v4.2.1 confident BED 内 `vcfeval`：SNP F1 **0.9962**、Indel F1 **0.9367**、总 F1 **0.9880**（无额外后验 QUAL cutoff，非全 WGS）。原始真实调用 1,899 变异，二次通过新 PR 版本脚本生成相同变异记录正文 SHA/评分摘要 SHA，AC-05 最小公开 E2 **PASS**；DeepVariant/hap.py 仍 NOT_RUN，不以此替代或转化成临床结论。详见 [G9 真正实验与源码复现证据](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md)。
