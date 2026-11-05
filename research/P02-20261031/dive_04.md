# Dimension 04: 该不该为股权降薪

## Dimension 04: 决策框架：该不该为股权降薪

### Current State

- **决策本质是把部分确定现金换成一张高方差彩票**。降薪换股权 = 接受"期望值不确定、兑现期 4 年起、单公司集中风险"的组合，决策依据不是"公司好不好"，而是三个输入的联合判断（见下方决策树）[^d4-tree]。
- **决策树（三输入）**：① 公司阶段——Pre-IPO 独角兽有二级市场定价参照（如字节回购价），风险最低但溢价也薄；A/B 轮公司股权翻 10 倍潜力大但死掉概率≥50%；② 个人现金流——若降薪导致 6 个月内现金流断裂或需要动用应急金，一票否决（期权还可能要求自付行权款+税）；③ 风险偏好——能否承受股权归零且工资差额永久损失。三输入中有两个为"差"，答案就是"不为股权降薪"[^d4-tree]。
- **期望值为负的信号清单（出现任意一条即下调期望值，出现两条以上视为负期望）**：① 无限改期——IPO/回购时间表反复推迟（排队、整改、市场窗口不佳等说辞）；② 无回购/无二级流动性——员工无法在任何节点把纸面价值变现，参考字节从 2025 年 4 月 161.42 美元到 10 月 180.37 美元的回购价上调（年涨约 12%），有回购的期权才有"类债券"下限，无回购的只是数字（E02共享背景）；③ 估值虚高融资——上一轮估值靠明星概念而非收入支撑，下一轮 down round 会稀释+行权价倒挂；④ 归属条款苛刻——4 年归属 + 1 年 cliff 属于行业默认，但离职不保留加速归属、期权 90 天内不行权即作废属于负面条款；⑤ 用股权解释全部薪酬差距——降薪 30% 以上而股权占比无法折算成可验证价值（E02共享背景：RSU 蒸发五机制中的未归属作废机制）。
- **美国口径：暴富是小概率事件**。Carta 数据显示，2019 Q1 的种子轮公司队列到 Q16（约 4 年后）仅 49.1% 晋级 A 轮；中位种子→A 轮时间从 2019 年的 1.5 年拉长到 2.1 年——即近半数员工的期权支撑公司在 4 年内都走不到可退出阶段[^d4-seeda]。行权意愿数据同样说明问题：2023 Q1 员工仅行权 28% 的已归属期权（2022 Q1 为 44%），2024 Q4 该比例仅 32.2%——行权要真金白银付行权款+税，员工用脚投票说明纸面价值兑现的不确定性[^d4-exercise][^d4-math]。
- **对地学博士：值得拿股权的场景收窄为三类**。① 产业早期+技术合伙人：以创始人/联创身份拿 5%–30% 期权池份额，赌的是"技术-公司"绑定而非打工溢价；② 硬科技早期核心员工（半导体、地学数据、遥感、能源）：在人才稀缺、期权池尚慷慨、公司估值尚未透支的 A/B 轮进入，用可替代性换谈判筹码（胡润 2025 新面孔 263 位主要来自半导体/AI，说明硬科技造富窗口确实存在——E02共享背景）；③ 有独立变现通道的 Pre-IPO 公司：有回购、有二手转让、有明确上市时间表的（如字节在职 200.41 vs 离职 180.37 美元的回购价差机制，E02共享背景）。反面场景：传统地矿/油气大企业的"股权激励"实为限制性绩效挂钩工具，不是暴富通道。
- **Offer 阶段必问的五个股权问题**：① 期权还是 RSU？行权价多少、当前优先股股价多少（决定期权是价内还是纸面）？② 归属节奏与离职条款——cliff 多长、离职后行权窗口多久、有无单览权利（single trigger acceleration）？③ 有无回购或员工二手转让计划，最近一次成交价和时间？④ 优先清算倍数（liquidation preference）多少——1x 还是参与分配，决定退出时员工是否先被投资人截流？⑤ 公司现金跑道和下一轮融资时间——决定 4 年归属期内倒下的概率。
- **期望值计算示例（假设明示，属建模推演非统计事实）**：以降薪 20 万/年 × 4 年 = 80 万现金代价，换 0.05% 期权为例。情景加权：40% 概率公司倒闭/无流动性 → 回报 0；35% 概率横盘或小幅回购 → 回报 30 万（扣除行权款和税后）；20% 概率以中位估值退出 → 回报 150 万；5% 概率成为 superstar 退出 → 回报 800 万。期望值 = 0×40% + 30×35% + 150×20% + 800×5% = 10.5 + 30 + 40 = 80.5 万 < 80 万现金代价，且未计入 4 年现金的机会成本（如稳健理财约 2%–3% 年化）。结论：只有把"superstar 概率"或回报倍数再上调，或降薪幅度降到 15% 以下，期望值才转正——**默认答案是"不为股权降薪"，除非你在赌自己进了那 5%**[^d4-ev]。三种口袋纪律对应：现金口袋（降薪部分）永久损失预算 ≤ 家庭金融资产 10%。

### Key Evidence

| 数据点 | 数值 | 时间 | 原文摘录(逐字) | 自评信度 | 来源 |
|---|---|---|---|---|---|
| 种子轮公司晋级 A 轮比例（2019 Q1 队列） | 49.1%（Q16 时点） | 2019 Q1–约2023 Q1（引用于 2024） | "The 2019 Q1 cohort hit 49.1% by Q16." | 高 | [^d4-seeda] |
| 种子到 A 轮中位时间 | 2.1 年（2019 年为 1.5 年） | 引用于 2024 | "Median time from Seed to Series A is now 2.1 years, up from 1.5 years in 2019." | 高 | [^d4-seeda] |
| 员工行权率（已归属期权中实际行权比例） | 28%（Q1 2022 为 44%） | 2023 Q1 | "The rate of vested stock options that employees exercised fell to 28% during the first quarter of 2023. in Q1 2022, employees exercised 44% of..." | 高 | [^d4-exercise] |
| 员工行权率（完全归属且价内期权） | 32.2% | 2024 Q4 | "In the fourth quarter of 2024, employees at startups on Carta opted to exercise just 32.2% of all equity grants that were both fully vested and..." | 高 | [^d4-math] |
| 初创股权薪酬整体缩水 | −36% | 引用于 2024–2025 | "There's been a 36% decrease in equity compensation compared to previous years, despite minor salary increases (1-2% year-on-year across functions)." | 中（二手转述 Carta） | [^d4-mucker] |
| 个人贡献者初始股权授予中位数变化 | 两年上涨近 11% | 2025 下半年报告 | "the median size of initial equity grants issued to individual contributors at companies on Carta is up nearly 11% over the past two years" | 中（摘要转述，原文页未能全文核验） | [^d4-carta-comp] |
| 字节期权回购价 | 161.42→180.37 美元，年涨约 12% | 2025 年 4 月→10 月 | E02共享背景，不重复检索 | 高 | E02共享背景 |
| 字节在职/离职回购价差 | 200.41 vs 180.37 美元 | E02期 | E02共享背景，不重复检索 | 高 | E02共享背景 |
| 硬科技造富窗口 | 胡润新面孔 263 位主要来自半导体/AI | 2025 | E02共享背景，不重复检索 | 高 | E02共享背景 |

### Tensions & Counter-arguments

- **"暴富率低"vs"期望值仍可能为正"**：近半数种子公司 4 年内未晋级 A 轮、行权率仅三成，是集中证据；但成功退出是右偏分布，一个 superstar 案例可拉高整个组合期望值。反驳：员工不能持组合，单公司持股方差不因右偏消失——期望值正不等于个人该下注。
- **行权率数据的双解**：行权率低既可读作"员工不看好"，也可读作"流动性受限+税负约束下的理性观望"（Carta 自己的口径是行权率随估值下行而下降）。不能把行权率直接等同于"股权无价值"。
- **中美口径差异**：Carta 数据基于美国私有公司（4 年归属、90 天行权窗口为主），中国公司条款（离职回购折价如字节 9 折、回购窗口由公司单方决定）差异大，直接套用美国暴富率会低估国内 Pre-IPO 制度摩擦；反向亦然，宇树 IPO 峰值 1300 亿回落至 695 亿、老铺黄金 +220%（E02共享背景）说明国内上市造富波动更剧烈。
- **股权缩水 36% 与授予额涨 11% 并存**（[^d4-mucker] vs [^d4-carta-comp]）：前者是期权（options）薪酬总盘对前些年的比较，后者是 RSU/初始授予中位数，两者口径不同不构成矛盾，但说明"股权在变稀缺也在变集中"，普通员工拿到的期权更少、更值钱的股权向核心人员集中。
- **地学博士的特殊反向观点**：学术界转型产业的技术合伙人路径，机会成本包含放弃的教职/编制安全垫；若博士已 30+ 岁、家庭现金流刚性，同样的股权 offer 对其期望值评估应比 25 岁工程师更保守——股权溢价不能补偿不可逆的职业路径切换成本。
- **未能核验项**：Carta H1 2024 报告中"1 in 5 options had..."的完整句子（疑似关于期权过期作废比例）因原文页抓取失败未获逐字摘录，标为待证，不影响主结论。

[^d4-tree]: 决策框架为本研究自建模型（推测/建模，非统计事实），输入阈值参考 Carta 行权率与晋级率数据锚定。
[^d4-seeda]: The Real State of Seed Today: The Top 10 Learnings (SaaStr，基于 Carta 数据). 2024. https://www.saastr.com/the-state-of-seed-today-10-key-learnings-from-cartas-latest-data
[^d4-exercise]: Startup employees were less likely to exercise stock options (Carta). 2023-06-02. https://carta.com/data/stock-options-exercise-q1-2023
[^d4-math]: Should I Exercise My Vested Stock Options? The Math May Surprise You (Carta). 2025-05-02. https://carta.com/data/stock-options-math-2024
[^d4-mucker]: Compensation Benchmarks for Early-Stage Startups From Carta (Mucker Capital). 约2024–2025. https://mucker.com/blog/compensation-benchmarks-early-stage-startups-from-carta
[^d4-carta-comp]: State of Startup Compensation: H2 2025 (Carta). 2025（页面日期标注 2026-05-04）. https://carta.com/data/startup-compensation-h2-2025
[^d4-ev]: 期望值计算为本研究建模示例，概率与回报均为假设，用于演示决策方法，非统计结论。
