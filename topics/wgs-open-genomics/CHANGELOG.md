# TOPIC-017｜变更记录
- **2026-11-21，v0.1.0（Draft）**：创建问题驱动框架；32 个 GitHub 仓库存在性核验；权威原文/指南初步来源清单；标记 E2/真实运行 NOT_RUN。规范业务入口：[Issue #72](https://github.com/fweiger/AI_book/issues/72)。

- **2026-11-21，v0.1.1（Draft）**：AC-05 新增由 Google DeepVariant/NIST GIAB 官方样本支撑的 chr20 35× 基准数据契约、preflight/fetch/run 脚本及方法学边界；本地脚本语法/预检 PASS，因无 Docker/DNS、正式下载与 DeepVariant/hap.py 实验 NOT_RUN；详见 [benchmark-hg002.md](benchmark-hg002.md) 和 [当日证据日志](sessions/2026-11-21-giab-benchmark-spec.md)。

- **2026-11-21，v0.1.1（Draft、同轮补充）**：Q03 一手 README 与方法论文核验后，增加 [Y 染色体研究方法对照](y-chromosome-methods.md)，明确 yhaplo GRCh37 坐标要求、Yleaf variants-only VCF 风险、Y-LineageTracker 的 SNP divergence time 和 Y-STR TMRCA 区别。无真实 chrY 计算，不提升到 E2。

- **2026-11-21，v0.1.2（Draft）**：根据用户澄清，确立**数据质量→论文→研究维度/深度→开源项目**为全专题主线；新增 [15 方向主矩阵](evidence-capability-matrix.md) 与 [22 篇论文 P-ID 注册表](paper-register.md)，明确跨域去重、零证据缺口及营养随机试验阴性证据。父系/chr20 改作独立子案例，不改变原 Goal/Scope/AC；仍未跑真实个人/公开 WGS。
