# 2026-11-14 · TOPIC-010 M3-A — 从四国殖民财政源头返回英国工业化成因

## 研究起点与任务保持
- 规范Issue [#30](https://github.com/fweiger/AI_book/issues/30)，现有Draft PR [#31](https://github.com/fweiger/AI_book/pull/31)；遵循Task Center V1，不新开总课题。
- 用户纠正研究偏移：放弃无界新增四国账本，直接回答葡、西、荷、法、英中为何英国率先持续机械化和生产率增长。
- 本轮目标为P1贸易/市场、P3技术商业化、P4七假说竞争性证据的**第一个有数值样本**，不是所有财政史或七假说的最终裁决。

## 实际读到的材料及等级
1. Broadberry–Gupta (2005) LSE免费作者稿 [PDF](https://www.lse.ac.uk/Economic-History/Assets/Documents/Research/GEHN/GEHNConferences/conf6/Conf6-BroadberryGupta.pdf)印刷pp32–35（PDF页0-index31–34）直接用web截图目视验证**表1原棉消费、表2不变官方价出口、表3当期价英印进出口、表4印度本地份额估计、表5英荷公司印度纺织品运输**；**不是原历史海关账**。该作者稿与Broadberry–Gupta(2009) *Economic History Review*同源研究，不能双重计数为独立复核。
2. UK Parliament [1721/1736纺织法历史表](https://www.parliament.uk/about/living-heritage/transformingsociety/tradeindustry/industrycommunity/keydates/)：机构网页已读，不代表法律执行效果。
3. Historic England [Cromford水力棉纺厂遗产记录](https://historicengland.org.uk/listing/the-list/list-entry/1488604)及Derby1721丝织意大利设计：官方遗产研究网页，不代表同年完整机械采用数。
4. Allen 2009 Jenny France/India/Britain投资利润模型 [期刊页面](https://doi.org/10.1017/S0022050709001326)；与Crafts2011 [批评性评述](https://doi.org/10.1017/S1361491610000201)：期刊摘要/公开经济史学术文献，作者模型38%/2.5%/-5.2%不能称历史真实企业净收益。
5. Raman2022 [纱线质量比较](https://doi.org/10.1111/ehr.13143)期刊网页摘要指出1746–1820英印度纺织物质量趋同；未取得或运行附录XLSX，不能称本项目验证了TPI结果。
6. Acemoglu–Johnson2024 MIT [PDF](https://shapingwork.mit.edu/wp-content/uploads/2024/04/Acemoglu_Johnson_April-2024.pdf)表A3引用Mitchell1984的1815/1830美国原棉在英国进口比例；HTML文本可读，截图缓存失败，此两条来源仅 `PUBLISHED_PDF_TEXT_EXTRACTED`，并非海关原账/视觉复核。

## 形成的结构化数据及真实测试
- `data/cotton_uk_consumption_exports_periods_m3a.csv` 16个历史阶段，分原棉年均数量（百万磅）与1697官方价格出口（千英镑），明确不可混入现价；
- `data/cotton_indian_piece_goods_eic_voc_m3a.csv` 8个阶段的印花棉布/EIC和VOC特定港口线路（pieces/year），VOC没有资料的两个阶段按缺失而非0；
- `data/cotton_britain_india_piece_trade_current_prices_m3a.csv` 8个当期价格时期，包括超出主研究1850终点的1854–56参照行显式打标；
- `data/uk_industrialization_h1_h7_discrimination_m3a.csv` 七假说逐一列支持材料、反例、下次区分性数据，非七个独立统计验证。
- 数据QA：以上分别16/8/8/7行、quote-aware CSV rectangular，唯一H1–H7、原棉时间窗口单调不交叠、2005表格原值、印度早期VOC两期缺失、1834–36转口额大于同期间进口的统计风险捕获；原棉1750→1800倍率21.2857，1697官方价出口倍率97.1163；**只算术PASS，历史因果NOT_RUN**。
- 原报告中误写`1930年代以前`已修正为`19世纪早期1831—35`，提交GitHub readback通过。

## 本轮改变的认识
- 此前的财政治理细节并未量化工业化结果变量。本轮直接见证英国原棉消费增长、制造出口增长；贸易输入与机械化阶段转换不再只是时间线预设。
- 印度是前期棉纺技术/质量与进口替代的竞争者，不是只作为英国工业原棉供应地；英国对印度**本土**市场的渗透滞后于英国在其他世界市场的出口扩张。
- 1771 Cromford是水力，不是已被证明的英国廉价煤直接驱动全部机械创新；荷兰高工资金融能力、法国科学能力、西葡早期殖民都是检验H1-H7充分性/必要性的反例。
- 1815/1830美国棉花来源与奴役劳动生产环境要求将19世纪规模化原料供给、技术起源年代以及受奴役者社会成本分开。
- Allen工资价格机制与Mokyr有用知识机制不可在尚无共同工业采用模型时择一判胜；Crafts的批评支持继续保持并行竞争假说。

## 仍缺材料
- 原始英国海关交易底账、印度殖民地织品货物流向全量表；Raman论文附录XLSX；英荷英法同一历史行业工资/机器价格/厂数/劳动生产率；葡西制造业投入与真实汇率；原料实物到工厂的匹配记录。
- 没有五国工业生产率同口径对照面板；殖民帝国长期净回报不在本轮检验；H1–H7因果裁决NOT_RUN；未完成独立史学评论审稿；不得把来源表的多版本视为独立因果复现。

## 唯一下一步
在**父Issue #30**建立英荷英法 H6/H7 区分性数据：工资相对于纺纱机器造价、维持年限、利率及水能/煤价的假设敏感性，匹配各国机械采用和工厂规模；再纳入葡西相对汇率/制造业竞争作外部反例。四个子案仅在有判别性的工业数据时重启。
