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

## 后续证据准入
- 主张需标：来源是现场主张/公司宣传/监管规范/同行评议论文/基准实验/独立复现/本专题推测；
- 所有数值标明测试版本、任务集合、日期和评价定义；
- 金融预测必须追溯 **信息实际公开时间**，禁止未来信息污染；
- 公开文献只阅读到摘要时，必须明确标记“摘要级”，不可声称全文精读。
