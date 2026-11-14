# TOPIC-012｜公开来源与证据等级（种子基线）

> 本页只保存公开、可合法访问的权威资料和研究层级；2026-11-14 首轮网页阅读。完整论文如未读取，不以“精读”标记。来源提供线索不是模型验证。

| ID | 来源 | 时间/属性 | 当前可据此说明什么 | 不可外推的结论 |
|---|---|---|---|---|
| S01 | [SpaceX Capabilities & Services](https://www.spacex.com/assets/media/Capabilities%26Services.pdf) | 官方报价 PDF，载明 through 2026；已查看PDF页面 | Falcon 9 标准付款方案 $74M；LEO 22,000kg为完全一次性配置的最大运力说明 | 实际同轨、同一次任务可按$74M买到22t运力 |
| S02 | [SpaceX Falcon 9](https://www.spacex.com/vehicles/falcon-9/) | 官方型号信息，2026-11访问 | 网页示出LEO最大载重约22.8t等构型信息 | 可复用条件与任意SSO轨道都能达到该最大值 |
| S03 | [SpaceX Rideshare](https://new.spacex.com/rideshare) | 官方公开报价页面，2026-11检索 | 50kg SSO起约$350k，增量$7k/kg，特定拼车条件 | 大型数据中心可直接按该单价整批运输 |
| S04 | [NASA Small Spacecraft Technology - Thermal Control](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/) | NASA技术综述，2026-05-07 | 现有热控技术分类：可展开散热器、热管、热开关、相变等 | 已具备商业GW计算集群所需的热控技术成熟度 |
| S05 | [GAO-26-109012 Data Centers in Space](https://www.gao.gov/products/gao-26-109012) | 美国政府问责署，2026-04-28，已读官网报告页 | 核心挑战：散热、通信、辐射、高密轨道、可靠性和商业成本 | 大型在轨数据中心现已大规模运行 |
| S06 | [BCG Space-Based Data Centers: Cost and Outlook to 2040](https://www.bcg.com/publications/2026/space-based-data-centers-cost-outlook) | 咨询机构情景研究，2026-08-27，已读摘要与公开说明 | 条件模型当前20年 TCO：太空约$660–750M/MW，地面约$230–300M/MW；发射、故障、kg/功率是关键敏感参数 | 所有轨道/发射方案的实际已成交成本和确定未来价格 |
| S07 | [Aili et al., Nature Electronics, 2025, The development of carbon-neutral data centres in space](https://doi.org/10.1038/s41928-025-01476-1) | 同行评议论文，2025；目前仅核GAO列有此参考 | 后续专业文献入口 | 已核论文全文、可复现实验或具体数字 |
| H01 | 用户2025-11-08太空散热讨论 | 历史会话片段 | 用户问题、理想MW散热估算 | 工程验证/完整原始聊天 |
| H02 | 用户2025-11-14废热温室讨论 | 历史会话片段 | 2GW热输入情景、5km²理想面积、1000万m²供暖量级 | 温室真实在轨可建造与商业收益 |

## 未来新增来源时必须记录
`source_id, publisher, published_date, event_or_quote_date, retrieved_date, document_url, read_depth, claim, units, assumptions, applicability, independent_from, limitations`。

优先级：运载服务商任务专属公开合同/发射许可数据及NASA/ESA官方工程资料 ＞ 原始实验/同行评审论文 ＞ 政府技术综述 ＞ 咨询机构可复算模型 ＞ 企业营销。不同证据性质不可直接取平均。

可追加的独立问题：Starship不同任务构型实际发射服务价格何时公开且可交易、未来长期报价是否涉及批量合同、超大型可展开散热器的质量单位面积、在轨算力设备失效率与可维护性。目前这些均保持 `UNKNOWN` 或 `SCENARIO`。
## 2026-11-14 视频核查新增证据
| ID | 公开来源 | 对应可验证主张 | 级别与限制 |
|---|---|---|---|
| S08 | [SpaceX Flight 15官方任务页](https://www.spacex.com/launches/starship-flight-15) | 目标26颗V3及两级塔捕计划 | 一手**计划**，不是最终回收结果 |
| S09 | [Space.com 2026-11-14星舰15实时报道](https://www.space.com/news/live/spacex-starship-flight-15-live-updates-nov-14-2026-starship-first-double-landing-attempt) | 26颗部署、B22中止、SpaceX解说GNC故障类别 | 多次直播更新；随时间变化，媒体转述须标记 |
| S10 | [AP第15飞报道](https://apnews.com/article/f9452dd86770dda36828a35bb27d65ee) | 入轨/部署、B22在墨西哥湾损失 | 独立新闻，不能证明精确FTS机制 |
| S11 | [Reuters FAA全国停飞报道](https://www.reuters.com/world/us/faa-issues-national-ground-stop-due-extraordinary-circumstance-reasons-safety-2026-11-13/) | 航管通讯故障与全国停飞 | 不能证明对B22塔捕产生影响 |
| S12 | [SpaceX SEC 2026年招股披露](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm) | V3预期100t、未来200t、60颗V3预期容量、轨道AI算力战略 | 公司披露中的**前瞻性估计**，不是型号现役认证 |
| S13 | [SpaceX SEC 2026年三季度报告](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm) | Starship研发/试验成本按季度披露 | 未有第15飞单次总成本审计 |
| S14 | [Ars Technica 2026年9月V3报道](https://arstechnica.com/space/2026/09/starships-first-orbital-launch-gives-lift-to-spacexs-next-gen-starlinks/) | V3约2吨/颗 | 公开媒体报道，不是本次官方运单 |
| H03 | 用户提供的2026-11-14未来学研究局视频转写，本地私有MD（Ubuntu MCP只读） | $130M/发、$20–30M/发、$40–85/kg及FAA相关猜测等**作者观点** | 未提供原始财务模型，不视为证实数字；公开仓库不复制私人转写全文 |

上述核查分析与证据边界详见 [FLIGHT15_COST_FACTCHECK_20261114.md](FLIGHT15_COST_FACTCHECK_20261114.md)。

## R3轨道维护与法规新增证据（2026-11-14）

| ID | 资料与日期 | 证实的范围 | 不能外推的结论 |
|---|---|---|---|
| S15 | [NASA 2026-11-05 国际空间站完成第8块iROSA安装](https://www.nasa.gov/blogs/spacestation/2026/11/05/spacewalkers-install-final-roll-out-solar-array/) | ISS电力能力约160→215kW，升级工作18次EVA | 无人自由飞行算力站必须用同样数量EVA或同样人力成本 |
| S16 | [NASA 2026 小型航天器电源技术目录](https://www.nasa.gov/smallsat-institute/sst-soa/power-subsystems/) | 100W/kg的ROSA公开产品表；NASA观察历史任务比功率约30W/kg聚集 | 2.5MW阵列已通过产品化、轨道部署或成本认证 |
| S17 | [NASA 2026 航天器电子设备目录](https://www.nasa.gov/smallsat-institute/sst-soa/small-spacecraft-avionics/) | 辐射容忍、纠错、冗余、ECC等技术需求与部分产品轨道履历 | NVIDIA H200阵列在轨故障率/采购价 |
| S18 | [NASA 2026 发射、部署与轨道转运](https://www.nasa.gov/smallsat-institute/sst-soa/integration-launch-and-deployment/) | 拼车/专属发射目的轨道、体积、适配器与时间差别 | 星舰100吨/发到任意指定轨道的真实商业合同 |
| S19 | [美国联邦公报2024-08-09 FCC离轨规则](https://www.govinfo.gov/content/pkg/FR-2024-08-09/html/2024-17093.htm) | 对适用的低轨非受控重入目标，**任务结束后**5年内完成处置 | 所有低轨设施5年强制结束经营 |
| S20 | [NASA GAO 2026-04-28 space-based data center报告](https://www.gao.gov/products/gao-26-109012) | 能源、热、辐射、链路和在轨服务风险 | 设备制造/维护已可用成交价 |
| S21 | [SpaceX Starship官方设计说明](https://new.spacex.com/vehicles/starship) | 可回收构型100+t为设计目标 | 2026年已经能出售$25M/100t到550km发射服务 |

**数据质量警示**：基于NASA的100W/kg产品指标，R3推导的1MW约2.5MW额定光伏并未获NASA、供应商对完整阵列的工程认证；R3所有发射合同、电子年故障率、维修机器人价格和成本数字仍是`scenario`。见 [R3报告](R3_ORBIT_SERVICE_DISPATCH_20261114.md)。
