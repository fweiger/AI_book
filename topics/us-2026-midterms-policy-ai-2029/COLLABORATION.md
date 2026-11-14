# TOPIC-011｜可被不同AI接手的研究合同

总Issue [#41](https://github.com/fweiger/AI_book/issues/41)，H01—H08对应[#42—#49](https://github.com/fweiger/AI_book/issues)，数据任务[#50](https://github.com/fweiger/AI_book/issues/50)。AI可独立参加、互相反驳、提出H09+，**不采用赞成/反对两个固定阵营或AI票数作为真相**。

## 每个工作包的输入输出
```yaml
topic_id: TOPIC-011
work_id: H01  # H01-H08 or DATA-00
parent_issue: 41
objective: 一个明确要验证/否定的机制边
frozen_asof: YYYY-MM-DDTHH:mm:ssZ
scope: 研究时段/国别/州或公司样本
inputs: 官方来源与许可数据的引用或链接
outputs: [hypothesis_card, primary_sources, support, strongest_counterevidence, metric_definition, reproducible_test, next_prediction]
acceptance: [发布时间可核, PIT无后视, 不虚构数据, 混杂因素, 强反例, 下轮行动]
status: NEEDS_EVIDENCE
```

## 子AI单条评论交付
- 本轮新增什么；关联H-ID/候选边/路径；检索日期和原始URL/直接核查深度。
- 至少一项支持证据与一项最强反证，或如实写“尚未找到”；同源信息注明引用链。
- 指标公式、单位、频率、样本、缺失率、对照设计、实际执行环境以及计算文件/代码链接。禁止公开私有地址和凭据。
- 预注册下一次可能支持/反驳的事件及最迟判定时间；不能用后验结果改预测。
- 结论：背景事实/描述相关/因果证据等级，状态 UNKNOWN/SUPPORTED/CHALLENGED/MIXED。
- 只有授权维护者审核PR合并后可更新正式C-ID；外部AI遵守[仓库投稿办法](../../CONTRIBUTING.md)。

## 建议运行节奏（非已部署定时任务）
周：政策/项目与财报事件扫描；月：证据与假说状态；季度：实际数据检验和冻结预测评分；任期结束2029-01-20总结。优先DATA-00、H01、H02、H04，再H03/H05/H06/H07；H08作为贯穿的反事实。
