# H10｜两层历史CPI预期来源：10个真正公布前样本 vs 46个事后日历（2026-11-14）

## 首要结论
**不能把历史财经日历的“Forecast”列不加时间核验地当作PIT市场共识**。本轮逐个读取2023—2026真实46次CPI发布日的**前一天网址**对应历史日历，页面能看见公布后填写的“Actual”，因此其URL日期不证明forecast版本在当时已存在。46天中headline和core各**28天**同时有可识别actual与forecast，其他日期有部分空缺；历史日历本身属于`RETROSPECTIVE_PAGE_UPDATED_AFTER_RELEASE_NOT_PIT`，仅为探索候选。

然后单独找到**10次有可证实公布前日期的专业预测来源**，分别对接BLS首次发布headline/core CPI月环比和Treasury 2Y/10Y当天有符号bp，制作[逐条10行PIT来源表](../data/h10_cpi_pre_release_dated_forecasts_10events_2023_2026.csv)。来源类型分为媒体引用的市场共识、明确机构预期和MNI专业样本中位数，**它们不是一份同口径专业问卷的随机样本**；MNI、MUFG、Reuters、Continuum等同日多来源不重复算同一次发行的独立样本。

## 一、公布前来源的10次真实事件

| 公布日 | 事前 headline/core 月环比预测% | BLS 首发 headline/core % | 2Y当天bp | 数据前瞻源 |
|---|---|---|---:|---|
| 2023-11-14 | 0.1/0.3 | 0.0/0.2 | **-22** | [InvestingLive 2023-11-14 01:27 GMT](https://investinglive.com/centralbank/us-cpi-will-be-eyed-ahead-of-the-december12-13-fomc-meeting-20231114/) |
| 2024-02-13 | 0.2/0.3 | 0.3/0.4 | **+18** | [Reuters 2024-02-12前瞻](https://ca.finance.yahoo.com/news/us-inflation-looms-large-asia-053650734.html) |
| 2024-05-15 | headline NA / core0.3 | headline0.3 / core0.3 | -8 | [Reuters 2024-05-13核心通胀共识](https://ca.finance.yahoo.com/news/morning-bid-us-inflation-every-050331355.html)；此来源对headline只给同比，**不猜月环比** |
| 2024-06-12 | 0.1/0.3 | 0.0/0.2 | **-6** | [InvestingLive 2024-06-11 18:05 GMT](https://investinglive.com/news/preview-eyes-will-be-on-every-detail-of-the-may-cpi-report-20240611/) |
| 2024-07-11 | 0.1/0.2 | -0.1/0.1 | **-12** | [Reuters 2024-07-10美元/通胀前瞻](https://ca.finance.yahoo.com/news/dollar-firm-powell-caution-kiwi-010519538.html) |
| 2024-09-11 | 0.2/0.2 | 0.2/0.3 | **+3** | [MNI 2024-09-10专业预期中位数](https://media.marketnews.com/USCPI_Prev_Sep2024_66514cfe2d.pdf) |
| 2025-03-12 | 0.3/0.3 | 0.2/0.2 | **+7** | [Calculated Risk 2025-03-11 14:51 EDT, 引专业共识](https://www.calculatedriskblog.com/2025/03/cpi-preview.html) |
| 2026-03-11 | 0.3/0.2 | 0.3/0.2 | +7 | [Continuum 2026-03-10 12:15 UTC 单机构预测](https://continuumeconomics.com/a/5d88223a/preview-due-march-11-us-february-cpi-a-moderate-gain-but-inflation-not-yet-defeated) |
| 2026-06-10 | 0.5/0.3 | 0.5/0.2 | **0** | [Continuum 2026-06-09 13:39 UTC 单机构预测](https://continuumeconomics.com/a/da75be83/preview-due-june-10-us-may-cpi-energy-and-air-fares-to-lead) |
| 2026-11-10 | 0.3/0.2 | 0.4/0.3 | **+17** | [FXStreet 2026-11-09 22:31 UTC 市场前瞻](https://www.fxstreet.com/analysis/us-cpi-preview-moderation-on-the-horizon-but-underlying-pressures-linger-202611092231) |

各次实际CPI全部按对应日期的**BLS原始首发公报**核对，而不是后来的CUSR季调指数版本；Treasury全天日差来自已取得[2023—26官方967日](../reports/2026-11-14_h10_cpi_release_ust_46event_historical_robustness.md)，因此与实际CPI公布后的5分钟反应并不完全相同。

## 二、初次样本的方向验证（严格按缺失及发布口径）

| 实验 | 有非零惊讶的事件 | 2Y有符号变动非零 | 方向一致 | 双侧精确二项p |
|---|---:|---:|---:|---:|
| **核心CPI，全部10个有日期前瞻** | 8 | 7 | **6/7** | **0.125** |
| 核心CPI，剔2026-11-10 | 7 | 6 | **5/6** | 0.218750 |
| 整体CPI | 6 | 6 | **5/6** | 0.218750 |
| 核心CPI，排除单机构预期 | 7 | 7 | **6/7** | 0.125 |

核心组有1天**核心CPI意外不为零但2Y收益率不变**（2026-06-10），因此不应把“同方向6/7”误写成“6/8”。10年期收益率的核心组为**5/7**，其双侧精确二项p约**0.4531**，同样不足形成可靠的方向规则。

**强反例 2025-03-12**：专业前瞻预计headline/core CPI各+0.3%，BLS首次实值各+0.2%，两项均**低于预期0.1pp**，但官方Treasury 2Y当日**+7bp**、10Y**+4bp**，与“通胀低于预期→收益率当天必跌”相反。即使源时间排序正确，也可能受其他消息、利率期限溢价和仓位影响。**2024-06-12当天还有FOMC政策会议公布**，也不可以拿当日日度收益率直接视作纯CPI冲击。

## 三、为什么之前28个历史日历“预测值”不能进入同一实验

[46次历史日历逐日标注的CSV](../data/h10_cpi_release_ust_46event_vendor_archive_not_pit.csv)：46个网页均有历史日期的URL，但内容后来填入实际值；headline/core各28个同时有actual+forecast，**实际预测的原始发布时间未知**。尤其：
- **2026-11-10**：事前FXStreet核心CPI SA MoM共识`0.2%`，但历史日历核心CPI forecast回显`0.3%`。若直接拿后者当预期，就会将真实`+0.1pp`核心CPI surprise错误算成`0.0pp`。
- **2026-03-11**：Continuum在前一天给核心 CPI `0.2%`的机构预测，历史日历显示`0.3%`；说明数据源之间的**机构/共识或后验版本差异**，不是可证明的当时谁知道什么。
- **2026-06-10**：Continuum核心 CPI `0.3%`，历史日历显示`0.35%`。由于一位小数的最初发布与未舍入的供应商预测可能不同，不能仅用绝对差推断“某份预测被篡改”；必须记录原始预测类型、精度及采集时间。

因此报告同时保留两个库：A级**已确认发布时间在先的10事件**用于非常有限的探索性方向验证，B级**46个事后历史日历**仅做取证候选，不合并统计，也不能拿较好的B级相关系数骗得回测显著性。

## 四、真实可复算与结论状态
- [10事件原始预期—首次实值—官方2Y/10Y方向CSV](../data/h10_cpi_pre_release_dated_forecasts_10events_2023_2026.csv)。
- [纯stdlib Python独立复算](../analysis/recompute_h10_pre_release_cpi_surprise_10_events.py)：逐行核验预测发表在数据公布之前、BLS原始公报URL、单位/减法、非零惊讶、2Y/10Y正负号、双侧精确二项概率；Ubuntu MCP以Github当前真实CSV运行**PASS**。
- **选择偏差**：能找到完整前瞻的10个事件不是从46个公布日中随机抽样，且包含不同机构的预期值。n仅7个有效有符号核心意外方向匹配，不能将6/7=85.7%包装成样本外预测胜率；p=0.125也不足以认为存在可推广统计规律。
- **因果问题未解决**：没有债券08:29与08:35的实际价格、其他同日数据与Fed讲话控制；即使9次方向全部一致，也不是严格CPI引起收益率变动的证据。正式H10`CPI Surprise→Fed路径预期→实际FOMC→公司再融资`仍**UNTESTED**，无新因果C-ID。

## 下一步
把上述时间戳标准应用于2023—26更多银行/Reuters/CME真正提前发布的通胀一致预期；同时找合法的美债2Y期货/短端利率分钟行情及同期Fed futures，避免在只知道“当天”时做单一CPI解释。基于真实整期事件和事前决策时点冻结，再做样本外统计与宏观状态分层。
