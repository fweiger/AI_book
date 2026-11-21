# TOPIC-017 / G12｜Haplogrep3 v3.3.2 官方 H100 VCF CLI 功能复现

> 日期：2026-11-22；唯一规范任务 [AI_book #72](https://github.com/fweiger/AI_book/issues/72)；同一 Draft PR #73；requirements_revision=1；协议锁定 `AI_tasks@f0e5ccb90c54265dcd07abb9a975c903eb031ccf` V1.2.2 PILOT。此轮仅使用公开官方回归 fixture，不读取/处理个人 DNA。

## 1. 本轮问题和验收边界

G11 已核实 D04 Haplogrep3 的输入是**已经完成上游调用的 mtDNA VCF/FASTA/HSD**，不是原始 WGS BAM/CRAM。G12 的有界问题是：固定官方 Haplogrep3 版本与树后，官方公开 VCF 能否由本地 CLI 产生可回读的分类/QC 输出，并与同 tag 官方 expected 文件逐字节一致？

**不在本轮验收：** 从 BAM/CRAM 检测 mtDNA 变异、read depth/callability、NUMTs 误比对、污染、组织间异质性、独立分类准确率、医疗结论。官方 expected 输出属于同一软件仓库的回归 fixture，不是独立 truth set。

## 2. 锁定来源和文件完整性

| 项目 | 锁定版本 / 来源 | 核验 |
|---|---|---|
| Haplogrep3 | [v3.3.2 release](https://github.com/genepi/haplogrep3/releases/tag/v3.3.2)，tag commit `78ab84774d8f5646ec846584246fd8eb55a9fb77` | PASS |
| Linux release | `haplogrep3-3.3.2-linux.tar.gz`，49,894,273 bytes | GitHub release digest 与本地 `sha256sum` 均为 `957165143ddd7d6ad9f34cc3af56b784fc236081e031c99bea4a574d6ad70959` |
| 测试 VCF | [test-data/vcf/H100.vcf](https://github.com/genepi/haplogrep3/blob/v3.3.2/test-data/vcf/H100.vcf)，848 bytes | Git blob `da808586b5130824073389b56eb5421c98726cda`；本地 SHA256 `2a0a96425aa457783913b66d7e3deb309970aa77bf9a91bd5153473c016f3ded` |
| 官方主预期 | [expected/H100/H100.txt](https://github.com/genepi/haplogrep3/blob/v3.3.2/test-data/expected/H100/H100.txt)，89 bytes | Git blob `6e5873971cbc341c733fa9ea5a25a403a8f5bad1` |
| 官方 QC 预期 | [expected/H100/H100.qc.txt](https://github.com/genepi/haplogrep3/blob/v3.3.2/test-data/expected/H100/H100.qc.txt)，213 bytes | Git blob `c0d6cf44a7f9b9b528049507f4c7c45077166f7c` |
| 官方 CLI 测试 | [ClassificationTaskTest.java](https://github.com/genepi/haplogrep3/blob/v3.3.2/src/test/java/genepi/haplogrep3/tasks/ClassificationTaskTest.java) | Git blob `22711d11788f9838593701bd4997f1ce4338dca7` |
| 官方 app tree 配置 | [haplogrep3.yaml](https://github.com/genepi/haplogrep3/blob/v3.3.2/haplogrep3.yaml) | Git blob `a4172c7f153752105fd89ad53a2494eef6a5501a`；示例固定 `phylotree-fu-rcrs@1.3` |
| Forensic Update 树 | [tree release 1.3](https://github.com/genepi/phylotree-fu-rcrs/releases/tag/1.3)，tag commit `5c740973cc70a6337aee965c49778dd80b1fa94b` | 官方 tree package SHA256 `ffb1d30c57b2d72d4451785f6a1c7c9ecce273971d2fafaa01f0ca94c566ced1` 与 CLI 安装目录内 package.zip 本地 SHA256 一致；`src/tree.yaml` Git blob `a9ff7df7ba27646dc2c56418614d88583542adb2` |

运行环境：31.5 Ubuntu 临时隔离目录；Linux x86_64；OpenJDK `21.0.11`；未做系统级安装。仅下载官方 release、官方树包和同 tag 公开 fixture。

## 3. 输入样本真实内容

- VCF contig 为 `MT`，参考口径 rCRS，范围覆盖 1–16569。
- **14 条变异记录**，均为 `GT=1/1`；包含 315.1C 插入等变异。
- 该输入没有 read-level BAM/CRAM、DP/AD、base/mapping quality 或每个位点的原始覆盖证据；不能用它检验上游 variant calling、异质性比例估计、NUMTs、污染或真实 WGS 深度。
- 官方单元测试 `testWithVcf` 选择 `phylotree-rcrs@17.0`，断言分类 H100、14 个输入变异、0 个 N、1 个 range；该测试**不对 Quality 分数做断言**。

## 4. 实际命令和结果

固定官方 app 配置推荐的树 `phylotree-fu-rcrs@1.3`，未指定 `--metric`（CLI 默认 Kulczynski），执行：

```bash
./haplogrep3 classify \
  --tree phylotree-fu-rcrs@1.3 \
  --input H100.vcf \
  --output H100.exact.tsv \
  --write-qc
```

- CLI 显示 Haplogrep 3 `3.3.2`。
- 命令退出码：**0**。
- 主分类文件和 QC 文件均成功生成。
- 主输出与官方 `H100.txt` 执行 `cmp`：**逐字节一致**。
- QC 输出与官方 `H100.qc.txt` 执行 `cmp`：**逐字节一致**。

主输出（与官方 expected 完全一致）：

```text
"SampleID"	"Haplogroup"	"Rank"	"Quality"	"Range"
"Sample1"	"H100"	"1"	"0.8356"	"1-16569"
```

QC 输出（与官方 expected 完全一致）：

```text
"SampleID"	"Haplogroup"	"Type"	"Message"	"Missing Mutations"	"Global Private Mutations"
"Sample1"	"H100"	"warning"	"The detected haplogroup quality 0.84 is below 0.9. (QUAL)"	""	"1041G 9410G 13656C 16189C 16192T"
```

最终稳定输出的 SHA256：

| 输出 | 本地 SHA256 | 对照 |
|---|---|---|
| `H100.exact.tsv` | `f401881a31b083c96817b130ef6525fce7e0e2ce2fcc436d24c1aed6d23fb50e` | 与官方 `H100.txt` SHA256 完全相同 |
| `H100.exact.qc.txt` | `731b95cac58435828467593c0ec4adae11ba0259b59053681bce1f9b24ba215f` | 与官方 `H100.qc.txt` SHA256 完全相同 |

## 5. 树版本敏感性：已定位初始 0.0005 差异

首轮使用 `phylotree-rcrs@17.0` 时得到 H100 / Quality `0.8351`，与官方 expected `0.8356` 不同。进一步固定不同树重复运行：

| Tree ID | Top hit | Quality |
|---|---|---:|
| `phylotree-fu-rcrs@1.3` | H100 | **0.8356** |
| `phylotree-fu-rcrs@1.0` | H100 | 0.8356 |
| `phylotree-rcrs@17.0` | H100 | 0.8351 |
| `phylotree-rcrs@17.3` | H100 | 0.8351 |

这不是 CLI 运行失败；**同一 VCF 的分类质量数值会随树版本变化**。最终选用 `phylotree-fu-rcrs@1.3`，因为 Haplogrep3 v3.3.2 的官方 app examples 明确配置该树，且两个输出文件均与官方 expected 精确一致。

必须保留 QC 警告：0.8356 对应四舍五入的 0.84，低于软件的 0.9 阈值；该样本不能被报告为通过该 QC 阈值。Quality 是工具/距离度量相关的分类评分，不能解释成某个祖先身份的后验概率或算法准确率。

## 6. 运行与文档观察

1. `haplogrep3 trees` 不只是列出树：本次它自动从官方树仓库下载并安装配置中的 **8 个树版本**。该副作用发生在临时隔离目录，未改系统目录；在共享/生产环境不能把该命令当成纯只读查询。
2. CLI `--help` 有 `--write-qc`，但 v3.3.2 的 [docs/parameters.md](https://github.com/genepi/haplogrep3/blob/v3.3.2/docs/parameters.md) 参数表未列此项，存在 CLI/文档不一致。
3. runner 文件持久性异常：首次输出为 `.txt` 的主结果在后续独立 shell 观察时变为等长 NUL 字节；原因未定位。改用 `.tsv` 输出名重跑后，主结果跨调用保持 ASCII 正文，且与 expected SHA256 完全一致；QC 文件一直正常。报告只采用稳定 `.tsv` 那次结果，不把异常归因于 Haplogrep 算法。
4. 未调用 Web Service；没有把任何 DNA 上传第三方。

## 7. 证据等级与 AC 影响

- **E0：PASS**——release tag、二进制发布 SHA、输入/expected Git blob、tree tag 与 package digest 均可追溯。
- **CLI 功能回归：PASS**——官方公开 H100 VCF 可分类，main/QC 两个输出与同 tag expected 逐字节一致。
- **E1：PARTIAL**——只验证一项公开 fixture 与树版本行为，不等于对 Haplogrep3 论文方法和全部适用条件的全文审计。
- **独立准确率 E2：NOT_RUN**——expected 与单元测试属于同一项目的内部回归资产，不是独立 mtDNA truth set；没有独立样本、独立变异真值或 precision/recall。
- **AC-02/04：PARTIAL**——D04 工具可执行性和输入/树/输出契约有实测增量，仍未覆盖上游 BAM/CRAM caller 与其余领域。
- **AC-05：保持原状态**——仅 G9 HG002 chr20 1Mb bcftools/RTG 独立 GIAB 基准为限界 PASS；G12 不把内部回归测试冒充 AC-05 独立 benchmark。
- **AC-03：PARTIAL；AC-06：PARTIAL**——47 篇全文未系统审完；Draft PR #73 未合并。
- 原 Goal/Scope/Non-goals/AC 和 15 域框架均未改变；未下载/处理个人 DNA。

## 8. 下一步候选和停止条件

G12 证明 Haplogrep3 的 **VCF → haplogroup/QC** 阶段可按官方版本重现，但不验证从 WGS BAM/CRAM 产生 VCF。下一候选是对已列入 D04 工具的 **Mutserve v2.0.3** 做一项有界上游回归：复用官方公开 `test.cram` / `test1.cram`、rCRS reference 和 `test-data/mtdna/cram/output/variants.vcf` / `variants.txt`，固定版本和输入哈希，比较 Mutserve 实际输出；若其要求的 CRAM index 不存在且无法在临时目录内解决，停止，不安装系统包、不搭平台。Mutserve README 明确 VCF 输出不包含 indels，故即使 SNV/heteroplasmy 功能 PASS，也不能宣称 mtDNA 全变异类型完成；之后应回到全域优先级，避免长期停留在 D04。

**结论：G12 CLI 功能回归 PASS；独立准确率 E2 仍 NOT_RUN。**
