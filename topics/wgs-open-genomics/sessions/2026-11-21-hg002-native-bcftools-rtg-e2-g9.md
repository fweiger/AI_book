# TOPIC-017｜G9：HG002 chr20 1 Mb 真实 SNV/Indel 调用与独立 GIAB benchmark

> 日期：2026-11-21；业务任务：[Issue #72](https://github.com/fweiger/AI_book/issues/72)；[Draft PR #73](https://github.com/fweiger/AI_book/pull/73)；**AC-05 最小公开参考基因组 E2：PASS（严格限定 chr20 2–3 Mb、bcftools/RTG）**。这不是原 G2 设计的 **DeepVariant/hap.py** 运行结果，后者仍 NOT_RUN。**仅公开 HG002，不涉及任何个人 DNA 或临床诊断。**

## 1. 实际来源、数据质量和可重复执行

- 直接复用 [G8 已下载并以本地 SHA-256、官方 BAM MD5 校验的 HG002 参考资料](2026-11-21-hg002-public-data-admission-g8.md)：HG002 / NA24385，NovaSeq PCR-free 35× 已比对 chr20 BAM/BAI，GRCh38 no-alt 参考 FASTA/FAI，NIST GIAB **v4.2.1 GRCh38** benchmark VCF/TBI 与 confident BED。**没有重下 G8 公共数据**。
- 计算环境：31.5 Ubuntu 24.04，16 CPU、可用内存约 24 GiB（检查时），所有实际运行只使用 4 threads。官方 Ubuntu noble 包 **bcftools 1.19 / htslib 1.19** 与二进制依赖 `libhts3t64/libhtscodecs2` 仅 `apt download` 并 `dpkg-deb -x` 到 **非公开 Git 工作区的临时目录**，未全局安装。实际动态链接及 `bcftools --version` PASS。
- 独立比较器：[RTG Tools 官方 3.13 发布版](https://github.com/RealTimeGenomics/rtg-tools/releases/tag/3.13)，下载官方 `rtg-tools-3.13-nojre.zip`（9,048,648 bytes），本地 SHA-256 `bc5c6badb07d7e20d1c5c557bd6d571a022bbd9f58fa1e3840bcff9431a18f96`；Java 21；RTG 3.13 / Core `c27844a5bb`。官方 [README](https://github.com/RealTimeGenomics/rtg-tools) 描述 vcfeval 为 **haplotype-aware** comparator；与简单坐标交集不同。
- 独立脚本：**[scripts/run-hg002-chr20-bcftools-rtg.sh](../scripts/run-hg002-chr20-bcftools-rtg.sh)**，Git blob `819278d12b78cae97da8f27c4d49a93228b4942d`。脚本不下载公开数据、不安装工具、不处理个人基因；用环境变量传递已有 G8 文件路径、bcftools/RTG 执行路径、单独输出目录；`preflight` 与 `run`，运行前 `sha256sum -c`，拒绝覆盖已有输出。
- 第一次手动命令和脚本化第二次运行的变异记录正文 **SHA-256 均为 `472eaed46a664cbb675dc2c09d224d7836c0680345f937100a0a48d6fad912b0`**（剔除 VCF 元信息行后，`bcftools view -H | sha256sum`），且 RTG **`summary.txt` SHA-256 均为 `24dac88c2c4ad5738ffa6b2d65c3280eabf98eeda79d25a1067fe5308a515ba6`**；原始压缩 VCF 二进制 SHA 不同（header/压缩可能含非位点元信息），所以以实际变异记录正文与评分摘要进行一致性验证。
- 真实运行 Job `wc_job_f-esO0u5Wkjsu8r2` **`completed/exit=0`**。手动首次 bcftools calling **4.31s**，脚本复现 **4.09s**（`/usr/bin/time` 进程耗时，非全链路耗时）。RTG vcfeval 首次 **1.49s**；不从局部小区间推断全 WGS 时长。

## 2. 确切方法与数据不可泄漏性

### 数据输入层

| 层 | 输入/范围 | 质量口径 |
|---|---|---|
| reads | 与 G8 对照 GCS MD5 的同一 HG002 35× chr20 BAM | BAM 公开科研数据，正式分析没有使用 truth VCF |
| reference | `GCA_000001405.15_GRCh38_no_alt_analysis_set.fasta`，`chr20` 长 **64,444,167 bp** | 用其 `.fai` 读取 chr20 片段再生成 RTG SDF；相同参考构建 |
| caller region | `chr20:2000000-3000000`（约 1 Mb） | bcftools 对 **此区间**调用；不代表 chr20 全部 |
| truth | GIAB HG002 `v4.2.1` GRCh38 参考 VCF 的对应区间 | 只用于**独立评估**；不参与变异调用 |
| evaluation BED | NIST `benchmark_noinconsistent.bed` ∩ chr20 `[2000000,3000000)` | **166 个区间，965,991 bp**（约 96.60% 的 1 Mb） |

### caller 与 comparator

调用（实际执行的参数）：
```bash
bcftools mpileup -Ou --max-depth 250 --threads 4 \
  -f GCA_000001405.15_GRCh38_no_alt_analysis_set.fasta \
  -r chr20:2000000-3000000 HG002.chr20.bam \
 | bcftools call -m -v --ploidy 2 -Oz --threads 4 -o HG002.chr20_2-3Mb.calls.vcf.gz
```
- bcftools `mpileup | call` 真实生成 **1,899 条变异 VCF 记录（1,543 SNP、356 Indel）**；其中部分可能在 confident BED 外，不能把 1,899 全算入 benchmark 分母。
- RTG `vcfeval` 使用单独 truth、同 build 的 chr20 SDF 和 `--evaluation-regions` 定义的可信 BED，`--roc-subset=snp,indel --vcf-score-field=QUAL`。**RTG 默认仅使用其判为 passing 的记录，分析时没有再施加自选 QUAL cutoff**。不能把 RTG “最大 F-measure 最优阈值”的行冒充原始未额外筛选指标。
- 比较器实际写出 `tp.vcf.gz / fp.vcf.gz / fn.vcf.gz / summary.txt / snp_roc.tsv.gz / indel_roc.tsv.gz`；复现脚本从 ROC **最后一行（全部评估输入、无额外 QUAL 阈值）**读取两类指标，保留 RTG 对不同 VCF 表达方式产生的 **TP-baseline 与 TP-call 两种口径**。

## 3. 真实计算结果（无额外 QUAL 筛选，CONFIDENT BED 内）

| 类型 | GIAB baseline | 评估 query | TP-baseline | TP-call | FP | FN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **SNP** | 1434 | 1441 | 1430 | 1434 | 7 | 4 | **0.9951** | **0.9972** | **0.9962** |
| **Indel** | 233 | 225 | 216 | 213 | 12 | 17 | **0.9467** | **0.9270** | **0.9367** |
| **Total** | 1667 | 1666 | 1646 | 1647 | 19 | 21 | **0.9886** | **0.9874** | **0.9880** |

**分母与真值口径**：GIAB 原始 chr20 1 Mb VCF 区间提取有 1,744 条记录；在 NIST confident BED 评估与 RTG 分型后，最终 baseline 1,667；**不能把这三个数字混为同一集合**。SNP/Indel 指标从 RTG 各自 `*_roc.tsv.gz` 最终完整评分行直接读取，TP 两列可能不同，属于 haplotype-aware variant representation 调整；不应以单一“匹配位点数”覆盖该差异。

**重要科学解释**：此次 SNP F1 0.9962 高于 Indel F1 0.9367，但只在该 **HG002 / NovaSeq PCR-free 35× / 参考 build / 1 Mb 高可信 BED / bcftools 1.19** 组合下成立。不能推断所有个人 30×/40× 短读长 WGS、复杂医学基因、Y/mtDNA、SV/CNV、HLA、药物基因或东亚队列有此精度；不能直接比较论文/厂商的完整染色体或另一版本 truth set。

## 4. 原始结果校验与再现

第一次手动结果：
- callset `sha256=f234425fc1299ccbb5df581432d6629d74ea0baa2f1718280c60070f60a473fa`
- GIAB truth subsection `sha256=3a6f4bf291d0177178670bd4260884c824ef5d0d0f54c0c2f7a18022d8ff2140`
- confident BED `sha256=a5d74c0a2575e0cca5236720c56e243525a20f1f8957d3ca75fb8020cc4ca672`
- RTG `summary.txt sha256=24dac88c2c4ad5738ffa6b2d65c3280eabf98eeda79d25a1067fe5308a515ba6`

**从同一 GitHub 脚本再跑一轮**：
- 本轮从 PR 下载脚本并核 `git hash-object=819278d12b78cae97da8f27c4d49a93228b4942d`，`bash -n`、`preflight` 均 PASS。
- 复现实验 `run exit=0`，生成 `inputs-checksums.log`、`caller.log`、`vcfeval-stdout.log`、`vcfeval/summary.txt`、`no-extra-quality-filter.tsv` 和 `sha256-outputs.txt`；SNP/Indel/total 精度表 **与首次完全一致**。
- 二次 VCF 压缩文件 SHA `4ea4725fc03b628902c0069d442df8a0690c6229e48414726b604896ef8fd708` 与首次不同，但记录正文哈希 **相同 `472eaed46a664cbb675dc2c09d224d7836c0680345f937100a0a48d6fad912b0`**；RTG summary 哈希也相同。这说明变异记录及其评估结果已跨两次执行一致，并非仅展示缓存文件或引自他人的 scoreboard。
- 公开 Git 仓库仅存**脚本、可读报告、哈希和统计摘要**，从未上传或复制完整 HG002 BAM、VCF 或参考 FASTA 到 Git。

## 5. 最小复现命令（在已有 G8 数据、bcftools 和 RTG 的环境）

```bash
export WGS_WORK_DIR=/absolute/private-or-temp/path/containing-G8-inputs
export WGS_EVAL_DIR=/absolute/NEW/outside-public-git/output
export BCFTOOLS_BIN=/absolute/path/to/bcftools
export RTG_BIN=/absolute/path/to/rtg
export WGS_THREADS=4
# BCFTOOLS_LIB_DIR=/absolute/path/to/isolate-unpacked-libs  # 仅原生动态库不在系统默认路径时
bash scripts/run-hg002-chr20-bcftools-rtg.sh preflight
bash scripts/run-hg002-chr20-bcftools-rtg.sh run
```

脚本不重新下载、不覆盖已有输出、不安装系统程序；若使用另一个 GNU/Linux 发行版必须重新核依赖。完整原始日志及 DNA 文件保留在 31.5 的非公开临时目录；任何临时目录未来清理后，以此报告的输入 hash、版本、命令和源码可重建。

## 6. AC、偏差、现存缺口与唯一后续建议

- **AC-05（公开样本最小可复现实验）：PASS / E2 PASS（限定 G9 的 1Mb bcftools + RTG 可复现实验）**；数据与调用在 31.5 实际发生，独立真值/输出/二次运行哈希可核。此前 G2 的 **DeepVariant/hap.py 固定方案：仍 NOT_RUN**，不得拿 G9 指标替换 DeepVariant 的性能。
- **D0 ALIGNED**：按前一 Tracker §7，合法复用 G8 数据，未改 Goal/Scope/AC；以真实实验替代继续修 Docker，阻断被局部绕开，原 15 域知识地图主线仍是唯一目标。
- **未完成**：AC-02 的 39 项工具全体许可证/运行审计、AC-03 的 47 篇论文逐篇方法和反证审计、AC-04 各领域可靠性外推核验、AC-06 Draft PR #73 未合并均需继续；这次 1 Mb 实验不能证明全部研究已完成。
- **当前唯一下一步建议**：回到用户最初关心的 **15 维全景**，优先在已建立的质量×论文×工具矩阵中审计每域 1 篇最重要的一手论文及方法/真实输入条件（15 域一轮的有限工作包）。已有公开实验说明“工具真正可跑”与“文献声明范围”应独立标注，避免长期只围绕 D01 的 Docker/数据微调而偏离主线。
