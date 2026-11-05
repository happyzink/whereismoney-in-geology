## Dimension 05: 电力与泡沫争论

> 检索执行日：2026-10-31。子问题：①数据中心用电量与电力瓶颈；②AI泡沫正反方；③算力租赁价格趋势；④电信/铁路泡沫对照；⑤泡沫破裂后的钱流切换。整体置信：电力数据高（官方一手为主）、泡沫争论高（人物表态均有出处）、租赁价格中（关键节点含二手转引）、历史对照中低（铁路量化数字未获一手摘录）、钱流路径以推断为主（已逐条标注）。

### Current State

**① 数据中心用电量与电力瓶颈（国内外数据，电网扩容需求）**

- 全球总量：IEA《Energy and AI》基准情景预计2030年全球数据中心用电约945TWh、占总电力近3%；2024年份额为美国45%、中国25%、欧洲15%，且2017年以来全球数据中心用电年均增速约12%、为总用电增速的4倍[^iea-energy-ai][^iea-cmes]。
- 中国总量（官方口径）：2025年全国数据中心用电量约1700亿千瓦时（≈170TWh），占全社会用电量比重约1.6%，全国一体化算力网络8大枢纽节点是主要增量[^nea-shiwuwu]。另有2020年200TWh/占2.7%的媒体口径，两口径冲突见Tensions第1条[^carbonbrief-cn]。
- 中国电网扩容（钱已进的地方）："十五五"电网投资将达5万亿元以上、较"十四五"增长超80%，期间新增投产15回特高压直流输电通道、西电东送规模超4.2亿千瓦；2026年国网特高压及输变电设备已密集招标落地（中国西电、平高电气等中标）[^nea-shiwuwu][^cls-tegaoya]。
- 美国电力瓶颈量化：PJM最近四次基础容量拍卖中，数据中心驱动的容量费合计294亿美元、占总额636亿美元的46%；2026/2027容量年拍卖创纪录329.17美元/MW-day（2025-07-22公布），2027/2028拍卖（2026-07）再度触及监管批准上限325美元/MW-day[^utilitydive-pjm][^igs-pjm329][^pjm-auction2028]。
- 电力设备瓶颈：2025年全球燃气轮机需求超100GW、2026年有望超120GW（东吴证券），数据中心电网供应缺口预计2028年后明显放大[^dongwu-gas-turbine]；xAI已向韩国斗山能源增购5台380MW燃气轮机、前两台2026年底交付，部分数据中心电网连线需等7年[^dcse-xai]。
- 【三种口袋】电力环节的钱：公司的钱＝云厂商电力运营成本＋电网/电源资本开支（中国5万亿电网投资、PJM容量费）；股东的钱＝容量电价上涨推高电价、由工商业与居民分担；打工人的钱＝电气工程与电力设备岗位扩张（特高压招标中标即招聘）。

**② 「AI泡沫」正反方：谁在警告 vs 谁在否认**

警告方（投资人/经济学家/研报）：
- Michael Burry（Scion Asset Management）：其最后一次13F申报披露5万张Palantir看跌期权、名义价值9.12亿美元（其此前对英伟达的看跌头寸细节本轮未取得一手摘录，列待证）[^fool-burry]。
- Torsten Slok（Apollo首席经济学家）：AI泡沫大于1990年代IT狂热，前十大权重股估值相对整体市场更为极端[^slok-apollo]。
- MIT NANDA报告：企业已在生成式AI上花费300至400亿美元、95%的公司迄今未获得商业回报[^mit-nanda]。
- GMO（2026-01-13）：明确预言泡沫将破裂，将导致经济大失速、利润骤降与股市严重下跌[^gmo-valuing]。
- 过剩与循环交易信号：Meta计划出售多余AI算力的报道曾触发约2000亿美元芯片股市值抛售（2026-07，二手转述、信度中低）[^intellectia-overcapacity]；OpenAI与Oracle的3000亿美元数据中心协议被作为"循环交易"（供应商即客户股东）的核心样本[^noahpinion-circular]。

否认方（产业资本与部分卖方）：
- 黄仁勋（英伟达）：2026-01达沃斯称AI行业"虽看似泡沫、实则正引发平台级变革"，还需数万亿美元基础设施投资[^cls-jensen]；2026-10-16再驳泡沫论，称应追踪"每年4万亿美元"构想下的巨额需求、把目光投向更广泛的需求创造型企业[^moomoo-jensen]。
- 高盛：2026年美股IPO回暖但未现泡沫、AI是融资核心驱动（首席美股策略师Ben Snider；2026年约50家IPO、累计融资约1200亿美元）[^goldman-ipo]。
- 需求实据：SemiAnalysis跟踪显示2026年3月H100一年期合约租金较2025年10月低点回升40%、所有型号GPU产能满租（二手转引）[^semianalysis-h100]。

**③ 算力租赁价格趋势（GPU租赁降价幅度，按头部/中位/门槛三口径）**

- 头部（超大规模长约）口径：H100一年期合约租金从2025年10月低点约1.70美元/小时回升到2026年3月约2.35美元/小时（+40%），当前满租[^semianalysis-h100]。
- 中位（现货/转售）口径：2023年H100现货8美元/小时一卡难求→2024年10月已有7个转售市场卖到2美元/小时以下，批发价较2023年峰值累计下跌约七至八成[^latent-gpu][^semianalysis-h100]。
- 门槛（零售列表价）口径：2026年公有云H100列表价仍高达Azure约12.29美元/小时、AWS约6.88美元/小时（2026-05列表价），与小客户可得价差约5倍——"降价"主要发生在批发端，零售端价格黏性极强[^spheron-gpu]。
- 中国市场：结构性过剩与结构性紧张并存——样本千卡智算中心上架率不足50%、已上架服务器实际利用率不足30%、年运营成本超3000万元[^stdaily-suanli]；但2026年上半年国内GPU租赁"没有迎来预期中的降温，反而比2025年底更紧张"（知乎行业分析，信度中低）[^zhihu-gpu2026]；中国移动2025年算力预算373亿元、占总资本开支25%、智算规模目标34EFLOPS（新华网，其时定位"通用算力相对过剩、智能算力相对短缺"）[^news-cn-cmcc]。
- 结论（据上四条归纳）：GPU租赁降价的完整弧线为2023年8美元→2024年破2美元→2025年10月见底1.70美元→2026年回升2.35美元，降幅最大阶段已过、2026年边际趋紧；"算力过剩—租金通缩"叙事与"满租—涨价"事实在2026年同时存在，见Tensions第2条。
- 【三种口袋】降租的钱：公司的钱＝算力运营商毛利承压、应用层成本红利；股东的钱＝GPU资产租金收益率与二手卡残值下降；打工人的钱＝推理成本下降利好AI应用岗位（推断，无直接数据）。

**④ 电信泡沫/铁路泡沫与AI算力投资的对照**

- 电信泡沫硬数据：2000-2002年美股自峰值下跌的7万亿美元中，约2万亿美元来自电信公司市值蒸发[^starr-telecom]；"2001年的光纤泡沫为今天的AI投资者提供了警告"（overcapacity——过剩而非失败是泡沫的常态）[^siebert-fiber]。
- 结构对照（推断，基于上述两文框架）：光纤泡沫后大量dark fiber滞留，带宽价格暴跌，2004年后被点亮并成就宽带/YouTube时代——"资本毁灭、基建留存、下游受益"三段式；对应AI：GPU折旧期（3-5年）短于光纤，资本毁灭更快、出清更快，过剩时租金通缩同样利好应用层（推断）。
- 铁路狂热（1840年代英国）：victorianweb记载其充满"从粗略的成本估计到彻底的欺诈"等不诚实行为；投资占GDP比重等量化数字本轮未取得一手摘录，列待证（见文末）[^victorianweb-mania]。
- 与本期共享背景的衔接：英伟达市值4.98万亿美元（2026-10-30收盘，E04共享背景、主表待核）约为2000年思科峰值市值（约5500亿美元，公开常识、未在本轮引用）的9倍量级；关键差异是英伟达FY2026净利1200.67亿美元（共享背景），有真实现金流支撑，而2000年思科市盈率远高于此——"巨头替代品"位置相似、估值质量不同（推断）。

**⑤ 若泡沫破裂，钱会流向哪（新旧钱流切换路径）**

- 已发生的预演：2024-07高盛交易台记录——AI资本支出"泡沫"担忧引发七巨头抛售，对冲基金管理人"被迫积极分散投资"，美国市场极端集中度引发大规模主题轮动[^goldman-rotation]。
- 股票端去向（推断＋部分证据）：价值/红利/防御板块（公用事业、必需消费、医药）、现金与短债、黄金与国债；GMO情景下利润骤降与经济失速利好久期资产[^gmo-valuing]。
- 实物端去向：电力本身就是AI行情的"新钱池"——2026-07中国电力板块因"政策利好+AI算力双轮驱动"涨停潮、特高压设备密集中标[^cls-tegaoya]；燃机、变压器、电网链条是"卖铲人的卖铲人"，其需求取决于数据中心实际上电量而非GPU股价，泡沫破裂时抗跌性最强（推断）[^dongwu-gas-turbine]。
- 下游受益逻辑（推断）：若算力租金重演2023-2025式通缩（8→1.70美元/小时），成本红利流向AI应用层与非AI软件——历史上泡沫破裂后"用基建的人"比"建基建的人"活得更好[^latent-gpu][^siebert-fiber]。
- 新钱→旧钱切换路径总结（推断）：AI股权浮盈兑现→公司回购/并购与capex同步收缩→资金流向防御性股票、固收、贵金属与电力实物资产；中国的对应版本是电网5万亿投资把利润留在电力设备链内部[^nea-shiwuwu]。
- 【三种口袋】泡沫破裂的账单分配：公司的钱＝长协算力合同违约与GPU资产减值；股东的钱＝参照电信泡沫2万亿美元市值蒸发[^starr-telecom]；打工人的钱＝数据中心建设/芯片岗位收缩，电力与国产替代链岗位相对抗跌（推断）。

[^iea-energy-ai]: IEA. Energy and AI. 2025-04. https://iea.blob.core.windows.net/assets/86ed1178-4d77-45ac-ab38-28e849f3b93f/EnergyandAI.pdf
[^iea-cmes]: 国际能源署《能源与人工智能》要点转载（中国电机工程学会）. 2025. https://www.cmes.org/library/recom/e09c7b4523dc417a8aace8a87011e7b4.html
[^nea-shiwuwu]: 国家能源局. "十五五"电网投资将达5万亿以上. 2026-07-17. https://www.nea.gov.cn/20260717/6ba0fac6398740758e0f0de19ef8d27e/c.html
[^carbonbrief-cn]: Carbon Brief. 解读：中国如何应对数据中心能源增长的需求. 访问2026-10-31. https://www.carbonbrief.org/translations-explainer-how-china-is-managing-the-rising-energy-demand-from-data-centres
[^cls-tegaoya]: 财联社. 政策利好+AI算力双轮驱动！电力板块掀涨停潮. 2026-07-23. https://www.cls.cn/detail/2434908
[^utilitydive-pjm]: Utility Dive. Data centers drove $6.3B in PJM capacity auction costs. 2026-07-20. https://www.utilitydive.com/news/pjm-data-centers-capacity-auction-imm-bowring/825626
[^igs-pjm329]: IGS Energy. PJM Capacity Auction Hits Record $329/MW-Day. 2025-07-22发布. https://www.igs.com/energy-resource-center/energy-101/capacity-auction-results--what-it-means-for-your-business-s-electric-bill
[^pjm-auction2028]: PJM Inside Lines. PJM Capacity Auction Procures 138,318 MW of Generation Resources. 2026-07-14. https://insidelines.pjm.com/pjm-capacity-auction-procures-138318-mw-of-generation-resources-as-work-continues-to-address-growing-electricity-demand
[^dongwu-gas-turbine]: 东吴证券（网易号转载）. 数据中心电网供应缺口2028年后明显放大. 2026-09-16. https://www.163.com/dy/article/L6VCOD7705199NPP.html
[^dcse-xai]: 数智元网. 马斯克"加单"燃气轮机 部分数据中心电网连线需等7年. 2026-01-12. http://www.dc-se.com/newsdetail.asp?id=59553
[^fool-burry]: The Motley Fool. Michael Burry Disclosed Put Options Worth an Estimated $1.1 Billion. 2026-09-17. https://www.fool.com/investing/2026/09/17/michael-burry-disclosed-put-options-worth-an-estim
[^slok-apollo]: Investing.com. Apollo economist warns: AI bubble now bigger than 1990s tech mania. 2025-07-16. https://ng.investing.com/news/stock-market-news/apollo-economist-warns-ai-bubble-now-bigger-than-1990s-tech-mania-2010458
[^mit-nanda]: MIT科技评论中文版. MIT报告揭生成式AI残酷现实：95%企业无回报. 2025-08-24. https://www.mittrchina.com/news/detail/15153
[^gmo-valuing]: GMO. Valuing AI: Extreme Bubble, New Golden Era, or Both. 2026-01-13. https://www.gmo.com/americas/research-library/valuing-ai-extreme-bubble-new-golden-era-or-both_viewpoints
[^cls-jensen]: 财联社. 黄仁勋驳斥"AI泡沫论"：基建还需数万亿美元投资. 2026-01-22. https://www.cls.cn/detail/2265930
[^moomoo-jensen]: moomoo资讯. 黄仁勋反驳AI泡沫担忧：追踪每年4万亿美元构想下的巨额需求. 2026-10-16. http://www.moomoo.com/hans/community/feed/mr-fu-an-refutes-concerns-about-an-ai-bubble-outlining-117451647418374
[^goldman-ipo]: 财华社. 高盛：2026年美股IPO回暖但未现泡沫，AI为融资核心驱动力. 2026. https://www.finet.hk/newscenter/kol_content/6a3f92f50027f873928cd409
[^intellectia-overcapacity]: Intellectia. AI Infrastructure Overcapacity Concerns: Chip Stocks Selloff. 2026-07-13. https://intellectia.ai/blog/ai-infrastructure-overcapacity-concerns-2026
[^noahpinion-circular]: Noah Smith. Should we worry about AI's circular deals?. 2025-10-22. https://www.noahpinion.blog/p/should-we-worry-about-ais-circular
[^latent-gpu]: Latent Space. $2 H100s: How the GPU Rental Bubble Burst. 2024-10-11. https://latent.space/p/gpu-bubble
[^semianalysis-h100]: SemiAnalysis数据经Threads用户转引. H100一年期合约租金2025-10低点1.70美元→2026-03的2.35美元. 2026. https://www.threads.com/@wylin.tw/post/DXL6gTYgaZd
[^spheron-gpu]: Spheron Network. GPU Cloud Pricing Comparison 2026: H100, H200, B200. 2026-10-23. https://www.spheron.network/blog/gpu-cloud-pricing-comparison-2026
[^zhihu-gpu2026]: 知乎专栏. 2026年上半年GPU算力租赁市场行情分析：一卡难求，价格坚挺. 2026-07-08. https://zhuanlan.zhihu.com/p/2058211180783597073
[^stdaily-suanli]: 科技日报. 深瞳丨利用率仅三成，"沉睡"的算力如何激活. 2025-07-17. https://www.stdaily.com/web/gdxw/2025-07/17/content_371093.html
[^news-cn-cmcc]: 新华网. 通用算力相对过剩 智能算力相对短缺 中国算力市场的成长烦恼. 2025-04-29. http://www.news.cn/finance/20250429/3df0c33317d2499ab3a297a413e0acce/c.html
[^starr-telecom]: Paul Starr（Princeton）. The Great Telecom Implosion. 2002-09. https://www.princeton.edu/~starr/articles/articles02/Starr-TelecomImplosion-9-02.htm
[^siebert-fiber]: Siebert Williams Shank. AI's Nuclear Moment: Lessons From the Dot-Com Era's Forgotten Twin. 2025-10-23. https://blog.siebert.com/ais-nuclear-moment-lessons-from-the-dot-com-eras-forgotten-twin
[^victorianweb-mania]: Victorian Web. Railway Mania (dishonest practice). 2014-03-13. https://victorianweb.org/technology/railways/fraud.html
[^goldman-rotation]: Investing.com港版（FX168转引高盛交易台）. 高盛：AI资本支出"泡沫"破裂 七巨头抛售引发. 2024-07-19. https://hk.investing.com/news/stock-market-news/article-577756

### Key Evidence

| 数据点 | 数值 | 时间 | 原文摘录(逐字) | 自评信度 | 来源 |
|---|---|---|---|---|---|
| 全球数据中心用电预测 | 945TWh，占近3% | 2030E（IEA基准） | "Global electricity consumption by data centres is projected to reach around 945 TWh by 2030 in the Base Case, representing just under 3% of total global" | 高 | [^iea-energy-ai] |
| 各国数据中心用电份额 | 美45%/中25%/欧15% | 2024 | "2024年，美国在全球数据中心电力消耗中所占份额最大（45%），其次是中国（25%）和欧洲（15%）" | 高 | [^iea-cmes] |
| 数据中心用电增速 | 年增约12%，为总用电增速4倍 | 2017年以来 | "自2017年以来，全球数据中心电力消耗每年增长约12%，是总电力消耗增速的四倍" | 高 | [^iea-cmes] |
| 中国数据中心用电量 | 1700亿千瓦时，占1.6% | 2025 | "2025年全国数据中心用电量约1700亿千瓦时，占全社会用电量比重约1.6%" | 高（官方一手） | [^nea-shiwuwu] |
| 中国电网投资 | 5万亿元以上，较"十四五"+80% | "十五五"规划 | "投资将达5万亿元以上，较'十四五'增长超80%，期间将新增投产15回特高压直流输电通道，西电送规模超过4.2亿千瓦" | 高 | [^cls-tegaoya] |
| PJM数据中心容量费占比 | 294亿美元，占46% | 最近四次容量拍卖 | "In PJM's last four base capacity auctions, data center-driven capacity charges totaled $29.4 billion — 46% of the $63.6 billion in total" | 高 | [^utilitydive-pjm] |
| PJM拍卖价格纪录 | 329.17美元/MW-day | 2025-07-22公布（2026/2027容量年） | "came in at a record-breaking $329.17/MW-day" | 高 | [^igs-pjm329] |
| PJM最新拍卖触及上限 | 325美元/MW-day | 2026-07-14公布（2027/2028） | "Capacity Price Comes in at the Cap of $325, Down 2.5%" | 高 | [^pjm-auction2028] |
| 全球燃机需求 | 2025年超100GW、2026年超120GW | 2025-2026 | "2025年全球燃机需求超过100GW，2026年有望达到120GW以上" | 中（券商转述） | [^dongwu-gas-turbine] |
| 并网排队时间 | 最长7年 | 2026-01报道 | 标题原文："部分数据中心电网连线需等7年" | 中 | [^dcse-xai] |
| Burry看跌头寸 | 5万张Palantir期权，名义9.12亿美元 | 13F，2026-09-17披露 | "In his final 13F filing for Scion Asset Management, Burry disclosed 50,000 put options on Palantir with a notional value of $912 million" | 高 | [^fool-burry] |
| Slok泡沫论 | 前10大权重股估值更极端 | 2025-07-16 | "Slok highlights that the top 10 stocks have disproportionately high valuations relative to the overall market" | 高 | [^slok-apollo] |
| MIT NANDA回报率 | 95%企业无商业回报 | 2025-08 | "尽管企业在生成AI上已花费了300至400亿美元，但95%的公司迄今并未能获得商业回报" | 高 | [^mit-nanda] |
| GMO泡沫预言 | 泡沫将破裂→利润骤降 | 2026-01-13 | "the bubble will burst … the deflating of the AI bubble will lead to a major stumble for the economy, a plunge in profits, and a severe decline" | 高（观点性预测） | [^gmo-valuing] |
| 黄仁勋否认（达沃斯） | 需数万亿美元基建投资 | 2026-01-22 | "人工智能行业虽看似泡沫，实则正引发平台级变革，需数万亿美元投资建设基础设施" | 高 | [^cls-jensen] |
| 黄仁勋否认（最新） | 需求参照年4万亿美元构想 | 2026-10-16 | "英伟达CEO黄仁勋针对这些担忧表示，应将目光投向更广泛的需求创造型企业" | 中（社区转述） | [^moomoo-jensen] |
| H100长约租金回升 | 1.70→2.35美元/小时（+40%） | 2025-10→2026-03 | "H100一年期合约租金从2025年10月的低点1.70美元，回升到2026年3月的2.35美元，涨幅40%。目前所有型号的GPU产能全都满租" | 中（二手转引SemiAnalysis） | [^semianalysis-h100] |
| H100现货价格崩跌 | 8→低于2美元/小时 | 2023→2024-10 | "Last year, H100s were $8/ hr if you could get them. Today, there's 7 different resale markets selling them under $2" | 高 | [^latent-gpu] |
| H100零售列表价 | Azure约12.29、AWS约6.88美元/小时 | 2026-05列表价 | "H100 cloud rates in 2026 run up to ~$12.29/ hr on Azure and ~$6.88/ hr on AWS (May 2026 list)" | 中 | [^spheron-gpu] |
| 中国智算中心利用率 | 上架率<50%、利用率<30%、年成本超3000万元 | 2025-07报道 | "这座千卡规模的智算中心，上架率不足50%。即便已上架的服务器，实际利用率不足30%，而年运营成本则超过3000万元" | 高（央媒调查） | [^stdaily-suanli] |
| 国内租赁边际变化 | 2026上半年较2025年底更紧张 | 2026-07-08 | "2026年上半年，GPU算力租赁市场没有迎来预期中的降温，反而比2025年底更紧张" | 低（知乎专栏） | [^zhihu-gpu2026] |
| 中国移动算力预算 | 373亿元，占资本开支25% | 2025年 | "中国移动2025年算力预算为373亿元，占总资本开支的25%，计划将智算规模提升至34EFLOPS" | 高 | [^news-cn-cmcc] |
| 电信泡沫市值损失 | 约2万亿美元/美股共跌7万亿 | 2000-2002 | "Out of the $7 trillion decline in the stock market since its peak, about $2 trillion have disappeared in the capitalization of telecom companies" | 高 | [^starr-telecom] |
| OpenAI-Oracle协议 | 3000亿美元数据中心协议 | 2025-10确认 | "OpenAI confirmed it had struck a separate $300 billion deal with Oracle to build out data centers in the US" | 高 | [^noahpinion-circular] |
| Meta过剩算力传闻冲击 | 触发约2000亿美元芯片股抛售 | 2026-07-13 | "Meta's plan to sell excess AI compute triggered a $200B chip stocks selloff" | 低（博客转述，未见一手报道） | [^intellectia-overcapacity] |
| 高盛交易台轮动记录 | 对冲基金抛售七巨头 | 2024-07-19 | "對衝基金管理人被迫積極分散投資，美國市場的極端集中度正在引發大規模的主題" | 中（转引FX168） | [^goldman-rotation] |

### Tensions & Counter-arguments

1. **中国数据中心用电量两口径冲突**：CarbonBrief转引2021年《中国日报》称2020年中国数据中心耗电已达200TWh、占全国2.7%、2030年预计400TWh（占3.7%）[^carbonbrief-cn]；而国家能源局官方口径2025年仅为约1700亿千瓦时（170TWh）、占1.6%[^nea-shiwuwu]。2020年高于2025年在物理上不可能同时成立——前者疑似更宽口径（或含预估、在建与挖矿负荷）或为当年媒体高估。**采用官方能源局口径，冲突记录在案**；这直接影响"中国电力瓶颈"的量级判断（中国占比远低于美国45%份额所暗示的水平）。
2. **"算力过剩"与"满租回升"并存**：警告方证据是Meta出售多余算力传闻、智算中心利用率不足30%[^intellectia-overcapacity][^stdaily-suanli]；否认方证据是2026年3月H100满租、租金回升40%[^semianalysis-h100]。两者可以同时为真：批发现货市场2023-2025年已出清并触底回升，零售列表价仍虚高（价差约5倍），中国市场呈区域/结构性过剩。**"GPU租赁大幅降价"主要描述2023-2025年，2026年边际叙事已切换为"一卡难求"**[^zhihu-gpu2026]——引用"降价"数据必须带时间窗。
3. **泡沫定义之争的实质**：黄仁勋的"需求真实论"与Slok/GMO的"估值集中论"并不互斥——基础设施有用≠当前价格合理≠所有投资人赚钱；GMO自己也承认可能是"极端泡沫与新时代并存"（标题即此意）[^gmo-valuing]。
4. **历史类比的软肋**：光纤不折旧、可闲置二十年，GPU三五年折旧殆尽，"过剩基建留存惠及后人"的铁路/电信剧本在AI中打了折扣；但反向看，GPU折旧快也意味着资本毁灭快、出清快，下行周期可能短于电信（推断）。
5. **13F证据的局限**：Burry的9.12亿美元是名义值（notional）而非实际风险敞口，期权费远小于此；且这是Scion"最后一次13F申报"[^fool-burry]——头寸规模不足以构成对泡沫的证实或证伪，媒体存在放大动机。
6. **本轮检索的未决冲突**：Altman所称OpenAI约1.4万亿美元算力承诺、Bain"2030年AI需2万亿美元年收入"、Burry对英伟达的具体看跌头寸、铁路狂热投资占GDP比重、光纤点亮率（"2002年仅约2.7%点亮"的常引数字）均未取得一手逐字摘录，**全部列为待证，不计入结论**；英伟达市值4.98万亿美元（2026-10-30）沿用E04共享背景，待主表核实。

**待证项与建议查法**：①铁路投资占GDP比重→查英格兰银行Quarterly Bulletin铁路狂热专文；②光纤点亮率→查TeleGeography或2002年FCC报告原始口径；③OpenAI 1.4万亿美元承诺→OpenAI官方博客与DevDay 2025实录；④Burry英伟达头寸→SEC EDGAR调Scion 13F-HR 2025Q3原文；⑤变压器交付周期→Wood Mackenzie/NEMA年度报告；⑥国内算力租赁价格指数→信通院或IDC圈口径，替换知乎样本。
