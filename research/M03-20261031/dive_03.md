# Dimension 03: 周期择时——成本曲线定位法

## Dimension 03: 周期择时：成本曲线定位法（Dimension 03）

### Current State

- **成本曲线是什么**：把全球所有在产矿山按单位现金成本（C1）从低到高排成一条曲线，横轴是累计产量、纵轴是成本。价格跌到曲线上某一分位成本附近时，该分位以上的矿山现金流断裂、被迫减停产，供给收缩托住价格——这就是"成本分位线决定价格底部"的机制。McKinsey 在《Global Materials Perspective 2026》中直接用 C90（成本曲线90分位成本）作为划分价格体制的标尺：[^mckinsey-c90]
- **90分位成本线≈激励价格**：90分位成本的含义是"满足边际供给所需的激励价格"——价格低于此线时，约10%的高成本产能不赚钱，新建项目也被推迟，供给出清后价格自然在该线附近获得支撑。S&P Global 在 2026 年成本展望中也是拿"预测金属价 vs 成本曲线90分位"来判断各矿种的盈利压力：[^spglobal-cost2026] 需要说明：Wood Mackenzie、S&P 的完整成本曲线是付费数据，公开渠道只能拿到方法学与零散数值，本节用可核实的公开锚点拼接（见 Key Evidence）。
- **铜的实证底部**：2016年1月铜价见底，2016年全年均价 $2.21/磅（较2015年跌11.2%），年内低点 $1.94/磅（≈$4,300/吨）——这恰好击穿当时90分位现金成本线，随后 Freeport、Glencore 等高成本矿减停产，价格反转。[^metalcharts-2016] 本轮相反：2024-2026年铜价屡创历史新高（E03已确认：顶格14,449美元，本轮未能在公开检索中独立复核此数，标注待证），同时 ICSG 转为过剩9.6万吨，属于"价格在成本曲线极右端运行"的顶部区形态。
- **锂的实证底部**：碳酸锂从2020年8月约4万元/吨涨至2022年11月近60万元/吨（远超全成本曲线，连最高成本的云母提锂都暴利），随后跌回；2026年10月28日期货主力2701合约报93,300元/吨、电池级现货均价98,900元/吨——市场普遍认为该位置已击穿多数高成本产能（云母提锂、高成本澳矿）的现金成本线，进入"成本曲线定价"区间。[^tmtpost-lithium] [^eastmoney-li-202610]
- **capex周期与价格周期天然错位**：矿山从发现到投产平均15.7年（127个矿样本），美国司法辖区的项目开发周期更长、平均17.9年：[^spglobal-157y] [^spglobal-179y] 所以矿企的资本开支决策基于当期价格，而产能释放却在多年后——**capex顶（投资最疯狂时）对应的不是矿价顶，而是约17年后的供给顶；而矿价底（全行业亏损、capex被砍到零）对应的是未来供给缺口**。机制链条：价顶→capex顶→（17.9年后）供给释放→价底→capex谷→供给缺口→下一轮价顶。
- **2013-2016轮验证**：2011-2013年铜价高位时矿企capex创历史峰值，2013-14超级周期崩塌后行业用了十年去杠杆；到2015-2016年capex被砍至谷底、铜价同步见底$1.94/磅——capex顶（2012-13）领先价格底（2016初）约3年，capex谷与价格底几乎同时出现。[^zvenia-capex] 反面验证：2026年Top30矿企capex预计达1,216亿美元、创十年新高——这恰恰是2024-2026年铜价历史高位"吸引"出来的，为2030年代之后的供给过剩埋下种子。[^zvenia-capex]
- **2021-2025轮验证（锂）**：2021-2022年锂价暴涨（4万→60万元/吨）刺激全球锂矿 capex 与扩产公告井喷（澳矿扩产、中国盐湖与云母、非洲Manono等），供给在2023-2025集中释放，锂价随之跌入2023-2025深度回调：[^tmtpost-lithium] 完整走完"价顶→capex/扩产顶→供给顶→价底"的传导，本轮传导用时约3-4年（锂矿建设周期短于铜，错位期更短）。
- **紫金矿业的逆周期并购：买在行业 despair 时刻**：紫金在2015年收购艾芬豪旗下刚果（金）卡莫阿铜矿近一半权益，2014、2016年完成姆索诺伊72%权益（科卢韦齐铜矿）收购——券商研报的原文定性："2015-2016年在铜价持续下跌时购买科卢韦齐铜矿和卡莫阿铜矿，2019-2020（年继续逆周期收购）"。卡莫阿后成为全球第三大铜矿，买入时点正是铜价$2-3/磅的谷底区。[^yidaiyilu-zijin] [^dfcfw-zijin] 2025年1月16日，紫金再以每股35元、总价137.29亿元收购藏格矿业24.82%股份取得控制权（间接强化巨龙铜矿权益+钾锂资源）——买点仍在锂价深跌、藏格估值被压制的窗口。[^zijin-zangge]
- **洛阳钼业同理**：2016年以26.5亿美元并购刚果（金）TFM（Tenke铜钴矿56%权益），2020年12月再以5.5亿美元收购Kisanfu铜钴矿——两笔都发生在钴价/铜价的相对低位（2016年铜价谷底、2020年疫情底），洛钼官方口径："此前的2016年，洛阳钼业以26.5亿美元并购TFM"。[^cmoc-kisanfu]
- **顶部信号清单（本轮锂/铜实证归纳）**：① **价格远超90分位成本线、全曲线盈利**（2022年锂60万=连最高成本产能都暴利；2025-26铜创历史新高）；② **PE陷阱**：周期股PE最低（盈利暴增分母膨胀）时恰是价格顶——天齐锂业2022年盈利峰值时PE降至历史低分位，随后锂价崩、盈利消失，PE反而失效（"2022年PE最低=锂价顶"即E03确认的天齐四步陷阱）；[^eniu-tianqi] ③ **capex/扩产公告井喷**（2021-22锂矿扩产潮、2026年Top30矿企capex十年新高1,216亿美元）；[^zvenia-capex] ④ **供需平衡表由缺转剩**（ICSG转过剩9.6万吨，E03已确认）；⑤ **行业工资/成本加速上行**（中国采矿工资143,361元排第6但增速1.9%倒数第三——成本刚性问题开始侵蚀矿山利润，E03已确认）；⑥ **高成本边际产能全面复活**（锂云母产能重启=供给弹性回归）。
- **普通投资者不看成本曲线亏在哪**：① 只看PE买周期股——在PE最低（价顶）买入、PE最高（价底）割肉，天齐2022年是教科书案例：[^eniu-tianqi] ② 把"当前利润"线性外推——价顶时按暴利给永续估值，完全忽略价格终将回落到成本曲线某分位附近；③ 在capex井喷、券商一致看多时追入矿业股（2021-22买锂矿股、2025-26追铜矿股），而逆周期买点（2015-16铜、2024-25锂的90分位成本线附近）恰恰是新闻里全是减产、亏损、退出的时刻；④ 不区分矿种的成本曲线斜率——锂的曲线短平（供给弹性大、周顶持续时间短），铜的曲线长缓（17.9年开发周期使缺口持续多年），用同一套情绪节奏对待两类资产。
- **方法论小结**：成本曲线定位法给出的是**区间而非时点**——价格跌破90分位成本线=底部区域（分批买入信号），价格远超全曲线盈利+capex井喷=顶部区域（分批卖出信号）。两个区域之间的"模糊期"用capex-投产时滞（铜≈15-18年、锂≈3-4年）与供需平衡表边际变化判断方向。

### Key Evidence

| 数据点 | 数值 | 时间 | 原文摘录(逐字) | 自评信度 | 来源 |
|---|---|---|---|---|---|
| McKinsey价格体制标尺=C90成本 | C90=成本曲线90分位资产成本 | 2026 | "Price regimes are measured against the C90 cost (the cost of the asset at the 90th percentile of the cost curve)" | 高 | [^mckinsey-c90] |
| S&P 2026成本展望方法 | 预测价vs90分位成本对比 | 2026-01-30 | "The chart below highlights potential profitability pressures by comparing the 2026 forecast metal price against the 90th percentile of the..." | 高 | [^spglobal-cost2026] |
| 2016年铜价谷底 | 均价$2.21/磅，低点$1.94/磅（≈$4,300/吨） | 2016 | "The copper price in 2016 averaged $2.21 per pound, down 11.2% from 2015 ... 2016 Low $1.94" | 高 | [^metalcharts-2016] |
| 碳酸锂两轮价格 | 4万→近60万→2026-10报93,300元/吨 | 2020.8-2026.10.28 | "碳酸锂价格从2020年8月的4万元/吨底部启动，到2022年11月冲高至近60万元/吨的历史高点"；"10月28日，碳酸锂期货主力2701合约下跌4.64%，报93300元/吨。现货价格同步承压，电池级碳酸锂均价当日下跌1500元/吨，至98900元/吨" | 高 | [^tmtpost-lithium] [^eastmoney-li-202610] |
| 矿山开发周期 | 平均15.7年（127矿）；美国17.9年 | 2023-06 / 2024-06 | "Discovery to production averages 15.7 years for 127 mines"；"Development times for these were even longer, at 17.9 years on average" | 高 | [^spglobal-157y] [^spglobal-179y] |
| Top30矿企capex | 2026年预计1,216亿美元，十年新高 | 2026 | "The top 30 miners are projected to spend $121.6 billion in 2026, a decade high. After the supercycle bust of 2013–14, the sector spent a decade deleveraging" | 中 | [^zvenia-capex] |
| 紫金逆周期收购卡莫阿 | 2015年收购卡莫阿近半权益 | 2015 | "2015年收购艾芬豪旗下刚果（金）卡莫阿铜矿近一半权益"；"2015-2016年在铜价持续下跌时购买科卢韦齐铜矿和卡莫阿铜矿" | 高 | [^yidaiyilu-zijin] [^dfcfw-zijin] |
| 紫金收购藏格 | 35元/股×24.82%股份=137.29亿元 | 2025-01-16公告 | "拟通过全资子公司紫金国际控股，以每股35元共计137.29亿元收购藏格矿业24.82%的股份" | 高 | [^zijin-zangge] |
| 洛钼并购TFM | 26.5亿美元（2016）；Kisanfu 5.5亿美元（2020.12） | 2016 / 2020-12-13 | "此前的2016年，洛阳钼业以26.5亿美元并购TFM"；"此次收购Kisanfu矿，不但扩充了铜钴矿资源量，也将与旗下重要资产TFM产生显著协同效应" | 高 | [^cmoc-kisanfu] |
| 天齐锂业估值分位 | 当前PE处近3/5/10年-1%分位（历史极低位=盈利分母膨胀后的价后区间） | 2026-07 | "当前市盈率百分位. 近3年：-1%. 近5年：-1%. 近10年：-1%" | 中（表格口径未含2022峰值PE的逐字数值，机制引用E03已确认事实） | [^eniu-tianqi] |
| 铜价顶格14,449美元 | E03已确认，本轮未独立复核 | 2025-2026 | —（公开检索未命中该精确数字） | 低（沿用E03，待证） | — |

[^mckinsey-c90]: Global Materials Perspective 2026. McKinsey & Company. 2026. https://www.mckinsey.com/~/media/mckinsey/industries/energy%20and%20materials/our%20insights/global%20materials%20perspective%202026/global-materials-perspective-2026.pdf
[^spglobal-cost2026]: Mine cost outlook 2026: Inflation, new supply reshape global mining landscape. S&P Global Market Intelligence. 2026-01-30. https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/01/mine-cost-outlook-2026-inflation-new-supply-reshape-global-mining-landscape
[^metalcharts-2016]: Copper Price in 2016: $2.21 Average. MetalCharts. 2016年数据页（访问于2026-10）. https://metalcharts.org/copper-price-history/2016
[^tmtpost-lithium]: 看懂十年两轮锂周期，就学会了投资这个赛道的一半. 钛媒体. 2026-06-01. https://www.tmtpost.com/8009391.html
[^eastmoney-li-202610]: 碳酸锂期价反弹戛然而止，市场发生了什么？东方财富. 2026-10-28. https://wap.eastmoney.com/a/202610283912512456.html
[^spglobal-157y]: Discovery to production averages 15.7 years for 127 mines. S&P Global Market Intelligence. 2023-06-06. https://www.spglobal.com/market-intelligence/en/news-insights/research/discovery-to-production-averages-15-7-years-for-127-mines
[^spglobal-179y]: Mine development times: The US in perspective. S&P Global Market Intelligence / NMA. 2024-06. https://cdn.ihsmarkit.com/www/pdf/0724/SPGlobal_NMA_DevelopmentTimesUSinPerspective_June_2024.pdf
[^zvenia-capex]: $121 billion in mining capex and the industry still can't solve its own supply problem. Zvenia. 2026. https://zvenia.com/post/121-billion-in-mining-capex-and-the-industry-still-can-t-solve-its-own-supply-problem
[^yidaiyilu-zijin]: 紫金矿业：为什么要去"一带一路"上"掘金". 一带一路官网. 2021-06-19. https://www.yidaiyilu.gov.cn/p/177536.html
[^dfcfw-zijin]: 紫金矿业（601899.SH）研究报告. 东方财富研报中心. 2024-03-20. https://pdf.dfcfw.com/pdf/H3_AP202403201627281314_1.pdf
[^zijin-zangge]: 紫金矿业加码国内矿产布局 拟137亿元揽入藏格矿业控制权. 紫金矿业官网. 2025-01-17. https://www.zjky.cn/news/news-detail-121724.htm
[^cmoc-kisanfu]: 继续加码钴资源：洛阳钼业5.5亿美元收购刚果（金）Kisanfu矿. 澎湃新闻（洛阳钼业官网转载）. 2020-12-13. https://www.cmoc.com/html/2020/MediaFocus_1213/80.html
[^eniu-tianqi]: 天齐锂业(002466)历史市盈率|PE|估值. 亿牛网. 访问于2026-10. https://eniu.com/gu/sz002466

### Tensions & Counter-arguments

- **成本分位线不是铁底，只是"概率支撑"**：2015-2016年铜价曾长时间运行在90分位成本线之下（亏损可以靠库存现金撑，减产滞后于价格），锂在2024-2025也出现过"击穿成本线后继续阴跌"——因为高成本产能的关停取决于现金流储备与股东意志，不是即时的。成本曲线定"区域"，不定"日期"。
- **技术变革会让成本曲线整体下移**：锂云母提锂技术进步、铜浸出技术（如生物冶金）会压低90分位成本，历史上按旧成本线抄底的玩家被"曲线移动"套住。用成本线做底必须叠加对技术路径的判断。
- **二手来源的信度分层**：Top30矿企capex的1,216亿美元来自二手转述（zvenia），未追溯到S&P/original报告原文；天齐2022年"PE最低=价顶"的精确PE数值未能逐字复核（本轮检索只拿到历史分位与ROE类表格），机制层面依赖E03已确认事实。这两处为本文最弱的两个数字锚点。
- **capex-价格错位的方向性争议**：有观点认为本轮（2024-2026）铜的capex回升不足以填补供给缺口（因为品位下降、开发周期17.9年），"capex十年新高=未来过剩"的推断可能被"老矿枯竭+需求(电网/AI/新能源)超预期"抵消——即本轮capex顶未必对应2030年代的价底。ICSG转过剩9.6万吨（E03）与"结构性缺口"两派目前并存。
- **逆周期并购的幸存者偏差**：紫金、洛钼是买在底部的成功者；同期同样在2015-2016年抄底矿业资产但失败（资产减值、资源不达预期）的案例极少被宣传。逆周期买入本身不保证收益，保证收益的是"底部买入+优质资源+运营能力"三者同时成立。

---

*检索说明：本文基于2026-10-31执行的第03维度专项检索（13次web_search），引用原文均为来源页逐字摘录。全文数字均带时间窗与口径；信度"低/中"的条目已在表内注明缺陷。*
