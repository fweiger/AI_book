# P06 · 临床可行性审计字段与时间轴字典 V1

此表仅定义**字段规范和必需计算结果**。真实病人层数据由医院系统生成/保存；公开仓库不得保存、示例化或导入可识别患者数据。

## 数据分层

| 逻辑表 | 主键/粒度 | 原始内容（只在批准环境） | 必要输出 |
|---|---|---|---|
| \`person_master\` | 患者内部主索引，最终转换为 study_key | 来源科室、基础危险因素、既往卒中/TIA、三高病程、药物、研究授权 | 唯一患者数、按来源去重 |
| \`sleep_exam\` | study_key × PSG/活动记录日期 × 检查序号 | PSG 原始 EEG/事件评分及 AHI/低氧；主观睡眠史另表 | 可用 PSG、非呼吸觉醒可重判人数、睡眠记录日期 |
| \`vascular_exam\` | study_key × 影像日期 × 部位/模态 | 颈动脉超声、HR-VWI MRI、斑块负荷/成分/IPH/纤维帽判读 | 影像是否合格、研究基线和随访日期 |
| \`blood_sample\` | study_key × 采血日期 × 采血时相 | CBC、单核亚群、预设炎症/氧化应激检测、感染/药物状态 | 有效血样、匹配时间差、检测是否可比 |
| \`cea_specimen\` | study_key × 手术日期 × 标本编号 | CEA 医疗指征、病理、组织保存和定位 | 标本可用性、是否同人术前配对 |
| \`clinical_event\` | study_key × 临床事件日期 | 首次卒中/TIA、手术/干预、死亡、失访、重要用药变化 | 暴露相对卒中时间顺序、失访与排除原因 |

研究患者主索引不得使用姓名/手机号/身份证字段导出；院内维护可追溯的映射表，研究公开材料只有**汇总**。若使用时序中的月/日，必须符合院内授权，不在公网公布精确日期。

## 核心测量变量字典

| 字段 | 记录方式 | 误读/偏倚检查 |
|---|---|---|
| \`psg_usable\`, \`event_annotation_available\` | 分别二值＋未知，附原始导联/评分版本 | 有 PSG 不等于可以区分呼吸性与非呼吸性觉醒 |
| \`arousal_nonresp_per_hour\` | 事件级重新评分后定义：符合规则的非呼吸相关觉醒次数 / 睡眠小时数 | **不能简单用总觉醒指数减 AHI**；须在时序上关联呼吸事件/腿动/其他触发 |
| \`arousal_resp_per_hour\`, \`ahi\`, \`odi\`, \`hypoxic_burden\` | 呼吸事件/血氧有效时段口径写清 | ODI 与 AHI 不等价，呼吸低氧可能造成混杂 |
| \`n3_minutes\`, \`nrem_swa\`, \`tst_minutes\`, \`waso_minutes\` | PSG 分期、原始 EEG 支持时记录 | 一晚 PSG 对长期睡眠暴露可靠性有限 |
| \`fragmentation_actigraphy\` | 设备型号、固件、算法、记录天数及有效日比例 | **不能**与 PSG 非呼吸觉醒用一个阈值或同一指数 |
| \`mri_hrvwi_quality\`, \`iph_present\`, \`plaque_burden\`, \`fibrous_cap\` | 影像模态、序列、部位、盲法读片与一致性 | 复查需确认同一侧、相同解剖段；“高危”定义必须预注册 |
| \`cea_eligibility\`, \`plaque_pathology\` | 是否因医疗指征手术，标本定位和结果 | 手术选择偏倚不能被简单统计回归全部消除 |
| \`sample_timing\`, \`infection_status\`, \`cbc_count\`, \`immune_assay\` | 相对睡眠觉醒的采血时相、近期感染/药物 | 炎症标志物存在昼夜变化与急性期效应 |
| \`htn_prior\`, \`dm_prior\`, \`lipid_disorder_prior\` | 睡眠基线**之前**有诊断/用药/指标依据；保留未知 | 当前用药控制正常不代表没有三高 |
| \`anti_htn_med\`, \`statin_med\`, \`glucose_med\` | 基线时有无、类型、变更日期 | 后续用药变化可能是时间变化混杂 |
| \`stroke_tia_first_date\`, \`sleep_exam_date\`, \`mri_date\`, \`cea_date\` | 日期由院内安全系统保管，输出时间差/先后分类 | 术后/卒中后睡眠不能声称暴露早于疾病 |

## 统计所需的 derived 字段（只在院内生成）

- \`sleep_before_first_stroke\`：睡眠记录日期是否早于首次卒中/TIA；从未卒中者另一个值，不把“没事件”混为“事件前”。
- \`sleep_mri_gap_days\`, \`sleep_blood_gap_days\`, \`sleep_cea_gap_days\`：确保配对窗口与具体模态、病变部位一致。
- \`imaging_followup_gap_days\`：仅当存在同一血管段可比影像才成立。
- \`has_early_plaque_at_baseline\`：严格区分新发斑块分析和既有斑块进展分析。
- \`baseline_hyperrisk_count\`：三高 0–3；任一项未知则总分不可认定为 0。
- \`exclude_recent_stroke\`, \`exclude_sdb_confounded\`, \`exclude_infection\`：预先定义时间窗及分析目的，排除与敏感性分析应区分。
- \`eligible_r1\`, \`eligible_r2\`, \`eligible_r3\`：独立队列资格，允许重叠但每类分母不得重复计数。

所有缺失值应区分 **未知/无记录/不适用/不合格/明确否定**，禁止把空白默认作“未患病”或“正常”。

## 质控门槛

- 先检查多次 PSG/影像按规则选定后的患者数是否唯一。
- 核查检查日期/卒中日期矛盾，不能靠“距术前最近”替代时间因果顺序。
- 主要暴露与结局在看回归结果前冻结，交互分析只预设少数关键项（如基线三高状态）。
- 对每个方案输出“可使用的病例数、预期事件数或连续终点方差、可用随访率”，正式样本量用实际估计值而非手术理论总数。
