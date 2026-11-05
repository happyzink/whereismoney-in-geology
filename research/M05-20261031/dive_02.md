## Dimension 02: 会员制消费订阅的经济账

### Current State

- Costco 是「会员费≈利润」的经典样本：FY2024 会员费收入 48.28 亿美元、净利润 73.67 亿美元，会员费/净利润 ≈ 65%；FY2025 进一步增至 53 亿会员费 vs 81 亿净利润，比例仍约 65%。也就是说，商品零售基本只赚「流量」，利润几乎全部来自会员费这一笔预收现金流。[^cost-10k] [^cost-ar2025] [^21jingji-costco]
- Costco 2024 年 9 月首次（自 2017 年以来）上调会员费：个人/商业卡 $60→$65，执行会员 $120→$130，印证其敢提价是因为续卡意愿极高、会员费需求近乎无弹性。[^retaildive-costco]
- 中国会员制的钱流同样成立但口径不同：山姆中国 2024 年 11 月会员数达 860 万，按最低 260 元年费计算仅会员费收入就超 22 亿元；京东 PLUS 截至 2024Q4 末突破 3400 万，按年费约 99 元估算会员费盘子约 30 亿元级别，但电商付费会员是「引流+复购」逻辑，会员费本身不等于利润。[^sina-sams] [^cbndata-jd]
- 视频平台是涨价与会员数下滑的分化现场：爱奇艺会员业务营收连续 4 个季度下滑，且已连续一年不再披露日均订阅会员数——付费墙提价的红利被内容拉新乏力抵消。[^163-iqiyi]
- 订阅疲劳有量化证据：Deloitte 2024 调查显示美国家庭平均每月花 61 美元订 4 个 SVOD 服务；Bango 2024 年调查（含台湾地区）显示超 64% 受访者认为订阅服务已经太多、近三成难以掌握订阅支出；第三方汇编称 87% 的 Z 世代流媒体订户报告订阅疲劳、37% 曾因此退订。[^deloitte-svod] [^bango-tw] [^readless-stats]
- 流媒体行业月度退订率（churn）普遍在 5% 上下，Netflix 最低：截至 2024 年 9 月毛流失率 1.8%、净流失率 1.0%（Antenna 估算）——内容护城河直接体现在退订率上。[^antenna-churn]
- 汽车订阅是「订阅化失败」的代表案例：沃尔沃 2024 年 9 月叫停 Care by Volvo 汽车订阅业务，仅表示要「专注于核心客户服务……提高运营效率」；蔚来则走另一条路——BaaS 电池按月租用 + 悦享出行按月订阅整车 + 智驾订阅，把「非车收入」订阅化而非整车订阅。[^sina-volvo] [^nio-baas] [^nio-subscription]
- 新消费的「会员化」不是预收会员费，而是把用户变成可反复触达的私域资产：霸王茶姬注册会员从 2023 年底 6940 万增至 2024 年底超 1.77 亿（招股书口径），2025Q1 达 1.924 亿——它的收入仍来自单杯消费，会员体系提升的是复购频次而非锁定的年费。[^xinhua-chagee] [^ofweek-chagee]
- 定价心理学机制：预付年费同时利用了沉没成本效应（已付成本扭曲后续使用决策）与「支付解耦」（mental accounting，把一次大额支付摊薄到 365 天，后续每次消费感觉「免费」），加上取消时点的支付疼痛被推迟到下一年，三重机制共同锁定用户。[^thaler-prepay] [^decisionlab-ma]

### Key Evidence

| 数据点 | 数值 | 时间 | 原文摘录(逐字) | 自评信度 | 来源 |
|---|---|---|---|---|---|
| Costco FY2024 会员费收入 | $4,828M | FY2024（截至2024-09-01） | "Membership fee revenue increased 5% to $4,828" | 高（SEC 10-K 一手） | [^cost-10k] |
| Costco FY2024 净利润 | $7,367M（推算占比≈65.5%） | FY2024 | 检索未直接命中原文数字，10-K 报表口径，widely reported | 高（一手报表，摘录待核） | [^cost-10k] |
| Costco FY2025 会员费/净利润 | 53 亿 / 81 亿美元（≈65%） | FY2025（2025-12年报） | "Net income was $8.1 billion, or $18.21 per diluted share, an increase of 10%. Revenue from membership fees increased by 10% to $5.3 billion" | 高（年报PDF一手） | [^cost-ar2025] |
| Costco FY2025Q3 会员费/净利润比 | ≈65% | 2025Q3（2025-06报道） | "净利润19亿美元，同比增长13.7%；会员费收入12.4亿美元，同比增长10.7%，占净利润的比重达65%" | 高（财经媒体引财报） | [^21jingji-costco] |
| Costco 会员费提价 | $65 / $130 | 2024-07宣布、2024-09-01生效 | "individual and business members in the U.S. and Canada will pay $65 — $5 more. Executive membership will be $130, or $10 more per year" | 高（行业媒体引公司公告） | [^retaildive-costco] |
| 山姆中国会员数与会员费收入 | 860 万 / >22 亿元 | 截至2024-11中旬 | "会员数量增至860万，按最低260元年费计算，仅会员费收入就超过22亿元" | 中高（媒体引CEO访谈） | [^sina-sams] |
| 山姆普通会员续卡率 | ≈70%（普通卡） | 2023年口径 | "2023年中国年费260元的普通会员续卡率约为70%，而年费为680元的…"（摘录截断，高卡数字未完整命中） | 中（二手转述，需溯源至山姆官方） | [^sohu-sams] |
| 京东 PLUS 会员数 | >3400 万 | 截至2024Q4末 | "公开数据显示，截至2024年四季度末，京东PLUS会员人数也已突破3400万" | 中（二手引公开数据） | [^cbndata-jd] |
| 爱奇艺会员业务下滑 | 连续4个季度营收下滑 | 2025-02报道 | "最近4个季度，爱奇艺会员业务营收持续下滑"；"这项数据已经连续缺失了一整年" | 中（财经自媒体财报整理，方向与财报一致） | [^163-iqiyi] |
| 美国家庭 SVOD 订阅量与支出 | 4 个 / $61每月 | 2024-03调查 | "On average, US subscribing households spend US$61 per month on four SVOD services" | 高（Deloitte 一手调查） | [^deloitte-svod] |
| 订阅疲劳比例 | >64% 认为订阅太多 | 2024-10（Bango调查） | "超过64%的受访者认为目前已有太多的选择"、近三成难以掌握支出 | 中高（Bango官方新闻稿转述） | [^bango-tw] |
| Netflix 退订率 | 毛流失1.8% / 净流失1.0% | 截至2024-09 | "as of September 2024 Netflix has the lowest Churn Rates with 1.8% Gross Churn and 1.0% Net Churn, according to Antenna estimates" | 高（Antenna 一手估算） | [^antenna-churn] |
| Z世代订阅疲劳 | 87% 报告疲劳 / 37% 曾退订 | 2026-02汇编（含Bango 2025数据） | "87% of Gen Z streaming subscribers report fatigue and 37% canceled at…" | 低-中（二手汇编，需回溯原始调查） | [^readless-stats] |
| 沃尔沃停止汽车订阅 | 业务叫停 | 2024-09-15报道 | "沃尔沃方面并没有明确给出停止订阅服务的原因，只是表示此举是为了'专注于核心客户服务、即将推出的新产品，以及提高运营效率'" | 高（IT之家经新浪转载） | [^sina-volvo] |
| 霸王茶姬注册会员 | 1.77 亿（2024年底）/ 1.924 亿（2025Q1） | 2024底/2025Q1 | "截至2024年底，霸王茶姬拥有超1.77亿注册会员，该数据在2023年还仅为6940万"；"一季度小程序注册会员数达到1.924亿" | 高（新华网引招股书 + 媒体引财报） | [^xinhua-chagee] [^ofweek-chagee] |
| 预付偏好的理论解释 | 沉没成本/双通道心理账户 | 学术文献（2012综述） | "关于个体的预付偏好, 很多学者从沉没成本的角度也提出了解释" | 高（心理学报一手综述） | [^thaler-prepay] |

**引用源定义**

[^cost-10k]: Costco Wholesale 10-K FY2024. 2024-10. https://www.sec.gov/Archives/edgar/data/909832/000090983224000049/cost-20240901.htm
[^cost-ar2025]: Costco Annual Report 2025. 2025-12. https://s201.q4cdn.com/287523651/files/doc_financials/2025/ar/COST-Annual-Report-2025.pdf
[^21jingji-costco]: 21世纪经济报道《开市客2025财年第三财季营收净利双增》. 2025-06-01. https://m.21jingji.com/article/20250601/herald/8c68b4aaed94eb2bdd3dc64d78a2c607_zaker.html
[^retaildive-costco]: Retail Dive "Costco to raise membership fee for the first time since 2017". 2024-07-11. https://www.retaildive.com/news/costco-raise-membership-fee/721087
[^sina-sams]: 新浪财经《今年有望突破900亿美元！山姆CEO谈成功秘诀》. 2024-12-21. https://finance.sina.com.cn/tech/roll/2024-12-21/doc-ineacxhi5503878.shtml
[^sohu-sams]: 搜狐《销售额超千亿！山姆会员店如何用"极致性价比"重塑消费心智》. 2025-02-26. https://www.sohu.com/a/863865513_121123909
[^cbndata-jd]: CBNData《花钱买不来体验，会员制沦为"割韭菜神器"？》. 2025-10-22. https://www.cbndata.com/information/294583
[^163-iqiyi]: 数读社（网易号）《会员收入连降4季度，爱奇艺梦碎"中国奈飞"》. 2025-02-26. https://www.163.com/dy/article/JP9KM9VD05568W0A.html
[^deloitte-svod]: Deloitte Insights "Customization and personalization lead the SVOD revolution" (Digital Media Trends 2024). 2024-03-20. https://www.deloitte.com/us/en/insights/industry/technology/digital-media-trends-consumption-habits-survey/2024/customization-and-personalization-lead-the-svod-revolution.html
[^bango-tw]: Bango 新闻稿（台湾，GlobalPR发布）《「订阅疲劳」趋势袭台》. 2024-10-08. https://globalpr.agency/cn/press-room/bango/press-releases/article/訂閱疲勞趨勢襲台
[^readless-stats]: Read Less "Subscription Fatigue Statistics (35+ Sourced Stats)". 2026-02-14. https://www.readless.app/blog/subscription-fatigue-statistics-2026
[^antenna-churn]: Antenna "2024 Top Subscription Insights: Net Churn". 2024. https://www.antenna.live/insights/antennas-2024-top-subscription-insights-net-churn
[^sina-volvo]: 新浪科技/IT之家《告别"月付汽车"：沃尔沃叫停汽车订阅业务》. 2024-09-15. https://finance.sina.com.cn/tech/digi/2024-09-15/doc-incpfxph0481980.shtml
[^nio-baas]: NIO蔚来官网《蔚来BaaS底层逻辑详解》. 2026-08-13. https://www.nio.cn/smart-technology/20260813001
[^nio-subscription]: 蔚来悦享出行官网页面（汽车订阅服务）. 访问于2026-11-01. https://www.nio.cn/subscription
[^xinhua-chagee]: 新华网《霸王茶姬何以冲刺"新茶饮美股第一股"》. 2025-04-01. http://www.xinhuanet.com/food/20250401/bf5c8e4c7bd1446daf8072ced54ee97f/c.html
[^ofweek-chagee]: OFweek《上市后首次交卷，霸王茶姬如何做一个懂用户的茶饮品牌？》. 2025-06-03. https://mp.ofweek.com/Internet/a556714384587
[^thaler-prepay]: 李爱梅等《消费者决策分析的新视角：双通道心理账户理论》，《心理学报》. 2012. https://journal.psych.ac.cn/xlkxjz/CN/article/downloadArticleFile.do?attachType=PDF&id=2733
[^decisionlab-ma]: The Decision Lab "Mental Accounting". 2019-08-16. https://thedecisionlab.com/biases/mental-accounting

### Tensions & Counter-arguments

1. **「会员费=利润」的因果方向存在争议**：另一派观点认为 Costco 的护城河是低毛利定价能力本身，会员费只是把本该属于商品加价的利润显性化为「信任凭证」；65% 的占比是结果而非机制。两种读法都成立，但估值含义不同（前者看会员数增长，后者看同店销售）。
2. **中国与美国会员制不可直接类比**：Costco 是「会员费即利润」模型（续卡率≈90%+ 是生命线），而中国电商付费会员（京东PLUS/88VIP）是「权益补贴」模型——会员费收入远低于权益成本，本质是拉高 ARPU 与留存的前置投入。山姆是唯一在中国跑通 Costco 式「会员费≈利润」的公司（860 万×260 元≈22 亿会员费 vs 其利润贡献需按其分部口径核算，目前无公开分部利润，此为待证项）。
3. **口径争议：注册会员 ≠ 付费会员**：霸王茶姬的 1.9 亿是免费注册口径，与山姆 860 万付费会员完全不可比；「订阅疲劳」类调查多为欧美样本或二手汇编（如 readless 引 Bango），转录过程中数字易失真，Z 世代 87%/37% 两条仅作线索级采信。
4. **退订率的口径分化**：Antenna 的 churn 是月度订阅取消率（流媒体月付为主），而 Costco/山姆是年付+人工续卡，退订率天然低一个数量级；用「Netflix 月流失 1.8%」对比「山姆续卡率 70%」是错误的同框，比较只能在同为月付或同为年付内部进行。
5. **汽车订阅的分化**：整车订阅（沃尔沃 Care、Care by Volvo 及早期车队型创业公司）持续退潮，但部件级订阅（蔚来 BaaS 电池月租、智驾订阅）在增长——「订阅化」在汽车行业成立的粒度是电池/软件，不是整车，这与「预付年费锁定」心理学的适用边界一致：标的可感知、替代成本低的才适合订阅。
6. **反向检验**：假设「预付年费能锁定用户」不成立，则应看到年费制平台退订率与月付无差异——但 Costco/山姆续卡率与 Antenna 月付 churn 的巨大差距、以及 Deloitte 显示的美国家庭宁可精简也不完全退订（维持 4 个 SVOD）都与之矛盾，假设成立（高置信，机制解释部分为心理学文献支持）。

### 待证项与下一步建议

- **待证**：Costco FY2024 净利润 $7,367M 的逐字原文（建议直接读 SEC 10-K Income Statement 一节截图/表格）；山姆中国的续卡率官方口径（高卡 680 元续卡率数字被截断）。
- **待证**：中国「平均同时订阅会员数」的一手调查（本次检索未命中可靠的中文一手样本，建议查 QuestMobile 或艾媒 2024-2025 付费会员报告原始 PDF）。
- **下一步**：若继续深挖，最有价值的是把「会员费/净利润」这一比率做成 Costco FY2015–FY2025 十年时间序列，验证其稳定性（结构性 vs 周期性），这直接支撑 M05 模式篇的核心论点。
