# TOPIC-017｜从一份个人 WGS 到遗传学、医学、家族史与古 DNA
> 来源与规范研究任务：[AI_book Issue #72](https://github.com/fweiger/AI_book/issues/72)  
> 建立：2026-11-21；专题版本：`0.1.6`；状态：**OPEN_RESEARCH / CATALOG_SEEDED**，不是科研复现或临床认证。  
> **本仓库公开；严禁保存任何人的真实 FASTQ/BAM/CRAM/VCF、家谱身份、疾病信息或其他敏感数据。**

## 最初的问题
当一位普通消费者取得 30–40× 短读长人类全基因组测序（WGS）数据后，能借助哪些开源研究方法、论文及参考数据库，可靠地探索什么？哪些领域只能生成候选假设，哪些需要亲属/人群样本、独立验证或临床确认？

## 核心框架
**WGS 数据质量/可分析能力 → 原始论文与证据要求 → 全方向问题/研究深度 → 对应开源项目 → 公开数据复现。**

**[先读全方向研究主矩阵：15 个研究维度 × 47 篇文献 × 39 个 GitHub 源码候选](evidence-capability-matrix.md)**。本主题采用广度优先、证据驱动的方法；父系 Q03 只是其中一个子方向。

- **技术底座**：FASTQ（reads）→ BAM/CRAM（比对）→ VCF/gVCF（变异调用）；与 GRCh38/GRCh37/T2T 参考版本、chrY/mtDNA 区域、变异类型一起记录。
- **遗传谱系**：Y 单倍群、mtDNA、常染色体 IBD、古 DNA、群体迁徙与亲缘网络。
- **医学与表型**：遗传病与 ACMG、药物基因组学、PRS、睡眠/饮食/运动复杂性状；明确统计相关不等于因果和临床诊断。
- **基因组结构**：SV、CNV、STR 和短读长盲区；甲基化、转录、微生物组不是标准 WGS 的直接输出。
- **证据体系**：Github 项目存在 E0 → 原始论文可核 E1 → 公开样本真实复现 E2 → 跨工具/队列 E3 → 独立临床可行动 E4。

## 导航
- **[全方向主矩阵：数据门槛 × 论文 × 研究深度 × GitHub](evidence-capability-matrix.md)** · [47 篇论文 P-ID 注册表](paper-register.md)
- [研究问题 Q01–Q10](questions.md) · [研究方向与深度矩阵](research-matrix.md)
- [39 项 GitHub 源码与许可证审计目录](open-source-projects.md)
- **[G4 六类代表论文与真实软件输入/许可证审计](cross-domain-evidence-audit.md)**
- **[G5 D02/D04/D08：结构变异、母系 mtDNA、携带者及复用许可](cross-domain-evidence-audit-g5.md)**
- **[G6 D05/D11/D13：IBD、睡眠与运动遗传学论文×源码证据](cross-domain-evidence-audit-g6.md)**
- **[G7 全 15 域一致性审计：D01 测序 QC、D15 多组学边界、Gauchian 争议](cross-domain-evidence-audit-g7.md)**
- **[WGS 采购与原始文件最小交付验收清单](wgs-data-acceptance-contract.md)**
- **[G8 公开 HG002 真正下载与哈希验收、镜像阻断及终态](sessions/2026-11-21-hg002-public-data-admission-g8.md)**
- **[G9 HG002 1Mb 真正变异调用 + 独立 RTG SNP/Indel 基准、二次复现哈希](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md)**（AC-05 公开最小 E2 PASS，DeepVariant 方案仍 NOT_RUN）
- [论文、原始标准与参考数据库](sources.md) · [按问题阅读路径](reading-path.md)
- [主张与证据 C-ID](claims.md) · [知识关系图](knowledge-map.md) · [JSON 图谱](knowledge-graph.json)
- [HG002 chr20 基准与可运行脚本](benchmark-hg002.md) · [Q03 父系 Y 工具方法深度核查](y-chromosome-methods.md) · [下一步](NEXT.md) · [里程碑变更](CHANGELOG.md) · [会话日志](sessions/README.md)
- [唯一 L 级目标跟踪器](GOAL_TRACKER.md)（动态状态，不取代规范 Issue）

## 研究深度的四个层级
1. **能运行**：在公开/合成样本上得到预期格式，不得因此称有效预测；
2. **有精度**：在 GIAB/标准样本对 SNV/Indel/SV 等提供基准误差；
3. **能外推**：在不同祖源、批次、平台和独立队列评估泛化；
4. **有行动价值**：有权威临床证据及合适的确证流程，研究结果不得自行形成医疗建议。

## 关键禁止推断
- 共享 Y 单倍群 ≠ 某个历史人物必定是你的父系祖先；古 DNA 共组 ≠ 某古人墓主人为直接祖先。
- **一个人的 WGS 不足以做 GWAS、训练新 PRS、验证真实群体迁徙；IBD 寻亲必须有合法且知情的第二个及更多样本。**
- 检出变异 ≠ 发病；PRS 风险概率需祖源/校准/环境信息；睡眠和饮食的 GWAS 不能生成精确个人处方。
- 当前为研究知识库，不处理真人隐私 DNA，不进行临床诊断。

## 初步状态
本轮：39 个仓库已在 GitHub 核实存在（其中至少 3 项使用受限，非无条件可复用开源许可）；论文标题/DOI 与官方研究说明首轮核对；**尚未运行 WGS、采集实测运行指标或审计全部仓库许可证**。状态以 [Issue #72](https://github.com/fweiger/AI_book/issues/72) 与实际仓库 PR 为准。
