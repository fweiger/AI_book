# TOPIC-017｜变更记录
- **2026-11-21，v0.1.0（Draft）**：创建问题驱动框架；32 个 GitHub 仓库存在性核验；权威原文/指南初步来源清单；标记 E2/真实运行 NOT_RUN。规范业务入口：[Issue #72](https://github.com/fweiger/AI_book/issues/72)。

- **2026-11-21，v0.1.1（Draft）**：AC-05 新增由 Google DeepVariant/NIST GIAB 官方样本支撑的 chr20 35× 基准数据契约、preflight/fetch/run 脚本及方法学边界；本地脚本语法/预检 PASS，因无 Docker/DNS、正式下载与 DeepVariant/hap.py 实验 NOT_RUN；详见 [benchmark-hg002.md](benchmark-hg002.md) 和 [当日证据日志](sessions/2026-11-21-giab-benchmark-spec.md)。

- **2026-11-21，v0.1.1（Draft、同轮补充）**：Q03 一手 README 与方法论文核验后，增加 [Y 染色体研究方法对照](y-chromosome-methods.md)，明确 yhaplo GRCh37 坐标要求、Yleaf variants-only VCF 风险、Y-LineageTracker 的 SNP divergence time 和 Y-STR TMRCA 区别。无真实 chrY 计算，不提升到 E2。

- **2026-11-21，v0.1.2（Draft）**：根据用户澄清，确立**数据质量→论文→研究维度/深度→开源项目**为全专题主线；新增 [15 方向主矩阵](evidence-capability-matrix.md) 与 [22 篇论文 P-ID 注册表](paper-register.md)，明确跨域去重、零证据缺口及营养随机试验阴性证据。父系/chr20 改作独立子案例，不改变原 Goal/Scope/AC；仍未跑真实个人/公开 WGS。

- **2026-11-21，v0.1.3（Draft）**：完成 [跨领域六案例原始论文×源码输入审计](cross-domain-evidence-audit.md)：Exomiser、PharmCAT/StellarPGx、pgsc_calc、DIETFITS、ancIBD、OptiType；识别 pgsc_calc 不是直接 WGS variants-only VCF 计算器、PharmCAT CYP2D6 VCF-only 研究模式不适于临床，新增 [StellarPGx](https://github.com/SBIMB/StellarPGx) 与 [OptiType](https://github.com/FRED-2/OptiType) 两个专项项目及 3 篇对应论文。首轮登记 **15 域 / 25 篇论文 / 34 个 GitHub 项目**；仍未进行实际 WGS 运行，原 Goal/Scope/AC 保持。

- **2026-11-21，v0.1.4（Draft）**：完成 [G5 D02/D04/D08 原始论文×源码×许可证审计](cross-domain-evidence-audit-g5.md)；新增 11 篇题录/标准 P026–P036 和五个源码项目 T35–T39，现有 **15 域 / 36 篇论文 / 39 个源码仓库候选**。修正 ExpansionHunter/Gauchian PolyForm Strict 与 InterVar 非商用免费限制；Truvari 为 SV VCF benchmark 非 caller，Mutserve VCF 不包含 indel；均未实际运行 WGS。

- **2026-11-21，v0.1.5（Draft）**：完成 [G6 D05/D11/D13 文献×源码输入审计](cross-domain-evidence-audit-g6.md)；新增 P037–P041 5 篇论文，当前 **15 域 / 41 篇去重论文 / 39 个 GitHub 源码候选**。本轮重点确认 hap-IBD 必须使用完整 phased 多人 GT + genetic map 才能做人与人 IBD，单人仅可研究 HBD/ROH；睡眠 GWAS 和运动活动 GWAS 均不能直接转化成个体时间表或训练处方；HERITAGE 21-SNP 样本内方差解释率不能当样本外预测准确率。开源仓库无虚假新增，E2 WGS 实际运行仍 NOT_RUN。
