# CASE-FRA-001｜M2 1788财政原刊谱系与冲突值审计（2026-11-14）

**权威任务：** https://github.com/fweiger/AI_book/issues/35  
**原有Draft PR：** https://github.com/fweiger/AI_book/pull/39  
**阶段：** M2，刊本目录审查与冲突值整数算术PASS；**原印刷表格逐格视觉审查未完成，1788王室国库实际现金和跨洋汇票最终清算NOT_ACQUIRED，因果NOT_RUN。**

## 一、本轮新增的实质性事实：1788年会计年度存在多种不同物理刊本

[2014年Morand/Le Floc'h拍卖目录Lot 28](https://www.dpetitot.fr/Ventes_passees/Pages/2014-11-13_files/Morand_13112014_web.pdf)具体描述同一本装订卷中的两册**Port-au-Prince（Mozard）原刊**：1788年出版的一册覆盖1785-11-10—1788-01-01；1789年出版的一册覆盖1788-01-01—1788-12-31。后者在**拍卖所见的具体存世藏本**中存有10张应为11张的折叠表，IV号表缺失。这**不代表整批1789年印本都缺IV号表**。

1867年Cilleclerc《Bibliotheca Americana》[no.105](https://upload.wikimedia.org/wikipedia/commons/9/96/University_of_Michigan_%28IA_aez2079.0001.001.umich.edu%29.pdf)同样列出1788—1789当地印本，并记载1790年Vincent-René de Proisy编写的**1789全年账册**，以及针对Marbois账目的1790年相关议会/出版物。我们核对的是历史书目描述，**尚未阅读这些争议小册子的正文，因此不能认定当时已证明错账或欺诈**。

[Columbia Law Library](https://pegasus.law.columbia.edu/record/127364)及[Manioc](https://www.manioc.org/patrimon/SCH13010)确认1790年**巴黎皇家印刷所**出版的1788全年报告。1798年Laborie英文财政附录又是另一份出版物，但可能复制Marbois行政底稿，并非统计独立样本。

研究需要严格区分**书籍出版年**与**财务覆盖年**：一个1790年书目里可能同时有1785—1788、1788全年和1789全年三套账。错误合并可能制造虚假的收入趋势。

## 二、此前数字异常仍需按印刷版本逐项核对

| ID | 指标 | 两组历史数字 | 差额 | 本轮状态 |
|---|---|---|---|---|
| FRA-VAR001 | 海军金库期初款 | 933,160 l5s5d / 935,160 l5s5d | 2,000里弗尔 | 数字原页未核实 |
| FRA-VAR002 | 海军金库支出 | 9,448,488 l7s8d / 9,448,188 l4s0d | 300里弗尔3苏8德尼 | 数字原页未核实 |
| FRA-VAR003 | 海军金库期末小计 | 分项算出1,390,162 l9s4d / 索引小计1,390,162 l16s4d | 7苏 | 数字原页未核实 |
| FRA-VAR004 | 1788出口货值 | 旧转录约1.80亿 / Ardouin约1.93亿 | 约1,300万 | 定义未统一 |
| FRA-VAR005 | 四金库列支与账表平衡总额 | 11,933,477 l17s6d / 13,444,854 l4s5d | 1,511,376 l6s11d | 大概率属于账表结余项区别，仍需原表确认 |

前三项差额和第五项差额按**1livre=20sous=240deniers**整数重新计算PASS。A与B只是不同转录/出版物的数据；不能单凭某个总表算术自洽宣称某版印错。第四项均为近似值，可能采用不同估值、交易覆盖或货币；不允许将差额认作1788年丢失的财政收入。

证据入库：[edition_provenance_m2.csv](edition_provenance_m2.csv)（8条刊本/后期史著）、[printing_discrepancy_register_m2.csv](printing_discrepancy_register_m2.csv)（5条冲突）。以前的CSV数值保持原样，状态记为`ORIGINAL_PRINT_IMAGE_NOT_VERIFIED`。

## 三、下一财政年度具有独立原始账本线索，但不能立刻计算同比

[Ulrick Duvivier, *Bibliographie générale et méthodique d’Haïti*, tome II, p.259](https://ufdcimages.uflib.ufl.edu/UF/00/09/51/43/00002/Volume2.pdf)登记了**Proisy 1790年Port-au-Prince刊本**，覆盖圣多明各**1789-01-01—1789-12-31**，并附多张金库折叠表。它提供一个可实施的1788/1789比较对象，但**本轮没有读取1789全年账目任何金额**。比较前需同口径核对：金库名称、期初/期末余额、旧欠收回、普通/非常税项、币种和管理责任人。

## 四、优先核验的唯一下一项工作

取得1789年**Port-au-Prince印刷的1788全年原始折叠N.III和N.XI账表高清扫描**，逐格与1790年巴黎重刊、1798年Laborie附录核对上述2,000l、300l3s8d及7s异常。若需要馆藏调阅，只请求指定页/表并保存扫描页码与页像文件ID，不能再将书目登记当成原页审读。

之后才能从1789年Proisy独立年度账本提取同口径时间序列。1788年法国本土`AN G¹46*`殖民税日记账仍待原件，**不计算巴黎国库净收入或殖民帝国投资回报率**。
