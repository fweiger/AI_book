# CASE-ESP-001 · M2r — Barlovento双口径财政汇款、哈瓦那收款审计与学术表4分母异常

**日期：** 2026-11-14  
**唯一规范 Issue：** https://github.com/fweiger/AI_book/issues/32  
**研究分支与 Draft PR：** `topic-010/case-esp-001-spain-20261114` / https://github.com/fweiger/AI_book/pull/36  
**实验状态：** 已发表公开数据的逐行抄录与算术检验；原始AGI/AGNM历史手稿未取得；正式历史因果检验 NOT_RUN。

## 1. 新增、可公开复核的学术原表

Serrano, José M. (2020), [La Habana, riqueza local, plata mexicana y financiación militar, 1765–1788](https://doi.org/10.18232/alhe.1005), `América Latina en la Historia Económica`, 27(1), e1005; [SciELO出版社HTML版](https://www.scielo.org.mx/scielo.php?pid=S1405-22532020000100002&script=sci_arttext)，[出版商页面](https://alhe.mora.edu.mx/index.php/ALHE/article/view/e1005)。该文章为 CC BY-NC 4.0 开放获取；仅保存数值化、归属注明的表格与审计代码，不复制整份PDF。

- [表1双版本逐年重建24行CSV](barlovento_dual_sender_reconstructions_m2r.csv)：1765–1788；作者使用AGI会计核查与历史Marichal–Souto–Klein序列对比；货币为8雷亚尔银比索 `pesos de a ocho reales`。
- [表4哈瓦那入账23行CSV](havana_reception_account_table4_m2r.csv)：1766–1788；是以哈瓦那地方财政归口为基础的已发表重建，并非直接从墨西哥发送账与西班牙国库利润推导；两份CSV不是独立档案影像采集。
- [stdlib复算验证脚本](validate_situados_m2r.py)：核对年度连续、双版本累计金额、逐年差额、公布百分比和发表平均数异常。

### 表1：两个历史重建的体量差异

|字段|论文刊载金额与复算|单位/样本|
|---|---:|---|
|Serrano|84,453,062|银比索，1765–1788累计24年|
|Marichal–Souto–Klein|103,172,038|同口径年份的作者对照版本|
|两个序列差额|18,718,976|MSK减Serrano，18.1435%之于MSK|
|战争1779–1783 Serrano|33,799,507|同五年累计；对应全部Serrano 40.02%|
|战争1779–1783 MSK|40,493,715|同五年累计；对应全部MSK 39.25%|

Serrano论文明确认为经典账目存在同一转账重复、内部现金调账误列为财政转移等风险；但其改建版本不是原始唯一真实值，**本项目无独立原件复核，不宣称哪套估计真实**。该差额不能自动等同“被挪用”或“腐败”金额。

### 表4：已发表年平均分母异常（本轮最强新算术发现）

|复核量|数值|
|---|---:|
|表4实列年份|1766–1788，**23行**|
|23行哈瓦那总收入之和|112,185,483 比索|
|23行收到的situados之和|74,541,779 比索|
|论文公布平均总收入|4,674,395 比索/年|
|论文公布平均situados|3,105,907 比索/年|
|按23行重新计算：年均总收入|4,877,629.695652 比索/年|
|按23行重新计算：年均situados|3,240,946.913043 比索/年|
|现象|**两项论文均值均等于23行总额÷24取整**|
|正确合计权重式situados份额|**66.44512%** = 74,541,779 /112,185,483|
|逐年百分比的简单平均|约68.74176%；论文公布69%，属于四舍五入，不应称作错误|
|以Serrano发送账1766–88对照哈瓦那收到situados|82,653,062对74,541,779，差 **8,111,283比索**|

**性质判定：**已验证的是“按论文所列23条记录，平均值使用相当于24年分母”的异常；这不是已经从编辑部确认的勘误，也不能排除存在未说明的第24年数据处理。论文指出1765因哈瓦那收款账不完整而从表4省略。论文段落中约74.5m和约8m的文字与上述收付数量级吻合。这些差异不能视为款项遗失，必须区分 *shipment dispatched* / *entered into receiving treasury* / *re-exported* / *military treasury split* 及年度时滞。

## 2. 更强机制证据：并非仅靠瓦伦西亚港的本土案例

Marichal & Matilde Souto 2012论文“[La Nueva España y el financiamiento del Imperio español en América: los situados para el Caribe en el siglo XVIII](https://carlosmarichal.colmex.mx/finanzas-coloniales/Situados%20imperio%20espanol.pdf)”在作者/协调者授权公开的学术文集PDF中（摘录文本印刷pp27–29）明确讨论：

1. Veracruz→La Habana→其他加勒比驻军的**两段式财政支付链**，并非墨西哥到马德里一条总账；
2. 银币运输可分多船、发行金库现金凑不齐则分批发送，运输船不足则长期延后、积存地点可能在Jalapa；银行纸面及名义财政授权不能代替支付时间戳；
3. 该文转引1758年Santo Domingo驻军因为逾10个月未发薪而叛乱，以及下令增拨25,000比索与在后续拨款偿还欠薪，脚注标有AGNM `Reales Cédulas Originales vol.78 exps.104/109` 和 `Historia vol.570 f.39`。**这里是作者转引的历史档案编号，不是本轮直接阅览的1758原档；其他研究可能把该驻军抗议写作1757，须先澄清年份而不作确定年代因果样本。**

这个更接近西班牙殖民财政 **situado拨款→跨岛运输→驻军收款→薪饷结欠→抗议** 的历史机制；瓦伦西亚港 `Banco vales reales→地方Junta→港口工人` 仍是独立的西班牙本土项目，不应跨主体硬接成同一条现款链。

2012来源PDF可读文本，但网页截图尝试失败 `CACHE_MISS`；2020来源对照使用SciELO原始公开HTML并以大学PDF文字查询交叉，原PDF截图访问亦失败 `CACHE_MISS`。不得把新数据标记为手稿影像直读。

## 3. 原研究最需要补上的双向账目核对

**发送端：** 墨西哥主财政库（柜台记账/内部转账）→Veracruz港（实际装船单）→La Habana **陆军/陆上国库**和**独立海军财政账户**；**接收端：** 港口实收→当地军事、船坞、堡垒、公共工资支出→对Puerto Rico、Santo Domingo、Florida等第三地转拨。

因此：
- 每笔跨库转账须有`sending_treasury / intermediate_treasury / receiving_treasury / year_dispatched / year_received / vales_or_silver / face_amount / actual_cash_amount / transfer_status / reexport_flag`。
- 哈瓦那收到的74.542m之中，论文报告约26.4m再转拨其他加勒比地区；该项是**文献汇总而非本轮逐笔核算**，任何“哈瓦那净留用”估算须另做去重并核对海军账。
- 不能拿1765–88的MSK全窗口与1766–88哈瓦那值直接相减；本报告只做**重叠23年**，显示约8.111m不同主体报告额差异，仍可能包括在途、再归口、双账户和会计调整。

## 4. 学术与政治经济学结论边界

- **PASS：** 论文出版社HTML表1、表4可用，24及23行的结构与逐行数值、总和、公布比率可以复算；发表均值分母恰好为24而表4只有23年；Serrano引用AGI具体类别与作者源差异观点可追查。
- **LITERATURE_REPORTED_ONLY：** 银币航运延迟/发薪叛乱具体史例、AGI/AGNM档案号；被报道的港口/军队欠付不等于实物账已取得。
- **NOT_ACQUIRED：** 原始AGI哈瓦那现金收支手稿、AGNM1757/1758实际王室令和驻军欠薪簿、1797瓦伦西亚港工资账、1994原论文原始表；也未取得UKDS授权数据库。
- **NOT_RUN：** 任何正式跨地区账簿因果识别、军事冲突与债务挤出回归、利润/工业衰落因果分析。
- **唯一下一研究动作：** 先追踪2012文集所引AGNM `Reales Cédulas Originales vol.78 exps.104,109` 与 `Historia vol.570 f.39` 的数字馆藏/年份，核对1757/1758军饷抗议的真实日期、金额和加拨25,000比索的王室命令；再以**付款实际签收**而非财政预算/名义拨款推断财政网络中的流动性瓶颈。瓦伦西亚原账册申请保持独立阻断。

## 5. M2r增量：圣多明各1757/1758驻军欠薪年代冲突与原档双线索

新增研究原文：Amadeo Julián (2017), “Comercio colonial, circulación monetaria y el Situado en Santo Domingo en el siglo XVIII”, `Clío` (Academia Dominicana de la Historia), año86, núm.194, 印刷pp39–41、73–74，[学会官网PDF](https://academiadominicanahistoria.org.do/wp-content/uploads/2018/04/clio194.pdf)。期刊PDF可检索正文全文已读，截图返回CACHE_MISS，**不是原档影像复核**。

- 本文将驻军抗议记为**1757年**；报告约150–180名驻军、部分1754–1757年的薪资积欠、通过谈判先付三个月、随后补足要求；印刷p41脚注29与p74史料清单指向 **AGI, Santo Domingo, 1088 / 1092**。该稿还指出1761年墨西哥金库对圣多明各有**20万比索历史欠拨**、提出年偿1万的表述，须用原始账本核对，**不能视为实际每年偿付**。
- Marichal & Souto (2012) 印刷p28记作**1758年**、大于10个月未领饷、王室决定situado增加25,000比索，注引 **AGNM, Reales Cédulas Originales vol.78 exps.104/109, Historia vol.570 f.39**。两文可能描述同一事件的骚动年/法令年/欠薪年度差异，但**尚无原档确认**。
- 存为 [1757/1758冲突双来源登记](santo_domingo_military_pay_arrears_1757_1758_conflict_m2r.csv)。它是一个有明确馆藏号的、比本土瓦伦西亚港更贴近殖民财政网络的候选机制案例，不新增国家/任务Issue。
- 新的第一优先行动是**查询AGI Santo Domingo 1088/1092的1757原卷与AGNM vol78 exps104/109的1758王室令真实文书日期**。先解决事件年，再试图把实际拨款、接收、发薪与抗议归为同一财政传导链，不能将同一事件重复纳入统计样本。
