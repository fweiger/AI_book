# 2026-11-14 H03原始B9勘误版本取证

从PJM官方网站重新取得Jan14主PDF（2026-01-12 CreationDate，36页，8,750,526 bytes，SHA 9f2826cfc39357c54d6e6203e60946b6ce9ea627cfceeeaf4d4cd343066c6bc8），以pypdf逐页查找B9相关完整数值表，未发现；正文明确所有表格另行Excel。2026Jan13修改的单独B9b有总关联负荷RTO2027=15866，但不能还原Above Embedded。Feb6独立B9和当前合并版都注明订正前处理错误，数值只代表更正后。
尝试Wayback CDX查Jan-Feb旧链接，但联网超时；GitHub公开研究镜像2026 Oct仍是当前更正后SHA，不可将缺失报为已证明不存在。未获取2026Feb6修订前B9原始XLSX bytes，不估算勘误MW。

新增另一量化敏感性：2025/2026原始发布RTO整个夏季峰值预测修订分别2027/28/29/30为 -3735/-4414/-4564/-875MW，同年的B9b总关联预测修订分别-1855/-2128/-2112/+1765MW；绝对值相对规模49.665%/48.210%/46.275%/201.714%（2030异号）。**B9b含嵌入基础模型，比例非因果贡献、非DC专属、非实际需求兑现**。
文件：[详细报告](../reports/2026-11-14_h03_uncorrected_b9_source_gate.md)、[10源状态](../data/h03_pre_correction_b9_source_availability.csv)、[4年规模比](../data/h03_rto_2025_2026_summer_vs_b9b_revision_magnitude.csv)、[验算脚本](../analysis/recompute_h03_pre_correction_source_gate.py)。政治归因依旧UNTESTED。
