# Dimension 01: SaaS三指标与估值溢价

## Dimension 01: SaaS三指标与估值溢价

### Current State

- **ARR（年度经常性收入）**：把订阅合同金额按年化口径确认的经常性收入指标，衡量"收入机器"的规模。口径上区分**收入确认口径ARR**（会计上分期确认）与**现金流口径**（当期实际收款的订阅现金流）；中国厂商（金蝶）按"订阅或长期承诺的年化经常性收入"自行定义[^sina-kingdee-report]。金山办公年报不披露严格意义的ARR，只披露个人/订阅业务收入与月活设备数——口径错位是中美SaaS对比的常见陷阱[^cls-kingsoft][^sina-kingsoft-ar]。
- **NRR（净收入留存率，Net Revenue Retention）**：期初同一批客户（不含新客）期末收入 ÷ 期初收入，含增购、扩容与降级、流失。美股经验基准：NRR≥110%为优秀线，这类公司群组的增速高于全体样本中位数[^saas-capital-nrr]；NRR 110%→120%每提升10个点，估值可提升20–30%[^m3ter-nrr]。
- **Churn（流失率）**：客户数或收入口径的年流失。美股SaaS 2025年**收入流失率中位数12.50%，前25%优秀线为年流失<5.48%**[^crv-churn]。注意高NRR与低流失可以并存——大客增购会掩盖中长尾流失，需拆开看。
- **Rule of 40**：收入增速% + 利润率%（EBITDA或FCF口径）≥ 40%。实操中"NRR>110% 且 Rule of 40>40"是拿到溢价倍数的门槛[^l40-multiples]；美股SaaS估值区间约4x–9x ARR，NRR>110%的组合落在区间顶端，弱NRR（<100%）即使Rule of 40达标也只拿到低于市场的倍数[^livmo-rule40]——这就是"NRR>110%估值翻倍"的机制版本：不是NRR单独翻倍，而是**高NRR把倍数从区间底部（~4x）抬到顶部（~9x），量级上接近翻倍**[^l40-multiples][^saasvaluationmultiple]。Bessemer发布的上市SaaS平均收入倍数为9.0x（2026-10-27抓取，均值非中位数，被少数高倍数拉高）[^saasvaluationmultiple]。
- **中国三大SaaS（2025年报/半年报口径）**：金山办公2025年营收59.29亿元（+15.78%），归母净利18.36亿元（+12%），国内WPS个人业务收入33.44亿元（+7.87%）——**盈利最好但个人订阅增速已回落到个位数**[^cls-kingsoft]；金蝶2025H1云服务ARR 37.3亿元（+18.5%）[^sina-kingdee-report]；用友2025年收入正增长但"增速不高"，因更大力度推进订阅模式转型，2025H1云服务收入27.63亿元、占营收77.2%，Q2云收入同比仅+8.2%——**转订阅正在用短期收入增速换长期经常性**[^sina-yonyou-forecast][^sina-yonyou-h1]。
- **中国SaaS难赚钱的三重解释**：①付费意愿——中国企业为软件付费的习惯弱，标准化服务价值感知低[^qq-saas]；②定制化陷阱——中国缺乏标准化工作流程规范，SaaS标准化产品被迫做项目制定制，毛利与复用度双降[^qq-saas]；③销售驱动vs产品驱动——过去十年"钱多+商业化顺序搞反"，靠销售堆增长而非产品自传播，导致获客成本高、NRR做不起来[^36kr-1600yi]。机制层交叉印证：三因素共同压制NRR与毛利率，而美股溢价恰恰建立在高NRR×标准化产品上（见上两条）。
- **AI订阅涨价的市场反应（微软Copilot/Adobe）**：微软365 Copilot定价$30/用户/月（叠加在M365订阅之上），分析师长期评价采用偏慢，到2026年4月才有"企业客户采用激增"的报道——涨价成功与否取决于AI功能的可感知ROI[^tikr-copilot][^coworker-copilot]；Adobe于2025-06-17（北美续约日起）对个人版Creative Cloud涨价，部分计划涨幅最高16.7%（$59.99档）[^adobe-helpx][^livingstone-adobe]，用户端接受度高（续约自动执行），但资本市场2025年对Adobe的主导叙事是AI竞争担忧，股价自2025年初一度下跌约40%——**涨价本身未引发流失危机，估值压力来自AI替代叙事而非订阅模式失效**[^leverageshares-adobe]。
- **对照锚点（美股）**：Salesforce在FY2026 Q1（2025-05-28电话会）披露Data Cloud and AI ARR同比增长超过120%[^fortune-sfdc]，FY2026 Q3 Data 360 ARR近14亿美元、同比+114%[^futurum-sfdc]——美股头部SaaS的AI增购正在把NRR逻辑再放大一轮，而中国三家尚无同量级的AI-ARR披露。

### Key Evidence

| 数据点 | 数值 | 时间 | 原文摘录(逐字) | 自评信度 | 来源 |
|---|---|---|---|---|---|
| SaaS收入流失率中位数 | 12.50%/年 | 2025年 | "SaaS companies sits at 12.50 percent in 2025 . Performers in the top 25 percent hold annual revenue churn below 5.48 percent." | 高 | [^crv-churn] |
| NRR优秀线与增速关系 | NRR≥110% | 2025-09 | "The growth rates for groups of companies with NRR of at least 110 % were higher than the population median" | 高 | [^saas-capital-nrr] |
| NRR对估值的弹性 | NRR+10pt→估值+20–30% | 2026-02 | "A 10-point lift in NRR (from 110 % to 120%) can translate to a 20-30% increase in valuation" | 中 | [^m3ter-nrr] |
| Rule of 40与溢价门槛 | NRR>110% 且 Ro40>40 | 2026-09 | "Rule of 40 is the sum of revenue growth rate and EBITDA margin. NRR above 110% and Rule of 40 above 40 are the practical thresholds for premium" | 中 | [^l40-multiples] |
| 弱NRR折价 | 倍数低于市场 | 2026-02 | "companies with Rule of 40 scores above 40% but weak net revenue retention (below 100%) still received below-market multiples" | 中 | [^livmo-rule40] |
| Bessemer上市SaaS收入倍数 | 9.0x（均值） | 2026-10-27抓取 | "Bessemer publishes an average revenue multiple (9.0x as fetched 27 October 2026), not a median" | 中 | [^saasvaluationmultiple] |
| 金山办公2025年营收/净利 | 59.29亿元 +15.78%；净利18.36亿元 +12% | 2026-03-25（2025年报） | "实现营业收入59.29亿元，同比增长15.78%；归属于母公司所有者净利润18.36亿元" | 高 | [^cls-kingsoft] |
| 金山办公个人订阅收入 | 国内WPS个人业务33.44亿元 +7.87% | 2025年报 | "国内 WPS 个人 业务 收入 33.44亿元，同比增长7.87%" | 高 | [^cls-kingsoft] |
| 金山办公月活设备 | PC端3.29亿 +13.18%；移动端3.49亿 +2.28% | 2025年报 | "设备数 3.29亿，同比增长13.18%，移动版月度活跃设备数 3.49亿，同比增长2.28%" | 高 | [^cls-kingsoft] |
| 金蝶云服务ARR | 37.3亿元 +18.5%（2025H1）；2024年ARR占总收入54.83% | 2025-12-23 | "2025H1公司 ARR 达37.3 亿元，同比增长18.5%，2024 年 ARR 占公司总收入比重达54.83%" | 中高（券商研报转述） | [^sina-kingdee-report] |
| 用友2025年收入指引 | 收入正增长、增速不高 | 2026-01-14（业绩预告） | "尽管公司2025年度收入实现正增长……同时更大力度推进向订阅业务模式转型，导致全年收入增速不高" | 高 | [^sina-yonyou-forecast] |
| 用友2025H1云服务收入 | 27.6335亿元，占营收77.2%；Q2云收入+8.2% | 2025-08-27（半年报） | "公司云服务业务实现收入276,335万元，占营业收入达77.2%……第二季度云服务业务实现收入171,583万元，同比增长8.2%" | 高（一手定期报告） | [^sina-yonyou-h1] |
| Salesforce Data Cloud & AI ARR增速 | 同比>120% | 2025-05-28（FY26Q1电话会） | "Data cloud and ARR grew more than 120 % year over year" | 高（管理层电话会原话转写） | [^fortune-sfdc] |
| Salesforce Data 360 ARR | 近14亿美元，同比+114% | 2025-12-05（FY26Q3） | "hitting nearly $1.4 billion in ARR —an explosive 114% year-over-" | 中（二手分析） | [^futurum-sfdc] |
| M365 Copilot定价 | $30/用户/月（叠加M365之上） | 2026-04-05报道 | "The product costs $30 per month on top of existing Microsoft 365" | 高（定价为官方口径） | [^tikr-copilot] |
| Adobe个人版涨价 | 2025-06-17起，部分计划涨幅至16.7%（$59.99档） | 2025-06生效 | "Customers will be charged the updated price on their next monthly or annual renewal date on or after June 17, 2025 for North America" | 高（Adobe官方帮助页） | [^adobe-helpx] |
| Adobe股价承压 | 自2025年初约-40%，主因AI担忧 | 2025-10-02 | "Down 40% on AI Fears, Can Adobe Stock Recover?" | 中（二手，跌幅口径未独立核算） | [^leverageshares-adobe] |
| 中国SaaS付费意愿/定制化解释 | 定性 | 2023-11-03 | "我国没有形成标准的工作流程和规范，SaaS标准化的服务无法真正发挥作用" | 中 | [^qq-saas] |
| 中国SaaS销售驱动解释 | 定性 | 2023-09-18 | "过去十年SaaS为什么在中国水土不服？因为有两个特定因素让中国SaaS很难逃出把商业化顺序搞反的宿命" | 中 | [^36kr-1600yi] |

### Tensions & Counter-arguments

1. **"NRR>110%估值翻倍"是机制近似，不是精确定律**：一手级研究只支持"NRR每+10pt→估值+20–30%"（m3ter，二手汇总）与"高NRR组合落在4x–9x区间顶部"（区间底部到顶部≈2.25x）；"翻倍"表述在倍数区间两端成立，但样本为上市/退出公司，存在幸存者偏差，不能外推到未盈利中国SaaS。[^m3ter-nrr][^l40-multiples][^saasvaluationmultiple]
2. **中美口径错位**：金山办公不披露ARR，只有"个人/订阅业务收入"（收入确认口径，含一次性买转订阅部分），与金蝶自报ARR（年化口径）、美股合规披露的NRR不可直接比；本文所有对比均已标注口径，读者不应把金山33.44亿个人收入当作ARR。[^cls-kingsoft][^sina-kingdee-report]
3. **用友金蝶的"订阅转型"与"当期利润"互相挤压**：用友业绩预告明说转订阅压低当期收入增速；金蝶仍处微利/盈亏平衡边缘（2024年预测净利-0.98~0亿元）。中国SaaS不是"不转"，而是转型的收入代价更大——反向观点认为问题在客户结构（大客户定制占比高），而非模式本身。[^sina-yonyou-forecast][^sina-kingdee-forecast]
4. **Adobe案例的反向解读**：若把Adobe股价-40%归因于"订阅涨价失败"是误读——涨价于2025-06自动续约执行、未见流失数据恶化，股价压力主因是AI生成工具对其创意软件护城河的替代担忧。订阅涨价的市场反应要区分"用户反应"（接受）与"投资者反应"（担忧AI替代）。[^adobe-helpx][^leverageshares-adobe]
5. **Copilot"采用慢"叙事正在反转中**：2024–2025年分析师普遍认为$30定价采用不及预期，2026年4月出现采用激增报道，但缺少可核对的席位数字；"AI叠加订阅=顺利涨价"的结论尚不稳固，标注为低置信待证。[^tikr-copilot][^coworker-copilot]
6. **待证项**：①金山办公2025年是否在年报中披露WPS AI相关ARR/付费用户数的严格口径（建议直接读年报全文PDF第4–5节经营分析）；②用友2025全年云收入终值（年报预计2026年3–4月披露，本文只有H1+预告）；③M365 Copilot席位/收入的一手披露（微软财报电话会）；④"NRR>110%公司EV/ARR倍数vs<100%公司"的量化对照表（建议查Bessemer State of the Cloud或KeyBanc SaaS Survey原始PDF）。

---

[^saas-capital-nrr]: What is a Good Retention Rate for a Private SaaS Company. SaaS Capital. 2025-09-18. https://www.saas-capital.com/blog-posts/what-is-a-good-retention-rate-for-a-private-saas-company
[^crv-churn]: SaaS Churn Rate Benchmarks for Investors (2026). CRV. 2026-06-19. https://www.crv.com/content/saas-churn-rate
[^m3ter-nrr]: Net Revenue Retention and SaaS Valuations: 2026. m3ter. 2026-02-17. https://www.m3ter.com/blog/net-revenue-retention
[^l40-multiples]: SaaS Multiples 2026: The Real Private Range (4x to 9x ARR). L40. 2026-09-24. https://www.l40.com/insights/saas-multiples
[^livmo-rule40]: Why the Rule of 40 Is Wrong for Most SaaS Exits. Livmo. 2026-02-18. https://livmo.com/blog/rule-of-40-saas-valuation
[^saasvaluationmultiple]: Three Indices, One Story Now: SaaS Capital 4.2x, Aventis 4.6x. saasvaluationmultiple.com. 2026-10抓取. https://saasvaluationmultiple.com/three-indices
[^cls-kingsoft]: 金山办公2025年净利同比增12% WPS AI月活同比增长超3倍. 财联社. 2026-03-25. https://www.cls.cn/detail/2324910
[^sina-kingsoft-ar]: 金山办公：2025年年度报告. 新浪财经公告. 2026-03-26. https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=688111&id=12019050
[^sina-kingdee-report]: 2025年金蝶国际公司研究报告：企业SaaS服务领军者，AI赋能. 新浪财经（券商研报转载）. 2025-12-23. https://finance.sina.com.cn/stock/relnews/hk/2025-12-23/doc-inhcuuni5242181.shtml
[^sina-kingdee-forecast]: 金蝶国际：预计3月17日公布年报，预测全年营业收入64.50~65.54亿元. 新浪财经. 2025-03-11. https://finance.sina.com.cn/stock/relnews/hk/2025-03-11/doc-inephwwc8510705.shtml
[^sina-yonyou-forecast]: 用友网络：2025年年度业绩预告. 新浪财经公告. 2026-01-14. https://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=600588&id=11913202
[^sina-yonyou-h1]: 用友网络科技股份有限公司2025年半年度报告. 巨潮/新浪财经PDF. 2025-08-27. http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESH_STOCK/2025/2025-8/2025-08-27/11369705.PDF
[^fortune-sfdc]: Salesforce (CRM) Q1 2026 Earnings Call Transcript. Fortune. 2025-05-28. https://fortune.com/company/salesforce-com/earnings/q1-2026
[^futurum-sfdc]: Salesforce Q3 FY 2026: AI Agents, Data 360 Lift Bookings and FY26 Outlook. Futurum Group. 2025-12-05. https://futurumgroup.com/insights/salesforce-q3-fy-2026-ai-agents-data-360-lift-bookings-and-fy26-outlook
[^tikr-copilot]: Microsoft Reports Surge in Copilot AI Adoption Among Business Clients. TIKR. 2026-04-05. https://www.tikr.com/blog/microsoft-nasdaq-stock-reports-surge-in-copilot-ai-adoption-among-business-clients
[^coworker-copilot]: Microsoft Copilot Enterprise Pricing 2026. coworker.ai. 2026-07-16. https://coworker.ai/blog/microsoft-copilot-enterprise-pricing
[^adobe-helpx]: Changes to Creative Cloud for individuals plans including pricing. Adobe官方帮助中心. 2026-02-12更新（涨价2025-06-17生效）. https://helpx.adobe.com/account/individual/subscriptions-and-plans/plan-types-and-eligibility/changes-to-individual-plan.html
[^livingstone-adobe]: Adobe's Creative Cloud price hike - what you need to know. Livingstone. 2025. https://blog.livingstone-tech.com/en/knowledge/adobes-creative-cloud-price-hike-what-you-need-to-know
[^leverageshares-adobe]: Down 40% on AI Fears, Can Adobe Stock Recover? Leverage Shares. 2025-10-02. https://leverageshares.com/us/insights/down-40-on-ai-fears-can-adobe-stock-recover
[^qq-saas]: 中国SaaS行业为啥这么难？路在何方？. 腾讯新闻. 2023-11-03. https://news.qq.com/rain/a/20231103A07AH900
[^36kr-1600yi]: 投了1600亿，中国SaaS没赚到认知以外的钱. 36氪. 2023-09-18. https://m.36kr.com/p/2438398997508359
