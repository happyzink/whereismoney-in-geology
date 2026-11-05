# E04 语义深挖 · Dimension 04（应用层：谁在赚钱谁在烧钱）

## Dimension 04: 应用层谁赚钱谁烧钱

> 检索时间：2026-10-31。口径说明：文中"年化收入/run-rate"指将最近单月×12 或最近季度×4 年化的口径，不等于会计年度确认收入；Anthropic 数据主要来自其泄露的 IPO 草稿（经 PitchBook/Morningstar 复核），OpenAI 为非上市公司，亏损口径以 The Information 等报道的现金消耗预测为主。事实与推断在行文中分别标注。

### Current State

**总判断（高置信）：** 2026 年应用层呈"头部模型公司收入爆发 + 巨额固定算力承诺"双轨：OpenAI 年化收入从 2025 年末约 $200 亿升至 2026 年 9 月约 $500 亿（二手估算）[^1][^2]；Anthropic 2026 年 7 月末 run-rate 超 $650 亿，但背有约 $5,180 亿（约 80% 不可撤销）的十年算力承诺[^5]。国内侧，DeepSeek 以极低训练成本口径与 2026 年连续降价两次冲击"堆算力"叙事，但年内已出现 Agent 高峰涨价的逆向信号[^6][^7][^8][^9][^10][^11]。已验证的付费场景集中于编程助手（Cursor $1B→$4B+）、广告（Meta AI 广告 run-rate >$600 亿）与客服（Salesforce Data Cloud+AI ARR $9 亿）[^12][^13][^14][^15]。

**① OpenAI 与 Anthropic：最新收入、亏损与融资（权威报道口径）**
- OpenAI 收入（口径：年化 run-rate）：2025 年末约 $20B[^1]；2026 年 2 月末超 $25B（The Information 引述知情人士）[^2]；2026 年 7 月单月收入超过 Q2 整季（BeInCrypto 转述标题）[^2]；Sacra 估算 2026 年 9 月年化约 $50B（二手估算，低-中置信）[^1]。
- OpenAI 亏损/烧钱（口径：现金消耗预测，The Information 报道经二手转引）：年烧钱 2026 年 $17B → 2027 年 $35B、峰值约 $47B（快照截断，峰值年份未显示）[^3]；2025-09 报道口径：管理层预计 2029 年前累计烧钱 $115B（二手通讯转引）[^4]。
- OpenAI 融资：2025-09 二手报道同文提及"incredible $500 billion valuation"[^4]；2025-03 软银领投 $40B、投后 $300B 一轮未能在本次检索中独立核验（待证）。
- Anthropic 收入（口径：泄露 IPO 草稿，PitchBook/Morningstar 2026-10-05 复核，高置信）：2025 年收入近 $4.6B（一年增长约 12 倍）[^5]；2026Q1 收入 $4.73B（超 2025 全年）、Q2 超 $11.50B（初步口径），7 月末 run-rate（最近单月×12）超 $65B[^5]。
- Anthropic 亏损：2025 年净亏损约 $42B，其中约 $34B 为可转债重估的非现金损失；剔除后经营亏损仍超 $8B；2025 年算力与基础设施支出 $7.33B（约为 2024 年三倍、占经营费用 58%、超过当年收入）[^5]。2026Q2 剔除股权激励（SBC）后经调整经营利润转正[^5]。
- Anthropic 融资/承诺：约 $518B、跨约十年的基础设施承诺，分布于六家伙伴——Broadcom 相关设备租赁 $161.2B、Google $111.1B、Amazon $110.0B、xAI 至多 $84.5B、Microsoft $31.4B、AMD 超 $20.0B；约 80% 不可撤销或与用量无关[^5]。已于 2026 年 6 月秘密递交 IPO 草稿，市场讨论估值约 $2T（≈7 月 run-rate 的 31 倍）[^5]；AMD 承诺购买至多 $50 亿 Anthropic 股票[^5]。
- 收入集中度（风险口径）：两位客户贡献 2025 年收入近 1/4（约 $1.1B）；Amazon+Google 渠道占 2025 年收入 47%（总额法确认）[^5]。
- 共享背景交叉（本批次已给定的共享事实，不重复求证）：算力卖方已确认赚钱（英伟达 FY2026 净利 $1,200.67 亿、+64.75%；寒武纪首次盈利 20.59 亿元）——与买方（模型公司）的巨额固定承诺形成对照。

**② 国内大模型价格战与 DeepSeek 低成本策略对算力叙事的冲击**
- DeepSeek V3 训练成本报道口径（事实，但仅限该口径）：V3 技术报告口径为约 278.8 万 H800 GPU 小时、按 $2/GPU 小时租价计约 $5.576M，仅覆盖正式预训练运行（论文口径，本次经二手报道确认其"$5M 级"主张；arXiv 原文未直接核读）[^6]；Bernstein 随即指出"2,048 块 H800 训练两个月、约 270 万 GPU 小时"只是预训练部分，真实总成本远高（不含研究、基础设施与人力）[^6]。
- 效率冲击算力叙事的标志事件（事实）：2025-01-27，NVIDIA 收跌 16.86%、单日市值蒸发 $589B，创美股历史最大单日市值损失[^7]。
- 国内价格战 2026 年时间线（事实，均带公告日）：
  - 2026-04-26：DeepSeek 全系 API 降价约 90%，"全系API输入缓存命中价格降至首发价的十分之一"，V4-Pro 叠加限时 2.5 折[^8]；
  - 2026-05-25：V4-Pro 宣布"永久降价为原定价的四分之一"，每百万 Token 输入（缓存命中）0.025 元、（缓存未命中）3 元、输出 6 元[^9]；
  - 2026-09-30：报道称价格战进入"每任务成本"时代，V4-Flash 输入缓存命中价格再降 50%（"DeepSeek 两天两次降价，百万Tokens 只要2分钱"）[^10]。
- 逆向信号（低置信，日期待证）：MIT TR 中国报道标题"DeepSeek涨价，OpenAI降价，Agent改写了大模型价格战"——V4-Pro 缓存未命中输入由 3 元/百万 Token 上调为高峰时段 9 元、空闲时段 4.5 元，输出由 6 元上调（公告日期未注明）[^11]。
- 对算力叙事的冲击（推断，基于上述证据）：训练端"低成本可复现"叙事 + 推理端价格战，两次压低"算力堆量=竞争力"的市场定价（前者对应 NVIDIA 单日 -$589B[^7]）；但 2026 年 Anthropic/OpenAI 的收入爆发与 $518B 级承诺表明算力需求侧并未收缩，叙事重心已从"训练堆量"转向"推理消耗 + 效率竞争 + 不可撤销锁定"[^5][^3]。

**③ 已验证跑通的 AI 付费场景（公司级收入数据）**
- 编程助手（验证最强）：Cursor 母公司 Anysphere ARR 轨迹：2025-11 约 $1B → 2026-02 约 $2B（Forbes 口径，多源一致）→ 2026 年 4 月末约 $3B → 2026 年 9 月初 >$4B（转引 Forbes，中置信）[^12][^13]。GitHub Copilot 的"$2B ARR"（2025 年初 BI 报道）本次未检索到一手来源，列为待证；仅获 2024-08 旧口径：Nadella 称 Copilot"accounted for over 40% of GitHub's revenue growth this year"[^17]。
- 广告生成/广告技术（内部化验证，非单独计费）：Meta 的 AI 广告基础设施（含 Advantage+）年化 run-rate 于 2025-10 超 $60B[^14]。（2025Q2 电话会"Advantage+ $20B run-rate"口径待证。）
- 客服/CRM Agent（增长快、绝对体量尚小）：Salesforce Data Cloud + AI ARR 于 FY2025 收官时达 $9 亿、同比 +120%，Agentforce 为主要驱动（公司口径）[^15][^16]；2026 财年更新数字待证。
- 付费验证强度排序（推断）：编程（直接订阅/席位费，收入可直接归因）＞ 广告（AI 提升广告主 ROI、收入内部化但规模最大）＞ 客服（ARR 增速高但绝对值小）。国内应用层可比公司级 AI 收入口径本次未检索到（未覆盖，见待证清单）。

### Key Evidence

| 数据点 | 数值 | 时间窗 | 原文摘录 | 自评信度 | 来源 |
|---|---|---|---|---|---|
| OpenAI 年化收入（2025 年末） | ≈$20B | 2025 年末 | "up from $20B at the end of 2025" | 中（估算方口径） | [^1] |
| OpenAI 年化收入（2026-02 末） | >$25B | 2026 年 2 月末 | "OpenAI's annualized revenue topped $25 billion at the end of February" | 中-高（转引 The Information） | [^2] |
| OpenAI 年化收入（2026-09） | ≈$50B | 2026 年 9 月 | "OpenAI hit $50B in annualized revenue in September 2026" | 低-中（二手估算） | [^1] |
| OpenAI 现金消耗预测 | 2026 年 $17B → 2027 年 $35B，峰值约 $47B | 2025-12 报道 | "annual cash burn is projected to rise from $17 billion in 2026 to $35 billion in 2027, peaking at $47…" | 中（快照截断，峰值年份未显示） | [^3] |
| OpenAI 累计烧钱与估值 | 2029 前累计 $115B；估值 $500B | 2025-09-09 | "Management now expects to burn through $115 billion in cash by 2029… an incredible $500 billion valuation" | 中低（二手通讯转引管理层口径） | [^4] |
| Anthropic 2025 年收入 | 近 $4.6B（约 12 倍增长） | 2025 财年 | "Revenue grew about 12-fold in 2025, from roughly $386 million to nearly $4.6 billion" | 高（泄露 IPO 草稿 + PitchBook 复核） | [^5] |
| Anthropic run-rate | >$65B | 2026 年 7 月末 | "By late July, the run rate, which annualizes the most recent month, passed $65 billion" | 高（同上） | [^5] |
| Anthropic 2025 年亏损 | 净亏≈$42B（含 $34B 非现金重估）；经营亏损>$8B | 2025 财年 | "The 2025 net loss of about $42 billion does not measure cash burn. Roughly $34 billion is a non-cash remeasurement" | 高（同上） | [^5] |
| Anthropic 2025 年算力支出 | $7.33B（占经营费用 58%） | 2025 财年 | "Anthropic spent $7.33 billion on compute and infrastructure in 2025, roughly triple the 2024 level and more than its revenue" | 高（同上） | [^5] |
| Anthropic 算力承诺 | ≈$518B/约十年，~80% 不可撤销 | 2026-10 披露 | "about $518 billion over roughly a decade, spread across six partners"；"About 80% of the total is noncancelable or payable regardless of usage" | 高（同上） | [^5] |
| Anthropic 收入集中度 | 两大客户≈1/4（~$1.1B）；Amazon+Google 渠道占 47% | 2025 财年 | "Two customers accounted for nearly a quarter of 2025 revenue, roughly $1.1 billion" | 高（同上） | [^5] |
| Anthropic IPO 进展 | 2026-06 秘密递交草稿；拟议估值≈$2T | 2026 年 6 月/10 月 | "Anthropic confidentially filed its draft IPO prospectus in June"；"At a $2 trillion valuation, investors would pay just under 31 times the July run rate" | 高（同上） | [^5] |
| DeepSeek V3 训练成本口径 | ≈$5.576M（2.788M H800 GPU 小时 @$2，仅预训练） | 2024-12 论文口径 | "used 2,048 NVIDIA H800 GPUs over a two-month period, consuming approximately 2.7 million GPU hours for pre-…" | 高（数字为论文/报道口径）；实际总成本争议=中 | [^6] |
| NVIDIA 单日市值损失 | -16.86%，$589B | 2025-01-27 | "Nvidia sheds $589 billion in market cap on DeepSeek concerns, most in history… closed down 16.86%" | 高 | [^7] |
| DeepSeek 全系降价 | ≈90%；缓存命中输入降至首发价 1/10 | 2026-04-26 公告 | "直降90%，创大模型价格新低！4月26日，DeepSeek官方发布API价格调整公告，全系API输入缓存命中价格降至首发价的十分之一" | 中-高（年份由 V4-Pro 表述推定） | [^8] |
| V4-Pro 永久降价 | 降至原价 1/4；命中输入 0.025 元/M、未命中 3 元/M、输出 6 元/M | 2026-05-25 | "调整价格后，DeepSeek-V4-Pro每百万Token输入（缓存命中）将花费0.025元，输入（缓存未命中）的价格为3元，输出6元" | 中-高 | [^9] |
| 价格战进入"每任务成本"时代 | V4-Flash 缓存命中输入再降 50% | 2026-09-30 | "API 降价50%：大模型价格战打到『每任务成本』时代"；"DeepSeek 两天两次降价，百万Tokens 只要2分钱" | 中（个人博客转述） | [^10] |
| V4-Pro 高峰溢价（逆向信号） | 未命中输入 3 元→高峰 9 元/M、空闲 4.5 元/M | 2026 年内（日期未注明） | "以V4 Pro 为例，每百万Token 的缓存未命中输入价格由3元调整为高峰时段9元、空闲时段4.5元" | 低（日期未核验） | [^11] |
| Cursor（Anysphere）ARR | $1B（2025-11）→$2B（2026-02）→$3B（2026-04 末）→>$4B（2026-09 前后） | 2025-11 至 2026-09 | "Cursor reached $2 billion in annualized recurring revenue, up from $1B ARR reported in late November 2025"；"Forbes reported that Cursor reached roughly $2 billion…in February 2026, $3 billion in late April, and more than $4…" | 中（$2B 多源一致；$3B/$4B 转引 Forbes） | [^12][^13] |
| Meta AI 广告 run-rate | >$60B | 2025-10-30 报道 | "The annual revenue run rate for Meta's AI ad infrastructure, including Advantage+, is now over $60 billion" | 中-高（转述财报电话会） | [^14] |
| Salesforce Data Cloud+AI ARR | $900M，+120% YoY | FY2025 收官（2025-02/04 披露） | "closing the year with $900 million in Data Cloud and AI annual recurring revenue"；"hit $900 million in Data Cloud and AI ARR, up 120 percent year-over-year" | 高（公司口径） | [^15][^16] |
| GitHub Copilot（旧口径） | "占 GitHub 当年收入增长 40%+" | 2024-08-13 | "accounted for over 40% of GitHub's revenue growth this year" | 低（旧、相对口径）；"$2B ARR"待证 | [^17] |

### Tensions & Counter-arguments

1. **Run-rate ≠ 确认收入（口径风险，高置信）**：Anthropic 的 run-rate 定义为"最近单月×12"，且"many large customers are not on long-term contracts, leaving them free to cut or shift their spending"——两位客户占 2025 年收入近 1/4，收入可在单季内回落而承诺支付不变[^5]。OpenAI 的 $50B 为估算方口径[^1]，与公司未审计数据不可直接混比。
2. **循环交易/供应链金融化（对"收入爆发"的对冲解释）**：Anthropic $518B 承诺中 Google/Amazon/AMD 合计约 $241B、三者均为（或已同意成为）股东，AMD 更承诺购买至多 $5B Anthropic 股票；PitchBook 提醒 IPO 投资者应结合这些条款阅读协议，并明确指出估值成立与否取决于"sustained free cash flow"尚未建立[^5]。即"收入爆发"部分由供应商入股与不可撤销承诺的结构放大。
3. **DeepSeek 成本口径不可外推（事实边界）**：$5.576M 仅是 V3 正式预训练运行的 GPU 租赁成本，Bernstein 指出未含研究、消融、基础设施与人力[^6]；"训练成本趋零"不等于"算力需求趋零"。2025-01-27 NVIDIA 单日 -$589B[^7] 是叙事冲击的直接证据，但 2026 年两家头部公司的收入与承诺数据[^5][^1]构成反例——本次未检索到"Jevons 悖论"表述的一手来源，列为待证。
4. **价格战正在变形，而非单向延续（中置信，部分待证）**：2026 年国内先"全系降价 90%"[^8]、再"永久降价 1/4"[^9]、9 月继续下探[^10]；但同期出现 Agent 场景高峰溢价的逆向信号（V4-Pro 高峰输入 9 元/M）[^11]，报道标题即"Agent 改写了大模型价格战"。若属实，价格战正让位于"按任务/时段价值定价"，对"模型层毛利必然归零"的推断构成反例。
5. **"谁赚钱谁烧钱"的再定义（推断）**：Anthropic 2026Q2 剔除 SBC 后经调整经营利润已转正[^5]，而 OpenAI 预计 2027 年仍烧 $35B[^3]——模型层内部已分化；烧钱大头正从研发转向不可撤销的算力承诺（Anthropic 约 80% 不可撤销[^5]），这实质是对算力叙事的隐性支撑而非冲击。结合共享背景（英伟达 FY2026 净利 $1,200.67 亿、寒武纪首次盈利 20.59 亿元），2026 年的主结构仍是"卖铲人确认利润、买铲人承诺现金"。

**待证与跟进（本次未定位，附建议查法）：**
- GitHub Copilot "$2B ARR"（2025 年初 Business Insider 报道）→ 查 BI 原文或微软 FY25Q2 财报电话会记录。
- OpenAI 2025-03 软银 $40B@$300B 与 2025-10 重组后 $500B 估值轮的一手报道 → 查 Reuters/CNBC 当日报道（本次仅获二手转引[^4]）。
- OpenAI 2026 年内是否完成新一轮融资/员工股转让 → 本次未检索到，查 The Information/Bloomberg 近月报道。
- Salesforce Data Cloud+AI ARR 2026 财年更新（市场流传 Q2 FY2026 达 $1.2B）→ 查 Salesforce 季度新闻稿。
- Meta 2025Q2 "Advantage+ $20B run-rate" 电话会原文 → 查 Meta Q2 2025 earnings call transcript。
- DeepSeek V4-Pro 涨价公告的官方日期与定价页 → 查 api-docs.deepseek.com 价格公告。
- 2024-05 DeepSeek V2（输入 ¥1/百万 tokens）引发国内价格战、阿里/字节跟进降价的报道 → 查 2024 年 5 月中文财经媒体。
- 国内应用层（办公/营销/客服 SaaS）公司级 AI 收入口径 → 本维度未覆盖，建议单开子任务。

[^1]: Sacra. OpenAI revenue, valuation & funding（公司研究页）. 估算基准 2026-09，访问于 2026-10-31. https://sacra.com/c/openai
[^2]: BeInCrypto. OpenAI Says July Annualized Revenue Topped All of Q2. 2026-07-30. https://beincrypto.com/openai-revenue-big-tech-earnings-week （转引 The Information）
[^3]: Wiss. OpenAI Valuation: What Tech Founders Need to Know. 2025-12-10. https://wiss.com/openai-valuation （转引 The Information；原页访问被拦截（HTTP 503），摘录取自检索快照）
[^4]: Brownstone Research. OpenAI's $115 Billion Cash Burn Is Just the Beginning. 2025-09-09. https://www.brownstoneresearch.com/bleeding-edge/openais-115-billion-cash-burn-is-just-the-beginning （二手通讯，转引管理层口径）
[^5]: Morningstar（原载 PitchBook）. PitchBook: Anthropic's Leaked Financials Reflect Fast Growth, Not $2 Trillion Valuation. 2026-10-05. https://global.morningstar.com/en-gb/markets/pitchbook-anthropics-leaked-financials-reflect-fast-growth-not-2-trillion-valuation （已全文核读；数据来自对泄露 IPO 草稿的报道）
[^6]: Business Standard. Deepseek – Bernstein challenges AI firms' claim $5 million development cost. 2025-01-29. https://www.business-standard.com/technology/tech-news/deepseek-bernstein-challenges-ai-firms-claim-5-million-development-cost-125012900936_1.html （DeepSeek-V3 技术报告口径另见 arXiv:2412.19437，本次未直接核读论文原文）
[^7]: Investing.com. Is DeepSeek Doomsday for AI Infra? Bernstein Weighs In（内文：Nvidia sheds $589 billion in market cap on DeepSeek concerns, most in history）. 2025-01-27. https://ng.investing.com/news/stock-market-news/is-deepseek-doomsday-for-ai-infra-bernstein-weighs-in-1728021
[^8]: 第一财经. 一财主播说丨DeepSeek全系API降价创大模型价格新低. 2026-04（公告日 2026-04-26，年份由 V4-Pro 表述推定）. https://www.yicai.com/video/103154214.html
[^9]: 财新. DeepSeek-V4-Pro宣布API价格永久降价为原定价的四分之一. 2026-05-25. https://m.caixin.com/m/2026-05-25/102447362.html
[^10]: 51CTO 博客. API 降价50%：大模型价格战打到"每任务成本"时代. 2026-09-30. https://blog.51cto.com/itcjf/14974313 （个人博客，二手转述）
[^11]: MIT Technology Review 中国. DeepSeek涨价，OpenAI降价，Agent改写了大模型价格战. 发布日期未注明（待证）. https://www.mittrchina.com/news/detail/16804
[^12]: Digital Applied. Cursor AI Hits $2B Revenue: Market Dominance. 2026-03-02. https://www.digitalapplied.com/blog/cursor-ai-2b-revenue-enterprise-coding-market-leader
[^13]: okara.ai. Cursor Revenue and ARR: How Cursor Grew to $4B So Fast（转引 Forbes）. 2026-09-11. https://okara.ai/blog/how-cursor-grew
[^14]: Marketing Dive. Meta's AI bets supercharge marketing efficiency — and costs. 2025-10-30. https://www.marketingdive.com/news/meta-ai-bets-supercharge-marketing-efficiency-costs/804238
[^15]: Salesforce Newsroom. Salesforce shares Data Cloud growth and momentum. 2025-04-16. https://www.salesforce.com/news/stories/data-cloud-growth （公司口径）
[^16]: CX Today. Salesforce Champions Unheralded Product Growth, in the Quarter of Agentforce. 2025-02-27. https://cxtoday.com/salesforce-champions-unheralded-product-growth-in-the-quarter-of-agentforce
[^17]: IT Brew. Microsoft earnings show role of Copilot tool in revenue. 2024-08-13. https://www.itbrew.com/stories/2024/08/13/github-copilot-stumbles-as-microsoft-earnings-report-remains-favorable
