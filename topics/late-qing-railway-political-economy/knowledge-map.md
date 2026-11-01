# TOPIC-004｜利益与制度机制知识图谱（研究假说版）

该图只表达**分析对象与待检验的关系**，不是全体箭头已由史料证明的因果图。

```mermaid
flowchart LR
  N1["N1 煤炭与运输成本"]
  N2["N2 旧陆运/船运/码头"]
  N3["N3 旗地与征地权利"]
  N4["N4 地形/融资/工程约束"]
  N5["N5 朝廷审批与政治否决权"]
  N6["N6 煤河+短铁路接驳"]
  N7["N7 矿务局与招商局关系"]
  N8["N8 驴马表述与机车运行"]
  N9["N9 分段扩建与制度变迁"]
  N4 -->|工程约束;研究文献支持| N6
  N3 -->|征地审批阻碍;研究文献支持| N5
  N7 -->|可能改变运输收益;待定量| N1
  N1 -->|经济激励;推论| N6
  N2 -.->|既有行业反对? 待证| N5
  N5 -->|许可/限制;研究文献支持| N8
  N6 -->|接驳;研究文献支持| N8
  N8 -->|发展;动态解释待证| N9
  N6 -.->|利益安置联盟? 待证| N2
  N5 -.->|联盟策略? 待证| N6
  classDef evidence fill:#e8f2ff,stroke:#7a9fba;
  classDef hypothesis fill:#fff2dc,stroke:#c4a46a;
  class N3,N4,N6,N7 evidence;
  class N2,N5,N8,N9 hypothesis;
```

## 关系解读

- **实线**：文献所支持的事件关联或一般经济作用，仍要看标注是否有推论。
- **虚线**：明确的待验证政治机制。
- 「旧运输业」「旗地持有人」「矿务局与招商局」**不能合并成二元阵营**；交通运输不同路段可能互补或替代。
- 图谱不是支付函数估算，更不证明李鸿章或唐廷枢的主观规划。

[机器可读 JSON](knowledge-graph.json) · [论点台账](claims.md) · [方法论](../../docs/methodology/infrastructure-reform-coalition-process-tracing.md)。
