# CASE-ESP-001｜西班牙帝国第一轮证据审查（M0）

**权威Issue**：[AI_book #32](https://github.com/fweiger/AI_book/issues/32) · **上位**：[TOPIC-010 #30](https://github.com/fweiger/AI_book/issues/30) · **状态**：第一轮史料/事件与数值证据准入；原始马德里财政年度账本、跨国因果回归尚未取得。

## 第一轮结论（不是最终因果判决）

**“殖民美洲白银支持帝国财政，而连续战争支出快于收入”得到非常直接的经济史档案研究支持。** Marichal的《Bankruptcy of Empire》指出，1780–1800年波旁王朝提高本土及美洲税收，但1779–83英西战争、1793–95对法战争、1796–1801及1805–08对英战争逐渐推高开支，政府开始以税捐、赠款与债务融资；[1784–1807马德里国库原始手稿研究](https://ideas.repec.org/a/cup/jechis/v41y1981i02p315-339_04.html)认为殖民收入受战争威胁，传统税基缺乏足够弹性。**我们尚未取得这些原始账本，因此不能宣布财政成本收益已经逐年复算。**

## A 科技：并非所有矿业都来自同一个“低技术奴隶开采”机制
- 波托西（今玻利维亚）和萨卡特卡斯（今墨西哥）银矿，以及冶炼、燃料、**汞齐法**与秘鲁Huancavelica的汞供应构成技术与资源链。
- 反例：冶炼技术、汞供应及劳动力可得性共同决定成本；不是简单将强制劳动视为零成本。〔[Oxford Research Encyclopedia](https://academic.oup.com/edited-volume/61800/chapter-abstract/546349390)〕

## B 人口劳动—银矿—全球贸易
- 波托西1572—1576矿业改革后的mita强制轮役动员规模，研究估计每年约**12,000—14,000名成年原住民男性**。这是劳动力调配流量，不是当地奴役人口总存量。〔[IRSH同行评审史料研究](https://www.cambridge.org/core/journals/international-review-of-social-history/article/women-in-the-silver-mines-of-potosi-rethinking-the-history-of-informality-and-precarity-sixteenth-to-eighteenth-centuries/DDD6EAB29255C2C34F189A6A83129200)〕
- 美洲白银与全球贸易的货币需求有关，但不等于“北美银矿由非洲奴隶普遍开采”；墨西哥与安第斯的劳动制度不同。

## C 军事与外交：存在英国压力，但不是英国单方操纵整个欧洲
- 乌得勒支和约改变商业权利；1780—1808战争中西班牙与英国/法国结盟关系发生反复变化。
- **最强反例**：西班牙对英作战的1779—1783年，实际上与法国及北美反英独立力量形成合作；不是所有西班牙战争都由英国单方面挑起。

## D 财政债务：直接验证假说的候选案例
- [Marichal](https://www.cambridge.org/core/books/abs/bankruptcy-of-empire/imperial-wars-and-loans-from-new-spain-17801800/A949A388DF0ED83E906CA22EBE8730A9)总结：加税增长，但战争支出快于税收，进而借款。
- [Barbier与Klein](https://ideas.repec.org/a/cup/jechis/v41y1981i02p315-339_04.html)还发现：殖民地来源税收波动对马德里中央国库尤其危险。**暂不将其学术判断伪装为本项目重算过的财务序列**。

## E 本土产业和殖民退出
- 需要另查西班牙本土制造/贸易品出口、货币供应、实际汇率，以及1808后帝国各地独立过程。财政压力不必是全部退出的唯一原因。

## 假说与反证
- **H1（财政过度延伸）**：军费和债息增长率高于王室可用财税流量；识别变量 `military_spend/treasury_revenue`、`colonial_treasury_remittances`、`debt_service/revenue`；优先原始来源Madrid Treasury 1784–1807。
- **H2（资源与治理危机）**：当地劳动强制、矿产资源质量、货币与跨洋交通冲击，加上1808拿破仑入侵，造成财政和殖民政治同时失稳。
- **证伪**：若军费增速未超税收、偿债成本未恶化但殖民政治仍崩溃，军事财政机制不能单独解释。

## 数据与审查状态
[12条事件](events_m0.csv)、[10项来源](source_registry_m0.csv)、[2个候选指标（其中一项有发表区间）](metrics_m0.csv)。格式与年份可按CSV检查；原始王室财政年度表 `NOT_ACQUIRED`，因果识别 `NOT_RUN`。

**下一项唯一任务：** 逐表取得Marichal和Barbier–Klein对1780—1807的收入、军费、殖民汇款与贷款明细，统一银比索/里亚尔/法定币、国库本土与新西班牙会计口径后再做趋势与支出收入比例。
