# E04·dive_02

## Dimension 02: 英伟达印钞机与产业链分钱

> 检索说明：本轮共执行17次web_search（覆盖NVIDIA官网/SEC文件、台积电官网年报与法说会纪要、SK海力士官方新闻室、Google Cloud官方新闻室、Anthropic官方公告及财经媒体）+2次fetch_content（NVIDIA Q4 FY2026新闻稿全文、AI芯片成本拆分页全文）。全部为2026年10月31日检索。三口袋（公司的钱/股东的钱/打工人的钱）与三口径（头部/中位/门槛）分布见Current State对应条目；每个数字标注时间窗与口径，来源逐条列于小节末尾。

### Current State

**① 英伟达利润率与FY2026分季度趋势（结论：毛利率逐季爬坡60.5%→75.0%，净利率约43%→63%，"印钞机"边际在加速而非衰减；高置信）**
- FY2026全年（2025-01-26至2026-01-25）：营收$215,938M（+65%），GAAP毛利率71.1%（non-GAAP 71.3%），GAAP净利$120,067M（+65%），摊薄EPS $4.90。FY2026毛利率较FY2025的75.0%下降3.9个百分点，原因是Q1包含对华H20相关计提导致该季毛利率异常（H20计提本轮未取得逐字原文，信度中）[^nvidia-q4fy26][^investors-h20]。
- 分季度（GAAP口径，Q1/Q2为推算+二手印证，Q3/Q4为一手财报）：Q1营收$44.06B、毛利率≈60.5%、净利≈$18.8B（Q1/Q2绝对值为全年减其余三季倒推，方法见Key Evidence注）；Q2营收$46.74B、毛利率72.4%、净利≈$26.4B[^nvidia-q3fy26][^earningsecho]；Q3营收$57.006B、毛利率73.4%（non-GAAP 73.6%）、净利$31.91B[^nvidia-q3fy26]；Q4营收$68.127B、毛利率75.0%（non-GAAP 75.2%）、净利$42.96B[^nvidia-q4fy26]。
- 净利率（推算=净利/营收）：Q1≈42.6%→Q2≈56.5%→Q3≈56.0%→Q4≈63.1%；全年55.6%（FY2025为55.8%，基本持平）。注意：Q4净利率含其他收益净额$5,604M（主要为权益投资公允价值变动），利润率质量有"水分"，见Tensions[^nvidia-q4fy26]。
- 数据中心是印钞机主体：Q4数据中心营收$62.3B（占当季91.5%，推算），全年$193.7B（+68%，占总营收89.7%，推算）[^nvidia-q4fy26]。
- FY2027Q1指引：营收$78.0B±2%、GAAP毛利率74.9%±50bp，且"NVIDIA is not assuming any Data Center compute revenue from China in its outlook"——高毛利趋势延续但中国收入已从基数中剔除[^nvidia-q4fy26]。二手来源称FY2027Q1实际营收$81.6B、净利$58.3B（中低信度，待10-Q核实）[^intellectia-q1fy27]。

**② 一颗GPU的价值链分钱（BOM口径，估算值±15-20%；结论：英伟达拿走卖价的78-88%，HBM约5-10%，台积电晶圆+CoWoS约4-6%，剩余环节个位数以下）**
- 以H100 SXM5为例（卖价估$27,000）：晶圆+良率成本（台积电）$300（≈1.1%）+HBM（SK海力士等）$1,350（≈5.0%）+CoWoS先进封装（台积电）$750（≈2.8%）=BOM合计$3,320，英伟达毛利≈$23,680、BOM口径毛利率88%[^siliconanalysts]。
- 更新一代：B200（$850+$3,250+$1,100=$6,750，卖价$40,000，83%）；GB200超级芯片（$1,700+$6,500+$2,200=$14,200，卖价$65,000，78%）——HBM占GB200物料成本约46%（推算），页面原文"HBM memory and advanced packaging account for over 60% of total BOM cost on every NVIDIA and AMD part"[^siliconanalysts]。
- 对照组：AMD MI300X BOM $5,300/卖价$15,000/毛利率65%，"NVIDIA chips command 78-88% gross margins compared to AMD's 65-66%"——溢价来源是CUDA生态与需求强度[^siliconanalysts]。
- 三口径（按GPU卖价分钱，BOM估算口径）：头部=英伟达78-88%；中位=单一大宗环节（HBM≈5%、CoWoS≈2.8%、晶圆≈1.1%，GB200上HBM升到≈10%）；门槛=整板/整机ODM与后段供应链，净利率低个位数（佐证：共享背景口径工业富联2025归母净利352.86亿元(+51.98%)、云服务商AI服务器收入增超3倍——共享背景数字，本轮未独立核实其收入与利润率，信度中）。
- 供给瓶颈方有议价权：原文"TSMC CoWoS capacity remains supply-constrained with 40-52 week lead times"；2026年8月HBM3e合约价基准约$17/GB[^siliconanalysts]。

**③ 台积电2025年净利与AI收入占比（结论：2025净利NT$1,717.88B≈US$55.21B（净利率≈45.1%，推算），HPC全年+48%，AI加速器占全年收入high-teens%；高置信）**
- 2025全年：净收入NT$1,717.88B；美元口径"net income of US $55.21 billion on consolidated revenue of US $122.42 billion"（较2024年净利$36.087B[共享背景口径]大increase，涨幅≈53%，推算）[^tsmc-ar]。
- Q4 2025单季：净利润5057亿新台币（同比+35%）、营收1.046万亿新台币、毛利率62.3%[^sina-tsmc]。
- AI口径（官方法说会纪要）："On a full-year basis, HPC increased 48% year-over-year"；"Revenue from AI accelerators accounted for high-teens percent of our total revenue in [2025]"——即AI加速器约占2025全年收入高十几个百分点（≈13-19%区间，推算）[^tsmc-4q25-transcript]。
- 2026年指引口径（二手转述）："AI accelerator revenue is still expected to grow at a mid-to-high-50s percent compound annual growth rate (CAGR)"——注意这是增速指引不是占比[^futurum-tsmc]。

**④ CUDA生态的锁定效应（结论：4M+注册开发者、40,000+组织构成迁移壁垒，是英伟达溢价的结构性来源；中高置信）**
- "more than 4 million developers have registered for CUDA and over 40,000 organizations use CUDA"（转引英伟达投资者材料）[^alphastreet-cuda]。
- 锁定的量化体现：同一物料成本结构下英伟达比AMD高13-23个百分点毛利率（BOM口径78-88% vs 65-66%），分析将其归因于"CUDA software ecosystem lock-in, stronger enterprise demand, and first-mover advantage"[^siliconanalysts]。
- 英伟达用开源模型+库继续加深锁定：FY2026Q4推出Nemotron 3开源模型族、CUDA-X库生态合作（India制造、Cadence/Siemens/Synopsys等）[^nvidia-q4fy26]。

**⑤ 英伟达的风险：客户集中度与自研芯片替代（结论：集中度异常高且在上升；自研芯片是真实但在"共存"中推进；中高置信）**
- 客户集中度（一手SEC文件）：FY2026全年"sales to one direct customer represented 22% of total revenue and sales to another direct customer represented 14% of total revenue"；前三季度口径为两大直接客户21%+13%[^sec-10k-fy26][^q3fy26-10q]。2026年4月披露口径升级为四大直接客户各超10%、合计61%（daloopa对Q1 FY2027文件的解读，原文截断，信度中）[^daloopa]。
- 谷歌TPU替代进度：2025-10-23官宣Anthropic将用至多100万颗TPU训练/服务Claude、价值数百亿美元("plans to access up to 1 million TPUs, worth tens of billions of dollars")；2026-04-06再签Google+Broadcom数吉瓦级下一代TPU产能协议[^google-anthropic-tpu][^anthropic-gbw]。
- 亚马逊自研替代进度：Anthropic与AWS"Project Rainier"集群"featuring 500,000+ Trainium2 chips to train"其模型（2025-12报道）[^uncoveralpha-trainium]。
- 但替代与共存并行（一手反证）：同季英伟达官宣与Meta多年期合作"including the large-scale deployment of NVIDIA CPUs, networking and millions of NVIDIA Blackwell and Rubin GPUs"，并宣布对Anthropic的投资与技术合作（Anthropic经Azure用NVIDIA系统跑Claude）[^nvidia-q4fy26]。

**三口袋分账（项目纪律①）**
- **公司的钱**：英伟达FY2026净利$120.067B（净利率55.6%，推算）[^nvidia-q4fy26]；台积电2025净利$55.21B（净利率45.1%，推算）[^tsmc-ar]；SK海力士2025营业利润47.2万亿韩元（营业利润率48.6%，推算；约合330-345亿美元，按2025年韩元汇率区间推算，低信度）[^skhynix-fy25]。
- **股东的钱**：英伟达FY2026"returned $41.1 billion to shareholders in the form of shares repurchased and cash dividends"，季度股息仅$0.01/股（回购绝对主导）；季末回购授权还剩$58.5B[^nvidia-q4fy26]。FY2026自由现金流$96.68B（二手推算口径）[^tikr]；2026年8月单季再返还约$26.0B[^nvidia-q2fy27]；2026年9月新增$150B回购授权、总额度升至$235B≈2.4×FY2026自由现金流[^tikr]。台积电/SK海力士股东回报本轮未检索，待证。
- **打工人的钱**：英伟达股权激励是主要员工回报载体——FY2026 GAAP与non-GAAP营业费用差额$6,382M（23,076−16,694，主要为SBC，推算）；FY2027Q1起non-GAAP计入SBC，指引季度SBC约$1.9B，原文"Stock-based compensation is a foundational component of NVIDIA's compensation program to attract and retain world-class talent"[^nvidia-q4fy26]。台积电/SK海力士/ODM环节员工薪酬数据本轮未检索，待证；ODM为劳动密集环节、净利率低个位数（门槛口径，见②）。

### Key Evidence

| 数据点 | 数值 | 时间 | 原文摘录(逐字) | 自评信度 | 来源 |
| --- | --- | --- | --- | --- | --- |
| 英伟达Q4 FY26营收/毛利率 | $68,127M / 75.0% | 止2026-01-25季度 | "record revenue for the fourth quarter ended January 25, 2026, of $68.1 billion, up 20% from the previous quarter and up 73% from a year ago. For fiscal 2026, revenue was $215.9 billion, up 65% from a year ago." | 高 | [^nvidia-q4fy26] |
| FY2026毛利率（GAAP/non-GAAP） | 71.1% / 71.3% | FY2026全年 | "For the quarter, GAAP and non-GAAP gross margins were 75.0% and 75.2%, respectively. For fiscal 2026, GAAP and non-GAAP gross margins were 71.1% and 71.3%, respectively." | 高 | [^nvidia-q4fy26] |
| FY2026净利与EPS | $120,067M / $4.90 | FY2026全年 | 净利行："$120,067"；EPS行："Diluted earnings per share $4.90"（FY25对照：净利"$72,880"、EPS"$2.94"） | 高 | [^nvidia-q4fy26] |
| Q3 FY26 | 营收$57,006M、GAAP毛利率73.4%、净利$31,910M | 止2025-10-26季度 | "For the quarter, GAAP and non-GAAP gross margins were 73.4% and 73.6%, respectively. Revenue $57,006 $46,743. Gross margin 73.4 % 72.4%"（后两组为Q3对Q2对照，即Q2毛利率72.4%） | 高 | [^nvidia-q3fy26] |
| Q2 FY26净利（二手印证） | ≈$26.4B | 止2025-07-27季度 | "$46.7B revenue (+56% YoY, +6% QoQ) and $26.4B net income (+59% YoY), Strong gross margins of 72.4 %" | 中 | [^earningsecho] |
| Q1 FY26（推算） | 营收$44,062M、净利≈$18.8B、毛利率≈60.5% | 止2025-04-27季度 | 推算方法：215,938−46,743−57,006−68,127=44,062（营收）；120,067−26,422−31,910−42,960=18,775（净利）；毛利率由全年毛利153,463减Q2-Q4推得≈60.6%。该季为H20相关计提所在季 | 中（数值自洽、口径推算） | [^nvidia-q4fy26][^investors-h20] |
| 数据中心收入 | Q4 $62.3B；FY26 $193.7B | Q4及FY2026 | "Fourth-quarter revenue was a record $62.3 billion, up 22% from the previous quarter and up 75% from a year ago…Full-year revenue rose 68% to a record $193.7 billion." | 高 | [^nvidia-q4fy26] |
| FY2026股东回报 | $41.1B | FY2026全年 | "During fiscal 2026, NVIDIA returned $41.1 billion to shareholders in the form of shares repurchased and cash dividends. As of the end of the fourth quarter, the company had $58.5 billion remaining under its share repurchase authorization." | 高 | [^nvidia-q4fy26] |
| FY27Q1指引（不含中国） | 营收$78.0B±2%；毛利率74.9% | 2026-02-25发布 | "Revenue is expected to be $78.0 billion, plus or minus 2%. NVIDIA is not assuming any Data Center compute revenue from China in its outlook." | 高 | [^nvidia-q4fy26] |
| H100价值链拆分 | 晶圆$300+HBM$1,350+CoWoS$750=BOM$3,320；卖价$27,000；毛利率88% | 2026-08快照 | "H100 SXM5 … $300Wafer + yield cost … $1,350HBM memory stack cost … $750CoWoS / advanced packaging cost … $3,320Total BOM manufacturing cost … $27,000Average selling price … 88%Gross margin" | 中（多源共识估算±15-20%） | [^siliconanalysts] |
| B200/GB200拆分 | B200 $6,750/$40,000/83%；GB200 $14,200/$65,000/78% | 2026-08快照 | "B200 … $6,750 … $40,000 … 83%"；"GB200 … $14,200 … $65,000 … 78%"；"HBM memory and advanced packaging account for over 60% of total BOM cost on every NVIDIA and AMD part below." | 中 | [^siliconanalysts] |
| HBM与封装占比 | HBM 30-64% of BOM；GB200 HBM $6,500/颗 | 2026-08 | "Across the chips in the table, HBM memory represents 30-64% of total manufacturing cost. For the GB200 superchip, HBM alone costs $6,500 per unit -- roughly double the entire manufacturing cost of an H100."；"~$17/GB HBM3e contract pricing" | 中 | [^siliconanalysts] |
| CoWoS供给约束 | 交期40-52周 | 2026-08 | "TSMC CoWoS capacity remains supply-constrained with 40-52 week lead times." | 中 | [^siliconanalysts] |
| 英伟达vs AMD毛利率 | NVIDIA 78-88% vs AMD 65-66% | 2026-08 | "NVIDIA chips command 78-88% gross margins compared to AMD's 65-66%. This margin gap reflects NVIDIA's CUDA software ecosystem lock-in, stronger enterprise demand, and first-mover advantage in data center AI." | 中 | [^siliconanalysts] |
| 台积电2025全年净利 | NT$1,717.88B / US$55.21B（收入US$122.42B） | 2025财年 | "Net income was NT $1,717.88 billion. In US dollar terms, TSMC generated net income of US $55.21 billion on consolidated revenue of US $122.42 billion" | 高 | [^tsmc-ar] |
| 台积电Q4 2025 | 净利5057亿新台币(+35%)、营收1.046万亿新台币、毛利率62.3% | 2025Q4 | "2025年第四季度净利润 5057亿元新台币，同比增35%； 营收 1.046万亿元新台币；毛利率62.3％" | 高 | [^sina-tsmc] |
| 台积电HPC/AI占比 | HPC全年+48%；AI加速器占收入high-teens% | 2025全年 | "On a full-year basis, HPC increased 48% year-over-year."；"Revenue from AI accelerators accounted for high-teens percent of our total revenue in [2025]"（摘录截自纪要片段） | 高 | [^tsmc-4q25-transcript] |
| SK海力士FY2025 | 营收97.1万亿韩元、营业利润47.2万亿韩元 | 2025财年 | "SK hynix posted record 2025 results with revenue of 97.1T won and operating profit of 47.2T won, driven by AI memory and HBM." | 高 | [^skhynix-fy25] |
| CUDA生态规模 | 4M+注册开发者、40,000+组织 | 2026-03报道（转引投资者材料） | "Nvidia's investor materials report that more than 4 million developers have registered for CUDA and over 40,000 organizations use CUDA" | 中高（二手转引一手） | [^alphastreet-cuda] |
| 客户集中度FY2026 | 最大直接客户22%、第二大14% | FY2026全年（10-K） | "For fiscal year 2026, sales to one direct customer represented 22% of total revenue and sales to another direct customer represented 14% of total revenue" | 高 | [^sec-10k-fy26] |
| 客户集中度9M FY26 | 两大直接客户21%、13% | FY2026前三季度（10-Q） | "For the first nine months of fiscal year 2026, sales to two direct customers represented 21% and 13% of total revenue, respectively" | 高 | [^q3fy26-10q] |
| 四大客户合计61% | 四大直接客户各>10%、合计61% | FY2027Q1披露（解读） | "NVIDIA's most recent disclosure shows four direct customers, each representing more than 10% of total revenue, collectively accounting for 61%…"（原文片段截断） | 中 | [^daloopa] |
| Anthropic×谷歌TPU | 至多100万颗TPU、数百亿美元 | 2025-10-23 | "Anthropic will train and serve Claude models with plans to access up to 1 million TPUs, worth tens of billions of dollars" | 高 | [^google-anthropic-tpu] |
| Anthropic×Google+Broadcom扩约 | 数吉瓦下一代TPU | 2026-04-06 | "We have signed a new agreement with Google and Broadcom for multiple gigawatts of next-generation TPU capacity that we expect to come online" | 高 | [^anthropic-gbw] |
| Anthropic×AWS Trainium2 | 500,000+颗 | 2025-12-18报道 | "AWS and Anthropic partnered on 'Project Rainier,' one of the world's largest AI training clusters, featuring 500,000 + Trainium2 chips to train" | 中高 | [^uncoveralpha-trainium] |
| Meta反证（仍买英伟达） | 数百万颗Blackwell/Rubin | 2026-02-25 | "a multiyear, multigenerational strategic partnership with Meta…including the large-scale deployment of NVIDIA CPUs, networking and millions of NVIDIA Blackwell and Rubin GPUs." | 高 | [^nvidia-q4fy26] |
| 英伟达×Anthropic投资合作 | 投资+技术合作 | 2026-02-25 | "Announced an investment and deep technology partnership with Anthropic, which is scaling its Claude model on Microsoft Azure, powered by NVIDIA systems." | 高 | [^nvidia-q4fy26] |
| Q2 FY27单季股东回报 | ≈$26.0B | 止2026-07季度 | "NVIDIA returned approximately $26.0 billion to shareholders in the form of shares repurchased and cash dividends." | 高 | [^nvidia-q2fy27] |
| 回购授权扩容与FCF | 授权$235B；FY26 FCF $96.68B | 2026-10-05 | "Nvidia's $150B buyback lifts capacity to $235B, about 2.4x fiscal 2026 free cash flow of $96.68B." | 中 | [^tikr] |
| 净利质量风险（投资收益） | Q4其他收益$5,604M；非上市权益$22,251M | Q4/FY2026 | "Other income, net 5,604 … 9,022 … 1,034"；"Non-marketable equity securities 22,251 … 3,387" | 高 | [^nvidia-q4fy26] |

[^nvidia-q4fy26]: NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2026. 2026-02-25. http://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
[^nvidia-q3fy26]: NVIDIA Announces Financial Results for Third Quarter Fiscal 2026. 2025-11-19. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2026
[^earningsecho]: EarningsEcho. NVIDIA Corporation - Earnings Analyzer（Q2 FY2026摘要）. 访问于2026-10-31. https://earningsecho.io/company/NVDA
[^investors-h20]: Investor's Business Daily. Nvidia Stock: AI Chipmaker Reports Fiscal Q1 Results. 2025-05-28. https://www.investors.com/news/technology/nvidia-stock-nvda-fiscal-q1-2026-earnings
[^sec-10k-fy26]: NVIDIA Form 10-K FY2026 (nvda-20260125). 2026-02提交. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^q3fy26-10q]: NVIDIA Form 10-Q Q3 FY2026. 2025-11-19. https://s201.q4cdn.com/141608511/files/doc_financials/2026/q3/13e6981b-95ed-4aac-a602-ebc5865d0590.pdf
[^daloopa]: Daloopa. NVIDIA Customer Concentration: A Big 4 Earnings Preview. 2026-04-17. https://daloopa.com/blog/analyst-pov/nvidia-customer-concentration-a-big-4-earnings-preview
[^nvidia-q2fy27]: NVIDIA Announces Financial Results for Second Quarter Fiscal 2027. 2026-08-26. https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027
[^tikr]: TIKR. Nvidia Just Authorized a $235 Billion Buyback, Backed by Free Cash Flow. 2026-10-05. https://www.tikr.com/blog/nvidia-just-authorized-a-235-billion-buyback-backed-by-free-cash-flow-that-grew-from-27-02-billion
[^tsmc-ar]: TSMC 2025 Annual Report Website. 2026. https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^tsmc-4q25-transcript]: TSMC 4Q25 Earnings Call Transcript. 2026-01-15. https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[^sina-tsmc]: 新浪财经. 台积电：2025年第四季度净利润同比增35%. 2026-01-15. https://finance.sina.com.cn/jjxw/2026-01-15/doc-inhhkmpz4881608.shtml
[^skhynix-fy25]: SK hynix Newsroom. SK hynix Announces FY25 Financial Results. 2026-01-28. https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results
[^google-anthropic-tpu]: Google Cloud Press Corner. Anthropic to Expand Use of Google Cloud TPUs and Services. 2025-10-23. https://www.googlecloudpresscorner.com/2025-10-23-Anthropic-to-Expand-Use-of-Google-Cloud-TPUs-and-Services
[^anthropic-gbw]: Anthropic. Anthropic expands Google and Broadcom compute deal. 2026-04-06. https://www.anthropic.com/news/google-broadcom-partnership-compute
[^uncoveralpha-trainium]: Uncover Alpha. Amazon Trainium: Scaling AI Without Breaking the Bank. 2025-12-18. https://www.uncoveralpha.com/p/amazon-trainium-scaling-ai-without
[^alphastreet-cuda]: AlphaStreet. Nvidia's CUDA Lock-In and Supply Scarcity Make Its AI Chip Moat Harder to Break Than It Looks. 2026-03-27. https://news.alphastreet.com/nvidias-cuda-lock-in-and-supply-scarcity-make-its-ai-chip-moat-harder-to-break-than-it-looks
[^siliconanalysts]: Silicon Analysts. AI Accelerator Manufacturing Cost Estimates (2026)（页面标注Last updated: August 2026；数据源标注Epoch AI、Raymond James、TrendForce、SemiAnalysis）. https://siliconanalysts.com/data/ai-chip-costs
[^semianalysis-ramp]: SemiAnalysis. Nvidia's Ramp – Volume, ASP, Cloud Pricing, Margins. 2023-08-20. https://newsletter.semianalysis.com/p/nvidias-ramp-volume-asp-cloud-pricing （H100 ASP与云定价的历史基准线索，本轮未展开）
[^futurum-tsmc]: Futurum. TSMC Q3 FY 2026 Earnings Beat and Raise on AI and HPC Demand. 2026-10-20. https://futurumgroup.com/insights/tsmc-q3-fy-2026-earnings-beat-and-raise-on-ai-and-hpc-demand
[^intellectia-q1fy27]: Intellectia. Nvidia Stock Analysis Q1 2026: Record $81.6B Revenue. 2026-05-22. https://intellectia.ai/blog/nvidia-stock-analysis-q1-2026

### Tensions & Counter-arguments

1. **BOM口径毛利率(78-88%) vs 财报口径毛利率(73-75%)的落差**：成本拆分页给出H100的88%毛利是"卖价−物料成本"的估算，未含整板/整柜物料、测试、物流、渠道与NVIDIA自有研发销售费用；且估算本身"may vary +/-15-20%"[^siliconanalysts]。公司报表口径73-75%（Q4）才是可审计事实[^nvidia-q4fy26]。两者不矛盾，但引用时必须注明口径，不能混用。
2. **"印钞机"在加速而非见顶**：FY2026毛利率同比降3.9个百分点（71.1% vs 75.0%）容易被解读为"利润率见顶"，实际是Q1 H20计提的一次性拖累；Q3/Q4毛利率73.4%→75.0%逐季新高，FY27Q1指引74.9%[^nvidia-q3fy26][^nvidia-q4fy26]。
3. **净利率的"水分"质疑**：Q4 GAAP净利率≈63.1%（推算）中含其他收益净额$5,604M；FY2026非上市权益证券从$3,387M暴增至$22,251M——英伟达大举投资自身客户（Anthropic、CoreWeave等，官方新闻稿可见其投资公告），“供应商-客户-股东”循环交易会放大净利并引来质量质疑[^nvidia-q4fy26]。
4. **客户集中度的口径争议**：10-K口径为"直接客户"（direct customer），可能包含经销商/系统集成商而非终端云厂商；且Q1 FY2027"四大客户合计61%"来自daloopa对文件的解读，原文片段截断，需回SEC原文核对[^sec-10k-fy26][^daloopa]。反向观点：集中度高是供给稀缺期的自然结果（谁买得多谁占比高），并不自动等于议价权丧失。
5. **自研替代是"共存"而非"替换"**：Anthropic同时是谷歌TPU大客户（100万颗）[^google-anthropic-tpu]、AWS Trainium用户（50万颗+）[^uncoveralpha-trainium]和英伟达投资合作对象[^nvidia-q4fy26]；Meta官宣数百万颗Blackwell/Rubin[^nvidia-q4fy26]。自研芯片更多发生在推理与特定负载，训练侧英伟达仍有溢价（BOM口径毛利率78-88% vs AMD 65-66%）[^siliconanalysts]。但需警惕：本维度未取得谷歌TPU出货量、亚马逊Trainium出货量与AMD MI系列市占的硬数据，替代进度只能确认"方向"，不能量化"速度"。
6. **CUDA锁定数字的局限**："4M+注册开发者"为英伟达投资者材料的二手转引，注册数≠活跃开发者；PyTorch/JAX等框架抽象层与ROCm成熟度在削弱锁定，本轮未检索ROCm进展，无法评估削弱速度[^alphastreet-cuda]。
7. **台积电AI口径易被误读**："high-teens percent"是2025全年AI加速器收入占比，"mid-to-high-50s percent CAGR"是2026年增速指引，两者量纲不同；HPC平台占比（含非AI）与AI加速器占比也不是一个数[^tsmc-4q25-transcript][^futurum-tsmc]。
8. **FY2027Q1实际数未经一手核实**：intellectia称FY27Q1营收$81.6B、净利$58.3B（若真则净利率≈71%，显著高于指引隐含水平，可能含投资收益），与官方指引$78.0B方向一致但超出+4.6%，引用需谨慎[^intellectia-q1fy27][^nvidia-q4fy26]。

**待证项与下一步（按价值排序）**
- HBM市场份额硬数（SK海力士在HBM的份额2025年约5-6成、SK海力士称HBM占其DRAM收入比例）：本轮检索只命中DRAM整体份额（SK海力士32.6%，2025-11口径[^mk-dram]），HBM专项份额建议查TrendForce/Counterpoint季报与SK海力士IR口径。
- 台积电与SK海力士的股东回报与员工薪酬（补齐三口袋）：查台积电2025年报"Dividend Policy"节与薪酬报告、SK海力士事业报告书。
- ODM/服务器组装环节的分钱实证：查工业富联2025年报（收入、AI服务器毛利率）与广达/纬创法说会，把"门槛口径"从推算升级为实测。
- 四大客户合计61%的SEC原文（Q1 FY2027 10-Q客户集中度节）：回SEC EDGAR核对逐字原文。
- 英伟达FY2027Q1 10-Q（验证$81.6B/58.3B与SBC、投资收益结构）：SEC EDGAR。
- 谷歌TPU/亚马逊Trainium出货与性能对标硬数据：查Broadcom AI收入指引、The Information/SemiAnalysis对TPU v7 Ironwood与Trainium3的拆解。
