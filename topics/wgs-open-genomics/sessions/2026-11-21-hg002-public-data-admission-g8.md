# TOPIC-017 / AC-05｜G8 HG002 chr20 公开数据接入实测与镜像准备（2026-11-21）

> 唯一业务 Issue [#72](https://github.com/fweiger/AI_book/issues/72)；仍在 [Draft PR #73](https://github.com/fweiger/AI_book/pull/73)；**真实公开 HG002 数据准备现已 PASS，DeepVariant/hap.py 变异准确率 E2 尚未成功运行。** 不涉及用户个人 DNA；原始数据只保留在 31.5 的仓库外临时研究目录，不提交本公开 GitHub。以下日志来自**真实 31.5 Ubuntu Runner 命令返回**，而非论文实验或模拟。

## 原目标、脚本和执行环境
- **任务**：最小公开 HG002 chr20 SNV/Indel 单样本 DeepVariant + GIAB v4.2.1 hap.py 精度基准；不能推广至全 WGS、chrY、临床 PGx、家族寻根。
- **现有未修改 GitHub 原脚本**：[scripts/run-giab-hg002-chr20.sh](../scripts/run-giab-hg002-chr20.sh)，Git blob SHA `fdb01d3f8ccd4996af23110678f713d777ceff07`；本轮从公开 raw URL 获取，并在执行前用 `git hash-object` 核验一致，`bash -n`、`preflight` **PASS**。
- 运行环境：31.5 Linux；Docker 29.1.3 / 16 CPU / 约 24 GiB available RAM；数据盘可用约 305 GB，Docker 系统盘约 87 GB。公开 GCS、NCBI DNS 与 HTTP HEAD 200；不同于前次受限的单独模型容器。
- **源脚本保持不变**；首次下载时间限制触发前，为节省已经下载的 422,596,608 字节，停止旧 Job 后仅在**临时目录中另存**一份包含 `curl -C -` 的续传版本，重新执行并保持同一官方固定数据契约。官方 NCBI 服务器报告 `Accept-Ranges: bytes`。与原研究仓库脚本的这一操作差异明确保留。

## 本轮实际下载与字节级校验（PASS）
| 文件 | 字节数 | 本地 SHA-256（文件自身真实计算） |
|---|---:|---|
| `HG002.novaseq.pcr-free.35x.dedup.grch38_no_alt.chr20.bam` | 1093938924 | `34ac157739e1feeb590f6eb7e11046ccc2aa3277fd55a3ce0942e774d931ed81` |
| `...chr20.bam.bai` | 196136 | `245dcdcc474b1971eeb36fc9a8af37b76ac8b4c7ce06a7bdee64e0c42bd93f34` |
| `GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.gz` | 872949833 | `fb4243ebb014caf27111f24dd62b7ce42160f28581da6f8fcd6cba5977778d02` |
| 同一参考基因组解压 `.fasta` | 3144230986 | `9cce8b926416dd96b152deea85188495b75f7ac8d634cc723a017067be8702b7` |
| 配套 `.fasta.fai` | 7804 | `502a1b8fb73ccd53285c28a0f12df90c818b4fe3de1e862ef47c593ef1a0a4b4` |
| `HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz` | 156252944 | `adb4d4a50048aa13353a06b84fcfcbca09a5d17525efaa4cea44f8822e81175c` |
| `...vcf.gz.tbi` | 1657747 | `23162712553413b10f88916c28bd1238deb703a7237be2910440773beea71894` |
| `...benchmark_noinconsistent.bed` | 11494021 | `fba9a57c36ec88e5d14ea3e259c8866c7935f4998d3ec0fa2d6c3962da5b5575` |

- 原脚本 `fetch` **退出码 0**；生成 `metadata/sha256-inputs.txt`，随后 `sha256sum -c` 对**上述全部 8 项返回成功**，压缩参考及真值 VCF `gzip -t` 通过。
- **独立对照源站元数据**：Google Cloud Storage HTTP 响应 `x-goog-hash: md5=jxpUGjSIA+MEJ1NZrFLaVw==`，下载 BAM 本地 `md5sum=8f1a541a348803e304275359ac52da57`；Python 转为 Base64 后**完全匹配**，这是对 BAM 的来源层字节一致性校验。其余文件 SHA-256 目前是本地复算稳定性，**不代表均已独立对照官方发布哈希**。
- 本轮 GCS BAM 和 NCBI HG002 真值属于**公开参考数据**，未把任何 WGS 文件或个人样本上传到 GitHub。

## 尚未完成与真实阻断
- **DeepVariant 容器第一次下载**：运行了 `docker pull google/deepvariant:1.10.0`，若干 layer 返回 `Download complete` / `Pull complete`，但整个 Job 先达到执行时限，**未得到最终 image digest 或成功镜像**。Docker 29.1.3 与外部 registry 可达；数据端并未阻断。
- **第二次容器拉取**使用原标签和已存在的缓存层继续；`jmcdani20/hap.py:v0.3.12` 亦在受控拉取中。最终成功与否须以独立 Job 的真实终态和 digest 决定，不以“在运行”当 PASS。
- **E2 `NOT_RUN`**：当前尚无 `output/HG002.chr20.calls.vcf.gz`、`happy/HG002.chr20.summary.csv`、Precision/Recall、CPU 内存实际 benchmark。没有编造 SNV/Indel 精度。
- **范围限制**：本轮先前讨论的容器/DNS 阻断被 31.5 替代环境实际突破（`DATA_ADMISSION_PASS`），但镜像拉取仍是局部运行前提；若再次失败，应停止无限下载/运维排障，并只保留真实输入和可迁移执行方法。

## 可检验的唯一后续动作
在**已有全部公开数据已校验**的基础上，待 Docker 镜像 digest 真实取得，执行原 [HG002 chr20 单样本规范](../benchmark-hg002.md) 中的 `run` 阶段并读取 `hap.py` 的 SNP/Indel separate summary；若镜像不能取得，保留 `E2 BLOCKED/NOT_RUN`，不降级输入与精度门槛，不自建平台。**Goal/Scope/AC 均不变**。

> 本文是公开数据研究运行证据，非个人基因检测报告。所有实际结果应继续用同一 Issue/Tracker 原 AC-05 记录，不为本轮新建 Issue。
