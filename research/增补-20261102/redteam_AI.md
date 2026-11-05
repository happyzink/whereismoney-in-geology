# 红队二·攻击E04 —— AI算力期结论（重派）· 增补 2026-11-02

> 立场：反方研究员。目标：用2026年10–11月最新公开证据攻击E04《半导体与AI算力——当前的淘金热》四组结论，而非辩护。
> 检索约束：web_search 14次（已用满），总工具16次。所有"最新"数据均来自2026年9月–11月2日窗口的检索快照；未能一手复核的均降级标注。
> 引用契约：[^id]语义句柄，源定义紧跟小节；关键数字逐字摘录并附信度与时间窗。

---

## 一、结论摘要

E04四组结论经本轮攻击后：**三组维持、一处数字需更正（PJM 46%→40%）、两处措辞需降级（"毛利率逐季新高"、"OpenAI烧钱350亿"）**（高置信）。红队三条主攻线中两条被证据击退：①GPU租赁价2026年不跌反涨、云厂商capex共识2026年翻倍至7630亿美元且未见削减，"卖铲人利润时效崩塌"暂不成立；③燃机积压116GW、PJM连续顶格成交，"电力瓶颈缓解"不成立（高置信）。真正有效的攻击在②买方信用侧：Anthropic S-1（2026-10-26公开）暴露"收入$16.3B（2026上半年） vs 承诺$587B"的覆盖率缺口与$80.7B GAAP亏损，循环交易规模升至约万亿美元量级（中置信，聚合源）——建议按第六节三档表逐条修正。

---

## 二、攻击线①：卖铲人利润的时效攻击（折旧 / 租金 / capex）

### 2.1 攻击预期 vs 实际证据
红队预设三条攻击路径，两条被新数据击退：

**路径A"GPU折旧周期临近→资产减值"：会计争议存在，但定价证据反向。**
- 会计侧：超大规模厂商对AI服务器（含GPU）公开采用**5–6年**折旧年限，批评者主张真实技术寿命**2–4年**，该争论2026年10月仍在发酵【信度:高，时间窗:2025-11-17至2026-10-21】。
- 定价侧（反方不利证据）：H100（2022年发布的老一代芯片）一年期租赁合约价2026年1月下旬**突破$2/hr/GPU**，2月中下旬较1月底**再涨15–20%**；2025-12-09至2026-01-06现货指数**上涨10%**；2026-10-01有报价商将H100费率**自$3.85上调至$4.50/GPU-hr（约+17%）**。若市场真预期GPU三年内归零，一年期远期租金不可能上行。折旧攻击**暂无定价证据支持**【信度:高】。

**路径B"算力租赁价格崩塌"：证伪。** 2026年租赁市场呈紧张而非过剩：H100费率区间$1.49/hr（Vast.ai现货低端）至$6.98/hr（Azure标价），GPU租赁市场规模2026年约$52B、预计2031年$199B【信度:中（市场空间数字为第三方估计）】。老一代（A100）低至$1.09/hr，说明**代际折价存在**，但"崩塌"不成立。

**路径C"云厂商开始削减capex"：未发现证据，反而是上调。**
- S&P Global（2026-10-26财报前瞻）："For CY 2026, consensus year-over-year capex is expected to more than double from **$362 billion to $763 billion**. For CY 2027, this spending is …"（原文截断，CY2027方向未读全）【信度:高，时间窗:2026-10-26】。
- Alphabet于2026-04-29将2026全年capex指引**上调至$180–190B**。
- 2026-08月初Q2财报周：微软、亚马逊因capex计划获涨，Alphabet/Meta/Oracle因capex计划下跌——市场分歧在"花多少"，不在"要不要花"。
- 截至2026-11-02，四大厂商9月季度财报刚披露完毕（前瞻 dated 2026-10-26），红队**未检索到任何一家宣布削减capex**；唯一风险信号是seekingalpha前瞻提示"CY2027 capex指引规模过大"的担忧【信度:中，属市场情绪而非事实】。

### 2.2 英伟达自身最新数据（攻击①必须先过的事实底座）
- FY2026 Q4（截至2026-01-25）：营收**$68.1B**（一手通稿）【信度:高，时间窗:2026-02-25】；FY2026全年营收**$215.9B（+65%）**、毛利率**约75.2%**（二手）【信度:中】。
- FY2027 Q2（2026-08-26披露）：营收**$96.2B**、数据中心**$89.0B（+117% YoY）**【信度:中-高，二手转述】。
- 下一份财报（Q3 FY2027）预计2026-11-18前后发布，**晚于本报告**，构成最近的时效检验点。

### 2.3 攻击①的战果
- **战果1（措辞降级）**：E04"毛利率75%逐季新高"不精确——FY2026 Q3（2025-11-20披露）GAAP毛利率**自74.6%降至73.4%**（non-GAAP 75.0%→73.6%），存在季度回落；"逐季新高"应改为"全年中枢约75%、季度间有波动"。
- **战果2（新增脚注）**：大四家（微软/Alphabet/亚马逊/Meta）占英伟达收入**约61%**（2026-04-17，daloopa基本面口径），且**20+GW客户自建芯片（自研ASIC）2027年爬坡**——"确认利润"的可持续性锚在四家客户的capex决策上，这是时效攻击真正的着力点（2027–28），而非2026Q4。
- **未战果**：折旧减值、租金崩塌、capex削减三条路径2026-11时点均无证据。

[^yardeni]: Yardeni QuickTakes. "DEEP DIVE: The Debate About the Quality of AI Earnings". 2025-11-17. https://www.yardeniquicktakes.com/deep-dive-the-debate-about-the-quality-of-ai-earnings
[^luminix]: useluminix. "GPU Depreciation and Useful Life at Hyperscalers". 2026-10-21. https://www.useluminix.com/reports/industry-analysis/when-will-the-ai-bubble-burst/source/1
[^semianalysis]: SemiAnalysis. "The Great GPU Shortage — rental capacity/pricing（H100 1年期租赁价格指数）". 2026-04-01. https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity
[^silicondata]: Silicon Data. "H100 Price Spike: Understanding the 10% Surge in GPU…". 2026-01-09. https://www.silicondata.com/blog/h100-price-spike
[^intuition]: IntuitionLabs. "H100 Rental Prices Compared: $1.49–$6.98/hr Across 15+…"（页面含2026-10-01生效费率）. 2025-10-24（更新）. https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison
[^thunder]: Thundercompute. "AI GPU Rental Market Trends (October 2026)". 2026-10-01. https://www.thundercompute.com/blog/ai-gpu-rental-market-trends
[^sphype]: S&P Global Market Intelligence. "Microsoft and Alphabet earnings previews"（含CY2026 capex共识$362B→$763B）. 2026-10-26. https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/10/microsoft-and-alphabet-earnings-previews
[^fool]: The Motley Fool. "Microsoft and Amazon Won the AI Spending Week". 2026-08-04. https://www.fool.com/investing/2026/08/03/microsoft-and-amazon-won-the-ai-spending-week
[^fortune-capex]: Fortune. "Microsoft, Meta, and Google just announced billions more"（Alphabet 2026 capex上调至$180–190B）. 2026-04-29. https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions
[^nvda-q4]: NVIDIA Newsroom. "NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2026"（Q4营收$68.1B，截至2026-01-25）. 2026-02-25. http://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
[^nvda-fy26]: Chronicle Journal/Finterra. "The Architect of the Intelligence Age — NVDA analysis"（FY2026营收$215.9B、毛利率75.2%，二手）. 2026-04-15. https://markets.chroniclejournal.com/chroniclejournal/article/finterra-2026-4-15-the-architect-of-the-intelligence-age-a-comprehensive-analysis-of-nvidia-nvda
[^nvda-q2fy27]: CenterConsulting. "NVIDIA Reports $96.2 Billion Quarter"（Q2 FY2027，数据中心$89.0B +117%）. 2026-08-26. https://www.centerconsulting.com/ai-library/milestones/2026-nvidia-q2-fy2027-earnings
[^nvda-q3fy26gm]: Investing.com. "NVIDIA Q3 FY26 presentation"（GAAP毛利率74.6%→73.4%）. 2025-11-20. https://www.investing.com/news/company-news/nvidia-q3-fy26-presentation-revenue-surges-62-as-data-center-business-dominates-93CH-4370153
[^daloopa]: Daloopa. "NVIDIA Customer Concentration: A Big 4 Earnings Preview"（61%收入集中度、20+GW自建芯片2027爬坡）. 2026-04-17. https://daloopa.com/blog/analyst-pov/nvidia-customer-concentration-a-big-4-earnings-preview
[^nvda10k]: NVIDIA 10-K (FY2026, nvda-20260125). 2026-02. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm

---

## 三、攻击线②：买方承诺现金的信用攻击（Anthropic / OpenAI / 循环交易 / 集中度）

**这是本轮攻击的主战场，战果集中于此。**

### 3.1 Anthropic：S-1落地，E04数字被证实但暴露覆盖率缺口
Anthropic于**2026-10-26公开提交S-1**（IPO注册文件）——证据等级从媒体爆料跳升为法定披露文件。
- E04锚点获证实：**$518B基础设施承诺、约80%不可撤销/无论是否使用均需付款**（路透口径，2026-09-29即有报道）【信度:高】。分项：Google **$111.1B**、Amazon **$110.0B（2026–2036）**、Microsoft **$31.4B**【信度:高，时间窗:S-1】。
- S-1另口径：截至2026-06-30，**未来采购承诺$265.6B + 未开始执行的租约$321.4B = $587B**（不同口径合计$518B–$587B并存，建议脚注注明口径差异）【信度:中-高】。
- Azure承诺上调：**至少$44.9B（2026-11至2033-05）**（与上述$31.4B为不同窗口/口径）【信度:高，时间窗:2026-10-27报道】。
- **攻击战果（覆盖率缺口）**：2026上半年GAAP收入**$16.3B**，GAAP亏损**$80.7B（主要为非现金）**——年化收入约$33B vs 承诺$518–587B，**覆盖比约1:16至1:18**；且**剩余履约义务（RPO）仅$10.8B（截至2026-06）**， Fortune标题直译即攻击核心："Anthropic为算力背上数十亿承诺，但其客户随时可以走人"【信度:高（S-1数字）、Fortune解读为二手】。
- 收入口径冲突（必须写明）：2026-07-14有统计称run-rate**超$30B**；2026-08-20有专栏称"mid-2026 ARR每季增约$9B、run rate达$65B"。两者与S-1的H1 GAAP收入$16.3B不能直接互比（run-rate≠GAAP确认收入），E04引用时应统一到S-1口径并注明差异【信度:中，冲突未决】。

### 3.2 OpenAI：融资到位、收入低于自家叙事、缺口模型加码
- 融资：2026-04-02报道，OpenAI完成**史上最大私募轮$122B**（超出$110B目标）——"承诺现金"的股权腿目前是兑现的【信度:中-高】。
- 收入口径出现公开矛盾：2026-09-30 Axios口径"run-rate接近**$70B**"；2026-10-08另一报道称"接近**$50B**，比此前报道的$70B估计低约$20B"。两说并存，红队倾向采信偏保守的$50B并标注冲突【信度:中，冲突未决，时间窗:2026-09-30/10-08】。
- 缺口测算加码：HSBC（2025-12-05）测算至2030年**自由现金流持续为负、$207B融资缺口**（即便收入达$213B）；2026-05-25有分析称其基建投入需要**约$650B/年收入**才能自洽，而当时run-rate约$25B（5个月后口径升至$50B）【信度:低-中（模型推算），仅作脚注】。
- 合同footprint：2026-05-14跟踪报告称**实际签约口径约$400B+/3年**（Stargate、Oracle、CoreWeave、SoftBank、Microsoft），显著低于$1.4T头条口径【信度:中】。
- E04"OpenAI 2027年预计烧$350亿"：建议**降级改写**——该数字已落后于事件链（$122B融资、$50B run-rate、HSBC $207B缺口模型），应换成带日期的区间与口径，否则会被多头的"$122B已到账"轻易反驳。

### 3.3 循环交易：从"叙事"变成"万亿美元会计对象"
- 2026年7月媒体报道的Nvidia–OpenAI **$600B融资安排，8月落定为$105B signed guarantee**；循环生态跟踪站统计英伟达—OpenAI等compute交易合计约**$657B、整个循环体系约万亿美元量级**【信度:低-中（聚合站，需一手核对），时间窗:2026-07/08】。
- 该站标题本身即红队论点："AI循环经济，已映射成图"（The AI circular economy, mapped）——E04结论②若不加循环交易脚注，会被质问为何遗漏2026年最大规模的公司间融资结构。
- 反方必须同时记录的反驳：Noah Smith（2025-10-22）指出"客户同时买供应商股票"并不必然构成收入虚增，循环保不闭环要看现金是否真的流动。此为观点级证据。

### 3.4 供应商集中度
- 英伟达口径：大四家**61%**收入集中（见2.2/[^daloopa]）；10-K自认"收入相当部分来自有限数量的合作伙伴与分销商"【信度:高】。
- Anthropic口径（线索级，未复核）：有分析称Anthropic占AWS 2026年收入约26%、Azure约25%——若属实，"买方承诺现金"同时意味着**云厂商收入对单一AI客户的双向集中**。该数字来自观点长文，仅列为待证线索【信度:低】。

[^s1-sec]: Anthropic, PBC — Form S-1. 2026-10-26. https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
[^ksl]: KSL（路透稿）. "Anthropic's $518 billion AI buildout hinges largely on deals that cannot be canceled, filing shows"（约80%不可撤销）. 2026-09-29. https://www.ksl.com/article/51629885/
[^ccnews]: Cloud Computing News. "Anthropic's $518 billion AI infrastructure plan spans major clouds"（Google $111.1B/Amazon $110B/Microsoft $31.4B，引路透）. 2026-10. https://www.cloudcomputing-news.net/news/anthropic-ai-infrastructure-518-billion
[^decoding]: Decoding Discontinuity. "Anthropic S-1: Nearly $1T Compute Commitments…"（采购承诺$265.6B+租约$321.4B=$587B）. 2026-10-27. https://www.decodingdiscontinuity.com/p/anthropic-s1-compute-commitments
[^geekwire]: GeekWire. "Who's getting Anthropic's compute spending? IPO filing shows…"（Azure≥$44.9B，2026-11至2033-05）. 2026-10-27. https://www.geekwire.com/2026/whos-getting-anthropics-compute-spending-ipo-filing-shows-where-the-tech-giants-really-stand
[^fortune-a]: Fortune. "Anthropic is on the hook for billions in compute. Its customers can walk at any time"（RPO $10.8B，截至2026-06）. 2026-10-26. https://fortune.com/2026/10/26/anthropics-s-1-makes-clear-its-on-the-hook-for-billions-in-compute-its-customers-can-walk-at-any-time-2
[^markgrid]: MarkGrid. "Anthropic S-1 Explained"（H1收入$16.3B、GAAP亏损$80.7B、约$450B云承诺）. 2026-10-22. https://markgrid.ai/resources/anthropic-ipo-filing-s1-revenue-losses-explained
[^codingcat]: codingcat.dev. "Anthropic's S-1, $518B in cloud commitments, and circular AI"（AWS采购义务$110.0B，2026–2036）. 2026-10-26. https://codingcat.dev/post/anthropic-s1-ipo-circular-ai-economy-etf-risk
[^shuaiguan]: Shuai Guan. "Anthropic Statistics"（run-rate超$30B）. 2026-07-14. https://shuaiguan.io/blog/anthropic-statistics
[^aisupremacy]: AI Supremacy (Michael Spencer). "We've never seen an Anthropic before"（mid-2026每季+$9B ARR、run rate $65B——与上条冲突）. 2026-08-20. https://www.ai-supremacy.com/p/we-have-never-seen-an-anthropic-before-2026-revenue-ipo
[^fastco]: Fast Company. "OpenAI's gigantic new funding round renews fears about profitability and cash burn"（$122B轮）. 2026-04-02. https://www.fastcompany.com/91520029/
[^mezha]: Mezha.Media. "OpenAI's Revenue Run Rate Nears $50 Billion, Below $70B estimate". 2026-10-08. https://mezha.net/eng/news/5a34a746_openai-s_revenue_run
[^vantage]: Vantage Markets. "OpenAI Revenue Run Rate Nears $70B"（引Axios）. 2026-09-30. https://www.vantagemarkets.com/market-news/openai-revenue-run-rate-70-billion-september-30-2026
[^hsbc]: Economic Times. "Half-trillion loss? HSBC says OpenAI facing titanic cash burn through 2030"（$207B缺口）. 2025-12-05. https://m.economictimes.com/news/international/us/half-trillion-loss-hsbc-says-openai-facing-titanic-cash-burn-through-2030/articleshow/125789463.cms
[^boing]: Boing Boing. "OpenAI needs a 26x revenue increase to justify its buildout". 2026-05-25. https://boingboing.net/2026/05/25/openai-needs-a-26x-revenue-increase-to-justify-its-buildout.html
[^presenc]: Presenc.ai. "OpenAI Compute Commitments Tracker, May 2026"（实际签约约$400B+/3年）. 2026-05-14. https://presenc.ai/research/openai-compute-commitments-tracker-2026
[^circmap]: ai-circular-economy.com. "Is there an AI bubble? The AI circular economy, mapped"（$600B→$105B signed guarantee；约$657B compute交易）. 2026（滚动更新）. https://ai-circular-economy.com/
[^noah]: Noahpinion (Noah Smith). "Should we worry about AI's circular deals?". 2025-10-22. https://www.noahpinion.blog/p/should-we-worry-about-ais-circular
[^zitron]: Ed Zitron / wheresyoured.at. "Don't Look Up"（Anthropic占AWS/Azure收入比线索）. 2026-08-11. https://www.wheresyoured.at/dont-look-up

---

## 四、攻击线③：电力瓶颈是否缓解

**结论：未缓解（高置信），E04"电力是物理税"维持，但其中一个数字要改。**

### 4.1 PJM容量市场：连续顶格，数据中心占比更正为40%
- 2027/28基准剩余拍卖（2025-12执行，报告2025-12-17）：**"所有价格顶格成交（$333.44/MW-day）"**，总成本**$16.4B**（较上一拍卖$16.1B +1.9%）——一手【信度:高】。
- 独立市场监督（IMM）2026-01-05：数据中心需求推高其他用户成本**$6,497,653,512**；Utility Dive转述即**"$16.4B中的$6.5B、占40%"**。**E04的"46%"应更正为40%（对应2027/28拍卖口径；46%疑为上一拍卖或不同分母口径）**【信度:高】。
- 边际缓解信号（诚实记录）：2028/29拍卖（2026-07-14公布）出清价**$325/MW-day**，为两轮顶格后首次略低于上限，且采购容量138,318MW——价格信号开始被供给响应，但绝对水平仍是2024/25（$28.92）的**11倍**【信度:高】。

### 4.2 燃气轮机：积压创新高，交期3年+
- GE Vernova：截至2026 Q2**燃气设备积压+槽位预订116GW**；Siemens Energy积压**€73B**、财年Q3**69GW firm积压**（当季签15GW、只交付6GW），**交期3年以上**【信度:中-高（二手转述财报）】。
- 供给侧扩产真实存在：三菱重工2025-09宣布**两年内燃机产能翻倍**——即缓解最早也在2027–28年之后，E04时间窗内"物理税"不变【信度:高】。

### 4.3 核电：审批与框架加速，但都是2027+的供给
- 美韩2026-09宣布**$120B"Project Power"框架：6台AP1000+2台APR1400**【信度:高（WNA国别档案，2026-10-27更新）】。
- NRC已**批准西屋AP1000标准设计认证（DC）更新/延续**；预计2026年新增**约25份SMR执照申请**；西屋-政府合作框架下**至少$80B新机组**待建【信度:中-高】。
- 超大规模厂商持续签核电offtake：Amazon宾州960MW园区、Microsoft三里岛（Crane）837MW重启等【信度:中-高】。
- 攻击结论：核电线全部落在2027–2035交付窗口，**2026–27不构成电力瓶颈的缓解证据**，反而强化"物理税"的时间刚性。

### 4.4 中国"十五五"电网5万亿+
本轮检索预算内未复查（14次用尽）。维持E04原文引用，标注"2026-11未复核"，不因未查而降级。

[^pjm-bra]: PJM. "2027/2028 Base Residual Auction Report"（全部顶格$333.44、$16.4B）. 2025-12-17. https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2027-2028/2027-2028-bra-report.pdf
[^pjm-imm]: PJM Independent Market Monitor. "Analysis of the 2027/2028 RPM Base Residual Auction, Part A"（数据中心推高成本$6,497,653,512）. 2026-01-05. https://www.monitoringanalytics.com/reports/Reports/2026/IMM_Analysis_of_the_20272028_RPM_Base_Residual_Auction_Part_A_20260105.pdf
[^ud-pjm]: Utility Dive. "Data centers were 40% of PJM capacity costs in last auction". 2026-01-07. https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951
[^pjm-2829]: Integrity Energy. "2028-2029 PJM Capacity Auction Results"（出清$325/MW-day，2026-07-14公布）. 2026-08-28. https://www.integrityenergy.com/resources/about-us/news-media/what-the-2028-2029-pjm-capacity-auction-results-mean-for-businesses
[^pjm-131]: PJM Inside Lines. "PJM Capacity Auction Procures 138,318 MW…". 2026-07-14. https://insidelines.pjm.com/pjm-capacity-auction-procures-138318-mw-of-generation-resources-as-work-continues-to-address-growing-electricity-demand
[^ieefa-pjm]: IEEFA. "Projected data center growth spurs PJM capacity prices by factor of 10"（$28.92→$329.17）. 2025-07-30. https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10
[^secondwatt]: SecondWatt. "Gas Turbine OEM Backlogs in 2026"（GE Vernova 116GW、Siemens €73B）. 2026-09-27. https://secondwatt.com/resources/turbine-oem-backlog-2026-lead-times-pricing
[^sandstone]: Sandstone Group. "GE Vernova's Gas Turbine Backlog Hits 116 GW…"（Siemens 69GW firm、交期3年+）. 2026（约8–9月）. https://sandstonegroup.us/ge-vernovas-gas-turbine-backlog-hits-116-gw-what-does-this-mean-for-the-ai-market
[^mhi]: Utility Dive. "Gas turbine manufacturers expand capacity…"（三菱两年内产能翻倍）. 2025-09-05. https://www.utilitydive.com/news/mitsubishi-gas-turbine-manufacturing-capacity-expansion-supply-demand/759371
[^wna]: World Nuclear Association. "Nuclear Power in the USA"（2026-09美韩$120B Project Power：6×AP1000+2×APR1400）. 更新于2026-10-27. https://world-nuclear.org/information-library/country-profiles/countries-t-z/usa-nuclear-power
[^ans]: ANS Nuclear Newswire. AP1000 design certification renewal approved by NRC. https://www.ans.org/news/tag-ap1000
[^pgs]: Partnership for Global Security. "A Nuclear Power Perspective for 2026"（3台AP1000推进、预计25份SMR申请）. 2026-01-16. https://partnershipforglobalsecurity.org/a-nuclear-power-perspective-for-2026%EF%BF%BC
[^westinghouse]: Westinghouse. "Strategic Partnership"（至少$80B新AP1000）. https://westinghousenuclear.com/about/strategic-partnership
[^nia]: Nuclear Innovation Alliance. "U.S. Nuclear Energy Project Tracker Update — April 2026". 2026-04-07. https://nuclearinnovationalliance.org/us-nuclear-energy-project-tracker-update-april-2026
[^irecruit]: iRecruit. "SMR Data Centers (2026): Every Nuclear Deal & Project"（Amazon 960MW、Microsoft TMI 837MW）. 2026-03-10. https://www.irecruit.co/insights/smr-nuclear-powered-data-center-developments

---

## 五、红队诚实声明：被证据击退的攻击

1. **"GPU租赁价格崩塌"**——2026年H100租赁价格上行（一年期合约$2/hr+且2月再涨15–20%），攻击不成立；仅老一代（A100 $1.09/hr）存在代际折价。
2. **"云厂商开始削减capex"**——截至2026-11-02未发现任何削减证据；CY2026共识capex较2025年翻倍至$763B。该攻击只能以"2027指引是否过猛"的形式存活（市场情绪级，非事实级）。
3. **"电力瓶颈缓解"**——燃机116GW积压+3年交期、PJM连续顶格、核电供给全部在2027+，缓解证据为零；唯一边际信号是2028/29拍卖$325略低于上限与三菱扩产。

---

## 六、对E04三档结论的逐条修正建议（维持 / 加脚注 / 降级）

| # | E04原结论 | 建议 | 理由与新证据 |
|---|---|---|---|
| ①a | 英伟达FY2026净利$1200.67亿 | **维持** | 与FY26营收$215.9B（+65%）、Q4营收$68.1B（一手）一致；建议脚注标明"GAAP、财年截至2026-01-25"，并把一手来源升级为10-K（[^nvda10k]）。 |
| ①b | 毛利率75%逐季新高 | **加脚注（措辞降级）** | Q3 FY26 GAAP毛利率74.6%→73.4%存在回落；应改为"全年中枢约75%、季度有波动"（[^nvda-q3fy26gm]、[^nvda-fy26]）。 |
| ①c | H100价值链88%归英伟达 | **维持** | 本轮未获新数据，未复核；不降级也不加固。 |
| ①d | （新增）卖铲人时效风险 | **加脚注** | 加两条：大四家客户集中度61%+20+GW自研芯片2027爬坡（[^daloopa]）；折旧5–6年 vs 2–4年会计争议（[^yardeni]、[^luminix]）。同时加"反脚注"：H100一年期租金2026年上行15–20%，折旧恐慌暂无定价证据（[^semianalysis]）。 |
| ②a | Anthropic算力承诺约$518B/约80%不可撤销 | **维持并升级证据等级** | S-1（2026-10-26）证实80%不可撤销；但必须并排脚注：H1收入$16.3B、GAAP亏损$80.7B、RPO仅$10.8B、采购承诺+租约合计$587B口径、客户可随时取消（[^s1-sec]、[^ksl]、[^decoding]、[^markgrid]、[^fortune-a]）。 |
| ②b | OpenAI 2027年预计烧$350亿 | **降级改写** | 数字落后于事件链：$122B融资已到账（2026-04）、run-rate口径$50B vs $70B公开矛盾（2026-09/10）、HSBC模型$207B缺口。建议替换为"run-rate约$50–70B（口径冲突待核）+股权腿$122B已落地+HSBC缺口模型"，原句删除（[^fastco]、[^mezha]、[^vantage]、[^hsbc]）。 |
| ②c | （新增）循环交易 | **加脚注（建议升格为独立风险小节）** | Nvidia–OpenAI $600B报道→$105B signed guarantee（2026-07/08）、循环体系约万亿美元量级（聚合源，低-中信度待核）；同时保留Noah Smith的反方观点（[^circmap]、[^noah]）。 |
| ②d | （新增）供应商集中度 | **加脚注** | 英伟达大四家61%（一手基本面口径）；Anthropic占AWS/Azure收入比（26%/25%）仅列线索级待证（[^daloopa]、[^zitron]）。 |
| ③a | PJM容量费46%由数据中心驱动 | **加脚注并更正数字** | 2027/28拍卖IMM口径为40%（$6.5B/$16.4B）；46%应标明属哪个拍卖年度与分母，否则与官方IMM冲突（[^pjm-imm]、[^ud-pjm]）。 |
| ③b | 中国十五五电网5万亿+ | **维持（未复核标注）** | 本轮检索预算未覆盖；不降级，标注"2026-11-02未复查"。 |
| ③c | 电力是物理税 | **维持** | PJM连续顶格（$333.44→$325）、GE Vernova 116GW积压、燃机交期3年+、核电供给在2027+。可加边际缓解脚注：2028/29出清价首破顶格+三菱产能翻倍，缓解信号最早2028（[^pjm-bra]、[^pjm-2829]、[^secondwatt]、[^mhi]、[^wna]）。 |
| ④ | 泡沫真分歧 | **维持，更新弹药清单** | 空方新增：TS Lombard"何时而非是否"（2026-10-26）、OpenAI run-rate低于此前估计$20B、Anthropic GAAP亏$80.7B、循环体系万亿美元量级。多方新增：$122B融资落地、CY2026 capex共识$763B、H100租金上行、Q2 FY27数据中心+117%（[^marketwatch]、[^mezha]、[^markgrid]、[^circmap]、[^fastco]、[^sphype]、[^semianalysis]、[^nvda-q2fy27]）。 |

[^marketwatch]: MarketWatch. "This strategist says it's a matter of when, not if, the AI bubble pops"（TS Lombard）. 2026-10-26. https://www.marketwatch.com/story/this-strategist-says-its-a-matter-of-when-not-if-the-ai-bubble-pops-heres-how-to-prepare-for-that-86ffbf30

---

## 七、待证项（本轮预算内未能闭环）

1. **Anthropic S-1原文数字**：$518B vs $587B口径差异、"75% of …"被截断的Fortune关键句、Azure $31.4B vs $44.9B窗口差异——需读S-1原文（sec.gov链接已存[^s1-sec]）。
2. **OpenAI run-rate $50B vs $70B**：两条二手报道冲突，需回溯Axios原文与The Information口径。
3. **Nvidia–OpenAI "$105B signed guarantee"**：仅聚合站陈述，需找一手公告或主流通讯社报道。
4. **CY2027 capex共识方向**：S&P引文在关键句处截断，需读原文判断2027是继续上行还是见顶。
5. **"46%"与"88%价值链"的E04内部出处**：反方无法核对其原始定义，建议正方补源定义。
6. **中国"十五五"电网投资与国内算力租赁价格**：预算用尽未查，下轮优先。
7. **Anthropic收入口径冲突**（$30B/2026-07 vs $65B/2026-08 vs S-1 H1 $16.3B GAAP）：需统一到招股书口径后重写E04②。

## 八、若继续投入，最值得查的方向

1. **2026-11-18英伟达Q3 FY2027财报**：验证$96.2B之后环比斜率与Rubin爬坡期毛利率指引——这是"卖铲人确认利润"下一个时效检验点。
2. **四大厂商CY2027 capex指引原文**（财报电话会逐字稿）：若任何一家首次给出"平台期/削减"措辞，E04①的脚注应立即升级为降级。
3. **Anthropic S-1的承销与定价**：IPO认购倍数将直接检验"买方承诺现金"的市场置信。
4. **PJM 2029/30拍卖与FERC对数据中心特别注意权（co-location）规则**：电力税的边际拐点观察位。
