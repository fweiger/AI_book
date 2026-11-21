# TOPIC-017 / AC-05｜GIAB HG002 chr20 最小变异检测基准（技术规范 v0.1）

> **2026-11-21，状态：SPEC_READY / TRUE_BENCHMARK_NOT_RUN。** 规范任务 [Issue #72](https://github.com/fweiger/AI_book/issues/72)；[研究草稿 PR #73](https://github.com/fweiger/AI_book/pull/73)。此文是复现规范，不是已完成实验报告。严禁加入个人真实 DNA。
>
> **本实验只测单样本 chr20 小变异 SNP/Indel 的 calling 与 benchmark。它不验证全 WGS、chrY 分支、宗亲匹配、SV、PRS 或疾病解释。**

## 为什么这组实验
Google DeepVariant 官方 [DeepTrio WGS case study (r1.10)](https://github.com/google/deepvariant/blob/r1.10/docs/deeptrio-wgs-case-study.md) 已给出公开 HG002 NovaSeq PCR-free **35× GRCh38 no-alt chr20 BAM/BAI**，配套 NIST GIAB **v4.2.1** 标准 VCF/BED 与 hap.py。我们先以**单样本 DeepVariant WGS 模型**构建低门槛可复制 baseline，再考虑多样本 DeepTrio 和额外 caller 对照。**不要将 DeepTrio 官方案例的指标冒充本项目的 DeepVariant 单样本运行结果。**

NIST 已说明 HG002 出现较新 **v5.0q** 基准，v4.2.1 对 HG002 属于被替换的旧 benchmark。本轮固定 v4.2.1 仅为与 DeepVariant 官方旧案例互相对照；后续新版须另开实验编号、重新记录可分析区及结果，不得混算。来源：[NIST GIAB](https://www.nist.gov/programs-projects/genome-bottle)、[NIST FAQ](https://www.nist.gov/programs-projects/faqs-genome-bottle)。

## 数据契约：固定样本、版本和来源
| 类别 | 唯一标识/文件 | 固定来源 | 使用边界 |
|---|---|---|---|
| 样本 | **HG002 / NA24385**（公开同意研究的 GIAB reference sample） | [GIAB/NIST](https://www.nist.gov/programs-projects/genome-bottle) | 非用户私人样本 |
| 测序读段 | `HG002.novaseq.pcr-free.35x.dedup.grch38_no_alt.chr20.bam` 和 `.bai` | [DeepVariant 官方 case-study bucket](https://storage.googleapis.com/deepvariant/case-study-testdata/) | 已比对的 chr20 BAM；无 FASTQ，此实验**不测试 fastp/比对流程** |
| Reference | `GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.gz` 与配套 `.fna.fai` | [NCBI GRCh38 no-alt directory](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.15_GRCh38/seqs_for_alignment_pipelines.ucsc_ids/) | 不能擅自换 hg19/其他 GRCh38 patch/no-alt 构建 |
| Truth VCF | `HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz` 和 `.tbi` | [NIST v4.2.1 GRCh38](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/AshkenazimTrio/HG002_NA24385_son/NISTv4.2.1/GRCh38/) | chr1–22 真值，比较时用 `-l chr20` |
| Confidence BED | `HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed` | 同上 | 仅在 BED 定义的 benchmark 区域计分 |
| Caller | `google/deepvariant:1.10.0`，`--model_type=WGS --regions chr20` | [Google DeepVariant](https://github.com/google/deepvariant/blob/r1.10/docs/deepvariant-quick-start.md) | 固定标签，还须记录 pull 后 image digest |
| Comparator | `jmcdani20/hap.py:v0.3.12`、`--engine=vcfeval --pass-only -l chr20` | [Google case study](https://github.com/google/deepvariant/blob/r1.10/docs/deeptrio-wgs-case-study.md) 与 [Illumina/hap.py](https://github.com/Illumina/hap.py/blob/master/doc/happy.md) | 标签与实际 SHA digest 需归档 |

> 网络来源采用**官方案例给出的文件名与目录**。此轮未对每一个大文件完成下载/哈希确认；如下载 HTTP 404、索引或 contig 不一致，必须停止并记录 BLOCKED，不得静默改用其他样本/参考版本。

## 操作说明（不自动下载）
脚本：[scripts/run-giab-hg002-chr20.sh](scripts/run-giab-hg002-chr20.sh)

```bash
# 在 Linux/macOS 且可用 Docker、curl、gzip、sha256sum 的环境中：
bash scripts/run-giab-hg002-chr20.sh preflight

# 指定一个不在 AI_book 公开 Git 路径内的工作目录；路径仅为示意，不写入仓库：
export WGS_WORK_DIR=/absolute/non-repository/wgs-hg002-test
export WGS_THREADS=4
bash scripts/run-giab-hg002-chr20.sh fetch
bash scripts/run-giab-hg002-chr20.sh run
```

真实下载和运行仅在明确选择 `fetch` / `run` 时发生；默认 `preflight` 不下载数据。脚本保存输入、输出的 SHA-256 清单和容器 digest。建议先检查可用磁盘、内存、CPU；测试时记录真实峰值。预留 **≥20 GiB** 只是初期工程预算，非已验证最低要求；如资源不足应停止，不自动申请/部署服务器。

## 验收与结果文件
| 指标/文件 | 目的 | 实际验收 |
|---|---|---|
| `metadata/sha256-inputs.txt` | 冻结原始输入版本 | 逐个非空；校验 hash 能复算 |
| `metadata/image-digests.txt` | 固定容器版本 | 有 DeepVariant + hap.py 的真实 digest |
| `output/HG002.chr20.calls.vcf.gz` | 单样本 DeepVariant 结果 | 文件非空、合法 VCF、chr20 与 GRCh38 一致 |
| `happy/HG002.chr20.summary.csv` | 变异真实基准 | 分别提供 SNP、INDEL 的 TP/FP/FN、Precision、Recall、F1 和 UNK |
| `metadata/sha256-outputs.txt` | 结果复核 | hash 可重算；不能替代算法正确性 |
| 运行日志/环境 | 错误、CPU/RAM、duration、下载量 | 使用真实日志，失败状态保留 |

公式：`Recall = TP/(TP+FN)`，`Precision = TP/(TP+FP)`，`F1 = 2PR/(P+R)`；`UNK` 是不参与 benchmark 的候选变异，**不能当作 FP=0、不能忽略其占比**。数据来自 hap.py [官方定义](https://github.com/Illumina/hap.py/blob/master/doc/happy.md)。

**完成标准**：至少一次真正执行成功，获得完整运行日志和 SNP/INDEL 单独评分，保存输入 hash、镜像 digest、结果 hash。只完成 `bash -n`、preflight 或 GitHub Actions 知识库结构验证时均标 `NOT_RUN`（相对于生物信息学实际 benchmark）。

## 当前本轮验证与限制
- **PASS（本地）**：脚本 `bash -n` 语法检查；`preflight` 的纯本地检查可执行。
- **BLOCKED（本轮当前执行环境）**：未提供 Docker；公开数据主机 DNS 无法解析（尝试 `storage.googleapis.com`），所以不能在此环境执行 `fetch` 与 `run`。
- **NOT_RUN**：正式数据下载、DeepVariant 真实调用、hap.py 评分、真实性能与资源评估。
- **不受影响**：已完成的学术/软件目录、下一步的父系与临床来源研究；不允许把当前环境问题当成整个 TOPIC-017 的阻断。
- **下一轮建议**：在具备 Docker/公网数据访问的合法环境运行同一脚本并回传仅公共样本的 QC/摘要；若未具备，改为优先审查 Q03 父系树的公开方法输入、参考谱系树及统计分叉年代，不无限排障。

## G8 补充：31.5 公开 HG002 数据实测与 Docker 镜像局部阻断（2026-11-21）
- [真实运行与 SHA-256/官方 BAM MD5 来源证据](sessions/2026-11-21-hg002-public-data-admission-g8.md) 已入 Draft PR #73；不同于本文件早期单独容器的 Docker/DNS 阻断，**31.5 Linux 实测 Docker 与公开 GCS/NCBI 通信成功**。
- 8 项指定参考/真值/BAM/索引真实下载完成并本地 `sha256sum -c` PASS，BAM 官方 GCS MD5 也确切一致；数据仅存非 Git 研究工作区。
- 原脚本的 `curl` 已修补为 `--continue-at -`，一次真实中断和恢复测试证明不会重下已写入的 .part 文件；不更改 HG002、reference、callset 或标准版本。
- **新局部阻断**：DeepVariant `google/deepvariant:1.10.0` 与 hap.py `jmcdani20/hap.py:v0.3.12` Docker 拉取有限尝试后没有最终 digest，已手动停止并 GET 观察终态；当前 `FETCH/INPUT_QC PASS`，`DEEPVARIANT/HAP.PY REAL_BENCHMARK NOT_RUN`。
- 严禁用论文结果/他人仓库 scoreboard 或 `bash -n` 宣称本项目 SNP/INDEL 精度。后续避免无界 Docker/代理排障；在现成授权环境尝试低风险替代 E2 入口或先完善医学证据体系。

## G9 独立原生工具 E2 实测：AC-05 最小样本已通过（2026-11-21）

**注意本文件 G2/G8 先前“DeepVariant/hap.py 未运行”仍为真实历史事实；G9 是独立的新测试方案，不能替代 DeepVariant 精度。**

- [G9 原始日志、方法、基准统计和复现哈希](sessions/2026-11-21-hg002-native-bcftools-rtg-e2-g9.md) · [GitHub 可复现脚本](scripts/run-hg002-chr20-bcftools-rtg.sh)
- 31.5 Linux 使用前次经官方 BAM MD5 及全部 SHA256 认证的 HG002 35× chr20 BAM；仅提取 `chr20:2000000-3000000`，NIST v4.2.1 高可信 BED 覆盖 **965,991 bp**（166 intervals）。
- **bcftools 1.19 + htslib 1.19** 对真实 BAM 直接 mpileup/call 得到 **1,899** 记录；**RTG Tools 3.13 vcfeval** 独立 haplotype-aware 评分，全部分项来自真实 `snp_roc.tsv.gz`/`indel_roc.tsv.gz` 的完整输入末行。
- 没有额外 post-hoc 质量分数筛选：**SNP Precision/Recall/F1 = 0.9951/0.9972/0.9962**，**Indel = 0.9467/0.9270/0.9367**，总计 **0.9886/0.9874/0.9880**。只能在此公开 1Mb 参考设置内解释。
- **第二次从 PR 下载源码并验证 Git blob** 后，独立重新运行 Exit 0、生成完整日志与 SHA，**变异记录正文 hash 和 RTG summary.txt SHA 与首次一致**，不是模拟执行、缓存 scoreboard 或引用别人的实验结论。
- **验收**：AC-05 公共数据最小可复现 E2 实验 **PASS（G9 局限）**；初始 DeepVariant/hap.py 方案仍 `NOT_RUN`，全 WGS、chrY、药物基因、SV、临床准确率 `NOT_TESTED`。下一阶段回到跨 15 域论文/工具/数据准入体系，不再扩建局部容器排障。
