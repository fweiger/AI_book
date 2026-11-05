# TOPIC-006 · 来源与核查范围（2026-11-05）

**S01｜演讲一手材料**：Joseph Kim / OpenAI，*How OpenAI Built ChatGPT for Bankers and Analysts*：[YouTube 视频](https://www.youtube.com/watch?v=opHmX7qClzE)，[AI Engineer 文字整理](https://ai.engineer/talks/opHmX7qClzE-openai-built-chatgpt-bankers-analysts)。本次读取了用户 Ubuntu 服务器上这场公开演讲的英文自动字幕（共 1,144 行、约 18:54）；不在公开仓库上传字幕或私人路径。关键片段：06:01–09:00 数据与产品实现；13:13–14:58 实用性阈值；15:00–16:47 金融训练；17:14–18:54 持续 Agent 与预测。字幕自动识别可能有误；关键事实请与视频或官方介绍交叉核对。证据作用：**证明 Kim 表达了哪些观点和预测**。

**S02｜OpenAI 产品官方陈述**：[Introducing ChatGPT for Financial Services, 2026-09-10](https://openai.com/index/introducing-chatgpt-financial-services/)。公开介绍与 Morgan Stanley、Evercore 的设计合作、授权金融数据、可追踪引用、模板、合规功能。证据作用：**产品方的功能与路线陈述，不是独立性能评价**。

**S03｜SEC 数据质量权威讨论**：[The Role of Machine Readability in an AI World](https://www.sec.gov/newsroom/speeches-statements/speech-bauguess-050318)。明确提醒结构化与机器可读不等于数据本身正确。证据作用：数据质量与标准化分离的监管讨论。

**S04｜SEC 结构化财报接口**：[EDGAR APIs / XBRL](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)。提供官方 XBRL 概念、单位、财务披露接口与限制。证据作用：数据类型与字段口径的技术规范。

**S05｜财务建模基准**：[Poeltl et al. (2026), MBABench-2.0, arXiv:2610.31711](https://arxiv.org/abs/2610.31711)。论文摘要报告 101 项构建任务、129 项质量准则、最佳受测 Agent 通过率 16%。**目前依据论文公开网页/摘要，不宣称已独立复算或审查每项样本**。

**S06｜金融评估偏差**：[Kong et al. (2026), Evaluating LLMs in Finance Requires Explicit Bias Consideration, arXiv:2602.14233](https://arxiv.org/abs/2602.14233)。讨论前视、幸存者、叙事、目标与成本偏差；方法论框架，非对 Kim 预测的直接验证。

**S07｜财务问答**：[Islam et al. (2023), FinanceBench, arXiv:2311.11944](https://arxiv.org/abs/2311.11944)。金融问题与原始证据字符串；历史被测模型的成绩不能当作 2026 模型的即时状态。

**S08｜财务数值推理**：[Chen et al. (2021), FinQA, ACL EMNLP](https://aclanthology.org/2021.emnlp-main.300/)。提供多步数值推理与可解释计算程序，可作为专用评测的一部分。

**S09｜真实电子表格工作流**：[SpreadsheetBench V2](https://spreadsheetbench.github.io/)。覆盖建模、修复、可视化与多表任务；不与 MBABench 直接合并排名。

## 2026-11-05 全行业扩展来源（新增公开网页与研究摘要级）

**S10｜BoE/FCA**：[Artificial intelligence in UK financial services - 2026, 2026-10-26](https://www.bankofengland.co.uk/report/2026/artificial-intelligence-in-uk-financial-services-2026)，86%报告使用 AI、80%报告部署 AI Agent、2%报告使用广泛自主权 Agent；仅在受访机构定义下成立。

**S11｜Cambridge CCAF**：[2026 Global AI in Financial Services Report](https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/2026-global-ai-in-financial-services-report/)，企业与监管机构采用情况及重点用例。自报调查不代表全行业随机抽样统计或独立收益。

**S12｜FSB 监管治理**：[2026-10-15 Final Sound Practices](https://www.fsb.org/2026/10/fsb-finalises-sound-practices-for-the-responsible-adoption-of-artificial-intelligence-ai/)，正式版本的12项治理实践；不再以2026年6月咨询稿替代。

**S13｜Anthropic 产品**：[Agents for financial services, 2026-05-05](https://www.anthropic.com/news/finance-agents)，模板、金融数据连接与跨Office使用；产品方说明，非独立效果评测。

**S14｜Bloomberg 产品**：[ASKB by Bloomberg AI](https://professional.bloomberg.com/products/bloomberg-terminal/ai/askb/)，以数据/新闻/研究/分析工具驱动的代理式自然语言工作流；产品方说明。

**S15｜金融研究代理基准**：[Vals Finance Agent v2.1，更新 2026-11-04](https://www.vals.ai/benchmarks/fabv2-1)，最佳被测模型67.85%；属于指定任务、环境与评价标准下的分数，不可与 MBABench 横向排名。

**S16｜检索失败机制研究**：[Kobeissi & Langlais，PMLR 2026](https://proceedings.mlr.press/v318/kobeissi26a.html)，150道 FinanceBench 问题分文档/页/块定位与检索瓶颈；可读论文网页与摘要级信息。

**S17｜交易长期反证**：[Li et al.，FINSABER，arXiv:2505.07078](https://arxiv.org/abs/2505.07078)，研究摘要报告部分LLM策略长期扩展后的优势衰减，不是对所有模型或策略的否定。

**S18｜财务工作簿端到端**：[WorkstreamBench，arXiv:2605.22664](https://arxiv.org/abs/2605.22664)，评估准确性、公式、格式等专业标准；摘要级。

**S19｜公开用例追踪**：[Evident Banking Q2 2026](https://evidentinsights.com/insights/banking-use-case-trends-q2-2026)、[Insurance Q2 2026](https://evidentinsights.com/insights/insurance-use-case-trends-q2-2026)，企业已披露的产品/用例统计，存在披露偏差。

**S20｜公共金融预测研究**：[US Office of Financial Research 2026-08-25](https://www.financialresearch.gov/the-ofr-blog/2026/08/25/deep-learning-methods-improve-financial-forecasts/)，用于传统深度学习与金融预测同基准比较的研究入口。

详细对照见 [全行业研究地图](landscape-2026-11-05.md)。

## 后续证据准入
- 主张需标：来源是现场主张/公司宣传/监管规范/同行评议论文/基准实验/独立复现/本专题推测；
- 所有数值标明测试版本、任务集合、日期和评价定义；
- 金融预测必须追溯 **信息实际公开时间**，禁止未来信息污染；
- 公开文献只阅读到摘要时，必须明确标记“摘要级”，不可声称全文精读。
