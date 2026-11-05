# 金融 AI 全行业研究地图｜2026-11-05（TOPIC-006 / R1）

> 证据截面：2026-11-05。此页是**公开来源的初步跨行业梳理**，不是所有金融机构的全覆盖统计，也不是任何产品的独立采购推荐。证据类别分为 A=监管/央行/公开统计，B=同行评议/可复核基准，C=产品方声明，D=研究假说。多个统计来自不同样本，**不能直接相加或比较为全球市场份额**。总讨论见 [Issue #22](https://github.com/fweiger/AI_book/issues/22)。

## 最重要的总体结果

- **已有使用≠可自主决策**：英国央行/FCA [2026-10-26 调查](https://www.bankofengland.co.uk/report/2026/artificial-intelligence-in-uk-financial-services-2026) 中，86%受访金融机构报告使用 AI，80%报告部署 Agent；仅2%报告广泛自主权 Agent。这里是**受访机构比例**而非行业所有 Agent 或交易笔数，决策支持部署与其他授权等级可共存。
- **行业重心在工作流/运营**：[剑桥大学商学院 2026 全球调查](https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/2026-global-ai-in-financial-services-report/) 的金融业受访对象里，流程自动化79%、可视化75%、软件工程75%、数据与知识管理69%达到试点或以上；欺诈检测58%、信用风险建模54%也是显著方向。
- **产品上市≠专业任务已普遍可靠**：OpenAI、Anthropic 与 Bloomberg 已提供有金融数据接入和代理化分析功能的产品/方案；而 [MBABench-2.0](https://arxiv.org/abs/2610.31711) 对101项构建完整金融工作簿任务的最佳受测代理总通过率为16%；另一套 2026-11-04 更新的 [Vals Finance Agent v2.1](https://www.vals.ai/benchmarks/fabv2-1) 上最佳模型为67.85%（基准任务与口径不同，**不能直接比较16%和67.85%**）。
- **投资 alpha 最需要额外审计**：[FINSABER 长时段回测研究](https://arxiv.org/abs/2505.07078) 发现部分已发表 LLM 交易优势在扩大时间和标的覆盖后显著恶化。不能由财报理解任务准确率推出可交易收益。

## 八大主线及当前进展（不是互斥市场份额）

| ID | 业务主线 | 已观察的产品/研究进展 | 当前可支持的成熟度判断 | 尚缺的关键环节 | 证据 |
|---|---|---|---|---|---|
| D01 | 金融专业数据、RAG、知识基础设施 | OpenAI 产品内置并索引许可数据；Claude 接多家金融数据商；Bloomberg ASKB 用 Terminal 数据/分析工具 | **产品已发布**；检索颗粒度可靠性仍待量化 | as-of、来源/页表定位、版本修订、供应商一致性、数据许可 | [OpenAI](https://openai.com/index/introducing-chatgpt-financial-services/)、[Anthropic](https://www.anthropic.com/news/finance-agents)、[ASKB](https://professional.bloomberg.com/products/bloomberg-terminal/ai/askb/)、[PMLR 2026](https://proceedings.mlr.press/v318/kobeissi26a.html) |
| D02 | 投行/股票研究、财报与尽调 | 财报/电话会检索、公司对比、研究报告/Pitchbook，内建财务数据与证据引用 | **商业工作流已经出现**；专业效果需基准及人工修复测量 | 跨来源冲突、财务术语、单位、上下文、长期迭代 | [OpenAI](https://openai.com/index/introducing-chatgpt-financial-services/)、[Vals FAB v2.1](https://www.vals.ai/benchmarks/fabv2-1) |
| D03 | Excel/三表/估值模型/企业财务规划 | 企业模板与表格工具增强、金融工作簿自动构建研究 | **工具可运行；复杂端到端交付仍未成熟** | 公式链、三表勾稽、可维护性、假设隔离、人工复核时长 | [Anthropic](https://www.anthropic.com/news/finance-agents)、[MBABench 2.0](https://arxiv.org/abs/2610.31711)、[WorkstreamBench](https://arxiv.org/abs/2605.22664) |
| D04 | 量化研究、收益预测、资产配置、交易 | 历史文本信号、情绪、策略代理、传统 ML 与深度学习预测 | **传统 ML 已有广泛研究与应用**；LLM 自主交易有稳健性缺口 | 严格样本外、市场状态、交易成本、容量、反身性及风险 | [BIS 2024 分类](https://www.bis.org/publ/arpdf/ar2024e.pdf)、[FINSABER](https://arxiv.org/abs/2505.07078)、[OFR 2026](https://www.financialresearch.gov/the-ofr-blog/2026/08/25/deep-learning-methods-improve-financial-forecasts/) |
| D05 | 信贷风控、反洗钱 KYC、欺诈/支付 | 已有较成熟传统 ML；在信贷审查、交易监测、调查与客户尽调中叠加 GenAI | **风控子任务广泛存在生产应用**；自动批准/拒绝客户决策需要更严格治理 | 可解释、公平、隐私、低误报、对抗欺诈和持续监测 | [剑桥 2026](https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/2026-global-ai-in-financial-services-report/)、[Evident Q2](https://evidentinsights.com/insights/banking-use-case-trends-q2-2026)、[FSB 2026](https://www.fsb.org/2026/10/fsb-finalises-sound-practices-for-the-responsible-adoption-of-artificial-intelligence-ai/) |
| D06 | 财富管理、客户沟通、投顾与保险 | 客服 Copilot，顾问辅助；保险核保资料整理和索赔流程中扩展 AI | **辅助应用已部署**；完全自主建议/定价/理赔需分开评价 | 适当性、利益冲突、责任归属、客户保护和评价闭环 | [剑桥 2026](https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/2026-global-ai-in-financial-services-report/)、[Evident 保险 Q2 2026](https://evidentinsights.com/insights/insurance-use-case-trends-q2-2026) |
| D07 | 金融机构内部流程与持续 Agent | IT/运营、对账、财务关账、知识管理、合规流程 Agent；跨应用编排 | **广泛探索与辅助生产**，但具广泛自主权的系统极少 | 长周期可靠性、权限审计、失败恢复、幂等、人工审批、成本 | [BoE/FCA 2026](https://www.bankofengland.co.uk/report/2026/artificial-intelligence-in-uk-financial-services-2026)、[Anthropic 十类模板](https://www.anthropic.com/news/finance-agents) |
| D08 | 金融 AI 模型评测、审计、治理/安全 | 监管框架、公开金融基准逐步完善，跨模型财务研究评分出现 | **评测/治理框架推进快**；可复现、无污染、真实经济价值仍待加强 | 评价基准代表性、模型版本、指标迁移、审计链、外包集中度 | [FSB 2026 正式发布12项治理实践](https://www.fsb.org/2026/10/fsb-finalises-sound-practices-for-the-responsible-adoption-of-artificial-intelligence-ai/)、[Vals v2.1](https://www.vals.ai/benchmarks/fabv2-1) |

## 把 Joseph Kim 的三项预测映射到主线

- **P1 减少人工 Excel/PPT**：D01→D02→D03→D08；若拿不到可审计数据、正确公式及专业验收，无法宣称 P1 达标。
- **P2 长期 AI 同事**：D01→D07→D08；能连续运行和能安全承担责任不同。
- **P3 超越顶尖专家的前瞻预测**：D01→D02/D04→D08；“会分析财报”≠“预测会更准”≠“交易净收益更高”。

## 最值得投入进一步实证的问题（优先不追逐模型排行榜）

1. **D01 数据检索瓶颈可分解**：2026 年 [PMLR 研究](https://proceedings.mlr.press/v318/kobeissi26a.html) 在150道 FinanceBench 问题上发现，检索到正确文档不保证正确页面/段落；领域化页面排序有潜力。建议测试 document / page / table-cell 三层 Recall@k 与回答证据精确性。
2. **D03 表格专业可靠性缺口**：MBABench 2.0 评估101个任务、129项标准，最强被测代理整体通过率约16%，说明应逐项报告 numeric correctness、formula integrity、format/readability、repair time。
3. **D04 预测不应跳过长期反证**：FINSABER 研究警示原先报告的 LLM 策略优势可能随样本规模和市场阶段变化而恶化；应预先登记基准、交易成本、数据可得时间和统计检验规则。
4. **D07 自主权要与采用率拆开**：英国央行2026调查仅2%的受访机构报告广泛自主权 Agent；不要把“已部署 Agent”解释为“可自动交易或支付”。
5. **D08 治理不可选**：FSB 2026-10-15 正式版本列出12项实践，包括数据治理、解释性、持续评估、人类监督、ICT安全和第三方依赖；不得把6月咨询稿当作当前最终文本。

## 证据分层和明显偏误
- **监管与机构问卷**反映受访者自报使用，不代表独立审计性能，也不保证样本全球代表性。
- **厂商产品页面**证明“发布/宣传了什么”，不能证明客户工作成效或真实 P&L。
- **基准结果**仅在特定任务、模型版本、工具权限、评分规则下有效；测试集、时间和任务不可混排名。
- **策略回测**不等于事前收益，特别需要无未来信息、真实费用、容量约束和多阶段对照。
- 所有关于未来专家替代、盈利改善与长期自主能力的断言均标记为**未验证预测**。

## 对 AI_book / AI_Trader 的分工边界

AI_book 负责：跨行业研究地图、来源/假说/反证、基准分析、通用“数据—能力—验证”研究方法。AI_Trader 负责：**在可使用的真实金融数据上执行可复现实验**（行情时点、财报模型、交易成本后效益等）。两个仓库用链接关联，不在公开 AI_book 中复制私有数据。

下一步的研究协议见 [multi-agent-protocol-2026-11-05.md](multi-agent-protocol-2026-11-05.md)，正式研究讨论见 [Issue #22](https://github.com/fweiger/AI_book/issues/22)。
