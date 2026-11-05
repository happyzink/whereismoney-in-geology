## Dimension 04: 全球对照——美国平台的"生态税"

### Current State

- **苹果 30% 抽成的量级**：苹果不单独披露佣金收入，但官方口径显示 2024 年全球 App Store 生态促成开发者账单与销售 **1.3 万亿美元**，其中约 90% 的销售开发者**未支付任何佣金**[^apple-appstore-study][^macrumors-us406]；佣金主要来自数字商品内购（30%/15% 两档）。苹果服务业务整体收入 2024 财年约 960 亿美元量级（待证，见待证项），App Store 抽成是其中最大单项。
- **Epic 诉讼后的变化（分区域）**：2021 年美国加州北区法院判决本身未禁止抽成（"The injunction said nothing about commissions"[^oyez-epic]）；但 **2025 年 4 月 30 日法院认定苹果违反禁令、发出永久禁令**：美国区不得阻止开发者放外链/外按按钮，且不得对外链交易收佣金——美国区数字商品抽成实质被击穿[^cleverbridge-epic][^ca9-epic]。苹果上诉中（第九巡回法院 2025 年 12 月维持框架）[^ca9-epic]。
- **欧盟 DMA 路径**：苹果被迫允许第三方应用市场与网页分发，佣金结构改为：2025 年 6 月起以 **5% Core Technology Commission (CTC)** 取代此前的 Core Technology Fee[^apple-dev-eu][^apple-newsroom-eu]，即欧盟"降税换开放"，美国则"外链免税"——30% 基准全球不同区域已被蚕食出三个价。
- **谷歌给苹果的默认搜索费**：**属实，2022 年为 200 亿美元**（法院解封文件）[^slashdot-googleapple]；2025 年 9 月 2 日 Judge Mehta 补救裁决禁止排他协议但**明确允许继续付款**（"Exclusive contracts banned. Payments still allowed."[^sej-mehta]），即"谷歌税"得以延续，苹果每年继续收到约 200 亿美元量级的纯租金。
- **云锁定效应定价**：英国 CMA 认定**出口流量费（egress fees）、不兼容架构与限制性许可条款**共同构成云市场"lock-in"，并建议监管干预[^mogin-cma]；美国 FTC 自 2025-2026 年扩大对 Microsoft 云捆绑（Azure/Entra ID/Copilot）的反垄断调查[^windowsforum-ftc]。欧盟自 2024 年 1 月起要求转换期出口费降至"成本覆盖"水平（零毛利）[^distribuee-egress]——说明监管者已把锁定溢价识别为一种"生态税"。AWS/Azure 收入体量：2026 Q3 三大云合计季度收入约 1,100 亿美元（AWS 460 亿、Azure 332 亿、Google Cloud 307 亿）[^midgard-cloud]。
- **为什么美国平台更赚钱（机制层）**：苹果/谷歌向全球用户收租（1.3 万亿美元生态、200 亿美元搜索费为全球单一买家竞价结果），而中国头部平台收入基本来自单一市场；同等抽成率下，可寻址市场规模差异直接决定租金绝对量。市盈率/市值对比的精确数字本轮检索未能核实（见待证项），机制结论为高置信，具体倍数为待证。
- **中国平台出海的租金能力**：TikTok Shop 美区对多数订单收 **6% referral fee**（2024 年 7 月从 2% 上调后）[^growmojo-tiktok][^5x-tiktok]，欧洲 2026 年 1 月起新商家前两月 4% 后阶梯上调[^ced-tiktok]；Temu 未公开费表，第三方口径佣金约 **5%–20%**（按类目/卖家类型浮动，自营销低、平台代投流高）[^inriver-temu]；Shein 市场模式为**免月费 + 10% 固定佣金**（2025 年中口径）[^m2e-shein]。对照：TikTok Shop 美区费率已接近亚马逊平原类目佣金（8%–15%）的下沿并在上调通道中——中国平台出海后同样在建立"抽成阶梯"，但整体费率仍低于美国成熟平台，说明租金能力仍在爬坡期。

### Key Evidence

| 数据点 | 数值 | 时间 | 原文摘录(逐字) | 自评信度 | 来源 |
|---|---|---|---|---|---|
| App Store 生态规模 | $1.3 万亿 | 2024 | "global App Store ecosystem facilitated $1.3 trillion in developer billings and sales in 2024" | 高(苹果一手，转引自分析) | [^apple-appstore-study] |
| 美国区免佣比例 | 90% 无佣金 | 2024 | "U.S. App Store facilitated $406 billion in developer billings and sales in 2024, and for 90 percent of those sales, developers paid no commission" | 高(苹果一手，论坛转引) | [^macrumors-us406] |
| 谷歌付苹果搜索费 | $200 亿 | 2022 | "Alphabet paid Apple $20 billion in 2022 for Google to be the default search engine in the Safari browser, according to newly unsealed court documents" | 高(法院解封文件) | [^slashdot-googleapple] |
| Mehta 裁决处理 | 付款保留 | 2025-09-02 | "Exclusive contracts banned. Payments still allowed." | 高(判决报道) | [^sej-mehta] |
| Epic 禁令(美区) | 外链交易零佣 | 2025-04-30 | "a U.S. court permanently barred Apple from forcing developers to use its in-app purchase system" | 高(多源一致) | [^cleverbridge-epic] |
| 禁令范围界定 | 不涉佣金本身 | 2021 原禁令 | "The injunction said nothing about commissions." | 高(判例摘要) | [^oyez-epic] |
| 欧盟新佣金 | CTC 5% | 2025-06 / 2026-08 | "Apple will charge a 5 percent Core Technology Commission." | 高(苹果一手) | [^apple-newsroom-eu][^apple-dev-eu] |
| 云锁定三要素 | egress/架构/许可 | 2025-12 | "The CMA reported that egress fees, incompatible architectures, and restrictive licensing terms contribute to a 'lock-in' effect" | 中(律所转述 CMA) | [^mogin-cma] |
| 欧盟出口费上限 | 成本覆盖、零毛利 | 2024-01 起 | "switching fees (including egress charged during a provider switch) must be reduced to a 'cost-covering' rate — no margin" | 中(行业分析转述) | [^distribuee-egress] |
| 云季度收入 | AWS 460/Azure 332/GCP 307 亿美元 | 2026 Q3 | "AWS $46.0 billion, Azure $33.2 billion and Google Cloud $30.7 billion" | 中(二手汇总) | [^midgard-cloud] |
| TikTok Shop 美区佣金 | 6% | 2024-07 | "The current TikTok Shop Referral Fee rate is 6%" | 高(多源一致) | [^growmojo-tiktok][^5x-tiktok] |
| TikTok Shop 欧洲佣金 | 新商家 4%(前两月) | 2026-01-08 起 | "New merchants joining from 8 January will pay just 4% commission for their first two months" | 中(服务商博客) | [^ced-tiktok] |
| Temu 佣金区间 | 5%–20% | 2025 口径 | "the Temu seller commission rate applies to every sale, and this is typically at a rate of between 5% and 20%" | 中(第三方，官方无费表) | [^inriver-temu] |
| Shein 佣金 | 10% 固定 | 截至 2025-06-30 | "no monthly fees and a flat 10% commission after an initial free period" | 中(第三方文档) | [^m2e-shein] |
| FTC 查微软云捆绑 | 扩大调查 | 2026-02 | "The Federal Trade Commission has quietly escalated a wide-ranging antitrust inquiry into Microsoft, issuing civil investigative demands" | 中(行业媒体) | [^windowsforum-ftc] |

### Tensions & Counter-arguments

1. **"1.3 万亿"≠租金基数**：苹果口径的 1.3 万亿包含电商实物销售等抽成外交易，官方同时强调 90% 销售零佣金——用生态规模乘以 30% 会严重高估苹果租金；真实佣金基数仅数字商品内购（估算需第三方如 Sensor Tower，本轮未取得，待证）。
2. **Epic 判决的"变化"被双方各自夸大**：苹果称"生态将崩"，开发商实测发现苹果仍可在链路设置摩擦；且禁令仅限美国区、欧盟是另一套 CTC 5% 体系，全球 30% 基准在多数区域仍有效——"30% 已死"是过度结论。
3. **200 亿美元搜索费是 2022 年数字**：2023-2025 年实际支付额更高（按 ISA 结构随 Safari 流量增长），但无解封文件支持，引用时必须带时间窗，不能说"现在每年 200 亿"。
4. **云锁定溢价的反方**：egress 费有降价记录（2024 年 3 月三大云同步下调），锁定更多来自数据引力/技能栈而非显性定价；CMA 干预建议落地程度未定。
5. **中美估值差**："美国平台更赚钱"在租金绝对量上成立，但中国平台以更低的抽成率换取增长（拼多多千亿扶持即主动退租），估值差可能反映风险溢价（地缘/监管）而非盈利能力差距；本轮未能核实市值倍数，不对此下硬结论。
6. **中国出海平台费率**：Temu 的 5%–20% 区间来自第三方推断（官方无费表），且全托管模式下"佣金"与"采销价差"不可分，口径与 TikTok Shop 的 referral fee 不完全可比。

[^apple-appstore-study]: App Store Study (Apple, 转引于 mjtsai.com). 2025-07-18. https://mjtsai.com/blog/2025/07/18/app-store-study-shows-90-of-what
[^macrumors-us406]: MacRumors: U.S. App Store Ecosystem Facilitated $406 Billion in 2024. 2025-05-29. https://forums.macrumors.com/threads/u-s-app-store-ecosystem-facilitated-406-billion-in-sales-in-2024-up-from-142-billion-in-2019.2457878
[^oyez-epic]: Oyez: Apple Inc. v. Epic Games, Inc. (案卷摘要). https://www.oyez.org/cases/2026/25-1311
[^cleverbridge-epic]: cleverbridge: Apple vs. Epic — A Legal Turning Point (2025-04-30 禁令). https://grow.cleverbridge.com/blog/apple-vs-epic-a-legal-turning-point
[^ca9-epic]: Ninth Circuit opinion, Epic Games Inc v Apple Inc (25-2935). 2025-12-11. https://cdn.ca9.uscourts.gov/datastore/opinions/2025/12/11/25-2935.pdf
[^apple-newsroom-eu]: Apple Newsroom: Apple announces changes for apps in the European Union. 2026-08-18. https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union
[^apple-dev-eu]: Apple Developer Support: Changes for apps in the European Union. https://developer.apple.com/support/apps-in-the-eu
[^slashdot-googleapple]: Slashdot/ court documents: Google's Payments To Apple Reached $20 Billion in 2022. 2024-05-02. https://apple.slashdot.org/story/24/05/02/1320207/googles-payments-to-apple-reached-20-billion-in-2022-antitrust-court-documents-show
[^sej-mehta]: Search Engine Journal: Google's Antitrust Ruling — What The Remedies Really Mean. 2025-09-08. https://www.searchenginejournal.com/googles-antitrust-ruling-what-the-remedies-mean-for-search-seo-and-ai-assistants/555086
[^mogin-cma]: Mogin Law: Are Clouds Too Sticky? Antitrust Authorities Probe Lock-in (CMA 结论转述). 2025-12-15. https://moginlawllp.com/global-antitrust-cloud-investigations-target-amazon-google-microsoft
[^distribuee-egress]: Distribuee: AWS Egress Fees — Mapping and Cutting Your Data Transfer. 2026-08-26. https://distribuee.com/en/insights/aws-data-transfer-egress-costs
[^midgard-cloud]: Midgard Finance: AWS vs Azure vs Google Cloud — Revenue and Market Share (2026 Q3). https://www.midgardfinance.com/research/cloud
[^windowsforum-ftc]: WindowsForum: FTC Ramps Up Microsoft Antitrust Probe on Cloud & AI. 2026-02-16. https://windowsforum.com/news/ftc-ramps-up-microsoft-antitrust-probe-on-cloud-licensing-and-ai-bundling.401440
[^growmojo-tiktok]: GrowMojo: A Deep Dive Into Sellers Fees for TikTok Shop in the U.S. 2024-07-25. https://growmojo.com/a-deep-dive-into-sellers-fees-for-tiktok-shop-in-the-u-s
[^5x-tiktok]: 5xdashboard: TikTok Shop Seller Fees — Full Cost Breakdown Per Order. 2026-10-07. https://5xdashboard.com/blog/tiktok-shop-seller-fees
[^ced-tiktok]: CedCommerce: TikTok Shop Raises Seller Fees Across Europe. 2025-12-12. https://cedcommerce.com/blog/tiktok-shop-raises-seller-fees-across-europe-as-platform-pushes-for-content-driven-commerce-expansion/
[^inriver-temu]: inRiver: Selling on Temu — Requirements, Fees & Commission Rates. https://www.inriver.com/resources/what-to-know-about-temu
[^m2e-shein]: M2E Cloud: Understanding Shein Marketplace Fees and Commission (费率截至 2025-06-30). https://docs.m2ecloud.com/docs/understanding-shein-marketplace-fees-and-commission

### 待证项

- **苹果佣金收入的绝对额估算**（如"App Store 年佣金约 250-350 亿美元"类估算）：需查 Sensor Tower/分析机构原始报告，而非苹果生态宣传口径。
- **苹果服务分部收入 FY2024/FY2025 精确值**：本轮检索未命中一手财报页，应查 Apple 10-K（services segment net sales）。
- **中美平台市值/市盈率倍数**：三轮检索均空结果（关键词过窄），建议用 Yahoo Quantum/公司财报页直接取数：Apple、Microsoft、Alphabet vs 腾讯(0700.HK)、阿里(9988.HK)、拼多多(PDD)在统一日期快照下的市值与经营利润率。
- **谷歌向苹果付款的 2023-2025 年实际额**：待 Mehta 案后续解封文件或苹果 10-K 风险披露。

### 建议的下一步

用 companiesmarketcap.com 或各财报页取统一日期的中美六平台市值+经营利润率快照表，补齐④的定量口径；再核苹果 10-K services 分部数字，把"生态税总账"从定性升级为可加总的量级。
