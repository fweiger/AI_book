# 2026-11-21｜AC-05 HG002 chr20 官方基准复现规范

- **规范来源**：[AI_book Issue #72](https://github.com/fweiger/AI_book/issues/72)，[Draft PR #73](https://github.com/fweiger/AI_book/pull/73)。
- **最初问题**：已找到 DeepVariant、hap.py 和 GIAB 后，怎样从“仓库存在”推进到可审计的真实测序变异准确率？
- **所读一手材料**：[DeepVariant r1.10 DeepTrio WGS case study](https://github.com/google/deepvariant/blob/r1.10/docs/deeptrio-wgs-case-study.md)（包含 HG002 chr20 BAM、真值集、参考基因组及 benchmark 命令）；[Illumina hap.py comparison handbook](https://github.com/Illumina/hap.py/blob/master/doc/happy.md)（TP/FP/FN/UNK 与指标定义）；[NIST GIAB 主项目](https://www.nist.gov/programs-projects/genome-bottle)及[2026 FAQ](https://www.nist.gov/programs-projects/faqs-genome-bottle)（HG002、公开数据许可及新版 benchmark）。
- **实际交付**：[benchmark-hg002.md](../benchmark-hg002.md) 为可审计数据契约；[scripts/run-giab-hg002-chr20.sh](../scripts/run-giab-hg002-chr20.sh) 为分离预检/下载/运行的脚本，脚本使用 GRCh38 no-alt、NISTv4.2.1、DeepVariant WGS 1.10.0、hap.py 0.3.12。
- **本地可核结果**：脚本本地 `bash -n` 检查通过、`preflight` 可调用。当前执行容器无 Docker，且无法解析 `storage.googleapis.com`；**未下载 HG002 数据、未运行变异检测、未获得真实 Precision/Recall/F1**。
- **方法性修正**：Google DeepTrio 的官方单/三人真实数值不是本项目的结果；v4.2.1 是固定复现基线，NIST 已公布 v5.0q，不能称旧版最新。chr20 SNP/Indel 评测不代表 chrY 或全基因组质量。
- **论点与证据状态**：C017-002 从目录级 E0 延伸到有真实官方输入与可执行规范的 E1；**E2 仍 NOT_RUN**。未新增临床结论。
- **竞争性解释/失败点**：即使 hap.py 统计很好，也可能受 BED 限定、等位表示、参考组装、测序平台和训练数据重叠影响；必须保存 UNK 及分层表现。
- **隐私**：使用公开同意的 GIAB 样本；没有处理或公开真实个人 DNA。
- **下一轮研究动作**：在具备 Docker/公共数据可访问环境尝试同脚本；若真实阻断持续，则不扩展基础设施，以 Q03 父系单倍群开放方法学审计推进核心研究。
