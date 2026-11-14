# TOPIC-010 M3-C · 2026-11-14 · 英法珍妮纺纱机资本阈值与利用率敏感性

**归属**：唯一[AI_book #30](https://github.com/fweiger/AI_book/issues/30)、原[Draft PR #31](https://github.com/fweiger/AI_book/pull/31)。**本轮范围**：恢复英法相同24锭纺纱机资本回收的原作者模型，揭示投资利润条件是否高于/低于15%门槛。已有荷英燃料和五国H1—H7研究不重复增量。

## 实际阅读
- Allen 2007 Oxford/Nuffield Working Paper375 [原PDF](https://www.nuff.ox.ac.uk/Users/Allen/unpublished/jenny5-dp.pdf)：网页PDF全文检索数值/模型/历史转述；2009 Cambridge *Journal of Economic History* [正式摘要](https://doi.org/10.1017/S0022050709001326)，**非两次独立历史样本**。
- Nicholas Crafts 2010 Warwick/CAGE Working Paper10/2010 [独立批评PDF](https://wrap.warwick.ac.uk/id/eprint/44710/1/WRAP_Carfts_10.2010_craftsindustrial.pdf)，Table1 4工资×3机器价格12格、pp4–6批判段落；实际文字层可检索，`web.run screen`截图两份 PDF均返回CACHE_MISS，**未完成PDF页面影像目视检查**，未提取任何受版权限制的全文。
- Kelly/Mokyr/Ó Gráda 2023 *Journal of Political Economy* [正式摘要](https://doi.org/10.1086/720890)：英国内1760年代—1830年代郡级低工资、高机械技能的工业化相关性，与跨英国/法国假设投资IRR不属于同一估计量。

## 实际执行过的核查
- 在本地Python使用`IRR(J,w)`按Crafts模型公式独立求根：`ΔL=250×0.4×(1−1/3)=66.6667`、每年修缮额=10%购置成本、设备年限10年，全部12格对照Crafts发表整数/半整数IRR，最大偏差约0.4758个百分点；`w6.25,J840`≈38.025%，`w4.66,J1450`≈2.499%，`w4.66,J840`≈23.791%，`w4.66,J1450,Y300,D0.5`≈17.856%。
- 15%最低收益率的数学边界：法国工资`w4.66`下`Jmax≈1038.14d`，比法国历史推算机器价1450d低28.404%；同机器价1450d法国所需工资`wmin≈6.5087d`，或250天/年下每天利用率`Dmin≈0.55869`。
- 用GitHub工具创建两个源数据CSV、可重跑Python脚本、完整报告；后续读取文件和行数可做存档核对。**本地执行的是等价原型测试，不得将未逐字节运行的GitHub版本脚本记为已经执行或CI通过。**

## 新判断及严重局限
- **更新H6**：相对工资不够，低机器售价、设备占用时间、市场、使用维修/工匠能力是并列必要审计条件。Crafts指出法国用英国机器价即使拿法国工资也过15%，法国原价提高工时也过15%，证明简单“法国低工资→法国一定不采用”不稳健。
- **更新H7**：法国1771已知/复制珍妮机（Allen所引Wadsworth&Mann）和1790约900台采用，说明知识不绝对隔绝；但制造能力/价格/利用率/市场缺独立真值，不能直接断言知识不足或机构阻碍。
- **不宣称H6被证伪**：跨国机器投资动机和英国内郡级低工资高工匠工业化可以共存，不同对象/年份/生产阶段。
- 机器成本840d/1450d是Allen根据更大机器估算24锭机价格；10%维修来自20世纪印度技术类比，40%工时占比假设；不是17世纪原始厂商现金账。
- **荷兰对照空缺**：现有英国—荷兰燃料价和风力工业资料无法合并为同型号1780纺纱机的荷兰机器价、工资、开机日数，不能制造荷兰IRR。H1—H7源家族不独立重复计算。

## 本轮文件
- `data/TOPIC010_M3C_SPINNING_JENNY_PROFITABILITY_CRAFTS_ALLEN_SENSITIVITY_20261114.md`
- `data/jenny_crafts_2010_4x3_irr_published_vs_replication_m3c.csv`
- `data/jenny_allen_crafts_counterfactual_utilization_m3c.csv`
- `data/validate_jenny_profitability_m3c.py`
- 当前会话文件（本文件）与研究README索引。

## 唯一下一步
获得荷兰/法国与英国**同种纺织机器、同一年代**的真实机器生产成本、装机/使用强度与技能培训材料，检验“价格/利用率门槛变化是否能解释实际采用差异”；数据取得前保留`NOT_ACQUIRED`，不把反事实视作真实历史统计。
