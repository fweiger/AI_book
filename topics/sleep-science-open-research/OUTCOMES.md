# TOPIC-009 · 睡眠结果与数据口径

| 结果 ID | 维度 | 主观/客观指标 | 解释限制 |
| --- | --- | --- | --- |
| SL01 | 数量 | TST：总睡眠分钟数；睡眠日记/PSG/活动记录仪 | 设备估算误差、补觉影响 |
| SL02 | 连续性 | SOL 入睡潜伏期、WASO 入睡后清醒、睡眠效率 SE=TST/卧床时间 | 入睡潜伏期主观估计不精确 |
| SL03 | 节律时间 | 起床/入睡/睡眠中点与自然光照时间 | 需明确时区、夏令时、工作日 |
| SL04 | 规律性 | 每周睡眠中点或起床时间 SD | 一周样本不足以断定节律障碍 |
| SL05 | 结构 | PSG 的 N1/N2/N3/REM、觉醒指数 | 手环估计睡眠阶段不能充当 PSG |
| SL06 | 日间恢复 | ESS、KSS、PVT、主观疲劳、功能损害 | PVT 存在学习和昼夜节律效应 |
| SL07 | 睡眠障碍分类 | 临床判断的失眠、OSA、异态睡眠等 | 问卷/消费设备只能筛查不能确诊 |
| SL08 | **主观满意度** | 睡眠满意度、自评质量、恢复感 | **不能直接从 TST、HRV 或设备深睡比例推断** |

主观满意度被单独保留，避免使用“睡了足够长”替代“睡得好”。维度框架参考 AHA 2025 与 Buysse 2014；本库 SL07 作为疾病分类结果标识，与正向睡眠健康指标分开。

研究定义参考 [S002](https://pmc.ncbi.nlm.nih.gov/articles/PMC3902880/)、[S021](https://pmc.ncbi.nlm.nih.gov/articles/PMC12147655/)。

**最小采样字段**（研究数据字典，非个人文件）：local_datetime、timezone、sleep_diary_id、bedtime、sleep_onset_estimate、wake_events、final_wake、get_up、caffeine_time、environment_time、wearable_device_model、measurement_quality_flag、intervention_flag。不得将实际个人数据提交到本仓库。

计量建议：所有时间序列保留原始时间戳和传感器偏移；预定义夜间窗口，避免用观察到的异常回头选择研究窗口。
