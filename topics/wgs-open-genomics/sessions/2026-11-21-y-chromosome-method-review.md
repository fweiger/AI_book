# 2026-11-21｜Q03 Y 染色体开源工具方法核查
- **问题**：独立 WGS 能直接输出父系家族史吗？为什么 Yleaf、Y-LineageTracker 和 yhaplo 对同一原始测序结果可能给出不同深度？
- **原始来源已读**：[Yleaf 官方 README](https://github.com/genid/Yleaf/blob/master/README.md)、[Y-LineageTracker 官方 README](https://github.com/Shuhua-Group/Y-LineageTracker/blob/main/README.md)、[yhaplo 官方 README](https://github.com/23andMe/yhaplo/blob/master/README.md)；[Y-LineageTracker 2021 方法摘要](https://pubmed.ncbi.nlm.nih.gov/33750289/)；[yhaplo 2016 bioRxiv](https://doi.org/10.1101/088716)；[YFull tutorial](https://www.yfull.com/tutorial/)。
- **验证实得**：Yleaf 支持 BAM/CRAM/VCF 与多参考树，但基因型未覆盖的点和参考推断需要审慎；Y-LineageTracker 明确区分 `time`（NRY haplogroup divergence）与 `tmrca`（Y-STR haplotypes）；yhaplo README 指出其输入 SNP 位置要求 hg19/GRCh37，且 variants-only VCF/低覆盖与阵列 Y 位点太少会导致误判。
- **新文档**：[y-chromosome-methods.md](../y-chromosome-methods.md)，定义 Y01–Y05 复现矩阵和每步“可以推断/不可推断”的证据门槛。
- **论文状态**：已读 README 与论文可检索摘要，没有对所有方法论文逐页复审。2026-11-21 预印本 DOI 已核对，并修正错误的 DOI 草稿。
- **软件许可**：yhaplo 的官方 README 表述为非商业授权，后续使用需逐仓审查 LICENSE；不可把 GitHub 公开直接等同无限制商业使用。
- **实际运行**：无父系单倍群软件真实执行，E2 NOT_RUN；未处理任何个人数据。
- **下一步**：用合法、公开并具备父系足够覆盖的男性样本，为 Y01/Y02 构造统一参考版本、相同 callable SNP set、工具输出分歧的可复现试验；不要因同一大单倍群就判定名人后代。
