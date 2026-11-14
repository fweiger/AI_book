# CASE-PRT-001｜M3 1743年宗主教座堂债务转换、黄金税抵押金库与殖民收入信用机制的三本账

> 2026-11-14；唯一权威业务Issue：[AI_book #34](https://github.com/fweiger/AI_book/issues/34)；原有[Draft PR #38](https://github.com/fweiger/AI_book/pull/38)。  
> 状态：**1743_INTEREST_RATE_CONVERSION_HISTORICALLY_DOCUMENTED / SPECIFIC_COLONIAL_EARMARKED_COFFERS_8_REPRODUCED / CASH_NEW_BORROWING_NOT_IDENTIFIED / ASCM_NOT_RUN**。本轮没有获取1743年皇家法令原件或1760年1,519笔逐笔券，所有前人档案读数应保留其真实引用链。

## 1. 核心纠偏：1743年约5,000 contos债权重组≠同年的净债务发行507.943 contos

### 证据的层级与传承，严禁伪装成独立档案重审

**历史研究根节点**：João Lúcio de Azevedo，《Épocas de Portugal Económico》，第二版，Lisboa: Livraria Clássica，1947，印刷页**375**（数字典藏页码`/365/`），[葡萄牙文史籍OCR与扫描入口](https://obrasraras.fcp.pa.gov.br/publication/file/livros/epocasportugaleconomico1947/365/)。

其脚注直接定位：
- **1743-02-04王室法令**：Gomes (1883) 《Collecção de leis da dívida pública portugueza》卷I页317；本轮**法令原始版本NOT_ACQUIRED**，目前仅有Azevedo的转引。
- **1743-03-28—1745-03-25宗主教座堂（Patriarcal）司库**向`Junta dos Três Estados`用于债务转换程序的记录金额，Azevedo引用**3,455:704$000 réis**，等于**3,455.704 contos**。底层档案线索是**1752年对Conselho de Fazenda的呈报，Colecção Pombalina, códice 459, fólio 130**；**1752手稿未独立查阅**，这笔转款是重组中的机构间资金流，不能等同王室新增净借款。
- **1747年Patriarcal相关债权每年名义收益**：**250:843$880 réis =250.843880 contos**，Azevedo再引Baptista de Castro，《Mapa de Portugal》卷III页189；**收益与本金存量必须分开**。
- **1749-03-16新一轮债券转换公告**：Gomes (1883) 卷I页318，降至约4.5%；**法令原件未独立查阅**。
- Azevedo描述一批旧债从私人持有人移向宗主教座堂，累计超过约5,000 contos；由于国家仍承担降息后债务，他称其不是简单注销全债，更接近**持有人与利率重构**。

**同一历史研究链的后继论文**：
1. Costa, Freire; Miranda, Münch; Nogues-Marco, Pilar (2021) [*Early Modern Financial Development in the Iberian Peninsula*](https://archive-ouverte.unige.ch/unige:147492)，作者公开31页工作论文，PDF已实际从作者大学仓库下载（2,178,448 bytes，SHA256 `887e66a3e2665a949a8e52ca964258c51a826ad7b008704cc9628fb05505a6a7`），正文第15–16页复述**1743年6.25%旧债→5%**并提约5,000百万réis从私人转至Sé Patriarcal，直接注明其引用**Azevedo (1973: 374–375)**。**并非独立于Azevedo的二次档案核验**。
2. 同三位作者2024剑桥**正式出版版本** [第13章，DOI 10.1017/9781108770217.015](https://doi.org/10.1017/9781108770217.015)，[University of Geneva出版社许可作者公开版本](https://archive-ouverte.unige.ch/unige:176869)。本轮实际下载PDF **408,496 bytes，SHA256 `12a6ada3f00469d6da77dea77b2161e5998f775e5ffd1dcdd5e907075a911724`**，全文明示从前述文献更新而来；对累计重组约5,000百万réis的转述亦承袭Azevedo。
3. 非完全相同作者的研究：Rita Martins de Sousa有关葡萄牙国债转换与铸币操作的公开文章亦提1743年5%、1749年4.5%，并引Azevedo/Gomes；**同样属于引用链交叉复述，而不是三套相互独立的原始债券合约数据**。

**对照实际重建数据**：
[DEBT.PT A官方工作簿](https://debt.pt/pdf/DEBT_%201529-1557%20%26%201641_1800.xlsx)（SHA256 `b2024474a20442b5577ca4667067edf22ffdf71a30faad01971f5a8d13104d17`），`Debt stock!H/I/F`，本仓库已经实跑的[159年发行/存量复算](data_m2/debtpt_issuance_vs_stock_delta_1642_1800_m3.csv)：
- 1743全年`H`净新增长期`juros` **+507.943005百万 réis**；
- `I`已记录短债净发行 **−15.100000百万 réis**；
- `F_t−F_{t−1}`总存量变化 **+492.843005百万 réis**（百万réis与contos等值）；
- `H`按DEBT.PT官方说明**包含赎回、再融资等净额调整**，并非新发债券面额，更不是王室新增现金收入。因此**5,000 / 507.943**不是债务量的时间序列增长倍数，也不能做会计加总。

[可检查来源主张短表](data_m2/juro_1743_1749_debt_conversion_evidence_m3.csv)：5条标注日期、金额、文献依赖、底层档案locator、实查状态和禁用解释。

### 明确标注的算术相容性检查（不是独立历史验证）

- 若一批总额恰为**5,000 contos**的债券全部承担**5%**票息，则年息是**250 contos**。
- Azevedo转载的**1747年宗主教座堂该项年收益250.843880 contos**，如假设同一批本金票息**恰为5%**，则倒推等值名义本金 **250.843880 / 0.05 = 5,016.8776 contos**，与大约5,000 contos的历史描述量级相近。
- 反事实情景：若5,000 contos旧债**全部由6.25%变为5%，本金完全不变**，每年名义票息差额为`5000*(0.0625-0.05)=62.5 contos`。这只说明机制的**可能量级**，不是经逐债券抵押、赎回和异期现金支付后计算出的实际年度节省。Azevedo也提醒重组并未覆盖所有符合利率条件的债券。

## 2. 原始DEBT.PT B财务金库：精确定位金税抵押，但它记录的是40年偿付净变化

官方原研究项目：[DEBT.PT—Sovereign debt and private credit in Portugal](https://debt.pt/)，项目协议`PTDC/HAR-HIS/28809/2017`，本轮再次实际下载**B财政金库官方Excel，35,399 bytes**，SHA-256 `48727613d6463b990842b7098a5b5c25aeaf9235ced3bb142634b591af5b6850`。另实际下载[DEBT.PT Documentation.pdf](https://debt.pt/pdf/DOCUMENTATION.pdf)，219,152 bytes，SHA256 `7794d0d7fdfa0c8e1fbd3658ff290abd521f6b6795a9eb51c38464055c2955d7`，逐字核对变量说明。

源工作簿**第二个工作表 Long-term debt** J/K对应**1722—1761年**债券数量与偿付额的**期间净余额变动**；M/N对应**1762—1800年**。因为包含债券赎回、利率降低以及一个债券被多个金库分担偿付，J/M不一定都是整数，K/N允许负值；**不准解释为40年累计税收，也不准当成1743年单年度收益或债券发行数**。

实际提取八个有助于解释信用抵押及对照的机构，关键行如下：

| 源表行号 | 财政金库/税种标签 | 1722—1761净债务偿付变化（百万réis） | 1762—1800净债务偿付变化（百万réis） | 适用范围 |
|---:|---|---:|---:|---|
| **32** | `Intendência das Dívidas dos Armazéns (and 1% tax on gold from Brasil after 1716)` | **+50.983813** | **+18.815907** | 明确提巴西黄金1%运输税，但与军需/仓库债务项目共享同一栏目 |
| **37** | `Conselho Ultramarino`（海外事务委员会） | **+41.093489** | **+1.455778** | 海外机构多种收入，不能全部视为黄金税 |
| **34** | `Casa da Moeda`（铸币局） | **+11.580000** | **+0.064000** | 混合铸币收益与其他币种，不可全归巴西黄金 |
| **39** | `Estanco do Tabaco`（烟草专营） | **+1.342310** | 0.000000 | 殖民商品相关专营，不是黄金税 |
| 31 | `Junta dos Três Estados` | +19.270637 | −2.409656 | 国内财政对照；1947史书另提该机构参与1743转债，但此**40年净变化不能直接确认具体转款** |
| 28 | `Alfândega Grande de Lisboa`（里斯本大海关） | +0.474993 | +4.380126 | 多源贸易税而非纯帝国收入 |

完整八行及原始机构全名：[debtpt_selected_fiscal_coffers_debt_service_changes_m3.csv](data_m2/debtpt_selected_fiscal_coffers_debt_service_changes_m3.csv)。

重点结论：**巴西黄金运输1%税确实是有正式可定位财政机构抵押的公共债券偿付税源**。但“具有抵押安排”“实际收到金税”“按期给债权人付息”“为新发行国债直接提供现金”是至少四个不同命题。此表仅证明**前一项的制度安排**，不是四项全部通过；不同混合金库账户之间也不允许无条件加总为一个帝国资金规模。

## 3. 2021年17% vs 2024年24%殖民抵押比例：样本定义不得混用

- Costa/Miranda/Nogues-Marco **2021工作论文**，在**D. João V国王（1706—1750）1,519条`padrões de juro`登记样本**中报告**17%**的登记关联殖民帝国税源（1%黄金运输税、染料木、海外税收结余、烟草等）。来源第16页实际PDF文本。
- 同作者更新后的**2024正式出版剑桥章节**，采用**1760年基准**报告约**24%**的相关债券关联殖民帝国税源，且把烟草和亚洲进口关税等纳入列举。来源2024出版章第348页及作者大学存档PDF第14页。
- 这两者并非同一研究样本在两个连续日期的严格可比指标：**工作论文为1706—1750时期登记样本；出版章节为1760基准存量/某类样本，24%确切统计分母须进一步获取作者原始样本清单**。不应据此写“殖民税源抵押占比从17%上升了7个百分点”。
- **这两份研究为同一作者合作项目不同版本**，不能被计作独立学派的双重实证支持。二者仍支持殖民税源开始被指定为偿债担保来源的历史机制存在。

## 4. 三本账审计框架（禁止跨账相抵）

| 账本 | 已有可核查实证 | 仍缺少什么才能支持机制 |
|---|---|---|
| **A 黄金转移账** | 2008铸币局/2025 Appendix B.1五年汇款到葡萄牙（公共和私人）。公共汇款在本地扣除部分地方军政开支后才汇出 | 1743具体到港日、宗主国国库入账日、指定税源付款的账户 |
| **B 债券抵押/偿付账** | DEBT.PT B直接列有巴西黄金运输1%税及海外委员会偿债金库。2021/2024研究给出殖民税源关联券比例的不同样本摘要 | 每份券的`coffer`、票息、抵押收入、实际欠息/支付流水、再融资分类 |
| **C 债权人重组与新融资账** | 1743债务降息/债权转移文献、1752档案定位；DEBT.PT A 1743净长期发行507.943百万réis | 1743赎回旧债、换新券和出售新券的**毛发行额**，与新钱真实流入国库的逐笔账和资金用途 |

不能以五年黄金到账对1743净长期发行做一元因果归因；同样不能把Azevedo所述约5,000 contos当作1743**新增借贷**，因为它更接近旧债处置与债权人改变。

## 5. 复现脚本及验证状态

新增标准库源版本锁定脚本：[data_m2/reproduce_debtpt_colonial_coffers_m3.py](data_m2/reproduce_debtpt_colonial_coffers_m3.py)；运行方式：

```bash
python3 reproduce_debtpt_colonial_coffers_m3.py \
  --source /your/path/DEBT_PT_FISCAL_COFFERS_B.xlsx \
  --output-dir /tmp/case-prt-coffers
```

本轮真实运行先从GitHub读取脚本再从DEBT.PT取得原始B XLSX，输出八行CSV；**PASS**，核对真实工作表源行32`J=516`（期间净计数）及`K=50,983,813.30 réis`，源行37`K=41,093,488.8 réis`。输出文件SHA256 `d7285cf22af3716211f2ed12cf62bb4d7009c319fcd92b2e2a45c696316429c5`。源作者B工作簿不转存到本公共GitHub。

同轮2021论文PDF、2024正式章节PDF和官方Documentation.pdf实际从公开机构取得并在内存中抽取特定原文页，散列/版本信息见第1/2节；**PDF源文件不镜像**。PDF网上截图抓取出现缓存错误，未把OCR/图像核查写成已通过。Azevedo1947馆藏页直接可读Web转录及引文但**1752年档案影印未获得**。

**严格未完成**：1743法令原件Gomes1883页317、1749公告页318、1752年`Colecção Pombalina cód. 459 f.130`原件；融资实际现金流；1748发表9%和现在工作簿8.152251%的来源版本差异；2024财政研究ICPSR 198143和2025黄金ASCM ICPSR209481可运行代码，均为`NOT_ACQUIRED/NOT_RUN/SOURCE_CONFLICT_OPEN`。不要将2024项目的GitHub结构CI通过代替原始历史档案或因果论文复现。

## 6. 可移交的唯一下一步

优先按**1743-02-04法令、1743-03-28—1745-03-25转款记录、1752年档案奏报**的精确档案定位向葡萄牙公共档案/作者核对，把**旧债赎回→Patriarcal接收→王室发行净额→金库实际支付**连接成统一日期+债券持有人层级的双重分录；再判断1743年究竟有多少真正新融资，而不是将5,000 contos的债权换手误报为财政增收。原有Issue和Draft PR保持OPEN，main不合并。

### 主要公开出处
- [DEBT.PT官网](https://debt.pt/)；[8页原始数据说明](https://debt.pt/pdf/DOCUMENTATION.pdf)。
- [Azevedo (1947) 印刷375页馆藏入口](https://obrasraras.fcp.pa.gov.br/publication/file/livros/epocasportugaleconomico1947/365/)。
- [Costa et al. 2021 working paper](https://archive-ouverte.unige.ch/unige:147492)；[2024剑桥出版章节 DOI](https://doi.org/10.1017/9781108770217.015)及[作者大学正式出版PDF](https://archive-ouverte.unige.ch/unige:176869)。
- [Costa & Henriques 2024国债全史](https://doi.org/10.1163/16456432-20040019)。
