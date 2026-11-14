# CASE-PRT-001｜1765—1767年王室国库真实入款/付款与四Contadorias日记簿：1766年371.4 contos贷款的四层证据链（M3）

> 研究日：2026-11-14；权威业务Issue：[fweiger/AI_book#34](https://github.com/fweiger/AI_book/issues/34)；继续现有[Draft PR #38](https://github.com/fweiger/AI_book/pull/38)。**结论状态：1977_ARCHIVAL_INVENTORY_VERIFIED / TRANSACTION_CASH_ENTRY_NOT_IDENTIFIED / AHTC_ORIGINAL_LEDGER_PAGES_NOT_ACQUIRED / CAUSAL_EFFECT_NOT_RUN。**本轮建立的是高度定向的原账调阅与四层账证检验路径，而不是已经读到1766年借款在国库入账。

## 1. 本轮真正新增的来源：原先只有“总账卷号”，现在找到国库实际收付的独立连续账册

官方一手档案**目录而非历史交易原件**：Alzira Teixeira Leite Moreira (1977), *Inventário do Fundo Geral do Erário Régio*, Tribunal de Contas, 官方PDF https://erario.tcontas.pt/pt/arquivo_biblioteca/instrumentos_pesquisa/Inventario_Adenda_Erario_Regio.pdf ，本轮**重新独立下载并检查**：216页、3,738,870 bytes、SHA256 `fd31975695bfbc0c5299e5eed2dda24c6b21c976eadd43528e7ff79baaef6739`。目录印刷约19页的**`605–781 Livros de registo das entradas e pagamentos no Real Erário nas Caixas de rendimentos correntes e pretéritos`（王室国库当年及往年款项的入款与付款登记簿）** 直接列出：

| 1765年入款/付款簿 | 官方目录所列日期 | 1766年入款/付款簿 | 官方目录所列日期 |
|---|---|---|---|
| **617** | 1765年1月1日—3月31日 | **621** | 1766年1月1日—4月4日 |
| **618** | 1765年4月1日—7月20日 | **622** | 1766年4月5日—6月30日 |
| **619** | 1765年7月22日—10月15日 | **623** | 1766年7月1日—9月5日 |
| **620** | 1765年10月16日—12月31日 | **624** | 1766年9月5日—12月31日 |

1767年后续账簿 **625/626/627/628**，涵盖年初至年末四段。总计**1765—1767年连续历史收付登记簿12册**；这些能构成追查1766年实际资金入库/支出的**最直接馆藏定位**，但在取得原稿前，**不能保证每次银行/机构资金流都完整记录于该系列，也不能说已找到371.4 contos贷款入账**。

此前找过的`Tesouraria-mor receita/despesa`第5—10卷或`Livros Caixa`第157—159卷，与新发现的`605–781`系列不应因为名称相似就认定为同一纸质账册。

## 2. 更细的查账链条：总账—日记簿—日记草稿—现金收付簿

原目录还列出可以与旧债军费结转及里约黄金税1%迟后记账互相印证的**对应册**：

| 角色 | 原目录卷号 | 覆盖期 | 本项目欲检验的具体问题 |
|---|---|---|---|
| 第一Contadoria总账 | **537**（1762—66），**538**（1767—69） | 1762—69 | **537 fólio36：约1,564 contos军需财务官责任余额的1766结转**；fólio227/180：1765两Caixa账户 |
| 其它三Contadorias总账 | **2699**、**3976**、**4154** | 各含1765—66 | 是否有对应Rio黄金1%内部往来、跨部门结算、相反方向过账 |
| 第一Contadoria正式日记簿 | **548**（1765—66）、**549**（1766—67） | 1765—67 | 从具体日期定位总账贷借事项的**原始分录** |
| Reino e Ilhas日记簿 | **2718**（1765—66）、**2719**（1766—67） | 1765—67 | 军费、税款和对方机构跨账往来 |
| Rio、东非、亚洲Contadoria日记簿 | **3982** | 1765—67 | 核查2011研究所说**1763及以后Rio黄金1%相关款直到1766才记入借方**的对应账 |
| 西非、Maranhão、Bahia日记簿 | **4160** | 1762—70 | 另一海外分账机构的对方分录和时间归属 |
| 第一Contadoria日记草稿 | **555**（1765）、**556**（1766年1—9月）、**557**（1766年9—12月） | 1765—66 | 正式日记簿不能解释的首次书写、分录重分类或过账日期 |
| 西非与Bahia日记草稿 | **4168**（1765—66）、**4169**（1766—69） | 1765—69 | 比较草簿与正规簿不同日期或未完成的款项 |

**本轮共28条精确卷号**＝12册收付登记＋5册总账＋6册正式日记簿＋5册日记草簿，见[data_m2/ahtc_1765_1767_receipts_diaries_master_crossledger_28_volumes_m3.csv](data_m2/ahtc_1765_1767_receipts_diaries_master_crossledger_28_volumes_m3.csv)，所有卷号与覆盖期来自同一**1977年档案馆官方目录**；不是28本手稿已经下载。

### 从“找得到这本书”到“证明发生这笔钱”所需四层凭证

A. **债权人侧**：Rita Martins de Sousa (2003)引用`ANTT Ministério do Reino, Junta do Depósito Público de Lisboa, Consultas (1754–1783), maço 360 caixa 481`记载1766年王室贷款约**371.4 contos**且1777年仍未偿，先核借款合同、发放日期、借款人和应收本金。

B. **国库收款侧**：新找到的**621—624**原账逐笔查1766年是否有`Junta do Depósito Público`、371.4 contos的全部或分期款、转付给另一财政机构、贷款抵销或无现金发行的票据，而不是只搜索“371.4”这个总额。**Mont Serrath (2013)已明确说他在当年国库账细目中没有找到对应款项**，因此这一层目前`NOT_LOCATED`，不能认定为已完成。

C. **同年复式记账侧**：**548**日记簿和**537**总账关联国库付款/入款与同期债权人、负债、应付息、内部往来等科目，必要时扩展到**549**和其它`2718/2719/3982/4160`的相反账户，检查日期差和财政范围。

D. **实际资金使用与旧账核销侧**：追查`537 fólio36`中1762—66军需财务官余额**约1,564 contos**转入1766损益，必须关联最终军事收款人签收日期与上述公共存款贷款的**实际到款时间**；不能凭历史时间接近把371.4贷款称为1,564旧账的直接融资。对Rio黄金1%延期入账，亦须从**3982**与其它Contadoria的反向日记分录锁定，才可将“税权对应年份”与“国库现金年份”分开。

若借款由代付款/抵销/机构直接支付军需承包商构成，王室收款簿不一定记录一笔371.4contos的正向现金入库。反证检验必须包含**不经过国库现金而经债权重组或第三方偿付**的替代解释，不能仅从“本卷找不到”推断资金不存在。

## 3. **新发现的档案目录日期缺陷**：必须保留而非自动填补

1977年目录中有若干明显原版日期冲突：

1. 第**619卷**写1765年**7月22日**起，而618截止**7月20日**，因此**7月21日目录层面没有被明确涵盖**。不能断言历史原簿也缺账或那一天实际无收付。
2. 第**623卷**末日及第**624卷**首日**均为1766年9月5日**，两卷范围可能**重叠**或首尾含义不同，不能未经核实重复计入9月5日资金。
3. 第**626卷**末日竟记为**1767年6月31日**——公历没有6月31日；本研究**保留原始字符串，标准化末日留空**，不擅自改成6月30日；第627卷写**7月3日**开始，因此7月1—2日可能尚未有明确覆盖证明。
4. 日记草簿**556**与**557**都包含1766年9月的部分期间，月份边界没有精确日期，**不能假设无重合或者全月重复**。

这些资料品质问题已作为明确`date_quality`字段保存，而非替历史档案“修正日期”。这使后续比较库存、交易量、年度现金收支时有可见且可检验的缺页与跨册风险。

## 4. 原件所在地与获取方式，具体优先级

葡萄牙审计法院官方 [Arquivo e Biblioteca](https://www.tcontas.pt/pt-pt/TribunalContas/ArquivoBiblioteca/Paginas/Arquivo-e-Biblioteca.aspx)确认：2024年7月5日协议将历史档案**实体移存ANTT**，但资料的管理及服务由**Tribunal de Contas**负责；**原件须预约、现有数字副本须联系`dadi@tcontas.pt`申请**。本轮没有实际向机构发送邮件、预约或获取手稿数字图像。

为降低一次调阅数量，建议**先询问8项P0书目的真实当前藏号和可用扫描**：
- **国库1766年四册收付簿621、622、623、624**，并请馆方确认9月5日边界；
- **第一Contadoria总账537，尤其folio36及folio227/180和1766年余额fol274**；
- **正式日记簿548（1765—66）、549（1766—67）**；
- **Rio Contadoria日记簿3982**，作为1763黄金相关1%税1766过账的替代机制证据。

确认卷号后应先按`Junta do Depósito Público`、`371,400,000 réis`、`Luís Gomes Peixoto`、`Junta dos Três Estados`、`1% ouro`等关键词请求**连续前后叶影印**，并检查索引是否还有实际日期、贷款笔数和收款代理人等不同拼写。馆方若只有部分数字副本，优先得到**相关首页、交易页和年终结账页**，而非要求整体档案全量复制。**未获得复制或公开授权的手稿不可自动上传公开AI_book**。

### 交易级证据登记规范（待原始手稿获得后才填具体值）

`historical_event_id, source_fund, current_cota, book_id, folio, archival_page_hash, old_book_cota, transaction_type, original_reis, currency_definition, entry_date, effective_date, money_received_or_paid_date, authorized_date, counterparty, counterpart_book_folio, direction, direct_cash_or_setoff_or_book_adjustment, missing_folio_status, verification_grade`。

未得到原件前，所有`actual_loan_cash_date, actual_amount_disbursed, 1766_fiscal_military_cash_effect`应保持`NOT_IDENTIFIED`，不得凭目录CSV产生假交易记录。

## 5. 真实执行与QA边界

新增：
- [28条官方馆藏卷号和来源标注表](data_m2/ahtc_1765_1767_receipts_diaries_master_crossledger_28_volumes_m3.csv)（2019等论文涉及的旧总账与新现金流原簿以真实系列区分）；
- [28卷官方来源、历史日期错误及藏号验证脚本](data_m2/validate_ahtc_1765_1767_direct_cash_books_28_volumes_m3.py)。

在网络化研究Runner中，实际重新下载本仓库当前分支CSV/脚本、1977年审计法院官方216页PDF，对官方PDF SHA256及1977年官方书号对应的系列/日期、全部P0集合、原始手稿未取得状态执行**EXIT0 PASS**：

```text
PASS 1977_archival_book_locations=28 cash_1765_1767=12
 cash_1766=4 master=5 journal=6 draft=5 P0=8
 catalogue_date_flags=6 flagged_ids=[557, 619, 623, 624, 626, 627]
 invalid_1767_June31=NOT_NORMALIZED 1766_Sep5=OVERLAP
 1766_371400000_reis_creditor_loan_crown_cash_ENTRY_NOT_FOUND
 handwritten_original_pages=NOT_ACQUIRED causal_inference=NOT_RUN
 csv_sha256=6ba13089be435cd174d06cf37170bfa43687c81445e1fac80b9576d707515826
```

第二项**故意篡改来源元数据**的反向测试：将原本目录误写`1767-06-31`第626卷的规范化末日擅改成`1767-06-30`，验证器以退出码2拒绝，错误理由为`wrong volume/series or date range`。本轮只能宣称**目录数据品质、原始文件哈希和证据准备可复算**，不能宣称已通过AHTC历史账务原件、1766现金账内的借款出现检查或任何财政军费因果模型。

## 6. 下一项唯一可验收任务

**取得能打开的1766年收款/付款原始账册第621—624卷至少涉及Junta do Depósito Público的连续原页，及对应日记簿548/549与总账537 fólio36等账页，再把已发表的371.4 contos债权与王室实际入账/代付/无现金换券明确匹配**。先核对*官方1977卷号与2024搬迁后现用cota及数字化可用性*。若无法合法获取原始图片，保持`NOT_ACQUIRED`并只继续发表资料的会计定义审查，不建立模拟逐笔流水。

2019博士正文“约2,765 contos”与同版附录E按借贷方向净额359.525124 contos的差异仍是`SOURCE_VERSION_SCOPE_OPEN`；1748债务率9%/8.152%冲突、1749/1750降息法令日期差、2025黄金ASCM复现包仍待继续验证。现有Draft PR不合并。
