# H10｜为什么“固定同一发布者”仍不等于完整PIT一致预期面板：2024发布源覆盖审计（2026-11-14）

## 完整发行日分母
冻结2024年全部12次BLS CPI实际公告日，逐月检查同一发布者 Calculated Risk 的固定标题/固定URL模式（YYYY/MM/cpi-preview.html）。只有**4月和12月**确实找到此具体标题的发布前页面；其它10个精确slug不存在，**并不代表当月该发布者没有其它“明日CPI”文章**。因此不能将其视为同源全年完整预测面板，也不能把找不到的10个月填零或借用无时点的财经日历forecast。见[12行逐月覆盖表](../data/h10_2024_calculatedrisk_cpi_preview_source_coverage.csv)。

## 同一发布者内部仍要分“机构预测”与“市场共识”

**2024-04-10公布2024年3月CPI：**
- [4月9日15:50美东时间 CPI Preview](https://www.calculatedriskblog.com/2024/04/cpi-preview.html)直接引用BofA机构预测 headline约0.3%/core约0.2%，并引Goldman core0.27%/headline0.29%，其中Goldman提到core consensus 0.3%。**这些银行单家预期不能代表统一的市场中位数**。
- 同一发布者[4月9日19:43“Wednesday: CPI, FOMC Minutes”预告](https://www.calculatedriskblog.com/search?by-date=false&max-results=10&start=1710&updated-max=2024-04-11T10%3A44%3A00-04%3A00)引用市场共识 headline **0.4%**、core **0.3%**。
- [BLS 2024-04-10首次新闻稿](https://www.bls.gov/news.release/archives/cpi_04102024.htm)实际headline0.4%、core0.4%，由市场共识计算是headline surprise **0.0pp**、core **+0.1pp**；若错误地将银行单方预测当共识则得到不同值。当天UST2Y日度+23bp、10Y+19bp，但**14:00还有FOMC会议纪要**，绝不能全部归因于08:30 CPI。

**2024-12-11公布11月CPI：**
- [12月10日15:00美东时间 CPI Preview](https://www.calculatedriskblog.com/2024/12/cpi-preview.html)明确市场headline/core预期均0.3%，[BLS 12月11日首次新闻稿](https://www.bls.gov/news.release/archives/cpi_12112024.htm)也都是0.3%。两者惊讶为0.0pp；2Y收益率该日0bp、10Y+4bp，不能纳入非零surprise方向胜率。
- 这一回合的有效非零核心CPI惊讶事件只有**1次**，**不可计算年度策略命中率/显著性**。该资料只用于进一步规范预测来源的分级/入组规则。

## 机制链含义
同一个财经网站/同一天，**BofA、Goldman、市场共识**可以是三种不同预测。要做真正CPI surprise→Fed预期→利率方向，至少需要：BLS首次发布时点、准确的SA headline/core MoM、预测样本类型、报道具体发表时间/是否事后修改、新闻发布后几分钟的期货/债券变动及同日竞争新闻。缺失任何字段就用NA，不把历史网页做成含未来信息的漂亮回测。

本次是来源质量审计，不更改H10 UNTESTED，且不因市场同日+23bp去认定因果。下一任务应从同一专业调查供应商历史发行快照建立**覆盖2023—2026全体发布日的原始共识数据库**，不是继续依赖单一标题slug。
