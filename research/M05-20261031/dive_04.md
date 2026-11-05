# Dimension 04: 反面——Churn如何杀死一切

## Dimension 04: Churn如何杀死一切

### Current State

- **Churn的数学是指数的，不是线性的**：月流失5%不是年流失60%（5%×12），而是 1−(1−0.05)^12 = 1−0.95^12 ≈ 45.96%，即**年流失约46%**。复利式流失意味着：客户基数越大，每月需要补充的新客绝对量越大，一旦获客引擎减速，收入池加速干涸。[^thinkingai-churn]
- **David Skok的经典论证**：churn是SaaS的"致命"变量——在月流失5%的假设下，公司需要不断把新收入用于填补流失缺口，增长曲线上限被死死压住；只有做到负churn（negative churn，靠增购/扩张超过流失）才能摆脱这个天花板。[^skok-churn]
- **死亡谷的先后顺序**：GRR（毛收入留存）先行恶化（客户开始取消/降级）→ 现金流入（预收的年费变薄）→ NRR跌破100%（流失超过扩张，存量收入池收缩）→ 估值倍数被压缩。2025–2026年的SaaS估值修正中，NRR低于100%的公司即便Rule of 40达标仍被给到折价倍数（有行业来源称倍数被压到3.5x ARR以下）。[^l40-multiples][^eilla-multiples]
- **中国订阅制的口径陷阱**：中国SaaS/订阅公司普遍靠**预付年费+大促拉新**，把"合同负债（递延收入）"一次性收进现金流，再按月确认收入。促销冲量会制造"收入虚胖"：当期营收好看，但合同负债/确认收入的比值下降、次年续费缺口暴露，收入的"含金量"（现金先行 vs ARR确认）必须分层看。[^stripe-revrec][^paypro-deferred]
- **用户对订阅的抵抗在中国尤为尖锐**：长视频付费率仅约25–30%（爱奇艺/腾讯视频口径），涨价直接引发退订——爱奇艺2020–2022年三次提价后，2023Q4日均订阅会员1.003亿，同比流失约1170万人；"自动续费"在黑猫投诉平台相关投诉累计超21万条。[^woshipm-sub][^21jingji-iqiyi][^jfdaily-auto]
- **抽卡是替代订阅的中国本土解法**：原神"空月祝福"小月卡30元、立即返300原石+30天每日90原石，本质是把"日活跃度锁定"与"低门槛高频付费"缝合——它不是订阅（不自动续费、无履约义务、确认口径是游戏道具消耗而非递延收入），但用随机性奖励实现了比订阅更强的留存钩子与更高ARPU上限。[^taptap-genshin][^yicai-genshin]
- **并非所有业务都适合订阅制**：低频使用、价值感知一次性（如一次性工具、耐用品、单次交易型服务）强行订阅只会推高churn；Zuora官方即提示该模式并非放之四海皆准。反面对照是Costco：92.3%（美加）/89.8%（全球）的续费率（2025财年末）说明订阅只有在持续可感知的"划算"支撑下才成立。[^zuora-model][^costco-ar]

### Key Evidence

| 数据点 | 数值 | 时间 | 原文摘录(逐字) | 自评信度 | 来源 |
|---|---|---|---|---|---|
| 月churn转年churn公式 | 5%月流失≈46%年流失 | 2024前后 | "If the monthly rate is steady, use annual churn = 1 − (1 − monthly churn)^12. A 5% monthly churn rate is about 46% a year." | 高（公式为数学事实，多源一致） | [^thinkingai-churn] |
| churn对增长的压制（Skok） | 月流失5% vs 2.5% vs 负churn的60个月曲线对比 | 经典文（持续更新） | "Illustrates graphically why churn is a huge problem as a SaaS company gets larger. It also looks at a very surprising factor that can massively..."（指negative churn） | 高（一手VC经典文献） | [^skok-churn] |
| NRR<100%的估值惩罚 | 倍数常被压至3.5x ARR以下 | 2026-02 | "Multiple industry sources indicate that NRR below 100% triggers discounted pricing, often pushing multiples below 3.5x regardless of other..." | 中（二手行业分析，方向明确） | [^eilla-multiples] |
| SaaS资本指数倍数下行 | 16.9x(2021峰值)→约7x(2025初)→约3.1x(2026中) | 2026-09 | "The SaaS Capital Index peaked at 16.9x ARR in 2021. It entered 2025 at roughly 7x, then fell to a decade-plus low near 3.1x ARR by mid-2026" | 中 | [^l40-multiples] |
| 递延收入机制 | 递延收入=合同总价值−已确认收入；按月确认 | 2026-04/08 | "递延收入（合同负债）记录在资产负债表上……它每月确认1000美元的收入，并以相同金额减少递延收入。" | 高（会计准则通行做法） | [^stripe-revrec][^paypro-deferred] |
| 中国长视频付费率 | 爱奇艺≤25%、腾讯视频约30%（会员数/MAU口径） | 2024-12-31 | "如果用付费会员数/月活MAU，那么爱奇艺的用户付费率估算不超过25%，腾讯视频的用户付费率估算约30%" | 中（研究者估算） | [^woshipm-sub] |
| 爱奇艺涨价→退订 | 2023Q4日均会员1.003亿，同比少约1170万 | 2025-02-27 | "到2023年第四季度，其日均订阅会员数为1.003亿，同比上年度流失了约1170万人。" | 高（引用爱奇艺财报数据） | [^21jingji-iqiyi] |
| 爱奇艺三连涨幅度 | 月卡19.8→30元(+51%)，连续年卡178→238元(+34%) | 2020–2022三次提价 | "爱奇艺三次提价，月卡从19.8元涨到了30元，连续包年则从178元涨到238元，涨幅分别为51%和34%。" | 高 | [^cyzone-iqiyi] |
| 自动续费投诉 | 黑猫平台相关投诉约21万条；芒果TV+自动续费投诉4000多条 | 2026-01-19 | "隐蔽扣款取消难，21万条投诉直指'自动续费'陷阱……在黑猫投诉平台检索'芒果TV+自动续费'，相关投诉达4000多。" | 高（主流媒体调查） | [^jfdaily-auto] |
| 原神小月卡机制 | 空月祝福30元=300原石+30天×90原石 | 2024-04-08 | "小月卡是'空月祝福'，购买需要30块钱，立即获得300原石，之后30天每天给你90原石" | 高（玩家社区逐字核对） | [^taptap-genshin] |
| 原神吸金能力 | 上市30天移动端2.45亿美元(约16.54亿元) | 2020-11-08 | "据Sensor Tower商店情报数据显示，9月28日上市以来……在30天内吸金2.45亿美元（人民币16.54亿元）" | 高（Sensor Tower转引） | [^yicai-genshin] |
| Costco续费率 | 美加92.3% / 全球89.8% | 2025财年末（年报2025-12） | "Our member renewal rate was 92.3% in the U.S. and Canada and 89.8% worldwide at the end of 2025." | 高（一手年报） | [^costco-ar] |
| 订阅模式适用边界 | Zuora明示并非普适 | 2024-12-19 | "Note: this model is not suitable for enterprise software. Any business that doesn't factor in fixed and variable costs will never get its..." | 中（官方术语页表述混乱，仅取"非普适"结论） | [^zuora-model] |

[^thinkingai-churn]: How to Calculate Churn Rate With Examples. ThinkingAI博客, 约2024. https://thinkingai.io/blog/how-to-calculate-churn-rate
[^skok-churn]: David Skok. Why Churn is CRITICAL in SaaS / Unlocking the Path to Negative Churn. forEntrepreneurs. https://www.forentrepreneurs.com/why-churn-is-critical-in-saas/
[^eilla-multiples]: What Are SaaS Multiples in 2026? The Correction Explained. Eilla blog, 2026-02-27. https://blog.eilla.ai/what-are-saas-multiples-in-2026-the-correction-explained
[^l40-multiples]: SaaS Multiples 2026: The Real Private Range (4x to 9x ARR). L40, 2026-09-24. https://www.l40.com/insights/saas-multiples
[^stripe-revrec]: SaaS 收入确认：定义和最佳实践. Stripe资源页, 2026-08-21. https://stripe.com/zh-my/resources/more/a-guide-to-revenue-recognition-for-saas-businesses
[^paypro-deferred]: 什么是SaaS递延收入？计算与会计. PayPro Global, 2026-04-02. https://payproglobal.com/zh/解答/什么是saas递延收入
[^woshipm-sub]: 订阅制消费在中国为什么这么难？一个用户研究者的商业观察. 人人都是产品经理, 2024-12-31. https://www.woshipm.com/operate/6207278.html
[^21jingji-iqiyi]: 净利暴跌60%，爱奇艺扑街了？. 21经济网, 2025-02-27. https://www.21jingji.com/article/20250227/herald/fbc614e0401dfe2e5c6e75f578ba4f93.html
[^cyzone-iqiyi]: 爱奇艺，变了. 创业邦, 约2024. https://m.cyzone.cn/article/755054
[^jfdaily-auto]: 隐蔽扣款取消难，21万条投诉直指"自动续费"陷阱. 解放日报/上观, 2026-01-19. https://www.jfdaily.com/wx/detail.do?id=1054208
[^taptap-genshin]: 原神68元大月卡性价比分析. TapTap玩家帖子, 2024-04-08. https://www.taptap.cn/moment/526796842353036288
[^yicai-genshin]: 一天最高吸金9000万，《原神》背后的公司米哈游到底什么来头. 第一财经, 2020-11-08. https://www.yicai.com/news/100828967.html
[^costco-ar]: Costco Annual Report 2025. Costco Wholesale, 2025-12. https://s201.q4cdn.com/287523651/files/doc_financials/2025/ar/COST-Annual-Report-2025.pdf
[^zuora-model]: What Is a Subscription Business Model?. Zuora, 2024-12-19. https://www.zuora.com/glossary/subscription-business-model/

### Tensions & Counter-arguments

1. **"46%"的口径争议**：46%是按恒定月流失率复利算的**毛客户流失**；实践中SaaS更看**净收入留存（NRR）**——若扩张收入足够大，收入池可在客户数流失下仍正增长。因此"churn杀死一切"只在扩张引擎失效时成立；不能把客户churn与收入churn混为一谈（Skok原文区分了gross/negative churn）。
2. **年费预付≠收入虚胖的指控需分层**：会计上合同负债恰恰是**保守口径**（先收钱后确认），真正风险在促销折扣冲量后，次年确认收入基数抬升而续费现金跟不上——即"合同负债/营收"比值恶化才是预警信号，本身不是造假。批评者与辩护者对该口径的解读存在系统性分歧。
3. **抽卡并非"更好的订阅"的同构物**：抽卡收入确认走道具消耗/玩家时长路径，无自动续费契约，波动性远高于订阅（依赖版本节奏）；把它当作订阅的替代，会低估订阅模式在现金流可预测性上的优势。反过来说，抽卡的强制日活设计（每日90原石过期作废）恰恰是对"中国用户抵触自动续费"这一本土约束的绕行，而非否认。
4. **爱奇艺案例的双向解读**：涨价→会员流失可以读作"订阅抵抗"，也可读作内容质量（爆款缺位）驱动——2023年《狂飙》期间会员仍在涨。单一案例无法把流失归因于涨价本身。
5. **待证项**：金山办公等A股SaaS的合同负债余额趋势（2024–2025年报具体数字）未在本次检索中拿到逐字数据，建议下一步查巨潮资讯网年报原文核对"合同负债"科目；美年/用友/金蝶的具体NRR披露（多数A股公司不披露NRR，需用客户留存率或订阅收入占比代理）。
