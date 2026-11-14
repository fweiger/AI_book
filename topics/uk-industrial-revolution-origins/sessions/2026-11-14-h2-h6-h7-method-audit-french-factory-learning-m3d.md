# 2026-11-14 · TOPIC-010 M3-D — H2/H6/H7跨论文识别边界与法国工厂学习

**规范任务** [AI_book #30](https://github.com/fweiger/AI_book/issues/30)，已有 Draft PR [#31](https://github.com/fweiger/AI_book/pull/31)。恢复上轮M3综合裁决，执行同一AI的方法学红队审查；不是独立第二AI（AC-07仍NOT_RUN）。

## 主要新证据

- Juhász、Squicciarini、Voigtländer[2024 JPE正式论文](https://doi.org/10.1086/730205)用法国机械棉纺厂历史企业数据研究机器采用后组织学习，早期生产率分布极不均匀，后续低效率企业退出和组织适应推动改善；同一作者[2020 CEPR公开研究说明](https://cepr.org/index.php/voxeu/columns/technology-adoption-and-productivity-growth-evidence-industrialisation-france)报告1806–1840约82%的后采用棉纺企业劳动生产率增长，2024最终表未独立核对。
- Juhász 2018 [AER官方摘要](https://doi.org/10.1257/aer.20151730)研究1803–15法国不同贸易封锁暴露下实际纺纱机容量增长，因变量是法国后发采用而非英国1750s机器首次发明；其[官方/作者补充附录](https://www.rjuhasz.com/research/napoleonic_blockade_onlineappendix.pdf)包含原棉输入、替代产业、稳健性反证，但统计复现NOT_RUN。
- Kelly/Mokyr/Ó Gráda [2023 JPE官方摘要](https://doi.org/10.1086/720890)支持英国内41郡的初始低工资、高机械技能与后续工业化。其[2020 UCD公开工作论文](https://researchrepository.ucd.ie/server/api/core/bitstreams/45847339-74fd-4126-aa9b-2f15c21d788d/content)说明用1851年60岁以上出生郡机械工职业反推早期技能，存在生存选择与工具变量排除限制待审；不是正式期刊表的独立复算。
- Allen(2009)和Gragnolati等(2011)纺纱珍妮NPV理论不同于上述区域和厂级历史回归；不能把模型IRR解释为真实企业收益或把各系数相加成国家工业革命贡献率。
- 英国的高工资或廉价煤不构成工业化单一充分条件，法国机器后发采用及真实企业学习证明`发明—购买—安装—组织高效运营—产出和出口`并非同一事件。

## 本轮新增计算（仅假设敏感性）

在同一Allen/Gragnolati法国珍妮模型下设置旧工艺劳动100等效日、工资4.66d、设备1450d、P=3、10年、年维护10%、门槛15%，令θ为新机最大新增产出实际卖出的比例、ρ为新增销量每单位净贡献实现系数。

`C(θ,ρ)=wL[(1−1/P)(1−θ)+(P−1)ρθ]−0.1J`，`J≤A(15%,10)×C`；在ρ=1时θ≥**19.836%**，若ρ=0.75则≥**31.738%**，ρ=0.5则≥**79.345%**，ρ=0.45即使θ=100%也不满足15%。以上均**本项目纯理论条件，不是1780年代法国实际订单/产量数据，假设旧产量售价不变且材料成本隐含在ρ**。

JavaScript公式及Python独立计算核对四情景数值吻合（本轮没有原始历史回归重跑）。

## GitHub新增文件与状态

- `data/TOPIC010_M3D_H2_H6_H7_CROSS_DESIGN_CAUSAL_AUDIT_20261114.md`
- `data/industrialization_h2_h6_h7_estimand_provenance_m3d.csv`（5条跨论文估计量）
- `data/france_jenny_h2_sales_absorption_threshold_m3d.csv`（4条纯反事实测试）
- README与本会话；现有四国子Issue不改、所有原PR仍草稿。

新结论：法国2024企业级研究使H7的“机器采用后仍需知识与企业组织学习”获得更直接的证据；Juhász2018支持某一局部市场保护冲击影响法国采用；H6在模型下有经济性但不能解释所有阶段。**整个五国交互因果模型、法国JPE2024复制数据与独立史学评审NOT_RUN。**

**唯一下一研究动作**：直接检查2024 JPE作者正式哈佛复现包 `https://doi.org/10.7910/DVN/EGWOPG`，若实际能取得厂级数据，分辨生产率成长中企业内改善/新进入/低效退出的贡献；否则阶段收束并请求真正独立审查，而非继续模拟或追踪帝国账簿。
