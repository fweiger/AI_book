# TOPIC-011｜2026-11-14 专家层—假说层—指标层—逐边因果链结构升级

## 用户问题
将原有美国2026中期选举至2029任期终点的宏观研究与财经/行业专家持续输入合并为两个入口；将所有原有指标抽离为可复用统一指标层；拆出马斯克Texas优惠、国会监督、赦免法律程序以及CPI/PCE→Fed→再融资两条正式H09/H10研究方向；形成可长期迭代的因果网络，而不是通过评论者共识断言事件将发生。

## 实际读取
- GitHub原PR #51的TOPIC-011 README、FRAMEWORK、PROTOCOL、METRICS全部内容、H01—H08注册表、K01—K10候选边、知识图谱、VIEW-S001十条主张及E001—E067事件账本。
- 继承前一轮已经通过Ubuntu MCP从大湾区老姚视频转写完整读取的文字事实；本轮**没有重新回听原视频音轨**，没有上传用户私人设备路径或受版权保护的转写。
- 联网核查：[Texas Tribune 2026-11-04](https://www.texastribune.org/2026/11/04/gina-hinojosa-texas-democrat-governor/)、[Houston Public Media 2026-11-11](https://www.knkx.org/2026-11-11/how-the-midterm-election-results-could-impact-elon-musks-many-business-interests-in-texas)、[Reuters 2026-11-08拟监督报道](https://www.reuters.com/legal/government/democrats-eye-musk-miller-probes-after-midterm-rout-2026-11-08/)、[BLS 2026-11-10 CPI](https://www.bls.gov/news.release/archives/cpi_11102026.htm)、[BLS 2025停摆缺失规则](https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm)、[Fed Waller 2026-11-10原讲话](https://www.federalreserve.gov/newsevents/speech/waller20261110a.htm)；2026-11-14检索。政策新闻不替代州政府官方合同/国会传票原件。

## 核心结构变化
1. EX(专家身份)→WORK(作品/发布时间)→VIEW(逐主张)→VIEW×H(支持/质疑/延伸，非独立事实证据)；已建立EX001/WORK001，兼容原VIEW-S001与VIEW-S001-C01—C10。
2. H09：公司级政治资源/政策合同监督对财务的增量作用（Issue #55），与H01/H06/H07相互关联；H10：通胀/PCE与Fed实际政策反应对再融资的传导（Issue #56），与H07/H08相互关联。**H01—H10全部UNTESTED**；正式C-ID仍空。新增研究结构必须MINOR 0.2.0。
3. 指标I层：`metrics/catalog.csv`统一91个指标或指标族（I01—14旧H、37项旧H03命名项、I15—54新）；每项频率、单位、实体粒度、PIT来源限制；仅BLS 7行真实数字种子，**不假装已有完整时序**。
4. CHAIN层：至少5条新机制子链，Texas、国会、赦免、Fed、政治×融资交互及旧宏观路径；`chain_edges.csv`逐边识别所需指标与反例。原始K07/K08/K09**已被旧因果边占用**，历史VIEW草稿冲突现改为`CHAIN-MUSK-...`与`CHAIN-FED-01`，K01—K10不重编号。
5. CASE-MUSK：州政府优惠、国会监督、赦免法律和财务冲击分开台账，按法律实体/合同/公告/生效日/现金回流执行；空表头明确缺数据。
6. 所有研究路径只能引用同一指标库与事件池，允许观点同源去重、支持反证并列、边级状态随时间变更，不用最后股价倒推先前所有因果边成立。

## 重要边界与反证
- Texas州政权换届是政治事件；**合同实际撤销/返还仍未通过本研究核到可确认的州官方文书**，不向系统写入“已追回”。
- 2026选后民主党议员提出调查计划并不证明已向Musk/Tesla签发正式传票；更不证明违法事实。
- 总统赦免需官方签署及具体范围；第五修正案和仍存在的州刑事追诉风险及国会程序需逐项核对。任何观点不能断言“签赦免令=无限强制证言”。
- BLS公布2026年10月headline月环比0.4、core0.3；2025年10月多系列缺失导致2026年10月同比NA（有些项目单独可见）。Waller 25/50bp是**条件性个人意见**，而不是委员会决策。只有未来实际决议经官方核实才记I24。
- 美股信用等结果与利率、产业周期、全球需求常有共同变动；企业政策依赖与债务双重暴露的效应必须有事前样本、对照、时间点和估计框架。

## 新建/更新文件
- 新目录：experts 3文件、hypotheses观点H多对多1文件、metrics 4文件、chains 3文件、cases/musk-2026 3文件；保留全部历史H03原CSV数据不迁移。
- 旧文档：README、FRAMEWORK、HYPOTHESES、METRICS、PATHWAYS、questions、知识图谱、知识地图、数据与专家入口、指标和因果注册表、CHANGELOG及本会话索引已更新到v0.2.0；历史预测和先前观点不重写事实。

## 待办/未取得
- FEC逐笔捐款真实完整口径、Texas州及地方完整合同/协议生效/兑现、针对特定公司正式传票、任何赦免公文、同口径Tesla和私人公司财务、债务及市场反应时间序列；故**没有统计模型结果、显著性或任何概率预测**。
- 下一轮优先确定法人与政策合约、官方程序日期，再冻结2026-11-02可得数据并做对照面板；缺失实物证据严格标NA。
